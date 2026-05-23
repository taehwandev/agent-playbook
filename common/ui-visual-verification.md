---
keyflow_id: sys_ui_visual_verification
status: review
type: human-reviewed-needed
---

# UI Visual Verification

Use when changing UI layout, interaction, visible text, controls, navigation,
responsive behavior, accessibility labels, or state presentation.

## Default

A build or typecheck proves that UI code compiles. It does not prove that the UI
is usable, visible, readable, or wired to the intended action.

Verify the user path, not only the component in isolation, when the change
affects navigation, commands, permissions, persistence, or cross-surface state.

## Check

- Main success path.
- Empty, loading, disabled, error, unavailable, and permission-denied states.
- Long text, localized text, missing images, missing icons, and slow data.
- Small and large viewports or containers relevant to the product.
- Light mode, dark mode, increased system font size, reduced motion, and high
  contrast when the platform supports them and the change can be affected.
- Keyboard focus, screen reader labels, hit targets, and visible focus state.
- Whether text, icons, badges, menus, or overlays overlap or resize the layout
  unexpectedly.
- Whether multiple entry points for the same command produce the same result.
- Whether visual state updates after actions, retries, refreshes, or navigation.

## Tools By Platform

Use repo-local tooling first. Common evidence sources include:

- Web: Playwright, Testing Library, axe, browser screenshots, geometry checks.
- Android: Compose UI Test, Espresso, screenshot or layout inspection.
- iOS: XCUITest, accessibility inspector, previews, screenshot checks.
- Desktop/application: platform smoke tests, WebDriver/Playwright when
  applicable, screenshot checks, menu/tray/window interaction smoke.

Also load `common/accessibility-i18n.md` for user-facing text, forms, labels,
dates, numbers, localization, focus, or screen-reader behavior. Load the
matching platform review card when platform UI tooling or conventions matter.

## Evidence

Use the strongest practical evidence available:

- component, view, or interaction tests for deterministic behavior
- accessibility-tree or semantic assertions for labels, roles, and states
- screenshot, pixel, geometry, or layout smoke checks for visual regressions
- manual smoke when automation cannot observe the affected surface

State what the check can and cannot prove. Geometry does not prove contrast or
copy quality. A screenshot does not prove that the command executed. A visible
button does not prove that the trusted boundary behind it was reached.

## Report

Name the scenario, environment, action, expected result, observed result, and
remaining risk when verification is manual or partial.
