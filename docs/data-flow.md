# Data flow — end-to-end

> Visualises how data moves through the 13 phases of `system-designer`. Each phase reads inputs from declared sources, emits outputs to declared targets, and signals progression through `tracking/project.json`.

## 1. High-level sequence diagram

```mermaid
sequenceDiagram
    participant U as User
    participant SK as SKILL.md
    participant MO as 00_master_orchestrator
    participant IA as 01_interview
    participant SF as 02_scaffolder
    participant PF as 03_prompt_factory
    participant LF as 04_library_docs
    participant ES as 05_error_seeder
    participant EM as 06_eu_act_mapper
    participant AD as 07_audit_designer
    participant RW as 08_report_writer
    participant TJ as 09_three_auditors_jury
    participant FS as Filesystem
    participant PA as prompt_architect

    U->>SK: high-level intent
    SK->>MO: invoke
    MO->>FS: read system_generator.json + references/* + templates/*

    Note over MO,IA: Phase 2 — interview
    MO->>IA: dispatch
    IA->>FS: read wizard/*.json
    loop one question per turn
        IA->>U: ask question + default + confidence
        U-->>IA: answer
        IA->>FS: atomic write SPEC.json (partial)
    end
    IA-->>MO: complete

    Note over MO: Phase 3 — planning_brief
    MO->>FS: write PLAN.md (≥3 alts @ %)

    Note over MO,U: Phase 4 — GATE 1 (HITL)
    MO->>U: render hitl_gate.md (alts + recommendation)
    U-->>MO: decision
    MO->>FS: write tracking/checkpoints/gate1.md

    Note over MO,SF: Phase 5 — scaffold
    MO->>SF: dispatch
    SF->>FS: read templates/**/*.tmpl
    SF->>FS: render full child tree (atomic writes)
    SF->>FS: log sha256 → tracking/project.json
    SF-->>MO: complete

    Note over MO,PF: Phase 6 — compose_prompts
    loop per role
        MO->>PF: compose role
        PF->>PA: invoke prompt_architect(role_spec)
        PA-->>PF: draft prompt
        PF->>PF: 14-rubric audit
        alt audit pass
            PF->>FS: atomic write <child>/prompts/<role>.md
        else audit fail (iter < 3)
            PF->>PA: re-invoke
        else iter == 3
            PF-->>MO: escalate to Gate 2
        end
    end
    PF-->>MO: complete

    Note over MO,LF: Phase 7 — fetch_library_docs
    MO->>LF: dispatch
    loop per library
        LF->>FS: try Context7 → primary → fallback → gh_release_api
        LF->>FS: write <child>/library_docs/<lib>/<ver>/MANIFEST.md
    end
    LF-->>MO: complete (or partial offline)

    Note over MO,ES: Phase 8 — seed_tracking
    MO->>ES: dispatch
    ES->>FS: read references/ai_error_catalog.md
    ES->>FS: write <child>/tracking/errors_catalog.json (30 AIE)
    ES->>FS: write <child>/tracking/errors.md (empty)
    ES-->>MO: complete

    Note over MO,EM: Phase 9 — emit_audit_sheet
    MO->>EM: dispatch
    EM->>FS: read references/eu_ai_act_mapping.md + Checklists/*.xlsx
    EM->>FS: write <child>/audit/eu_ai_act_mapping.md
    EM-->>MO: complete
    MO->>AD: dispatch
    AD->>FS: read mapping + checklists
    AD->>FS: write <child>/audit/audit_sheet.xlsx (or csv+md)
    AD-->>MO: complete + completeness_pct

    Note over MO,TJ: Phase 10 — self_audit
    MO->>PA: 14-rubric audit on every emitted prompt
    MO->>TJ: dispatch (if auditor_mode != none)
    TJ->>PF: compose N auditor prompts
    PF->>PA: per auditor
    par parallel (or sequential fallback)
        TJ->>FS: auditor 1 reads sheet, writes auditor_1_*.md
        TJ->>FS: auditor 2 reads sheet, writes auditor_2_*.md
        TJ->>FS: auditor 3 reads sheet, writes auditor_3_*.md
    end
    TJ->>TJ: jury aggregation
    TJ->>FS: write jury_session_<id>.md (with dissents flagged)
    TJ-->>MO: complete + escalations
    MO->>FS: write <child>/audit/self_audit.md

    Note over MO: Phase 11 — reflection
    MO->>FS: write <child>/audit/reflection_session_0.md

    Note over MO,U: Phase 12 — GATE 2 (HITL)
    MO->>U: render hitl_gate.md (audit summary + dissents)
    U-->>MO: decision
    MO->>FS: write tracking/checkpoints/gate2.md

    Note over MO,RW: Phase 13 — handoff
    MO->>RW: dispatch
    RW->>FS: read SPEC.json + references/scientific_report_format.md
    RW->>FS: write <child>/docs/reports/{cumulative,imrad,<chosen>}.md + ADR template
    RW-->>MO: complete
    MO->>FS: write <child>/HANDOFF.md
    MO-->>U: STOP signal + handoff summary
```

