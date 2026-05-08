# Jury Consensus Protocol · Reference for Phases 13.7 & adaptive_audit_meta

> Authoritative consensus rules shared by `prompts/12_improvement_jury.md` (fixed 5-axis) and `prompts/14_adaptive_audit_meta.md` (dynamic 3-10 personas). Every aggregation behaviour in the two prompts derives from this document.
>
> Generator version: `0.2.0` · Last reviewed: `{{TEMPORAL_NOW}}`

## Audience

- Prompt 12 (improvement jury, fixed 5 axes): `regression`, `calibration`, `portability`, `eu_ai_act_drift`, `memory_integrity`. Consensus rules below apply per row of an improvement proposal.
- Prompt 14 (adaptive meta-validator, dynamic n): personas tailored to scope; findings split into `error` and `improvement` types; consensus rules apply per finding cluster.

## Verdict vocabularies

### Improvement-jury verdicts (per row, per axis)
- `approve`              — axis sees no risk to its invariants; supports merge.
- `approve_with_caveat`  — supports merge with a small noted concern.
- `dissent`              — does not block but disagrees with majority direction.
- `reject`               — blocks merge from this axis's perspective.
- `not_applicable`       — axis has no jurisdiction over this row.

### Adaptive-meta verdicts (per finding type)
- For `error` findings: each auditor reports a confidence% on the error standing.
- For `improvement` findings: each auditor reports a confidence% on the improvement being a net-positive change.

## Consensus rules — Improvement Jury (prompt 12)

For each proposal row:

```python
# 1. any axis 'reject' with conf >= 70 → row REJECTED (HITL required)
if any(verdict == 'reject' and conf >= 70):
    row_status = 'REJECTED'
    HITL_required = True

# 2. any axis 'dissent' → row DISSENT (HITL required)
elif any(verdict == 'dissent'):
    row_status = 'DISSENT'
    HITL_required = True

# 3. >=4 axes 'approve' or 'approve_with_caveat' AND mean(conf of approving) >= 75
elif (count(verdict in ('approve','approve_with_caveat')) >= 4
      and mean(approving_confs) >= 75):
    row_status = 'APPROVED'
    HITL_required = False     # batch HITL still happens at the end

# 4. otherwise
else:
    row_status = 'AMBIGUOUS'
    HITL_required = True
```

**Batch verdict.** The whole proposal is APPROVED only if `(#APPROVED / #total) >= 0.80` AND `#REJECTED == 0`. Otherwise the batch surfaces with row-level breakdown.

**The post-consensus HITL gate is mandatory** regardless of batch verdict. No source change applies without explicit human approval.

## Consensus rules — Adaptive Meta-Validator (prompt 14)

For each finding cluster (group findings by `invariant_or_idea_signature`):

### Error path

```python
if max(cluster.conf) >= 70:
    status = 'BLOCKER'        # orchestrator pauses next task
elif count(cluster, conf in [50,69]) >= 2:
    status = 'WARNING'        # surfaces at next HITL gate
else:
    status = 'WEAK'           # logged; no action
```

### Improvement path

```python
weighted_mean = sum(cluster.confs) / len(cluster.confs)
spread        = max(cluster.confs) - min(cluster.confs)

if weighted_mean >= 70 and spread <= 30:
    status = 'QUEUE_FOR_HITL'      # row inserted into corrections.db pending_review
elif weighted_mean >= 70 and spread > 30:
    status = 'DISSENT_HITL_NOW'    # surface immediately to user
else:
    status = 'DEFER'               # logged; no action
```

## Why "confidence-weighted but not confidence-blind"

Pure majority voting collapses dissent. Pure unanimity blocks any progress on close calls. The protocol therefore:

1. **Preserves dissent** explicitly (`DISSENT`, `DISSENT_HITL_NOW`) — surfaces it instead of averaging it.
2. **Requires a confidence floor** (`mean ≥ 75` for improvement-jury approval; `≥ 70` for adaptive blockers/queues) — protects against confident-by-accident outliers.
3. **Treats spread as a signal** (improvement path) — wide disagreement at high mean confidence is a stronger HITL trigger than narrow disagreement at low mean.

## Recommended owners per axis (improvement-jury default)

| axis | typical owner |
|---|---|
| `regression`         | the engineer who emitted the proposal in 13.5 |
| `calibration`        | the calibration steward / P2 reviewer |
| `portability`        | the P1 reviewer / runtime engineer |
| `eu_ai_act_drift`    | the regulatory archivist / compliance lead |
| `memory_integrity`   | the memory steward |

For adaptive-meta panels, the recommended owner is the persona whose lens raised the finding (with confidence-weighted tie-breaking).

## Cross-prompt invariants

- Both prompts MUST: keep dissent visible; never auto-merge; always surface a HITL block when a blocker / dissent / ambiguity exists; persist consensus reports atomically.
- Both prompts MUST NOT: collapse dissent into approval-with-caveat; block on a single low-confidence outlier; modify source files.

## Versioning

Threshold values (`75`, `70`, `30`, `0.80`) are calibrated against pilot runs (≈85% confidence in their level). Any change requires:
1. A row in `feedback_learning/corrections.db` (`category=HITL` or `tooling`).
2. Approval at phase 13.7 itself (the protocol auditing its own update is a meta-test).
3. A changelog entry in this file's `## Changelog` section.

## Changelog

- `0.2.0` — initial protocol with the 4 improvement-jury rules + 3 error rules + 3 improvement rules for adaptive meta.
