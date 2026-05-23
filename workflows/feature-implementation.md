---
keyflow_id: sys_0086dc0e66ec
status: draft
type: ai-generated
---

# Feature Implementation Workflow

Use when implementing a new feature or meaningful behavior change.

## Read

- `common/agent-operating-skill.md`
- `common/llm-coding-discipline.md`
- `common/product-spec-to-implementation.md`
- one matching platform architecture card

## Steps

1. Restate the requested behavior and assumptions.
2. Identify the smallest implementation boundary.
3. Check repo-local instructions, existing patterns, and affected tests.
4. Implement only the requested behavior.
5. Verify with the nearest useful command or manual smoke check.
6. Report what changed, how it was verified, and any residual risk.

## Stop If

- The requirement has multiple incompatible interpretations.
- The implementation needs product policy not present in the repo.
- Verification is impossible and the risk is not acceptable to state explicitly.
