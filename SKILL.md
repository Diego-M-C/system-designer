---
name: system-designer
description: Use when scaffolding a new SDD-methodology AI system from a single user intent. Triggers on "generate system", "scaffold AI project", "create SDD project", "build EU AI Act compliant system", or when this folder is dropped into any LLM chat (Claude Code, Cursor, Cline, Gemini CLI, Copilot CLI, Codex) with a high-level project request. Produces a complete child-system tree with master orchestrator, living tracking, KPIs, HITL gates, memory module, common-AI-error catalog, EU AI Act audit excels, scientific-report templates, and on-demand skills/agents — every prompt composed via the co-located prompt-architect skill. Portable across LLMs (no proprietary APIs in runtime).
---

# system-designer · SDD AI System Generator

## What this is

A **portable, LLM-agnostic meta-skill** that takes a user's high-level intent ("build a fraud-detection system", "design an oncology triage assistant", "scaffold a legal-compliance reviewer") and emits a complete EU AI Act-compliant project skeleton with full traceability, HITL governance, and on-demand orchestration.

This is **not** a single system. This is a **generator of systems** — same backbone every time (SDD + tracking + KPIs + HITL + memory + error catalog + EU AI Act + audit + scientific reports), particularised per intent.

## Core principles (non-negotiable, transversal to every artifact emitted)

**P1 · Portability.** Every artifact emitted runs in any LLM with file-system access. No Claude Code-only APIs, no proprietary hooks, no MCP-mandatory dependencies in runtime. Tools are described abstractly; fallbacks are mandatory.

**P2 · Calibrated probabilities.** Every output, decision, alternative, estimate, KPI target, prediction MUST carry a confidence % or range. Refuse to produce uncalibrated assertions. "X is the best" → forbidden. "X has ~75% fit; Y 15%; Z 10%" → required. See `references/calibrated_probabilities.md`.

**P3 · On-demand generation.** Nothing emitted for show. Each artifact (orchestrator, skill, agent, dashboard, dependencies, etc.) is created only if the interview phase confirms it is needed.

**P4 · Prompt-architect dependency.** Every prompt this skill emits — including this skill's own master orchestrator — is composed through the co-located `prompt_architect/SKILL.md`. No raw, un-audited prompts exit.

**P5 · Living documentation.** Every emitted artifact is a living document. The generated child system updates `tracking/project.json`, `tracking/sessions/*`, `tracking/decisions.md`, `tracking/errors.md`, `audit/audit_sheet.xlsx` on every relevant action. Static docs are forbidden.

## When to invoke

- User drops this folder into any LLM and asks to build/scaffold a system.
- User invokes `/system-designer` (Claude Code) or types "use system-designer to…".
- User has a high-level intent but no scaffolding.
- User needs an EU AI Act-compliant skeleton.

## Do NOT invoke for

