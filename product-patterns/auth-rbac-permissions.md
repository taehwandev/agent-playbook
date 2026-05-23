---
keyflow_id: sys_8a635e708aeb
status: draft
type: ai-generated
---

# Auth, RBAC, Permissions

Use for login, membership, role, permission, entitlement, and tenant-boundary work.

## Separate

- Auth: who the user is.
- Authorization: what action is allowed.
- Role: product-facing permission bundle.
- Permission: action-level allow/deny.
- Entitlement: plan or feature access.

## Rules

- Server is the final authority.
- Client checks are for UX and request prevention.
- Distinguish unauthenticated, unauthorized, plan-limited, not-a-member.
- Prefer action permissions over role-name checks.
- Recheck permissions after role change, org switch, invite accept, logout.

## Check

- Is this enforced on server and represented in UI?
- Does cache update after permission changes?
- Does the error avoid leaking sensitive data?
