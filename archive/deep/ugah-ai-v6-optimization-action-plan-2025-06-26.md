# Ugah AI v6 Optimization & Reorganization Action Plan (2025-06-26)

## 1. Guiding Principles
- Prioritize modularity, maintainability, and reversibility in all changes.
- Avoid hardcoded or difficult-to-maintain solutions; favor clear structure and cross-referencing.
- Preserve all valuable, working content—define criteria for value and usage before merging or archiving.
- Document all changes and ensure every action is reversible (with backup and changelog).
- Maintain a balance between professional rigor and a friendly, approachable system identity.

## 2. Actionable Steps
- Review all prompts, docs, and meta files in v6 for redundancy, outdated content, or excessive documentation.
- Propose merges or archiving for files that are duplicative or no longer relevant, ensuring nothing valuable is lost.
- Update folder and file structure for clarity and discoverability, following the v6 folder structure proposal.
- Prepare a migration/rollback plan for any structural changes.
- Ensure all cross-references and metadata are updated and validated after changes.

## 3. Rule Change Proposals
- Add/clarify rules for defining "valuable, working content" (e.g., referenced, recently edited, not marked deprecated).
- Require a user review/approval step before destructive merges or deletions.
- Encourage concise, actionable documentation over excessive or bureaucratic notes.
- (Already implemented) Require clarity self-assessment before any operation; ask user for details if clarity <98%.

## 4. Prompt/Doc Consolidation Plan
- Identify prompts/docs that are outdated, redundant, or overly verbose.
- Propose merging similar prompts or archiving those with little or no usage.
- Move archived files to a dedicated `archive/` folder within v6 for easy retrieval.
- Maintain a changelog of all moves, merges, and removals for auditability.

## 5. Friendly Professional Tone Integration (Suggestions Only)
- Consider updating system identity and onboarding docs to reflect a balance of professionalism and approachability.
- Use clear, direct language in prompts and docs, but allow for occasional friendly, supportive notes.
- Avoid excessive formality or jargon; focus on clarity and helpfulness.
- Gather user feedback on tone preferences before making this the default.

## 6. Changelog & Rollback Note
- All changes will be logged in the v6 changelog and a migration plan will be prepared before any major edits.
- The full backup (2025-06-26) ensures all changes are reversible. 