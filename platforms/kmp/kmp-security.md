---
keyflow_id: sys_kmp_security
status: review
type: human-reviewed-needed
---

# KMP Security

Use when Kotlin Multiplatform work touches credentials, local files, shell or
process execution, network clients, secure storage, platform permissions,
native interop, logging, release builds, signing, or open-source-safe setup.

Also use `common/secure-development-baseline.md` and
`common/security-privacy-review.md`. For desktop shell, IPC, signing,
notarization, updates, or privileged APIs, also use the application security
card.

## Rules

- Treat each actual implementation and platform adapter as a security boundary.
- Do not store secrets in shared resources, test fixtures, generated source, or
  public sample configuration.
- Keep credentials and tokens out of user-visible errors, telemetry, logs,
  screenshots, crash reports, and serialized run artifacts.
- Validate data crossing platform boundaries: files, URLs, shell output,
  clipboard, native callbacks, permissions, deep links, and interop pointers.
- Keep shell, filesystem, network, clipboard, notification, and secure-storage
  access behind narrow adapters with explicit allowed operations.
- Do not assume one target's permission or sandbox model applies to another.
- Document target-specific release requirements such as signing, entitlements,
  notarization, package identifiers, or store configuration in repo-local docs.

## Review Questions

- Which targets can access the secret, file, permission, or privileged API?
- What is the user-visible failure when a target denies access or lacks the
  capability?
- Can a compromised renderer, plugin, file, clipboard value, callback, or native
  input invoke a broader operation than intended?
- Are debug/test credentials, local paths, signing material, or private prompts
  excluded from the open-source diff?

## Verification

- Run the relevant compile/test target and a focused adapter or smoke check when
  privileged behavior changed.
- Inspect the diff for secrets, local config, broad shell/filesystem APIs,
  unsafe logs, and silent unsupported-target fallbacks.
