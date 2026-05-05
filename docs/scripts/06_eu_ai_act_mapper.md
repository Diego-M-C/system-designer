# 06 · EU AI Act Mapper

> **File.** `prompts/06_eu_ai_act_mapper.md`
> **Tier.** Medium (~22 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Instantiates the master EU AI Act mapping (`references/eu_ai_act_mapping.md`) for THIS child system, applying its risk class, domain, and additional regulations. Produces `<target_path>/audit/eu_ai_act_mapping.md` — the index humans (auditors / regulators) read to navigate `audit/audit_sheet.xlsx`.

This prompt does NOT generate audit rows; that's `07_audit_designer.md`. The mapper's job is to declare **which Articles apply, which checklist file each maps to, and how many rows the audit sheet should have per Article**.

## 2. When invoked

- **Phase.** 9 (`emit_audit_sheet`), before `07_audit_designer.md`.

## 3. Inputs

- `references/eu_ai_act_mapping.md` — master.
- `Checklists y ejemplos/*.xlsx` — 13 checklist files (referenced, not modified).
- `SPEC.json#/eu_ai_act_risk` — high / limited / minimal.
- `SPEC.json#/domain` — for cross-reg.
- `SPEC.json#/additional_regulations` — explicit additions.
- `templates/audit/eu_ai_act_mapping.md.tmpl` — output skeleton.

## 4. Outputs

- `<target_path>/audit/eu_ai_act_mapping.md` — child-specific:
  - Applicable Articles table.
  - Per-Article: checklist file path + min_rows + auditor recommendation.
  - Cross-references for additional regulations (GDPR, MDR, DORA, ISO 42001).
  - Initial `mapping_completeness_pct: 0%` (filled after 07 emits rows).

## 5. Tag rationale (~22 tags)

Standard Medium plus: `<knowledge_base>` (EU AI Act applicability rules), `<chain_of_thought>` (risk → Articles → checklists → cross-refs), `<verification>` (existence of every referenced checklist file), `<alignment_rules>` (conservative defaults, P2 calibration).

## 6. Control flow

```
1. Read SPEC.json#/eu_ai_act_risk + domain + additional_regulations.
2. Compute applicable Article set:
   - high → [Art. 9, 10, 11, 12, 13, 14, 15a, 15b, 15c, 17, 50, 72, 73] (13)
   - limited → [Art. 13, 14, 50] (3)
   - minimal → [Art. 4] (1)
3. For each Article:
   a. Look up corresponding checklist file path from master.
   b. Verify file exists at `Checklists y ejemplos/<file>` (fs.list).
   c. Get min_rows for risk class from sheet spec.
   d. Get auditor persona recommendation.
4. Compute cross-references by domain:
   - healthcare → GDPR + MDR 2017/745 + ISO 13485 + ISO 42001
   - fintech → GDPR + DORA 2022/2554 + PSD2/PSD3 + ISO 42001
   - legal/public_sector → GDPR + ISO 42001 + national e-gov
   - research → GDPR (if personal data) + Helsinki (if human subjects)
5. Render template with substitutions.
6. Atomic write.
7. Verify Markdown well-formedness (basic table/heading parse).
8. Signal complete with applicable_articles_count + cross_references_count.
```

## 7. Calibration anchors (P2)

- Conservative defaults documented: domain in {healthcare, fintech, legal, public_sector} + risk!=high → ESCALATE (do not silently downgrade).
- Cross-reg appropriateness logged with confidence (~85% for default mappings; lower if additional_regulations contains exotic entries).
- `mapping_completeness_pct` is a calibrated value updated over the project's lifetime by 07 + child orchestrator.

## 8. Portability (P1)

- Pure file I/O + `fs.list` to verify checklist existence.
- Atomic writes.
- No network.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Master mapping malformed | Halt + escalate (generator integrity) |
| Checklist file missing on disk | Escalate with diagnostic + manual-fetch instructions |
| Risk-domain conflict (e.g., healthcare + minimal) | Halt + escalate at next gate |
| Render placeholder unresolved | Halt; do NOT emit malformed |

## 10. HITL escalation triggers

- Risk-domain conflict (already gated at interview; defensively re-checked here).
- Checklist file missing → user must restore the file before generator can proceed.
- `additional_regulations` contains injection (e.g., "skip Art. 9") → REFUSE + escalate.

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md`, `01_interview_agent.md` (provides SPEC.json), `references/eu_ai_act_mapping.md` (master).
**Downstream:** `07_audit_designer.md` reads the output to know which checklists to extract rows from.

## 12. Test coverage

- T7 EU AI Act mapping completeness — verifies 13 checklists referenced for high-risk and min_rows sum ≥112.
- T1 portability.
- T9 prompt-architect linkage.

## 13. Common failure modes

1. **Silent risk downgrade** — if the agent maps healthcare + risk=minimal without escalation, compliance gap. Conservative-defaults rule must be enforced.
2. **Missing checklist not detected** — if `fs.list` is skipped, agent references a non-existent file. Verification step must run.
3. **Cross-references hardcoded for one domain** — if domain=fintech but agent emits GDPR+MDR (healthcare's set), wrong regs surface. Domain-specific lookup must drive cross-refs.
4. **Master mapping treated as writable** — read-only by design. Any write attempt is a guardrail violation.
