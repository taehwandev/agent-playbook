---
keyflow_id: sys_verification_policy
status: draft
type: human-reviewed-needed
---

# Verification Policy

Work is not done just because files changed. Completion requires evidence or a
clear explanation of why evidence could not be collected.

## Verification Order

Prefer the smallest reliable check first:

```text
format / static check
typecheck / compile
unit test
focused integration test
UI or end-to-end test
manual smoke test
package / release check
```

Run broader checks when the change touches shared models, cross-module
contracts, persistence, auth, permissions, payments, filesystem, network,
platform integration, or release packaging.

## Evidence To Preserve

In the final response, include:

- exact command names for automated checks
- whether each check passed, failed, or was not run
- a short reason for skipped checks
- residual risk when verification is partial

## When Tests Are Missing

If no useful test exists:

- add a focused test when the change is risky enough
- otherwise perform a manual smoke check
- state that automated coverage is missing

## Do Not Overclaim

Do not say a feature is complete when:

- behavior is mocked or placeholder-only
- the user path was not exercised
- persistence or sync-back was not verified
- auth, permissions, or data loss cases are untested
- only formatting or compilation was checked for a behavioral change
