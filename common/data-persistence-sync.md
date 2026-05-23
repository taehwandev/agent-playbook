---
keyflow_id: sys_data_persistence_sync
status: draft
type: ai-generated
---

# Data Persistence Sync

Use for local persistence, cloud sync, offline mode, migrations, import/export, cache invalidation, and conflict handling.

## Separate

- Draft/local UI state
- Durable local persistence
- Server source of truth
- Derived cache
- Exported or shared artifacts

## Rules

- Define ownership before adding a second copy of data.
- Persist only stable state, not transient UI state.
- Version data that can outlive one app release.
- Make stale writes and conflict behavior explicit.
- Keep migration and backward compatibility near the storage boundary.
- Treat import/export as contracts with validation and failure states.

## Sync Questions

- Is this local-first, server-first, or offline-capable?
- What happens on stale save?
- Can two clients edit the same resource?
- What data is safe to cache?
- What must be cleared on logout, org switch, revoke, or downgrade?

## Tests

Cover load, save, migration, corrupted data, quota/storage failure, stale version, retry, and logout cleanup where relevant.
