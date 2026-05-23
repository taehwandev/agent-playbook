---
keyflow_id: sys_0678d6c5f03c
status: draft
type: ai-generated
---

# Web Review

Use for React/web UI, browser behavior, and frontend PR review.

## Review

- Check route/data boundaries, cache invalidation, form validation, and error states.
- Verify accessibility: labels, roles, focus order, keyboard use, contrast.
- Check responsive layout for mobile, tablet, desktop.
- Ensure permission and entitlement checks are not UI-only.
- Look for duplicated fetch/error/permission logic in components.
- Check whether mock data, demo toggles, and localStorage state are clearly separated from real service behavior.

## React Checks

- Component state ownership is local unless multiple screens actually need it.
- Effects have dependencies, cleanup, and abort behavior where relevant.
- Derived state is not stored unnecessarily.
- Context/provider additions have cross-route ownership, not one-screen convenience.
- Hooks expose intent and state, not hidden product policy.
- Form submit paths handle pending, success, validation error, permission denied, and network error.

## Service Checks

- Invite, share, billing, auth, and role UI do not promise server enforcement that does not exist.
- Buttons hidden by permission are also blocked at action/API boundary.
- Role and plan checks use named helpers or policy functions instead of repeated JSX booleans.
- Browser storage is not the source of truth for protected access.

## Tools

- Static: TypeScript, ESLint, framework lint.
- Unit: Vitest or Jest for policy, mapper, hook, reducer.
- Component: Testing Library by role, label, visible text, interaction.
- UI/E2E: Playwright for navigation, auth, forms, permissions, critical flows.
- A11y: axe or Playwright accessibility checks when available.

## UI Test Focus

- User can complete the main flow.
- Loading, empty, error, and permission-denied states render correctly.
- Keyboard-only path works for forms, dialogs, menus, tables.
- No text overflow or layout break across key viewport sizes.
- Denied users cannot trigger the protected command, not only fail to see the button.
