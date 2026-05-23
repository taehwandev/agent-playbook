---
keyflow_id: sys_kmp_state_data
status: review
type: human-reviewed-needed
---

# KMP State And Data

Use when touching shared Kotlin state, coroutines, `Flow`, repositories,
persistence, sync, settings, caching, or one-off effects in a Kotlin
Multiplatform project.

For platform APIs and actual implementations, also use
`kmp-platform-integration.md`. For broader state shape rules, also use
`common/state-modeling.md` and `common/error-modeling.md`.

## Defaults

- Shared state owners expose immutable UI state and explicit events.
- Model loading, content, empty, error, permission denied, offline, unsupported,
  and sync states explicitly.
- Keep one-off navigation, toast/snackbar, file picker, permission prompt, and
  window effects separate from persistent state.
- Repositories coordinate data sources and map platform or network failures into
  typed shared failures.
- Persistence, secure storage, settings, files, clocks, dispatchers, UUIDs, and
  network clients belong behind adapters when target behavior can differ.
- Inject coroutine dispatchers or schedulers when tests need deterministic
  execution.
- Keep target-specific lifecycle collection in target UI source sets. Shared
  state owners should expose streams without assuming Android lifecycle or a
  desktop window lifecycle.

## Data Boundary Rules

- Version persisted data that can survive app upgrades.
- Treat cached, migrated, imported, synced, generated, or platform-provided data
  as untrusted until validated.
- Define what happens on logout, account switch, permission revoke, target
  unsupported, and offline startup.
- Keep platform DTOs, database entities, and native interop objects out of
  shared domain models unless the repo intentionally owns that contract.
- Avoid blocking I/O on UI dispatchers. Long work needs cancellation, progress,
  timeout, and user-visible failure state.

## Check

- Can each target create the same initial state from equivalent inputs?
- Can process restart, app relaunch, window reopen, or target lifecycle changes
  restore the needed state?
- Are `StateFlow`, `SharedFlow`, `Channel`, callback, and suspend APIs chosen
  intentionally?
- Does each platform adapter map errors into the same shared failure contract?
- Do tests cover the shared state machine and at least one platform adapter path
  when adapter behavior changed?
