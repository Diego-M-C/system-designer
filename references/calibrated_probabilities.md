# Calibrated Probabilities — Operational Rules (Principle P2)

> **Why:** an uncalibrated assertion in a high-stakes system is indistinguishable from a confident lie. Calibration converts the system's outputs from "trust me" to "here is the evidence and the residual uncertainty".
>
> **Scope:** every output of `system-designer` and every artifact emitted into a child system. No exceptions.

---

## 1 · Forbidden tokens (in emitted prose)

The following tokens are forbidden in any prose, decision, alternative, KPI target, library version recommendation, or summary emitted by the generator or by any prompt it composes:

| Token | Why forbidden | Replacement pattern |
|---|---|---|
| `best`, `the best` | implies absolute ordering without evidence | "highest fit ≈X% relative to alternatives Y, Z" |
| `always`, `never` | universal claims rarely defensible | "in observed cases (N=…), X% of the time" or "in our reference set, …" |
| `guaranteed` | absolute claim | "high confidence (≈X%) under assumptions A, B" |
| `certain`, `definitely` | overconfidence | "≈X% confidence, conditioned on …" |
| `impossible` | unprovable | "very low likelihood (<5%), conditioned on …" |
| bare numerics ("X% accuracy", "5 days", "3 errors") | missing uncertainty band | "X% (95% CI a–b)" / "5 days ± 1" / "3 errors (range 1–5)" |

A regex scan runs in the self-audit phase: `\b(best|always|never|guaranteed|certain|definitely|impossible)\b`. Hits → escalation.

## 2 · Required formats per output type

| Output type | Required format | Example |
|---|---|---|
| **Strategic recommendation** | "Recommend X. Confidence ≈Y%. Reason: Z. Risk if wrong: W." | "Recommend Postgres 16. Confidence ≈85%. Reason: matches all `SystemSpec.stack` constraints + active LTS. Risk if wrong: migration cost ≈10–15h." |
| **Estimate (numeric)** | "≈X (range a–b, ±c%)" | "≈12 prompts (range 9–16, ±25%)" |
| **Probability (event)** | "≈X% likely" with anchor | "≈30% likely the user will downgrade EU AI Act risk to `limited`, anchor = past 5 invocations" |
| **Alternative at HITL gate** | "[Letter] label — fit ≈X% — pros/cons" | see `prompts/00_master_orchestrator.md#format` |
| **KPI target** | "target ≥X% with floor ≥Y%" | "target ≥95%, floor ≥85% over rolling 5 sessions" |
| **Library version rec** | "Recommend ver X.Y.Z (released D, ≈A% adoption among comparable projects, fallback Y.Y'.Z')" | "Recommend FastAPI 0.115.x (released 2024-10, ≈70% adoption fit, fallback 0.111.x)" |
| **Risk** | "Risk: description. Probability ≈X%. Impact: low/med/high. Mitigation: …" | see `<planning>` block of orchestrator |
| **Confidence in own answer** | "Self-confidence ≈X%. Backed by: [citation or 'pattern-match' or 'reasoned-only']" | inline at bottom of every gate brief |

## 3 · Confidence thresholds → behaviour

| Self-confidence range | Required action |
|---|---|
| **90–99%** | Auto-proceed allowed; MUST cite explicit reference (EU AI Act article, Anthropic doc, prompt-architect rule) |
| **70–89%** | Auto-proceed allowed; pattern-match acceptable in lieu of cite |
| **50–69%** | Pause — surface as alternative at next HITL gate; do NOT auto-pick |
| **<50%** | REFUSE to recommend; emit only as "consideration requiring human input"; mark with explicit `requires_human_decision: true` |

## 4 · Fit-% across alternatives — sum constraint

