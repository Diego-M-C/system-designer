# 00 · Master Orchestrator

> **File.** `prompts/00_master_orchestrator.md`
> **Tier.** Complex (46 tags) — exceeds the 30-tag floor and includes all 13 mandatory Complex tags.
> **Self-audited.** This is the only prompt in the suite that audits itself via prompt-architect at G9=A level (per `system_generator.json#/self_audit`).

## 1. Purpose

The conductor of the entire generator. It owns the **13-phase state machine**, holds the **HITL gates**, and dispatches every other specialist prompt. Nothing else in the suite has cross-phase awareness — they are pure single-shot specialists.

If you delete this file, the generator stops working. If you delete any other prompt, the generator skips that phase but the others still run.

## 2. When invoked

- **Trigger.** `SKILL.md` routes here whenever the user invokes `/system-designer`, drops the folder, or asks to scaffold an SDD project.
- **Phase ownership.** All 13 phases (`read_context` → `handoff`).

## 3. Inputs

- `system_generator.json` — phase definitions, schemas, KPI list, principles.
- `wizard/interview_questions.json` + `wizard/defaults.json` — for phase 2.
- `references/*.md` — calibration, portability, AIE catalog, EU AI Act mapping, scientific reports.
- `templates/**/*.tmpl` — for phase 5 scaffold.
- `prompt_architect/SKILL.md` — for self-audit at G9 + every prompt's composition.
- `<target_path>/tracking/project.json` — if it exists (resumability).

## 4. Outputs

- All 30+ mandatory artifacts in the child tree (delegated to specialists).
- `<target_path>/tracking/project.json` — phase progression, current_phase pointer.
- `<target_path>/tracking/checkpoints/gate1.md` and `gate2.md` — HITL artifacts.
- `<target_path>/HANDOFF.md` — final.
- Signals: phase-complete events to the LLM runtime so the user sees progress.

## 5. Tag rationale (46 tags)

Why each tag earns its place:

- **`<role>`, `<persona>`, `<audience>`, `<domain>`** — orchestrator must speak to multi-LLM runtimes; declares its identity precisely.
- **`<task>`, `<sub_tasks>`** — the 13 phases are listed as sub-tasks (one per phase) so any LLM can follow without rebuilding the state machine in its head.
- **`<success_criteria>`, `<scope>`, `<priority>`, `<non_do_conditions>`** — defines what success looks like (all 13 phases complete + 2 HITL gates passed) and what's out of scope (running the child system).
- **`<context>`, `<knowledge_base>`, `<definitions>`, `<assumptions>`** — declares the world model (5 principles, EU AI Act lookup table, terminology).
- **`<temporal_context>`** — `{{TEMPORAL_NOW}}` placeholder substituted at execution time; required because the orchestrator timestamps every emitted artifact.
- **`<input>`, `<schema>`** — what comes in, what shape.
- **`<constraints>`, `<guardrails>`, `<capability_boundary>`** — three-layer enforcement: hard rules (constraints), soft rules (guardrails), what-it-cannot-do (capability_boundary).
- **`<planning>`, `<decomposition>`** — the 13-phase plan, with each phase's substeps.
- **`<verification>`, `<reflection>`** — verifies its own output and reflects per phase.
- **`<tools>`, `<tool_selection>`** — abstract tools (Tier A); selection logic per platform.
- **`<action>`, `<observation>`, `<scratchpad>`, `<state>`** — ReAct-style discipline so the orchestrator's reasoning is auditable.
- **`<delegation>`, `<handoff>`** — how it dispatches specialists and how it transfers to child orchestrator.
- **`<output>`, `<format>`, `<final_output>`, `<confidence>`, `<response_length>`** — output discipline.
- **`<stop_condition>`, `<hitl_conditions>`, `<error_handling>`, `<fallback>`** — termination logic.
- **`<orchestration>`** — ties phases together explicitly.
- **`<injection_defense>`, `<alignment_rules>`, `<compliance>`** — prompt-injection and EU AI Act compliance.
- **`<evaluation>`, `<test_cases>`, `<rubric>`, `<metrics>`** — self-evaluation criteria.
- **`<version>`, `<metadata>`, `<dependencies>`, `<cache_hint>`** — operations.

## 6. Control flow

