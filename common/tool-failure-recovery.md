---
keyflow_id: sys_tool_failure_recovery
status: review
type: human-reviewed-needed
---

# Tool Failure Recovery

Use when a build, test, lint, typecheck, formatter, package, script, or local
tool command fails.

## Default

Do not blindly retry, broadly revert, or silence the failure. Read the actual
stdout/stderr, identify the failing boundary, and make the smallest correction
that addresses the observed error.

## Diagnose

Capture the useful facts before editing:

- command, working directory, and exit code
- first failing file and line number, when present
- error code, exception type, test name, or assertion message
- whether the failure is from code, config, missing dependency, environment,
  sandbox, permissions, network, timeout, or flaky external state
- whether the failing area was touched by the current task

If output is truncated, rerun the narrowest command that exposes the relevant
error. Do not paste secret values from logs.

## Correct

- Fix the smallest relevant code, config, test, fixture, or docs issue.
- Preserve unrelated user changes and unrelated failures.
- Rerun the narrowest command that proves the correction.
- Escalate or ask only when the failure requires network, credentials,
  destructive cleanup, external state, or a product decision.
- If the same command fails twice for different reasons, repeat diagnosis from
  the new output instead of assuming the old cause.

## Do Not

- Repeat the same failing command more than twice without a changed hypothesis.
- Delete tests, loosen assertions, or bypass lint rules only to make checks pass.
- Catch and ignore runtime errors to hide a failing path.
- Roll back broad files when a line-level correction is available.
- Mark verification as passed when the command failed for environment reasons.

## Report

For unresolved failures, report:

```text
Command:
Failure:
Likely cause:
What was changed:
Next action or blocker:
Residual risk:
```
