---
keyflow_id: sys_android_module_structure
status: review
type: human-reviewed-needed
---

# Android Module Structure

Use when deciding Android Gradle modules, package layout, `api`/implementation
splits, feature ownership, build convention plugins, or where new code should
live.

This card follows current Android guidance: modularization is a tool for
maintainability, build isolation, visibility control, and replaceable
boundaries; it is not mandatory ceremony for every feature.

References:

- Android app modularization:
  `https://developer.android.com/topic/modularization`
- Android app architecture:
  `https://developer.android.com/topic/architecture`
- Android UI layer:
  `https://developer.android.com/topic/architecture/ui-layer`

## Default Rule

Start with the smallest owner boundary that works:

```text
package/private file -> feature package -> feature module -> api/impl pair
-> shared core module -> public SDK-like contract
```

Use a single package or module unless a real caller, dependency, build,
navigation, testing, or ownership boundary needs a split. Multi-module apps need
clear dependency direction; otherwise the extra modules only move complexity into
Gradle.

## Module Families

Use repo-local names first. A large Android app commonly separates these module
families:

| Family | Owns | Must Not Own |
| --- | --- | --- |
| `app` | Application class, build types/flavors, app-level DI graph, startup, top-level navigation wiring. | Feature implementation, repository implementation details, shared UI primitives. |
| `build-logic` | Convention plugins, common Android/Kotlin/Compose/test settings, dependency bundles. | Product behavior or runtime code. |
| `core` | Stable platform/runtime primitives such as dispatchers, router contracts, lifecycle helpers, security adapters, resource providers, test utilities. | Feature product policy or screen-specific UI. |
| `core-ui` / `core-app` | Design system, resources, permission helpers, network shell, toast/dialog primitives, app UI infrastructure. | Feature-specific copy, routes, analytics, or repository calls. |
| `data` / `core-data` | Repository contracts, repository implementations, local/remote data sources, DTO mapping, DataStore/Room/cache ownership. | Compose UI, navigation decisions, screen state. |
| `domain` | Optional use cases and product policies reused across screens or risky enough to test independently. | Pass-through wrappers around one repository call. |
| `feature-api` | Navigation contracts, public entrypoints, route data, events, small caller-facing models. | Screens, ViewModels, repository implementations, DI bindings with heavy dependencies. |
| `feature` / `feature-impl` | Route holders, stateless screens, ViewModels, feature-local components, UI mappers, feature DI. | Shared design primitives or cross-feature data contracts. |
| `feature-common` / `holder` | Reused product UI or workflow holders with a named owner and stable caller contract. | Dumping ground for unrelated screen fragments. |
| `dev` / `testing` / `assertion` | Dev-only screens, fakes, assertions, fixture builders, test helpers. | Production-only behavior that callers need at runtime. |

If the repo already uses convention plugins, apply the nearest plugin instead of
copying dependency blocks by hand. If no convention exists, update or add one
only when at least two modules will share the same setup.

## Split Decision

Choose a single feature module when:

- only one screen or flow owns the code
- no other module needs to compile against the contract
- navigation is local or can be wired from the current module
- implementation dependencies are acceptable to callers
- the boundary is still changing quickly

Choose a `feature-api` plus `feature` implementation pair when:

- another feature, holder, app module, or navigation graph must reference the
  destination without depending on implementation
- route data, activity/fragment/Compose entrypoints, or public events cross the
  feature boundary
- the implementation has heavy dependencies such as camera, webview, ads,
  billing, SDK integrations, or large UI libraries
- the split prevents circular dependencies
- a fake, dev, paid/free, flavor-specific, or replaceable implementation is
  realistic

Choose a repository `api` plus implementation pair when:

- feature modules need a repository interface and stable entities
- DTOs, Retrofit/Room/DataStore, SDK clients, or cache implementations should
  not leak into callers
- test modules need an assertion or fake implementation
- multiple repository implementations can exist for flavors, dev tools, or
  platform-specific behavior

Do not create `api` modules that contain only one unused interface and no caller
that benefits from avoiding the implementation dependency.

