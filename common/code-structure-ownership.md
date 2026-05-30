---
keyflow_id: sys_code_structure_ownership
status: review
type: human-reviewed-needed
---

# Code Structure And Ownership

Use when deciding file layout, package layout, module boundaries, public
contracts, `api`/`impl` splits, or where new code should live.

Structure should make ownership, dependency direction, and review scope obvious.
Do not create modules or packages just because a pattern exists elsewhere.

The default choice is local or single-module code. Split only when the split
protects a real caller-facing boundary, extension point, dependency edge, or
ownership line.

## Ownership Levels

Choose the lowest level that gives the code a clear owner:

```text
file-private -> package/internal -> feature/module -> feature-api contract
-> shared/core module -> public package/API
```

- File-private code is best for one caller and unstable details.
- Package/internal code is best for nearby collaborators with the same owner.
- Feature/module code is best for a cohesive behavior surface.
- Shared/core code is best for stable contracts used by multiple owners.
- Public package/API code needs compatibility, versioning, migration notes, and
  stronger tests.

## Module Split Choices

Most multi-module designs choose between two shapes.

## Decision Rule

Choose a single module unless the answer to at least one of these questions is
yes:

- Does another module need to compile against this contract without depending on
  the implementation?
- Does navigation, deep linking, plugin loading, dependency injection, or feature
  registration cross this boundary?
- Is this an extension point where another implementation can reasonably replace
  the current one?
- Would implementation dependencies leak heavy, platform-specific, paid, test,
  or optional dependencies to callers?
- Does the split remove a circular dependency, reduce build coupling, or let
  different owners change contract and implementation independently?

If all answers are no, keep the code local or in one module and revisit the
boundary when pressure appears.

## Modernization Drill

When modernizing an old or oversized codebase, separate structure moves from
behavior changes:

1. Inventory current imports, public exports, target/module membership,
   generated files, resources, tests, and runtime entry points.
2. Name the current owner and the intended owner before moving files.
3. Extract the smallest stable contract first: route data, component API,
   repository interface, platform adapter, use case, or typed model.
4. Compile or typecheck the contract boundary before moving implementation.
5. Move one feature, package, module, or source set at a time.
6. Keep compatibility shims only with an owner, removal condition, and test.
7. Remove old imports, duplicate exports, and dead target membership after the
   new boundary is verified.

Avoid combining broad moves with product behavior changes. If behavior must
change to make the split correct, call it out as a separate acceptance point.

### Single Module

Use one module or package when:

- The feature has one implementation and one owner.
- No other module needs to compile against its contract.
- Navigation, routing, or integration is local to the feature.
- The implementation dependencies are acceptable for all callers.
- The boundary is still changing and an interface would mostly duplicate files.
- Tests can cover behavior without isolating a public contract module.

This is the default for small or early features.

### API / Impl Pair

Use an `api` / `impl` split when at least one of these is true:

- Another module must depend on route contracts, events, interfaces, DTOs, or
  factories without depending on UI/data/framework implementation.
- Navigation, deep links, plugin loading, dependency injection, or feature
  registration needs a stable contract surface.
- Multiple implementations exist or are likely: fake/real, platform-specific,
  paid/free, local/remote, test/prod, or replaceable provider.
- The implementation has heavy dependencies that should not leak to callers.
- The split prevents circular dependencies or reduces build coupling.
- Different teams or agents can own contract and implementation independently.
- Contract compatibility matters for generated clients, SDKs, plugins, or public
  packages.

An `api` module should contain only stable contracts:

```text
interfaces, route/event contracts, public models, typed commands,
factory/provider contracts, small value types, compatibility docs
```

An `impl` module should contain implementation details:

```text
screens, adapters, repositories, framework code, internal mappers,
real/fake providers, DI bindings, platform integrations
```

Do not create an `api` module only to mirror architecture. If no caller can use
the API without the implementation, the split is probably too early.

## Boundary Pressure Signals

Split or introduce a stronger boundary when these signals repeat:

- feature files import data-source, SDK, or platform implementation packages
- UI code reaches raw transport, database, file, or channel payloads
- shared packages need feature-specific flags, copy, analytics, or route
  decisions
- tests must boot unrelated app shells to exercise one state transition
- one implementation dependency forces all callers to carry a heavy optional SDK
- build changes require touching many unrelated target or package manifests
- a "common" folder has several unrelated owners and no stable public contract

When only one signal appears once, prefer a local cleanup before a module split.

## Package Layout

Prefer package names that express responsibility, not technical noise. Common
top-level groups include:

```text
api/ or contract/     public caller-facing contracts
impl/ or internal/    implementation details
model/                plain values owned by this boundary
state/                UI/application state and effects
component/            reusable UI or interaction pieces
data/                 persistence, network, cache, external data sources
domain/               product rules, use cases, policies
platform/             OS, runtime, SDK, filesystem, shell, browser adapters
testing/ or fixture/  test doubles, samples, deterministic fixtures
```

Use the repo's existing names first. Do not rename established packages unless
the rename itself is the task.

## Boundary Rules

- Dependencies point inward or downward; implementation does not leak upward.
- Public contracts avoid framework-heavy types unless the platform is the
  contract.
- Domain and model layers avoid UI, persistence, transport, and platform types.
- UI layers do not own data source details or long-lived external side effects.
- Shared modules do not depend on feature implementation modules.
- Generated code, fixtures, and examples have explicit ownership.

## Review Checklist

- Who owns this file or module?
- Which callers are allowed to import it?
- Is the public surface smaller than the implementation?
- Does the split remove coupling or only add ceremony?
- Can the contract be tested without the implementation?
- Will a future implementation swap require changing callers?
- Are package names stable enough to keep?

## Verification

For structure changes, verify the boundary, not only formatting:

- compile/typecheck all affected modules
- run focused tests for contract mappers, route resolution, or provider wiring
- inspect import direction for forbidden dependencies
- check generated clients, fixtures, or public exports when the API changed
- report whether the change chose single module or `api`/`impl`, and why
