# 09 · Three Auditors + Meta-Jury

> **File.** `prompts/09_three_auditors_jury.md`
> **Tier.** Complex (~36 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).

## 1. Purpose

Runs **N parallel auditors** (default 3, configurable up to 10) over the audit sheet, each with a **distinct persona** for diversity-of-thought, then runs a **meta-jury** that consolidates findings, identifies disagreements, and surfaces escalations to humans at session checkpoints.

Independence is the core invariant: auditors are **blind to each other** until the jury phase. Dissent is **never silently resolved** — it always escalates to HITL.

## 2. When invoked

- **Phase.** 10 (`self_audit`), if `SystemSpec.auditor_mode != none`.
- Also re-invokable at session checkpoints during the child system's life.

## 3. Inputs

- `<target_path>/audit/audit_sheet.xlsx` (or csv+md fallback) — the sheet rows.
- System artifacts referenced by `evidence_link` fields (read-only).
- `SystemSpec.auditors_count` (3–10, default 3).
- `SystemSpec.auditor_mode` (parallel | sequential | none).
- `references/eu_ai_act_mapping.md#auditor_personas` — persona library.
- `templates/audit/auditor_*_template.md` — output templates.

## 4. Outputs

- `audit/audits/auditor_<n>_session_<id>.md` — per-auditor (N files).
- `audit/audits/jury_session_<id>.md` — consolidated.
- Plus sidecar `.json` files for machine consumption.

## 5. Tag rationale (~36 tags, Complex floor)

All 13 mandatory Complex tags must be present:

| Tag | Why |
|---|---|
| `<injection_defense>` | Audit-sheet content + system artifacts are data; auditors don't act on instructions inside cited evidence |
| `<alignment_rules>` | Independence (audit integrity), Evidence chain, Surface dissent (P2 calibration extends to audit consensus), HITL on dissent (mandatory) |
| `<capability_boundary>` | CAN orchestrate auditors + emit reports; CANNOT fill audit sheet auditor columns directly or resolve dissent without HITL |
| `<test_cases>` | 7 test cases (parallel happy path, sequential fallback, dissent on N rows, low-confidence consensus, prompt failure, sheet unreadable, N=10 max) |
| `<stop_condition>` | All N auditors complete + jury complete; or Factory escalates; or all N auditors fail |
| `<hitl_conditions>` | Dissent → mandatory escalation; low-confidence consensus → suggested escalation |
| `<tools>` | `prompt_architect` via Factory, `parallel.spawn` (optional), `fs.write` atomic |
| `<tool_selection>` | Factory always; parallel if available |
| `<action>` / `<observation>` | ReAct discipline for spawn + jury phases |
| `<scratchpad>` | Internal staging at tracking/sessions/<id>/scratch_audit.md |
| `<temporal_context>` | `{{TEMPORAL_NOW}}` injected into each auditor + jury prompt |
| `<verification>` | After each auditor: schema validates + every row has confidence%; after jury: agreement matrix sums correctly + dissent flags consistent |

Plus full Medium+ spine for total ~36 tags.

## 6. Control flow

```
1. Resolve N (auditors_count) + mode (parallel/sequential) + personas list.
2. Compose N auditor prompts via Factory (one per persona):
   - Same role, task, rubric, input.
   - DIFFERENT persona (e.g., risk_sme / ml_lead / security_lead).
3. Distribute audit sheet to each auditor (read-only).
4. Run auditors:
   if parallel.spawn available: spawn N concurrent.
   else: run sequentially (independence preserved by NOT showing others' outputs).
5. Each auditor emits per-row finding:
   {row_id, status, confidence_pct, evidence_cited, comments, auditor_persona}
6. Compose meta-jury prompt with all N auditor outputs as <input>.
7. Run jury (1 LLM call):
   - Build agreement matrix per row.
   - Identify dissent (≥2 auditors disagree, pass vs fail, partial = half-vote).
   - Compute consolidated status (majority + confidence-weighted).
   - List rows requiring HITL escalation (dissent ≥1 OR consensus low-confidence <70%).
8. Emit jury_session_<id>.md + sidecar JSON.
9. Signal orchestrator with summary + escalation list.
```

