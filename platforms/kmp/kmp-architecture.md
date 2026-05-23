---
keyflow_id: sys_kmp_architecture
status: review
type: human-reviewed-needed
---

# KMP Architecture

Use for Kotlin Multiplatform, Compose Multiplatform, shared Kotlin modules,
Gradle source sets, `expect`/`actual` boundaries, and shared mobile/desktop
application logic.

For Compose Multiplatform UI, also use `kmp-compose-ui.md`. For state,
coroutines, repositories, persistence, and data flow, also use
`kmp-state-data.md`. For platform APIs, source sets, native interop, shell,
files, clipboard, permissions, or background resources, also use
`kmp-platform-integration.md`. For target-specific shells, also load the
matching Android, iOS, or application card.

## Boundaries

```text
App Target -> Platform Shell -> Shared Presentation/UI -> Use Case
-> Repository -> Platform Adapter
```

Use source sets as ownership boundaries:

```text
commonMain    shared models, domain rules, state, pure services, shared UI
commonTest    shared behavior tests
androidMain   Android adapters, permissions, lifecycle, resources
iosMain       Apple adapters, native interop, platform services
desktopMain   desktop shell, files, process, window/system adapters
```

## Rules

- Keep `commonMain` free of target-only APIs unless the dependency explicitly
  supports every target used by the repo.
- Put platform behavior behind an injected interface or a small
  `expect`/`actual` boundary with the same contract on every target.
- Keep target entry points thin. They should wire platform services, DI,
  windows/activities/controllers, and lifecycle into shared presentation or use
  cases.
- Keep domain models free of Compose, Android, UIKit, AppKit, file-system,
  process, and credential APIs.
- Treat Gradle source-set dependencies as architecture decisions. A dependency
  that only works on one target should not leak into common source sets.
- Do not hide target gaps with silent no-op actual implementations. Return an
  explicit unsupported capability, typed failure, or disabled command state.
- Keep target-specific formatting, localization, permissions, filesystem paths,
  and resource lookup in target adapters or UI mapping layers.

## Refactor Signals

- `commonMain` imports Android, desktop, iOS, JVM-only, or native APIs without a
  deliberate source-set boundary.
- A target app entry point owns business rules instead of wiring shared
  components.
- Shared code branches on target names instead of using a capability or adapter.
- Actual implementations behave differently without the contract naming that
  difference.
- A shared module depends on platform UI or storage just to reach a convenience
  API.

## Verification

- Run the narrowest compile/test task for every affected target or state why a
  target cannot be checked.
- Add shared tests in `commonTest` for platform-neutral behavior.
- Add platform tests or smoke checks for actual implementations, permissions,
  files, shell/process behavior, lifecycle, and resource cleanup.
- Review the final diff for accidental target-only imports in shared source
  sets and for no-op actuals that mask unsupported behavior.
