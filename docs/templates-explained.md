# templates/ — section-by-section walkthrough

> The `templates/` directory holds the **file skeletons** rendered into the child system tree. Every `*.tmpl` has a corresponding output file in `<target_path>/<system_name>/`.

| Group | Files | Output location |
|---|---|---|
| Top-level | `CLAUDE.md.tmpl`, `README.md.tmpl`, `SPEC.md.tmpl`, `SPEC.json.tmpl`, `ARCHITECTURE.md.tmpl`, `HANDOFF.md.tmpl`, `hitl_gate.md.tmpl` | `<system>/` |
| Tracking | `tracking/project.json.tmpl`, `kpis.json.tmpl`, `session.json.tmpl`, `decisions.md.tmpl`, `errors.md.tmpl`, `errors_catalog.json.tmpl`, `inputs_outputs_perf.json.tmpl`, `checkpoint_decision.md.tmpl` | `<system>/tracking/` |
| Memory | `memory/MEMORY.md.tmpl`, `user.md.tmpl`, `project.md.tmpl`, `feedback.md.tmpl`, `reference.md.tmpl` | `<system>/memory/` |
| Audit | `audit/audit_sheet.json.spec.tmpl`, `eu_ai_act_mapping.md.tmpl`, `self_audit.md.tmpl`, `reflection_session_0.md.tmpl`, `evaluation_session_0.json.tmpl`, `assumptions.md.tmpl` | `<system>/audit/` |
| Reports | `reports/imrad.md.tmpl`, `tripod_ai.md.tmpl` (+ on-demand others) | `<system>/docs/reports/` |
| Library docs | `library_docs/MANIFEST.md.tmpl`, `library_docs_manifest.tmpl` | `<system>/library_docs/<lib>/<version>/` |

## Placeholder convention

Two kinds:

- **Metadata placeholders** — substituted at scaffold time by `02_scaffolder.md`. Examples: `{{system_name}}`, `{{TEMPORAL_NOW}}`, `{{system_version}}`, `{{domain}}`, `{{eu_ai_act_risk}}`.
- **Content placeholders** — preserved as literal `{{...}}` for the child orchestrator to fill at runtime. Examples: `{{abstract_background}}`, `{{session_summary}}`, `{{methods_data_provenance}}`, `{{kpi_duration_actual}}`.

The scaffolder MUST distinguish these. Substituting a content placeholder with `""` is a critical bug.

---

## 1. Top-level templates

### `CLAUDE.md.tmpl` — Child orchestrator contract

The most important template. Renders to `<system>/CLAUDE.md`, which IS the child orchestrator's instructions. Contains:

- **Mandatory reads** — list of files the child orchestrator must load at session start.
- **Session lifecycle** — `PLAN → EXECUTE → TEST → DOCUMENT → AUDIT_ROW_APPEND → CHECKPOINT_HITL`.
- **8 operating constraints** — calibration, atomic writes, library doc consultation before coding, AUDIT_ROW_APPEND mandatory, etc.
- **Prompt composition protocol** — every new prompt goes through prompt-architect.
- **Library freshness** — re-fetch if `last_fetched_at` >7 days.
- **Memory protocol** — when to read MEMORY.md, when to update.
- **Audit rhythm** — append rows per session.
- **Stop conditions** — when child orchestrator surrenders to HITL.
- **Report cadence** — when to update cumulative.md.

### `README.md.tmpl` — Child README

User-facing README of the child system. Quickstart, structure tree, reproducibility note, compliance summary, contributing.

### `SPEC.md.tmpl` / `SPEC.json.tmpl` — SDD spec

17-section Spec-Driven Development document:

1. metadata (system_name, version, owner, date)
2. intent
3. stakeholders
4. goals (with confidence%)
5. scope
6. non-goals
7. risks (with likelihood × impact)
8. functional requirements (FR-NNN)
9. non-functional requirements (NFR-NNN, with target + confidence)
10. data flow
11. architecture summary
12. sessions plan
13. milestones (with dates + confidence)
14. reproducibility (random seeds, env)
15. calibration commitment (which fields will carry confidence)
16. open questions
17. changelog

### `ARCHITECTURE.md.tmpl` — Child architecture

15 sections including: context (mermaid graph), layers, component diagram, data flow (sequence), storage/schema, compute/deployment, LLM integration, observability, security, EU AI Act compliance architecture per Article, anti-patterns, versioning + rollback, performance budget, decision log pointer.

