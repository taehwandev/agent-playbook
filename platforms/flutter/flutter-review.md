---
keyflow_id: sys_flutter_review
status: review
type: human-reviewed-needed
---

# Flutter Review

Use when reviewing Flutter widgets, state owners, Dart packages, repositories,
platform channels, plugins, target setup, or mobile/desktop/web behavior.

## Findings Priority

1. User-visible crash, route/state regression, data loss, or unsupported target hidden as success.
2. Security, credential, WebView, deep-link, permission, channel, or plugin risk.
3. Missing analyzer/test/build evidence for affected targets.
4. Business logic in widgets, lifecycle leaks, missing disposal, or async race.
5. State model, repository, cache, or persistence bug.
6. Maintainability, naming, package layout, or duplicated platform adapters.

## Check

- Does the change follow the repo's chosen state management and navigation style?
- Are feature folder, package, plugin, or federated plugin boundaries checked
  against `flutter-project-structure.md` when package exports, path
  dependencies, platform implementations, or package moves changed?
- Are widgets rendering state and emitting events rather than owning business logic?
- Are platform channels, plugins, and native callbacks behind typed services?
- Are unsupported platform paths, permission denial, lifecycle changes, and
  plugin failures represented in state?
- Are controllers, streams, timers, isolates, listeners, and plugin handles
  disposed by the owner?
- Are semantics, localization, long text, narrow layout, keyboard/focus, and
  target-specific interactions covered when UI changed?
- Was analyzer/test/build/golden/integration verification run for the affected
  package or target, or is the skipped evidence clearly explained?

## Output

Lead with concrete findings:

```text
Findings:
- [High] platforms/flutter/... - issue, impact, recommendation, verification
```

If no findings remain, say so and list target/test gaps that were not checked.
