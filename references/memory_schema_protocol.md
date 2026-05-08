# Memory Schema Protocol · Reference for Phase 4.5 (and inherited child sessions)

> Authoritative protocol for the per-project memory contract negotiated by `prompts/15_memory_schema_architect.md`. The contract becomes the audit subject of the **mandatory** `memory_completeness_auditor` persona inside `prompts/14_adaptive_audit_meta.md`. **Memory is the foundation; the contract is the substrate.**
>
> Generator version: `0.3.0` · Last reviewed: `{{TEMPORAL_NOW}}`

## Why a per-project contract

A generic memory taxonomy ("save what seems relevant") fails three ways:

- **Silent gaps** — important events not memorised; future sessions repeat avoidable work.
- **Noise pollution** — irrelevant events memorised; signal-to-noise drops; recurrence detection mis-fires.
- **Audit blind spots** — without a contract, "what's missing" cannot be defined; the meta-validator can flag drift but not absence.

Negotiating a per-project schema (with HITL ownership) makes the trade-off explicit and auditable. Each domain has different memorable events. The starter library encodes that knowledge; the user steers it to fit their project.

## Layers of memory

The system has two layers, both mandatory:

| Layer | Purpose | Lifecycle |
|---|---|---|
| **Anthropic 4-typed baseline** (`memory/{user, feedback, project, reference}.md` + `MEMORY.md` index) | General persistence: who the user is, feedback, project state, external references | Built by phase 8 (seed_tracking); updated continuously by every phase that produces memorable events |
| **Project-contracted structured modules** (`memory/<module>.{json|jsonl|md}`) | Domain-specific structured events with a calibrated schema and audit rules | Negotiated at phase 4.5; written by phases / tasks per the `trigger`; audited by `memory_completeness_auditor` per task and per session |

The contract complements the baseline; it never replaces it.

## Schema format

The authoritative contract is `memory_schema/manifest.json`. A regenerated mirror lives at `memory_schema/manifest.md`. Per-module schemas live at `memory_schema/modules/<module_name>.json` (one file per module).

### Field flags (4 levels)

| flag | semantics |
|---|---|
| `mandatory` | must be present in every entry; absence is an audit BLOCKER |
| `mandatory_if_<condition>` | conditional mandate (e.g., `mandatory_if_status!=pass`); absence under condition is BLOCKER |
| `recommended` | should be present; absence is a WARNING (not blocker) |
| `optional` | nice-to-have; absence is silent |

### Format options (8 choices · "always pick the best per module")

The architect ALWAYS proposes the format that best fits the module's workload — no blanket choice. Forcing every module into the same format produces silent failure: similarity search without FTS5; precedent traversal without graph; analytics without columnar.

| format | tier | when to choose | soft deps | fallback when dep absent |
|---|---|---|---|---|
| `structured_md`  | A | narrative-plus-fields, git-diffable, ≤500 entries; e.g., `refactor_history`, `hypothesis_log` | none | — |
| `csv`            | A | tabular, spreadsheet-friendly export, ≤10k flat rows | none | — |
| `json`           | A | small index-style; rewrite-each-update; ≤1k entries; e.g., `milestone_checkpoints` | none | — |
| `jsonl`          | A | append-only event log; >1k entries; flat schema; e.g., `test_outcomes`, `decision_logs`, `adverse_events` | none | — |
| `sqlite`         | A | indexed queries · FTS5 similarity · transactions · joins · multi-table; e.g., `transaction_pattern_audits`, `precedent_chains` (≤2-hop) | `sqlite3` (Python stdlib + universal CLI) | — (always available) |
| `parquet`        | B | columnar analytics · large datasets (>100k rows) · batch reads; e.g., per-feature drift archives, longitudinal calibration metrics | `pyarrow` or `fastparquet` | `jsonl` + monthly summary `csv` |
| `vector_db`      | B | semantic similarity search over embeddings · RAG-style memory; e.g., document-similarity dedupe across sessions | `sqlite-vss` ext OR `faiss-cpu` sidecar | `jsonl` + offline embeddings sidecar (degradation documented) |
| `graph_db`       | B | high relationship-density · multi-hop traversal; e.g., legal `precedent_chains` (>2-hop), supply-chain dependency graphs | `kuzu` OR `networkx` (pickled adjacency) | `jsonl` adjacency-list with explicit `source_id`/`target_id`/`edge_type` fields |

**Tier semantics:**
- **Tier A** — runs in any LLM with file-system access; `sqlite` qualifies because the Python stdlib + the `sqlite3` CLI are present on every major OS (already used by `feedback_learning/corrections.db`).
- **Tier B** — recommended for the workload, but the runtime may not have the dep. The architect MUST declare the fallback in `manifest.json#modules[].fallback`. The fallback is then audited as a degraded mode.

### Format selection matrix (workload signals → recommended format)

