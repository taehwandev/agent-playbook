---
keyflow_id: sys_a66e7e6b4a9d
status: review
type: ai-generated
---

# Invitation Workflows

Use for team, tenant, workspace, or organization invite flows.

For concrete invite records, token handling, state machine, accept-time
revalidation, delivery side effects, and tests, also use
`invitation-implementation.md`.

## Flow

```text
create -> notify -> accept -> link/create account -> join tenant -> assign role
```

## Rules

- Invite creation needs its own permission.
- Limit which roles the inviter can assign.
- Distinguish existing member, pending invite, expired invite, revoked invite.
- Canonicalize email before duplicate checks.
- Revalidate tenant, role, token, and inviter policy at accept time.
- Refresh session and permissions after accept.

## UI States

- success
- duplicate invite
- already member
- permission denied
- role not assignable
- expired or revoked token

## Audit

Record create, resend, revoke, accept with actor, tenant, target email, and role.
