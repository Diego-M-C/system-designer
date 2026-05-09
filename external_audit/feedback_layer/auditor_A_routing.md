---
auditor_id: A
persona_slug: error_memory_routing_specialist
session_id: feedback-layer-audit-v100-2026-05-09
ran_at: 2026-05-09T12:00:00Z
overall_verdict: NEEDS_IMPROVEMENT
overall_confidence_pct: 82
findings_count: 8
self_kpis:
  files_read: 19
  evidence_citation_rate_pct: 100
  mean_finding_confidence_pct: 81
---

# Error-Memory Routing Specialist · Feedback-Layer External Audit · v1.0.0

## 1. Executive verdict (≤120 words)

The capture/persistence layer (phase 13.5) and the source-change audit gate (phase 13.7) are **architecturally mature**: the SQLite schema is fit for purpose, the dual-mirror (DB + MD) is genuinely atomic, status lifecycle is explicit, and HITL is inviolable. However, the **routing logic between captured corrections and the rest of the system has structural gaps** that defeat the user's anchor concern ("*el agente lo lea para no cometer esos errores*"). Specifically: (a) child orchestrators are not wired to read `corrections.db` at session start; (b) `category=memory` corrections have no documented path to update `memory_schema/manifest.json`; (c) the AIE catalog's auto-extension protocol predates phase 13.5 and never bridges from approved corrections to new AIE entries. Routing is **under-specified, not broken** — actionable in P1 patches.

## 2. Strengths observed (≥3, each anchored to file:line)

- **Deterministic threshold rule with full SQL observability.** `prompts/11_feedback_learning_loop.md:124-130` makes the trigger expression a single SELECT plus an explicit user override, and `corrections_schema.sql.tmpl:32` indexes `(status, learn_in_system)` so the counter check is O(log n). No hidden heuristics. Confidence 95%.
- **Lifecycle preserved via status, never via deletion.** `corrections_schema.sql.tmpl:23-24` enforces a CHECK on the 4-state status enum; `prompts/11_feedback_learning_loop.md:210` and `prompts/12_improvement_jury.md:202-203` both explicitly forbid row deletion. This means the audit chain is reconstructable from the DB at any future point — strong EU AI Act Art. 12 fit. Confidence 92%.
- **FTS5 sync is correctly wired at the schema level.** `corrections_schema.sql.tmpl:46-59` implements the canonical `corrections_ai/ad/au` trigger trio against a `content='corrections'` virtual table — the recurrence-detection substrate is present and idiomatic. The infrastructure exists; what is missing is a *consumer of the search* outside phase 13.5 itself (see Finding F-3). Confidence 90%.
- **HITL inviolability survives the routing layer.** `prompts/11_feedback_learning_loop.md:208-209` and `prompts/12_improvement_jury.md:218-220` both make the human keystroke a hard pre-condition for any state transition, and the jury's `<knowledge_base>` consensus rule (`prompts/12_improvement_jury.md:110-141`) refuses auto-merge even on unanimous high-confidence approval. Routing into source-changes cannot bypass humans. Confidence 93%.
- **Adaptive auditor is the channel that *does* work for routing improvements in.** `prompts/14_adaptive_audit_meta.md:44-46` cleanly states "improvements queued at status='pending_review', learn_in_system=2 (SKIP) until phase 13.5 prompts the human" — the auditor → phase 13.5 inflow is unambiguous. The defect is on the *outflow* side. Confidence 88%.

## 3. Findings (errors AND improvement candidates)

