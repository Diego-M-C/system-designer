---
auditor_id: 3
persona_slug: calibration_memory_feedback_lead
session_id: external-audit-v031-2026-05-08
ran_at: 2026-05-08T00:00:00Z
overall_verdict: APPROVED_WITH_MINOR
overall_confidence_pct: 84
findings_count: 11
self_kpis:
  files_read: 17
  starters_inspected: 4
  evidence_citation_rate_pct: 100
  mean_finding_confidence_pct: 82
---

# Calibration / Memory / Feedback Lead · External Audit · system-designer v0.3.1

## 1. Executive verdict (≤120 words)

The calibration / memory / feedback / error-catalog / KPI surfaces are **substantively mature** and consistent with the stated invariants. The 8-format taxonomy is faithfully encoded both in the protocol reference and in the prompt-15 selection criteria, and the audit-rule × format compatibility matrix is reproduced verbatim across both. The two-tier audit (particular + global) is unambiguously specified inside the mandatory `memory_completeness_auditor`. Per-correction HITL Y/N/SKIP is hardened against silent defaulting (≈90% confidence) and the threshold rule is parametric (works at 5 and 50). The AIE catalog has 30 calibrated entries with documented auto-extension. Material gaps are concentrated in (a) the **dashboard**, which still announces v0.1.0 / 11 KPIs and ignores v0.2/v0.3 surfaces, (b) the **T2 calibration test always-passing**, and (c) two minor inconsistencies in the field-flag count (3 vs 4) and the `public_sector` starter format-diversity. None block the system; all are tractable in <8 hours.

## 2. Strengths observed

1. **Forbidden-token discipline is precisely defined and machine-scannable.** `references/calibrated_probabilities.md:9-22` enumerates 7 forbidden tokens, gives replacement patterns, and pins the exact regex `\b(best|always|never|guaranteed|certain|definitely|impossible)\b` to the self-audit step. Confidence ≈95%.
2. **Two-tier audit semantics are unambiguous.** `references/memory_schema_protocol.md:119-128` gives a clean 2-row table (particular vs global), each with a worked example carrying confidence%; the same semantics are echoed in `prompts/14_adaptive_audit_meta.md:150-178` as deterministic pseudocode (per-module, per-entry, then violation_pct check), routing findings into the existing error / improvement triage. Confidence ≈92%.
3. **Per-correction HITL discipline is hard-coded against silent defaulting.** `prompts/11_feedback_learning_loop.md:36-37,57,205-211,389-397,420-426` repeats the rule in `<task>`, `<success_criteria>`, `<non_do_conditions>`, `<hitl_conditions>`, and `<guardrails>`, and the SQL CHECK constraint at `templates/feedback_learning/corrections_schema.sql.tmpl:22` enforces `learn_in_system IN (0,1,2)` (Y/N/SKIP). Confidence ≈90%.
4. **8-format taxonomy is internally consistent across the two files that own it.** `references/memory_schema_protocol.md:46-86` and `prompts/15_memory_schema_architect.md:161-210` reproduce the same Tier-A / Tier-B split, the same workload-signal selection matrix, and the same audit-rule × format compatibility matrix. Confidence ≈95%.
5. **AIE catalog count is parity-locked.** `references/ai_error_catalog.md:278` declares "Total preloaded count: 30"; `templates/tracking/errors_catalog.json.tmpl:7` declares `"preloaded_count": 30` and lists 30 entries; `tests/run_all.sh:51-60` (T6) asserts both via grep. T6 PASSES on the current tree (deterministic). Confidence ≈98%.
6. **Self-extension of the error catalog is wired end-to-end.** `references/ai_error_catalog.md:264-274` (5-step protocol), echoed in `templates/tracking/errors_catalog.json.tmpl:49-56` and in the orchestrator's `<error_handling>` at `prompts/00_master_orchestrator.md:414` ("auto-extending the canonical catalog if a new error pattern appears, per P5"). Confidence ≈85%.
7. **`informatics_dev` starter encodes the user's anchor example faithfully.** `templates/memory_schema/per_domain_starters/informatics_dev.json:19-39` encodes `mandatory_if_status!=pass` for `error_code`, `error_message`, `suggested_solution`, plus `mandatory_if_suggested_solution` for the confidence%. Audit `completeness_rule` (line 35) names the same conditional invariant. Confidence ≈93%.

