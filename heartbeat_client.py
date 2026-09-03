"""
Hackatime / WakaTime Telemetry Dispatcher.
Formats and sends authentic VS Code telemetry heartbeats with rate-limiting, error handling, and stats.
"""

import os
import sys
import time
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Dict, Any, List

LANGUAGE_MAP = {
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".json": "JSON",
    ".md": "Markdown",
    ".py": "Python",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".txt": "Text",
}


class HeartbeatClient:
    def __init__(self, api_key: str, api_url: str, project_name: str, rate_limit_seconds: int = 30, dynamic_project_name: bool = True):
        self.api_key = api_key
        self.api_url = api_url.rstrip("/")
        self.project_name = project_name
        self.rate_limit_seconds = rate_limit_seconds
        self.dynamic_project_name = dynamic_project_name

        # Ensure correct endpoint
        if not self.api_url.endswith("/users/current/heartbeats"):
            if self.api_url.endswith("/v1"):
                self.endpoint = f"{self.api_url}/users/current/heartbeats"
            else:
                self.endpoint = f"{self.api_url}/v1/users/current/heartbeats"
        else:
            self.endpoint = self.api_url

        self.last_heartbeat_time: float = 0
        self.total_sent: int = 0
        self.successful: int = 0
        self.failed: int = 0
        self.last_status: Optional[int] = None
        self.last_error: Optional[str] = None

        # Build Authorization header
        auth_str = base64.b64encode(self.api_key.encode("utf-8")).decode("utf-8") if self.api_key else ""
        self.headers = {
            "Authorization": f"Basic {auth_str}",
            "Content-Type": "application/json",
            "User-Agent": "wakatime/v1.105.0 (win32-10.0.22631) vscode/1.92.2 vscode-wakatime/24.1.0",
        }

    def detect_language(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        return LANGUAGE_MAP.get(ext, "JavaScript")

    def should_send(self, is_write: bool) -> bool:
        """Determines if a heartbeat should be dispatched according to rate limiting."""
        now = time.time()
        if is_write:
            return True
        return (now - self.last_heartbeat_time) >= self.rate_limit_seconds

    def send_heartbeat(self, event: Dict[str, Any], force: bool = False) -> bool:
        """Dispatches a single heartbeat to the Hackatime/WakaTime endpoint."""
        if not self.api_key:
            self.last_error = "No API key configured"
            return False

        is_write = event.get("is_write", False)
        if not force and not self.should_send(is_write):
            return False

        file_path = event.get("file_path", "")
        language = self.detect_language(file_path)
        timestamp = event.get("time", time.time())

        report_project = (
            event.get("project_name")
            if self.dynamic_project_name and event.get("project_name")
            else self.project_name
        )

        payload = [
            {
                "entity": file_path,
                "type": "file",
                "time": timestamp,
                "project": report_project,
                "language": language,
                "lines": event.get("total_lines", 1),
                "lineno": event.get("line_no", 1),
                "cursorpos": event.get("cursorpos", 1),
                "is_write": is_write,
                "category": "coding",
            }
        ]

        self.total_sent += 1
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(self.endpoint, data=data, headers=self.headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                self.last_status = resp.status
                if resp.status in (200, 201, 202):
                    self.successful += 1
                    self.last_heartbeat_time = time.time()
                    self.last_error = None
                    return True
                else:
                    self.failed += 1
                    self.last_error = f"Unexpected HTTP {resp.status}"
                    return False
        except urllib.error.HTTPError as e:
            self.failed += 1
            self.last_status = e.code
            self.last_error = f"HTTP {e.code}: {e.reason}"
            return False
        except urllib.error.URLError as e:
            self.failed += 1
            self.last_status = None
            self.last_error = f"Network Error: {e.reason}"
            return False
        except Exception as e:
            self.failed += 1
            self.last_status = None
            self.last_error = str(e)
            return False
