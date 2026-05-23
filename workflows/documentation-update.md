---
keyflow_id: sys_documentation_update_workflow
status: review
type: human-reviewed-needed
---

# Documentation Update Workflow

Use when creating, reviewing, or restructuring docs, guides, specs, READMEs,
agent instructions, release notes, or knowledge-base pages.

## Read

- `workflows/agent-task-lifecycle.md`
- `common/code-conventions.md` for naming and clarity
- `common/project-naming.md` when names, slugs, or product identifiers appear
- `common/verification-policy.md` when links, examples, or commands can be checked
- task-specific architecture, product-pattern, security, or release cards when the docs describe those surfaces

## Steps

1. Identify the document audience, purpose, source of truth, and expected action.
2. Check existing docs for overlap before adding a new page or section.
3. Keep repo-specific commands, paths, role matrices, and domain terms in repo-local docs.
4. Link to shared cards instead of copying full guidance.
5. Verify examples, links, file paths, commands, and metadata where practical.
6. Report what changed, what was verified, and any stale or missing source material.

## Stop If

- The doc would invent product policy, commands, or architecture not present in the repo.
- The same guidance already exists and should be linked or updated instead.
- The requested doc depends on a private source that is unavailable.
