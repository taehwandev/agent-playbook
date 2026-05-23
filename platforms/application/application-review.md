---
keyflow_id: sys_4c70aafdfcb1
status: review
type: ai-generated
---

# Application Review

Use for Mac/native desktop, Tauri, Electron, menu bar, window, and system integration review.

## Review

- Check window/menu/shortcut actions route through commands or use cases.
- Verify file, shell, clipboard, notification, permission, and update boundaries.
- Ensure renderer/webview code does not expose privileged APIs broadly.
- Check background task cancellation, progress, retry, and error reporting.
- Confirm logs avoid secrets, tokens, file contents, and private user data.
- Check menu bar, shortcut, toolbar, and panel entry points share command behavior.
- Verify timers, monitors, power assertions, and OS resources are released on stop, failure, timeout, and quit.

## Tools

- Native Mac: XCTest/XCUITest, `xcodebuild test`, SwiftLint if configured.
- Tauri: frontend tests, Playwright, Rust `cargo test`, command tests.
- Electron: unit tests, Playwright, packaging smoke tests.
- Release: signing, permission, auto-update, and first-launch smoke checks.
- Mac release: signing, notarization/stapling, Gatekeeper, quarantine, and update smoke checks when configured.

## UI Test Focus

- Window opens, restores, and closes without state loss.
- Menu, shortcut, tray/menu bar, and toolbar actions work.
- File picker, drag/drop, clipboard, notification, and permission flows behave safely.
- Background work can be cancelled and reports user-visible errors.
- Menu bar/tray controls reflect the same state as panel/window controls.
- Active OS assertions or monitors do not survive stop, expiry, or app termination.
