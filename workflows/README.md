---
keyflow_id: sys_1897b4d3cb65
status: draft
type: ai-generated
---

# Workflows

Workflows turn the small guidance cards into repeatable agent paths.

Use workflows when the task has multiple steps, review risk, or a handoff point.
Keep each workflow short enough to load with the relevant `common/` and
`platforms/` cards.

## Current Workflows

- `feature-implementation.md`: turn a request into scoped implementation and verification.
- `review-and-commit.md`: review the current work, verify it, then prepare a clean commit unit.

## Rule

Workflow files should reference cards instead of copying them. If workflow text
starts repeating a common rule, move the rule into `common/` and link it here.
