---
keyflow_id: sys_android_background_work
status: draft
type: ai-generated
---

# Android Background Work

Use when Android work touches WorkManager, foreground services, alarms, push notifications, sync, uploads, downloads, or long-running jobs.

## Rules

- Use WorkManager for deferrable durable work that must survive process death.
- Use foreground services only when user-visible ongoing work requires it.
- Model retry, cancellation, duplicate prevention, and idempotency before implementation.
- Respect Doze, battery saver, metered network, notification permission, and app standby behavior.
- Keep background work behind a use case or worker boundary, not inside Composables.
- Persist enough progress to recover after process death, but avoid storing sensitive payloads unnecessarily.

## Check

- What starts, cancels, retries, and observes this work?
- Does the user see progress, failure, and recovery actions?
- Can the job run twice without duplicate server effects?
- What happens across rotation, process death, logout, account switch, and network loss?
- Are notifications clear, permission-aware, and not leaking private content?

## Tests

Cover worker success, retryable failure, permanent failure, cancellation, duplicate enqueue policy, and auth/session changes during work when applicable.
