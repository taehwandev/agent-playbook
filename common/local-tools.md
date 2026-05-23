---
keyflow_id: sys_local_tools
status: draft
type: human-reviewed-needed
---

# Local Tools Policy

Use installed local tools when they provide better evidence, faster inspection,
or safer execution than guessing.

## Principles

- Prefer local inspection over assumptions.
- Prefer repo-provided scripts and wrappers over global commands.
- Prefer read-only commands before commands that mutate files or external
  state.
- Use network only when current external information is required or local
  evidence is insufficient.
- Do not invent tool availability. Check it.

## Agent And AI CLIs

- Use Antigravity CLI as `agy`.
- Do not use Gemini CLI as the Google agent path when the environment says
  Antigravity has replaced it.
- For usage and quota visibility, prefer Agent Cat:

```text
agentcat snapshot --json
```

- For local model availability, prefer runtime commands such as:

```text
ollama list
```

## Discovery Pattern

When local tooling matters:

1. Check whether the command exists.
2. Check the version or health command when safe.
3. Prefer the absolute path if PATH is unreliable.
4. Record failures plainly instead of silently falling back.

Example:

```text
command -v agy
agy --version
command -v agentcat
agentcat snapshot --json
```

## Repo Commands

Exact build, test, lint, package, deploy, and smoke commands belong in each
repo's local instructions. Shared docs should not hard-code repo-specific
commands.

## Reporting

When local tools affect the result, report:

- tool name
- command run
- success or failure
- important limitation, such as missing auth, stale cache, or unavailable quota
  data