```
expected_volume_lifetime   query_pattern           relationship_density   recommended       alt_1                  alt_2
< 100                      index lookup            flat                   json              structured_md (≤500)   csv
≤ 500                      human review            flat                   structured_md     json                   csv
> 1k append-only           scan + filter           flat                   jsonl             sqlite (joins)         csv
> 1k                       indexed + similarity    flat or relational     sqlite (FTS5)     jsonl + offline FTS    parquet (analytics)
> 100k                     columnar / OLAP         flat                   parquet           jsonl + summary csv    sqlite
any                        semantic similarity     flat                   vector_db         sqlite + offline emb   jsonl + emb sidecar
any                        multi-hop traversal     high                   graph_db          sqlite (recursive CTE) jsonl adjacency
any                        narrative+fields        flat                   structured_md     sqlite + md sidecar    csv
```

### Audit-rule compatibility per format

```
audit rule                              json  jsonl  csv   md    sqlite  parquet  vector_db  graph_db
field-level mandatory check              ✓     ✓     ✓     ✓     ✓       ✓        ✓          ✓
counting / threshold (missing %)         ~     ✓     ✓     ~     ✓       ✓        ✓          ✓
similarity / dedupe (FTS5-style)         ✗     ✗     ✗     ✗     ✓       ✗        ✓          ✗
multi-table join                         ✗     ✗     ✗     ✗     ✓       ~        ✗          ~
graph traversal (multi-hop)              ✗     ✗     ✗     ✗     ~ CTE   ✗        ✗          ✓
columnar analytics (large)               ✗     ~     ~     ✗     ✓       ✓        ✗          ✗

✓ = native     ~ = via fallback / workaround     ✗ = not supported (re-pick format)
```

If an audit rule cannot run natively in the proposed format, the architect must (a) propose a different format, (b) document the fallback degradation in the manifest, or (c) ask the user to relax the rule.

### Anti-patterns refused at HITL

- `vector_db` for <100 entries (overkill).
- `graph_db` when relationships are flat.
- `parquet` for human-review-primary modules (kills git-diff visibility).
- `json` (single-object) for >1k entries (rewrite cost dominates).
- Six starter modules all picking the same format (red flag — flagged in reflection).
- Module's audit_rule needs FTS5 and format=`jsonl` without an offline FTS sidecar declared.

### Trigger grammar

Triggers are written in plain English; the meta-validator parses pragmatically (regex + LLM check). Examples that the auditor recognises:

- `every test execution` · `every session close` · `every commit` · `every Gate #1 approval`
- `every adverse event` · `every regulatory update detected` · `every hypothesis revision`
- `every error logged with severity >= warn`

### Audit rules (two-tier)

```
audit:
  completeness_rule:    <English invariant for entry-level completeness>
  missing_threshold_pct: <0-100>
  particular_audit:     <English rule for per-process audit, e.g., 'every test execution emits exactly one entry; absence is a finding'>
  global_audit:         <English rule for cross-session audit, e.g., 'monthly: detect entries where related_correction_id is null but error_message matches a corrections.db FTS5 hit'>
```

`missing_threshold_pct` defaults: 5% (balanced); 1% (high-risk); user override supported up to 20% with HITL confirmation.

## Two-tier audit semantics

The mandatory `memory_completeness_auditor` persona inside `prompts/14_adaptive_audit_meta.md` runs both tiers on every task and every session:

| tier | what it checks | when it fires | example finding |
|---|---|---|---|
| **particular** | for the scope at hand (one task or one session), are the contracted fields populated? was the entry written at all? | every adaptive_audit invocation | "Test #14 attempt 2 status=fail but suggested_solution missing → BLOCKER (conf 92%)" |
| **global** | across all sessions, are the contracted modules' missing-thresholds breached? are any modules empty across N sessions? | every adaptive_audit invocation; signals re-negotiation when global trends warrant | "decision_logs.violation_pct = 8% (threshold 5%) → BLOCKER (conf 88%); recommend re-negotiate flag set on `rationale` field" |

Two-tier protects against both immediate omission and long-term drift.

## Per-domain starters (illustrative summaries — full JSON in `templates/memory_schema/per_domain_starters/`)

### `informatics_dev`

- *test_outcomes* (jsonl, mandatory) — the user's anchor example: every test #N attempt #N status / error_code / suggested_solution + confidence%
- *decision_logs* (jsonl, mandatory) — every architectural decision: rationale, alternatives_considered, confidence, related_artifacts
- milestone_checkpoints (json) — current state of key milestones
- refactor_history (structured_md) — what was refactored, why, what didn't break
- performance_baselines (jsonl) — perf measurements per session for regression detection
- dependency_changes (jsonl) — every dep version bump with diff summary

### `healthcare_clinical`

