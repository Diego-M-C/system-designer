---
jury_session_id: feedback-layer-consensus-v100-2026-05-09
ran_at: 2026-05-09T13:42:00Z
auditors_consulted: [routing, hitl, implementation]
batch_verdict: NEEDS_IMPROVEMENT
batch_confidence_pct: 83
findings_consolidated_count: 17
findings_with_dissent_count: 1
total_estimated_effort_hours: 38-58
recommended_release: v1.1.0
---

# Consensus Jury · Feedback-Layer Audit · system-designer v1.0.0 → v1.1.0

> Synthesis of three independent Opus auditor reports on the feedback-learning layer (phases 13.5, 13.7, adaptive_audit_meta, and the dashboard surface). Applies the protocol declared in `references/jury_consensus_protocol.md`, treating each axis as one auditor and each consolidated finding as one row of the improvement proposal. Read-only audit — no source files were modified.

## 1. Per-axis verdicts (matrix)

| Axis | Auditor | Verdict | Confidence | Findings raised | Effort range (h) | Lane focus |
|---|---|---|---:|---:|---:|---|
| routing            | A | NEEDS_IMPROVEMENT     | 82% | 8 | 20–34 | error-memory routing — capture → consumption |
| hitl               | B | APPROVED_WITH_MINOR   | 84% | 6 |  ~4.3 | HITL capture surface + dashboard rendering |
| implementation     | C | NEEDS_IMPROVEMENT     | 82% | 9 |  ~22.5 | proposal → merge cycle + post-merge audit |

Three auditors, 23 raw findings. Mean axis confidence ≈ 82.7%. Verdict spread: 2 NEEDS_IMPROVEMENT vs 1 APPROVED_WITH_MINOR — confidence on the dissenting (B) verdict (84%) sits above its own findings' anchor depth and is consistent with the lane it owns being the most-anchored part of the system (the ≥4-prose-layer never-default invariant). Confidence in the matrix as a fair summary: 90%.

## 2. Batch verdict (with derivation)

**Verdict: `NEEDS_IMPROVEMENT` at 83% confidence.**

Derivation under `references/jury_consensus_protocol.md` §"Consensus rules — Improvement Jury":

- 0 axes report `reject` at ≥70% confidence → rule 1 does not fire (no hard REJECT).
- 2 axes report `NEEDS_IMPROVEMENT` (treated here as `dissent` from approval) at 82% confidence each → rule 2 fires (dissent above the dissenter floor of 75%) → `row_status = DISSENT, HITL_required = True`.
- The 2/3 dissent vote also fails rule 3 (which would need ≥4 of 5 axes approving — n/a at 3 axes; the operational equivalent is unanimity-minus-one).

Under the protocol the consensus is `NEEDS_IMPROVEMENT`. Auditor B's `APPROVED_WITH_MINOR` is preserved as a documented dissent — it is correct in its own lane (HITL capture is mature) and is not collapsed into the majority. The batch verdict reflects the ROUTING and IMPLEMENTATION lanes carrying tractable but real architectural seams that the v1.0.0 maturity claim did not surface. Confidence in derivation: 92%.

**Honest framing.** The system was declared mature at v1.0.0 by a global audit. This focused audit confirms the *substrate* (SQLite + FTS5 + dual mirror + status-based lifecycle + 5-axis jury + 6-anchor never-default invariant) is genuinely production-grade. The seams are in **the routing graph** — between capture and consumption (lane A) and between proposal-approval and post-merge verification (lane C). The system is not broken; it is half-routed.

## 3. Strengths the panel converged on

| # | strength | axes_confirming | mean_confidence_pct |
|---|---|---|---:|
| S-1 | HITL inviolability is genuinely defended-in-depth (≥4 independent prose layers + SQL CHECK on never-default-`learn_in_system`; post-consensus HITL gate is `ALWAYS regardless of batch verdict`). | routing + hitl + implementation | 93 |
| S-2 | Dissent is preserved structurally (no auto-collapse into approve_with_caveat at protocol level; HITL_required on any dissent). | routing + implementation | 92 |
| S-3 | Status-lifecycle is reconstructable from DB at any future point — fit for EU AI Act Art. 12 traceability (no row deletions, status enum CHECK, atomic transitions, parameterised SQL). | routing + implementation | 92 |
| S-4 | Threshold rule is deterministic and observable (single SQL count + override; pending_review.md surfaces BELOW/AT_THRESHOLD/ABOVE; FTS5 substrate idiomatic). | routing + hitl | 91 |
| S-5 | Per-correction HITL block INFORMS before asking (severity / category / recurrence / classification confidence% / proposed action with its own confidence% / per-choice consequence text). ISO 9241-110 self-descriptive. | hitl | 92 |

