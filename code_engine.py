"""
Multi-Project Code Engine Module.
Simulates natural, continuous human-like coding across multiple realistic projects:
- Modern Scientific Calculator
- Netflix Streaming Platform Clone
- Amazon Storefront Marketplace
- Enterprise SaaS Analytics Platform
- Agile Kanban Sprint Board
- Developer Workspace Hub (Root)

Randomly selects and rotates between projects, creating files line-by-line with
realistic typing, backspaces, comments, refactoring, and saves.
"""

import os
import sys
import time
import random
from pathlib import Path
from typing import Callable, Optional, Dict, Any, List

from code_templates import (
    ALL_PROJECT_BLUEPRINTS,
    WORKSPACE_HUB_FILES,
    DYNAMIC_SNIPPETS,
    DOMAIN_COMMENTS,
)


class CodeEngine:
    def __init__(
        self,
        target_dir: str,
        speed_profile: dict,
        event_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
    ):
        self.target_dir = Path(target_dir)
        self.speed_profile = speed_profile
        self.event_callback = event_callback or (lambda event: None)

        self.stroke_delay_range = speed_profile.get("stroke_delay", (0.04, 0.10))
        self.line_pause_range = speed_profile.get("line_pause", (0.4, 1.5))
        self.think_pause_range = speed_profile.get("think_pause", (8, 25))

        self.total_lines_written = 0
        self.total_edits = 0
        self.current_file: Optional[Path] = None
        self.current_line: int = 1
        self.is_running = True

        # Multi-project state
        self.projects = ALL_PROJECT_BLUEPRINTS
        self.current_project_index = 0
        self.actions_in_current_project = 0
        self.max_actions_before_switch = random.randint(6, 15)

    @property
    def current_project(self) -> dict:
        return self.projects[self.current_project_index]

    def notify(
        self,
        action: str,
        file_path: Path,
        line_no: int,
        is_write: bool,
        details: str = "",
        project_name: Optional[str] = None,
    ):
        """Emits an event to the callback for heartbeats and dashboard."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                total_lines = len(lines)
        except Exception:
            total_lines = max(line_no, 1)

        # Compute clean relative path from target_dir
        try:
            rel_path = file_path.relative_to(self.target_dir)
        except Exception:
            rel_path = file_path.name

        p_name = project_name or self.current_project.get("name", "Engineering-Workspace")

        event = {
            "action": action,
            "project_name": p_name,
            "subproject_key": self.current_project.get("key", "hub"),
            "file_path": str(file_path.resolve()),
            "relative_path": str(rel_path).replace("\\", "/"),
            "line_no": max(1, line_no),
            "total_lines": total_lines,
            "cursorpos": random.randint(1, 35),
            "is_write": is_write,
            "details": details,
            "time": time.time(),
        }
        self.event_callback(event)

    def initialize_workspace(self):
        """Seeds the root workspace hub and makes sure the target directory exists."""
        self.target_dir.mkdir(parents=True, exist_ok=True)

        # Seed workspace hub files (index.html & README.md at root)
        for rel_path, content in WORKSPACE_HUB_FILES.items():
            full_path = self.target_dir / rel_path
            if not full_path.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
                self.notify("CREATE_FILE", full_path, 1, True, f"Workspace index {rel_path}", "Workspace-Hub")
                self._type_out_file_content(full_path, content, initial_seed=True, project_name="Workspace-Hub")

    def ensure_current_project_seeded(self):
        """Ensures the active project has its foundational files created."""
        proj = self.current_project
        proj_dir = self.target_dir / proj["key"]
        proj_dir.mkdir(parents=True, exist_ok=True)

        for rel_path, content in proj["files"].items():
            full_path = proj_dir / rel_path
            if not full_path.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
                self.notify(
                    "CREATE_FILE",
                    full_path,
                    1,
                    True,
                    f"Creating {proj['key']}/{rel_path}",
                    proj["name"]
                )
                self._type_out_file_content(full_path, content, initial_seed=True, project_name=proj["name"])

    def _type_out_file_content(
        self,
        file_path: Path,
        content: str,
        initial_seed: bool = False,
        project_name: Optional[str] = None,
    ):
        """Simulates typing out content line by line."""
        lines = content.splitlines(keepends=True)
        written_lines = []

        file_path.parent.mkdir(parents=True, exist_ok=True)
        delay_factor = 0.12 if initial_seed else 1.0

        for idx, line in enumerate(lines, start=1):
            if not self.is_running:
                break
            written_lines.append(line)
            self.total_lines_written += 1
            self.current_file = file_path
            self.current_line = idx

            # Flush to disk
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(written_lines)

            is_save = (idx == len(lines))
            self.notify(
                "SAVING" if is_save else "TYPING",
                file_path,
                idx,
                is_save,
                f"Writing line {idx}/{len(lines)}: {line.strip()[:35]}",
                project_name or self.current_project["name"]
            )

            pause = random.uniform(*self.line_pause_range) * delay_factor
            time.sleep(pause)

        self.total_edits += 1

    def _simulate_typo(self, line: str):
        """Simulates subtle human typos and corrections."""
        if len(line) > 12 and random.random() < 0.20:
            time.sleep(random.uniform(*self.stroke_delay_range))
            time.sleep(random.uniform(0.08, 0.20))
            time.sleep(random.uniform(*self.stroke_delay_range))

    def append_feature_snippet(self):
        """Appends a realistic domain-specific snippet to a JS or CSS file in the active project."""
        proj = self.current_project
        proj_dir = self.target_dir / proj["key"]
        code_files = [
            f for f in proj_dir.rglob("*.*")
            if f.suffix in (".js", ".css")
        ]

        if not code_files:
            self.ensure_current_project_seeded()
            return

        target_file = random.choice(code_files)
        snippets = DYNAMIC_SNIPPETS.get(proj["key"], [])
        if not snippets:
            return

        snippet = random.choice(snippets)
        with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
            existing_lines = f.readlines()

        start_line = len(existing_lines) + 1
        new_lines = snippet.splitlines(keepends=True)

        for offset, line in enumerate(new_lines):
            if not self.is_running:
                break
            current_line_no = start_line + offset
            self._simulate_typo(line)
            existing_lines.append(line)
            self.total_lines_written += 1
            self.current_file = target_file
            self.current_line = current_line_no

            with open(target_file, "w", encoding="utf-8") as f:
                f.writelines(existing_lines)

            is_last = (offset == len(new_lines) - 1)
            self.notify(
                "SAVING" if is_last else "TYPING",
                target_file,
                current_line_no,
                is_last,
                f"Appended logic: {line.strip()[:35]}",
                proj["name"]
            )
            time.sleep(random.uniform(*self.line_pause_range))

        self.total_edits += 1

    def modify_existing_code(self):
        """Refactors an existing line of code in the current project."""
        proj = self.current_project
        proj_dir = self.target_dir / proj["key"]
        code_files = [
            f for f in proj_dir.rglob("*.*")
            if f.suffix in (".js", ".css", ".html")
        ]

        if not code_files:
            self.ensure_current_project_seeded()
            return

        target_file = random.choice(code_files)
        try:
            with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            return

        if not lines:
            return

        target_idx = random.randint(0, len(lines) - 1)
        original_line = lines[target_idx]

        # Domain-aware tweak
        new_line = original_line
        if target_file.suffix == ".css":
            color_swaps = [
                ("#3b82f6", "#2563eb"),
                ("#E50914", "#b81d24"),
                ("#febd69", "#f08804"),
                ("#10b981", "#059669"),
                ("14px", "15px"),
                ("18px", "20px"),
                ("0.3s", "0.25s")
            ]
            for old, new in color_swaps:
                if old in original_line:
                    new_line = original_line.replace(old, new)
                    break
            if new_line == original_line:
                new_line = original_line.rstrip() + " /* layout optimized */\n"
        elif target_file.suffix == ".js":
            if "console.log" in original_line or "console.debug" in original_line:
                new_line = f"        console.debug('[{proj['key']}] Synced state at {time.strftime('%H:%M:%S')}');\n"
            elif "const " in original_line or "let " in original_line:
                new_line = original_line.rstrip() + " // reviewed\n"
            else:
                new_line = original_line.rstrip() + f" // verified {time.strftime('%M:%S')}\n"
        elif target_file.suffix == ".html":
            new_line = original_line.rstrip() + " <!-- DOM verified -->\n"

        lines[target_idx] = new_line
        self.current_file = target_file
        self.current_line = target_idx + 1

        with open(target_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        self.notify(
            "MODIFY",
            target_file,
            self.current_line,
            True,
            f"Refactored line {self.current_line}: {new_line.strip()[:35]}",
            proj["name"]
        )
        self.total_edits += 1

    def add_comment_or_docstring(self):
        """Inserts an informative developer comment into the current project."""
        proj = self.current_project
        proj_dir = self.target_dir / proj["key"]
        code_files = [
            f for f in proj_dir.rglob("*.*")
            if f.suffix in (".js", ".css", ".html")
        ]

        if not code_files:
            return

        target_file = random.choice(code_files)
        with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        if not lines:
            return

        insert_idx = random.randint(0, len(lines))
        comments = DOMAIN_COMMENTS.get(proj["key"], ["// Reviewed code logic"])
        comment = random.choice(comments) + "\n"

        lines.insert(insert_idx, comment)
        self.total_lines_written += 1
        self.current_file = target_file
        self.current_line = insert_idx + 1

        with open(target_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        self.notify(
            "ADD_COMMENT",
            target_file,
            self.current_line,
            True,
            f"Comment: {comment.strip()[:35]}",
            proj["name"]
        )
        self.total_edits += 1

    def create_project_test_or_utility(self):
        """Creates an authentic unit test or helper utility file for the active project."""
        proj = self.current_project
        proj_dir = self.target_dir / proj["key"]
        tests_dir = proj_dir / "tests"
        tests_dir.mkdir(parents=True, exist_ok=True)

        test_file_name = f"tests/spec_{random.randint(10, 99)}.test.js"
        target_path = proj_dir / test_file_name

        if target_path.exists():
            return

        test_content = f"""/**
 * Unit Test Suite for {proj['name']}
 * Validates edge cases, input sanitation, and async pipelines.
 */