- Editing an existing project (use that project's own orchestrator).
- One-off code questions.
- Designing a single prompt (use `prompt_architect/` directly).
- Running or deploying the generated system (out of scope — generator stops at handoff).

## High-level workflow

The skill executes the **master orchestrator** at `prompts/00_master_orchestrator.md`. The orchestrator runs the following 17 phases (full spec in `system_generator.json#/phases`):

1. **read_context** — load prompt-architect, EU AI Act checklists, audit example, references, templates, wizard.
1.5. **context_setup** *(v0.2.0)* — run `prompts/13_context_curator.md`. Ask the user for project context; fetch implementation guides, legislation (if applicable), non-library docs, curated internet sources via `mcp.playwright` (recommended) or `fetch()` fallback; each source carries a calibrated confidence% under `references/context_confidence_protocol.md`. Library docs are explicitly out of scope here (phase 7). The child inherits this curator and re-runs it at every session boundary.
2. **interview** — run `wizard/interview_questions.json` against the user; default via `wizard/defaults.json` for skipped questions.
3. **planning_brief** — emit calibrated plan with ≥3 alternatives at every strategic fork.
4. **GATE 1 (HITL)** — present plan; block until user approves.
5. **scaffold** — emit the child-system tree in `<target_path>` (default `<cwd>/<system_name>/`).
6. **compose_prompts** — invoke prompt-architect on every child prompt (Simple/Medium/Complex per role); audit each.
7. **fetch_library_docs** — download fresh docs of every chosen library into `<target_path>/library_docs/` (Context7 first, fallback direct fetch). Distinct from phase 1.5: this owns *library* documentation only.
8. **seed_tracking** — initialise `tracking/`, `memory/`, `errors_catalog.json` (≥30 pre-loaded common AI errors), `decisions.md`.
9. **emit_audit_sheet** — generate `audit/audit_sheet.xlsx` Session-1 base + 13 EU AI Act checklist references.
10. **self_audit** — run prompt-architect Complex audit on every emitted prompt; portability + calibration scans; emit `audit/self_audit.md`.
11. **reflection** — structured reflection report on what was emitted, skipped, lowest-confidence decisions.
11.5. **structural_consistency** *(v0.2.0)* — run `prompts/10_data_flow_validator.md`. Compute `n_validators ∈ [3,10]` from a calibrated importance formula; spawn dynamic specialist validators + 1 mandatory simulation agent; consolidate into `data_flow_validation/structural_consistency/consolidated_report.md`; surface dissents to Gate #2.
12. **GATE 2 (HITL)** — present generated tree + reflection + structural-consistency consolidation; block until user approves.
13. **handoff** — emit `<target_path>/HANDOFF.md`. Generator does NOT continue developing the child system.
13.5. **feedback_session** *(v0.2.0)* — run `prompts/11_feedback_learning_loop.md`. Capture human feedback after handoff; classify under `references/feedback_taxonomy.md`; persist to `feedback_learning/corrections.db` (SQLite + FTS5) and `corrections.md` mirror; per-correction HITL: "should the system learn from this? Y/N/SKIP"; trigger improvement proposal at threshold (default 15) or explicit user request.
13.7. **improvement_audit** *(v0.2.0)* — run `prompts/12_improvement_jury.md`. 5 specialist auditors (`regression`, `calibration`, `portability`, `eu_ai_act_drift`, `memory_integrity`) audit the proposal with `references/jury_consensus_protocol.md`; mandatory HITL gate at end; no source change merges without explicit human approval.
14. **STOP** — handoff complete; child orchestrator (`<target_path>/CLAUDE.md`) takes over.

### Cross-phase: adaptive audit meta *(v0.2.0)*

`prompts/14_adaptive_audit_meta.md` is invoked **at the end of every task and at every session end** in BOTH the generator (per-phase) and the inherited child. It computes `n_auditors ∈ [3,10]` from an importance score, freshly composes each auditor via prompt-architect with a persona tailored to the scope, runs them in parallel, separates errors (blockers) from improvements (queued for phase 13.5), and surfaces HITL only when needed. Prompt 12 is its fixed-5-axis special case.

## Artifacts (full map in `system_generator.json#/artifacts`)

### Mandatory (always emitted)
- `CLAUDE.md`, `README.md`, `SPEC.md` + `SPEC.json`, `ARCHITECTURE.md`, `HANDOFF.md`
- `tracking/{project.json, project.md, kpis.json, decisions.md, errors.md, errors_catalog.json}`
- `tracking/sessions/0001_bootstrap/{session.json, session.md, kpis.json, errors.jsonl, observations.jsonl, scratch.md, checkpoint_decision.md, inputs_outputs_perf.json}`
- `memory/{MEMORY.md, user.md, project.md, feedback.md, reference.md}`
- `audit/{audit_sheet.xlsx, eu_ai_act_mapping.md, self_audit.md, reflection_session_0.md, evaluation_session_0.json}`
- `audit/checklists/` — references to the 13 EU AI Act checklists
- `docs/{decisions/, architecture/, reports/imrad.md.tmpl, reports/tripod_ai.md.tmpl}`
- `library_docs/<lib>/<version>/` — fresh docs per chosen library
- *(v0.2.0)* `context/{context_manifest.json, context_sources/, consult_websites.md, download_recommendations.md, curation_log.jsonl}` — phase 1.5 corpus
- *(v0.2.0)* `data_flow_validation/{sequence_snapshots/, structural_consistency/}` — phase 11.5 validators + simulation
- *(v0.2.0)* `feedback_learning/{corrections.db, corrections.md, classifications.json, pending_review.md}` — phase 13.5 store
- *(v0.2.0)* `improvement_audit/{auditor_*.md, consensus_report.md}` *(when phase 13.7 fires)*
- *(v0.2.0)* `adaptive_audit/<scope_kind>_<scope_id>_session_<sid>/{manifest.json, auditor_*.md, consensus.md}` *(per-task / per-session)*

### On-demand (only if interview confirms need)
- `CLAUDE.md`-orquestador (only if child needs autonomous orchestration)
- `.claude/skills/*` (one per domain capability the child requires)
- `.claude/agents/*` (subagents)
- `tools/` (custom scripts/prompts)
- Dashboard (none / static_html / streamlit / nextjs)
- `.git/` (only if user opts in at interview)
- Test harness scaffolding (per stack)

## Integration

- **prompt-architect** at `prompt_architect/SKILL.md` — invoked for every prompt this skill emits.
- **Tag taxonomy** at `prompt_architect/prompt_editor_skill.json` — authoritative tag source.
- **EU AI Act corpus** at `EU_AI_Act_guides/` and `Checklists y ejemplos/`.
- **Audit example** at `Ejemplo de hoja de AUDITORIA_HUMANA.xlsx` (structure derived for the generated audit sheet).
- **Anthropic best-practice corpus** at `Informes_Cursos_Anthropic/`.

## Self-audit (the generator audits itself — principle G9=A)

Every run emits `audit/self_audit.md` with:
- prompt-architect audit results for each emitted child prompt (rubric in `system_generator.json#/self_audit/rubric`).
- Mandatory-floor verification per Complex prompt (13 tags).
- Portability check: deduct 5 pts per Claude-Code-specific dependency, 10 pts per platform-only API.
- Calibration scan: count of un-probabilistic assertions in templates (target = 0).
- EU AI Act mapping completeness (% of applicable Annex III articles mapped).

If any rubric item ❌, the orchestrator iterates ≤3 times before escalating to user at GATE 2.

## Portability invocation pattern (P1)

This skill is invokable from **any LLM** that can read/write files:

1. Drop the entire `Sistem_designer/` folder into the chat (or paste its absolute path).
2. Send a prompt: *"Use system-designer to scaffold an SDD system that <intent>."*
3. The LLM reads `SKILL.md` (this file) → `system_generator.json` → `prompts/00_master_orchestrator.md` → executes.

No installation, no MCP setup, no platform-specific config required. See `references/portable_invocation.md` for the full pattern + per-platform notes (Claude Code, Cursor, Cline, Gemini CLI, Copilot CLI, Codex).

## See also

| File | Purpose |
|------|---------|
| `system_generator.json` | Machine-readable spec — phases, artifacts, gates, schemas, rubric |
| `prompts/00_master_orchestrator.md` | The actual XML prompt that runs the workflow |
| `prompts/01_interview_agent.md` | Wizard interactivo (on-demand subagent) |
| `prompts/02_scaffolder.md` | Template-rendering subagent |
| `prompts/03_prompt_factory.md` | prompt-architect wrapper for child prompts |
| `prompts/04_library_docs_fetcher.md` | Context7 + fallback fetch agent |
| `prompts/05_error_prevention_seeder.md` | Loads ~25 common AI-coding errors |
| `prompts/06_eu_ai_act_mapper.md` | Maps Articles → checklists → audit rows |
| `prompts/07_audit_designer.md` | Generates `audit/audit_sheet.xlsx` incrementally |
| `prompts/08_report_writer.md` | IMRaD + TRIPOD-AI templater |
| `prompts/09_three_auditors_jury.md` | 3 parallel auditors + meta-jury |
| `prompts/10_data_flow_validator.md` *(v0.2.0)* | Phase 11.5 — `n ∈ [3,10]` validators + 1 mandatory simulation agent |
| `prompts/11_feedback_learning_loop.md` *(v0.2.0)* | Phase 13.5 — feedback DB + classify + learn-Y/N/SKIP HITL |
| `prompts/12_improvement_jury.md` *(v0.2.0)* | Phase 13.7 — fixed 5 specialist auditors + mandatory HITL |
| `prompts/13_context_curator.md` *(v0.2.0)* | Phase 1.5 — calibrated source corpus + living updates |
| `prompts/14_adaptive_audit_meta.md` *(v0.2.0)* | Per-task / per-session 3-10 dynamic auditors with persona-fit |
| `references/calibrated_probabilities.md` | P2 implementation rules |
| `references/portable_invocation.md` | P1 pattern across LLMs |
| `references/ai_error_catalog.md` | ≥30 pre-loaded errors |
| `references/eu_ai_act_mapping.md` | Article → checklist → audit-row map |
| `references/scientific_report_format.md` | IMRaD / TRIPOD-AI / CONSORT-AI guide |
| `references/data_flow_invariants.md` *(v0.2.0)* | Invariants for phase 11.5 validators |
| `references/feedback_taxonomy.md` *(v0.2.0)* | Severity × category × recurrence taxonomy |
| `references/jury_consensus_protocol.md` *(v0.2.0)* | Shared consensus rules for prompts 12 + 14 |
| `references/context_confidence_protocol.md` *(v0.2.0)* | Source confidence taxonomy for phase 1.5 |
| `templates/` | Molds for every artifact emitted (incl. `data_flow_validation/`, `feedback_learning/`, `improvement_audit/`, `adaptive_audit/`, `context/` in v0.2.0) |
| `wizard/interview_questions.json` | Interview script |
| `wizard/defaults.json` | Sensible defaults for skipped answers |

## Version

`0.2.0` · 2026-05-08 · adds 5 new prompts (10-14), 4 new references, 5 new template trees, extended 13-phase orchestration to 17 phases (1.5, 11.5, 13.5, 13.7), per-task / per-session adaptive audit meta-validator. Backward-compatible with `0.1.0` projects via `SystemSpec.compatibility.v0_1_0` flag (skips new phases).
`0.1.0` · 2026-04-29 · core (SKILL.md + master orchestrator + system_generator.json + prompts 00-09 + references + templates + wizard).
