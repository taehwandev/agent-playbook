---
keyflow_id: sys_38c7a50e835b
status: review
type: ai-generated
---

# Server Data And Jobs

Use when touching database, migrations, transactions, queues, webhooks, or background jobs.

## Defaults

- Tenant and permission filters are mandatory, not optional call-site details.
- Transactions wrap multi-write invariants.
- Migrations account for locks, backfills, rollback, and old app versions.
- Jobs and webhooks are idempotent when retry is possible.
- Queues define retry policy, backoff, timeout, priority, and dead-letter or
  poison-message handling when failures can persist.
- Scheduled jobs define ownership, overlap/concurrency policy, lock behavior,
  clock source, timezone behavior, catch-up/backfill, and missed-run recovery.
- Multi-step jobs define compensation, replay, or reconciliation for partial
  success after database writes or external side effects.
- External clients map errors before returning to API callers.
- Logs contain correlation detail, not secrets or personal data.

## Check

- Can this run twice safely?
- What happens halfway through the write?
- Is cross-tenant access impossible by construction?
- Is rollback or forward fix documented?
- What prevents overlapping scheduled runs or duplicate workers?
- What compensates partial success after an external side effect?
- What observes stuck, delayed, duplicated, or dead-lettered work?

## Tests

Cover transaction rollback, idempotent retry, duplicate webhook delivery, job
timeout, permanent failure, dead-letter behavior, overlapping schedule
prevention, timezone/catch-up behavior, partial-failure compensation, and
old/new app version compatibility when applicable.
