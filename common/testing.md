---
keyflow_id: sys_4d909f6cacff
status: draft
type: ai-generated
---

# Testing Principles

Test behavior users or other code depend on.

## Prioritize

1. Product rules and permissions
2. Data mapping and API contracts
3. State transitions and errors
4. Critical user flows
5. Bug regressions

## Cover

- success
- loading
- empty
- permission denied
- validation error
- API/network error

## Prefer

- Unit tests for pure policy, mapper, validator logic.
- State tests for ViewModel, hook, reducer, store.
- UI tests by visible text, role, label, and interaction.
- E2E only for high-value cross-boundary flows.

## Report

If a test cannot run, state the command skipped, why, and residual risk.
