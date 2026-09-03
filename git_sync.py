"""
Git Synchronization Module for Hackatime & VS Code Coding Simulator.
Automatically commits and pushes latest coding progress to GitHub on pause/exit.
Target Remote: https://github.com/theojassahu/Practice.git
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
from typing import Tuple, Optional


def run_git_command(args: list, cwd: Path) -> Tuple[int, str, str]:
    """Executes a git command and returns (returncode, stdout, stderr)."""
    try:
        proc = subprocess.run(
            ["git"] + args,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Git command timed out after 30 seconds"
    except Exception as e:
        return -1, "", str(e)


def copy_progress_files(source_dir: Path, dest_dir: Path):
    """
    Copies latest generated project files from source_dir (e.g. My_First_Hackatime_Website)
    into the repo directory under projects/ to ensure all work is tracked and versioned.
    """
    if not source_dir.exists():
        return

    projects_dest = dest_dir / "projects"
    projects_dest.mkdir(parents=True, exist_ok=True)

    # Directories to copy
    for item in source_dir.iterdir():
        if item.name.startswith("."):
            continue

        target_dest = projects_dest / item.name
        if item.is_dir():
            if target_dest.exists():
                shutil.rmtree(target_dest, ignore_errors=True)
            shutil.copytree(item, target_dest, dirs_exist_ok=True)
        elif item.is_file():
            shutil.copy2(item, target_dest)


def sync_progress_to_github(
    target_dir: str,
    repo_dir: Optional[str] = None,
    remote_url: str = "https://github.com/theojassahu/Practice.git",
    custom_msg: Optional[str] = None,
) -> Tuple[bool, str]:
    """
    Stages, commits, and pushes all progress to the GitHub repository.
    """
    source_path = Path(target_dir)
    repo_path = Path(repo_dir) if repo_dir else Path(__file__).parent.resolve()

    print(f"\n[Git Sync] Saving latest coding progress to {remote_url}...", flush=True)

    # 1. Ensure git is initialized in repo_path
    if not (repo_path / ".git").exists():
        code, out, err = run_git_command(["init"], repo_path)
        if code != 0:
            return False, f"git init failed: {err}"

    # 2. Ensure remote origin is set
    code, out, err = run_git_command(["remote", "get-url", "origin"], repo_path)
    if code != 0:
        run_git_command(["remote", "add", "origin", remote_url], repo_path)
    elif out != remote_url:
        run_git_command(["remote", "set-url", "origin", remote_url], repo_path)

    # 3. Ensure branch is main
    run_git_command(["branch", "-M", "main"], repo_path)

    # 4. Mirror active projects from target_dir into repo_path/projects
    try:
        copy_progress_files(source_path, repo_path)
    except Exception as e:
        print(f"[Git Sync] Warning syncing project files: {e}", file=sys.stderr)

    # 5. Stage all changes
    code, out, err = run_git_command(["add", "-A"], repo_path)
    if code != 0:
        return False, f"git add failed: {err}"

    # 6. Check if there are changes to commit
    code, status_out, err = run_git_command(["status", "--porcelain"], repo_path)
    if not status_out:
        print("[Git Sync] Everything up to date! No uncommitted changes.", flush=True)
        return True, "No changes to commit"

    # Count modified files
    num_changes = len(status_out.strip().splitlines())

    # 7. Generate realistic commit message
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    if custom_msg:
        commit_msg = custom_msg
    else:
        commit_msg = f"chore(progress): save active coding session [{timestamp}] - {num_changes} files updated"

    code, out, err = run_git_command(["commit", "-m", commit_msg], repo_path)
    if code != 0:
        return False, f"git commit failed: {err}"

    print(f"[Git Sync] Committed {num_changes} files: '{commit_msg}'", flush=True)

    # 8. Push to remote main
    print(f"[Git Sync] Pushing to origin main...", flush=True)
    code, out, err = run_git_command(["push", "origin", "main"], repo_path)
    if code != 0:
        # If rejected due to remote updates, attempt rebase and push
        if "rejected" in err.lower() or "fetch first" in err.lower():
            print("[Git Sync] Remote has newer commits. Pulling and rebasing...", flush=True)
            run_git_command(["pull", "--rebase", "origin", "main"], repo_path)
            code, out, err = run_git_command(["push", "origin", "main"], repo_path)

        if code != 0:
            msg = f"git push failed: {err or out}"
            print(f"[Git Sync] ⚠️  {msg}", file=sys.stderr)
            return False, msg

    success_msg = f"Successfully pushed progress to {remote_url} (branch: main)"
    print(f"[Git Sync] ✅ {success_msg}\n", flush=True)
    return True, success_msg


if __name__ == "__main__":
    from config import Config
    cfg = Config()
    custom_message = sys.argv[1] if len(sys.argv) > 1 else None
    success, msg = sync_progress_to_github(
        target_dir=cfg.target_dir,
        repo_dir=str(Path(__file__).parent),
        remote_url="https://github.com/theojassahu/Practice.git",
        custom_msg=custom_message,
    )
    sys.exit(0 if success else 1)