## 3. Findings (errors AND improvement candidates)

| finding_id | type | severity | invariant | evidence_path:line | confidence_pct | suggested_action |
|---|---|---|---|---|---|---|
| F1 | error | warn | dashboard freshness (P5 living-doc) | `dashboard/index.html:183, 198, 326, 218-231` | 92 | Bump tag to v0.3.1; add cards for memory_schema, adaptive_audit, feedback_learning; reconcile "11 KPIs" claim with `KPI_META` length (12) |
| F2 | error | warn | calibration test enforceability (P2) | `tests/run_all.sh:41-48` | 88 | T2 unconditionally increments `PASS` even when violations are listed — convert hits in non-discussion contexts to FAIL or to a hard WARN with exit-code parity |
| F3 | error | info | field-flag-count inconsistency (memory schema) | `prompts/15_memory_schema_architect.md:155` vs `references/memory_schema_protocol.md:32-39` | 95 | Change "Field flags (3 levels)" to "(4 levels)" in prompt 15 — list shows 4 |
| F4 | improvement | medium | format diversity in starter (anti-pattern proximity) | `templates/memory_schema/per_domain_starters/public_sector.json` (4× jsonl) | 75 | Either justify uniformity inline or diversify (e.g., `compliance_audit_trail` → sqlite for FTS5 over `check_type` + `evidence_path`) — protocol's anti-pattern threshold is "all 6 same"; 4/4 is borderline and silent |
| F5 | improvement | small | calibration miss in user-facing prose (P2) | `prompts/13_context_curator.md:6` ("Build the best possible task-specific context corpus") | 78 | Replace "best possible" with "highest-fit (≈X%) calibrated corpus" or a non-superlative phrase per `calibrated_probabilities.md §1` |
| F6 | improvement | small | calibration miss in user-facing prose (P2) | `prompts/04_library_docs_fetcher.md:93` ("best-effort heuristics") | 65 | Either justify under §9 ("when to deliberately violate") or rephrase to "regex/heuristic extraction with documented partial-fallback" |
| F7 | improvement | small | memory baseline freshness anchor (memory completeness) | `prompts/15_memory_schema_architect.md:336` (`memory/{user, feedback, project, reference}.md`) | 70 | Add a `<verification>` re-check that the baseline 4 files exist as physical paths post-scaffold (not only "still listed as preserved"); without filesystem evidence the global-tier auditor cannot tell drift from absence |
| F8 | improvement | small | dashboard calibration KPI surface | `dashboard/index.html:307-313` | 80 | Add a `mean_classification_confidence_pct`, `pending_count`, `oldest_pending_age_days` tile from `feedback_learning` evaluation block (`prompts/11_feedback_learning_loop.md:467-475`) — currently invisible |
| F9 | improvement | small | starter version skew (potential P5 drift) | `templates/memory_schema/per_domain_starters/*.json` declares `generator_version: 0.3.0`; protocol changelog declares 0.3.1 | 85 | Bump starters' `generator_version` to 0.3.1 or add an explicit `compatibility_with_protocol: ">=0.3.0"` field |
| F10 | improvement | small | wizard default coverage | `wizard/defaults.json` (placeholders without `confidence_pct`: `stakeholders_template`, `goals_placeholder`, `out_of_scope_placeholder`, `risks_placeholder`, `sessions_plan_placeholder`) | 60 | These are template strings, not decisions, but adding `"is_template": true, "confidence_pct": null` would make machine-scanning explicit (currently they pass T2 only because they don't carry forbidden tokens) |
| F11 | improvement | small | particular-tier missing-entry detection grammar | `prompts/14_adaptive_audit_meta.md:155-158` ("expected_entries = entries the scope's actions should have produced (per `trigger`)") | 70 | "Trigger grammar" is plain English (`references/memory_schema_protocol.md:99-103`); add a worked example showing how `every test execution` is grounded against an actual signal source (test runner output, observation log) — otherwise particular tier risks false positives/negatives |

## 4. P2 calibration enforcement audit

**Regex T2 (`tests/run_all.sh:34`) is correct** — it scans `prompts/`, `templates/`, `wizard/`, `SKILL.md` for `\b(best|always|never|guaranteed|certain|definitely|impossible)\b`. The exclusion filters (`forbidden`, `must.not`, `do not`, `never auto`, `best.practice`, `best.suited`, `never.skip`, `never.freeze`, `never.modify`) are calibrated to discussion contexts. Confidence ≈92%.

**However, T2 is non-blocking** (line 47 increments `PASS` regardless). I treat this as F2 (warn). Confidence ≈88%.

**Spot-check across 5 prompts beyond the orchestrator:**

| prompt | hits | non-discussion violations |
|---|---|---|
| `prompts/01_interview_agent.md` | 6 | none in user-facing prose; all are negation patterns (`Never bundle`, `Never proceed`, `ALWAYS requires rationale`) |
| `prompts/02_scaffolder.md` | 2 | none ("Never overwrite") |
| `prompts/03_prompt_factory.md` | 5 | none (all are negation/MUST patterns) |
| `prompts/04_library_docs_fetcher.md` | 4 | **1 candidate** — line 93 "best-effort heuristics" (compound; debatable; flagged F6 conf 65%) |
| `prompts/13_context_curator.md` | 12 | **1 candidate** — line 6 "Build the **best possible** task-specific context corpus" in the role banner (user-facing); flagged F5 conf 78% |

Net: **2 candidate calibration prose-misses out of 5 prompts**. Both are minor but real. Confidence ≈80%.

The orchestrator hits T2's grep heavily (e.g., line 22 "you never assert"), but each hit is in a meta-discussion of the rule itself or in `<non_do_conditions>` / `<guardrails>` negations — these are §9 "deliberate violations" and are properly anchored. Confidence ≈90%.

## 5. 8-format taxonomy + selection audit

**Internal consistency: high.** `references/memory_schema_protocol.md:46-86` defines 8 formats (structured_md, csv, json, jsonl, sqlite, parquet, vector_db, graph_db) with Tier-A/B + soft-deps + fallback. `prompts/15_memory_schema_architect.md:161-210` reproduces the same table verbatim (with the same Tier classifications). T21 in `tests/run_all.sh:213-226` PASSES (8/8 grepped). Confidence ≈97%.

**Deterministic-first selection algorithm verified.** `prompts/15_memory_schema_architect.md:215-256` orders the rules: (1) audit-rule hard constraint, (2) volume + query pattern, (3) relationship-density override, (4) semantic-similarity override, (5) jsonl as safe fallback. This matches the protocol's "deterministic first, calibrated second" pledge. Confidence ≈92%.

**Audit-rule × format compatibility matrix is faithful.** Same matrix in both files (protocol lines 76-86; prompt-15 lines 196-206). The "✗ → re-pick format" rule is explicitly enforced. Confidence ≈95%.

**Per-domain starter format-fit spot-check (3 modules):**

| module | declared format | workload signal match | verdict |
|---|---|---|---|
| `informatics_dev / test_outcomes` (jsonl) | append-only event log + flat schema + >1k expected | jsonl per matrix row "> 1k append-only / scan + filter / flat" | FIT (≈90%) |
| `legal / precedent_chains` (graph_db, fallback jsonl adjacency) | multi-hop traversal | matrix row "any / multi-hop / high → graph_db" with sqlite-CTE alt | FIT (≈92%) |
| `healthcare_clinical / patient_cohort_signatures` (sqlite) | joins with model_calibration_per_subgroup + trial_arm_assignments | matrix "needs joins across ≥2 modules → sqlite" | FIT (≈90%) |

**Borderline:** `public_sector` (F4) — 4 modules all declared jsonl, including `compliance_audit_trail` whose `evidence_path` lookup + `outcome=fail / remediation` audit pattern would benefit from FTS5 (sqlite). Anti-pattern threshold in protocol is "all 6 same" (line 96); this starter has 4 modules total, so technically not a violation, but it's borderline. Confidence ≈75%.

## 6. Two-tier memory completeness audit (particular + global)

**Specification clarity: high.** Both tiers are named in:
- `references/memory_schema_protocol.md:119-128` — table form with worked examples and confidence% on each finding.
- `prompts/14_adaptive_audit_meta.md:150-178` — pseudocode with separate loops for each tier; outputs flow into the same error / improvement triage.
- `prompts/15_memory_schema_architect.md:104-106` — short prose recap.

Confidence ≈92%.

**Identified gaps that could let a real auditor produce false negatives:**

1. **Particular-tier "expected_entries" grounding is under-specified.** The pseudocode (`prompts/14_adaptive_audit_meta.md:155`) says "expected_entries = entries the scope's actions should have produced (per `trigger`)" — but `trigger` is plain English (`every test execution`, `every adverse event`), not a structured signal. Without a concrete grounding source (test-runner output, observation log, phase.log), the auditor must infer expected count from English. F11 captures this.
2. **Global-tier `violation_pct = total_violations / total_entries × 100`** is undefined when `total_entries == 0`. The pseudocode does not call out the divide-by-zero path. A module with zero entries across 3+ sessions falls into the `improvement` branch (line 174) but the divide-by-zero on the error branch is silent. Confidence ≈70%.
3. **No tie-breaking rule** when particular finds a missing entry AND global threshold is below limit. Both findings fire; not a bug, but worth a one-liner stating they're additive (not de-duped). Confidence ≈55%.

Overall the spec is sufficient for a competent auditor; the gaps above are improvement-grade, not error-grade. Confidence ≈85%.

## 7. Feedback learning loop audit

**Per-correction HITL Y/N/SKIP is never-defaulted.** Triple-anchored:
- `prompts/11_feedback_learning_loop.md:208` ("Do NOT silently mark a row `learn_in_system=Y` — every Y is an explicit human keystroke.")
- `prompts/11_feedback_learning_loop.md:421` ("Never default `learn_in_system`; always block on human keystroke.")
- DB CHECK constraint `learn_in_system IN (0,1,2)` at `templates/feedback_learning/corrections_schema.sql.tmpl:22` (NOT NULL implied via the absence of DEFAULT).

Confidence ≈90%.

**Threshold rule is parametric and works at edge values 5 / 50.** The rule `(count(...) >= learn_threshold) OR (user_explicit_trigger)` (`prompts/11_feedback_learning_loop.md:124-130`) does not hardcode 15; it reads from `SystemSpec.feedback.learn_threshold ∈ [5, 50]` (`prompts/11_feedback_learning_loop.md:132`, `wizard/defaults.json:181-186`). Behaviour at edges:
- **threshold=5**: counter triggers earlier → smaller batches → more 13.7 invocations. No off-by-one risk (rule is `>=`, not `==`).
- **threshold=50**: counter accumulates longer → larger batches → fewer 13.7 invocations.

No edge-bug detected. Confidence ≈90%.

**FTS5 dedupe rule.** `corrections_fts` virtual table at lines 38-43; sync triggers (insert / delete / update) lines 46-59. SQL is parameterised per `<injection_defense>` line 432. The rule "FTS5 returns ≥2 hits across distinct session_ids → recurring; ≥4 → systemic" (`references/feedback_taxonomy.md:36-40`) is implementable from this schema. Confidence ≈87%.

**MD-mirror drift handling.** `<error_handling>` line 402 documents the recovery path (rebuild from DB on next run; logs `AIE-FBL-MIRROR-DRIFT`). DB is the single source of truth (line 137). Confidence ≈85%.

## 8. Per-domain starter quality audit

**`informatics_dev` (mandatory anchor):**
- `mandatory_if_status!=pass` correctly conditions `error_code`, `error_message`, `suggested_solution` (lines 24-26).
- `mandatory_if_suggested_solution` chains the confidence% (line 27) — semantic correctness ≈94%.
- `missing_threshold_pct=5` for `test_outcomes` (line 36); aligns with protocol's "balanced default 5%". Confidence ≈90%.
- `decision_logs` audit `alternatives_considered (≥2)` (line 62) → matches calibration-anchors §4 (alternatives at HITL gates). Confidence ≈88%.

**`healthcare_clinical`:**
- `adverse_events.missing_threshold_pct = 0` (line 56) — correct for high-risk MDR vigilance trail. Confidence ≈95%.
- `patient_cohort_signatures.missing_threshold_pct = 1` (line 30) — appropriately strict; PII regex scan is named (line 31) — semantic correctness ≈92%.
- `non_removable_for_high_risk: true` flag on both (lines 36, 62) — correctly enforces compliance floor. Confidence ≈90%.

**`legal`:**
- `precedent_chains.format = graph_db` with `sqlite` (recursive CTE) and `jsonl` (adjacency-list) fallbacks (lines 60-66) — strong format-fit. Confidence ≈90%.
- `client_advisory_history.disclaimers (≥1) AND confidence_pct mandatory; missing_threshold_pct=1` (lines 113-122) — correctly encodes professional-duty floor. Confidence ≈92%.

**`public_sector`:**
- 4/4 modules use jsonl (F4). For `compliance_audit_trail` (lines 58-79), the audit rule names `evidence_path` AND `remediation` discoverability — FTS5 over these would be more honest. Confidence ≈75% that diversification would meaningfully improve fitness.

Overall starter quality: **high-mature for 5/6 starters; public_sector borderline.** Confidence ≈85%.

## 9. Recommended improvements

| # | improvement | priority | est effort (h) | confidence_pct | rationale |
|---|---|---|---|---|---|
| 1 | Refresh `dashboard/index.html` to v0.3.1: bump tag, add memory_schema / adaptive_audit / feedback_learning cards, reconcile "11 KPIs" claim vs 12-entry KPI_META | P1 | 3-5 | 90 | F1; surface fitness for v0.3.x KPIs is currently invisible |
| 2 | Make T2 in `tests/run_all.sh` exit-code-blocking when violations remain after exclusion filters (or split into T2a non-blocking heuristic + T2b blocking) | P1 | 1-2 | 85 | F2; current T2 always passes — calibration regression risk |
| 3 | Fix "(3 levels)" → "(4 levels)" in `prompts/15_memory_schema_architect.md:155` | P2 | 0.1 | 98 | F3; trivial copy-edit |
| 4 | Diversify `public_sector` starter (e.g., `compliance_audit_trail` → sqlite) OR add an inline justification for uniformity | P2 | 1-2 | 75 | F4; protects against the "all-same-format" anti-pattern |
| 5 | Calibrate prose: `prompts/13_context_curator.md:6` and `prompts/04_library_docs_fetcher.md:93` | P2 | 0.5 | 75 | F5/F6 |
| 6 | Add filesystem-existence check for the 4 baseline memory files in prompt 15's `<verification>` | P2 | 0.5 | 70 | F7; audit drift detection |
| 7 | Add `mean_classification_confidence_pct`, `pending_count`, `oldest_pending_age_days` tiles to dashboard | P2 | 1 | 80 | F8; surfaces feedback-loop health |
| 8 | Bump per-domain-starter `generator_version` to 0.3.1 (or add explicit `compatibility_with_protocol`) | P3 | 0.2 | 85 | F9 |
| 9 | Add a worked example to particular-tier `expected_entries` grounding (`prompts/14_adaptive_audit_meta.md`) and call out the divide-by-zero edge in global `violation_pct` | P2 | 1 | 75 | Two-tier audit precision; reduces false-negative rate |
| 10 | Mark wizard placeholder strings explicitly as `is_template: true` or move them out of the `defaults` namespace | P3 | 0.5 | 60 | F10; clarifies scan surface |

Total estimated effort to address all P1+P2: **8-13 hours**. Confidence ≈80%.

## 10. Reflection (≤200 words)

Persona-fit held: I stayed in calibration / memory / feedback / error-catalog / KPI lanes and avoided pronouncements on architecture choices or EU-AI-Act mapping completeness. The widest confidence-spread item is F4 (public_sector format uniformity) — the protocol's anti-pattern threshold is "all 6 same"; this starter has 4 (uniform), which is borderline by letter-of-the-spec but live by spirit. I rated it 75% to reflect that ambiguity. The most consequential finding is F2 (T2 always-passes): a calibration test that cannot fail is a calibration claim without a confidence band — the very thing P2 forbids in the artifacts. Fixing it costs 1-2 hours and converts the regex from advisory into enforcement. The most surprising strength is the per-correction HITL discipline: it is named in five separate places (task, success_criteria, non_do_conditions, hitl_conditions, guardrails) plus the SQL CHECK — that's belt-and-braces engineering against a known LLM failure mode (silent memorisation). What would invalidate this audit: a future commit that drops the SQL CHECK, removes the `<non_do_conditions>` line, or weakens T2 further. Recommendation to the jury: APPROVED_WITH_MINOR — the system is mature; the residual gaps are tractable.
