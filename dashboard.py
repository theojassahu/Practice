"""
Interactive Terminal UI (TUI) Dashboard for Hackatime Simulator.
Provides live statistics, activity animation, and event history stream.
"""

import os
import sys
import time
from datetime import timedelta
from typing import List, Dict, Any, Optional

# Ensure UTF-8 stdout on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# Colors
CYAN = "\033[36m"
BRIGHT_CYAN = "\033[96m"
GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
YELLOW = "\033[33m"
BRIGHT_YELLOW = "\033[93m"
MAGENTA = "\033[35m"
BRIGHT_MAGENTA = "\033[95m"
BLUE = "\033[34m"
BRIGHT_BLUE = "\033[94m"
RED = "\033[31m"
WHITE = "\033[37m"
BG_DARK = "\033[48;5;234m"
BG_BLUE = "\033[48;5;24m"

ACTION_ICONS = {
    "CREATE_FILE": f"{BRIGHT_GREEN}📁 CREATE{RESET}",
    "CREATE_COMPONENT": f"{BRIGHT_CYAN}🧩 MODULE{RESET}",
    "TYPING": f"{BRIGHT_YELLOW}✍️  TYPING{RESET}",
    "SAVING": f"{BRIGHT_GREEN}💾 SAVED {RESET}",
    "MODIFY": f"{BRIGHT_MAGENTA}🔧 REFACT{RESET}",
    "ADD_COMMENT": f"{BLUE}💬 DOCS  {RESET}",
    "THINKING": f"{MAGENTA}☕ PAUSE {RESET}",
    "HEARTBEAT": f"{BRIGHT_CYAN}⚡ SYNCED{RESET}",
    "GIT_SYNC": f"{BRIGHT_GREEN}📦 GIT   {RESET}",
}