### `HANDOFF.md.tmpl` — Final scaffold summary

Scaffold summary, self-audit summary table, invocation instructions, 3 dependency tiers, first 3 sessions planned, where-to-look table, resumption protocol, HITL escalation points, scope boundary.

### `hitl_gate.md.tmpl` — HITL gate format

Standardized format used at Gate #1 + Gate #2:

```
## HITL Gate <#> · <phase>

Calibrated alternatives:
[A] <option>  fit ~XX%
    pros: ...
    cons: ...
[B] <option>  fit ~YY%
[C] <option>  fit ~ZZ%
[D] <free-form input>
[E] abort

Recommendation: A · confidence ~CC%
Reasoning: ...

Reply with letter or free-form text. Auto-skip prohibited (P4 alignment).
```

---

## 2. tracking/ templates

### `project.json.tmpl` — Master project state

```json
{
  "system_name": "{{system_name}}",
  "system_version": "{{system_version}}",
  "current_phase": "{{current_phase}}",
  "current_session_id": "{{current_session_id}}",
  "completed_phases": [],
  "gates_status": {
    "GATE_1": {"status": "pending"},
    "GATE_2": {"status": "pending"}
  },
  "artifacts_emitted": [],
  "audit_results": [],
  "errors_seen_summary": {},
  "kpis_running": {},
  "compliance": {...},
  "configs": {...},
  "calibration_violations": 0,
  "portability_violations": 0
}
```

### `kpis.json.tmpl` — 11 KPIs

