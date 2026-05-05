---
description: Scaffold a new EU AI Act-compliant SDD project from a high-level intent (calibrated planning, HITL gates, living tracking, audit excels, scientific reports — all on-demand).
---

# /system-designer

> Convenience slash command that invokes the **system-designer meta-skill** in Claude Code.
> Equivalent to: "Read SKILL.md and run the system-designer workflow."

## Usage

```
/system-designer <high-level intent>
```

Examples:

```
/system-designer build a fraud-detection system for SEPA transfers
/system-designer scaffold an oncology triage assistant (high-risk healthcare)
/system-designer create a legal-compliance reviewer for GDPR DPIAs
/system-designer
```

If invoked with no argument, the skill jumps straight to the interview phase.

## What this command does

1. Loads the meta-skill at `SKILL.md` (the entry-point of `system-designer`).
2. Runs the **master orchestrator** at `prompts/00_master_orchestrator.md`.
3. Executes the 13-phase workflow:
   - `read_context` → `interview` → `planning_brief` → **GATE 1 (HITL)** → `scaffold` → `compose_prompts` → `fetch_library_docs` → `seed_tracking` → `emit_audit_sheet` → `self_audit` → `reflection` → **GATE 2 (HITL)** → `handoff` → STOP.
4. Stops at handoff. The generator does **not** continue developing the child system — that's the child orchestrator's job.

## Core invariants enforced (no auto-skip ever)

- **P1 Portability** — no `claude_code:` / `cursor:` / `mcp__` references in emitted artifacts.
- **P2 Calibration** — every estimate, alternative, KPI, and HITL option carries a confidence % or range; forbidden tokens (best, always, never, guaranteed, certain, definitely, impossible) are rejected.
- **P3 On-demand** — emits only what the interview confirmed.
- **P4 Prompt-architect** — every emitted prompt passes through `prompt_architect/SKILL.md`. Master orchestrator self-audited at G9=A level.
- **P5 Living docs** — every artifact updates `tracking/project.json`, `tracking/sessions/*`, `audit/audit_sheet.xlsx` per session.
- **2 HITL gates** — Gate #1 (post-planning) and Gate #2 (post-scaffold) **always** ask the user; never auto-approve.

## Calibration of this command itself

Confidence the slash command will resolve the meta-skill correctly in your Claude Code session:
- ~92% if `.claude/commands/system-designer.md` lives at repo root.
- ~75% if invoked from a different cwd (skill needs to be reachable via `Read SKILL.md`).
- Fallback: type "Read SKILL.md and run the system-designer workflow" — works on any LLM, not just Claude Code.

## What it produces

A complete child-system tree under `<cwd>/<system_name>/` (default location, override via interview):

```
<system_name>/
├── CLAUDE.md / SPEC.md / SPEC.json / ARCHITECTURE.md / HANDOFF.md
├── prompts/                # composed via prompt_architect
├── library_docs/           # fresh fetched, per chosen lib + version
├── tracking/               # project.json + sessions + decisions + errors_catalog (30 AIE)
├── memory/                 # 4 typed memories (user/project/feedback/reference)
├── audit/                  # 13-sheet xlsx + EU AI Act mapping + self_audit + reflection
├── docs/reports/           # cumulative + chosen standard (IMRaD/TRIPOD-AI/CONSORT-AI/STARD-AI/SPIRIT-AI)
└── docs/decisions/         # ADR log
```

Plus 11 session KPIs, calibration & portability self-scans, and a fully audited prompt suite.

## Out of scope for this command

- Editing an existing project (use that project's own orchestrator, not this generator).
- Single-prompt design (use `prompt_architect/SKILL.md` directly, not this generator).
- Running or deploying the generated child system (handoff stops the generator; child orchestrator takes over).

## Documentation

- `README.md` — repo overview.
- `docs/ARCHITECTURE.md` — full system architecture (this generator).
- `docs/scripts/*.md` — per-prompt deep-dive (one file per `prompts/*.md`).
- `references/calibrated_probabilities.md` — P2 operational rules.
- `references/portable_invocation.md` — P1 contract + per-LLM notes.
- `references/eu_ai_act_mapping.md` — EU AI Act coverage table.
- `tests/README.md` — self-validation suite.
- `dashboard/index.html` — static visualisation of `tracking/project.json`.

## Behaviour

The slash command itself is a thin convenience layer for Claude Code. The actual logic lives in the meta-skill, so it works identically on any LLM via "Read SKILL.md and run the workflow" — see `references/portable_invocation.md` for per-platform notes.
