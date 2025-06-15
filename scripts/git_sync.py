"""
Lord-Ugah-AI-v6 Git Sync Script

This script automates basic GitHub sync operations:
- Add, commit, and push changes
- Pull updates from remote

Usage:
- Run with 'push' to add, commit, and push (will prompt for a commit message)
- Run with 'pull' to fetch and merge updates from remote
"""
import os
import subprocess
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run_git_command(args):
    result = subprocess.run(["git"] + args, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"Git command failed: {' '.join(args)}")
        sys.exit(result.returncode)


def git_push():
    run_git_command(["add", "."])
    msg = input("Enter commit message: ").strip()
    if not msg:
        msg = "Update Lord-Ugah-AI-v6"
    run_git_command(["commit", "-m", msg])
    run_git_command(["push"])
    print("Changes pushed to remote.")


def git_pull():
    run_git_command(["pull"])
    print("Pulled latest changes from remote.")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("push", "pull"):
        print("Usage: python3 scripts/git_sync.py [push|pull]")
        sys.exit(1)
    if sys.argv[1] == "push":
        git_push()
    elif sys.argv[1] == "pull":
        git_pull()


if __name__ == "__main__":
    main() 