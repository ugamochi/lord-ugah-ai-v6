# Lord-Ugah-AI-v6 Onboarding & Integration Workflow

Welcome to Lord-Ugah-AI-v6! This guide will help you get started, maintain, and expand the system.

## 1. Adding a New Ugahbase
- Run `scripts/ugahbase_creator.py` and follow the prompt.
- The new Ugahbase will be created from the template and registered automatically.
- Update cross-references in related Ugahbases as needed.

## 2. Adding Notes
- Use `templates/note-template.md` as a starting point for new notes.
- Place notes in the appropriate Ugahbase folder.
- Fill in metadata (title, created, updated, tags, crossrefs, etc.).

## 3. Adding or Evolving Templates
- To add a new note or Ugahbase template, place it in the `templates/` directory.
- To evolve templates, analyze which are most used (future automation planned).

## 4. Maintaining Cross-References
- Use the `crossrefs` field in YAML frontmatter to link related notes/Ugahbases.
- Run `scripts/link_validator.py` to check for missing or broken cross-references.
- See `meta/cross-reference-map.md` for guidelines.

## 5. Expanding the System
- Use `scripts/expansion_helper.py` for suggestions on new Ugahbases and connections.
- Add new domains by creating new Ugahbases and updating cross-references.

## 6. Meta-System Maintenance
- Run `scripts/meta_updater.py` to update the Ugahbase registry and expansion log.
- Run `scripts/performance_monitor.py` to check system health and performance.

## 7. Further Help
- See `README.md` for a quick overview.
- See `v6-build.md` and `v6-enhance-1.md` for system philosophy and enhancement plans.

---

**Tip:** Use this file as a quick reference for onboarding and integration tasks. Update as the system evolves. 