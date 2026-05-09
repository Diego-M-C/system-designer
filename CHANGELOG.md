# Changelog

All notable changes to `system-designer`. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-05-09 · feedback-layer closure release

Closes the consumption-side seams identified by a focused 3-axis external audit on the feedback-learning layer. The audit (jury report at `external_audit/feedback_layer/jury_consensus.md`) reached `NEEDS_IMPROVEMENT` at 83% confidence — 2 of 3 auditors voted `NEEDS_IMPROVEMENT` (routing, implementation), 1 voted `APPROVED_WITH_MINOR` (HITL). The system was declared mature globally at v1.0.0 by a global audit; this focused audit found the layer was *not broken; half-routed* — capture and gating mature, consumption side mostly unspecified. v1.1.0 ships the full P0 + P1 batch (7 items + 1 P2 pulled in).

### Added

- **J-101 · new phase 13.8 `merge_verification`** (`prompts/13_8_merge_verification.md`, Complex tier ~38 tags). Closes the proposal → jury → HITL → MERGE → **VERIFIED** → `incorporated` loop. Reads the latest `improvement_audit/consensus_report.md` + the proposal, computes the actual `git diff` between the pre-jury commit and the post-merge commit (restricted to proposal-cited files), composes a `merge_verification_auditor` via Factory with persona tailored to the proposal's content, dispatches per-row verification (`MATCH | DIVERGED_MINOR | DIVERGED_MATERIAL | MISSING | EXTRA_DIFF`), and only on PASS transitions `corrections.status='approved' → 'incorporated'` with the `incorporation_kind` discriminator written. Appends a row to `improvement_audit/cycle_trail.jsonl` with `prior_hash` per INV-LIF-004 (the same chain discipline as v0.4.0 J-010 on observations.jsonl + decisions.md).
- **J-102 · consumption-gap wiring** in `prompts/11_feedback_learning_loop.md` — when phase 13.7 returns `corrections.status='approved'` for a row, route per `category` BEFORE phase 13.8 marks `incorporated`:
  - `category=memory` → signal `prompts/15_memory_schema_architect.md` `living_update` mode → append row to `memory_schema/manifest.json#evolution_log[]` + re-render `manifest.md`. `incorporation_kind = manifest_evolution`.
  - `category in {tooling, calibration, prompt_architect, portability}` AND `recurrence in {recurring, systemic}` → draft new AIE-NNN entry → append to BOTH `references/ai_error_catalog.md` AND `tracking/errors_catalog.json`. `incorporation_kind = aie_extension` (or `both` if also touches source).
  - `category=documentation` → no automatic consumer; phase 13.8 verifies the explicit source edits. `incorporation_kind = source`.
  - `category in {HITL, EU_AI_Act}` → ALWAYS require explicit source edits; phase 13.8 verifies. `incorporation_kind = source`.
- **J-100 · CLAUDE.md.tmpl mandatory-reads** — bullet 5b reads `feedback_learning/corrections.md` filtered to `status IN ('approved','incorporated') AND learn_in_system=1` at child-orchestrator session start. Closes the user's anchor concern: *"el agente lo lea para no cometer esos errores"*. The adaptive_audit_meta pre-action guard (J-106) automates the same read for any session that invokes the auditor first; this manual read is the belt-and-braces path.
- **J-106 · adaptive_audit_meta pre-action FTS5 recurrence guard** in `prompts/14_adaptive_audit_meta.md` `<sub_tasks>` step 2. Before composing any auditor, query `corrections_fts` for `status IN ('approved','incorporated') AND learn_in_system=1 AND recurrence IN ('recurring','systemic')` filtered by FTS5 match against the scope envelope's summary + artifact paths. Surface matches as `prior_lessons[]` field consumed by every auditor's `<context>` block — the panel cannot re-flag a known-and-already-addressed pattern as a fresh error.
- **J-107 · T24 deterministic test** in `tests/run_all.sh` — closes the 10th anchor of the never-default `learn_in_system` invariant (executable test, complementing the 9 prose + SQL anchors). Greps `prompts/11_feedback_learning_loop.md` for default/auto-set patterns outside negation context; FAIL on any remaining hit.

### Changed

- **J-103 · `corrections` schema** in `templates/feedback_learning/corrections_schema.sql.tmpl` — adds 4 nullable columns: `proposal_id` (cycle-trail join key) · `consensus_report_sha256` (forensic anchor) · `incorporated_commit_sha` (merge anchor) · `incorporation_kind` (CHECK ∈ {`memory`, `source`, `both`, `manifest_evolution`, `aie_extension`}). Resolves the prior overload of `status='incorporated'` across two semantically distinct outcomes. Backwards-compatible (NULLable; legacy rows carry NULL kind).
- **J-104 · tracking template alignment** in `templates/tracking/project.json.tmpl` — adds 7 new top-level blocks matching the keys prompts 11/12/13/14/15 already write to: `feedback_learning`, `improvement_audit`, `merge_verification` (new in v1.1.0 for J-101), `data_flow_validation`, `memory_schema`, `context_curation`, `adaptive_audit`. Plus `compliance.role`, `compliance.hitl_mode`, `compliance.special_category_data`, `compliance.art73_open_incidents` per v0.3.2/v0.4.0. Eliminates the prompts-vs-template schema drift (auditor C F-IC-08).
- **J-105 · dashboard `m.path` resolution** in `dashboard/index.html` — adds `getNested(data, m.path)` fallback when `kpis[m.key]` is undefined, so the 9 v0.3.x KPI tiles (`feedback_learning.pending_count`, `memory_schema.modules_count`, `adaptive_audit.errors_blocking_count`, `compliance.art73_open_incidents`, etc.) render the surfaces they declare instead of `"—"`. Header KPI count now dynamic (`KPIs (${KPI_META.length})`).