class Dashboard:
    def __init__(self, project_name: str, target_dir: str, speed_mode: str, enable_heartbeat: bool, headless: bool = False):
        self.project_name = project_name
        self.target_dir = target_dir
        self.speed_mode = speed_mode
        self.enable_heartbeat = enable_heartbeat
        self.headless = headless

        self.start_time = time.time()
        self.log_history: List[Dict[str, Any]] = []
        self.max_history = 8

        # Windows ANSI color support activation
        if os.name == "nt":
            os.system("")

    def add_log(self, action: str, details: str, file_name: str = ""):
        entry = {
            "time": time.strftime("%H:%M:%S"),
            "action": action,
            "details": details,
            "file": file_name,
        }
        self.log_history.append(entry)
        if len(self.log_history) > self.max_history:
            self.log_history.pop(0)

        if self.headless:
            icon_tag = action
            try:
                print(f"[{entry['time']}] [{icon_tag}] {file_name} - {details}", flush=True)
            except Exception:
                safe_details = details.encode("ascii", errors="replace").decode("ascii")
                print(f"[{entry['time']}] [{icon_tag}] {file_name} - {safe_details}", flush=True)

    def render(
        self,
        current_file: Optional[str],
        current_line: int,
        total_lines: int,
        total_edits: int,
        heartbeat_stats: Dict[str, Any],
        current_action: str,
        active_project: Optional[str] = None,
        git_sync_remaining: Optional[int] = None,
    ):
        """Draws the full interactive dashboard."""
        if self.headless:
            return

        uptime_sec = int(time.time() - self.start_time)
        uptime_str = str(timedelta(seconds=uptime_sec))

        hb_sent = heartbeat_stats.get("total_sent", 0)
        hb_success = heartbeat_stats.get("successful", 0)
        hb_failed = heartbeat_stats.get("failed", 0)
        hb_status = heartbeat_stats.get("last_status", "N/A")
        hb_err = heartbeat_stats.get("last_error")

        success_rate = f"{(hb_success / hb_sent * 100):.1f}%" if hb_sent > 0 else "100%"

        # Truncate paths for visual display
        display_dir = self.target_dir
        if len(display_dir) > 55:
            display_dir = "..." + display_dir[-52:]

        display_file = current_file or "Initializing..."
        if len(display_file) > 40:
            display_file = "..." + display_file[-37:]

        # Spinner animation
        spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        spinner = spinner_chars[int(time.time() * 5) % len(spinner_chars)]

        output = []
        # Clear screen and move to top
        output.append("\033[H\033[J")

        # Top Header Banner
        output.append(f"{BOLD}{BG_BLUE}{WHITE}  ⚡ HACKATIME & VS CODE ACTIVITY SIMULATOR  {RESET}")
        output.append(f"{DIM}─────────────────────────────────────────────────────────────────────────────{RESET}")

        # Meta info
        hb_mode_text = f"{BRIGHT_GREEN}ACTIVE (HTTP 202){RESET}" if self.enable_heartbeat else f"{YELLOW}DISABLED{RESET}"
        output.append(f" {BOLD}Project:{RESET} {BRIGHT_CYAN}{self.project_name}{RESET}  |  {BOLD}Speed:{RESET} {BRIGHT_MAGENTA}{self.speed_mode.upper()}{RESET}  |  {BOLD}Heartbeat:{RESET} {hb_mode_text}")
        output.append(f" {BOLD}Target Folder:{RESET} {DIM}{display_dir}{RESET}")
        output.append(f" {BOLD}Git Remote:{RESET}    {CYAN}https://github.com/theojassahu/Practice.git{RESET} {BRIGHT_GREEN}(Auto-sync Every 5m + On Pause){RESET}")
        output.append(f"{DIM}─────────────────────────────────────────────────────────────────────────────{RESET}")

        # Metrics Grid
        sync_str = f"in {git_sync_remaining // 60}m {git_sync_remaining % 60:02d}s" if git_sync_remaining is not None else "in 5m"
        output.append(f" {BOLD}SESSION METRICS:{RESET}")
        output.append(
            f"   ⏱️  {BOLD}Uptime:{RESET} {WHITE}{uptime_str}{RESET}           "
            f"📝 {BOLD}Total Lines Written:{RESET} {BRIGHT_GREEN}{total_lines:,}{RESET}"
        )
        output.append(
            f"   🔄 {BOLD}Total Edits/Saves:{RESET} {WHITE}{total_edits:,}{RESET}     "
            f"⚡ {BOLD}Heartbeats Sent:{RESET} {BRIGHT_CYAN}{hb_success}/{hb_sent}{RESET} ({success_rate})"
        )
        if hb_err:
            output.append(f"   ⚠️  {BOLD}Heartbeat Notice:{RESET} {YELLOW}{hb_err[:50]}{RESET}")
        else:
            output.append(
                f"   🌐 {BOLD}Telemetry Status:{RESET} {BRIGHT_GREEN}HTTP {hb_status or 202} OK{RESET}       "
                f"📦 {BOLD}Next Git Push:{RESET} {BRIGHT_CYAN}{sync_str}{RESET}"
            )

        output.append(f"{DIM}─────────────────────────────────────────────────────────────────────────────{RESET}")

        # Active File & Cursor State
        action_badge = ACTION_ICONS.get(current_action, current_action)
        output.append(f" {BOLD}LIVE EDITOR STATE:{RESET}  {spinner} {action_badge}")
        if active_project:
            output.append(f"   📁 {BOLD}Active Subproject:{RESET} {BRIGHT_CYAN}{active_project}{RESET}")
        output.append(f"   📄 {BOLD}Active File:{RESET} {BRIGHT_YELLOW}{display_file}{RESET}")
        output.append(f"   📍 {BOLD}Line Number:{RESET} {WHITE}{current_line}{RESET}")

        output.append(f"{DIM}─────────────────────────────────────────────────────────────────────────────{RESET}")

        # Activity Stream
        output.append(f" {BOLD}RECENT ACTIVITY LOG:{RESET}")
        if not self.log_history:
            output.append(f"   {DIM}Waiting for first editor action...{RESET}")
        else:
            for entry in self.log_history:
                icon = ACTION_ICONS.get(entry["action"], f"[{entry['action']}]")
                fname = f"{entry['file'][:20]:<20}" if entry["file"] else " " * 20
                output.append(f"   {DIM}{entry['time']}{RESET} {icon:<18} {CYAN}{fname}{RESET} {entry['details']}")

        output.append(f"{DIM}─────────────────────────────────────────────────────────────────────────────{RESET}")
        output.append(f" {DIM}Press {BOLD}Ctrl+C{RESET}{DIM} in this terminal to pause and safely exit anytime.{RESET}\n")

        # Print all at once to prevent flicker
        full_text = "\n".join(output)
        try:
            sys.stdout.write(full_text)
            sys.stdout.flush()
        except UnicodeEncodeError:
            sys.stdout.write(full_text.encode("ascii", errors="replace").decode("ascii"))
            sys.stdout.flush()
        except Exception:
            pass
