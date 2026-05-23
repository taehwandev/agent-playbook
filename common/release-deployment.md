---
keyflow_id: sys_release_deployment
status: review
type: human-reviewed-needed
---

# Release Deployment

Use when packaging, deploying, publishing, migrating, signing, tagging, creating
release notes, changing environment config, or preparing rollback-sensitive work.

## Default

A release is not complete because the build succeeded. It needs a clear artifact,
environment, verification gate, and rollback or forward-fix path.

## Separate

- Build artifact
- Runtime configuration
- Secrets and credentials
- Database or storage migration
- Feature flag or rollout policy
- Deployment action
- Post-release smoke and monitoring
- Rollback or forward-fix plan

## Rules

- Keep local, development, staging, and production configuration separate.
- Do not hard-code environment behavior that should be injected by deployment,
  release config, or local config.
- Verify signing, credentials, package identity, bundle id, domain, callback URL,
  or app id before release when applicable.
- Make migrations backward compatible when old and new app versions can overlap.
- Run destructive migrations only with a rollback, restore, or forward-fix plan.
- Feature flags need an owner, default, rollout condition, monitoring signal, and
  cleanup plan.
- Release notes should mention user-visible changes, migrations, breaking
  changes, security impact, and required operator action.
- Never print or commit deployment secrets, signing material, or generated
  production config.

## Release Gate

Before release, confirm:

- source revision and artifact version are known
- required tests, builds, or smoke checks passed or have accepted risk
- config and secret injection happened in the intended environment
- monitoring, logs, crash reports, or health checks can show failure
- rollback or forward-fix path is realistic for the changed surface

## Post-Release Check

Verify the most important user or system path after release. If verification is
manual, record exactly what was checked and what was not checked.