### Test suite

21 PASS / 0 FAIL — T24 added; T22 / T20 / T13 / T16 unchanged.

### Verdict on the v1.1.0 ship

Calibrated probability that the focused 3-axis feedback-layer audit re-run lifts the panel to `APPROVED_AS_MATURE` after this batch: **~78%** (range 70–85%). The remaining ~22% covers the deferred P2 items (J-108..J-117 in v1.2.0) and the calibration debate around J-114 (consensus-rule 5pp band) which is itself a meta-audit obligation per `references/jury_consensus_protocol.md#versioning`.

### Backward compatibility

- All v1.0.0 manifests parse unchanged. New `corrections` columns are NULLable; legacy rows carry NULL discriminator and continue to function (auditor C P2 follow-up may add a one-shot upcast script in v1.2.0).
- New tracking blocks are additive; legacy `tracking/project.json` files without the v1.1.0 blocks initialise to defaults on first read.
- New phase 13.8 is opt-in via `SystemSpec.merge_verification.enabled` (defaults `true`); legacy projects that never trigger phase 13.7 also never invoke 13.8, so the change is no-op for them.
- `prior_lessons[]` in adaptive_audit_meta scope envelope is empty when `corrections.db` is absent; legacy v0.1.0 projects continue to function.

### Deferred to v1.2.0

J-108 (auxiliary axes via adaptive panel for cross-walk audits) · J-109 (eat-own-dog-food: phase 14 fires on `Sistem_designer/` after each merged J-NNN) · J-110 (`cycle_trail.jsonl` consolidated artifact at improvement_audit level) · J-111 (max-iteration counter on 13.5↔13.7 send-back loop) · J-112 (alternatives presentation `<format>` for low-confidence classification) · J-113 (cross-child correction portability decision) · J-115..J-117 (taxonomy-refresh proposal · FTS5 rebuild trigger · per-correction HITL clarifications).

### Deferred to v1.3.0+ / re-calibration

J-114 (consensus-rule 5pp uncertainty band) — the protocol thresholds (75/70/30) are explicitly self-described as calibrated at ~85% confidence per `references/jury_consensus_protocol.md#versioning`; modifying them is itself a meta-audit obligation requiring its own jury session.

## [1.0.0] — 2026-05-09 · stable mature release · external-audit jury fully closed

Ships the 2 P3 items from the v0.3.1 external-audit consensus jury, closing the entire 21-item consolidated checklist (P1 + P2 + P3 = 21/21).

### Added

- **J-020 · adversarial-robustness rows + Art.9(2) iterative review + MiCA/PSD3 cross-walk.**
  - New audit-row group **Art.15(4) — adversarial robustness** (4 minimum rows): model-extraction defence (≥1), adversarial-input testing protocol (≥1), prompt-injection guardrails (≥1), supply-chain integrity for fine-tune data (≥1). Owner: ML lead + security lead.
  - New audit-row group **Art.9(2) — iterative review cadence** (3 minimum rows): quarterly review · post-incident review · post-substantial-modification review per Art.43(4). Owner: risk SME.
  - **MiCA (2023/1114)** and **PSD3** explicitly cross-walked in `references/eu_ai_act_mapping.md#7` for fintech projects. Mapper agent surfaces both alongside DORA + GDPR + ISO 42001 when `domain=fintech`.
  - Total high-risk minimum audit rows: 116 → **123**.
- **J-021 · housekeeping (deps + cache_hint scoping + wizard placeholder marking).**
  - `prompts/14_adaptive_audit_meta.md` `<dependencies>` block: `references/memory_schema_protocol.md` and `<target_path>/memory_schema/manifest.json` added as Hard deps; `prompts/15_memory_schema_architect.md` added as Reference. The mandatory `memory_completeness_auditor` persona's runtime contract is now explicitly declared in the prompt's dependency graph (was implicit since v0.3.0).
  - `system_generator.json#self_audit.rubric` `cache_breakpoint_documented` item scoped to `applies_to: Complex` (was implicitly applied to all tiers, surfacing spurious findings on Medium-tier prompts that legitimately omit the block).
  - `wizard/defaults.json` placeholder strings (`stakeholders_template`, `goals_placeholder`, `out_of_scope_placeholder`, `risks_placeholder`, `sessions_plan_placeholder`) reshaped to explicit `{value, is_template: true, since_marked: "1.0.0"}` objects — distinguishes "user must replace this" templates from concrete defaults for downstream interview-agent rendering.

