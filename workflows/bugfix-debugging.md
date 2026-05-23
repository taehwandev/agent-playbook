---
keyflow_id: sys_bugfix_debugging_workflow
status: review
type: human-reviewed-needed
---

# Bugfix Debugging Workflow

Use when investigating a bug, regression, failing test, flaky behavior, or
production-like failure.

## Read

- `common/agent-operating-skill.md`
- `common/testing.md`
- `common/verification-policy.md`
- `common/observability-error-handling.md`
- matching platform architecture or review card from `index.md`
- security, persistence, API contract, or product-pattern cards when affected

## Steps

1. Reproduce or capture the failure with the smallest reliable command, log, or manual path.
2. Define expected versus actual behavior and the user or system impact.
3. Inspect the nearest ownership boundary before changing code.
4. Fix the cause, not only the symptom, with the smallest behavior-preserving scope.
5. Add or adjust logs, metrics, diagnostics, or user-visible error handling when
   the failure would otherwise be hard to detect or support.
6. Add or update a focused regression check when practical.
7. Re-run the failing check and any nearby checks that prove the affected boundary.
8. Report reproduction, root cause, changed behavior, observability impact,
   verification, and remaining risk.

## Stop If

- The failure cannot be reproduced and no reliable evidence points to a cause.
- The likely fix crosses auth, billing, data loss, migration, or release boundaries without enough context.
- The bug report conflicts with documented product behavior.