## 2. State persistence per phase

Every phase writes to `tracking/project.json#current_phase` BEFORE returning. This makes the orchestrator resumable: if interrupted at phase N, re-invocation reads `current_phase=N` and resumes.

```
tracking/project.json
├── current_phase: "scaffold"           ← updated by phase 5 before returning
├── current_session_id: "0001"
├── completed_phases: ["read_context", "interview", "planning_brief", "GATE_1_HITL"]
├── gates_status:
│   ├── GATE_1: {status: "approved", timestamp: ...}
│   └── GATE_2: {status: "pending"}
├── artifacts_emitted: [{path, sha256, session_id, rendered_at}, ...]
├── audit_results: []  (filled by phase 10)
├── errors_seen_summary: {}  (updated by child orchestrator over time)
├── kpis_running: {}  (updated by every phase)
├── compliance: {eu_ai_act_risk, additional_regs, ...}
└── configs: {auditor_mode, auditors_count, report_standard, ...}
```

## 3. Atomic-write pattern

Every `fs.write` follows this convention:

```
1. Compute target_path (e.g., "tracking/project.json").
2. Compute tmp_path = target_path + ".tmp".
3. Write content to tmp_path.
4. Atomic rename: tmp_path → target_path.
5. (Optional) compute sha256, log to tracking/project.json#artifacts_emitted.
```

Rationale: a crash between steps 3 and 4 leaves `*.tmp` (cleanable) without corrupting the original. After step 4, the rename is atomic at the OS level — readers see either the old or the new content, never a half-written file.

## 4. HITL gate data flow

```
Phase reaches gate
  ↓
Render templates/hitl_gate.md.tmpl with:
  - alternatives [A, B, C, ...]
  - fit% per alternative (sum to 100)
  - pros / cons per alternative
  - recommendation + confidence%
  - rationale
  ↓
Present to user (LLM-runtime-specific output)
  ↓
Wait for user decision (block; no auto-skip ever)
  ↓
On decision:
  - parse letter or free-form text
  - if free-form: classify into existing alt or treat as [D]
  - log to tracking/checkpoints/gate<N>.md (atomic write)
  - log to tracking/decisions.md as ADR
  - update tracking/project.json#gates_status[GATE_N]
  ↓
Continue to next phase OR loop back if user rejected
```

## 5. Resumability flow

```
On invocation:
  1. Read SKILL.md → route to 00_master_orchestrator.md.
  2. Master orchestrator: try to read <target>/tracking/project.json.
     a. If absent → fresh start at phase 1.
     b. If present → read current_phase, completed_phases.
        - Validate state (sha256 of artifacts_emitted matches files on disk).
        - If validation passes → resume at current_phase.
        - If validation fails → halt + escalate (potential corruption).
```

## 6. Library doc fetch ladder (phase 7 detail)

