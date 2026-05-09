---
auditor_id: B
persona_slug: hitl_capture_human_comms_specialist
session_id: feedback-layer-audit-v100-2026-05-09
ran_at: 2026-05-09T09:35:28Z
overall_verdict: APPROVED_WITH_MINOR
overall_confidence_pct: 84
findings_count: 6
self_kpis:
  files_read: 11
  evidence_citation_rate_pct: 100
  mean_finding_confidence_pct: 84
---

# HITL Capture & Human Communication Specialist · Feedback-Layer External Audit · v1.0.0

## 1. Executive verdict (≤120 words)

The HITL capture surface for phase 13.5 is **mature in design intent**, ~84% confident in fitness-for-purpose. The per-correction block in `prompts/11_feedback_learning_loop.md:340-355` informs the human (severity / category / recurrence / confidence% / proposed action) BEFORE asking Y/N/SKIP, with explicit consequence text per choice — this is the strongest part of the surface. The never-default invariant is anchored at ≥4 prose layers + 1 SQL CHECK. Three minor findings reduce confidence: (a) the dashboard's v0.3.x KPI cards declare a `path` attribute that the renderer ignores (line 279 reads `kpis[m.key]`, never `m.path`), so the four feedback/adaptive surfaces silently render "—"; (b) the dashboard heading claims "KPIs (11)" while KPI_META holds 21 entries; (c) no deterministic test catches a silent learn-default regression.

## 2. Strengths observed (≥3, each anchored to file:line)

