# 11 · Feedback Learning Loop

> **File.** `prompts/11_feedback_learning_loop.md`
> **Tier.** Complex (~42 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.2.0

## 1. Purpose

Captures human feedback at session close, classifies it under a calibrated taxonomy, persists to a hybrid SQLite + Markdown store, and asks the human **per-correction** whether the system should learn from it. Triggers a batched improvement proposal at threshold (default 15) or an explicit user `TRIGGER` keyword. **Nothing is memorised without an explicit human Y.**

## 2. When invoked

- **Phase 13.5** — strictly after `handoff` (phase 13).
- Inherited by the child orchestrator: re-runs at the close of every session.
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true`.

## 3. Inputs

- `<target_path>/tracking/project.json` — session state, `feedback.learn_threshold`, `pending_count`.
- `<target_path>/audit/audits/jury_session_<id>.md` — disambiguates classification.
- `<target_path>/data_flow_validation/structural_consistency/consolidated_report.md`.
- `<target_path>/feedback_learning/corrections.db` (existing or new).
- `references/feedback_taxonomy.md` — calibrated taxonomy.

## 4. Outputs (under `<target_path>/feedback_learning/`)

- `corrections.db` — SQLite + FTS5; authoritative source of truth.
- `corrections.md` — auto-regenerated mirror from DB (single render at run end).
- `classifications.json` — taxonomy snapshot at session close.
- `pending_review.md` — filter view of `learn_in_system=Y AND status=pending_review`.
- `improvement_proposal.md` — only when threshold or explicit trigger.
- `session_close_<session_id>.md` — reflection.

## 5. Persistence model

Dual: **SQLite is authoritative; MD is regenerable**. After every row insert:

1. Begin transaction.
2. `INSERT INTO corrections (...)` (parameterised; SQL-injection safe).
3. FTS5 sync triggers fire automatically.
4. Re-render `corrections.md` from DB.
5. Commit. Atomic write of MD via `*.tmp` + rename.

If MD write fails after DB commit: log `AIE-FBL-MIRROR-DRIFT`; on next run, mirror is rebuilt from DB.

## 6. Classification taxonomy (3 axes)

- **Severity** ∈ {`info`, `warn`, `error`, `critical`}
- **Category** ∈ 9 buckets (`calibration`, `portability`, `memory`, `prompt_architect`, `HITL`, `EU_AI_Act`, `tooling`, `documentation`, `other`)
- **Recurrence** ∈ {`one_off`, `recurring` (FTS5 hits ≥2), `systemic` (≥4 OR ≥2 categories)}
- **Confidence%** on the classification itself (P2; <70% surfaces alternatives at HITL).

## 7. Per-correction HITL (mandatory)

```
=== CORRECTION #n ===
Auto-classified: severity=<s> · category=<c> · recurrence=<r> · confidence ≈X%
Should the system LEARN from this?  [Y / N / SKIP]
=== /CORRECTION ===
```

`Y` (1) → improvement queue. `N` (0) → record only. `SKIP` (2) → defer to next session. **Never defaulted.**

## 8. Threshold rule

```
trigger = (count(rows WHERE learn_in_system=1 AND status='pending_review') >= learn_threshold)
       OR (user_explicit_trigger == True)
```

Default `learn_threshold = 15` (configurable via wizard Q34, range 5–50). On trigger: emit `improvement_proposal.md`, signal phase 13.7. **Never patches source from this phase.**

## 9. Calibration & portability anchors

- Every classification + every proposed action carries a confidence%.
- SQLite is Python stdlib + universal CLI; FTS5 is in default builds since 3.9; MD-only mode is the documented fallback.

## 10. HITL escalation triggers (beyond per-correction)

- Improvement proposal triggered → confirm "send to phase 13.7? Y/N".
- `category=other` selected → confirm classification (potential taxonomy gap).
- Severity `critical` entered → ask whether to halt subsequent sessions.
- Auto-classifier confidence <70% on classification → show alternatives.
- FTS5 detects exact-match prior session feedback → confirm dedupe vs. independent record.

## 11. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` at phase 13.5 and by the child orchestrator at session close.
- ↓ delegates classification helpers to `prompts/03_prompt_factory.md`.
- → reads `references/feedback_taxonomy.md` and `templates/feedback_learning/*.tmpl`.
- ← signals `prompts/12_improvement_jury.md` (phase 13.7) when threshold fires.

## 12. Test coverage

- T11 / T13 / T16 confirm prompt, schema parseable, templates exist.
- 8 in-prompt `<test_cases>`: empty session / single info / 15th learn-Y / explicit TRIGGER below threshold / DB unavailable / FTS5 dedupe / `category=other` / critical severity.

## 13. Common failure modes

- **DB locked** — concurrent write attempt; retry with backoff up to 3 times; if still locked → escalate.
- **Mirror drift** — MD write fails after DB commit; rebuilt on next run; logged but not data-losing.
- **Schema migration needed** — older DB file detected; emits a sidecar migration template; never auto-migrates destructively.
- **Critical severity entered late** — child orchestrator may need to pause future sessions; user decision logged in `decisions.md`.
