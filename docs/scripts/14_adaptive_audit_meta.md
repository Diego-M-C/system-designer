# 14 · Adaptive Audit Meta · Per-Task / Per-Session 3-10 Specialist Auditors

> **File.** `prompts/14_adaptive_audit_meta.md`
> **Tier.** Complex (~44 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.2.0

## 1. Purpose

A **meta-generator of validation-layer auditors**. Given a scope (a task or a session), this prompt computes how many auditors are needed (3–10) from a calibrated importance score, and **freshly composes each auditor via prompt-architect** with a persona that is an actual expert in the thing being audited. Auditors run in parallel, separate **errors** (must-address blockers) from **improvements** (queued for phase 13.5), and surface HITL only when needed. Prompt 12 is the fixed-5-axis special case; prompt 10 is a scope-specialised special case.

## 2. When invoked

- **Cross-phase** — at the **end of every task** AND at every **session end** in BOTH the generator (per-phase) and the inherited child.
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true` OR the user opts out at wizard Q35.

## 3. Inputs

- Scope envelope from orchestrator: `{scope_kind: task|session, scope_id, scope_summary, artifacts_in_scope[], eu_risk, touched_modules[], importance_signals, parallel_capability_available}`.
- `<target_path>/tracking/project.json` — invocation history + thresholds.
- `references/jury_consensus_protocol.md` — shared with prompt 12.
- `prompt_architect/prompt_editor_skill.json` — persona/focus tag taxonomy.

## 4. Outputs (under `<target_path>/adaptive_audit/<scope_kind>_<scope_id>_session_<sid>/`)

- `manifest.json` — scope envelope snapshot + n + persona list + deviation rationale (if any).
- `auditor_<i>_<persona_slug>.md` (× n) — per-auditor with self-KPI block.
- `consensus.md` — agreement matrix × errors × improvements × KPI roll-up + reflection.

Plus inserts into `feedback_learning/corrections.db` for queued improvements (`status=pending_review`, `learn_in_system=2 (SKIP)` until phase 13.5 prompts).

## 5. Importance score (0–100, calibrated)

```
importance =
    (eu_risk == 'high' ? 30 : eu_risk == 'limited' ? 15 : 5)
  + (touched_modules contains 'safety_floor'              ? 20 : 0)
  + (touched_modules contains 'calibration'               ? 15 : 0)
  + (touched_modules contains 'memory'                    ? 15 : 0)
  + (touched_modules contains 'prompt_architect_floor'    ? 15 : 0)
  + (touched_modules contains 'HITL_logic'                ? 15 : 0)
  + (touched_modules contains 'eu_ai_act_mapping'         ? 10 : 0)
  + ceil(len(artifacts_in_scope) / 5)
  clamp [0, 100]

n_auditors = clamp(3, round(importance / 10), 10)
```

Examples: rename a doc heading → n=3 · update calibration scan → n=5 · edit master orchestrator HITL → n=8 · scaffold high-risk healthcare → n=10.

## 6. Persona library (illustrative; Factory may compose any plausible expert)

`regulatory_archivist` · `calibration_skeptic` · `portability_engineer` · `prompt_rubric_specialist` · `memory_discipline_steward` · `data_flow_integrity_lead` · `hitl_governance_auditor` · `living_doc_curator` · `error_taxonomy_curator` · `simulation_designer` · `ux_clarity_critic` · `domain_expert_<slug>` (e.g., `oncology_clinician`, `compliance_lawyer`, `fraud_analyst`).

**Persona-fit is enforced** — generic personas trigger re-composition in reflection. Each auditor declares its own KPIs (composed in by Factory).

## 7. Consensus rules (separate paths for errors and improvements)

### Errors

```
if max(cluster.conf) >= 70:                        status = BLOCKER
elif count(cluster, conf in [50,69]) >= 2:         status = WARNING
else:                                              status = WEAK
```

### Improvements

```
weighted_mean = mean(cluster.confs)
spread        = max(cluster.confs) - min(cluster.confs)

if weighted_mean >= 70 and spread <= 30:           status = QUEUE_FOR_HITL  → corrections.db
elif weighted_mean >= 70 and spread > 30:          status = DISSENT_HITL_NOW
else:                                              status = DEFER
```

## 8. Calibration & portability anchors

- Every finding carries confidence%.
- Each auditor freshly composed via `prompts/03_prompt_factory.md` → P1 inherited.
- SQL parameterised; no auditor output ever interpolated into SQL strings.

## 9. HITL escalation triggers

- Any error reaches `BLOCKER` — orchestrator pauses next task.
- Any improvement reaches `DISSENT_HITL_NOW` — surface immediately.
- `n_auditors` clamps at 10 — possible under-coverage.
- Persona-fit reflection flags any auditor as generic — surface for re-composition.
- Auditor self-confidence < 60% — flag the audit as weak.

## 10. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` (cross-phase hook) and by the child orchestrator at task/session boundaries.
- ↓ delegates every auditor composition to `prompts/03_prompt_factory.md`; persona briefs derived from scope.
- → reads `references/jury_consensus_protocol.md`, `prompt_architect/prompt_editor_skill.json`.
- ← inserts into `feedback_learning/corrections.db` (improvement rows queue for phase 13.5); signals orchestrator with blockers.

## 11. Why this is the general engine

- **Prompt 12 (improvement_jury)** = fixed 5 axes (regression / calibration / portability / eu_drift / memory) for the post-improvement audit.
- **Prompt 10 (data_flow_validator)** = scope-specialised for the structural snapshot at phase 11.5; includes 1 mandatory simulation agent.
- **Prompt 14 (this one)** = general engine. Different `n` and different personas per call. Both 12 and 10 can be conceptualised as `adaptive_audit_meta` configurations with constrained inputs.

## 12. Test coverage

- T11 / T15 / T16 confirm prompt + range-doc + templates.
- 8 in-prompt `<test_cases>`: low-importance / high-importance / critical-error / dissent / sequential / auditor-crash / persona-fit-flag / DB-unavailable.

## 13. Common failure modes

- **Generic persona slip** — Factory returns a persona slug like `generic_critic`; reflection catches it; re-composition triggered (max 3 retries).
- **Importance score floor** — touched_modules empty + artifacts_in_scope < 5 + eu_risk minimal → importance ≈ 5 → n=3 (the floor); reflection notes possible under-coverage.
- **DB unavailable** — improvements written to `improvements_queued.json` sidecar; phase 13.5 ingests on next run.
- **HITL fatigue** — surface only when needed (blocker / DISSENT_HITL_NOW). Routine queueing happens silently to `corrections.db`; user reviews at phase 13.5 in batch.