These strengths are the reason the system carries a v1.0.0 maturity claim defensibly. The remediation in §4 is additive — not a redesign.

## 4. Consolidated improvement checklist (v1.1.0 batch)

Findings deduplicated across axes. Where two or more auditors flagged overlapping issues they are merged into a single J-NNN with `axes_supporting` and `confidence_spread` recorded. Numbering starts at **J-100** to namespace from the prior global-audit cycle's J-001..J-021.

| J-id | concrete_action | axes_supporting | priority | severity | mean_conf% | spread | evidence | effort_h | target | depends_on |
|---|---|---|---|---|---:|---:|---|---:|---|---|
| **J-100** | `templates/CLAUDE.md.tmpl:24-37` × ADD bullet 5b "Read `feedback_learning/corrections.md` filtered to `status IN ('approved','incorporated') AND learn_in_system=1`" × outcome: agent reads memorised corrections at session start (closes user anchor concern). | routing | P0 | error | 92 | 0 | `templates/CLAUDE.md.tmpl:24-37`; A-F1 | 1–2 | v1.1.0 | — |
| **J-101** | `prompts/12_improvement_jury.md:454` + new `prompts/13_8_merge_verification.md` × ADD phase 13.8 prompt: reads latest `consensus_report.md` APPROVED, diffs `Sistem_designer/` pre-jury vs post-merge commit, dispatches `merge_verification_auditor`, only then transitions `corrections.status='approved' → 'incorporated'`. | implementation | P1 | error | 88 | 0 | `prompts/12_improvement_jury.md:41,454`; `prompts/11_feedback_learning_loop.md:67`; `references/feedback_taxonomy.md:73`; C-F-IC-01/02/03 | 5–7 | v1.1.0 | J-103 |
| **J-102** | **CONSUMPTION GAP CLUSTER** · `prompts/11_feedback_learning_loop.md:215-220` (post-13.7 branch) × WIRE: on `category=memory & status=approved` → signal phase 4.5 `living_update` with `manifest.json#evolution_log[]` write; on `category in {tooling,calibration,prompt_architect,portability}` → draft AIE-NNN entry append to `tracking/errors_catalog.json` with `preloaded:false, first_seen_session=<correction.session_id>`. | routing + implementation | P1 | error | 84 | 0 | A-F2 + A-F4; `prompts/15_memory_schema_architect.md:30-40`; `references/ai_error_catalog.md:264-274`; `templates/memory_schema/manifest.json.tmpl:11-13` (evolution_log placeholder unused) | 9–14 | v1.1.0 | — |
| **J-103** | `templates/feedback_learning/corrections_schema.sql.tmpl:9-30` × ADD columns `proposal_id TEXT`, `consensus_report_sha256 TEXT`, `incorporated_commit_sha TEXT`, `incorporation_kind TEXT CHECK(incorporation_kind IN ('memory','source','both','manifest_evolution','aie_extension'))` (all NULLable) × outcome: cycle trail join keys + status-semantics discriminator. Backwards-compatible. | routing + implementation | P1 | error | 87 | 5 | A-F5 + C-F-IC-06; `corrections_schema.sql.tmpl:23-29`; `prompts/11_feedback_learning_loop.md:172-176` | 2–3 | v1.1.0 | — |
| **J-104** | `templates/tracking/project.json.tmpl` × ADD `improvement_audit` and `feedback_learning` blocks matching the keys prompts 11 & 12 already write to blind × outcome: schema drift between prompts and template eliminated. | implementation | P1 | error | 95 | 0 | C-F-IC-08; `prompts/12_improvement_jury.md:288-301`; `prompts/11_feedback_learning_loop.md:295-306`; verified absent in `templates/tracking/project.json.tmpl` | 1 | v1.1.0 | — |
| **J-105** | **OBSERVABILITY GAP CLUSTER** · `dashboard/index.html:278-285` × IMPLEMENT `getNested(data, m.path)` fallback when `kpis[m.key]` is undefined; `:337` × CHANGE static "KPIs (11)" to dynamic `KPIs (${KPI_META.length})` × outcome: the four v0.3.x feedback / adaptive_audit / Art.73 / data-flow tiles render the surfaces they declare. | hitl + implementation | P1 | warn | 91 | 6 | B-F1 + B-F2 + C-F-IC-05 (partial — full cycle_trail in J-110); `dashboard/index.html:219-242,278-285,337` | 1.2–1.8 | v1.1.0 | — |
| **J-106** | `prompts/14_adaptive_audit_meta.md:34-44` × ADD pre-action recurrence guard: when adaptive auditor builds a scope envelope, run an FTS5 query against `corrections` filtered to `status IN ('approved','incorporated') AND recurrence IN ('recurring','systemic')`; surface as `prior_lessons[]` field in the envelope. | routing | P1 | error | 80 | 0 | A-F3; `prompts/11_feedback_learning_loop.md:244-249` (FTS5 currently only a write-time classifier) | 4–6 | v1.1.0 | J-100 |
| **J-107** | `tests/run_all.sh` + `tests/README.md:38-46` × ADD T24: grep `prompts/11_feedback_learning_loop.md` for any `default.*learn_in_system` pattern outside negation/refusal context; fail if found × outcome: closes the only missing layer of the never-default invariant (9 prose+SQL anchors + 1 test = 10). | hitl | P2 | warn | 88 | 0 | B-F3; `tests/run_all.sh` (no current T-id covers silent-default regression) | 1.2–1.8 | v1.1.0 | — |
| **J-108** | `prompts/12_improvement_jury.md:99-106` × DECISION: keep fixed 5 axes; instead dispatch `prompts/14_adaptive_audit_meta.md` in parallel for `external_dependency_audit` whenever proposal cites EU AI Act / AESIA / ISO references and `child_compatibility_audit` whenever proposal touches `memory_schema/manifest.json` or template schemas × outcome: closes 5-axis coverage gap without destabilising the fixed-5 contract. | implementation | P2 | warn | 78 | 0 | C-F-IC-09; `prompts/00_master_orchestrator.md:600-621` (Sistem_designer ships scaffolds whose contract is the manifest schema) | 3–5 | v1.2.0 | — |
| **J-109** | `prompts/00_master_orchestrator.md:75` + new manifest entry × ADD `meta_skill_self_scope` envelope: prompt 14 fires on `Sistem_designer/` after each merged J-NNN, treating the meta-skill source as a virtual child. Operationalises "eat-one's-own-dog-food" beyond narrative. | implementation | P2 | warn | 80 | 0 | C-§6; `external_audit/jury_consensus.md:96`; `references/jury_consensus_protocol.md:113-114` (currently narrative only) | 2.5–3.5 | v1.2.0 | J-101 |
| **J-110** | `templates/improvement_audit/cycle_trail.jsonl.tmpl` (NEW) × EMIT append-only artefact with prior-hash chaining (per INV-LIF-004): one line per phase transition with `cycle_id`, `event` (proposal_emitted / jury_started / hitl_decision / merge_applied / merge_verified / re_audit_ran), `ts`, `sha256_of_artefact`, `corrections_ids[]`, `commit_sha?`. | implementation | P2 | warn | 85 | 0 | C-F-IC-05 + C-§7; `references/data_flow_invariants.md#INV-LIF-004` | 3–5 | v1.2.0 | J-101, J-103 |
| **J-111** | `prompts/12_improvement_jury.md:347,392,478` × ADD max-iteration counter (default 3) on the 13.5 ↔ 13.7 send-back loop with HITL escalation on hit × matches the ≤3-retries discipline at `prompts/12_improvement_jury.md:396`. | implementation | P2 | warn | 82 | 0 | C-F-IC-04 | 1.2–1.8 | v1.2.0 | — |
| **J-112** | `prompts/11_feedback_learning_loop.md:368,395` × ADD a 2nd `<format>` block "alternatives presentation" with `[A] cat=X — fit ≈Y% / [B] cat=Z — fit ≈W%` shape, mirroring `prompts/00_master_orchestrator.md:344-364`. | hitl | P2 | warn | 75 | 0 | B-F4 | 0.8–1.2 | v1.2.0 | — |
| **J-113** | `prompts/00_master_orchestrator.md:54-75` + `prompts/02_scaffolder.md:30-37` × DECISION (document explicitly): cross-child correction portability is intentional silo (privacy/scope) OR opt-in inheritance via a `references/learned_corrections_global.md` curated by the meta-skill maintainer with HITL sign-off. Surface choice at phase 4.5. | routing | P2 | warn | 75 | 0 | A-F6 | 2–4 | v1.2.0 | — |
| **J-114** | `prompts/12_improvement_jury.md:118-130` + `references/jury_consensus_protocol.md:30-50` × SMOOTH consensus rule 1 with a 5pp uncertainty band: any reject at conf ≥65 with no compensating axis at conf ≥85 → DISSENT (not APPROVED). Removes 69%/70% cliff. **DISSENT NOTED** — protocol thresholds are calibrated at ~85% confidence per `references/jury_consensus_protocol.md:112`; this is a calibration debate, not a clear bug. | implementation | P3 | info | 72 | 0 | C-F-IC-07 | 0.8–1.2 | deferred | J-101 (eat-own-dog-food) |
| **J-115** | `templates/feedback_learning/session_close.md.tmpl:18` × AUTO-EMIT `taxonomy_refresh_proposal.md` when `OTHER_COUNT > 3` and queue it as a `category=documentation, severity=warn` correction (self-feeds the loop). | routing | P3 | info | 75 | 0 | A-F7; `references/feedback_taxonomy.md:80-82` | 0.8–1.6 | v1.2.0 | — |
| **J-116** | `prompts/11_feedback_learning_loop.md:218` × SPECIFY `corrections_fts` rebuild trigger: rebuild every 100 inserts OR on schema upgrade; add counter to `tracking/project.json#feedback_learning.fts_rebuild_count`. | routing | P3 | info | 70 | 0 | A-F8 | 0.8–1.2 | v1.2.0 | J-104 |
| **J-117** | `prompts/11_feedback_learning_loop.md:336` + `templates/feedback_learning/pending_review.md.tmpl:8` × CLARIFY: per-correction HITL fires AFTER each line is parsed (not after `DONE`); document `{{TRIGGER_NOTICE}}` example renderings for each of BELOW / AT_THRESHOLD / ABOVE. | hitl | P3 | info | 70 | 0 | B-F5 + B-F6 | 0.4–0.8 | v1.2.0 | — |