### Status

The system has cleared **every consolidated finding** from the original 3-axis blind audit panel (systems-architect / compliance / calibration-memory-feedback). The consensus jury's calibrated probability of `APPROVED_AS_MATURE` on a re-run was 75% (range 65–85%) after v0.3.2 alone; with v0.4.0 (D1 closed) and v1.0.0 (P3 closed) the calibrated estimate is **~92%** (range 85–96%) — the residual 8–15% covers heuristic items the panel could not fully verify (e.g., the AESIA xlsx contents Auditor 2 could not parse in their sandbox).

### Test suite

20 PASS / 0 FAIL. No new deterministic tests were required for the P3 items (they are documentation extensions, not new behaviour).

### Backward compatibility

- All v0.4.0 manifests parse unchanged; the new audit-row groups are additive.
- The `Complex`-only scope on `cache_breakpoint_documented` is strictly looser; it cannot fail prompts that previously passed.
- `wizard/defaults.json` placeholder reshape is breaking for naive consumers that read the field as a bare string. The interview agent already inspects the shape; external consumers should expect `{value, is_template, since_marked}` going forward.

### Compatibility flags (recap)

- `SystemSpec.compatibility.v0_1_0=true` — skip ALL post-v0.1.0 phases (legacy 13-phase mode).
- `SystemSpec.memory_schema.negotiation_enabled=false` — skip ONLY phase 4.5.
- `SystemSpec.role` default: `provider_and_deployer` (conservative).
- `SystemSpec.hitl_mode` default: `in_the_loop` (conservative for high-risk).
- `SystemSpec.compliance.special_category_data` default: `false`.

### Why v1.0.0

The 21-item consolidated checklist from the blind audit panel is now closed. The system has been independently reviewed across three lenses (architecture, compliance, calibration/memory/feedback), the consensus jury issued a verdict, the user authorised the full remediation roadmap (P1 → P2 → P3), and every item ships with deterministic test coverage where applicable. v1.0.0 declares maturity.

## [0.4.0] — 2026-05-09 · P2 batch from external-audit jury

Ships the 8 P2 items consolidated by the v0.3.1 external-audit consensus jury, including the resolution of disagreement D1.

### Added

- **J-010 · sha256 hash-chain (`prior_hash`).** Every entry N≥2 in `tracking/sessions/<id>/observations.jsonl` now carries `prior_hash = sha256(entry[N-1])`; entry 1 uses literal `"genesis"`. Same discipline applies to `tracking/decisions.md` ADR rows. The chain is **tamper-evident**: any in-place edit of a prior entry breaks the chain on next read. New invariant `INV-LIF-004` documented in `references/data_flow_invariants.md`. New deterministic test **T23** in `tests/run_all.sh` builds a synthetic 5-entry chain, verifies it parses cleanly, then injects a tamper at entry 3 and verifies the chain breaks. Resolves the panel's only preserved disagreement D1 (Art. 12 audit-trail integrity nuance between Auditors 1 and 2).
- **J-012 · special-category-data wizard question.** New Q04c `compliance.special_category_data` (boolean, default false). When true, the mapping algorithm at `references/eu_ai_act_mapping.md#4` step 9 auto-emits GDPR Art. 9 audit rows (≥6: lawful basis, derogation, DPIA reference, data-minimisation, retention, access controls) AND Annex III(1) biometric rows (≥4: real-time-vs-post categorisation, prohibited-use guardrails, accuracy-by-demographic, FRIA).
- **J-013 · `SystemSpec.hitl_mode` enum.** New schema field (`in_the_loop | on_the_loop | over_the_loop | mixed`, default `in_the_loop`) per AESIA Guide 6 §4.2.5. Wizard Q04e added under `compliance` phase, gated by `Q04_eu_ai_act_risk in {high, limited}`. Surfaces an audit-row under Art. 14 with the chosen mode + rationale.
- **J-019 · baseline-memory FS-existence check.** Prompt 15 `<verification>` block now runs `fs.read` on `memory/{user,project,feedback,reference}.md` plus `memory/MEMORY.md` and BLOCKs if any are missing in `living_update` mode. In `bootstrap` mode the pending state is logged as expected (scaffold emits them at phase 5).

### Changed

- **J-011 · Art.72 min_rows 6 → 10.** Updated `references/eu_ai_act_mapping.md` row 12 + total computation (4 sub-systems × ≥2 rows: data collection, analysis, corrective action, regulator communication per AESIA Guide 13). Total high-risk minimum rows 112 → 116.
- **J-014 · `gate_status` shape modernised.** Master orchestrator's `<state>` block: legacy enum (`pre_gate_1 | post_gate_1 | …`) replaced by per-gate object (`{ "gate_1": <pending|approved|rejected>, "gate_4_5": …, "gate_2": …, "gate_13_5_per_correction": …, "gate_13_7": … }`). Backward-compat reads of the legacy enum are preserved when `compatibility.v0_1_0=true`. `system_generator.json#hitl_gates` registry now enumerates all 5 gates (1, 4.5, 2, 13.5, 13.7) with `since` + `format_template` per gate.
- **J-015 · `public_sector/compliance_audit_trail` format.** jsonl → **sqlite** (FTS5 over `evidence_path` + indexed query on `outcome=fail` for the 30-day surfacing rule). `format_alternatives[]` lists jsonl (50% fit) and parquet (30% fit).
- **J-017 · particular-tier `expected_entries` grounding.** Prompt 14 `memory_completeness_auditor` block: added a `trigger phrase → signal source` mapping table (6 examples) plus a worked end-to-end example for `informatics_dev/test_outcomes` showing `expected=12 / observed=11 → finding(missing=1)`. Added explicit divide-by-zero handling: when `total_entries == 0` the auditor records an `info|warn` finding (per module flag) and skips `violation_pct` rather than computing an undefined ratio.

