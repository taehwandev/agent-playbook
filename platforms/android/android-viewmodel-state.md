---
keyflow_id: sys_android_viewmodel_state
status: review
type: human-reviewed-needed
---

# Android ViewModel And State

Use when creating, changing, moving, or reviewing Android ViewModels, `UiState`,
`Flow`, use cases, repositories, persistence, permission state, or navigation
events.

For Compose screen/component structure, also read `android-compose-ui.md`. For
background work, also read `android-background-work.md`. For reusable extraction,
also read `../../common/reusable-code-design.md`.

## State Ownership

Use this shape unless the repo has a stricter local pattern:

```text
Route/Composable -> ViewModel -> Use Case -> Repository -> DataSource/Adapter
```

- Route/Composable collects state, sends user intent, and handles lifecycle-aware
  UI effects.
- ViewModel owns screen state, user intent handling, cancellation, and event
  output.
- Use case owns product rules and orchestration when logic is reused, risky, or
  independently testable.
- Repository owns source coordination, caching, DTO/domain mapping, and error
  normalization.
- Data sources/adapters own Room, DataStore, files, sensors, permissions,
  notifications, SDKs, and network clients.

Do not add a use case or repository only as a pass-through. Add it when it
protects a product rule, side effect, test boundary, cache boundary, or platform
API boundary.

## ViewModel Contract

ViewModels should expose one observable state stream and explicit intent methods
or typed actions:

```kotlin
data class ProfileUiState(
    val content: ProfileViewData? = null,
    val status: LoadStatus = LoadStatus.Loading,
    val permission: PermissionState = PermissionState.Unknown,
    val snackbar: SnackbarMessage? = null,
)

sealed interface ProfileAction {
    data object Retry : ProfileAction
    data object Edit : ProfileAction
    data object DismissMessage : ProfileAction
}
```

Rules:

- Prefer immutable `data class` or sealed state over scattered `MutableState`
  and nullable fields.
- Keep `MutableStateFlow` private and expose `StateFlow`.
- Use lifecycle-aware collection from UI.
- Convert DTO/domain models into UI models before state reaches Compose.
- Keep permission denied, offline, empty, loading, error, disabled, and submitted
  states representable when the flow can reach them.
- Keep one-off effects separate from persistent state. Use a typed effect stream
  or route callback for navigation, snackbar, permission launch, external
  activity, and file/share actions.

## Flow And Coroutine Rules

- Use `viewModelScope` for work owned by the ViewModel.
- Inject dispatchers, clocks, and schedulers when tests need control.
- Cancel or replace in-flight work when query, account, permission, or route
  arguments change.
- Suppress stale results from older requests.
- Use `stateIn` or `shareIn` intentionally; define initial value, sharing
  policy, and stop timeout.
- Avoid collecting infinite flows inside use cases without a clear owner.
- Map errors into user-visible state or typed domain errors before UI.

## Persistence And Cache

- Room entities, DataStore schemas, files, and cache records should not leak
  directly into UI state.
- Version persisted data that can survive app upgrades.
- Define cleanup on logout, account switch, org/workspace change, permission
  revoke, and downgrade.
- Define invalidation for offline caches and remote refresh.
- Handle corrupt DataStore/files, failed migrations, missing permissions, and
  storage quota or disk errors.

## Navigation And Events

- Parse navigation arguments at the route boundary and pass typed values to the
  ViewModel.
- Do not hide route decisions in random booleans inside `UiState`.
- Navigation, snackbar, permission prompt, file picker, and external app launch
  should be explicit outputs from the state owner.
- Events must not replay after rotation unless replay is the intended behavior.

## Tests

Choose the closest checks configured in the repo:

- ViewModel tests for state transitions, retry, submit, permission denied,
  stale result suppression, and one-off effects.
- Use case tests for product rules, auth/tenant/billing policy, and side-effect
  orchestration.
- Repository tests for cache, mapper, error, migration, and source selection.
- Coroutine tests with injected dispatchers and deterministic clocks.
- Compose UI tests for lifecycle collection, rendering state, and emitted
  actions.

Review the final diff for direct data-source calls from UI, public mutable
state, impossible UI state combinations, replaying one-off events, missing
logout cleanup, and untested coroutine timing.
