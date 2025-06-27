# End-of-Chat Analysis Prompt

**Created:** 2025-06-24  
**Purpose:** Generate comprehensive system improvement suggestions after development sessions

---

## Prompt Template

```
You are an expert system architect analyzing our development session to improve the lord-ugah-ai-v6 prompt ecosystem. Before proceeding, check @.cursor-rules for mandatory requirements and project structure guidelines.

**Session Context:** [DESCRIBE THE MAIN TASK/PROJECT WE WORKED ON]

**Analysis Required:**
Please create a comprehensive analysis document called `[project-name]-v6-suggestions.md` with the following sections:

### 1. New Prompts to Create
- List specific prompts that would automate or improve tasks we did manually
- Include purpose, target use case, and priority level
- Focus on reusable, modular prompts following kebab-case naming

### 2. Existing Prompts to Edit
- Identify current v6 prompts that need updates based on our learnings
- Specify what improvements are needed
- Note any outdated techniques or missing best practices

### 3. .cursor-rules Updates
- Suggest new rules to add based on patterns we discovered
- Identify workflow optimizations that should be standardized
- Include accessibility, performance, or quality guidelines we applied

### 4. System Architecture Improvements
- Document any architectural decisions or patterns worth preserving
- Note integration opportunities with existing v6 functions
- Suggest folder structure or organization improvements

### 5. Knowledge Base Additions
- Capture technical insights, best practices, or solutions we developed
- Document any external research or standards we applied
- Note debugging techniques or troubleshooting approaches

**Requirements:**
- Use programmatic date insertion: `date +%Y-%m-%d`
- Follow kebab-case for all file names
- Include reusable code examples where applicable
- Maintain modular, user-focused documentation
- Consider WCAG accessibility and performance optimization guidelines
- Structure for future scalability and reusability

Generate this analysis to help evolve our prompt ecosystem and capture the valuable patterns we developed during this session.
```

---

## Usage Instructions

1. **Replace placeholders:** Update `[DESCRIBE THE MAIN TASK/PROJECT]` and `[project-name]` with session-specific details
2. **Run date command:** Always get current date with `date +%Y-%m-%d` before using
3. **Include context:** Provide brief summary of what was accomplished in the session
4. **Review .cursor-rules:** Reference current rules to avoid duplicating existing guidelines

## Example Usage

```
You are an expert system architect analyzing our development session to improve the lord-ugah-ai-v6 prompt ecosystem. Before proceeding, check @.cursor-rules for mandatory requirements and project structure guidelines.

**Session Context:** We built a comprehensive Table of Contents generator for Webflow Rich Text blocks, implementing 2025 best practices for smooth scrolling, accessibility features, and multi-ToC synchronization.

[Continue with analysis requirements...]
```

---

**Notes:**
- This prompt is designed to be modular and reusable across different development sessions
- Always update with current date and specific session context
- Can be adapted for different types of analysis (technical, creative, workflow, etc.) 