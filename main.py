"""
Main Orchestrator for Hackatime & VS Code Activity Simulator.
Coordinates the Code Engine, Telemetry Heartbeat Client, and Interactive Dashboard.
"""

import os
import sys
import time
import signal
import atexit
from pathlib import Path

from config import Config, parse_cli_args
from heartbeat_client import HeartbeatClient
from code_engine import CodeEngine
from dashboard import Dashboard


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
        self.is_running = False
        self.code_engine.stop()
        if not self.config.headless:
            print("\n\n[Simulator] Safely shutting down simulation session. Progress saved!")
        sys.exit(0)

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
        self.dashboard.render(
            current_file=self.last_event.get("relative_path", ""),
            current_line=self.last_event.get("line_no", 1),
            total_lines=self.code_engine.total_lines_written,
            total_edits=self.code_engine.total_edits,
            heartbeat_stats=heartbeat_stats,
            current_action=self.last_event.get("action", "TYPING"),
            active_project=self.last_event.get("project_name") or self.code_engine.current_project["name"],
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
                self._refresh_dashboard()
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.dashboard.add_log("THINKING", f"Handled exception: {str(e)[:40]}")
                time.sleep(2)


def main():
    cli_args = parse_cli_args()
    config = Config(cli_args)
    app = SimulatorApp(config)
    app.run()


if __name__ == "__main__":
    main()
