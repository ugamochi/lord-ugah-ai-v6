"""
Lord-Ugah-AI-v6 Link Validator Script

This script scans all markdown files in Ugahbases, extracts cross-references, and reports missing or orphaned links.
Run this to maintain system integrity and ensure all crossrefs are valid.
"""
import os
import re
from glob import glob
import subprocess
# Dual import pattern: allows running as a module or as a script
try:
    from .utils import get_current_datetime  # module import
except ImportError:
    from utils import get_current_datetime   # script import

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UGAHBASES_DIR = os.path.join(ROOT, "lord-ugah-ai-v6", "ugahbases")

CROSSREF_PATTERN = re.compile(r'crossrefs:\s*\[(.*?)\]', re.DOTALL)

def find_markdown_files():
    """Return a list of all markdown files in Ugahbases."""
    return glob(os.path.join(UGAHBASES_DIR, "**", "*.md"), recursive=True)


def extract_crossrefs(md_path):
    """Extract crossrefs from a markdown file."""
    with open(md_path, "r") as f:
        content = f.read()
    match = CROSSREF_PATTERN.search(content)
    if not match:
        return []
    refs = match.group(1)
    # Split by comma, strip whitespace and quotes
    return [r.strip().strip('"\'') for r in refs.split(",") if r.strip()]


def validate_crossrefs():
    """Check all crossrefs and report missing/orphaned links."""
    md_files = find_markdown_files()
    all_paths = set(os.path.relpath(f, UGAHBASES_DIR) for f in md_files)
    errors = []
    for md in md_files:
        rel_md = os.path.relpath(md, UGAHBASES_DIR)
        refs = extract_crossrefs(md)
        for ref in refs:
            # Normalize reference (remove ../, etc.)
            ref_path = os.path.normpath(os.path.join(os.path.dirname(rel_md), ref))
            if not ref_path.endswith('.md'):
                ref_path += '/index.md'  # Assume directory crossref points to index.md
            if ref_path not in all_paths:
                errors.append((rel_md, ref))
    return errors


def main():
    print("[Lord-Ugah-AI-v6] Link Validator")
    errors = validate_crossrefs()
    if errors:
        print("Missing or orphaned cross-references found:")
        for src, ref in errors:
            print(f"  In {src}: {ref} not found")
    else:
        print("All cross-references are valid.")


if __name__ == "__main__":
    main() 