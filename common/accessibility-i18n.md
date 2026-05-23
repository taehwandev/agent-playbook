---
keyflow_id: sys_accessibility_i18n
status: review
type: human-reviewed-needed
---

# Accessibility I18n

Use when changing UI text, forms, controls, navigation, media, keyboard/focus
behavior, dates, numbers, currency, localization, or user-facing error states.

## Accessibility Rules

- Interactive controls need an accessible name, role, state, and clear target.
- Do not rely on color, icon shape, motion, or position alone to communicate
  state or errors.
- Preserve keyboard, switch control, screen reader, and touch navigation paths
  when the platform supports them.
- Keep focus order predictable after navigation, dialog, menu, validation, and
  async state changes.
- Support text scaling, long labels, small screens, and high contrast modes where
  the platform provides them.
- Media, image, chart, map, and canvas surfaces need text alternatives or a
  product-approved fallback path.
- Motion and animation should respect reduced-motion settings when the platform
  exposes them.

## Internationalization Rules

- Keep user-facing strings out of low-level logic when the repo has a localization
  boundary.
- Do not concatenate translated fragments when grammar, plurality, gender, or word
  order can vary.
- Format dates, times, time zones, numbers, currency, addresses, and names with
  locale-aware APIs when shown to users.
- Store stable machine values separately from localized display values.
- Design layouts for long text, missing translations, and mixed-language content.
- Avoid hard-coded region, calendar, currency, measurement, or address assumptions
  unless the product is intentionally scoped that way.

## Check

- Can the user complete the main path with keyboard or assistive technology?
- Does the UI still work with long text, text scaling, and small screens?
- Are validation and permission errors announced or visible in context?
- Are user-facing dates, numbers, and currencies formatted for the user's locale?
- Is any text embedded in images, generated assets, placeholders, logs, or
  low-level constants where localization cannot reach it?

## Tests

Use platform-appropriate checks such as role/name queries, keyboard navigation,
screen reader labels, screenshot or layout checks with long text, and locale or
timezone-specific unit tests when relevant.