| finding_id | type | severity | invariant | evidence_path:line | confidence_pct | suggested_action |
|---|---|---|---|---|---|---|
| F-1 | error | error | Child orchestrator must consult prior memorised corrections at session start so the agent does not repeat them. | `templates/CLAUDE.md.tmpl:24-37` | 92 | Add bullet 5b to "Mandatory reads at session start" listing `feedback_learning/corrections.md` filtered to `status IN ('approved','incorporated')`. |
| F-2 | error | error | Approved corrections with `category=memory` should propagate to `memory_schema/manifest.json#modules` (or `#evolution_log`). | `prompts/11_feedback_learning_loop.md:33-42` AND `prompts/15_memory_schema_architect.md:30-40` | 88 | Add a step in phase 13.7 (or post-13.7 merge) that, on `category=memory` AND `status='approved'`, signals phase 4.5 in `living_update` mode with the proposal as input. Wire `manifest.json#evolution_log[]` writes. |
| F-3 | error | error | Recurrence detection (FTS5) is wired only as a *classifier* of the current correction; the agent never queries it as a *guard* before acting. | `prompts/11_feedback_learning_loop.md:244-249` | 90 | Add a "consult corrections_fts before acting on any task whose category overlaps a known recurring pattern" step to `templates/CLAUDE.md.tmpl` and to `prompts/14_adaptive_audit_meta.md`'s scope-envelope construction. |
| F-4 | improvement | warn | AIE catalog auto-extension protocol is decoupled from approved-correction outflow. | `references/ai_error_catalog.md:264-274` AND `prompts/05_error_prevention_seeder.md` (no AIE-from-correction wiring) | 85 | Add a step in phase 13.7's post-approval branch: for `category in {tooling, calibration, prompt_architect}`, draft an AIE-NNN entry and append to `tracking/errors_catalog.json` (with `preloaded:false`, `first_seen_session=<correction.session_id>`). |
| F-5 | error | warn | The "incorporated" status is collapsed across two semantically distinct outcomes (memory entry vs. source change) — the schema lacks a discriminator. | `corrections_schema.sql.tmpl:23-29` | 80 | Add a column `incorporation_kind TEXT CHECK(incorporation_kind IN ('memory','source','both','manifest_evolution','aie_extension'))` populated when `status` transitions to `incorporated`. Backwards-compatible (NULLable). |
| F-6 | improvement | warn | Cross-system (cross-child-project) feedback portability is undocumented. A correction learned in child X is permanently siloed from child Y. | `prompts/00_master_orchestrator.md:54-75` AND `prompts/02_scaffolder.md:30-37` (no global-lessons inheritance) | 78 | Decide explicitly: (a) intentional silo (privacy/scope) → document the rationale in a one-paragraph note; OR (b) optional inheritance via a `references/learned_corrections_global.md` curated by the meta-skill maintainer with HITL sign-off. Surface choice at phase 4.5. |
| F-7 | improvement | warn | `category=other` is the documented signal for taxonomy refresh, but the loop does not actually emit a *proposal* to amend `references/feedback_taxonomy.md`. | `references/feedback_taxonomy.md:80-82` AND `templates/feedback_learning/session_close.md.tmpl:18` | 75 | When session-close `OTHER_COUNT > 3`, automatically draft a `taxonomy_refresh_proposal.md` and queue it as a `category=documentation, severity=warn` correction. Self-feeds the loop. |
| F-8 | improvement | info | The `corrections_fts` rebuild step (`prompts/11_feedback_learning_loop.md:218`) is conditional ("if needed") with no triggering condition specified; idempotent rebuild every N inserts is safer. | `prompts/11_feedback_learning_loop.md:218` | 70 | Specify "rebuild every 100 inserts OR on schema upgrade"; add a counter to `tracking/project.json#feedback_learning.fts_rebuild_count`. |

## 4. Classification → action routing matrix

The taxonomy declares 9 categories × 4 severities × 3 recurrences = 108 cells, but the documented action paths only instantiate explicitly for ~6 of the 9 categories. The matrix below traces what each category should produce when `learn_in_system=Y AND status='approved'`:

| category | documented outflow | undocumented outflow | confidence_pct |
|---|---|---|---|
| `calibration`        | source change to prompt files (calibration auditor of jury) | NEW: should also auto-extend AIE catalog (`AIE-025` family) | 82 |
| `portability`        | source change (portability auditor of jury) | NEW: should auto-extend AIE catalog | 82 |
| `memory`             | NONE — falls into source-change bucket but the natural outflow is `memory_schema/manifest.json` evolution (see F-2) | manifest.json#evolution_log update; per-module schema field add/flag-change | 88 |
| `prompt_architect`   | source change (rubric-violation fix) | AIE-028/029/030 family auto-extension | 80 |
| `HITL`               | source change to gate framing | could also become a memory-type=user entry if user-preference; ambiguous | 70 |
| `EU_AI_Act`          | source change to mapping doc + audit_sheet row | could also extend `audit/eu_ai_act_mapping.md#evolution_log` | 75 |
| `tooling`            | source change (fallback ladder) | AIE catalog extension | 80 |
| `documentation`      | source change to docs | already wired for `living_update` of context corpus (`prompts/13_context_curator.md:114`) | 85 |
| `other`              | flagged for taxonomy refresh in reflection (`templates/feedback_learning/session_close.md.tmpl:18`) | NO automatic proposal emitted (see F-7) | 78 |

