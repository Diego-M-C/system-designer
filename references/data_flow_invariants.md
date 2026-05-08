# Data Flow Invariants · Reference for Phase 11.5

> Authoritative list of invariants the structural-consistency validators check at phase 11.5 (`prompts/10_data_flow_validator.md`). Each invariant has: a unique id, an English statement, the validator persona that owns it, and the calibrated confidence floor for raising a finding.
>
> Generator version: `0.2.0` · Last reviewed: `{{TEMPORAL_NOW}}`

## Numbering convention

Invariant IDs follow the pattern `INV-<persona>-<NNN>` where `<persona>` is the lowercase short slug of the owning validator persona.

## Invariant catalog

### data_lineage_auditor

| id | invariant | confidence floor for finding |
|---|---|---:|
| `INV-LIN-001` | Every entry in `tracking/project.json#artifacts_emitted[]` has `path`, `sha256`, `phase`, `session_id`, `rendered_at`. | 80 |
| `INV-LIN-002` | Every consumer's `<context>` block references at least one path that appears as a producer in `artifacts_emitted[]`. | 75 |
| `INV-LIN-003` | Snapshots (`data_flow_validation/sequence_snapshots/`) match disk state by sha256 (no orphan files; no missing files). | 85 |
| `INV-LIN-004` | `tracking/sessions/<id>/observations.jsonl` has one entry per write listed in `artifacts_emitted[]`. | 70 |

### memory_consistency_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-MEM-001` | `memory/MEMORY.md` index contains exactly one entry per non-index file under `memory/*.md`. | 85 |
| `INV-MEM-002` | Every memory entry has frontmatter with `name`, `description`, `type` ∈ {user, feedback, project, reference}. | 85 |
| `INV-MEM-003` | No memory file exceeds 200 lines (long memories are unstable; should be split). | 60 |
| `INV-MEM-004` | Memory entries created by phase 13.5 carry `source: feedback_learning` and a `correction_id` linking back to `corrections.db`. | 70 |

### intercom_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-COM-001` | Every `<delegation>` target prompt path resolves to an existing file. | 90 |
| `INV-COM-002` | Every tool referenced in `<tools>` is declared in `system_generator.json#/dependencies` (hard or soft). | 80 |
| `INV-COM-003` | Every fallback in `<fallback>` matches a declared soft dependency or a documented capability. | 75 |
| `INV-COM-004` | Cross-prompt references (e.g., "see prompts/04_…") resolve to existing files. | 90 |

### schema_integrity_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-SCH-001` | `tracking/project.json` validates against `templates/tracking/project.json.tmpl` schema. | 85 |
| `INV-SCH-002` | `tracking/kpis.json` includes the 11 mandatory Bloque B-6 KPIs. | 80 |
| `INV-SCH-003` | `tracking/errors_catalog.json` has ≥30 AIE entries and every entry conforms to its schema. | 85 |
| `INV-SCH-004` | `feedback_learning/corrections.db` schema matches `templates/feedback_learning/corrections_schema.sql.tmpl`. | 80 |
| `INV-SCH-005` | `audit/eu_ai_act_mapping.md` references ≥13 checklist files (one per area). | 80 |

### simulation_agent (mandatory)

The simulation agent runs the 5 scenarios in `prompts/10_data_flow_validator.md#simulation_scenarios`. It does not own atomic invariants but emits a pass/fail per scenario with confidence%.

### lifecycle_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-LIF-001` | No `*.tmp` files committed under `<target_path>/`. | 95 |
| `INV-LIF-002` | sha256 chain in `artifacts_emitted[]` is internally consistent (no recomputed hash mismatches). | 80 |
| `INV-LIF-003` | Atomic-write pattern observable: every write in `observations.jsonl` references both a `tmp_path` and a `final_path`. | 70 |
| `INV-LIF-004` *(v0.4.0)* | **Tamper-evident sha256 chain** (`prior_hash` field): every entry N (N≥2) in `tracking/sessions/<id>/observations.jsonl` carries `prior_hash = sha256(entry[N-1])`; every ADR row in `tracking/decisions.md` carries `prior_hash = sha256(prior ADR row's serialized form)`. Entry 1 of a fresh session uses the literal string `"genesis"`. The chain enables tamper-evident audit trails (Art. 12 evidence chain). T23 in `tests/run_all.sh` validates a synthetic chain. | 90 |

### calibration_consistency_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-CAL-001` | Zero forbidden tokens (`best`, `always`, `never`, `guaranteed`, `certain`, `definitely`, `impossible`) in user-facing artifacts (excluding documented forbidden-list contexts). | 85 |
| `INV-CAL-002` | Every numeric estimate, KPI target, plan alternative carries a confidence % or range. | 80 |
| `INV-CAL-003` | Calibration drift vs. phase-10 baseline is ≤5% (post-improvements regressions caught). | 70 |

### portability_consistency_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-POR-001` | Zero Claude-Code-only identifiers (`mcp__`, `Skill\(`, `SubagentType`, `TodoWrite`) outside `tests/`. | 85 |
| `INV-POR-002` | Every soft dependency has a documented fallback. | 80 |
| `INV-POR-003` | Tool descriptions are abstract (e.g., `fs.read`, `fetch`, `now`) rather than runtime-specific. | 80 |

### error_catalog_drift_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-ERR-001` | `tracking/errors_catalog.json` count ≥ 30 (seeded baseline). | 95 |
| `INV-ERR-002` | New entries since baseline have `id`, `pattern`, `mitigation`, `discovered_in_session`. | 80 |
| `INV-ERR-003` | Every `AIE-*` referenced in `errors.jsonl` exists in `errors_catalog.json`. | 80 |

### eu_act_traceability_auditor

| id | invariant | confidence floor |
|---|---|---:|
| `INV-EUA-001` | Every Annex III applicable Article maps to ≥1 row in `audit/audit_sheet.xlsx`. | 85 |
| `INV-EUA-002` | Every audit row's `evidence_link` points to an existing artifact OR is explicitly `pending`. | 75 |
| `INV-EUA-003` | Mapping completeness ≥95% for `eu_ai_act_risk = high` (or downgrade documented in `decisions.md`). | 80 |

## Confidence floor rationale

A validator may surface findings below its confidence floor as `pending` rather than `fail`. The consolidator at phase 11.5 weights them differently in the score derivation (only ≥70% findings deduct from `consistency_score`).

## Versioning

Invariants are appended over time. Removing or renumbering an invariant requires:
1. A row in `feedback_learning/corrections.db` (`category=tooling`).
2. Approval at phase 13.7.
3. A changelog entry in this file's `## Changelog` section.

## Changelog

- `0.2.0` — initial catalog (≈30 invariants across 9 personas + simulation_agent).