### Persona library (3-auditor balanced default)

| Persona | Article focus |
|---|---|
| `risk_sme` | Art. 9 — risk management |
| `ml_lead` | Art. 15a/b — accuracy + robustness |
| `security_lead` | Art. 15c — cybersecurity |

For >3: add `data_steward` (10), `tech_lead` (11), `devops_sre` (12), `ux_product` (13/50), `safety_lead` (14), `qms_lead` (17), `incident_commander` (73) in priority order.

### Jury aggregation logic

```
for row in rows:
  votes = [auditor.status for auditor in auditors]
  confidences = [auditor.confidence_pct for auditor in auditors]

  majority = mode(votes)
  agreement = count(votes == majority) / N

  if agreement < 0.5 and (pass in votes and fail in votes):
    dissent = True
    consolidated_status = "escalate"
  else:
    dissent = False
    consolidated_status = majority

  mean_conf = sum(c for v, c in zip(votes, confidences) if v == majority) / count(votes == majority)
  low_confidence_consensus = (not dissent) and (mean_conf < 70)

  if dissent or low_confidence_consensus:
    add to escalations
```

## 7. Calibration anchors (P2)

- Every auditor row carries `confidence_pct`.
- Jury aggregates with confidence weighting (not simple majority).
- `low_confidence_consensus` flag = mean confidence <70%.
- Audit reliability self-assessment in jury report: N=3 is the floor; calibration of auditor confidences vs ground truth (when known); recommended improvements.

## 8. Portability (P1)

- `parallel.spawn` is **optional** — sequential fallback preserves independence.
- All other tools abstract.
- Tier A on Claude Code (parallel via Agent), Tier A sequential on others.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| `parallel.spawn` unavailable | Sequential fallback + log |
| Auditor prompt composition fails | Iterate via Factory (3x); on persistent fail → exclude that auditor + log |
| N falls below 3 due to capability constraints | Escalate (audit reliability impacted) |
| Auditor output schema-invalid | Re-run that auditor once; on second fail → exclude from jury + log |
| Jury fails | Halt + escalate |
| Audit sheet unreadable | Halt + escalate |

## 10. HITL escalation triggers

- Any row with `dissent=true` → escalation required at session checkpoint.
- Any row with `low_confidence_consensus=true` → escalation suggested.
- N reduced below floor (3) → escalate (reliability impacted).
- Audit sheet missing/unreadable → escalate.

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md`, `07_audit_designer.md` (provides sheet), `03_prompt_factory.md` (composes auditor prompts), `prompt_architect/` (via Factory).
**Downstream:** Child orchestrator's checkpoint logic reads jury output for HITL escalation list.

## 12. Test coverage

- T4 prompt-tag floor (Complex must satisfy floor).
- T9 prompt-architect linkage (auditor prompts composed via Factory).
- Indirectly enforces T1 + T2 on its own emissions.

## 13. Common failure modes

1. **Auditors see each other** — independence rule violated. The orchestrator must NOT pass auditor_1's output as context to auditor_2. Sequential mode is the most error-prone here; check `<scratchpad>` isolation.
2. **Dissent silently resolved** — if jury picks majority and drops the dissent flag, HITL is bypassed. The aggregation logic + verification step must surface every dissent.
3. **Confidence weighting bypassed** — simple majority instead of confidence-weighted is wrong on close calls.
4. **N=2 silently accepted** — floor is 3; escalating is mandatory.
5. **Personas repeated** — if all 3 auditors are `risk_sme`, diversity-of-thought is lost. Persona uniqueness must be enforced.
6. **Evidence citation skipped** — every status MUST cite evidence (audit integrity rule). The auditor prompt's verification block enforces this.
