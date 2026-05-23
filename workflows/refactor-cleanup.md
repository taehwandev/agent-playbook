---
keyflow_id: sys_refactor_cleanup_workflow
status: review
type: human-reviewed-needed
---

# Refactor Cleanup Workflow

Use when behavior should stay the same and the goal is structure, naming,
ownership, deletion, or maintainability.

## Read

- `common/refactoring.md`
- `common/code-conventions.md`
- `common/change-size-policy.md`
- `common/testing.md`
- matching platform architecture card from `index.md`
- generated-files or dependency policy when those files change

## Steps

1. Identify the current behavior and the next change that the refactor should make easier.
2. Choose one ownership boundary: UI, state, domain, data, platform, contract, or test.
3. Make the smallest move, rename, extraction, deletion, or adapter cleanup that improves that boundary.
4. Avoid changing product behavior, formatting unrelated files, or mixing dependency updates.
5. Verify behavior with the nearest existing check or a focused smoke path.
6. Report the preserved behavior, structural change, verification, and any follow-up left separate.

## Stop If

- The refactor needs product behavior changes to make sense.
- The diff is mostly mechanical churn that obscures the behavior boundary.
- No verification exists and the touched surface is risky enough to need one first.
