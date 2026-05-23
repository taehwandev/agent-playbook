---
keyflow_id: sys_aea75f7837ca
status: review
type: ai-generated
---

# Android State And Data

Use when touching Compose state, ViewModel, Flow, repository, persistence, or permissions.

For detailed ViewModel, `UiState`, Flow, repository, use case, persistence, and
one-off event implementation rules, also use `android-viewmodel-state.md`.

## Defaults

- Composable renders state and sends events.
- ViewModel owns durable UI state and lifecycle-aware work.
- Use sealed/state models for loading, empty, error, permission denied.
- Separate one-off events from persistent state.
- Repository owns data source coordination and error mapping.
- Room, DataStore, files, permissions, notifications stay behind adapters.
- Inject dispatchers or schedulers for coroutine tests.
- Use lifecycle-aware collection for UI-observed Flow.
- Version persisted data that can survive app upgrades.

## Check

- Does collection respect lifecycle?
- Can process recreation restore needed state?
- Are navigation args parsed away from business rules?
- Does logout, account switch, or permission change clear cached state?
- Are Room migrations, DataStore changes, and offline cache invalidation covered?
- Are StateFlow, SharedFlow, Channel, and one-off events chosen intentionally?
