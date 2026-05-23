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

## Exception Handling

- Do not write empty catch blocks.
- Do not convert an exception into success without recording a typed failure,
  user-visible state, log, metric, audit event, or explicit recovery path.
- Preserve the original cause when wrapping or mapping errors.
- Rethrow, return a typed result, or surface a recoverable user state; do not
  hide the failure to make a command, test, or UI path appear successful.
- If an error is intentionally ignored, keep the scope narrow and leave a short
  reason. Ignored errors must not affect correctness, data integrity, security,
  billing, permissions, or user-visible completion.

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
