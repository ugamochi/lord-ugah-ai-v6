"""
Lord-Ugah-AI-v6 Expansion Helper Script

This script analyzes Ugahbases for content gaps and connection opportunities.
It suggests new Ugahbases and cross-references based on tags and usage patterns.
"""
import os
import re
from glob import glob
from collections import Counter, defaultdict
from scripts.utils import get_current_datetime
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UGAHBASES_DIR = os.path.join(ROOT, "lord-ugah-ai-v6", "ugahbases")

TAGS_PATTERN = re.compile(r'tags:\s*\[(.*?)\]', re.DOTALL)
CROSSREF_PATTERN = re.compile(r'crossrefs:\s*\[(.*?)\]', re.DOTALL)

def find_markdown_files():
    """Return a list of all markdown files in Ugahbases."""
    return glob(os.path.join(UGAHBASES_DIR, "**", "*.md"), recursive=True)


def extract_tags(md_path):
    """Extract tags from a markdown file."""
    with open(md_path, "r") as f:
        content = f.read()
    match = TAGS_PATTERN.search(content)
    if not match:
        return []
    tags = match.group(1)
    return [t.strip().strip('"\'') for t in tags.split(",") if t.strip()]


def extract_crossrefs(md_path):
    """Extract crossrefs from a markdown file."""
    with open(md_path, "r") as f:
        content = f.read()
    match = CROSSREF_PATTERN.search(content)
    if not match:
        return []
    refs = match.group(1)
    return [r.strip().strip('"\'') for r in refs.split(",") if r.strip()]


def analyze_gaps_and_suggestions():
    """Analyze Ugahbases for content gaps and suggest new Ugahbases/crossrefs."""
    md_files = find_markdown_files()
    tag_counter = Counter()
    crossref_counter = Counter()
    tag_to_files = defaultdict(list)
    crossref_to_files = defaultdict(list)
    for md in md_files:
        tags = extract_tags(md)
        crossrefs = extract_crossrefs(md)
        for tag in tags:
            tag_counter[tag] += 1
            tag_to_files[tag].append(md)
        for ref in crossrefs:
            crossref_counter[ref] += 1
            crossref_to_files[ref].append(md)
    # Suggest tags that are common but not represented as Ugahbases
    existing_ugahbases = set(os.listdir(UGAHBASES_DIR))
    suggested_ugahbases = [tag for tag, count in tag_counter.items() if tag not in existing_ugahbases and count > 1]
    # Suggest crossrefs that are common but not reciprocated
    orphan_crossrefs = [ref for ref, count in crossref_counter.items() if count > 1 and ref not in tag_counter]
    return suggested_ugahbases, orphan_crossrefs


def main():
    print("[Lord-Ugah-AI-v6] Expansion Helper")
    suggested_ugahbases, orphan_crossrefs = analyze_gaps_and_suggestions()
    if suggested_ugahbases:
        print("Suggested new Ugahbases (based on common tags):")
        for tag in suggested_ugahbases:
            print(f"  - {tag}")
    else:
        print("No new Ugahbases suggested.")
    if orphan_crossrefs:
        print("Orphaned cross-references (not reciprocated or missing as tags):")
        for ref in orphan_crossrefs:
            print(f"  - {ref}")
    else:
        print("No orphaned cross-references found.")


if __name__ == "__main__":
    main() 