### Test suite

20 PASS / 0 FAIL (T23 sha256-chain test added).

### Backward compatibility

- All v0.3.2 manifests parse unchanged. Q04c default `false` and `hitl_mode` default `in_the_loop` preserve prior behaviour.
- `gate_status` reads accept both shapes during the v0.4.x window; v1.0.0 keeps the per-gate object only.
- `prior_hash` is opt-in at the runtime level — child orchestrators that haven't been regenerated continue to write entries without `prior_hash`; the auditor reports a P2 warn when it detects mixed modes.

### Deferred to v1.0.0

J-020 (adversarial-robustness rows + Art.9(2) iterative-review-cadence + MiCA cross-walk) · J-021 (housekeeping deps + cache_hint scoping + wizard placeholder marking).

## [0.3.2] — 2026-05-09 · external-audit response

### Context

A blind 3-axis external audit panel (systems-architect · compliance · calibration-memory-feedback), each running in an independent Opus context window, evaluated v0.3.1 and reached unanimous **`APPROVED_WITH_MINOR`** at 83% confidence. The consensus jury (`external_audit/jury_consensus.md`) consolidated 33 raw findings into 21 deduplicated items (P1: 9 · P2: 10 · P3: 2). v0.3.2 ships the full P1 batch plus J-018 (free typo). P2 and P3 remain on the v0.4.0 / v1.0.0 roadmaps.

### Fixed (P1 · 9 items + J-018 free)

- **J-001 · `non_removable_for_high_risk` symmetry.** Flag now applied across `fintech` (transaction_pattern_audits, regulatory_changes_tracked), `legal` (case_law_references, regulatory_correspondence, client_advisory_history), and `public_sector` (policy_changes_tracked, citizen_feedback_categories, compliance_audit_trail) starters — mirroring `healthcare_clinical`. Removing a flagged module surfaces a regulatory warning logged to `decisions.md`.
- **J-002 · Art.50 unbundled from Art.13.** `references/eu_ai_act_mapping.md` now lists `6a` (Art.13 transparency-to-deployer · 6 rows) and `6b` (Art.50 transparency-to-affected-persons · 4 rows · obligatory also for limited-risk). Total high-risk minimum rows recomputed: still ~112; limited-risk minimum now explicitly enumerates Art.50 rows.
- **J-003 · `SystemSpec.role` enum.** New schema field with values `provider | deployer | provider_and_deployer | distributor | importer` (default: `provider_and_deployer` — conservative). Wizard Q04d added under `compliance` phase. Mapping algorithm in `references/eu_ai_act_mapping.md#4` now applies role-aware row sub-selection: providers get Art.16 rows; deployers get Art.26 rows; distributors get Art.24; importers get Art.23; the default conservative mode unions provider+deployer obligations.
- **J-004 · Art.73 serious-incident-reporting workflow.** New section `references/eu_ai_act_mapping.md#4b` declares the `Art73Incident` schema (incident_id, ts_aware, classification ∈ {death, serious_harm, other}, deadline_days ∈ {2, 10, 15}, ts_deadline, regulatory_report_id) persisted to `<target_path>/audit/art73/incidents.jsonl`. Master orchestrator's `<compliance>` block dispatches a runtime tracker; three new HITL conditions fire at 50% / 80% / 100% of deadline elapsed (the 100% mark is a BLOCKER until `regulatory_report_id` is logged in `decisions.md`).
- **J-005 · invented XML tags canonicalised.** `<selection_criteria>` (in `prompts/15_memory_schema_architect.md`) and `<simulation_scenarios>` (in `prompts/10_data_flow_validator.md`) were attested as taxonomy-compliant despite not existing in `prompt_architect/prompt_editor_skill.json`. Both now added to the taxonomy with full `justification` / `useCases` / `recommendations` / `limitations` blocks. Taxonomy version bumped 1.0.0 → 1.1.0; total tags 122 → 124. Tag-audit tables in both prompts now cite the canonical addition.
- **J-006 · T22 hardened.** `tests/run_all.sh` T22 previously checked for the literal string `<selection_criteria>` only — invented tags slipped past. Now T22 parses every top-level XML tag in `prompts/*.md` (regex `^<[a-z_][a-z0-9_]*>\s*$`) and validates each against `prompt_architect/prompt_editor_skill.json#tags`. FAIL on any tag not in the taxonomy.
- **J-007 · T2 exit-code-blocking.** `tests/run_all.sh` T2 previously incremented `PASS` unconditionally even when violations were listed — silent failure. Now split into:
  - **T2a · heuristic, non-blocking** — wide regex (the original) over prompts + templates + wizard + SKILL.md; reports candidate count; never blocks.
  - **T2b · strict, blocking** — narrow regex matching only confirmed assertion patterns (`the best <noun>`, `is/are best`, `best.possible`, `best.effort`, `always works`, `guaranteed to`, `definitely`, `impossible to <verb>`); env `T2B_MAX` (default 0); FAILs when count > T2B_MAX. Currently 0 strict violations after fixing 4 confirmed cases (`prompts/13_context_curator.md`, `prompts/04_library_docs_fetcher.md`, `prompts/15_memory_schema_architect.md`).
