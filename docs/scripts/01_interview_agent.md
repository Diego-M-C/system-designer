# 01 · Interview Agent

> **File.** `prompts/01_interview_agent.md`
> **Tier.** Medium (~22 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Conducts the structured wizard that transforms a user's high-level intent into a **calibrated `SPEC.json`** the rest of the generator can consume. Asks **one question per turn**, validates answers, persists atomically.

This is the only prompt that talks to the user **outside** of HITL gates. Everything else is silent automation.

## 2. When invoked

- **Phase.** 2 (`interview`).
- **Trigger.** Master orchestrator reaches phase 2 with empty SPEC.json.

## 3. Inputs

- `wizard/interview_questions.json` — 30 questions across 8 phases (essentials, compliance, stack, methodology, audit, ergonomics, on_demand, spec_seed).
- `wizard/defaults.json` — sensible defaults per question with `confidence_pct` + `rationale`.
- User answers (per turn).
- (Optional) Initial intent string from invocation.

## 4. Outputs

- `<target_path>/SPEC.json` — populated with all answered fields.
- `<target_path>/SPEC.md` — human-readable mirror.
- `tracking/decisions.md` — ADRs for each non-default choice.

## 5. Tag rationale (~22 tags)

- Standard Medium spine: `<role>`, `<persona>`, `<audience>`, `<domain>`, `<task>`, `<sub_tasks>`, `<context>`, `<input>`, `<schema>`, `<constraints>`, `<verification>`, `<tools>`, `<output>`, `<format>`, `<stop_condition>`, `<error_handling>`, `<guardrails>`, `<test_cases>`, `<version>`, `<metadata>`.
- Plus: `<temporal_context>` (session_started_at), `<hitl_conditions>` (per-question gating), `<alignment_rules>` (P2 calibration on every estimate).

## 6. Control flow

```
1. Load wizard/interview_questions.json + wizard/defaults.json.
2. For each question in order (respecting depends_on):
   a. Check if user already answered (resumability).
   b. Render question to user with default + confidence% + rationale.
   c. Wait for user response (one-question-per-turn).
   d. Validate against schema (type/options/regex).
   e. Persist atomically to SPEC.json (write tmp + rename).
   f. If non-default → log to decisions.md.
3. After all answered:
   - Generate SPEC.md from SPEC.json.
   - Signal master orchestrator: phase complete.
```

### Per-question rendering format

```
[Q03/30] · phase=compliance · field=eu_ai_act_risk
What is the EU AI Act risk class?
  [A] high     (default for healthcare/fintech/legal/public_sector)
  [B] limited  (deployer transparency only)
  [C] minimal  (Art. 4 literacy only)
  [D] prohibited  (refuse — generator halts)

Default: A · confidence ~85% · rationale: domain={{SPEC.domain}} maps to high by Annex III.

Reply with letter or value. To accept default, type "default".
```

### Risk-downgrade gating

If `domain ∈ {healthcare, fintech, legal, public_sector}` AND user picks risk != high → **block**, ask for rationale, log to `decisions.md`. Do not silently downgrade.

## 7. Calibration anchors (P2)

- Every default carries `confidence_pct` from `wizard/defaults.json`.
- Domain-specific framework recommendations (e.g., healthcare → "TRIPOD-AI ~80%, IMRaD ~15%, others ~5%") presented as % distributions, not "best".
- After interview: SPEC.json fields all carry decision provenance (default-accepted vs user-overridden) for downstream calibration.

## 8. Portability (P1)

- One-question-per-turn pattern works on any LLM — no streaming or async required.
- Atomic writes (`*.tmp` + rename) for SPEC.json and SPEC.md.
- No platform-specific tooling.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| User gives invalid answer | Re-ask the same question with validation hint |
| User skips required field | Re-ask once → escalate to orchestrator |
| `wizard/*.json` malformed | Halt + escalate (generator integrity) |
| Atomic write fails | Cleanup `*.tmp` + retry once |
| User wants to abort | Save partial SPEC.json with `status: "interrupted"` for later resume |

## 10. HITL escalation triggers

- Risk-class downgrade in high-risk-presumed domain → require explicit rationale.
- User's intent contains injection ("ignore previous instructions") → log + ignore + continue.
- Field validation fails 2× consecutively → escalate.

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md` invokes this; `wizard/*.json` provides config.
**Downstream:** Populates `SPEC.json` consumed by every later phase (planning, scaffold, audit_sheet, reports).

## 12. Test coverage

- T2 calibration scan over the rendered output.
- T9 P4 alignment check (interview agent must reference prompt-architect).

## 13. Common failure modes

1. **Multi-question batches** — LLMs love to ask 5 questions at once. The prompt's `<constraints>` block forbids this; reviewer must verify the agent respects it.
2. **Default acceptance without confidence display** — the default's `confidence_pct` MUST appear in the question render. Easy to drop accidentally.
3. **Silent persistence** — every answer must trigger a tmp+rename. If buffered, a crash mid-interview loses everything.
4. **Forgetting `depends_on`** — questions with `depends_on: domain=healthcare` should be skipped if the dependency isn't met.
