"""
Full-Stack Engineering Workspace Orchestrator.
Coordinates the Code Engine, Telemetry Client, and Interactive Dashboard.
"""

import os
import sys
import time
import signal
import atexit
import threading
from pathlib import Path

from config import Config, parse_cli_args
from heartbeat_client import HeartbeatClient
from code_engine import CodeEngine
from dashboard import Dashboard
from git_sync import sync_progress_to_github


class SimulatorApp:
    def __init__(self, config: Config):
        self.config = config
        self.is_running = True

        # Initialize Dashboard
        self.dashboard = Dashboard(
            project_name=self.config.project_name,
            target_dir=self.config.target_dir,
            speed_mode=self.config.speed,
            enable_heartbeat=self.config.enable_heartbeat,
            headless=self.config.headless,
        )

        # Initialize Heartbeat Client
        self.heartbeat_client = HeartbeatClient(
            api_key=self.config.api_key,
            api_url=self.config.api_url,
            project_name=self.config.project_name,
            rate_limit_seconds=self.config.rate_limit_seconds,
            dynamic_project_name=self.config.dynamic_project_name,
        )

        # Initialize Code Engine with event hook
        self.code_engine = CodeEngine(
            target_dir=self.config.target_dir,
            speed_profile=self.config.current_speed_profile,
            event_callback=self.on_code_event,
        )

        self.last_event = {
            "action": "STARTUP",
            "file_path": "",
            "relative_path": "",
            "line_no": 1,
            "details": "Initializing simulator...",
        }

        # Git synchronization tracking
        self.last_git_sync_time = time.time()
        self.git_sync_lock = threading.Lock()
        self.is_syncing_git = False

        # Setup exit handlers
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)
        self._write_pid_file()
        atexit.register(self._cleanup_pid_file)

    def _write_pid_file(self):
        pid_file = Path(__file__).parent / ".simulator.pid"
        try:
            with open(pid_file, "w") as f:
                f.write(str(os.getpid()))
        except Exception:
            pass

    def _cleanup_pid_file(self):
        pid_file = Path(__file__).parent / ".simulator.pid"
        if pid_file.exists():
            try:
                pid_file.unlink()
            except Exception:
                pass

    def _handle_signal(self, signum, frame):
        self.stop_and_save()
        sys.exit(0)

    def stop_and_save(self):
        self.is_running = False
        self.code_engine.stop()

        if self.config.git_sync_on_pause:
            with self.git_sync_lock:
                try:
                    sync_progress_to_github(
                        target_dir=self.config.target_dir,
                        repo_dir=str(Path(__file__).parent.resolve()),
                        remote_url=self.config.git_remote_url,
                    )
                except Exception as e:
                    print(f"[Git Sync] Notice: {e}", file=sys.stderr)

        if not self.config.headless:
            print("\n[Workspace] Session paused. Updates saved to GitHub!")

    def check_periodic_git_sync(self):
        """Checks if the 5-minute auto-save interval has elapsed."""
        if not self.config.git_sync_on_pause:
            return

        interval = getattr(self.config, "git_sync_interval_seconds", 300)
        if interval <= 0:
            return

        now = time.time()
        if (now - self.last_git_sync_time) >= interval and not self.is_syncing_git:
            self.last_git_sync_time = now
            threading.Thread(target=self._async_periodic_sync, daemon=True).start()

    def _async_periodic_sync(self):
        """Non-blocking background worker that pushes progress snapshots to GitHub."""
        with self.git_sync_lock:
            self.is_syncing_git = True
            try:
                self.dashboard.add_log("GIT_SYNC", "Syncing workspace updates to GitHub...")
                success, msg = sync_progress_to_github(
                    target_dir=self.config.target_dir,
                    repo_dir=str(Path(__file__).parent.resolve()),
                    remote_url=self.config.git_remote_url,
                )
                if success and "No changes" not in msg:
                    self.dashboard.add_log("GIT_SYNC", f"Pushed updates to GitHub ({time.strftime('%H:%M:%S')})")
            except Exception as e:
                self.dashboard.add_log("GIT_SYNC", f"Notice: {str(e)[:40]}")
            finally:
                self.is_syncing_git = False

    def on_code_event(self, event: dict):
        """Called whenever code_engine types, modifies, or saves a file."""
        self.last_event = event

        # Send heartbeat to Hackatime if enabled
        if self.config.enable_heartbeat:
            sent = self.heartbeat_client.send_heartbeat(event)
            if sent:
                self.dashboard.add_log(
                    "HEARTBEAT",
                    f"Synced heartbeat ({event.get('line_no')} lines)",
                    event.get("relative_path", "")
                )

        # Add event to dashboard log
        action = event.get("action", "TYPING")
        if action != "HEARTBEAT":
            self.dashboard.add_log(
                action,
                event.get("details", ""),
                event.get("relative_path", "")
            )

        # Render dashboard update
        self._refresh_dashboard()

    def _refresh_dashboard(self):
        heartbeat_stats = {
            "total_sent": self.heartbeat_client.total_sent,
            "successful": self.heartbeat_client.successful,
            "failed": self.heartbeat_client.failed,
            "last_status": self.heartbeat_client.last_status,
            "last_error": self.heartbeat_client.last_error,
        }

        interval = getattr(self.config, "git_sync_interval_seconds", 300)
        elapsed = time.time() - self.last_git_sync_time
        remaining = max(0, int(interval - elapsed)) if interval > 0 else None

        self.dashboard.render(
            current_file=self.last_event.get("relative_path", ""),
            current_line=self.last_event.get("line_no", 1),
            total_lines=self.code_engine.total_lines_written,
            total_edits=self.code_engine.total_edits,
            heartbeat_stats=heartbeat_stats,
            current_action=self.last_event.get("action", "TYPING"),
            active_project=self.last_event.get("project_name") or self.code_engine.current_project["name"],
            git_sync_remaining=remaining,
        )

    def run(self):
        """Main execution loop."""
        self.dashboard.add_log("CREATE_FILE", "Initializing multi-project workspace...")
        self.code_engine.initialize_workspace()
        self.code_engine.ensure_current_project_seeded()

        # Infinite simulation cycle
        while self.is_running:
            try:
                self.code_engine.perform_random_action()
                self.check_periodic_git_sync()
                self._refresh_dashboard()
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.dashboard.add_log("THINKING", f"Handled exception: {str(e)[:40]}")
                time.sleep(2)

        self.stop_and_save()


def main():
    cli_args = parse_cli_args()
    config = Config(cli_args)
    app = SimulatorApp(config)
    app.run()


if __name__ == "__main__":
    main()