- **Per-correction preview format INFORMS before asking** — `prompts/11_feedback_learning_loop.md:342-354` shows severity / category / recurrence / classification confidence% AND a proposed-action draft with its own confidence%, then surfaces Y/N/SKIP with one-line consequence text per choice. ISO 9241-110 self-descriptiveness + suitability for the task are both satisfied. Confidence ~95%.
- **Never-default invariant anchored at multiple layers** — prose constraint at `prompts/11_feedback_learning_loop.md:197` (`<constraints>` #2: "NEVER auto-default `learn_in_system`"), `:208` (`<non_do_conditions>`: "Do NOT silently mark a row `learn_in_system=Y`"), `:421` (`<guardrails>`: "Never default `learn_in_system`; always block on human keystroke"), `:438` (`<alignment_rules>` #2: "no implicit defaults"), `:56` (`<success_criteria>`: "no implicit defaults; SKIP is allowed and recorded"), plus `references/feedback_taxonomy.md:59` ("The system NEVER defaults this field. Every value reflects an explicit human keystroke") and SQL CHECK at `templates/feedback_learning/corrections_schema.sql.tmpl:22`. Six prose layers + 1 SQL anchor. Confidence ~95%.
- **Threshold rule is deterministic and observable** — `prompts/11_feedback_learning_loop.md:124-132` declares `count(rows WHERE learn_in_system='Y' AND status='pending_review') >= learn_threshold OR user_explicit_trigger`, and `templates/feedback_learning/pending_review.md.tmpl:14-17` exposes `BELOW / AT_THRESHOLD / ABOVE` to the human in the regenerable view. The user knows whether the next Y will fire. Confidence ~92%.
- **Session-close summary is daily-digest-grade** — `templates/feedback_learning/session_close.md.tmpl:5-19` surfaces collected-this-session count, severity / category / learn-decision distributions, pending total, threshold + status, oldest-pending-days, lowest-confidence classification, and an actionable recommendation. <60-second consumability target met. Confidence ~90%.
- **Critical-severity halt is wired through, not just documented** — `prompts/11_feedback_learning_loop.md:394` (`<hitl_conditions>` #4) confirms "Severity = critical → confirm whether to halt subsequent sessions" and the master orchestrator's `prompts/00_master_orchestrator.md:411` shows Art.73-incident BLOCKER linkage halting subsequent sessions until `regulatory_report_id` is logged. The wiring is real, not decorative. Confidence ~80%.

## 3. Findings (errors AND improvement candidates)

| finding_id | type | severity | invariant | evidence_path:line | confidence_pct | suggested_action |
|---|---|---|---|---|---:|---|
| B-F1 | error | warn | KPI cards must render the surface they declare | `dashboard/index.html:236-241` (paths declared) vs `:278-285` (renderer reads only `kpis[m.key]`) | 92 | Implement `getNested(data, m.path)` fallback when `kpis[m.key]` is undefined; v0.3.x feedback / adaptive_audit / Art.73 / data-flow tiles will then render |
| B-F2 | error | info | UI labels match the data they expose | `dashboard/index.html:337` ("KPIs (11)") vs `:219-242` (21 entries in KPI_META) | 95 | Change heading to `KPIs (${KPI_META.length})` or "KPIs" without count |
| B-F3 | improvement | warn | Test coverage anchors the never-default invariant | `tests/run_all.sh` (no T-id covers silent learn-default); `tests/README.md:38-46` (T2 calibration only, T10 gate-skip only) | 88 | Add T24 — grep `prompts/11_feedback_learning_loop.md` for `default.*learn_in_system` without a negation/refusal context; fail if found |
| B-F4 | improvement | warn | Calibrated alternatives at confidence <70% | `prompts/11_feedback_learning_loop.md:368` ("<50%: REFUSE auto-class; ask the user to pick") + `:395` ("Confidence <70% on classification — show alternatives; never auto-pick") — but no `<format>` block specifies HOW alternatives are rendered | 75 | Add a 2nd `<format>` block "alternatives presentation" with `[A] cat=X — fit ≈Y% / [B] cat=Z — fit ≈W%` shape, mirroring master orchestrator's gate format at `prompts/00_master_orchestrator.md:344-364` |
| B-F5 | improvement | info | Batch ergonomics for many corrections | `prompts/11_feedback_learning_loop.md:336` ("Type one item per line. End with `DONE`") — does not specify whether the per-correction HITL fires once per line OR after the user finishes batch entry | 70 | Clarify in `<format>`: per-correction HITL fires AFTER each line is parsed, not after `DONE`; or explicitly support `DONE` as deferred-batch with per-row HITL after |
| B-F6 | improvement | info | Pending-review must surface `TRIGGER_NOTICE` semantics | `templates/feedback_learning/pending_review.md.tmpl:8` ({{TRIGGER_NOTICE}} placeholder) — no documentation of what TRIGGER_NOTICE renders at `BELOW` / `AT_THRESHOLD` / `ABOVE` | 70 | Add per-status example renderings as a comment block in the template, or move the legend to top so the user reads it first |

## 4. Per-correction HITL block fidelity audit

The per-correction prompt at `prompts/11_feedback_learning_loop.md:340-355` is well-architected:

```
=== CORRECTION #<n> ===
Feedback: <≤160 chars>
Auto-classified: severity=<s> · category=<c> · recurrence=<r> · confidence ≈<X>%
Proposed action draft: <≤120 chars> (confidence ≈<Y>%)

Should the system LEARN from this correction?  [Y / N / SKIP]
- Y    : promote to improvement queue
- N    : record for traceability only; never feeds memory or proposal
- SKIP : defer; revisit next session
```

Walk-through of the ISO 9241-110 dialogue principles:
- **Self-descriptiveness** (~95%): every line explains itself; consequence text is per-choice.
- **Suitability for the task** (~90%): the 4 informational rows precede the question, not after.
- **Conformity with user expectations** (~85%): Y/N/SKIP is conventional; "SKIP" is explicitly recorded as defer (not "ignore").
- **Error tolerance** (~80%): the prompt does not show what happens on a typo (e.g., user types "y " or "yes"). Could be tightened.
- **Controllability** (~85%): the user can also `STOP` mid-loop (`prompts/11_feedback_learning_loop.md:386`).

**Verdict:** the human is INFORMED before deciding. No "asked but not informed" failure mode in this block. Confidence ~92%.

The single residual concern (B-F4) is the calibration of the classifier itself when `<70%`: the prompt says "show alternatives" but does not specify the alternative-presentation `<format>` shape. The master orchestrator's gate format (`prompts/00_master_orchestrator.md:344-364`, `[A] fit ≈X% / [B] fit ≈Y% ...`) is the established Anthropic-aligned pattern; the feedback loop should mirror it for consistency.

## 5. Never-defaulted invariant — multi-layer enforcement count

| Layer | Anchor | path:line | strength |
|---|---|---|---|
| 1. Prose `<constraints>` | "NEVER auto-default `learn_in_system`; always block on human Y/N/SKIP." | `prompts/11_feedback_learning_loop.md:197` | strong |
| 2. Prose `<non_do_conditions>` | "Do NOT silently mark a row `learn_in_system=Y` — every Y is an explicit human keystroke." | `prompts/11_feedback_learning_loop.md:208` | strong |
| 3. Prose `<guardrails>` | "Never default `learn_in_system`; always block on human keystroke." | `prompts/11_feedback_learning_loop.md:421` | strong |
| 4. Prose `<alignment_rules>` #2 | "P3 for memorisation: nothing is memorised without explicit Y." | `prompts/11_feedback_learning_loop.md:438` | strong |
| 5. Prose `<success_criteria>` | "no implicit defaults; SKIP is allowed and recorded" | `prompts/11_feedback_learning_loop.md:56` | strong |
| 6. Reference `<priority>` #2 | "Human consent on every learn decision (no silent memorisation — protects against noise pollution and adversarial drift)." | `prompts/11_feedback_learning_loop.md:72` | strong |
| 7. Per-correction `<hitl_conditions>` #1 | "Per-correction learn decision (every correction) — Y/N/SKIP. ALWAYS." | `prompts/11_feedback_learning_loop.md:391` | strong |
| 8. Taxonomy reference | "The system NEVER defaults this field. Every value reflects an explicit human keystroke at phase 13.5." | `references/feedback_taxonomy.md:59` | strong |
| 9. SQL CHECK | `learn_in_system INTEGER NOT NULL CHECK(learn_in_system IN (0,1,2))` | `templates/feedback_learning/corrections_schema.sql.tmpl:22` | weak (catches NULL-write but accepts "0=N" as a silent-default) |
| 10. Test coverage | none direct; T2 calibration + T10 gate-skip do NOT close this loop | `tests/run_all.sh` | **MISSING** (B-F3) |

**Score:** 9 prose+SQL layers; 0 test layers. Anchor depth at the prompt level is **strong** (6 prose-layer anchors comfortably exceed the ≥4-layer threshold). The gap is at the test layer — there is no executable assertion that catches a silent-default regression. Confidence ~88% that the invariant is honoured at runtime; ~88% that a test covering the regression would close the gap. See B-F3.

## 6. Threshold semantics audit (edge values 5, 50, TRIGGER)

Threshold rule at `prompts/11_feedback_learning_loop.md:124-132` and `references/feedback_taxonomy.md:62-68`:

```
trigger = (count(rows WHERE learn_in_system = 1 AND status = 'pending_review') >= learn_threshold)
       OR (user_explicit_trigger == True)
```

Edge-value walk:
- **`learn_threshold = 5`** (lower bound, range `[5, 50]`): the 5th `learn_in_system=1 AND status='pending_review'` row trips the trigger on the next counter recompute (`prompts/11_feedback_learning_loop.md:219`). Behaviour deterministic; confidence ~92%.
- **`learn_threshold = 50`** (upper bound): rows accumulate without firing until count = 50. The pending-review view at `templates/feedback_learning/pending_review.md.tmpl:14-17` correctly distinguishes `BELOW` / `AT_THRESHOLD` / `ABOVE`. Confidence ~90%.
- **TRIGGER below threshold** (test case T4 at `prompts/11_feedback_learning_loop.md:481`): "user types `TRIGGER` at count=7 → proposal emitted with the 7 rows; counter does not reset". Override semantics correct. Confidence ~92%.
- **What counts toward the counter** — only `learn_in_system=1 AND status='pending_review'`. SKIP rows (learn_in_system=2) and N rows (learn_in_system=0) do NOT count. `pending_review` rows that have already been promoted to `approved` (jury-approved but not yet merged) are NOT counted toward the firing trigger — confirmed by SQL view `v_pending_improvements` at `templates/feedback_learning/corrections_schema.sql.tmpl:62-69` filtering `status = 'pending_review'`. This is correct: an approved-but-not-yet-merged row should not re-trigger the proposal pipeline. Confidence ~85%.

**Verdict:** threshold semantics are deterministic and the edge cases match the documented test cases. No finding. Confidence ~90%.

## 7. Dashboard + pending_review.md surface audit

### 7.1 Dashboard tile rendering — **B-F1 + B-F2**

`dashboard/index.html:219-242` declares 21 KPI_META entries. Entries 13-21 (the v0.3.x surfaces) carry a `path` attribute (e.g., `path: "feedback_learning.pending_count"` at `:236`). The renderer at `:278-285`:

```js
const kpis = data.kpis_running || {};
const kpiHtml = KPI_META.map(m => {
  const v = kpis[m.key];   // <-- only reads from kpis_running by m.key
  return `<div class="kpi ${m.color || ""}">
    <div class="label">${m.label}</div>
    <div class="value">${fmtKpi(v)}</div>
    ...`;
}).join("");
```

The `m.path` declaration is **defined but never read**. Practical consequence: when `tracking/project.json` carries `feedback_learning.pending_count` at the top level (as the prompt's `<state>` block at `prompts/11_feedback_learning_loop.md:295-307` documents), the renderer looks for `data.kpis_running.feedback_pending_count` (using `m.key`), finds undefined, and `fmtKpi(undefined)` returns `"—"`. The four feedback / adaptive_audit / Art.73 tiles that the v0.3.2 changelog claims to expose (`prompts/00_master_orchestrator.md:6`) will silently render as empty cards.

This is a **rendering-vs-spec contract violation**, not a security issue, but it directly hurts the audit trail the user paid for. **B-F1, severity=warn, confidence=92%.**

Adjacent: `dashboard/index.html:337` says `<h2>KPIs (11)</h2>` — but KPI_META has 21 entries. **B-F2, severity=info, confidence=95%.**

### 7.2 `pending_review.md` rendering — APPROVED

`templates/feedback_learning/pending_review.md.tmpl` is well-formed:
- Filter is correct (`learn_in_system = 1 AND status = 'pending_review'`, `:3`).
- Single git-diffable view ✓ (regenerable from DB on every run, per `prompts/11_feedback_learning_loop.md:218`).
- Threshold status surfaced ✓ (`{{THRESHOLD_STATUS}}` at `:6`; legend at `:14-17` with `BELOW / AT_THRESHOLD / ABOVE`).
- Sort order is documented (oldest → newest, `:3`).

One micro-nit (B-F6): `{{TRIGGER_NOTICE}}` at `:8` is unspecified — no example for what it renders at each status. Not blocking. Confidence ~88% that the template is fit-for-purpose.

## 8. Recommended improvements (if any)

| # | improvement | priority | effort_h | confidence_pct | rationale |
|---|---|---|---:|---:|---|
| 1 | Implement `getNested(data, m.path)` fallback in `dashboard/index.html` so v0.3.x tiles render the surfaces they declare | high | 1 | 92 | B-F1; the four feedback / adaptive_audit / Art.73 tiles silently render "—" today |
| 2 | Fix dashboard heading from "KPIs (11)" to dynamic `KPIs (${KPI_META.length})` | low | 0.2 | 95 | B-F2; misleading label |
| 3 | Add T24 deterministic test: grep that no instruction in `prompts/11_feedback_learning_loop.md` defaults `learn_in_system` outside negation context | medium | 1.5 | 88 | B-F3; closes the only missing layer of the never-default invariant |
| 4 | Add a 2nd `<format>` block in `prompts/11_feedback_learning_loop.md` for the `<70%` alternatives presentation, mirroring master-orchestrator's `[A] fit≈X%` pattern | medium | 1 | 75 | B-F4; the prompt-architect alternative-presentation pattern should be applied uniformly |
| 5 | Clarify in the feedback solicitation `<format>` block whether per-correction HITL fires per line or after `DONE` | low | 0.3 | 70 | B-F5; ergonomic ambiguity for batch entry |
| 6 | Document `{{TRIGGER_NOTICE}}` example renderings inside `pending_review.md.tmpl` | low | 0.3 | 70 | B-F6; template self-descriptiveness |

Total estimated effort: ~4.3h. None of these block APPROVED_WITH_MINOR.

## 9. Reflection (≤200 words)

The HITL capture surface is the single most-anchored part of the feedback layer — six independent prose layers + a SQL CHECK + a per-correction `<hitl_conditions>` block + a taxonomy reference all converge on "no silent learn-Y". This is rare in HITL systems and reflects mature design intent. The per-correction prompt INFORMS the human (severity / category / recurrence / classification confidence% / proposed action with its own confidence% / consequence text per choice) before asking — ISO 9241-110-aligned.

The two real defects sit elsewhere: the dashboard renderer's `m.path` is declared but never resolved (so the tiles meant to expose this surface render empty), and there is no executable test that would catch a silent-default regression. Both are tractable in <2h each. The remaining four improvement candidates are micro-ergonomics: alternative-presentation format consistency, batch-entry semantics, template self-descriptiveness.

I am ~84% confident that v1.0.0 is mature enough to ship in APPROVED_WITH_MINOR status. The dashboard fix (B-F1) is the only one I would prioritise before the next major release; the others can ride a regular maintenance cycle.
