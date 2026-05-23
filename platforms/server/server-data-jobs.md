---
keyflow_id: sys_38c7a50e835b
status: draft
type: ai-generated
---

# Server Data And Jobs

Use when touching database, migrations, transactions, queues, webhooks, or background jobs.

## Defaults

- Tenant and permission filters are mandatory, not optional call-site details.
- Transactions wrap multi-write invariants.
- Migrations account for locks, backfills, rollback, and old app versions.
- Jobs and webhooks are idempotent when retry is possible.
- External clients map errors before returning to API callers.
- Logs contain correlation detail, not secrets or personal data.

## Check

- Can this run twice safely?
- What happens halfway through the write?
- Is cross-tenant access impossible by construction?
- Is rollback or forward fix documented?