Initial values for all 11 KPIs (see ARCHITECTURE.md#15) with ranges/confidence + calibration/portability violation counters.

### `session.json.tmpl` — Per-session state

Phases, files touched, decisions, audit rows, library docs, errors, io_perf (latency p50/p95, memory, cpu, tokens), checkpoint.

### `decisions.md.tmpl` — ADR log

ADR-NNN entries with title, date, context, decision, calibrated alternatives, confidence, citations, consequences.

### `errors.md.tmpl` — Error narrative

ERR-NNN entries: id, AIE pattern matched, session, severity, description, fix, prevention added.

### `errors_catalog.json.tmpl` — 30 AIE preloaded

Full JSON skeleton with the 30 AIE-NNN entries hardcoded for fast-path. `05_error_prevention_seeder.md` verifies count == 30 before emit.

### `inputs_outputs_perf.json.tmpl` — Per-script test data

Sample I/O, performance (latency p50/p95, memory, cpu, tokens), determinism flag, environment.

### `checkpoint_decision.md.tmpl` — HITL checkpoint doc

Alternatives table, recommendation + confidence, user decision, implications for next session.

---

## 3. memory/ templates

### `MEMORY.md.tmpl` — Index

Lists 4 typed memory files with brief descriptors.

### `user.md.tmpl` — User profile

Role, preferences, validated behaviours, past corrections.

### `project.md.tmpl` — Project facts

Motivations, constraints, open questions, decided-vs-tentative.

### `feedback.md.tmpl` — User feedback log

FB-NNN entries with date, rule, **Why:** and **How to apply:** lines.

### `reference.md.tmpl` — External pointers

Links to Linear, Slack, Grafana, CI/CD, secrets vaults, documentation portals.

---

## 4. audit/ templates

### `audit_sheet.json.spec.tmpl` — 13-sheet xlsx spec

Defines:
- Sheet structure: 00_README, 01..12, 99_Status_Log.
- Per-Article sheet: min_rows_high_risk, min_rows_limited, min_rows_minimal, checklist_source, columns.
- Rendering instructions for `07_audit_designer.md`.
- Fallback format (CSV+MD).

### `eu_ai_act_mapping.md.tmpl` — Child-specific mapping

Renders to `<system>/audit/eu_ai_act_mapping.md`. Has applicable_articles_table, per-Article rows, cross_references for additional regulations, and a `mapping_completeness_pct` field.

### `self_audit.md.tmpl` — 12-section self-audit

Coverage, rubric scoring, calibration scan results, portability scan results, EU AI Act mapping completeness, living-doc integrity, fallbacks used, violations, iterations.

### `reflection_session_0.md.tmpl` — Structured reflection

What was emitted, what was skipped, lowest-confidence decisions, failure modes encountered, lessons, what to do differently next session.

### `evaluation_session_0.json.tmpl` — Machine-readable evaluation

All metrics from the reflection in queryable form for the dashboard.

### `assumptions.md.tmpl` — Explicit assumptions

Each assumption: ID, statement, verification plan, confidence, status (pending/verified/falsified).

---

## 5. reports/ templates

### `imrad.md.tmpl` — IMRaD universal

Title page, abstract, Intro, Methods, Results, Discussion, Conclusions, References, Supplementary. Always emitted (universal fallback).

### `tripod_ai.md.tmpl` — TRIPOD-AI 33-item

For predictive AI in healthcare. Includes AI/ML-specific additions: model architecture, training data provenance, hyperparameters, performance distribution by subgroup, calibration, fairness, generalisation evidence.

### Other report templates (on-demand)

- `consort_ai.md.tmpl` — clinical trials.
- `stard_ai.md.tmpl` — diagnostic studies.
- `spirit_ai.md.tmpl` — protocols.

Emitted only if SPEC.json indicates the relevant sub-domain.

---

## 6. library_docs/ templates

### `MANIFEST.md.tmpl` — Per-library metadata

Each library's `MANIFEST.md` contains:
- name, version
- last_fetched_at
- source_used (context7 / primary / fallback / github_release_api)
- primary_url, fallback_url
- sha256 of fetched content
- re-fetch protocol (when to refresh)
- offline-mode behaviour

### `library_docs_manifest.tmpl` — 26 library URL mappings

Master URL list for every supported library. Each entry has:
- name, current_version
- primary URL (official docs)
- fallback URL (alternative)
- github_release_api (last resort)
- fetch_protocol (Context7-first / HTTP-only / etc.)

The 26 libraries cover: anthropic-python-sdk, fastapi, pydantic, sqlalchemy, alembic, postgres, timescaledb, redis-py, celery, pytest, tenacity, tiktoken, polars, duckdb, scikit-learn, xgboost, pytorch, transformers, langchain, langgraph, vercel-ai-sdk, next.js, streamlit, openpyxl, and more.

---

## 7. How rendering works

### `02_scaffolder.md` flow

```
For each *.tmpl file (mandatory + on-demand triggered):
  1. Read template content.
  2. For each {{key}}:
     - If key in metadata_keys → substitute SPEC.json[key] or runtime value (TEMPORAL_NOW, etc.).
     - Else → leave literal (content placeholder).
  3. Atomic write to target path.
  4. Compute sha256, log to tracking/project.json#artifacts_emitted.
```

### Substitution categories

**Metadata (substituted):**
- `{{system_name}}`, `{{system_version}}`, `{{domain}}`, `{{eu_ai_act_risk}}`
- `{{TEMPORAL_NOW}}` — ISO 8601 timestamp
- `{{owner}}`, `{{repo_url}}`
- `{{report_standard_chosen}}`
- `{{auditors_count}}`

**Content (preserved as literal `{{...}}`):**
- `{{abstract_background}}`, `{{abstract_methods}}`, `{{abstract_results}}`, `{{abstract_conclusions}}`
- `{{session_summary}}`, `{{session_kpis}}`, `{{session_decisions}}`
- `{{kpi_duration_actual}}`, `{{kpi_coverage_added}}`, ...
- `{{audit_row_NNN_status}}`, `{{audit_row_NNN_evidence}}`
- `{{adr_NNN_decision}}`, `{{adr_NNN_rationale}}`

The scaffolder distinguishes via a metadata key list embedded in the prompt's `<knowledge_base>`.

---

## 8. Why templates/ exists separate from references/

- **`references/`** — operational rules consumed at runtime. Never copied into the child tree.
- **`templates/`** — file skeletons copied (with substitution) into the child tree once at scaffold.

Updating a reference fixes a rule; updating a template changes what the child tree looks like.

---

## 9. Adding a new template

To add a new artifact to the child tree:

1. Create the template file: `templates/<group>/<name>.tmpl` with placeholders.
2. Register in `system_generator.json#/artifacts.mandatory` or `#/artifacts.on_demand` (with trigger condition for on-demand).
3. If on-demand: add the trigger logic to `02_scaffolder.md`'s knowledge_base.
4. Add a test case to `tests/README.md#T3` to verify it validates against schema.
5. Document in this file (templates-explained.md).
