# 12 · Improvement Jury · 5 Specialist Auditors

> **File.** `prompts/12_improvement_jury.md`
> **Tier.** Complex (~38 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.2.0

## 1. Purpose

Audits a candidate `improvement_proposal.md` (emitted by phase 13.5) along **5 fixed axes** in parallel, applies a confidence-weighted consensus rule, and gates any source change behind a **mandatory HITL gate**. This is the **fixed-5-persona special case** of the general engine at `prompts/14_adaptive_audit_meta.md`.

## 2. When invoked

- **Phase 13.7** — when `feedback_learning_loop` (phase 13.5) signals a triggered proposal.
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true`.
- Re-invocable on `[D] Send back` to phase 13.5 → after re-draft → re-audit cycle.

## 3. Inputs

- `<target_path>/feedback_learning/improvement_proposal.md` — the candidate batch.
- `<target_path>/feedback_learning/corrections.db` — referenced rows (queried).
- Baselines: `data_flow_validation/.../consolidated_report.md` (regression), `audit/audits/jury_session_<id>.md` (calibration & EU drift), `audit/self_audit.md` (portability), `memory/MEMORY.md` + `memory/*.md` (memory integrity).
- `references/jury_consensus_protocol.md` — the protocol enforced.

## 4. Outputs (under `<target_path>/improvement_audit/`)

- `auditor_<n>_<axis>_session_<id>.md` (× 5) — per-axis verdicts.
- `consensus_report.md` — matrix × consensus + HITL gate.
- `archive/<id>/` — on rejection.

Plus DB status updates on `corrections` rows under transactional control.

## 5. The 5 fixed axes

- **regression** — does not undo prior fixes (`AIE-NNN`); does not break phase-11.5 invariants.
- **calibration** — preserves P2; no forbidden tokens; existing % bands not weakened.
- **portability** — preserves P1; no Claude-Code-only or platform-specific identifiers.
- **eu_ai_act_drift** — does not weaken `audit/eu_ai_act_mapping.md` coverage; no risk-class downgrade without `decisions.md` rationale.
- **memory_integrity** — no entries added without explicit `learn_in_system=Y` row; index ↔ files coherent.

## 6. Per-axis verdicts

`approve` · `approve_with_caveat` · `dissent` · `reject` · `not_applicable` (each with confidence%).

## 7. Confidence-weighted consensus

```
# Per row:
if any(verdict == 'reject' and conf >= 70):           row_status = REJECTED
elif any(verdict == 'dissent'):                       row_status = DISSENT
elif (count(approve|approve_with_caveat) >= 4
      and mean(approving_confs) >= 75):               row_status = APPROVED
else:                                                 row_status = AMBIGUOUS

# Batch:
if (#APPROVED / #total) >= 0.80 and #REJECTED == 0:   batch = APPROVED
else:                                                 batch = HITL_REQUIRED
```

Dissent is **preserved**, never averaged into approve_with_caveat.

## 8. HITL gate (mandatory)

```
[A] Approve all APPROVED rows; reject DISSENT/REJECTED; archive AMBIGUOUS
[B] Approve subset (you list row_ids)
[C] Reject the entire batch
[D] Send back to phase 13.5 with notes
```

No source change merges without an explicit human reply. On approval: `UPDATE corrections.status='approved' WHERE id IN (...)` in a single transaction.

## 9. Calibration & portability anchors

- Every verdict has a confidence%; ranges anchored to evidence (file:line).
- Every auditor composed via `prompts/03_prompt_factory.md` → P1 inherited.
- Sequential fallback documented when `parallel.spawn` unavailable.

## 10. HITL escalation triggers (within the gate)

- Any `reject` with confidence ≥ 70 — emphasised.
- Any auditor self-confidence < 70% — flagged in gate header.
- `not_applicable` rows > 20% of batch — surface (potential proposal mis-scope).
- User chooses [B] or [D] — block on row_ids / notes.

## 11. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` at phase 13.7 (when 13.5 signals).
- ↓ delegates 5 auditor compositions to `prompts/03_prompt_factory.md`.
- → reads `references/jury_consensus_protocol.md`, baselines.
- ← updates `corrections.db` statuses; archives rejected proposals.

## 12. Test coverage

- T11 / T14 confirm prompt + 5-axis discipline.
- 7 in-prompt `<test_cases>`: unanimous / one-axis-rejects / dissent / low-confidence-unanimity / sequential / DB transaction fail / send-back.

## 13. Common failure modes

- **Auditor unrecoverable** — Factory fails 3 times for one axis → refuse to run with <5; escalate.
- **DB transaction conflict** — UPDATE rolls back; no status changes; user notified; jury can re-run on the same proposal.
- **Send-back loop** — user repeatedly chooses [D]; track loop_count in `tracking/project.json#improvement_audit.send_back_count`; > 3 surfaces a meta-warning.
- **Pure-doc proposal** — touches no axis; 5 `not_applicable` → `AMBIGUOUS` batch by design; HITL surfaces immediately.
