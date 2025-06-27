# Lord-Ugah-AI-v6

Personal knowledge management system for Ugah. Domain-based organization with AI-friendly rules.

## Quick Start

1. **Create New Ugahbase**: `python scripts/ugahbase_creator.py`
2. **Add Notes**: Use `templates/note-template.md`, place in appropriate ugahbase
3. **Cross-Reference**: Use `crossrefs` field in YAML frontmatter
4. **Validate Links**: `python scripts/link_validator.py`
5. **Update System**: `python scripts/meta_updater.py`

## Current Ugahbases
- `books` - References and learning resources
- `client-communication` - Client interaction patterns
- `music-production` - Audio creation and tools
- `system-architecture` - Technical design patterns
- `vibe-coding` - Development workflows and tools
- `webflow-development` - Webflow/web development expertise

## Running Scripts

Simple. Run them from the project root:

```bash
cd lord-ugah-ai-v6
python scripts/ugahbase_creator.py
python scripts/link_validator.py
python scripts/meta_updater.py
```

That's it.

## Configuration (Optional)

Simple `.env` file for customization:
- `UGAHBASE_ROOT_DIR` - Custom ugahbase location (default: `./ugahbases`)
- `DEBUG` - Enable debug output (`true`/`false`)

Scripts work fine with defaults. Only configure if you need custom paths. 