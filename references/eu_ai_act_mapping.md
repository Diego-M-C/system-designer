# EU AI Act → Checklist → Audit-Row Mapping

> **Source regulation:** Regulation (EU) 2024/1689 — Artificial Intelligence Act, OJ L 2024/1689 (in this repo: `EU_AI_Act_guides/OJ_L_202401689_EN_TXT.pdf`).
>
> **Implementation guides:** AESIA (Spanish AI Supervisory Agency) guides in `EU_AI_Act_guides/Guides/` and consolidated zip `EU_AI_Act_guides/Checklists y ejemplos.zip`.
>
> **Checklists corpus:** 13 Excel checklists in `Checklists y ejemplos/`. Each one maps to one or more Articles. The generator references these directly from the child system's `audit/checklists/`.
>
> **Purpose of this file:** the `06_eu_ai_act_mapper.md` agent reads it and emits `<target_path>/audit/eu_ai_act_mapping.md` (instantiated for the specific child system, with risk classification applied).

---

## 1 · Risk classification (Art. 6 + Annex III)

| Risk class | Article | Behaviour by default |
|---|---|---|
| Prohibited | Art. 5 | REFUSE to scaffold; surface to user. |
| High-risk | Art. 6 + Annex III | DEFAULT for all scaffolds (conservative). All 13 checklists active. Mapping completeness ≥95%. |
| Limited-risk | Art. 50 (transparency) | Subset of checklists active (Transparencia + Supervisión Humana). User MUST confirm downgrade explicitly. |
| Minimal-risk | implicit | Only voluntary code-of-conduct mapping. User MUST confirm downgrade explicitly + log rationale to `decisions.md`. |

**Annex III high-risk areas** (any scaffold targeting these defaults to high-risk):
- Biometrics (categorisation, emotion recognition)
- Critical infrastructure (energy, water, gas, road traffic)
- Education and vocational training (admission, grading)
- Employment (recruitment, performance, firing)
- Essential services (credit scoring, public assistance, insurance pricing, emergency triage)
- Law enforcement
- Migration / asylum / border control
- Administration of justice / democratic processes

If `SystemSpec.domain` ∈ {healthcare, fintech, legal, public_sector} → presumed high-risk unless user proves otherwise.

---

## 2 · Article → checklist mapping

The 13 checklists in `Checklists y ejemplos/`:

| # | Checklist file | Primary Article | Secondary Articles | Audit area code |
|---|---|---|---|---|
| 1 | `Gestión de riesgos_Checklist.xlsx` | **Art. 9** (risk management) | Art. 6, Annex III | `risk_management` |
| 2 | `05.01 Ejemplo ilustrativo del desarrollo de un sistema de gestión de riesgos.xlsx` | **Art. 9** (illustrative example) | — | `risk_management_example` |
| 3 | `Gobernanza del dato_Checklist.xlsx` | **Art. 10** (data + data governance) | Art. 26 (deployer) | `data_governance` |
| 4 | `Documentación tecnica_Checklist.xlsx` | **Art. 11** (technical documentation) + Annex IV | — | `technical_documentation` |
| 5 | `Registros_Checklist.xlsx` | **Art. 12** (record-keeping / logs) | Art. 19 (registers retained) | `record_keeping` |
| 6 | `Transparencia_Checklist.xlsx` | **Art. 13** (transparency to deployer) + **Art. 50** (transparency to user) | Art. 11 | `transparency` |
| 7 | `Supervisión Humana_Checklist.xlsx` | **Art. 14** (human oversight) | — | `human_oversight` |
| 8 | `Precision_Checklist.xlsx` | **Art. 15** (accuracy) | Art. 17 | `accuracy` |
| 9 | `Solidez_Checklist.xlsx` | **Art. 15** (robustness) | — | `robustness` |
| 10 | `Ciberseguridad_Checklist.xlsx` | **Art. 15** (cybersecurity) | Art. 9 | `cybersecurity` |
| 11 | `Gestión de Calidad_Checklist.xlsx` | **Art. 17** (quality management system) | — | `quality_management` |
| 12 | `Vigilancia Poscomercializacion_Checklist.xlsx` | **Art. 72** (post-market monitoring) | Art. 17 | `post_market_monitoring` |
| 13 | `Gestión de incidentes_Checklist.xlsx` | **Art. 73** (serious incidents reporting) | Art. 72 | `incident_management` |

---

## 3 · Article → audit_sheet rows (templated)

Each row in `<target_path>/audit/audit_sheet.xlsx` conforms to `system_generator.json#/definitions/AuditRow`. Required minimum row count per Article (high-risk default):