- *patient_cohort_signatures* (jsonl, mandatory; anonymised) — cohort identifiers + sampling fingerprints (no PII)
- *adverse_events* (jsonl, mandatory) — Art. 14 EU AI Act + MDR vigilance trail
- trial_arm_assignments (jsonl) — randomisation lineage
- model_calibration_per_subgroup (json) — calibration metrics by demographic strata
- regulatory_correspondence (structured_md) — letters / queries / responses with regulators

### `fintech`

- *transaction_pattern_audits* (jsonl, mandatory) — sampled audit decisions with rationale
- *regulatory_changes_tracked* (jsonl, mandatory) — DORA / MiCA / PSD3 updates affecting the system
- model_drift_alerts (jsonl) — per-feature drift over time
- fraud_taxonomy_evolution (structured_md) — how the fraud taxonomy changed and why
- counterparty_risk_revisions (json) — updated risk ratings per counterparty

### `legal`

- *case_law_references* (jsonl, mandatory) — every case cited with relevance score
- *regulatory_correspondence* (structured_md, mandatory) — communications with regulators / clients
- precedent_chains (jsonl) — derivation chains for advice given
- jurisdiction_mapping (json) — which laws apply per matter
- client_advisory_history (jsonl) — advice given (with disclaimers) per client

### `public_sector`

- *policy_changes_tracked* (jsonl, mandatory) — every policy update detected
- *citizen_feedback_categories* (jsonl, mandatory) — categorised feedback for service improvement
- compliance_audit_trail (jsonl) — every compliance check with outcome
- service_uptime_incidents (jsonl) — per-incident postmortems

### `research`

- *hypothesis_log* (structured_md, mandatory) — hypotheses with timestamps and revisions
- *experiment_runs* (jsonl, mandatory) — every run with seeds, dataset_version, results
- replication_attempts (jsonl) — internal + external replications
- peer_review_feedback (structured_md) — reviewer comments + responses
- dataset_versioning (jsonl) — dataset hashes + provenance

## Hybrid composition for `domain=other`

When `SystemSpec.domain == "other"`:
- The architect refuses any default starter.
- The user picks 1-2 closest starters; the architect composes a hybrid (intersection of mandatory modules + union of recommended modules); the user iterates.
- The hybrid lineage is recorded in `manifest.json#starter_used` (e.g., `hybrid:informatics_dev+research`).

## Calibration anchors

- Every field flag carries `confidence_pct` (the architect's confidence the flag is correctly assigned).
- Every audit threshold carries `confidence_pct`.
- The negotiation record logs `agent_confidence_pct` on the contract as a whole.
- `memory_completeness_auditor` reports its findings with confidence%; high-confidence findings (≥70%) become BLOCKERs; the BLOCKER blocks the next task until the gap is closed (or the user overrides at HITL).

## Schema evolution

Schemas evolve over project life:

- **Re-negotiation** — child orchestrator may invoke phase 4.5 in `living_update` mode at session boundaries (e.g., after the user adds a new module or removes one no longer used). Lineage preserved in `manifest.json#evolution_log[]`.
- **Migration** — when a field is added or its flag changed, existing entries are validated against the new schema. Existing entries that don't match are flagged (not deleted) and the user decides at HITL whether to fix or grandfather.
- **Versioning** — `manifest.json#schema_version` increments on any structural change (field added/removed, flag changed, threshold changed). Sha256 changes on every change.

## Lifecycle of a contracted module

```
phase 4.5 negotiate → manifest.json + per-module file written
phase 5 scaffold → render templates/memory/structured_module.* per module
runtime (every trigger event) → append entry to <module.path>
adaptive_audit (every task / session end) → memory_completeness_auditor reads manifest + file, audits, surfaces findings
phase 13.5 feedback_session → corrections related to memory may suggest schema changes
phase 13.7 improvement_jury → schema changes audited as proposals before merge
phase 4.5 living_update → re-negotiate based on accumulated learnings
```

## What this protocol does NOT do

- Replace the canonical 4-typed Anthropic memory baseline (always preserved).
- Define library-doc memory (phase 7's domain).
- Define context corpus (phase 1.5's domain — `references/context_confidence_protocol.md`).
- Auto-evolve the schema without HITL approval.

## Versioning of this protocol

Adding a new starter, changing a default threshold, or altering the field-flag semantics requires:

1. A row in `feedback_learning/corrections.db` (`category=memory` or `tooling`).
2. Approval at phase 13.7.
3. A changelog entry in this file's `## Changelog` section.

## Changelog

- `0.3.1` — format taxonomy expanded from 3 to 8 (md / csv / json / jsonl / sqlite / parquet / vector_db / graph_db); per-format portability tier + soft deps + fallback chain; format-selection matrix (workload → recommended + 2 alternatives); audit-rule × format compatibility matrix; anti-patterns explicitly refused.
- `0.3.0` — initial protocol (6 per-domain starters; 4 field flags; 3 format options; two-tier audit; HITL negotiation pattern).
