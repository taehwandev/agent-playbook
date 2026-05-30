---
keyflow_id: sys_kmp_review
status: review
type: human-reviewed-needed
---

# KMP Review

Use when reviewing Kotlin Multiplatform, Compose Multiplatform, shared Kotlin
modules, source-set changes, platform actuals, or target app integration.

## Findings Priority

1. Cross-target behavior mismatch, unsupported target hidden as success, or data loss.
2. Security, credential, file, shell, permission, or native interop risk.
3. Shared source-set dependency leak or platform API import in common code.
4. Missing target build/test evidence.
5. UI/state ownership, cancellation, cleanup, or lifecycle bug.
6. Maintainability, naming, package layout, or duplicated adapters.

## Check

- Does the route use the target repo's local KMP/Gradle/module rules?
- Are module and source-set boundaries checked against
  `kmp-module-structure.md` when Gradle modules, umbrella frameworks, or package
  moves changed?
- Are source-set dependencies intentional and compileable for every affected target?
- Is shared code free of accidental Android, desktop, iOS, JVM-only, or native-only APIs?
- Do actual implementations satisfy the same contract or return typed unsupported failures?
- Are platform resources cleaned up on cancellation, failure, lifecycle teardown, and app quit?
- Are state, effects, repositories, and platform adapters owned by the right layer?
- Is verification run for every affected target, or is the skipped target and
  residual risk stated?

## Output

Lead with concrete findings:

```text
Findings:
- [High] platforms/kmp/... - issue, impact, recommendation, verification
```

If no findings remain, say so and list target/test gaps that were not checked.