**Counts.** 23 raw findings → 17 consolidated J-NNNs (3 cross-axis clusters merged 6 raw findings into 3 entries). 1 P0 + 6 P1 + 7 P2 + 3 P3. Effort range (sum of low-high): **38–58 hours**, ±20%.

## 5. Cross-axis disagreements

No finding pair shows confidence spread >30 percentage points. Largest spreads:

| J-id | spread (pp) | reading |
|---|---:|---|
| J-105 | 6 | hitl 92% (B-F1 strong evidence at `dashboard/index.html:278-285`) vs implementation 87% (C-F-IC-05 lower because it folds in cycle_trail.jsonl which is split out into J-110). Within-tolerance. |
| J-103 | 5 | routing 80% vs implementation 90% — implementation auditor cited five concrete schema fields; routing auditor cited the kind-discriminator alone. Merge well-justified. |

**Verdict-level dissent (preserved, not collapsed).** Auditor B (`APPROVED_WITH_MINOR` at 84%) disagrees with the batch `NEEDS_IMPROVEMENT`. The protocol §"Why confidence-weighted but not confidence-blind" requires this dissent to be surfaced rather than averaged. Recorded here: B's lane (HITL capture) is mature and shippable on its own; the batch verdict reflects the broader feedback layer's routing + implementation seams, not the HITL surface.

