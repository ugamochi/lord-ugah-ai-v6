"""
Lord-Ugah-AI-v6 Template Usage Analyzer

This script analyzes which note and Ugahbase templates are most used in the system.
- Scans all notes and Ugahbases for template markers or structure.
- Prints a summary of template usage counts.
"""
import os
import re
from glob import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = [
    os.path.join(SCRIPT_DIR, "..", "ugahbases"),
    os.path.join(SCRIPT_DIR, "..", "..", "ugahbases"),
]
UGAHBASES_DIR = None
for candidate in CANDIDATES:
    abs_candidate = os.path.abspath(candidate)
    if os.path.isdir(abs_candidate):
        UGAHBASES_DIR = abs_candidate
        break
if UGAHBASES_DIR is None:
    raise FileNotFoundError("Could not find 'ugahbases' directory relative to script location.")

TEMPLATE_MARKERS = [
    "note-template.md",
    "ugahbase-template/index.md",
    "ugahbase-template/starter-note.md",
]


def get_note_files():
    """Return a list of all markdown note files in Ugahbases."""
    return glob(os.path.join(UGAHBASES_DIR, "**", "*.md"), recursive=True)


def analyze_templates():
    """Count how many notes/Ugahbases are based on each template."""
    notes = get_note_files()
    usage = {marker: 0 for marker in TEMPLATE_MARKERS}
    for note in notes:
        with open(note, "r") as f:
            content = f.read()
        for marker in TEMPLATE_MARKERS:
            if marker in content or f"template: {marker}" in content:
                usage[marker] += 1
    return usage


def print_report(usage):
    print("[Lord-Ugah-AI-v6] Template Usage Report")
    for marker, count in usage.items():
        print(f"Template '{marker}': {count} uses")
    print("Template usage analysis complete.")


def main():
    usage = analyze_templates()
    print_report(usage)


if __name__ == "__main__":
    main() 