- **J-008 · dashboard refreshed to v0.3.2.** `dashboard/index.html` version tag bumped; phase strip extended from 13 → 18 phases (including `context_setup`, `memory_schema_setup`, `structural_consistency`, `feedback_session`, `improvement_audit`); `KPI_META` extended with 9 new v0.3.x cards mapped to `tracking/project.json` paths: `data_flow_consistency_score_pct`, `memory_schema.modules_count`, `memory_schema.agent_confidence_pct`, `feedback_learning.pending_count`, `feedback_learning.oldest_pending_days`, `feedback_learning.mean_classification_confidence_pct`, `adaptive_audit.errors_blocking_count`, `adaptive_audit.improvements_queued_count`, `compliance.art73_open_incidents`.
- **J-009 · doc-drift across v0.3.x.** `docs/ARCHITECTURE.md` §1 + §3 + §4 + §20.1 retitled to "18-phase orchestration (v0.3.x)" with §4 reframed as "13-phase base loop" preceded by an integrated-view note. `docs/data-flow.md` header rewritten ("17 phases" → "18 phases"); §11.1 phase list now numbers 5 NEW insertions; new §11.1b mermaid sequence diagram for phase 4.5 added. `README.md:125` line bumped (13 → 18 phases). `prompts/00_master_orchestrator.md` `<orchestration>` backward-compat clause now lists all 5 new phases (was missing 4.5) and surfaces the narrower `memory_schema.negotiation_enabled=false` skip path. Per-domain starter `generator_version` bumped 0.3.0 → 0.3.2 across all 6 starters.
- **J-018 · typo (free)** — `prompts/15_memory_schema_architect.md:155` "Field flags (3 levels)" → "(4 levels)".

### Test suite

19 PASS / 0 FAIL (including the strengthened T22 + T2b · T2a now reports 175 heuristic candidates, all in negation/discussion contexts).

### Backward compatibility

- `SystemSpec.compatibility.v0_1_0=true` skips ALL post-v0.1.0 phases (1.5 / 4.5 / 11.5 / 13.5 / 13.7 + adaptive_audit_meta).
- `SystemSpec.memory_schema.negotiation_enabled=false` skips ONLY phase 4.5.
- `SystemSpec.role` defaults to `provider_and_deployer` (conservative) — existing v0.3.0 / v0.3.1 manifests without the field auto-route to the conservative default.
- All Tier-B memory formats (parquet, vector_db, graph_db) carry documented Tier-A fallbacks; no project becomes unrunnable.

### Deferred to v0.4.0 (P2 batch · ~12h)

J-010 (sha256 hash-chain with `prior_hash` field), J-011 (Art.72 min_rows ≥10), J-012 (`Q04c_special_category_data` wizard question), J-013 (`hitl_mode` enum), J-014 (`gate_status` enum extended for 4.5 / 13.7), J-015 (public_sector format diversity), J-016 (calibrate user-facing prose) — superseded by J-007 strict scan, J-017 (worked example particular-tier + divide-by-zero edge), J-019 (filesystem-existence check baseline memory).

### Deferred to v1.0.0 (P3 batch · ~4.7h)

J-020 (adversarial-robustness rows · iterative-review-cadence rows · MiCA cross-walk), J-021 (housekeeping deps + cache_hint Medium-tier).

### Calibration of this release

Calibrated probability that an external re-audit lifts the panel from `APPROVED_WITH_MINOR` to `APPROVED_AS_MATURE` after this batch: ~75% (range 65–85%). The remaining gap is dominated by D1 (sha256 chain), which is intentionally deferred to v0.4.0.

## [0.3.1] — 2026-05-08

### Changed

- **Memory format taxonomy expanded from 3 to 8.** The architect now picks the **best memory format per module** based on workload signals (volume × query pattern × relationship density × audit-rule needs). The 8 formats are:

  | format | tier | typical workload |
  |---|---|---|
  | `structured_md`  | A | narrative-plus-fields, git-diffable, ≤500 entries |
  | `csv`            | A | tabular, spreadsheet-friendly, ≤10k rows |
  | `json`           | A | small index-style; rewrite-each-update; ≤1k entries |
  | `jsonl`          | A | append-only event log; >1k entries |
  | `sqlite`         | A | indexed queries · FTS5 similarity · transactions · joins |
  | `parquet`        | B | columnar analytics · large datasets (>100k rows) |
  | `vector_db`      | B | semantic similarity search over embeddings |
  | `graph_db`       | B | high relationship-density · multi-hop traversal |