| Article | Min rows | Row source | Auditor recommended |
|---|---|---|---|
| Art. 9 — risk management | 12 | rows from `Gestión de riesgos_Checklist.xlsx` + 6 from illustrative example | risk SME |
| Art. 10 — data governance | 14 | rows from `Gobernanza del dato_Checklist.xlsx` | data steward |
| Art. 11 — technical documentation | 18 | rows from `Documentación tecnica_Checklist.xlsx` | tech lead |
| Art. 12 — record-keeping | 8 | rows from `Registros_Checklist.xlsx` | DevOps / SRE |
| Art. 13/50 — transparency | 10 | rows from `Transparencia_Checklist.xlsx` | UX / product |
| Art. 14 — human oversight | 8 | rows from `Supervisión Humana_Checklist.xlsx` | safety lead |
| Art. 15 — accuracy | 6 | rows from `Precision_Checklist.xlsx` | ML lead |
| Art. 15 — robustness | 6 | rows from `Solidez_Checklist.xlsx` | ML lead |
| Art. 15 — cybersecurity | 8 | rows from `Ciberseguridad_Checklist.xlsx` | security lead |
| Art. 17 — quality management | 10 | rows from `Gestión de Calidad_Checklist.xlsx` | QMS lead |
| Art. 72 — post-market monitoring | 6 | rows from `Vigilancia Poscomercializacion_Checklist.xlsx` | SRE / product |
| Art. 73 — incident management | 6 | rows from `Gestión de incidentes_Checklist.xlsx` | incident commander |

**Total minimum rows (high-risk):** ~112. The audit sheet starts with these and grows incrementally as sessions add domain-specific evidence.

---

## 4 · Mapping algorithm (used by `06_eu_ai_act_mapper.md`)

```
1. Determine eu_ai_act_risk from SystemSpec.
2. If high-risk: include all 13 checklists, instantiate all minimum rows.
3. If limited-risk: include {Transparencia, Supervisión Humana} + Art. 50 disclosure rows.
4. If minimal-risk: include only voluntary-code-of-conduct row + Art. 4 (literacy) row; log downgrade rationale.
5. For each included checklist:
   a. Reference (do NOT copy) the Excel from ../Checklists y ejemplos/.
   b. Generate <target_path>/audit/checklists/<area>.md with: source path, items count, mapped Article, status fields.
   c. Append rows to audit_sheet.xlsx (or CSV+MD fallback).
6. Compute mapping_completeness_pct = (rows_emitted / rows_required) * 100.
7. If completeness < 95% on high-risk: escalate at Gate #2.
```

---

## 5 · Living-doc behaviour (P5)

`audit/audit_sheet.xlsx` is **incremental**, not final-state:

- Session-0001 emits the **baseline rows** (the ~112 minimum from §3).
- Each subsequent session that touches a high-risk surface (data ingest, model update, UX change, incident) emits new rows and links them to its session id (`AuditRow.session_id`).
- Each session writes a `audit/audits/session_<id>/added_rows.csv` for diffability.
- Status transitions on rows (`pending → partial → pass/fail`) are recorded with timestamps in `audit/audits/status_log.jsonl`.

The audit sheet is **never frozen** until the system is decommissioned. Final audit is the snapshot at decommission.

---

## 6 · Auditor configuration

Per `SystemSpec.auditor_mode` (default `parallel_with_meta_jury`, `auditors_count: 3`):

- **3 parallel auditors** — each reads the same audit sheet + system artifacts independently, emits findings in `audit/audits/auditor_<n>_session_<id>.md`.
- **Meta-jury (1 LLM)** — reads the 3 reports, produces `audit/audits/jury_session_<id>.md`: agreement matrix, dissent analysis, final consolidated finding per row.
- **HITL escalation:** any row where ≥2 auditors disagree → user decides at gate.

Auditor agents composed via `09_three_auditors_jury.md` (each an independent prompt-architect Complex-tier prompt with distinct `<persona>` for diversity-of-thought).

---

## 7 · Cross-reference to other regulations (informational)

| Reg / Standard | Relation to EU AI Act | Applicable when |
|---|---|---|
| **GDPR** (2016/679) | Art. 10 cross-refs (lawful basis, special-category data) | always for personal data |
| **ISO/IEC 42001** | Art. 17 quality management system reference | recommended for high-risk |
| **ISO/IEC 23894** (AI risk management) | Art. 9 reference | recommended for high-risk |
| **ISO/IEC 24029-2** (robustness assessment of NN) | Art. 15 reference | applicable to NN-based systems |
| **NIST AI RMF** | Cross-walks with Art. 9, 17 | informational |
| **MDR 2017/745** (medical devices) | If domain=healthcare → also applicable | always for medical-device-classifiable systems |
| **DORA** (2022/2554) | If domain=fintech (operational resilience) | always for financial entities |

The mapper agent surfaces relevant cross-references in `audit/eu_ai_act_mapping.md#cross_references` based on `SystemSpec.domain`.

---

## 8 · Mapping-completeness self-test

After scaffolding, the self_audit phase computes:

```
completeness_pct = (audit_rows_emitted / audit_rows_required[risk_class]) * 100
```

Thresholds:
- High-risk: ≥95% required for Gate #2 pass.
- Limited-risk: ≥85% required.
- Minimal-risk: ≥50% required (rationale logged).

Below threshold → ❌ in `audit/self_audit.md` → iterate ≤3 times → escalate at Gate #2.
