---
keyflow_id: sys_e01bf7495d2e
status: review
type: ai-generated
---

# Architecture Design

Use when planning architecture for a feature, module, service, or app surface.

## Method

Design from change pressure, not diagrams. First identify what changes together, what must be protected, and what needs independent testing. Then choose boundaries.

## Steps

1. Name the user or system behavior.
2. Identify state owners and data sources.
3. Separate UI, domain, data, platform, and integration responsibilities.
4. Mark risky boundaries: auth, tenant, billing, persistence, sync, jobs, external APIs.
5. Pick the smallest architecture that keeps those risks visible.
6. Define verification before implementation.

## Rules

- Keep architecture local until reuse or risk justifies shared layers.
- Prefer explicit contracts over implicit global state.
- Use adapters for platform and external systems.
- Avoid architecture that requires touching many unrelated files for one product change.
- Record tradeoffs when choosing speed over structure or structure over simplicity.

## Output

For non-trivial work, leave a short decision note: chosen shape, rejected alternative, risk, verification.
