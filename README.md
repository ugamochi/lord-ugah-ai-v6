# Lord-Ugah-AI-v6

Personal knowledge management system scaffold. See v6-build.md for full architecture, rules, and expansion philosophy.

## How to Use

1. **Initialize the System**
   - Run `scripts/initialize.py` to ensure all folders are present.

2. **Create a New Ugahbase**
   - Run `scripts/ugahbase_creator.py` and follow the prompt.
   - New Ugahbases are generated from the template and registered automatically.

3. **Add Notes**
   - Use `templates/note-template.md` as a starting point for new notes.
   - Place notes in the appropriate Ugahbase folder.

4. **Cross-Reference Notes**
   - Use the `crossrefs` field in YAML frontmatter to link related notes/Ugahbases.
   - See `meta/cross-reference-map.md` for guidelines.

5. **Validate and Expand**
   - Run `scripts/link_validator.py` to check for missing or broken cross-references.
   - Run `scripts/expansion_helper.py` for suggestions on new Ugahbases and connections.

6. **Meta-System**
   - The `meta/` folder tracks Ugahbase registry, expansion log, and cross-reference map.

For more, see the full system prompt in `v6-build.md`.

## Running Scripts: Best Practice

All scripts in `scripts/` use a dual import pattern for maximum flexibility and maintainability. You can run them in two ways:

**Recommended (Best Practice):**

    python -m lord-ugah-ai-v6.scripts.ugahbase_creator
    python -m lord-ugah-ai-v6.scripts.link_validator

This treats `scripts/` as a proper Python package and avoids import errors.

**Alternative (for quick testing):**

    python lord-ugah-ai-v6/scripts/ugahbase_creator.py
    python lord-ugah-ai-v6/scripts/link_validator.py

The scripts will automatically detect how they are run and import dependencies correctly.

**Why this pattern?**
- Ensures scripts are modular, maintainable, and testable
- Avoids hardcoded sys.path hacks or fragile workarounds
- Follows Python best practices for package and script design

See comments in each script for details. 