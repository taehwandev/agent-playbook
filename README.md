---
keyflow_id: sys_e2d59ab64adc
status: stable
type: ai-generated
---

# Agent Playbook

Shared agent guidance for work across repos, apps, platforms, and AI tools.

Root placeholder:

```text
<KEYFLOW_AGENT_ROOT>
```

Start here:

```text
<KEYFLOW_AGENT_ROOT>/AGENTS.md
<KEYFLOW_AGENT_ROOT>/index.md
```

## Structure

```text
common/           Shared engineering rules and workflows
platforms/        android, ios, web, server, application tracks
product-patterns/ Reusable product patterns such as auth, invite, billing
workflows/        Repeatable agent work paths
docs/             Static site for GitHub Pages
templates/        Repo-local routing snippets
```

## Rules

- Repo-local instructions always win.
- `AGENTS.md` is the shared entrypoint for agent runtimes.
- Use `index.md` to choose only the needed documents.
- Start most coding work from `common/agent-operating-skill.md`.
- Use `workflows/agent-task-lifecycle.md` for multi-step agent work of any kind.
- Use `workflows/development-cycle.md` for multi-step implementation work.
- A typical coding task should load `common/llm-coding-discipline.md`,
  `common/code-conventions.md`, one platform architecture card, and only
  relevant detail or concern cards.
- Naming is surface-specific: app display names can use product capitalization,
  while repos, slugs, services, and CLIs usually use lowercase `kebab-case`.
- Security, background work, release, permission, and OS integration concerns should load their detail cards explicitly.
- Keep repo paths, commands, components, role matrices, domain terms, and product-specific policy out of this library.
- Keep shared documents short, action-oriented, and reusable.
- Move repeated platform-neutral rules into `common/`.
- Move reusable SaaS or product mechanics into `product-patterns/`.
- Use `workflows/` to compose common and platform cards into repeatable work paths.
- Frontmatter `status` values mean `draft`, `review`, `stable`, or
  `deprecated`. Prefer `review` for active guidance and `stable` only for
  entrypoints or cards that are ready for broad reuse.
- Frontmatter `type` values describe provenance and review state:
  `ai-generated`, `human-reviewed-needed`, or `human-reviewed`. Use `status`
  for operational readiness and `type` for audit or human review queues.

## Folder Roles

- `.agent/`: hidden KeyFlow Desktop workspace context
- `agent/`: explicit shared library for multiple repos and agents
