"""
Lord-Ugah-AI-v6 Initialization Script

This script checks for required folders and creates any that are missing.
Run this once to ensure the system structure is ready for use.
"""
import os
import subprocess
from scripts.utils import get_current_datetime

REQUIRED_DIRS = [
    "scripts",
    "templates/ugahbase-template",
    "templates/cursor-rules-templates",
    "ugahbases/react-debugging",
    "ugahbases/vibe-coding",
    "ugahbases/music-production",
    "ugahbases/client-communication",
    "ugahbases/system-architecture",
    "meta",
    "archive/deprecated",
]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ensure_dirs():
    """Ensure all required directories exist."""
    created = []
    for rel_path in REQUIRED_DIRS:
        abs_path = os.path.join(ROOT, "lord-ugah-ai-v6", rel_path)
        if not os.path.exists(abs_path):
            os.makedirs(abs_path, exist_ok=True)
            created.append(rel_path)
    return created


def main():
    print("[Lord-Ugah-AI-v6] Initialization started.")
    created = ensure_dirs()
    if created:
        print("Created missing directories:")
        for d in created:
            print(f"  - {d}")
    else:
        print("All required directories already exist.")
    print("[Lord-Ugah-AI-v6] Initialization complete.")


if __name__ == "__main__":
    main() 