## 6. Recommended v1.1.0 batch composition

Group P0 + P1 items (J-100..J-106) into 4 logical batches that ship as a coherent v1.1.0. Dependency order shown.

### Batch B1 · "The agent reads memorised corrections" (closes user anchor concern)
- **Items:** J-100 (mandatory-reads bullet) → J-106 (FTS5 pre-action recurrence guard)
- **Dependency order:** J-100 first (single-file edit, unblocks J-106 which extends the read-time consumption pattern).
- **Total effort:** 5–8 h
- **Concern closed:** "*el agente lo lea para no cometer esos errores*" — the user's anchor concern. After B1, every child session reads approved/incorporated corrections at start AND adaptive auditor surfaces prior_lessons[] in scope envelopes.

### Batch B2 · Schema + tracking template alignment (unblocks B3)
- **Items:** J-103 (schema columns) + J-104 (project.json.tmpl blocks)
- **Dependency order:** parallel; both are pure-additive template/schema edits.
- **Total effort:** 3–4 h
- **Concern closed:** schema drift between prompts and templates; provides join keys (proposal_id, consensus_report_sha256, incorporated_commit_sha) that B3 needs.

### Batch B3 · Close the merge-verification loop (post-merge audit + consumption gap)
- **Items:** J-101 (phase 13.8 merge_verification) + J-102 (consumption gap cluster: memory/AIE wiring)
- **Dependency order:** J-103 from B2 must land first (J-101 reads the new schema columns; J-102 writes `incorporation_kind`). J-101 and J-102 can ship in parallel after B2.
- **Total effort:** 14–21 h
- **Concern closed:** the open loop after `status='approved'`. After B3 the cycle is: approved → diff verified → memory/manifest updated OR AIE catalog extended → status='incorporated' with full forensics.

