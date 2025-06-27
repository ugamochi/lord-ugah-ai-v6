---
title: "Simple Workflows"
created_date: 2025-06-26
modified_date: 2025-06-26
tags: [workflows, checklists, simplicity]
---

# Simple Workflows

Quick checklists for common tasks. No overthinking.

## Adding a New Ugahbase

□ Run `python scripts/ugahbase_creator.py`  
□ Enter name (kebab-case like `machine-learning`)  
□ Edit the `.cursor-rules` file for domain-specific rules  
□ Create your first note using the starter template  

Done.

## Adding a Note

□ Copy `templates/note-template.md`  
□ Place in appropriate ugahbase folder  
□ Fill out the YAML frontmatter (title, tags, crossrefs)  
□ Write your content  

Done.

## System Maintenance (Monthly)

□ Run `python scripts/link_validator.py` - fix any broken links  
□ Run `python scripts/meta_updater.py` - update registry  
□ Clean up any unused files  
□ Archive outdated content to `archive/deep/`  

Done.

## Version Control

□ Follow the [Git Sync Checklist](git-sync-checklist.md)  
□ Review changes with `git status` before committing  

Done.

## When System Feels Bloated

□ Use `@meta/ugah-ai-bloat-remover-prompt-2025-06-26.md`  
□ Delete anything that sounds like enterprise software  
□ Keep only what you actually use  
□ Archive the rest  

Done.

---

**Philosophy**: If it needs more than 4 steps, it's too complex. 