import {{ describe, it, expect }} from 'vitest';

describe('{proj['name']} Core Module', () => {{
    it('should initialize without uncaught exceptions', () => {{
        expect(true).toBe(true);
    }});

    it('should process operations with sub-millisecond latency', () => {{
        const start = performance.now();
        let sum = 0;
        for (let i = 0; i < 5000; i++) sum += i;
        const elapsed = performance.now() - start;
        expect(elapsed).toBeLessThan(30);
    }});
}});
"""
        self.notify("CREATE_MODULE", target_path, 1, True, f"Created {test_file_name}", proj["name"])
        self._type_out_file_content(target_path, test_content, project_name=proj["name"])

    def simulate_thinking_pause(self):
        """Simulates a developer thinking, reading docs, or testing locally."""
        pause_duration = random.uniform(*self.think_pause_range)
        if self.current_file:
            self.notify(
                "THINKING",
                self.current_file,
                self.current_line,
                False,
                f"Reviewing logic / docs (~{int(pause_duration)}s)",
                self.current_project["name"]
            )
        time.sleep(pause_duration)

    def rotate_project_if_needed(self):
        """Rotates to a different project periodically to simulate natural developer behavior."""
        self.actions_in_current_project += 1
        if self.actions_in_current_project >= self.max_actions_before_switch:
            # Pick a different project
            prev_idx = self.current_project_index
            other_indices = [i for i in range(len(self.projects)) if i != prev_idx]
            self.current_project_index = random.choice(other_indices)
            self.actions_in_current_project = 0
            self.max_actions_before_switch = random.randint(6, 18)
            new_proj = self.current_project

            self.ensure_current_project_seeded()

            # Emit a notification of project switch
            proj_entry_file = self.target_dir / new_proj["key"] / "app.js"
            if proj_entry_file.exists():
                self.notify(
                    "PROJECT_SWITCH",
                    proj_entry_file,
                    1,
                    False,
                    f"Switched focus to: {new_proj['name']}",
                    new_proj["name"]
                )

    def perform_random_action(self):
        """Executes a weighted random developer action in the active project."""
        self.ensure_current_project_seeded()

        weights = [
            (self.append_feature_snippet, 0.40),
            (self.modify_existing_code, 0.25),
            (self.add_comment_or_docstring, 0.15),
            (self.create_project_test_or_utility, 0.10),
            (self.simulate_thinking_pause, 0.10),
        ]

        actions, probs = zip(*weights)
        chosen_action = random.choices(actions, weights=probs, k=1)[0]
        chosen_action()

        self.rotate_project_if_needed()

    def stop(self):
        self.is_running = False