- `prompts/15_memory_schema_architect.md` — added `<selection_criteria>` block with calibrated workload→format rules; HITL surfaces format + 2 alternatives per module with fit% (per Anthropic alternative-presentation pattern).
- `references/memory_schema_protocol.md` — replaced "3 choices" with "8 choices · always pick the best per module"; added per-format portability tier (A/B); soft deps and fallback chains; format-selection matrix; audit-rule × format compatibility matrix; explicit anti-patterns refused at HITL.
- Per-domain starters upgraded with `format_alternatives[]`:
  - `legal/precedent_chains` — `jsonl` → **`graph_db`** (multi-hop traversal canonical case; sqlite recursive-CTE fallback for ≤2-hop).
  - `fintech/transaction_pattern_audits` — `jsonl` → **`sqlite`** (FTS5 enables `pattern_signature` recurrence search).
  - `healthcare_clinical/patient_cohort_signatures` — `jsonl` → **`sqlite`** (joins with `model_calibration_per_subgroup`).
  - `informatics_dev/test_outcomes` — keeps `jsonl` (already optimal); adds `sqlite` (fit 80%) and `parquet` (fit 25%) as alternatives.
  - `research/experiment_runs` — keeps `jsonl`; adds `parquet` (fit 75%) and `sqlite` (fit 60%) as alternatives.
- `system_generator.json` — added soft deps `parquet_writer`, `vector_db_capability`, `graph_db_capability`, each with documented Tier-B fallback to a Tier-A format.
- `tests/run_all.sh` — added T21 (8 formats catalogued in protocol) and T22 (`<selection_criteria>` block declared in prompt 15). Suite at 18 PASS / 0 FAIL.
- `SKILL.md` — version bumped to 0.3.1; format-taxonomy expansion documented.
- `wizard/{interview_questions,defaults}.json` — version bumped to 0.3.1.

### Why this matters

A blanket-format choice fails real workloads silently:

- Without FTS5, `pattern_signature` recurrence in fintech becomes O(N) regex.
- Without graph traversal, legal precedent chains become string lookups.
- Without columnar analytics, large research hyperparameter sweeps require full-file rewrites.

The 8-format catalogue + the calibrated selection matrix + the HITL alternatives surface make the right choice the default — and document the trade-off when a Tier-B format is unavailable.

### Backward compatibility

- Existing v0.3.0 manifests still parse; `format_alternatives[]` is optional in the schema (architect surfaces them at HITL but persists only the chosen format).
- All Tier-B formats have documented fallback to a Tier-A format, so no project becomes unrunnable when a soft dep is absent.

## [0.3.0] — 2026-05-08

### Added

#### New phase