### Batch B4 · Observability surface
- **Items:** J-105 (dashboard fallback + heading)
- **Dependency order:** independent; can ship in parallel with B1, B2, B3.
- **Total effort:** 1.2–1.8 h
- **Concern closed:** the four v0.3.x feedback/adaptive_audit/Art.73/data-flow tiles render the surfaces they declare instead of "—".

### Batch B5 (optional, P2-pull-in if capacity allows) · Test layer for never-default
- **Items:** J-107
- **Total effort:** 1.2–1.8 h
- **Concern closed:** closes the 10th anchor for the never-default invariant (executable test, not just prose).

**v1.1.0 total effort:** B1 + B2 + B3 + B4 = **23.4–34.8 h** (P0+P1 only). Pulling in J-107 adds 1.2–1.8 h. Remaining P2/P3 (J-108..J-117) targeted at v1.2.0 / deferred = ~14–22 h.

**Eat-own-dog-food note.** v1.1.0 itself should be audited by the system's own phase 13.7 jury before merge — operationalising the principle currently invoked only in narrative (per C-§6 and the `references/jury_consensus_protocol.md:113-114` meta-test obligation). J-109 then makes this a standing cadence in v1.2.0.

## 7. Reflection (≤300 words)

**Convergence vs divergence.** The panel converged strongly on 5 strengths (mean confidence 91.6%) and 3 cross-axis clusters (consumption gap A+C, status semantics A+C, observability gap B+C). It diverged on the verdict — B saw a mature HITL surface and voted APPROVED_WITH_MINOR; A and C saw open routing/implementation seams and voted NEEDS_IMPROVEMENT. The protocol does not collapse this into "approved with caveats"; the dissent is preserved (§5).

**Lowest-confidence consensus item.** J-114 (consensus-rule 5pp band) at 72%. The protocol thresholds (75/70/30) are explicitly self-described as calibrated at ~85% confidence per `references/jury_consensus_protocol.md:112`. Recommending a change to them is itself a calibration debate, hence deferred — the system's own meta-test obligation (§"Versioning") would gate any actual change.

**What would invalidate this consolidation.** (i) If the auto-extension protocol at `references/ai_error_catalog.md:264-274` was always intended to be runtime-only (not feedback-fed) by design, J-102's AIE-extension half loses force. (ii) If a `merge_audit_workflow.md` exists outside the audited set and was simply not cited, J-101 collapses to a documentation finding. (iii) If `m.path` in `dashboard/index.html` is reserved for a planned v0.4.x feature and the empty-tile rendering is intentional, J-105 collapses. The panel found no evidence for any of these three; confidence the consolidation holds: ~84%.

**Hand-off note — user anchor concern closure.** Execute **Batch B1 first** (J-100 + J-106, 5–8 h). After B1 lands, every child orchestrator session begins by reading approved/incorporated corrections from `feedback_learning/corrections.md`, and the adaptive auditor surfaces recurring/systemic prior lessons in every scope envelope. The user's "*el agente lo lea para no cometer esos errores*" is operationally satisfied at that point. Batches B2 + B3 + B4 then make the closure auditable, observable, and forensically reconstructable.