## Dependency Direction

Keep dependencies acyclic and predictable:

```text
app
  -> feature-api and selected feature implementations
feature implementation
  -> own feature-api, design system, core utilities, repository-api, domain
feature-api
  -> small route/data contracts and stable core contracts only
repository implementation
  -> repository-api, network/local data sources, mappers, config
repository-api
  -> stable entities and repository interfaces only
core/designsystem
  -> platform primitives, resources, tokens, reusable UI contracts
```

Forbidden edges:

- `feature-api -> feature implementation`
- `repository-api -> repository implementation`
- `repository -> feature`
- `core/designsystem -> feature`
- `domain -> UI, Compose, Android framework UI types, DTO transport models`
- `app -> concrete repository internals` except app-level DI binding when the
  repo intentionally centralizes bindings there

## Feature Package Layout

Inside a feature implementation module, prefer packages that reveal behavior and
dependency direction:

```text
<feature>/
  <Feature>Route.kt          ViewModel/lifecycle/navigation/effect wiring
  <Feature>ViewModel.kt      screen state owner
  model/                     UiState, UiAction, UiEffect, UI display models
  compose/ or ui/            stateless screen composables
  compose/component/         feature-local components
  preview/                   PreviewParameterProvider and sample states
  convert/ or mapper/        domain/repository -> UI model mapping
  di/                        feature-local bindings
  navigation/                local graph or route registration when needed
```

For small screens, keeping `Route`, `Screen`, `UiState`, and preview provider in
one package is fine. Split packages when each area has a separate owner, many
files, or tests.

## Repository Package Layout

Inside a repository implementation module, keep API contracts and transport
details separate:

```text
repository-<name>-api/
  <Name>Repository.kt        caller-facing interface
  model/                     stable entities returned to domain/UI

repository-<name>/
  <Name>RepositoryImpl.kt    source coordination and error normalization
  <Name>Api.kt               Retrofit or remote source contract
  local/                     Room/DataStore/file source if present
  model/                     request/response DTOs
  mapper/ or convert/        DTO/cache -> entity mapping
  di/                        implementation bindings
```

Repository entities should be stable for callers. DTOs, request bodies,
response wrappers, database rows, SDK models, and generated network models stay
inside implementation packages unless the repo explicitly treats them as public
contracts.

## Shared UI And Holder Modules

Create a shared UI, holder, or feature-common module only when it has a stable
caller contract and repeated use:

- Use design-system modules for domain-free primitives, tokens, typography,
  buttons, list rows, dialogs, sheets, and accessibility contracts.
- Use feature-common modules for product UI patterns shared by several feature
  owners.
- Use holder modules for reusable workflow entrypoints or embedded surfaces that
  own their own state/effects and have a clear lifecycle.
- Keep analytics labels, permission policy, route decisions, and repository
  calls in the caller or holder state owner, not in a leaf component.

If a shared module needs many feature flags, product-specific callbacks, or a
full screen `UiState`, keep the code feature-local instead.

## Migration Strategy

When modernizing an old Android feature:

1. Record the current owner boundary and imports before moving files.
2. Extract stable contracts first: route data, repository interface, public
   entities, or UI component API.
3. Compile or typecheck the contract boundary before moving implementation.
4. Move implementation behind the contract in the smallest reviewable slice.
5. Add or update tests/previews for the moved boundary.
6. Remove only old code that is no longer referenced.

Do not combine broad module moves with behavior changes unless the behavior
change is necessary to make the split correct.

## Review Checklist

- Is this package/module the lowest boundary that protects the real owner?
- Does each `api` module have at least one caller that should avoid the
  implementation dependency?
- Are DTOs, SDK models, database rows, and Android framework objects kept out of
  stable feature/domain contracts?
- Can a feature implementation depend on repository APIs without importing
  repository internals?
- Are design-system modules free of product routes, analytics, permissions, and
  repository calls?
- Did the change update convention plugins instead of duplicating Gradle setup
  across modules?
- Are previews, ViewModel tests, repository tests, or import-direction checks
  covering the new boundary?
