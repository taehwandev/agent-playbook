---
keyflow_id: sys_60c9ad0c6826
status: draft
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
- Keychain, files, notifications, permissions, and persistence stay behind adapters.

## Check

- Can stale async results update the UI?
- What happens when the view disappears?
- Does permission denial have a user-visible state?
- Is sensitive data outside plain UserDefaults and logs?
