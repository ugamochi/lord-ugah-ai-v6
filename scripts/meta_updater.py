"""
Lord-Ugah-AI-v6 Meta Updater Script

This script automates updates to meta/ugahbase-registry.md and meta/expansion-log.md.
- Scans ugahbases/ for all Ugahbases.
- Updates the registry with Ugahbase names and creation dates (from index.md or file creation time).
- Appends to the expansion log if new Ugahbases are detected.
"""
import os
import re
import subprocess
from utils import get_current_datetime
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UGAHBASES_DIR = os.path.join(ROOT, "ugahbases")
REGISTRY_PATH = os.path.join(ROOT, "meta", "ugahbase-registry.md")
EXPANSION_LOG_PATH = os.path.join(ROOT, "meta", "expansion-log.md")

CREATED_PATTERN = re.compile(r'created:\s*"(.*?)"')

def get_ugahbases():
    """Return a list of Ugahbase names (directories) in ugahbases/."""
    return [d for d in os.listdir(UGAHBASES_DIR) if os.path.isdir(os.path.join(UGAHBASES_DIR, d)) and not d.startswith('.')]


def get_creation_date(ugahbase):
    """Try to get the creation date from index.md, else use folder creation time."""
    index_path = os.path.join(UGAHBASES_DIR, ugahbase, "index.md")
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            content = f.read()
        match = CREATED_PATTERN.search(content)
        if match:
            return match.group(1)
    # Fallback: use folder creation time
    stat = os.stat(os.path.join(UGAHBASES_DIR, ugahbase))
    return datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d")


def update_registry(ugahbases):
    """Write all Ugahbases and their creation dates to the registry file."""
    lines = ["# Ugahbase Registry\n", "\n"]
    for u in sorted(ugahbases):
        date = get_creation_date(u)
        lines.append(f"- {u} (created {date})\n")
    with open(REGISTRY_PATH, "w") as f:
        f.writelines(lines)


def update_expansion_log(ugahbases):
    """Append new Ugahbases to the expansion log if not already present."""
    if not os.path.exists(EXPANSION_LOG_PATH):
        with open(EXPANSION_LOG_PATH, "w") as f:
            f.write("# Expansion Log\n\n")
    with open(EXPANSION_LOG_PATH, "r+") as f:
        log = f.read()
        for u in ugahbases:
            date = get_creation_date(u)
            entry = f"- {date}: Added '{u}' Ugahbase"
            if entry not in log:
                f.write(entry + "\n")


def main():
    print("[Lord-Ugah-AI-v6] Meta Updater")
    ugahbases = get_ugahbases()
    update_registry(ugahbases)
    update_expansion_log(ugahbases)
    print("Meta-system registry and expansion log updated.")


if __name__ == "__main__":
    main() 