**Recurrence × severity overlay** is well documented for **classification** (`prompts/11_feedback_learning_loop.md:114-116`) but **not for action**: a `(category=memory, recurrence=systemic, severity=critical)` row and a `(category=memory, recurrence=one_off, severity=info)` row both flow through the same threshold-counter pipeline. The jury's row-by-row consensus partially mitigates this, but the routing pre-jury is severity-blind. **Suggestion:** weight `pending_count` by severity (critical=4, error=2, warn=1, info=0.25) so the threshold fires faster on safety-relevant clusters. Confidence 78%.

## 5. The "agent reads memorised corrections" loop audit

This is the user's **anchor concern** and it is where the routing layer is **weakest**.

**Trace attempted:**

1. `templates/CLAUDE.md.tmpl:24-37` — "Mandatory reads at session start": the bullet list contains 9 items (SPEC, ARCHITECTURE, project.json, decisions.md, errors_catalog.json, MEMORY.md, library_docs MANIFEST, eu_ai_act_mapping, current session.json). **`feedback_learning/corrections.md` and `corrections.db` are absent.** Confidence 95%.
2. `prompts/13_context_curator.md:114` — partial mitigation: in `living_update` mode at session start the context curator reviews "recent corrections (`feedback_learning/corrections.db`) for `category=documentation` and propose adds." But this is **scoped to one category** (documentation), and only reviews the *context corpus*, not behaviour. Confidence 92%.
3. `prompts/14_adaptive_audit_meta.md:34-44` — adaptive auditor is invoked at task/session **end**, not start; it queues new improvements to corrections.db but does not surface prior approved corrections to the running agent. Confidence 90%.
4. `prompts/11_feedback_learning_loop.md` — only runs at session **close** (phase 13.5). Confidence 99%.

**Conclusion (F-1):** the `corrections.db` is *written* fastidiously and *audited* by the jury, but no documented child-orchestrator wiring causes the agent to *read* approved/incorporated corrections at session start. The natural fix is a one-line addition to `templates/CLAUDE.md.tmpl`'s mandatory-reads list pointing at `corrections.md` filtered to `status IN ('approved','incorporated') AND learn_in_system=1`, plus a "surface top-3 oldest unincorporated `recurring/systemic` rows" pre-action guard.

