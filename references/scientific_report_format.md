# Scientific Report Format — IMRaD · TRIPOD-AI · CONSORT-AI

> **Purpose:** the child system emits formal reports in `docs/reports/` at session checkpoints (cumulative) and at end-of-project (final). The reports are publication-grade — formatted as if for a peer-reviewed journal.
>
> **Standard selection:** chosen by `08_report_writer.md` from `SystemSpec.domain` + system type. Decision tree below.

---

## 1 · Standard selection

```
                   ┌─ healthcare + predictive system ─→ TRIPOD-AI (extended)
                   ├─ healthcare + RCT / clinical trial ─→ CONSORT-AI (extended)
SystemSpec.domain ─┤
                   ├─ healthcare + diagnostic AI study ─→ STARD-AI
                   ├─ healthcare + AI intervention protocol ─→ SPIRIT-AI
                   ├─ legal / public_sector + decision-support ─→ IMRaD + EU AI Act Annex IV adapter
                   └─ fintech / research / other ─→ IMRaD (universal fallback)
```

Default: IMRaD. Any deviation requires explicit interview answer.

---

## 2 · IMRaD (Introduction · Methods · Results · Discussion · Conclusions)

Template at `templates/reports/imrad.md.tmpl`. Sections (mandatory):

### 2.1 · Title page
- Project name + version
- Authors (incl. AI-collaborator declared explicitly)
- Date (ISO)
- Repository / DOI if registered

### 2.2 · Abstract (≤300 words)
- Background (1–2 sentences)
- Objective (1 sentence)
- Methods (2–3 sentences)
- Results (3–4 sentences with key %)
- Conclusion (1–2 sentences)
- Calibrated: every numeric in the abstract carries a CI or range.

### 2.3 · Introduction
- Background + motivation
- Gap addressed
- Objectives (numbered)
- Hypotheses (if applicable, with prior probability)

### 2.4 · Methods
- Study design / system architecture
- Data sources (with EU AI Act Art. 10 traceability)
- Pre-processing
- Modelling / decision logic
- Evaluation protocol (metrics, baselines, statistical tests)
- HITL integration points
- Compute / environment (model versions, library versions from `library_docs/MANIFEST.md`)
- Reproducibility statement (seeds, configs, commit hashes)
- Ethics / data governance / consent

### 2.5 · Results
- Descriptive statistics (with CIs)
- Primary outcomes (with effect size + CI)
- Secondary outcomes
- Sensitivity / ablation analyses
- Errors caught (link to `tracking/errors_catalog.json` summary)
- Calibration plots (model confidence vs observed)
- Audit results summary (link to `audit/audit_sheet.xlsx` snapshot)
- Figures + tables (numbered, captioned, source data linked)

### 2.6 · Discussion
- Principal findings restated
- Comparison to prior work
- Strengths
- Limitations (≥3, each with severity + mitigation)
- Generalisability (with caveats)
- Decision-quality reflection (HITL gates: agreement vs override rate)

### 2.7 · Conclusions
- Bottom-line statement (calibrated)
- Recommendations for deployer
- Future work (≤5 bullets)

### 2.8 · References
- All citations verified (no AIE-001 cite-not-found violations)
- DOI / URL where available
- Cross-link to `library_docs/MANIFEST.md` for software citations

### 2.9 · Supplementary materials
- Full audit sheet (PDF export of `audit/audit_sheet.xlsx`)
- Decisions log (`tracking/decisions.md`)
- Errors catalog (`tracking/errors_catalog.json`)
- Sessions log (summarised from `tracking/sessions/*`)
- Self-audit report (`audit/self_audit.md`)

---

## 3 · TRIPOD-AI (predictive systems)

Extended Transparent Reporting of a multivariable prediction model for AI. Template at `templates/reports/tripod_ai.md.tmpl`. Adds to IMRaD:

### Mandatory TRIPOD-AI items (selected — full list in template)

| Item | Section | Content |
|---|---|---|
| 1a | Title | Identify as a prediction model + AI/ML method used |
| 3a | Introduction | Source(s) of data |
| 4a | Methods | Specify key dates (sample collection, follow-up start/end) |
| 6a | Methods | Define outcome predicted, including assessment + scoring |
| 7a | Methods | Define each predictor in detail |
| 8a | Methods | Sample size justification |
| 9 | Methods | Missing-data handling |
| 10b | Methods | All steps of model building (variable selection, hyperparameters, regularisation) |
| 10c | Methods | Method for internal validation (e.g., bootstrap, k-fold CV) |
| 11 | Methods | Risk-group definition (if applicable) |
| 12 | Methods | Model performance measures (discrimination, calibration) |
| 14a | Results | Sample flow (CONSORT-style diagram) |
| 14b | Results | Participants characteristics (table) |
| 16 | Results | Model presentation (full equation / coefficients / decision tree / model card) |
| 17 | Results | Model performance (with CIs) |
| 18 | Discussion | Interpretation considering objectives, limitations, similar studies |
| 19a | Discussion | Discuss any potential clinical use of model + implications |
| 20 | Discussion | Limitations of the study |
| 21 | Other | Supplementary information location |
| 22 | Other | Funding sources |

