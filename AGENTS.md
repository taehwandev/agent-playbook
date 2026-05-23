---
keyflow_id: sys_agent_entrypoint
status: stable
type: human-reviewed
---

# KeyFlow Shared Agent Instructions

This file is the entrypoint for agents that consult the shared KeyFlow agent library.

## Purpose

Use this library to prevent repeated mistakes across repositories. It provides shared operating habits, review criteria, architecture principles, and platform guidance. Repo-local instructions remain the source of truth for project paths, commands, naming, domain rules, and product-specific policy.

## Priority

When instructions conflict, follow this order:

1. System and developer instructions from the active agent runtime.
2. The user's current request.
3. The target repo's local instructions, such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `.agents/README.md`, or `CONTRIBUTING.md`.
4. More specific shared KeyFlow documents, such as platform or product-pattern docs.
5. Shared KeyFlow common cards.
6. General guidance in `README.md`.

If the conflict changes behavior, verification, security, or data handling, call it out before or after the work.

## Always Read For Agent Work

For implementation, review, refactoring, debugging, documentation, or planning tasks, first consult:

```text
<KEYFLOW_AGENT_ROOT>/common/agent-operating-skill.md
```

Then load only the supporting documents relevant to the task.

## Supporting Documents

Use `index.md` as the full document map. Do not duplicate the full index in repo-local instructions. Start with these direct routes, then load only the specific cards selected by `index.md`.

```text
<KEYFLOW_AGENT_ROOT>/index.md
<KEYFLOW_AGENT_ROOT>/common/llm-coding-discipline.md
<KEYFLOW_AGENT_ROOT>/common/code-conventions.md
```

## Workflow Documents

```text
<KEYFLOW_AGENT_ROOT>/workflows/agent-task-lifecycle.md
<KEYFLOW_AGENT_ROOT>/workflows/agent-handoff-continuation.md
<KEYFLOW_AGENT_ROOT>/workflows/development-cycle.md
<KEYFLOW_AGENT_ROOT>/workflows/planning-research.md
<KEYFLOW_AGENT_ROOT>/workflows/documentation-update.md
<KEYFLOW_AGENT_ROOT>/workflows/feature-implementation.md
<KEYFLOW_AGENT_ROOT>/workflows/bugfix-debugging.md
<KEYFLOW_AGENT_ROOT>/workflows/refactor-cleanup.md
<KEYFLOW_AGENT_ROOT>/workflows/release-readiness.md
<KEYFLOW_AGENT_ROOT>/workflows/review-and-commit.md
```

## Operating Rule

Do not copy this whole library into a repo. Link only the documents relevant to that repo. Keep repo-specific paths, commands, role matrices, API names, and domain language in the repo-local instructions.

`<KEYFLOW_AGENT_ROOT>` means the directory containing this shared library. In a repo-local template, replace it with that repo's actual shared-library path or an environment variable such as `${KEYFLOW_AGENT_ROOT}`.
