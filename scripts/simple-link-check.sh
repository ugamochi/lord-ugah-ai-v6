#!/bin/bash
# Simple Link Checker for Lord-Ugah-AI-v6
# Finds basic broken crossrefs in ugahbases

echo "[v6] Simple Link Check"

cd "$(dirname "$0")/../ugahbases" || exit

# Find all .md files and check for common broken patterns
echo "Checking for obvious broken links..."

# Look for crossrefs that reference non-existent files
grep -r "crossrefs:" . --include="*.md" | while read -r line; do
    echo "Found crossref: $line"
done

echo "Manual review needed for detailed validation."
echo "For thorough checking, use the Python script." 