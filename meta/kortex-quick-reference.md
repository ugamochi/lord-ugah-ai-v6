---
title: "Kortex Quick Reference"
created_date: 2025-06-26
modified_date: 2025-06-26
tags: [meta, prompt-engineering, kortex, quick-reference]
crossrefs: [system-architecture]
---

# Kortex Quick Reference for Ugah AI v6

Essential Kortex principles for better prompts. Keep it simple, make it work.

## The 5-Part Structure

1. **Role** - Expert identity (e.g., "senior frontend developer with React/TypeScript expertise")
2. **Task** - What you want in 1-2 sentences
3. **Specifications** - 8-15 specific guidelines
4. **Examples** - Show what you want with @ references
5. **Response Format** - How to structure the output

## Prompt Template

```
**Role:** [Expert with specific domain knowledge]
**Task:** [Clear objective]
**Requirements:**
- [Specific guideline 1]
- [Specific guideline 2]
- [etc., 8-15 total]
**Examples:** @existing-file or concrete examples
**Output:** [Explicit format requirements]
```

## Quality Standards

- **Minimum 3 examples** for complex prompts
- **2+ expertise areas** in role definition
- **8+ specific requirements** (not general "follow best practices")
- **Explicit output structure**

## V6 Integration

Already implemented in:
- Root `.cursor-rules` (Kortex-enhanced standards)
- Webflow-development ugahbase
- Templates for new prompts

Use this structure for new prompts. It works.

---

**Full analysis archived in:** `archive/deep/kortex-integration-analysis-full.md` 