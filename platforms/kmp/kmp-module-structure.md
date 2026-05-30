---
keyflow_id: sys_kmp_module_structure
status: review
type: human-reviewed-needed
---

# KMP Module Structure

Use when deciding Kotlin Multiplatform shared modules, source sets, Gradle
module boundaries, umbrella frameworks, `expect`/`actual` placement, or package
layout.

This card follows current Kotlin Multiplatform guidance: start simple, use the
default hierarchy template when it fits, split shared code as it grows, and make
iOS framework consumption an explicit architecture decision.

References:

- Hierarchical project structure:
  `https://kotlinlang.org/docs/multiplatform/multiplatform-hierarchy.html`
- Project configuration:
  `https://kotlinlang.org/docs/multiplatform/multiplatform-project-configuration.html`
- Advanced project structure:
  `https://kotlinlang.org/docs/multiplatform/multiplatform-advanced-project-structure.html`

## Default Rule

Start with the smallest KMP boundary that works:

```text
package-private/internal code -> feature package -> single shared module
-> feature shared modules -> umbrella module/framework -> published library
```

A single shared module is often the right starting point. Split only when build
scale, source-set ownership, feature ownership, iOS framework shape, or
dependency leakage creates real pressure.

## Module Families

Use repo-local names first. KMP projects commonly separate these families:

| Family | Owns | Must Not Own |
| --- | --- | --- |
| Target apps | Android app, iOS app, desktop/web shell, app lifecycle, platform navigation host, DI assembly. | Shared business rules or repository implementation details duplicated per target. |
| Shared umbrella module | iOS-exported framework surface, dependency aggregation, shared DI entrypoint, stable app-facing API. | Feature implementation details that do not need iOS export. |
| Shared feature module | Feature state owners, use cases, repositories used by that feature, shared UI when Compose Multiplatform is used. | Platform-only APIs outside source-set adapters. |
| Shared core/domain module | Pure models, policies, result/error types, clocks/dispatchers contracts, reusable use cases. | Compose UI, Android/iOS framework types, database rows, network DTOs. |
| Shared data module | Repository contracts, repository implementations, cache/network coordination, DTO/entity mapping. | Target UI state or platform permission prompts. |
| Platform adapter module/source set | Android/iOS/desktop/web implementations, file/permission/secure storage/native interop adapters. | Silent no-op behavior or shared product policy. |
| Compose/design module | Shared Compose UI, theme, resources, design primitives, previews where supported. | Target lifecycle, platform SDK calls, repository internals. |
| Build logic/testing | Convention plugins, target setup, fixtures, fake adapters, test utilities. | Runtime behavior hidden from production owners. |

## Source Set Ownership

Use the default hierarchy template unless the project has a documented reason to
configure manual `dependsOn` edges.

```text
commonMain      target-neutral models, state, use cases, repository contracts
commonTest      shared state, mapper, policy, and repository contract tests
androidMain     Android adapters, lifecycle, resources, permissions
iosMain         Apple adapters, native interop, platform services
desktopMain     window, file, process, tray/menu, shortcut adapters
wasmJsMain/jsMain browser APIs and web-specific adapters
```

Rules:

- A source set may depend only on APIs available to every target it compiles to.
- Put iOS-only dependencies in `iosMain`, Android-only dependencies in
  `androidMain`, and browser-only APIs in web source sets.
- Avoid manual intermediate source sets until the default hierarchy cannot
  express the target sharing shape.
- Do not use `expect`/`actual` for large services. Prefer injected interfaces
  when the behavior needs fakes, multiple implementations, or test control.

## Split Decision

Keep one shared module when:

- the shared code is small enough to navigate and compile
- all target apps consume the same shared surface
- source-set dependencies are simple
- iOS can consume one generated framework without broad API noise
- the module boundary is still changing quickly

Split into shared feature modules when:

- feature owners need independent review and build boundaries
- Android or JVM consumers need only some shared features
- dependencies differ meaningfully by feature
- tests, generated code, or resources are becoming hard to scope
- a feature can be developed or released independently

Add an umbrella module/framework when:

- the iOS app needs a single stable framework that aggregates multiple shared
  modules
- multiple KMP frameworks would duplicate dependencies or complicate Swift
  integration
- the exported Swift surface needs curation and compatibility review

Publish modules separately only when versioning, ownership, and migration notes
are part of the workflow.

## Dependency Direction

Keep shared dependencies predictable:

```text
target app
  -> umbrella/shared feature modules
umbrella
  -> selected shared feature/core/data modules
shared feature
  -> core/domain, data contracts, platform adapter contracts, compose/design
data implementation
  -> data contracts, network/cache/local adapters, mappers
platform source sets
  -> target SDKs and actual adapter implementations
core/domain
  -> pure Kotlin contracts and policies only
```

Forbidden edges:

- `commonMain -> androidMain/iosMain/desktopMain/jsMain`
- shared core/domain -> Compose UI, Android, UIKit, AppKit, browser, DTO, or
  database-specific types
- platform adapters -> feature UI state unless that adapter is feature-local
- feature module -> another feature implementation when a contract can express
  the dependency
- actual implementation that silently succeeds when the target is unsupported

## Package Layout

Inside a shared feature module:

```text
src/commonMain/kotlin/<feature>/
  <Feature>StateHolder.kt
  <Feature>UiState.kt
  action/
  model/
  domain/
  data/
  ui/                     shared Compose UI if used
  platform/               adapter contracts
src/androidMain/kotlin/<feature>/platform/
src/iosMain/kotlin/<feature>/platform/
src/commonTest/kotlin/<feature>/
```

Inside a shared data module:

```text
repository/
  <Name>Repository.kt      caller-facing contract
  <Name>RepositoryImpl.kt  source coordination when shared
model/                    stable entities
remote/                   network DTOs and client wrappers
local/                    cache/settings/database wrappers
mapper/                   DTO/cache/native -> entity mapping
```

## Migration Strategy

When modernizing an old KMP shared module:

1. Record current targets, source sets, manual `dependsOn` edges, exported
   frameworks, and app consumers.
2. Move target-only imports out of `commonMain` before splitting modules.
3. Prefer the default hierarchy template; keep manual source sets only when the
   target sharing shape requires them.
4. Extract stable contracts and tests before moving implementation.
5. Add an umbrella module before exposing several shared modules to iOS.
6. Compile every affected target or state the target that could not be checked.

## Review Checklist

- Is the split driven by target sharing, feature ownership, dependency leakage,
  build scale, or iOS framework shape?
- Does `commonMain` compile without accidental target-only APIs?
- Are source-set dependencies inherited intentionally instead of duplicated?
- Are `expect`/`actual` boundaries small and contract-compatible?
- Does iOS consume one curated umbrella framework when multiple shared modules
  would duplicate dependencies?
- Are platform unsupported states explicit in shared state or capability models?
- Are `commonTest` and at least one target-specific check covering the new
  boundary?
