---
keyflow_id: sys_850baab06765
status: stable
type: ai-generated
---

# Repo Agent Routing Template

Add this to repo-local agent instructions.

```text
Shared agent library:
<KEYFLOW_AGENT_ROOT>/AGENTS.md
<KEYFLOW_AGENT_ROOT>/index.md

Use repo-local instructions first.
Use the shared index only to select the smallest relevant document set.
Do not load every shared document by default.
Replace `<KEYFLOW_AGENT_ROOT>` with this repo's actual shared-library path or an
environment variable such as `${KEYFLOW_AGENT_ROOT}`.
Keep repo paths, commands, components, role matrices, and domain terms in this repo.
```

Core direct routes:

```text
Document index: <KEYFLOW_AGENT_ROOT>/index.md
Agent operating skill: <KEYFLOW_AGENT_ROOT>/common/agent-operating-skill.md
LLM discipline: <KEYFLOW_AGENT_ROOT>/common/llm-coding-discipline.md
Code conventions: <KEYFLOW_AGENT_ROOT>/common/code-conventions.md
Agent task lifecycle: <KEYFLOW_AGENT_ROOT>/workflows/agent-task-lifecycle.md
Agent handoff/continuation: <KEYFLOW_AGENT_ROOT>/workflows/agent-handoff-continuation.md
Development cycle: <KEYFLOW_AGENT_ROOT>/workflows/development-cycle.md
Planning/research workflow: <KEYFLOW_AGENT_ROOT>/workflows/planning-research.md
Documentation workflow: <KEYFLOW_AGENT_ROOT>/workflows/documentation-update.md
Feature workflow: <KEYFLOW_AGENT_ROOT>/workflows/feature-implementation.md
Bugfix/debugging workflow: <KEYFLOW_AGENT_ROOT>/workflows/bugfix-debugging.md
Refactor workflow: <KEYFLOW_AGENT_ROOT>/workflows/refactor-cleanup.md
Release readiness workflow: <KEYFLOW_AGENT_ROOT>/workflows/release-readiness.md
Review/commit workflow: <KEYFLOW_AGENT_ROOT>/workflows/review-and-commit.md
```

Use `index.md` for platform, product-pattern, and task-specific common cards
instead of copying the full shared library into repo-local instructions.
