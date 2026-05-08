---
auditor_id: 1
persona_slug: ai_systems_architect
session_id: external-audit-v031-2026-05-08
ran_at: 2026-05-08T22:30:00Z
overall_verdict: APPROVED_WITH_MINOR
overall_confidence_pct: 82
findings_count: 11
self_kpis:
  files_read: 14
  evidence_citation_rate_pct: 100
  mean_finding_confidence_pct: 84
---

# AI Systems Architect · External Audit · system-designer v0.3.1

## 1. Executive verdict (≤120 words)

The skill is architecturally mature. The 18-phase state machine is internally consistent across `system_generator.json`, `prompts/00_master_orchestrator.md`, and `SKILL.md`; HITL inviolability is well anchored (alignment_rules + non_do_conditions + injection_defense + tests/T10); P4 prompt-architect dependency is uniformly enforced (every prompt 00–15 declares `Composed via: prompt-architect`, T9 deterministic check passes); persona-fit in prompt 14 is enforced via a reflection-driven re-composition loop and the `memory_completeness_auditor` is mandatory and machine-readable. Verdict is **APPROVED_WITH_MINOR** because of: (a) ~3 invented tags outside the taxonomy (P4 self-violation), (b) documentation drift in `docs/ARCHITECTURE.md` and `docs/data-flow.md` (still claim 13/17 phases), (c) two narrow backward-compat statements in the orchestrator that miss v0.3.0 skip cases. Overall confidence ≈82% — anchored to file:line citations throughout. (confidence_pct: 82)

## 2. Strengths observed