Fit % across alternatives at a HITL gate **need not sum to 100**. They are *fit estimates per option* (how well each option matches the user's stated constraints), not probabilities of mutually exclusive outcomes.

State this verbatim once per gate: *"Note: fit % across options are independent fit estimates, not probabilities of mutually exclusive outcomes. They may sum to >100% or <100%."*

Exception: if alternatives ARE mutually exclusive AND collectively exhaustive (rare), sum must be 100% ± 5%, and the gate brief states *"Mutually exclusive — % sum to 100"*.

## 5 · Anti-overconfidence patterns (heuristics)

When self-rating confidence, deduct points for:

- **No explicit citation** — cap at 89%.
- **First time encountering this domain** — cap at 70%.
- **User input partially ambiguous** — cap at 75%.
- **Knowledge cutoff older than `temporal_context` by >12 months** — cap at 70%.
- **Reasoning chain >5 steps** — cap at 80% (compounding uncertainty).
- **Contradicting reference docs** — cap at 60%, surface conflict.
- **Library version not pinned in `library_docs/MANIFEST.md`** — cap at 70% on any code recommendation referencing it.

## 6 · Calibration self-check protocol

Run after every output emission:

```
1. Scan output for forbidden tokens (regex).
2. For each numeric: verify uncertainty band present.
3. For each recommendation: verify confidence % present.
4. For each alternative: verify fit % + pros/cons present.
5. Cross-check: confidence rating vs evidence (citation or pattern-match).
6. If any check fails: refactor → re-emit. Do NOT pass to user.
```

Hits logged to `audit/self_audit.md#calibration_violations` with: timestamp, location (file + line), forbidden token / missing element, fix applied.

## 7 · Citation patterns (high-confidence outputs require evidence)

A confidence ≥90% MUST cite:

- **EU AI Act**: format `EU AI Act Art. <N>(<para>)` (e.g., `Art. 9(2)(c)`).
- **Anthropic doc**: format `Anthropic <doc-name> §<section>` (e.g., `Anthropic prompt-engineering / Be explicit`).
- **prompt-architect rule**: format `prompt-architect / <rule-name>` (e.g., `prompt-architect / Complex mandatory floor`).
- **Internal artifact**: format `<repo-path>:<line>` (e.g., `references/eu_ai_act_mapping.md:42`).
- **External research**: format `Author et al., Year, DOI/URL`.

No citation → confidence capped at 89%.

## 8 · Examples (correct / incorrect)

❌ **Bad:** *"Postgres is the best database for this system."*
✅ **Good:** *"Recommend Postgres 16 over alternatives (MongoDB, MySQL). Fit ≈85% — matches SDD's strict-typing requirement (cite: SPEC.md#schema), TimescaleDB extension fits the time-series KPI need (cite: SystemSpec.stack.libraries[2]). Confidence ≈85%, residual risk: vendor lock-in to PG-specific features (mitigation: abstract via SQLAlchemy)."*

❌ **Bad:** *"This will take 5 days."*
✅ **Good:** *"Estimated 5 days ± 1.5 days (range 3.5–7), assuming 1 dev full-time, no blocking dependencies. Confidence ≈75% based on past 3 comparable scaffolds."*

❌ **Bad:** *"Always validate user input."*
✅ **Good:** *"Validate user input at every system boundary (HTTP handlers, file ingest, user-message parsing). Internal-only code may skip if invariants hold. Cite: Anthropic prompt-engineering / data≠instructions."*

❌ **Bad:** *"3 alternatives presented."*
✅ **Good:** *"3 alternatives presented. [A] fit ≈70%, [B] fit ≈45%, [C] fit ≈30%. Sum >100 because non-mutually-exclusive. Recommend A, confidence ≈80%."*

## 9 · When to deliberately violate

Calibration is a default, not a law. Violate when:
- Quoting user input verbatim (preserve original).
- Reading a reference doc verbatim (annotate with the calibration when paraphrasing).
- Test fixtures that need exact strings.

Document each violation in `audit/self_audit.md#calibration_violations_intentional` with rationale. Un-documented violations become un-auditable drift.
