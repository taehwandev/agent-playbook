---
keyflow_id: sys_692dbba31f65
status: draft
type: ai-generated
---

# LLM Coding Discipline

Use before coding. These rules reduce common LLM mistakes. Bias toward caution over speed; use judgment for trivial tasks.

## Think First

- State assumptions when they affect implementation.
- If multiple interpretations exist, surface them.
- Ask when ambiguity changes the result.
- Push back on unnecessary scope or complexity.

## Keep It Simple

- Build only what was asked.
- No speculative features, config, flexibility, or abstractions.
- No single-use abstraction.
- If the solution feels much larger than the problem, simplify.

## Change Surgically

- Touch only lines tied to the request.
- Match existing style.
- Do not refactor adjacent code unless required.
- Remove only unused code created by your change.
- Mention unrelated dead code; do not delete it.

## Verify The Goal

Turn work into a testable goal:

```text
1. Change -> verify: check
2. Change -> verify: check
```

If success cannot be verified, name the gap before proceeding.
