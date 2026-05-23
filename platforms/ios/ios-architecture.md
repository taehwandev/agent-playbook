---
keyflow_id: sys_e5ada2ab6483
status: draft
type: ai-generated
---

# iOS Architecture

Use for SwiftUI/UIKit app structure, state, navigation, and async work.

For navigation, async work, persistence, permissions, or actor boundaries, also use `ios-state-concurrency.md`.

## Boundaries

```text
View/ViewController -> ViewModel/State -> Use Case -> Repository/Client -> Platform Adapter
```

## Rules

- View renders state and sends intent.
- Model loading, empty, error, permission states explicitly.
- Keep async task ownership and cancellation visible.
- Keep UI updates on the correct actor boundary.
- Wrap API, persistence, keychain, file, notification, permission APIs.
- Keep DTOs out of Views when they carry transport details.

## Refactor Signals

- SwiftUI body owns side effects and business rules.
- ViewModel exposes raw API DTOs.
- Permission checks repeat in Views.
- ViewController owns UI, API, and state transformation together.