**Note on overlap with auditor B:** auditor B owns the *capture* UX. This finding is in *my lane* (post-capture routing into the agent's working context). Confidence the lane separation holds: 88%.

## 6. Memory crystallisation pathway audit

**Trace attempted:** approved correction with `category=memory` → ?

- `prompts/11_feedback_learning_loop.md:30-42`: writes to `corrections.db`, drafts `improvement_proposal.md`, signals 13.7. No mention of `memory_schema/manifest.json`.
- `prompts/12_improvement_jury.md:215-220`: on approval sets `status='approved'`. The jury's `memory_integrity` axis (`prompts/12_improvement_jury.md:106`) audits *that* `memory/MEMORY.md` is not polluted, but **does not write** new memory modules.
- `prompts/15_memory_schema_architect.md:209-212` (the protocol): documents schema evolution as `re-negotiation → migration → versioning` but does not specify *who* triggers re-negotiation in living_update mode after an approved memory-correction.
- `references/memory_schema_protocol.md:225-228`: states "Adding a new starter, changing a default threshold... requires a row in `feedback_learning/corrections.db` (`category=memory` or `tooling`); approval at phase 13.7; a changelog entry" — but this describes a protocol for the **meta-skill maintainer**, not an automated wiring inside a running child system.

**Conclusion (F-2):** the path "approved memory-correction → manifest.json update" is **declared as user obligation, not as system wiring**. There is a clean place to add it: phase 13.7's post-approval branch could conditionally signal phase 4.5 in `living_update` mode with the approved correction as input. The `manifest.json` template even has a placeholder `evolution_log` field (`templates/memory_schema/manifest.json.tmpl:11-13`) that is never written-to anywhere in the prompt set — confirming this is unfinished wiring rather than a deliberate omission. Confidence 88%.

## 7. AIE catalog auto-extension audit

**Trace attempted:** approved correction with `category in {tooling, calibration, prompt_architect}` → new AIE entry?

- `references/ai_error_catalog.md:264-274` ("Auto-extension protocol"): describes **5 steps**, all of which fire **inside a running session that catches a NEW error pattern**. The trigger is `session error-handler emits draft entry to tracking/sessions/<id>/errors.jsonl` — i.e., a **runtime exception detector**, not the feedback loop.
- `prompts/05_error_prevention_seeder.md:14-20`: only runs at scaffold time (phase 8); does not consume corrections.db.
- `prompts/00_master_orchestrator.md:126`: "Self-extending: each new error caught in a session is appended" — phrased as runtime catch, not human feedback.
- `prompts/12_improvement_jury.md:102` (regression auditor): only **reads** `errors_catalog.json` to verify no regressions; does not extend.

**Conclusion (F-4):** the auto-extension protocol predates the feedback layer (the catalog was AIE-1 through AIE-30 at v0.1.0; phase 13.5 is v0.2.0; phase 13.7 is v0.2.0). The two systems were **never bridged**. A correction like "the prompt-architect rubric let through a Complex prompt missing `<hitl_conditions>`" (category=prompt_architect, severity=error) intuitively *should* spawn `AIE-031 · hitl-conditions-missing` if it is approved at the jury, but no documented wiring does this. Confidence 85%.

## 8. Recommended improvements (if any)

| # | improvement | priority | estimated effort (hours) | confidence_pct | rationale |
|---|---|---|---|---|---|
| 1 | Add `corrections.md` (filtered to approved/incorporated) to child orchestrator's session-start mandatory reads | P0 | 1-2 | 92 | Resolves F-1; directly addresses user's anchor concern. Single-file edit to `templates/CLAUDE.md.tmpl`. |
| 2 | Wire `category=memory & status=approved` → phase 4.5 `living_update` invocation with manifest.json#evolution_log writes | P1 | 6-10 | 85 | Resolves F-2; the manifest template already has the slot. Requires a new step in phase 13.7's post-approval branch and a new `<input>.from_correction_id` parameter for prompt 15. |
| 3 | Wire pre-action recurrence guard: when adaptive auditor receives a scope envelope, run an FTS5 query against approved/recurring/systemic corrections; surface as `prior_lessons[]` field in the envelope | P1 | 4-6 | 80 | Resolves F-3; turns the FTS5 substrate from a write-time classifier into a read-time guard. |
| 4 | Wire `category in {tooling,calibration,prompt_architect} & status=approved` → AIE catalog draft append | P1 | 3-5 | 82 | Resolves F-4; closes the loop between human-in-the-loop feedback and the runtime error detector. |
| 5 | Add `incorporation_kind` discriminator column to corrections schema | P2 | 1-2 | 80 | Resolves F-5; makes the lifecycle queryable for cross-system analytics. NULLable, backward-compatible. |
| 6 | Decide and document cross-child portability stance (silo vs. opt-in inheritance) | P2 | 2-4 | 75 | Resolves F-6; either decision is defensible — the gap is the *un*-decision. |
| 7 | Severity-weighted threshold counter (critical=4, error=2, warn=1, info=0.25) | P3 | 2-3 | 70 | Improves matrix coverage of section 4; faster trigger on safety clusters. Optional / configurable. |
| 8 | Auto-emit taxonomy-refresh proposal when `OTHER_COUNT > 3` at session close | P3 | 1-2 | 75 | Resolves F-7; small self-healing loop. |

**Note:** all 8 are additive, none require breaking changes to v1.0.0 outputs already in the wild. P0+P1 are ~14-23 hours; P2+P3 are ~6-11 hours. Total ≈ 20-34 hours, ±20%.

## 9. Reflection (≤200 words)

The feedback layer's **substrate** (SQLite + FTS5 + dual mirror + status-based lifecycle + 5-axis jury) is genuinely production-grade — the kind of FRACAS implementation I would expect at ISO/IEC 42001 §10.2 maturity. What it lacks is **the consumption side of the routing graph**. The system is fastidious about *capturing* corrections (Auditor B's lane) and rigorous about *gating* source changes (Auditor C's lane), but the in-between — "an approved correction is now a known lesson; how does that lesson reach the running agent's context next time, become a structured memory module, or extend the AIE catalog?" — is mostly unspecified. The five wiring gaps (F-1 through F-5) are individually small and collectively decisive: they are the difference between a feedback layer that *records* and one that *learns*. The good news is that the architecture made room for these wirings (the `evolution_log` placeholder, the `corrections_fts` virtual table, the `incorporated` status value) — they are *placeholders in waiting*, not redesigns. P0+P1 patches close the user's anchor concern. The system is **not broken; it is half-routed**. Confidence in this synthesis: 84%.
