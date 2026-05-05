# 07 · Audit Designer

> **File.** `prompts/07_audit_designer.md`
> **Tier.** Medium (~24 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Bootstraps the child system's `audit/audit_sheet.xlsx` (or CSV+MD fallback). Reads the 13 checklist Excels + the EU AI Act mapping doc emitted by `06`, extracts ≥`min_rows` items per applicable Article, and produces the **Session-1 baseline rows** (status="pending"). Subsequent sessions append on top — this is a living document (P5).

Output structure: 14 sheets (`00_README` + `01..12` per Article + `99_Status_Log`).

## 2. When invoked

- **Phase.** 9 (`emit_audit_sheet`), after `06_eu_ai_act_mapper.md`.

## 3. Inputs

- `<target_path>/audit/eu_ai_act_mapping.md` (from 06).
- `Checklists y ejemplos/*.xlsx` (13 files, read-only).
- `templates/audit/audit_sheet.json.spec.tmpl` — sheet spec.
- `Ejemplo de hoja de AUDITORIA_HUMANA.xlsx` — example structure reference.
- Capability flag: `xlsx_available` (probed at start).

## 4. Outputs

- **Primary**: `<target_path>/audit/audit_sheet.xlsx` — 14 sheets, ≥112 rows for high-risk.
- **Fallback (if xlsx unavailable)**: `audit_sheet.csv` + `audit_sheet.md` (sidecar) with identical content.
- Update to `<target_path>/audit/eu_ai_act_mapping.md` with achieved counts.
- `mapping_completeness_pct` baseline computed.

## 5. Tag rationale (~24 tags)

Medium spine plus:
- `<temporal_context>` — `added_at` per row.
- `<fallback>` — explicit xlsx → CSV+MD → JSON ladder.
- `<observation>` — rows_per_article + completeness_pct emitted.
- `<verification>` — read-back row count, schema validation per row, completeness threshold check.
- `<injection_defense>` — checklist cells with imperatives rendered as text only.

## 6. Control flow

```
1. Probe capability: xlsx.write available?
2. Read audit/eu_ai_act_mapping.md → list of (Article, checklist_path, min_rows).
3. For each (Article, checklist_path):
   a. Try open xlsx with reader → extract items.
   b. On reader fail: fallback to placeholder rows (item="[manual review needed — see <path>]") + log.
   c. Build AuditRow objects (row_id, area, eu_ai_act_article, checklist_ref, item, evidence_link="", status="pending", auditor="", auditor_confidence_pct=null, comments="", session_id="0001_bootstrap", added_at=now()).
   d. Append to in-memory sheet.
4. Initialize 99_Status_Log with one entry per row (from_status=null, to_status=pending).
5. Render output:
   - if xlsx_available: xlsx.write with 14 sheets.
   - else: csv.write rows + render audit_sheet.md sidecar.
6. Compute mapping_completeness_pct = (rows_emitted / sum(min_rows)) * 100.
7. If mapping_completeness_pct < threshold (95% for high-risk) → escalate.
8. Update audit/eu_ai_act_mapping.md with achieved counts.
9. Signal complete with format_used + total_rows + completeness_pct + fallbacks_used.
```

### Sheet structure

| Sheet | Purpose |
|---|---|
| `00_README` | Audit-orientation for human auditors (instructions, columns explained, status enum) |
| `01..12` | One per Article (9, 10, 11, 12, 13, 14, 15a, 15b, 15c, 17, 50, 72, 73) |
| `99_Status_Log` | Append-only history of every status change (from, to, who, when, comment) |

### AuditRow fields

```json
{
  "row_id": "string (e.g., 01_RM_001)",
  "session_id": "string (e.g., 0001_bootstrap)",
  "area": "enum",
  "eu_ai_act_article": "string (e.g., Art. 9(2)(a))",
  "checklist_ref": "string (file path)",
  "item": "string (description from checklist)",
  "evidence_link": "string (empty initially)",
  "status": "pass | fail | partial | not_applicable | pending",
  "auditor": "string (empty initially)",
  "auditor_confidence_pct": "int | null",
  "comments": "string"
}
```

## 7. Calibration anchors (P2)

- `mapping_completeness_pct` is a calibrated metric with threshold by risk class:
  - high → ≥95%
  - limited → ≥85%
  - minimal → ≥70%
- Per-row: `auditor_confidence_pct` enforced when auditors fill (downstream).
- Placeholder rows (when xlsx-reader fails): logged with confidence ~50% on item description, recommend manual review.

## 8. Portability (P1)

- `xlsx.write` is **optional**. Tier A platforms without xlsx capability → CSV+MD fallback.
- Last-resort fallback: `audit_sheet.json` if both xlsx + csv unavailable.
- Atomic writes for all output files.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| xlsx-reader fails on a checklist | Placeholder rows + log + escalate at Gate #2 |
| `xlsx.write` unavailable | CSV+MD fallback; log to `audit/self_audit.md#portability_fallbacks` |
| Both xlsx + csv unavailable | JSON-only emit + log severe portability issue + escalate |
| `mapping_completeness_pct` < threshold | Escalate to Gate #2 |
| Atomic write fails | Cleanup `*.tmp` + retry once |

## 10. HITL escalation triggers

- Completeness below threshold for risk class.
- Checklist file unreadable → "manual checklist review needed" note.
- All output formats unavailable → severe portability issue.

## 11. Dependency edges

**Upstream:** `06_eu_ai_act_mapper.md` (provides mapping doc), `00_master_orchestrator.md` (dispatches), `Checklists y ejemplos/*.xlsx`, sheet spec template.
**Downstream:** `09_three_auditors_jury.md` reads this sheet for auditor assignments. Child orchestrator appends rows per session.

## 12. Test coverage

- T7 EU AI Act mapping (verifies row totals).
- T1 portability — abstract tools + fallback documented.
- T9 prompt-architect linkage.

## 13. Common failure modes

1. **xlsx reader silently swaps content** — if reader misinterprets cells (e.g., date formats), items are misquoted. Verification step should sanity-check row count against checklist's row count.
2. **Sheet collision** — two Articles mapping to overlapping rows (shouldn't happen given 1:1 mapping, but defensive).
3. **`evidence_link` auto-filled** — must remain empty initially; child sessions populate it. If 07 fills it, it pollutes the audit trail.
4. **Status auto-fill beyond "pending"** — only humans set pass/fail. The seeder must NEVER write pass/fail.
5. **Placeholder rows not flagged** — if xlsx-reader fails for one Article and emits placeholders silently, auditors waste time on them. Flag clearly in `00_README`.