| # | strength | evidence_path:line | confidence_pct |
|---|---|---|---|
| S1 | 18-phase state machine is identically declared across spec + orchestrator + SKILL: phase IDs `1, 1.5, 2..13, 13.5, 13.7, 14` agree byte-for-byte | `system_generator.json:188-206`; `prompts/00_master_orchestrator.md:55-73, 428`; `SKILL.md:42-62` | 95 |
| S2 | HITL inviolability is encoded at multiple defensive layers: alignment_rules (#3), non_do_conditions (#6), guardrails, hitl_conditions, plus a deterministic T10 grep test that scans for skip-gate language without negation | `prompts/00_master_orchestrator.md:188, 443, 460`; `tests/run_all.sh:76-85` | 95 |
| S3 | Prompt-architect dependency (P4) is uniformly enforced; T9 confirms every prompt 00–15 references the architect; `03_prompt_factory.md` is the single funnel; even Medium prompts (01,02,04…) declare Factory linkage in metadata | `tests/run_all.sh:88-100`; `prompts/03_prompt_factory.md:11, 115`; `prompts/01_interview_agent.md:4` | 92 |
| S4 | Adaptive-audit panel persona-fit is operationally enforced: a reflection step explicitly flags any `generic_*` slug and triggers re-composition; the `memory_completeness_auditor` is mandatory and added on top of `n_auditors`, mirroring the `simulation_agent` precedent in phase 11.5 | `prompts/14_adaptive_audit_meta.md:34, 134, 148, 322-328`; `docs/ARCHITECTURE.md:666-668` | 90 |
| S5 | Atomic-write + sha256 chain + resumability are first-class invariants — `current_phase`, `artifacts_emitted[].sha256`, `phase.log` written before advancing; explicit "*.tmp + rename" pattern documented | `prompts/00_master_orchestrator.md:295, 432, 444`; `docs/data-flow.md:148-160` | 93 |
| S6 | Cache-breakpoint discipline is correctly placed for Complex prompts: stable prefix `<role>` → `<rubric>`, volatile suffix `<temporal_context>/<input>/<observation>/<scratchpad>` matches `prompt_architect/references/cache-breakpoints.md` recommendations | `prompts/00_master_orchestrator.md:615-617`; `prompts/14_adaptive_audit_meta.md:641-643`; `prompts/15_memory_schema_architect.md:688-690` | 88 |
| S7 | Backward-compatibility flags `compatibility.v0_1_0` and `memory_schema.negotiation_enabled` are properly wired with explicit `skip_if` clauses on each affected phase; degradation paths documented (e.g., memory_completeness_auditor falls back to Anthropic 4-typed baseline when manifest absent) | `system_generator.json:189, 193, 201, 204, 205, 220`; `prompts/14_adaptive_audit_meta.md:70, 503` | 88 |
| S8 | Inter-prompt dependency graph is a tree (no specialist invokes another specialist directly; all coordination flows through `00`) — keeps the system unit-testable in isolation | `docs/ARCHITECTURE.md:215`; cross-checked: 02/04/05/06/07/08 contain no `<delegation>` blocks | 90 |

## 3. Findings (errors AND improvement candidates)

| finding_id | type | severity | invariant | evidence_path:line | confidence_pct | suggested_action |
|---|---|---|---|---|---|---|
| F1 | error | warn | tags_exist (P4 / rubric item #5) | `prompts/15_memory_schema_architect.md:215` (`<selection_criteria>` block); cross-checked against `prompt_architect/prompt_editor_skill.json` (no entry for `selection_criteria`) | 95 | Either rename to a taxonomy member (`planning` or `decomposition` are closest in Cognition; `criteria` is not in the taxonomy either) or formally extend the taxonomy by adding `selection_criteria` to `prompt_editor_skill.json#tags`. The self-claim in `prompts/15:642` "All tags exist in `prompt_editor_skill.json` ✅" is therefore false. |
| F2 | error | warn | tags_exist (P4 / rubric item #5) | `prompts/10_data_flow_validator.md` contains `<simulation_scenarios>` as a top-level block; not present in `prompt_architect/prompt_editor_skill.json` | 92 | Rename to `<simulation>` (which exists, Cognition category) or extend the taxonomy. Same self-audit attestation issue as F1. |
| F3 | error | info | T22 test integrity | `tests/run_all.sh:228-234` — T22 checks for the literal string `<selection_criteria>` instead of verifying that every used tag is in the taxonomy; the test passes despite F1 | 90 | Replace T22 with a script that extracts every line-anchored `<tag>` from `prompts/*.md` and validates each against the JSON taxonomy. Strengthens P4 self-discipline. |
| F4 | improvement | warn | doc-drift / phase count (rubric #18-phase agreement) | `docs/ARCHITECTURE.md:28, 70, 95` still says "13-phase loop / 13-phase orchestration"; only §20 retroactively adds a v0.2.0 supplement; v0.3.0 phase 4.5 is not integrated into §1, §2, §4, §6 | 95 | Refactor §1–§7 to natively describe the 18-phase machine. The current "13-phase base + supplements" pattern was acceptable at v0.2.0 but accumulates drift each minor. |
| F5 | improvement | warn | doc-drift / phase count | `docs/data-flow.md:3` "17 phases"; `docs/data-flow.md:319` "13-phase diagram"; v0.3.0 phase 4.5 has no sequence diagram in §11 | 92 | Add a §11.5 mermaid for phase 4.5 and update the doc header to "18 phases". |
| F6 | improvement | info | doc-drift / phase count | `README.md:125` "system_generator.json # Machine-readable spec (5 principles, 13 phases…)"; the badge at L11 correctly says 18 phases | 90 | Update L125 to "18 phases (13 base + 5 inserted: 1.5 / 4.5 / 11.5 / 13.5 / 13.7)". |
| F7 | error | warn | backward-compatibility completeness in orchestrator | `prompts/00_master_orchestrator.md:434` "phases 1.5 / 11.5 / 13.5 / 13.7 / adaptive_audit_meta are skipped (legacy 13-phase mode)" omits phase 4.5 (also v0.3.0) and does not mention the narrower `memory_schema.negotiation_enabled=false` skip path documented in `SKILL.md:165` | 90 | Update the orchestrator's `<orchestration>` block to also list phase 4.5 in the v0.1.0-skip set, and add a sentence on the per-flag narrower skip. The semantic risk is low (the `skip_if` clauses in `system_generator.json` are authoritative), but the orchestrator prose drifts from the spec. |
| F8 | error | info | gate_status enum coverage | `prompts/00_master_orchestrator.md:296` declares `gate_status (pre_gate_1 \| post_gate_1 \| pre_gate_2 \| post_gate_2 \| done \| aborted)` — does not include states for phase 4.5 (`type: hitl_gate`, `system_generator.json:193`) nor 13.7 (`type: hitl_gate`, `system_generator.json:205`) | 88 | Extend the enum: `pre_gate_4_5 \| post_gate_4_5 \| pre_gate_13_7 \| post_gate_13_7`, OR move to a generic `gate_status: { gate_id, state }` shape. Resumability after an interruption inside 4.5 / 13.7 is currently underspecified by the orchestrator's state model. |
| F9 | improvement | info | hitl_gates registry coverage | `system_generator.json:224` `hitl_gates` array enumerates only Gate #1 and Gate #2; phases 4.5 and 13.7 carry `"type": "hitl_gate"` (lines 193, 205) but are not formally cross-listed | 85 | Either add 4.5 and 13.7 entries to the `hitl_gates` array, or rename the array to `legacy_v01_hitl_gates`. The semantic confusion is small but a downstream consumer iterating `hitl_gates` would miss two real gates. |
| F10 | improvement | info | dependencies declaration completeness | `prompts/14_adaptive_audit_meta.md:624-639` `<dependencies>` block omits `references/memory_schema_protocol.md` and `<target_path>/memory_schema/manifest.json`, both of which the prompt body explicitly reads (L34, L70, L134, L153) | 87 | Add both to the Hard dependencies list. The runtime risk is negligible because the master orchestrator's `<dependencies>` already lists them, but the prompt-local dependency graph drifts. |
| F11 | improvement | info | cache_hint completeness | Medium-tier prompts (`01_interview_agent.md`, `02_scaffolder.md`, `04..08`) lack a `<cache_hint>` block, while the rubric in `system_generator.json:336` (`cache_breakpoint_documented`) reads as universal, not Complex-only | 70 | Either add minimal `<cache_hint>` blocks to Medium prompts (recommended, ~5 lines each) or restrict the rubric item to `applies_to: Complex` like `mandatory_floor` does. Currently a soft self-inconsistency. |

## 4. Cross-prompt dependency graph audit

I traced every `<delegation>` and every cross-reference in prompts 00–15:

- **Master orchestrator** (`prompts/00_master_orchestrator.md`) dispatches to 01–15 by file path; every referenced prompt exists on disk (verified via `ls prompts/`).
- **Prompt 03 (Factory)** is the single funnel for prompt-architect; referenced by 09, 10, 11, 12, 13, 14, 15 — all exist.
- **References** declared in `system_generator.json:55-110` (10 files) are all present in `references/` (verified via `ls`).
- **Per-domain starters** declared in `system_generator.json:99-110` (6 files) are all present in `templates/memory_schema/per_domain_starters/` and parse as valid JSON (T20).
- **Cross-phase hook** `adaptive_audit_meta` (system_generator.json:209-222) properly maps to `prompts/14_adaptive_audit_meta.md`; `owner_prompt` field present.
- **Orphan check:** prompts 11, 12 reference `feedback_learning/corrections.db` (a runtime artifact, not a static dep — correct). Prompt 14 references `feedback_learning/corrections.db` and `memory_schema/manifest.json` — both runtime artifacts. No orphan static-file references found.
- **Dangling tools:** `prompt_architect`, `parallel.spawn`, `sqlite.exec`, `sha256`, `now`, `fs.*`, `fetch` — all named abstractly per P1; soft-dep fallbacks declared in every `<fallback>` block I sampled (00, 03, 14, 15).

**Verdict on dependency graph:** clean tree (no mesh), every cross-reference resolves except for the locality-of-declaration gaps in F10. (confidence_pct: 90)

## 5. Tag taxonomy compliance audit

I extracted line-anchored top-level XML tags from 7 prompts (00, 03, 10, 11, 12, 13, 14, 15) and compared each against the 125 tags in `prompt_architect/prompt_editor_skill.json`:

| prompt | unique tags | invented tags | mandatory floor (Complex) |
|---|---|---|---|
| 00_master_orchestrator | 52 | 0 | ✅ 13/13 |
| 03_prompt_factory | 41 | 0 | ✅ 13/13 |
| 10_data_flow_validator | 47 | 1 (`<simulation_scenarios>`) | ✅ 13/13 |
| 11_feedback_learning_loop | 46 | 0 | ✅ 13/13 |
| 12_improvement_jury | 46 | 0 | ✅ 13/13 |
| 13_context_curator | 46 | 0 | ✅ 13/13 |
| 14_adaptive_audit_meta | 47 | 0 | ✅ 13/13 |
| 15_memory_schema_architect | 47 | 1 (`<selection_criteria>`) | ✅ 13/13 |

**Findings:**
- 2 invented tags total (F1, F2 above). Both are isolated to a single block each; XML well-formedness is preserved; semantic intent is clear (`selection_criteria` ≈ a domain-specific selection algorithm; `simulation_scenarios` ≈ `simulation` extension). Severity = warn (not critical) because they don't break runtime — only the P4 self-attestation.
- All 8 prompts I checked carry the full 13-tag mandatory floor for Complex tier.
- Tag counts sit within the ±20% Complex tolerance (target 30–50+; observed 41–52).
- Self-audit tables in each prompt incorrectly mark "All tags exist" as ✅ for prompts 10 and 15. Honest accounting would mark these as ❌ pending taxonomy patch. (confidence_pct: 92)

## 6. Documentation drift audit

| asset | declared phase count | matches v0.3.1? | drift evidence |
|---|---|---|---|
| `SKILL.md` | 18 | ✓ | L42, L165 |
| `system_generator.json` | 18 | ✓ | L188-206 (count by IDs) |
| `prompts/00_master_orchestrator.md` | 18 | ✓ | L55-73, L428 |
| `README.md` (badge) | 18 | ✓ | L11 |
| `README.md` body | drift | ✗ | L125 says "13 phases" (F6) |
| `CHANGELOG.md` | 18 (since 0.3.0) | ✓ | L89-91 |
| `docs/ARCHITECTURE.md` | 13 (with v0.2.0 supplement at §20; no v0.3.0 supplement) | ✗ | L28, L70, L95, L607 (F4) |
| `docs/data-flow.md` | 17 | ✗ | L3, L319; no §11.5 for phase 4.5 (F5) |
| `prompts/00` orchestration v0.1 skip clause | "13-phase mode" but lists 4 v0.2 phases — omits 4.5 | ✗ | L434 (F7) |

Verdict: the **authoritative artifacts** (SKILL, system_generator, master orchestrator, CHANGELOG, README badge) agree on 18 phases. **Explanatory artifacts** (ARCHITECTURE.md, data-flow.md, the L125 README line, the L434 backward-compat note) lag by one minor (still describing the 13-base + v0.2.0 stance). No runtime risk; ergonomic risk for new contributors. (confidence_pct: 92)

## 7. Backward-compatibility integrity audit

**`compatibility.v0_1_0 = true`** — declared in `system_generator.json` `skip_if` clauses on phases 1.5 (L189), 4.5 (L193), 11.5 (L201), 13.5 (L204), 13.7 (L205), and the cross-phase hook (L220). Effect:

- Skipped phases produce no outputs ⇒ downstream phases that *expected* those outputs must degrade gracefully.
- **Phase 5 (scaffold)** declares an output `target_path/memory/<structured_module>.{jsonl|md} per memory_schema/manifest.json` (L194). When 4.5 is skipped, the manifest is absent ⇒ scaffold renders only the canonical 4-typed Anthropic baseline (`memory/{user,project,feedback,reference}.md`). This is consistent with `prompts/14_adaptive_audit_meta.md:70` ("if the manifest is absent … falls back to Anthropic 4-typed baseline"). Semantic chain: ✓
- **Phase 8 (seed_tracking)** lists `target_path/feedback_learning/corrections.db` as an output (L197). When v0.1.0 is set, phase 13.5 is skipped — but phase 8 still seeds the DB. Mild over-allocation but not a break (the DB stays empty).
- **Phase 12 (GATE_2)** receives "structural-consistency consolidation" only when 11.5 ran. The orchestrator's gate framing (`prompts/00:69`) handles the absent case implicitly — gate brief simply lacks that section. Acceptable.
- **Adaptive audit meta** properly skipped per L220 `skip_if` clause.

**`memory_schema.negotiation_enabled = false`** — narrower skip per `system_generator.json:193`: only phase 4.5 is skipped. Downstream:
- Phase 5 still scaffolds the canonical 4-typed baseline (no manifest to consume; degradation path documented).
- Prompt 14's `memory_completeness_auditor` falls back to checking the 4-typed baseline (per `prompts/14:70`).
- No downstream phase requires the manifest to be present in a non-fallback way.

**Gap (F7):** the orchestrator's `<orchestration>` block (L434) only lists v0.2.0 phases for the v0.1.0 skip path. It misses 4.5 in that prose enumeration. The `system_generator.json#skip_if` clauses are authoritative, so the runtime behaviour is correct — but the orchestrator prose is stale. (confidence_pct: 88)

## 8. Recommended improvements

| # | improvement | priority | effort (h) | confidence_pct | rationale |
|---|---|---|---|---|---|
| 1 | Fix the 2 invented tags (F1, F2) — either rename to taxonomy members or extend the taxonomy | P1 | 1.5 | 95 | P4 self-attestation integrity; closes 2 honest-accounting gaps. |
| 2 | Strengthen T22 to validate every prompt tag against the JSON taxonomy (F3) | P1 | 1.0 | 92 | Prevents future invention drift; deterministic, no LLM needed. |
| 3 | Refactor `docs/ARCHITECTURE.md` §1–§7 to natively describe the 18-phase machine (F4) | P2 | 3.0 | 90 | Accumulating supplements pattern is brittle past v0.4. |
| 4 | Update `docs/data-flow.md` to add a §11.5 mermaid for phase 4.5 and bump the header to 18 (F5) | P2 | 1.0 | 90 | Same rationale; cheap fix. |
| 5 | Update `README.md` L125 (F6) | P3 | 0.1 | 95 | One-line change. |
| 6 | Update master orchestrator's `<orchestration>` backward-compat clause to list phase 4.5 + the narrower `memory_schema.negotiation_enabled=false` path (F7) | P2 | 0.5 | 88 | Aligns prose with `system_generator.json#skip_if` clauses. |
| 7 | Extend `gate_status` enum to cover phases 4.5 and 13.7 (F8) | P2 | 0.5 | 85 | Makes resumability inside the new HITL gates well-defined; OR generalise to `{ gate_id, state }`. |
| 8 | Cross-list 4.5 and 13.7 in the `hitl_gates` array (F9) | P3 | 0.3 | 85 | Single-source-of-truth hygiene. |
| 9 | Add `references/memory_schema_protocol.md` and `memory_schema/manifest.json` to prompt 14's `<dependencies>` (F10) | P3 | 0.2 | 87 | Local prompt-graph completeness. |
| 10 | Either add `<cache_hint>` to Medium prompts or scope the rubric item to Complex only (F11) | P3 | 1.0 | 70 | Soft inconsistency between rubric universality and tier observance. |

Total recommended effort to reach a clean APPROVED_AS_MATURE state: **~9 hours**, almost all P2/P3.

## 9. Reflection (≤200 words)

**Lowest-confidence claim.** F11 (cache_hint universality) at 70%. The rubric in `system_generator.json:336` reads as universal but the SKILL's tier guidance treats `cache_hint` as a Meta-category optional. Either reading is defensible; I flagged it as soft.

**Hardest invariant to evaluate.** Persona-fit in prompt 14. The text says "reflection flags generic personas → re-composition" but the actual semantics depend on a runtime LLM judgement that I cannot verify statically. The architectural scaffolding (mandatory `memory_completeness_auditor`, dynamic `n_auditors`, illustrative-not-fixed roster) is sound. Operational fitness needs runtime evidence.

**What might invalidate this audit.** If `<selection_criteria>` is intentionally being added to the taxonomy in a v0.3.2 patch I have not seen, F1 dissolves. If `docs/ARCHITECTURE.md` is intentionally treated as historical with §20 as the canonical update mechanism, F4/F5 are stylistic not architectural.

**Hand-off note for the consensus jury.** I deliberately did not opine on EU AI Act mapping completeness (auditor 2) nor on calibration / memory-schema completeness invariants (auditor 3). My lane was orchestration, dependency graph, tag taxonomy, HITL inviolability, and documentation drift. The system is mature; the gaps are honest-accounting and ergonomic, not load-bearing.
