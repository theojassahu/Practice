"""
Configuration Manager for Hackatime & VS Code Activity Simulator.
Reads ~/.wakatime.cfg, config.json, environment variables, and CLI arguments.
"""

import os
import sys
import json
import configparser
import argparse
from pathlib import Path

DEFAULT_TARGET_DIR = r"C:\Users\pvoja\Desktop\OJAS\CODING\My_First_Hackatime_Website"
DEFAULT_API_URL = "https://hackatime.hackclub.com/api/hackatime/v1"
CONFIG_FILE_NAME = "config.json"


def get_user_wakatime_cfg() -> dict:
    """Parses ~/.wakatime.cfg for api_key, api_url, and hostname."""
    cfg_path = Path.home() / ".wakatime.cfg"
    result = {
        "api_key": None,
        "api_url": DEFAULT_API_URL,
        "hostname": None,
        "heartbeat_rate_limit_seconds": 30,
    }

    if cfg_path.exists():
        try:
            parser = configparser.ConfigParser()
            parser.read(str(cfg_path), encoding="utf-8")
            if "settings" in parser:
                settings = parser["settings"]
                result["api_key"] = settings.get("api_key", "").strip() or None
                result["api_url"] = settings.get("api_url", DEFAULT_API_URL).strip()
                result["hostname"] = settings.get("hostname", "").strip() or None
                rate_limit = settings.get("heartbeat_rate_limit_seconds", "30").strip()
                if rate_limit.isdigit():
                    result["heartbeat_rate_limit_seconds"] = int(rate_limit)
        except Exception as e:
            print(f"[Config] Warning reading {cfg_path}: {e}", file=sys.stderr)

    return result


class Config:
    def __init__(self, cli_args: argparse.Namespace = None):
        waka_cfg = get_user_wakatime_cfg()

        # Load local config.json if exists
        local_cfg = {}
        local_cfg_path = Path(__file__).parent / CONFIG_FILE_NAME
        if local_cfg_path.exists():
            try:
                with open(local_cfg_path, "r", encoding="utf-8") as f:
                    local_cfg = json.load(f)
            except Exception as e:
                print(f"[Config] Warning reading local {CONFIG_FILE_NAME}: {e}", file=sys.stderr)

        # Precedence: CLI args > local config.json > ~/.wakatime.cfg > defaults
        self.target_dir = os.path.abspath(
            (cli_args and cli_args.target_dir)
            or local_cfg.get("target_dir")
            or DEFAULT_TARGET_DIR
        )

        self.project_name = (
            (cli_args and cli_args.project_name)
            or local_cfg.get("project_name")
            or os.path.basename(self.target_dir)
        )

        self.api_key = (
            (cli_args and cli_args.api_key)
            or local_cfg.get("api_key")
            or waka_cfg.get("api_key")
            or ""
        )

        self.api_url = (
            (cli_args and cli_args.api_url)
            or local_cfg.get("api_url")
            or waka_cfg.get("api_url")
            or DEFAULT_API_URL
        )

        self.hostname = (
            (cli_args and cli_args.hostname)
            or local_cfg.get("hostname")
            or waka_cfg.get("hostname")
            or os.environ.get("COMPUTERNAME", "WIN-DEV")
        )

        self.speed = (
            (cli_args and cli_args.speed)
            or local_cfg.get("speed")
            or "normal"
        ).lower()

        self.enable_heartbeat = True
        if cli_args and cli_args.no_heartbeat:
            self.enable_heartbeat = False
        elif "enable_heartbeat" in local_cfg:
            self.enable_heartbeat = bool(local_cfg["enable_heartbeat"])

        self.headless = bool(
            (cli_args and cli_args.headless)
            or local_cfg.get("headless", False)
        )

        self.dynamic_project_name = bool(
            (cli_args and getattr(cli_args, "dynamic_project", None) is not None and cli_args.dynamic_project)
            or local_cfg.get("dynamic_project_name", True)
        )

        self.rate_limit_seconds = int(
            (cli_args and cli_args.rate_limit)
            or local_cfg.get("rate_limit_seconds")
            or waka_cfg.get("heartbeat_rate_limit_seconds")
            or 30
        )

        # Speed profiles (min_delay, max_delay in seconds between typing strokes/lines)
        self.speed_profiles = {
            "chill": {"stroke_delay": (0.08, 0.18), "line_pause": (0.8, 2.5), "think_pause": (15, 45), "burst_duration": (20, 60)},
            "normal": {"stroke_delay": (0.04, 0.10), "line_pause": (0.4, 1.5), "think_pause": (8, 25), "burst_duration": (30, 90)},
            "fast": {"stroke_delay": (0.02, 0.06), "line_pause": (0.2, 0.8), "think_pause": (4, 12), "burst_duration": (45, 120)},
            "turbo": {"stroke_delay": (0.005, 0.02), "line_pause": (0.05, 0.3), "think_pause": (2, 6), "burst_duration": (60, 180)},
        }

    @property
    def current_speed_profile(self) -> dict:
        return self.speed_profiles.get(self.speed, self.speed_profiles["normal"])

    def save_to_file(self, path: Path = None):
        """Saves current configuration to config.json."""
        if path is None:
            path = Path(__file__).parent / CONFIG_FILE_NAME
        data = {
            "target_dir": self.target_dir,
            "project_name": self.project_name,
            "api_key": self.api_key,
            "api_url": self.api_url,
            "hostname": self.hostname,
            "speed": self.speed,
            "enable_heartbeat": self.enable_heartbeat,
            "dynamic_project_name": self.dynamic_project_name,
            "headless": self.headless,
            "rate_limit_seconds": self.rate_limit_seconds,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


def parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Realistic VS Code & Hackatime Coding Activity Simulator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--target-dir",
        "-t",
        type=str,
        default=DEFAULT_TARGET_DIR,
        help="Target project directory path to simulate coding in",
    )
    parser.add_argument(
        "--project-name",
        "-p",
        type=str,
        default=None,
        help="Project name reported to Hackatime (defaults to folder name)",
    )
    parser.add_argument(
        "--speed",
        "-s",
        choices=["chill", "normal", "fast", "turbo"],
        default="normal",
        help="Typing and coding simulation speed preset",
    )
    parser.add_argument(
        "--api-key",
        "-k",
        type=str,
        default=None,
        help="Hackatime / WakaTime API key (defaults to ~/.wakatime.cfg)",
    )
    parser.add_argument(
        "--api-url",
        "-u",
        type=str,
        default=None,
        help="Hackatime API URL (defaults to ~/.wakatime.cfg or Hackatime)",
    )
    parser.add_argument(
        "--hostname",
        type=str,
        default=None,
        help="Machine hostname reported in heartbeats",
    )
    parser.add_argument(
        "--rate-limit",
        "-r",
        type=int,
        default=30,
        help="Minimum seconds between Hackatime heartbeats",
    )
    parser.add_argument(
        "--no-heartbeat",
        action="store_true",
        help="Disable direct Hackatime API heartbeats (file edits only)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run without interactive terminal UI dashboard (log output only)",
    )
    return parser.parse_args()
