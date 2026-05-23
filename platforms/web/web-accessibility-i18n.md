---
keyflow_id: sys_web_accessibility_i18n
status: draft
type: ai-generated
---

# Web Accessibility I18n

Use for web UI text, forms, menus, dialogs, keyboard flow, focus, localization, and responsive text behavior.

## Accessibility

- Prefer semantic elements and accessible names.
- Dialogs need focus entry, focus trap or clear return behavior, and escape/close handling.
- Forms need labels, validation messages, and error association.
- Icon-only controls need accessible names or tooltips.
- Keyboard users must reach and operate critical actions.
- Disabled and permission-denied states should be understandable.
- Do not rely on color alone for status, role, plan, or validation state.

## I18n

- Keep product UI text out of hardcoded component strings when the repo has i18n.
- Do not concatenate translated fragments when grammar can vary.
- Dates, numbers, currency, names, and pluralization need locale-aware formatting.
- Long translations must fit without overlap, clipping, or tiny unreadable controls.
- Product/domain terminology belongs in repo-local glossary when specific.

## Product Copy Boundaries

- UI copy must not imply real auth, invite, billing, or privacy guarantees before backend enforcement exists.
- Prototype/demo copy should be visibly scoped or kept out of production routes.
- Permission-denied copy should distinguish login required, role denied, plan limited, and unavailable feature.
- Avoid feature-explainer text inside the working UI when the state/action itself can communicate the workflow.

## Tests

- Query UI by role, label, and visible text.
- Test important keyboard flows.
- Check longest expected translation or pseudo-localized copy for compact UI.
- Verify dialogs restore focus or leave focus in a predictable place.
- Do not weaken accessible-name assertions without explaining the copy change.
