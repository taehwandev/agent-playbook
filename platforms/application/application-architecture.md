---
keyflow_id: sys_7a1b89bb9a49
status: draft
type: ai-generated
---

# Application Architecture

Use for desktop/native app shells: Mac, Tauri, Electron, menu bar, windows, local files, and system integration.

For files, shell, clipboard, notifications, background work, updates, power assertions, menu bar/tray controls, or privileged APIs, also use `application-system-integration.md`.

For signing, notarization, IPC, URL schemes, renderer bridges, shell/file access, or credential exposure risk, also use `application-security.md`.

## Boundaries

```text
Window/Scene/View -> Presentation State -> Command/Use Case -> App Service -> System Adapter
```

## Rules

- Separate window lifecycle from screen state.
- Route menu, shortcut, toolbar actions through commands.
- Wrap file, shell, notification, clipboard, permission APIs.
- Keep IPC contracts typed and explicit.
- Long-running work needs cancellation, progress, and error reporting.
- Distinguish user-facing errors from logs.
- Keep menu bar/tray, panel, shortcut, and toolbar entry points on the same command path.
- Keep OS resource ownership explicit: status items, windows, monitors, timers, assertions, and background workers.

## Refactor Signals

- Window code owns file I/O, network, and product rules.
- Menu actions repeat permission/state checks.
- Renderer exposes privileged APIs too broadly.
- Background task ownership is unclear.
- App quit, timeout, or failure does not clean up active OS resources.
