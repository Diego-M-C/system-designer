# Changelog

All notable changes to `system-designer`. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/spec/v2.0.0.html).

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

[0.2.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.2.0
[0.1.0]: https://github.com/Diego-M-C/system-designer/releases/tag/v0.1.0