### TRIPOD-AI specific additions
- AI/ML method specification (architecture, training procedure)
- Data preprocessing for AI (feature engineering, embeddings, augmentation)
- Computational infrastructure (GPUs, training time)
- Fairness / subgroup performance (per protected attribute)
- Calibration over time (drift)
- Interpretability methods used (SHAP, LIME, attention, etc.)
- External validation status

---

## 4 · CONSORT-AI (clinical trials of AI interventions)

Extended CONSORT for AI/ML clinical trials. Template at `templates/reports/consort_ai.md.tmpl`. Adds to CONSORT 2010:

### CONSORT-AI specific items (selected)
- AI version + lock-down date
- Intended use + stage of evaluation
- Input data handling (resolution, format, quality control)
- Output specification + how it informs decisions
- Integration into clinical workflow
- Human-AI interaction protocol
- Performance monitoring + drift detection
- Error analysis
- Code + data + model availability statements

---

## 5 · STARD-AI (diagnostic AI studies)

Extended STARD for diagnostic AI. Use when system performs binary/multi-class classification on diagnostic data. Template at `templates/reports/stard_ai.md.tmpl`.

---

## 6 · SPIRIT-AI (clinical trial protocols with AI)

Extended SPIRIT for AI trial protocols. Use when emitting a pre-registered protocol. Template at `templates/reports/spirit_ai.md.tmpl`.

---

## 7 · Calibration in reports (P2)

Every numeric result must have:
- Point estimate
- Uncertainty (95% CI, IQR, ± SD as appropriate)
- N (sample size)
- Source (data path / `tracking/sessions/<id>/observations.jsonl`)

Forbidden in reports:
- "significant" without p-value + CI
- "improved" without effect size + CI
- "best" / "worst" without ranking + caveats
- bare numbers

---

## 8 · Reproducibility statement (mandatory section)

Every report includes:

```markdown
## Reproducibility

- **Source code:** <repo URL or local path> @ commit `<hash>`
- **Data:** <DOI / dataset URL / "private — see DPA at audit/dpa.md">
- **Environment:** see `library_docs/MANIFEST.md` (frozen at commit `<hash>`)
- **Random seeds:** see `SPEC.json#reproducibility.seeds`
- **Compute:** <hardware spec> · <wall-clock>
- **Configs:** see `SPEC.json#configs`
- **How to reproduce:** see `README.md#reproduce`
```

---

## 9 · Cumulative vs final reports

The child system emits reports at TWO cadences:

| Cadence | When | Content |
|---|---|---|
| **Cumulative (per session)** | At every HITL checkpoint | Section appended to `docs/reports/cumulative.md`: session summary, KPIs delta, errors caught, decisions made, audit rows added |
| **Milestone (per phase)** | At phase boundary defined in SPEC | Mid-project IMRaD draft, refreshed |
| **Final** | At project completion / decommission | Full standard-compliant report (TRIPOD-AI / CONSORT-AI / STARD-AI / IMRaD), publication-ready |

The report writer agent (`08_report_writer.md`) handles both modes.

---

## 10 · Quality gate (before publication)

Before any report is marked "publication-ready", the child orchestrator runs:

1. **Calibration scan** — `references/calibrated_probabilities.md §6` protocol.
2. **Citation verification** — every reference resolvable; no AIE-001 violations.
3. **Standard-compliance check** — every mandatory item of the chosen standard present (TRIPOD-AI: 22 items; CONSORT-AI: extended CONSORT; etc.).
4. **EU AI Act audit consistency** — claims in report match `audit/audit_sheet.xlsx` status.
5. **Reproducibility check** — every claim links back to a session / observation / commit.
6. **HITL final review** — user (or named human author) signs off.

Failure on any check → report marked DRAFT, reasons logged, iterate.

---

## 11 · Deliverable formats

The report is emitted in:
- `docs/reports/<name>.md` — primary, source of truth
- `docs/reports/<name>.pdf` — generated via pandoc / weasyprint (on-demand if executor supports)
- `docs/reports/<name>.html` — generated via pandoc (on-demand)
- `docs/reports/<name>.docx` — generated via pandoc (on-demand)

The MD source is canonical. Other formats are derivatives, regenerated on each commit to MD.
