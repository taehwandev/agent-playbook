---
keyflow_id: sys_state_modeling
status: review
type: human-reviewed-needed
---

# State Modeling

Use when designing or reviewing UI state, application state, domain state,
async state, one-off effects, reducers, stores, ViewModels, hooks, or state
machines.

State design should make impossible states hard to represent.

## State Kinds

Separate these kinds of state:

- Persistent state: can survive refresh, process recreation, sync, or storage.
- Screen/UI state: what the user can currently see or interact with.
- Derived state: computed from source state and cheap to recompute.
- Draft state: local in-progress user input.
- Effect/event: one-time command such as navigation, toast, file picker,
  permission prompt, external launch, or analytics dispatch.
- Cache state: stale/fresh data with invalidation rules.

Do not store the same fact in multiple places without naming the source of truth.

## Explicit Async States

Model async surfaces explicitly:

```text
idle -> loading -> content -> empty -> error -> refreshing
permission denied -> offline -> conflict -> partial
```

Use only the states the feature needs, but make them typed. Avoid combinations
such as `isLoading`, `error`, `data`, `isEmpty`, and `isOffline` that can produce
contradictory states.

## Effects

One-off effects are not persistent state.

- Navigation, toast/snackbar, focus request, permission launch, external app
  launch, download, and analytics dispatch should be modeled as commands or
  effects.
- Effects should be consumed once and should not replay accidentally after
  rotation, refresh, retry, or process recreation.
- If an effect must be recoverable, persist the underlying intent instead of the
  UI event.

## Ownership

- UI owns transient interaction state that only affects rendering.
- State holder owns screen state, async lifecycle, and effect emission.
- Domain owns product rules and mutation decisions.
- Data/cache owns freshness, invalidation, pagination cursors, and persistence.
- Platform adapter owns OS/runtime state such as permissions, network reachability,
  clipboard, filesystem handles, and app lifecycle.

## Naming

Prefer names that state the boundary:

```text
FooUiState
FooUiAction
FooUiEffect
FooDomainState
FooCacheState
FooDraft
```

Use repo-local names first, but keep persistent state, visible state, and
one-time effects distinguishable.

## Review Checklist

- What is the source of truth?
- Can loading and error exist with stale content, or are they exclusive?
- What happens on retry, refresh, logout, permission change, or account switch?
- Can the state survive lifecycle or process recreation when required?
- Are one-off effects separated from durable state?
- Are invalid, missing, stale, duplicated, lower-bound, and upper-bound cases
  represented or rejected?

## Verification

Verify state transitions closest to the owner:

- reducer/store/ViewModel/hook tests for state transitions
- mapper tests for domain-to-UI state
- lifecycle or refresh tests for stale and retry behavior
- UI/component tests for visible states and emitted actions
