---
keyflow_id: sys_agent_editing_safety
status: review
type: human-reviewed-needed
---

# Agent Editing Safety

Use this when an agent may edit files, run commands, inspect local state, or
touch data outside the current repository.

## File Safety

- Read before editing.
- Keep edits scoped to the request.
- Do not revert user-owned changes unless explicitly asked.
- Do not run destructive commands unless the user clearly requested them.
- Be extra careful when editing outside the current repo.
- Leave generated or build outputs alone unless they are required evidence or
  explicitly part of the task.

## Secrets And Private Data

Do not print, copy, summarize, or persist secrets from:

- credential files
- tokens
- private keys
- auth cookies
- local database rows containing sensitive user data
- prompt logs containing private content

Metadata such as provider name, model, timestamp, token count, and status can be
used when needed, but prompt or secret content should not be exposed.

## External State

Treat these as high risk:

- network writes
- deploys
- package publishes
- release creation
- database migrations
- account, billing, permission, or invite changes
- filesystem writes outside the repo or approved workspace

Prefer dry runs, previews, local checks, or explicit approval before changing
external state.

## Command Safety

- Prefer commands that terminate on their own. Avoid interactive, watch, tail,
  server, or long-running commands unless the task needs them.
- Use repo-provided wrappers and documented commands before ad hoc global tools.
- Bound long-running checks with the agent runtime's timeout, a documented test
  timeout, or a clear stop condition.
- Do not leave background processes running unless the user asked for a dev
  server or long-lived process and you report the URL, port, pid, or stop
  command.
- Avoid broad shell expansions, command substitution, and writes outside the repo
  unless the target path and risk are clear.
- Inspect commands before running them when they came from generated scripts,
  downloaded content, package scripts, or untrusted docs.
- Treat commands that mutate git history, delete files, publish packages,
  deploy, migrate databases, change permissions, or write external state as
  approval-required unless the user explicitly requested that exact action.

## Conflict Handling

If shared KeyFlow guidance conflicts with repo-local instructions, follow the
repo-local instructions and mention the conflict when it matters. Shared docs
are defaults, not overrides.
