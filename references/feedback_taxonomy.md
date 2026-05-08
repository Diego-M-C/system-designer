# Feedback Taxonomy · Reference for Phase 13.5

> Authoritative classification taxonomy for human feedback collected at phase 13.5 (`prompts/11_feedback_learning_loop.md`). Each correction is classified under three orthogonal axes: **severity** × **category** × **recurrence**. Plus a calibrated confidence% on the classification itself.
>
> Generator version: `0.2.0` · Last reviewed: `{{TEMPORAL_NOW}}`

## Why a taxonomy

Free-text feedback is high-fidelity but low-utility for batched improvement reasoning. The taxonomy lets `feedback_learning/corrections.db` index, search, and aggregate signals across sessions. It is also the input shape phase 13.7 (`improvement_jury`) audits.

## Severity (4 levels)

| code | meaning | typical action |
|---|---|---|
| `info` | Observation. Logged for context; no urgency. | record only; no proposal weight. |
| `warn` | Minor issue. Should improve in next 1–3 sessions. | promote at threshold. |
| `error` | Incorrect output or behaviour. Address in current improvement cycle. | promote eagerly; counts strongly toward threshold. |
| `critical` | Safety, compliance, or correctness failure. | block subsequent sessions until resolved; consider out-of-band patch. |

## Category (9 buckets)

| code | meaning | examples |
|---|---|---|
| `calibration`        | uncalibrated assertion / P2 violation | "the system claims X is best", missing % on a KPI target. |
| `portability`        | platform-specific leakage / P1 violation | `mcp__` reference outside tests, hardcoded Claude Code call. |
| `memory`             | wrong/missing memory capture or noisy pollution | a fix-recipe was memorised; a user role wasn't. |
| `prompt_architect`   | composition rubric miss | mandatory floor incomplete, tags out of canonical order. |
| `HITL`               | gate framing / dissent surfacing / consent capture | gate auto-skipped, alternatives lacked confidence%. |
| `EU_AI_Act`          | mapping gap / weak evidence / mis-classified risk | Article 14 row had no evidence_link. |
| `tooling`            | abstraction / fallback ladder gap | a soft dependency had no fallback. |
| `documentation`      | outdated / missing / contradictory docs | README claimed v0.1 features after v0.2 ship. |
| `other`              | does not fit; flag for taxonomy refresh | rare; signals taxonomy needs an update. |

## Recurrence (3 tiers)

| code | meaning | how detected |
|---|---|---|
| `one_off`   | first observation | FTS5 search of `corrections_fts` returns 0 prior similar hits. |
| `recurring` | observed ≥2 sessions | FTS5 returns ≥2 hits across distinct session_ids. |
| `systemic`  | observed ≥4 sessions OR linked to ≥2 categories | FTS5 ≥4 OR cross-category cluster. |

## Confidence% on classification

Mandatory (P2). The auto-classifier surfaces `< 70%` to HITL for human override. Anchors:

- `90–99` — the feedback explicitly names the category (e.g., "calibration violation here") AND severity is unambiguous.
- `70–89` — strong textual cues; low ambiguity.
- `50–69` — heuristic; show alternatives at HITL.
- `< 50` — refuse auto-class; ask the user to pick.

## Learn decision (per correction, by human)

| code | numeric | meaning |
|---|---:|---|
| `Y`    | 1 | promote to improvement queue; eligible for batched proposal at threshold. |
| `N`    | 0 | record for traceability only; never feeds memory or proposal. |
| `SKIP` | 2 | defer; row stays `pending_review`; counts toward threshold only after a future Y. |

The system NEVER defaults this field. Every value reflects an explicit human keystroke at phase 13.5.

## Threshold

```
trigger = (count(rows WHERE learn_in_system = 1 AND status = 'pending_review') >= learn_threshold)
       OR (user_explicit_trigger == True)
```

Default `learn_threshold = 15`. Configurable in `SystemSpec.feedback.learn_threshold` ∈ [5, 50] via the wizard.

## Status lifecycle

```
pending_review ──(jury approve)──► approved ──(merge cycle)──► incorporated
              ╰─(jury reject)───► rejected
```

Rows never delete; lifecycle is via `status`.

## When category=`other` shows up

Treat as a signal that the taxonomy itself needs a refresh. The session-close reflection (template `feedback_learning/session_close.md.tmpl`) flags `other` count > 3 as a recommendation to extend this document.

## Changelog

- `0.2.0` — initial taxonomy (4 severity × 9 categories × 3 recurrence; 3 learn-decision values; threshold default 15).
