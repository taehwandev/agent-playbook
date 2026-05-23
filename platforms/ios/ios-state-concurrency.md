---
keyflow_id: sys_60c9ad0c6826
status: review
type: ai-generated
---

# iOS State And Concurrency

Use when touching SwiftUI/UIKit state, navigation, async work, or platform permissions.

## Defaults

- View owns only local presentation state.
- ViewModel or observable state owns loading, empty, error, and permission states.
- Navigation state is modeled, not hidden in side effects.
- Async work has visible ownership, cancellation, and error handling.
- UI updates respect actor boundaries.
- Long-running tasks define cancellation on disappear, logout, account switch,
  and permission changes.
- Persisted state defines migration, corruption, and app-upgrade behavior.
- Keychain, files, notifications, permissions, and persistence stay behind adapters.

## Check

- Can stale async results update the UI?
- What happens when the view disappears?
- What cancels or restarts work after logout, account switch, app backgrounding,
  or process termination?
- Does permission denial have a user-visible state?
- Is sensitive data outside plain UserDefaults and logs?
- Are Task, async sequence, Combine, and observation lifetimes chosen
  intentionally?

## Tests

Cover cancellation, stale result suppression, permission denial, persistence
migration, process relaunch, and actor-boundary behavior when applicable.
