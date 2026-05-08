# 10 · Data Flow Validator + Structural Consistency Auditors

> **File.** `prompts/10_data_flow_validator.md`
> **Tier.** Complex (~40 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.2.0

## 1. Purpose

Captures a structural snapshot of the freshly-scaffolded child tree and dispatches **`n ∈ [3, 10]` specialist validators plus 1 mandatory simulation agent** to verify that data lineage, memory graph, inter-module communication, schema integrity, and atomic-write discipline are coherent end-to-end. The certificate of "this living architecture really memorises and inter-communicates as designed" before Gate #2.

## 2. When invoked

- **Phase 11.5** — strictly after `reflection` (phase 11) and strictly before `GATE_2_HITL` (phase 12).
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true`.
- Not invoked at runtime by the child system (the child has its own `adaptive_audit_meta` panels).

## 3. Inputs

- `<target_path>/tracking/project.json` — `current_session_id`, `artifacts_emitted[]`, `eu_ai_act_risk`, `audit_completeness_pct`.
- `<target_path>/tracking/sessions/<id>/observations.jsonl` — per-action lineage with sha256.
- `<target_path>/audit/{self_audit, audits/jury_session_<id>}.md` — phase-10 baseline.
- `<target_path>/{memory, prompts, SPEC.json, PLAN.md, HANDOFF.md}` — read-only.
- `references/data_flow_invariants.md` — the catalogue of ≈30 invariants the validators check.

## 4. Outputs (under `<target_path>/data_flow_validation/`)

- `sequence_snapshots/snapshot_session_<id>.md` — file inventory + dependency edges + state-machine snapshot.
- `structural_consistency/validators_manifest.json` — formula trace + chosen personas + outputs map.
- `structural_consistency/validator_<n>_<persona>.md` (× `n_validators`) — schema in `templates/data_flow_validation/validator_result.md.tmpl`.
- `structural_consistency/simulation_report.md` — the 5 mandatory scenarios.
- `structural_consistency/consolidated_report.md` — agreement matrix, dissents, escalations, `consistency_score` (0–100).

## 5. Validator-count formula (calibrated)

```
n_validators = clamp(
  3,
  ceil(artifacts_emitted / 30)
  + ceil((100 - audit_completeness_pct) / 20)
  + (eu_ai_act_risk == "high" ? 2 : 0),
  10
)
```

`+1` mandatory simulation agent is always added on top.

## 6. Validator personas (menu)

`data_lineage_auditor` · `memory_consistency_auditor` · `intercom_auditor` · `schema_integrity_auditor` · **`simulation_agent` (mandatory)** · `lifecycle_auditor` · `calibration_consistency_auditor` · `portability_consistency_auditor` · `error_catalog_drift_auditor` · `eu_act_traceability_auditor`. The first 3 are the floor; the rest are added by the formula.

## 7. The 5 mandatory simulation scenarios

- **S1 · Resumability** — synthetic interrupt at phase 5; verify resumption is unambiguous from `tracking/project.json#current_phase`.
- **S2 · Library-doc fetch failure** — Context7 + primary URL fail; walk fallback ladder; PASS if it ends at `OFFLINE.md`.
- **S3 · Jury dissent preservation** — inject conflicting auditor verdicts; PASS if dissent surfaces (not averaged).
- **S4 · Calibration drift** — inject `always`-token; PASS if regex + LLM scan both fire.
- **S5 · Atomic-write race** — sample 5 writes from `observations.jsonl`; PASS if all show `tmp_path → final_path`.

## 8. Consistency score derivation

```
score = 100
  - 5 × dissents_count
  - 3 × low_confidence_findings (<70%)
  - 2 × partial_status_count
  - 10 × any_failed_simulation_scenario
  clamp [0, 100]
```

Score `< 80` → Gate #2 escalation.

## 9. Calibration & portability anchors

- Every finding carries a confidence%; floors per-invariant in `references/data_flow_invariants.md`.
- All validators composed via `prompts/03_prompt_factory.md` → P1 inherited.
- `parallel.spawn` soft; sequential fallback documented in the consolidated report.

## 10. HITL escalation triggers

- `consistency_score < 80`
- Any simulation scenario fails
- Any dissent flagged
- `n_validators` clamps at 10 (potential under-coverage signal)
- Simulation agent self-confidence < 70%

## 11. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` at phase 11.5.
- ↓ delegates to `prompts/03_prompt_factory.md` for every validator + simulation prompt.
- → reads `references/data_flow_invariants.md`, baselines from phase 10.
- ← consumed by Gate #2 (escalations) and phase 13.7 (the improvement jury reads this to gauge regression baselines).

## 12. Test coverage

- T11 / T16 confirm the prompt + templates exist.
- T15 confirms `n_auditors` range 3..10 documented (shared with prompt 14).
- 6 in-prompt `<test_cases>` covering tiny / high-risk / dissent-injected / simulation-fail / no-parallel / write-retry.

## 13. Common failure modes

- **Generic personas** — formula clamps at 10 but personas not tailored to the child's domain → flagged in reflection; orchestrator re-composes.
- **Simulation flakiness** — scenario `pending` instead of pass/fail when the agent cannot evaluate (e.g., `observations.jsonl` empty). Always escalates to Gate #2.
- **Stale snapshot** — if a file is written between snapshot and validator dispatch, sha256 drift triggers a re-snapshot (max 1 retry).