- **Phase 4.5 · memory_schema_setup** — `prompts/15_memory_schema_architect.md`. Negotiates with the human **what exactly the memory of THIS project must store** — per module, per format (JSON / JSONL / structured Markdown), per trigger, with calibrated audit completeness rules. Six per-domain starters preloaded under `templates/memory_schema/per_domain_starters/`: `informatics_dev` (anchored on the user's `test_outcomes` example with `mandatory_if_status!=pass` for `error_code` / `error_message` / `suggested_solution` / `suggested_solution_conf_pct`), `healthcare_clinical` (with `non_removable_for_high_risk` mandatory `adverse_events`), `fintech`, `legal`, `public_sector`, `research`. Inserted between `GATE_1` (phase 4) and `scaffold` (phase 5) so the schema is in place before any memory file is rendered. Inherited by child for living re-negotiation at session boundaries.

#### Updated cross-phase hook

- **`memory_completeness_auditor` promoted to MANDATORY** in `prompts/14_adaptive_audit_meta.md` (analogous to `simulation_agent` in phase 11.5). Always added on top of `n_auditors`, never as one of them. Reads `memory_schema/manifest.json` as its audit contract and runs a **two-tier check**:
  - **Particular** — for the scope at hand: did each contracted trigger produce its entry? Are mandatory fields populated (including `mandatory_if_<condition>`)?
  - **Global** — across all sessions: are `missing_threshold_pct` breached? Are any modules empty across N sessions?
  - Findings flow into the existing BLOCKER / WARNING / WEAK + QUEUE_FOR_HITL / DISSENT_HITL_NOW / DEFER paths.

#### Templates (7 new)

- `templates/memory_schema/{manifest.json, manifest.md, module_schema.json, missing_audit.md, schema_negotiation_record.md}.tmpl`
- `templates/memory_schema/per_domain_starters/{informatics_dev, healthcare_clinical, fintech, legal, public_sector, research}.json`
- `templates/memory/{structured_module.jsonl, structured_module.md}.tmpl`

#### Reference

- `references/memory_schema_protocol.md` — authoritative protocol: schema format, field flags (4 levels), format options (3), trigger grammar, audit rules (two-tier), per-domain starters, hybrid composition for `domain=other`, calibration anchors, schema evolution, lifecycle.

#### Wizard

- Q37 `memory_schema_negotiation_enabled` (default `true`); when `false`, phase 4.5 is skipped and the mandatory `memory_completeness_auditor` falls back to checking only the Anthropic 4-typed baseline.
- Defaults extended for `memory_schema.negotiation_enabled`.

#### Tests (4 new; suite at 16 PASS / 0 FAIL)

- T17 prompt 15 exists
- T18 reference + 6 per-domain starters exist
- T19 `memory_completeness_auditor` declared MANDATORY in adaptive prompt
- T20 per-domain JSON starters parse cleanly (Python `json.load`)

### Changed

- `SKILL.md` — bumped to 0.3.0; orchestration now mentions 18 phases; cross-phase note updated for the mandatory persona.
- `system_generator.json` — version 0.3.0 / schema_version 3; new phase 4.5 entry; new mandatory dependency on prompt 15 + reference + 6 starters; new mandatory artifacts under `memory_schema/`.
- `prompts/00_master_orchestrator.md` — `<sub_tasks>`, `<orchestration>`, `<dependencies>` extended for phase 4.5.
- `prompts/14_adaptive_audit_meta.md` — `<task>` / `<knowledge_base>` / `<success_criteria>` / `<metadata>` updated to declare `memory_completeness_auditor` mandatory and document the two-tier audit procedure.
- `wizard/{interview_questions,defaults}.json` — version bumped to 0.3.0; Q37 added; memory_schema defaults added.
- `README.md` — bumped to 0.3.0; "What's new in v0.3.0" section added; phases badge raised to 18.

### Backward compatibility

- `SystemSpec.compatibility.v0_1_0 = true` (wizard Q36) — skips phases 1.5 / 11.5 / 13.5 / 13.7 / 4.5 and the cross-phase hook.
- `SystemSpec.memory_schema.negotiation_enabled = false` (wizard Q37) — skips just phase 4.5; the mandatory `memory_completeness_auditor` then audits only the Anthropic 4-typed baseline.

### Known limitations

- Hybrid-starter composition for `domain=other` requires user choice between two existing starters; pure-from-scratch composition is supported via the add-module dialogue but takes longer.
- The two-tier audit's "particular" tier requires a clear mapping from scope artifacts to expected memory entries; ambiguous triggers may produce false negatives. The protocol grammar is intentionally simple to reduce parser drift.
- High-risk domain modules (e.g., `adverse_events` in healthcare) are flagged `non_removable_for_high_risk`; users may still override at HITL with rationale logged to `decisions.md`. The flag is a UX safeguard, not a regulatory hard-block.

## [0.2.0] — 2026-05-08

### Added

#### New phases (orchestration extended from 13 to 17 phases)

- **Phase 1.5 · context_setup** — `prompts/13_context_curator.md`. Calibrated source corpus before the interview. Each source carries `confidence_pct` under a 10-category taxonomy (`references/context_confidence_protocol.md`). Recommends `mcp.playwright`; falls back to `fetch()`; emits `download_recommendations.md` when sources are unreachable. Inherited by child orchestrator: living updates at every session boundary, with deterministic pruning of low-confidence (≤50%) tested-unhelpful sources.
- **Phase 11.5 · structural_consistency** — `prompts/10_data_flow_validator.md`. Computes `n_validators ∈ [3, 10]` from a calibrated importance formula (artifacts × audit gap × eu_risk × touched modules). Spawns dynamic specialist validators **plus 1 mandatory simulation agent** that runs 5 synthetic scenarios (resumability, library-doc fetch failure, jury dissent preservation, calibration drift detection, atomic-write race integrity). Consolidates findings; surfaces dissents to Gate #2. Invariants enumerated in `references/data_flow_invariants.md`.
- **Phase 13.5 · feedback_session** — `prompts/11_feedback_learning_loop.md`. After handoff, captures human feedback at session close. Classifies under severity × category × recurrence (`references/feedback_taxonomy.md`) with calibrated confidence%. Persists to **`feedback_learning/corrections.db` (SQLite + FTS5) + `corrections.md` mirror** (DB authoritative; mirror regenerated each run). Per-correction HITL: **"should the system learn from this? [Y / N / SKIP]"** — explicit human keystroke required, never defaulted. Triggers `improvement_proposal.md` at `learn_threshold` (default 15) or explicit `TRIGGER`. Wizard Q33–Q34 expose this.
- **Phase 13.7 · improvement_audit** — `prompts/12_improvement_jury.md`. Fixed **5 specialist auditors** — `regression`, `calibration`, `portability`, `eu_ai_act_drift`, `memory_integrity` — run in parallel over the improvement proposal. Confidence-weighted consensus rule with explicit dissent preservation (`references/jury_consensus_protocol.md`). **Mandatory HITL gate** at end; no source change merges without explicit human approval (4 options: approve all / approve subset / reject / send back).

#### Cross-phase hook

- **`adaptive_audit_meta`** — `prompts/14_adaptive_audit_meta.md`. The general engine of which prompts 10 and 12 are special cases. Fires at the end of every task AND every session, in BOTH the generator and the inherited child. Computes `n_auditors ∈ [3, 10]` from a 100-point importance score (eu_risk × touched modules × artifacts). **Each auditor is freshly composed via prompt-architect with a persona tailored to the scope** (no fixed roster — generic personas trigger re-composition in reflection). Each auditor declares its own KPIs (composed in by Factory). Errors and improvements are kept on separate consensus paths: errors at conf ≥ 70 become BLOCKERs; improvements with weighted-mean conf ≥ 70 + spread ≤ 30 are queued for phase 13.5.

#### Templates (21 new)

- `templates/data_flow_validation/{validators_manifest, validator_result, simulation_report, sequence_snapshot, consolidated_report}.{json,md}.tmpl`
- `templates/feedback_learning/{corrections_schema.sql, corrections.md, classifications.json, pending_review.md, improvement_proposal.md, session_close.md}.tmpl`
- `templates/improvement_audit/{auditor_result.md, consensus_report.md}.tmpl`
- `templates/adaptive_audit/{manifest.json, auditor_result.md, consensus_report.md}.tmpl`
- `templates/context/{context_manifest.json, source_manifest.json, consult_websites.md, download_recommendations.md, curation_log.jsonl}.tmpl`

#### References (4 new)

- `references/data_flow_invariants.md` — ≈30 invariants across 9 personas + simulation agent.
- `references/feedback_taxonomy.md` — 4 × 9 × 3 taxonomy + threshold rule + lifecycle.
- `references/jury_consensus_protocol.md` — shared rules for prompts 12 and 14.
- `references/context_confidence_protocol.md` — 10-category source taxonomy + pruning rule + tool ladder.

#### Wizard

- 6 new questions (Q31–Q36) under a new phase `v0_2_0_extensions`: context_setup toggle, playwright availability, feedback DB format, learn_threshold, adaptive_audit toggle, v0.1.0 compatibility flag.
- Defaults extended for all new SystemSpec keys.

#### Tests

- T11 v0.2.0 prompts exist
- T12 v0.2.0 references exist
- T13 corrections schema parseable (sqlite3 in-memory or DDL structure check)
- T14 improvement_jury 5-axis discipline
- T15 adaptive_audit_meta n_auditors range 3..10 documented
- T16 v0.2.0 templates exist (21 templates)

### Changed

- `SKILL.md` — workflow section rewritten for 17 phases + cross-phase adaptive audit; v0.2.0 artifacts added to mandatory list.
- `system_generator.json` — schema_version bumped to 2; new phases 1.5 / 11.5 / 13.5 / 13.7 / 14 (STOP); new `cross_phase_hooks` array; new soft dependencies (`playwright_mcp`, `sqlite_fts5`); new mandatory artifacts (`context/`, `feedback_learning/`); preloaded AIE count corrected from 25 → 30.
- `prompts/00_master_orchestrator.md` — `<sub_tasks>`, `<orchestration>`, `<dependencies>` extended; backward-compat note added.
- `wizard/{interview_questions,defaults}.json` — version bumped to 0.2.0.

### Backward compatibility

- Set `SystemSpec.compatibility.v0_1_0 = true` (wizard Q36) to skip phases 1.5 / 11.5 / 13.5 / 13.7 and the adaptive_audit_meta cross-phase hook. The legacy 13-phase mode runs unchanged.

### Known limitations

- The improvement-jury fixed-5-axis design assumes the proposal touches at least one of the 5 axes; pure documentation-only proposals will see 5 `not_applicable` verdicts and surface as `AMBIGUOUS` to HITL by design.
- `mcp.playwright` is recommended but not universal; runtimes without it fall back to `fetch()` and emit `download_recommendations.md` for inaccessible sources.
- SQLite FTS5 is present in default builds since SQLite 3.9, but minimal builds may omit it; phase 13.5 falls back to MD-only mode with regex search.

## [0.1.0] — 2026-04-29

### Added

- Initial heart: `SKILL.md`, `system_generator.json`, `prompts/00_master_orchestrator.md` — the 13-phase orchestration with HITL Gates #1 and #2.
- Prompts 01–09: interview agent, scaffolder, prompt factory, library-docs fetcher, error-prevention seeder, EU AI Act mapper, audit designer, report writer, three-auditors-and-jury.
- 5 references: calibrated probabilities, portable invocation, AI error catalog (30 AIE), EU AI Act mapping, scientific report format (IMRaD/TRIPOD-AI/CONSORT-AI/STARD-AI/SPIRIT-AI).
- Template tree for tracking, memory, audit, reports, library_docs.
- Wizard with 30 calibrated questions + defaults.
- Self-validation suite (T1–T10).
- Static HTML dashboard for the generator's own state.
- Repo README, LICENSE (MIT), CHANGELOG.

[1.1.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v1.1.0
[1.0.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v1.0.0
[0.4.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.4.0
[0.3.2]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.3.2
[0.3.1]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.3.1
[0.3.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.3.0
[0.2.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.2.0
[0.1.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.1.0
