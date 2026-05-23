---
keyflow_id: sys_2005f8bbf4b2
status: review
type: ai-generated
---

# Commit Review

Use when reviewing one or more commits instead of the current working tree.

## Read

- Commit message: stated intent and scope.
- Diff: actual behavior changed.
- Tests: what was added, changed, or missing.
- Related docs: requirements, service guide, repo instructions.

## Check

- Does the commit do what the message claims?
- Is each changed line traceable to the commit purpose?
- Did it mix feature, refactor, formatting, or generated churn?
- Are migrations, API contracts, permissions, or data changes reversible or documented?
- Is there a test or verification path for the changed behavior?

## Output

Lead with findings. Include commit SHA when useful. If the commit is too broad to review confidently, say what split would make it reviewable.
