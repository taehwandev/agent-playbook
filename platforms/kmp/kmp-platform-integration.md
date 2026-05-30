---
keyflow_id: sys_kmp_platform_integration
status: review
type: human-reviewed-needed
---

# KMP Platform Integration

Use when Kotlin Multiplatform work touches source sets, `expect`/`actual`,
native interop, platform services, files, shell/process execution, clipboard,
notifications, permissions, secure storage, background work, or app lifecycle.

For source-set hierarchy, shared module splits, and umbrella framework shape,
also use `kmp-module-structure.md`.

## Adapter Choice

Prefer the smallest boundary that keeps shared code honest:

| Boundary | Use When |
| --- | --- |
| Interface injection | The behavior needs fakes, multiple implementations, or dependency inversion. |
| `expect`/`actual` function or class | The API is small, stable, and truly target-specific. |
| Target source-set wrapper | The behavior belongs only to one target UI or shell. |
| Capability object | Some targets support the action and others must disable or explain it. |

Do not use `expect`/`actual` as a dumping ground for large services. Large
platform behavior is usually easier to test behind an interface.

## Rules

- Every actual implementation must satisfy the same contract or return an
  explicit unsupported result.
- Platform adapters validate external inputs from files, URLs, shell output,
  clipboard, platform callbacks, notifications, permissions, and native APIs.
- Long-running adapters need cancellation, timeout, progress, retry policy, and
  cleanup on failure, cancellation, logout, app quit, or lifecycle teardown.
- File paths, environment variables, process execution, native handles, and
  credentials must not leak into shared models or user-safe errors.
- Keep platform resource ownership explicit: windows, monitors, jobs, file
  watchers, sockets, callbacks, notification listeners, and native pointers need
  an owner and release path.
- Add target-specific tests or smoke checks when actual implementations, Gradle
  targets, packaging, permissions, or native interop changed.

## Stop If

- A target cannot support required behavior and the product has no fallback,
  disabled state, or acceptance decision.
- The change requires credentials, signing, entitlements, release packaging, or
  external service setup that is not present in repo-local docs.
- A platform adapter would need to print, persist, or expose secrets to make the
  feature work.

## Verification

- Run compile/test tasks for affected source sets and app targets.
- Exercise unsupported-target behavior, permission denial, cancellation, and
  cleanup when they are reachable.
- Review the final diff for accidental broad platform API exposure in
  `commonMain`, silent no-op actuals, missing cleanup, and private detail in
  logs or user-visible errors.
