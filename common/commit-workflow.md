---
keyflow_id: sys_f20b4c0c0d16
status: draft
type: ai-generated
---

# Commit Workflow

Use before creating commits, regardless of git client, IDE, CLI, or AI tool.

## Commit Unit

- One commit should carry one reviewable intent.
- Do not mix feature, refactor, formatting, generated files, and dependency churn unless they are inseparable.
- Every changed line should trace to the commit purpose.
- If a commit needs a long explanation, consider splitting it first.

## Before Commit

- Check repo-local commit rules first.
- Inspect the final diff, not memory of the work.
- Remove only unused code created by this change.
- Run the nearest useful verification, or record why it was skipped.
- Do not include secrets, local paths, debug logs, or temporary artifacts.

## Message

Prefer:

```text
type(scope): what changed

Why:
- reason or product context

Verified:
- command or manual check
```

Keep the subject about behavior or structure, not effort. Mention migrations, breaking changes, security impact, and follow-up work explicitly.