```
1.  read_context
    ├─ load prompt-architect, references, templates, wizard, system_generator.json
    ├─ if <target_path>/tracking/project.json exists → read current_phase → resume
    └─ emit observation: "context_loaded ok"

2.  interview
    ├─ delegate → 01_interview_agent.md
    ├─ wait for SPEC.json populated
    └─ on each question: HITL (one-question-per-turn)

3.  planning_brief
    ├─ read SPEC.json + references/*.md
    ├─ emit ≥3 alternatives @ confidence% for every strategic fork
    └─ write <target>/PLAN.md

4.  GATE_1_HITL  ── BLOCKING ──
    ├─ render templates/hitl_gate.md.tmpl
    ├─ present to user
    └─ block until user picks A/B/C with rationale → write tracking/checkpoints/gate1.md

5.  scaffold
    ├─ delegate → 02_scaffolder.md
    └─ wait for child tree skeleton

6.  compose_prompts
    ├─ delegate → 03_prompt_factory.md (per emitted role)
    └─ wait for all <target>/prompts/*.md audited

7.  fetch_library_docs
    ├─ delegate → 04_library_docs_fetcher.md
    └─ best-effort; offline → log + proceed

8.  seed_tracking
    ├─ delegate → 05_error_prevention_seeder.md
    ├─ render tracking/project.json + memory/* templates
    └─ verify 30 AIE entries

9.  emit_audit_sheet
    ├─ delegate → 06_eu_ai_act_mapper.md
    ├─ delegate → 07_audit_designer.md
    └─ verify mapping_completeness_pct ≥ threshold

10. self_audit
    ├─ run 14-rubric audit on every emitted prompt (via prompt_architect)
    ├─ run P1 + P2 scans
    ├─ delegate → 09_three_auditors_jury.md (optional, per SystemSpec.auditor_mode)
    └─ write <target>/audit/self_audit.md

11. reflection
    ├─ aggregate KPIs
    ├─ list lowest-confidence decisions
    └─ write <target>/audit/reflection_session_0.md

12. GATE_2_HITL  ── BLOCKING ──
    ├─ render hitl_gate.md.tmpl with self_audit summary + dissents from jury (if any)
    ├─ present to user
    └─ block until user approves → write tracking/checkpoints/gate2.md

13. handoff
    ├─ delegate → 08_report_writer.md (final scaffolding of reports)
    ├─ write <target>/HANDOFF.md
    └─ STOP
```

## 7. Calibration anchors (P2)

The orchestrator enforces P2 at every cross-cutting decision:

- **Planning** — every alternative carries fit% summing to 100%.
- **Estimates** — duration, coverage, token usage all `value @ confidence%` or `range [lo, hi] @ confidence%`.
- **HITL gates** — render template includes mandatory fit% per option + recommended option with confidence.
- **Self-audit** — every audit row has confidence_pct.
- **Reflection** — explicitly lists lowest-confidence decisions for next session.

If any sub-prompt emits an uncalibrated assertion (forbidden token), the orchestrator's verification step rejects it and re-runs the sub-prompt up to 3 times before escalating to Gate #2.

## 8. Portability (P1)

- All `<tools>` are abstract: `fs.read`, `fs.write` (atomic), `fetch`, `now`, `prompt_architect`, optional `xlsx.write`, optional `context7.fetch`, optional `parallel.spawn`.
- Per-LLM mapping in `references/portable_invocation.md`.
- Tier A across 6+ LLMs; Tier B (manual paste) on plain web LLMs.
- The orchestrator detects platform via early `<observation>` and selects tools accordingly.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Specialist agent fails | Retry once → escalate to Gate #2 with details |
| HITL gate timed out | Block indefinitely (no auto-skip ever) |
| Context7 unavailable | Fallback ladder via `04_library_docs_fetcher.md` |
| `xlsx.write` unavailable | CSV+MD fallback via `07_audit_designer.md` |
| `parallel.spawn` unavailable | Sequential fallback via `09_three_auditors_jury.md` |
| Atomic write fails | Cleanup `*.tmp` + retry once → escalate |
| Resume from project.json with corrupted state | Halt + escalate (do not auto-recover, risk of data loss) |

## 10. HITL escalation triggers

- **GATE_1_HITL** — always.
- **GATE_2_HITL** — always.
- **Mid-phase** — only if a sub-prompt escalates and resumption is unsafe (e.g., self_audit reveals P1 or P2 violations not auto-fixable).
- **Risk-class downgrade** in high-risk-presumed domains — already gated at interview but defensively re-checked here.

## 11. Dependency edges

**Upstream (this prompt depends on):**
- `system_generator.json` (machine spec).
- `prompt_architect/SKILL.md` (P4 audit at G9).
- `references/*.md` (operational rules).

**Downstream (this prompt invokes):**
- `prompts/01..09_*.md` (specialists).
- All templates (via `02_scaffolder.md`).
- All wizard JSON (via `01_interview_agent.md`).

## 12. Test coverage

- **T1 portability** — orchestrator's `<tools>` block scanned.
- **T2 calibration** — entire prompt body scanned.
- **T4 prompt-tag floor** — Complex tier requires all 13 mandatory tags + ≥30 total.
- **T9 prompt-architect linkage** — `<alignment_rules>` cites P4 + frontmatter declares "Composed via: prompt-architect".
- **T10 HITL non-skip** — gates 1 and 2 present without auto-skip language.

## 13. Common failure modes (review checklist)

1. **Phase order corruption** — every phase except 1 (read_context) writes to `tracking/project.json#current_phase` BEFORE returning. Skipping this breaks resumability.
2. **HITL gate auto-skipped** — if a future PR tries to add `if env.SKIP_GATES then ...`, T10 should catch it but review carefully.
3. **Calibration leak** — orchestrator emits a "best alternative" without %. T2 catches it but only if the token survives in user-facing text; cross-check `<final_output>` block.
4. **Capability boundary widening** — orchestrator must NEVER fill audit rows or run the child system. If `<capability_boundary>` softens, push back.
5. **Tag drift** — Complex floor requires 13 specific tags. If any disappear (refactor), T4 catches it; reviewers should also check `system_generator.json#/self_audit/required_tags`.
