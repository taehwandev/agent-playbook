---
keyflow_id: sys_1897b4d3cb65
status: review
type: ai-generated
---

# Workflows

Workflows turn the small guidance cards into repeatable agent paths.

Use workflows when the task has multiple steps, review risk, or a handoff point.
Keep each workflow short enough to load with the relevant `common/` and
`platforms/` cards.

## Current Workflows

- `agent-task-lifecycle.md`: route any agent task from intake to report.
- `agent-handoff-continuation.md`: preserve state across interruption, resume, or handoff.
- `development-cycle.md`: complete the common build/change/verify/side-effect-audit/handoff cycle.
- `planning-research.md`: investigate, compare options, and produce an implementation plan or recommendation.
- `documentation-update.md`: create, review, or restructure docs without duplicating source guidance.
- `feature-implementation.md`: turn a request into scoped implementation and verification.
- `bugfix-debugging.md`: reproduce, fix, and verify bugs or regressions.
- `refactor-cleanup.md`: improve structure while preserving behavior.
- `release-readiness.md`: prepare release, deployment, package, or migration handoff.
- `review-and-commit.md`: review the current work, verify it, then prepare a clean commit unit.

## Rule

Workflow files should reference cards instead of copying them. If workflow text
starts repeating a common rule, move the rule into `common/` and link it here.
