---
keyflow_id: sys_stack_discovery
status: review
type: human-reviewed-needed
---

# Stack Discovery

Use before running project commands, adding dependencies, editing build config,
or writing framework-specific code in an unfamiliar repo.

## Default

Do not guess the package manager, framework, language version, test runner, or
project command. Discover them from repo files first, then use repo-local
instructions and scripts.

## Inspect First

Look for the files that define the stack:

- repo instructions: `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`,
  `CODEX.md`, `.agents/README.md`, `CONTRIBUTING.md`
- JavaScript/TypeScript: `package.json`, lockfiles, `tsconfig.json`,
  framework config, `.nvmrc`, `.node-version`
- Python: `pyproject.toml`, lockfiles, `requirements*.txt`, `.python-version`
- Swift/iOS: `Package.swift`, `Podfile`, Xcode project/workspace, scheme docs
- Android/JVM: `settings.gradle*`, `build.gradle*`, `gradle.properties`,
  `gradle/wrapper/gradle-wrapper.properties`
- Rust/Go: `Cargo.toml`, `Cargo.lock`, `go.mod`, `go.sum`
- containers or CI: `Dockerfile`, compose files, CI workflow files

Prefer the lockfile and repo scripts over global defaults.

## Decide Commands

- Use the package manager implied by the lockfile.
- Use scripts or wrappers from the repo before ad hoc commands.
- Check framework and runtime versions before using version-specific APIs.
- Check test and lint command names before inventing a command.
- For monorepos, identify the affected workspace before running broad commands.

## Stop If

- Multiple package managers or lockfiles conflict and repo docs do not resolve
  the conflict.
- The expected manifest, wrapper, or workspace cannot be found.
- Running the likely command would install dependencies, write outside the repo,
  hit the network, or change external state without approval.

## Report

When stack discovery affects the work, report the discovered package manager,
framework/runtime, workspace, and command source.
