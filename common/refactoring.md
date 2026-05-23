---
keyflow_id: sys_f6cb537c3133
status: draft
type: ai-generated
---

# Refactoring Playbook

Use when behavior should stay the same and structure should improve.

## Order

1. Identify current behavior.
2. Find the responsibility boundary.
3. Rename or extract the smallest useful unit.
4. Move code only after ownership is clear.
5. Run the nearest verification.

## Good Targets

- UI file owns too much state calculation.
- API/DTO mapping leaks into UI.
- Permission checks repeat inline.
- Platform SDK calls appear across screens.

## Avoid

- Big file moves without behavior checks.
- New abstractions before real duplication.
- Mixing feature change, formatting churn, and refactor.

## Done

Next change location is clearer, failure flow is easier to see, and tests or smoke checks still pass.
