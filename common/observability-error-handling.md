---
keyflow_id: sys_observability_error_handling
status: review
type: ai-generated
---

# Observability Error Handling

Use when adding or reviewing errors, logging, diagnostics, monitoring, audit events, support traces, or user-facing failure states.

## Separate

- User-facing message
- Developer diagnostic
- Operational log
- Audit event
- Recovery action

## Rules

- Every async boundary needs a visible success, loading, and failure path.
- Do not swallow errors silently.
- User messages should explain what the user can do next.
- Logs should help debug without leaking secrets or unnecessary personal data.
- Audit events should record actor, target, action, time, and result.
- Retry needs idempotency or a clear duplicate-handling strategy.

## Error Shape

Prefer typed errors or result objects over string matching.

```text
code
status / HTTP status
message
retryable
field errors
correlation id
```

## Check

- Can support or engineering trace the failure?
- Can the user recover or understand the block?
- Is sensitive data excluded from logs and telemetry?
- Are repeated failures rate-limited or deduplicated?
