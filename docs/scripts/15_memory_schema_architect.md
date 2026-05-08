# 15 · Memory Schema Architect

> **File.** `prompts/15_memory_schema_architect.md`
> **Tier.** Complex (~42 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.3.0

## 1. Purpose

Negotiates with the human **what exactly the memory of THIS project must store** — per module, per format (JSON / JSONL / structured Markdown), per trigger, with calibrated audit completeness rules. The negotiated schema becomes a contract that the **mandatory** `memory_completeness_auditor` persona inside `prompts/14_adaptive_audit_meta.md` audits against on every task and every session — both at particular level (a specific process inside a phase) and at global level (the whole project's memory state).

Memory is the foundation: an over-broad schema produces noise; an under-broad schema produces silent failure. This phase makes the trade-off explicit and human-owned.

## 2. When invoked

- **Phase 4.5** — strictly between `GATE_1` approval and `scaffold` (phase 5). Mode = `bootstrap`.
- Inherited by the child orchestrator: re-invokable at session boundaries in `living_update` mode.
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true` OR `SystemSpec.memory_schema.negotiation_enabled == false` (wizard Q37). When skipped, the meta-validator's mandatory `memory_completeness_auditor` falls back to checking only the Anthropic 4-typed baseline.

## 3. Inputs

- `<target_path>/SPEC.json` — domain / risk / stack / granularity / regulations.
- `<target_path>/tracking/project.json` — phase state (Gate #1 must be `approved`).
- `<target_path>/audit/planning_brief_session_0.md` — disambiguates domain nuances.
- `references/memory_schema_protocol.md` — authoritative protocol.
- `templates/memory_schema/per_domain_starters/<domain>.json` — 6 starters.

## 4. Outputs (under `<target_path>/memory_schema/`)

- `manifest.json` — authoritative contract.
- `manifest.md` — regenerated mirror.
- `modules/<module_name>.json` — per-module schema (one file per module).
- `negotiation_session_<id>.md` — HITL audit trail (starter chosen, edits, rejections, reflection).

Plus updates to `tracking/project.json#memory_schema`.

## 5. Field flags (4 levels)

| flag | semantics |
|---|---|
| `mandatory`              | must be present in every entry; absence is an audit BLOCKER |
| `mandatory_if_<cond>`    | conditional mandate (e.g., `mandatory_if_status!=pass`); BLOCKER under condition |
| `recommended`            | should be present; absence is a WARNING (not blocker) |
| `optional`               | nice-to-have; absence is silent |

## 6. Format options (3 choices)

| format | when to choose |
|---|---|
| `json`           | small index-style modules (rewrite each update); e.g., `milestone_checkpoints` |
| `jsonl`          | high-volume event-style modules (append-only, one event per line); e.g., `test_outcomes` |
| `structured_md`  | narrative-plus-fields modules with frontmatter + table sections; e.g., `refactor_history`, `hypothesis_log` |

## 7. The user's anchor example (informatics_dev · `test_outcomes`)

```json
{
  "name": "test_outcomes",
  "format": "jsonl",
  "trigger": "every test execution",
  "fields": [
    { "name": "test_number",                 "flag": "mandatory" },
    { "name": "attempt_number",              "flag": "mandatory" },
    { "name": "status",                      "flag": "mandatory" },
    { "name": "error_code",                  "flag": "mandatory_if_status!=pass" },
    { "name": "error_message",               "flag": "mandatory_if_status!=pass" },
    { "name": "suggested_solution",          "flag": "mandatory_if_status!=pass" },
    { "name": "suggested_solution_conf_pct", "flag": "mandatory_if_suggested_solution" }
  ],
  "audit": {
    "completeness_rule": "every entry with status != pass must have error_code AND error_message AND suggested_solution AND suggested_solution_conf_pct",
    "missing_threshold_pct": 5
  }
}
```

This is the calibrated anchor for `informatics_dev`. The user's question "test nº 1 prueba 1 éxito? si no error X sugerencia de solución" maps directly into the conditional mandates.

## 8. Per-domain starters (6)

| starter_id | mandatory modules (illustrative) |
|---|---|
| `informatics_dev`     | test_outcomes, decision_logs |
| `healthcare_clinical` | patient_cohort_signatures (anonymised), adverse_events |
| `fintech`             | transaction_pattern_audits, regulatory_changes_tracked |
| `legal`               | case_law_references, regulatory_correspondence |
| `public_sector`       | policy_changes_tracked, citizen_feedback_categories |
| `research`            | hypothesis_log, experiment_runs |

For `domain=other`: agent refuses default; user picks 1-2 closest starters; agent composes a hybrid.

## 9. Two-tier audit (enforced by prompt 14)

- **Particular** — for the scope at hand: did each contracted trigger produce its entry? Are mandatory fields populated?
- **Global** — across all sessions: are missing-thresholds breached? Are any modules empty across N sessions?

Both tiers run on every adaptive_audit invocation. Findings flow into the existing BLOCKER / WARNING / WEAK + QUEUE_FOR_HITL / DISSENT_HITL_NOW / DEFER paths.

## 10. HITL surface (mandatory)

```
=== MEMORY SCHEMA NEGOTIATION ===
Domain: <d>  ·  EU AI Act risk: <r>  ·  Stack: <s>
Starter chosen: <id>  (agent confidence ≈X%)

[A] Accept all proposed modules as-is.
[B] Edit a specific module (you list module# and changes).
[C] Add a new module (you describe; I propose schema; we iterate).
[D] Skip negotiation and use only the baseline 4-typed Anthropic memory (NOT recommended).
=== /MEMORY SCHEMA NEGOTIATION ===
```

No contract persists without an explicit human keystroke. `[D]` requires double-confirmation with explicit warning about audit blind spots.

## 11. Calibration & portability anchors

- Every field flag carries `confidence_pct`. Every audit threshold carries `confidence_pct`. The negotiation record logs `agent_confidence_pct` on the contract as a whole.
- JSON / JSONL / structured Markdown are universal — Tier-A portability holds.

## 12. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` at phase 4.5; by child orchestrator at session boundaries (living_update mode).
- ↓ delegates field-rationale and hybrid-starter sub-prompts to `prompts/03_prompt_factory.md`.
- → reads `references/memory_schema_protocol.md`, 6 per-domain starters.
- ← consumed by phase 5 (scaffold renders structured-memory module files), phase 14 (mandatory `memory_completeness_auditor` reads manifest as contract), phase 13.5 (improvement_proposal can suggest schema changes), phase 13.7 (5-axis jury audits proposed schema changes before merge).

## 13. Common failure modes

- **`domain=other` collapse** — user accepts a single starter where a hybrid would have been better; reflection flags it; offer re-negotiation at next session.
- **Conditional-mandate collapse** — user lowers `mandatory_if_<cond>` to `recommended` without rationale; flagged in negotiation record; future re-negotiation is a strong candidate.
- **Threshold drift** — user sets `missing_threshold_pct` >20%; HITL surfaces; over-permissive thresholds defeat audit purpose.
- **Schema not consumed** — child writes events outside the contracted modules; `memory_completeness_auditor` flags as drift; orchestrator surfaces at HITL.
- **High-risk regulator floor** — user attempts to remove `non_removable_for_high_risk` modules (e.g., `adverse_events` in healthcare); HITL surfaces regulatory warning; user can override with rationale logged to `decisions.md`.