```
For each library in SPEC.json#/stack:
  ┌─────────────────────────────────────────────┐
  │ Try Context7 MCP                            │
  │ mcp__context7__get_library_docs(name, ver)  │
  └────────────────────┬────────────────────────┘
                       │ fail
                       ↓
  ┌─────────────────────────────────────────────┐
  │ Try primary URL (from manifest)             │
  │ fetch(primary_url)                          │
  └────────────────────┬────────────────────────┘
                       │ fail
                       ↓
  ┌─────────────────────────────────────────────┐
  │ Try fallback URL (from manifest)            │
  │ fetch(fallback_url)                         │
  └────────────────────┬────────────────────────┘
                       │ fail
                       ↓
  ┌─────────────────────────────────────────────┐
  │ Try github_release_api (from manifest)      │
  │ fetch(api.github.com/.../releases/tags/v?)  │
  └────────────────────┬────────────────────────┘
                       │ fail
                       ↓
  ┌─────────────────────────────────────────────┐
  │ Write OFFLINE.md + log fallback             │
  │ Continue with reduced confidence            │
  └─────────────────────────────────────────────┘
```

## 7. Audit sheet write fallback ladder (phase 9 detail)

```
Try xlsx.write(path, sheets) ───────────► xlsx emitted, done
            │ unavailable
            ↓
Try csv.write(path, rows) + render sidecar .md ───► csv+md emitted, log fallback
            │ unavailable
            ↓
Try fs.write(path, json) ──────────────────► json-only, log severe portability issue, escalate
```

## 8. Auditor parallelism flow (phase 10 detail)

```
N = SystemSpec.auditors_count (default 3)
mode = SystemSpec.auditor_mode

if mode == "parallel" and parallel.spawn available:
  spawn N auditors concurrently:
    auditor_i reads audit_sheet (read-only)
    auditor_i writes audit/audits/auditor_<i>_*.md
    (auditors are blind to each other)
  wait_all

elif mode == "sequential" or parallel.spawn unavailable:
  for i in 1..N:
    auditor_i reads audit_sheet (read-only)
    auditor_i writes audit/audits/auditor_<i>_*.md
    (still blind: each only reads sheet, never others' outputs)

# All N auditor outputs ready
jury reads all N outputs
jury computes agreement matrix per row
jury flags dissents + low_confidence_consensus
jury writes audit/audits/jury_session_<id>.md

# escalations
for each row with dissent or low_confidence_consensus:
  add to escalations list
  escalations surface at Gate #2
```

## 9. KPI update flow

Every phase that finishes updates `tracking/kpis.json` and `tracking/project.json#kpis_running`:

```
On phase completion:
  duration_actual_min = now() - phase_started_at
  files_modified_count += <files_emitted_this_phase>
  tokens_consumed_estimate.range[1] += <upper_estimate>
  agent_self_confidence_pct = <self-reported>

  if errors encountered: errors_count += 1; errors_by_severity[sev] += 1
  if HITL: hitl_decisions_count += 1
  if rollback: rollbacks_count += 1
  if calibration violation detected: calibration_violations += 1
  if portability violation detected: portability_violations += 1

  atomic write tracking/kpis.json + tracking/project.json
```

## 10. End-to-end data lineage

Each child tree artifact has provenance traceable back to its source:

| Artifact | Sources | Phase |
|---|---|---|
| `<child>/SPEC.json` | user answers, `wizard/*.json` defaults | 2 |
| `<child>/PLAN.md` | `SPEC.json`, `references/*` | 3 |
| `<child>/CLAUDE.md` | `templates/CLAUDE.md.tmpl` + `SPEC.json` | 5 |
| `<child>/prompts/*.md` | `prompt_architect/SKILL.md` + role spec | 6 |
| `<child>/library_docs/*` | Context7 / primary / fallback / gh_release_api | 7 |
| `<child>/tracking/errors_catalog.json` | `references/ai_error_catalog.md` | 8 |
| `<child>/audit/eu_ai_act_mapping.md` | `references/eu_ai_act_mapping.md` + `SPEC.json` | 9 |
| `<child>/audit/audit_sheet.xlsx` | `Checklists y ejemplos/*.xlsx` + mapping doc | 9 |
| `<child>/docs/reports/*` | `references/scientific_report_format.md` + `templates/reports/*.tmpl` | 13 |
| `<child>/HANDOFF.md` | aggregation of all phases | 13 |

The sha256 of every emitted file is logged in `tracking/project.json#artifacts_emitted`, giving end-to-end reproducibility.
