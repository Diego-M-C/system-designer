# 02 · Scaffolder

> **File.** `prompts/02_scaffolder.md`
> **Tier.** Medium (~20 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Renders the full child-system tree from `templates/**/*.tmpl` into `<target_path>/<system_name>/`. Substitutes metadata placeholders, **preserves content placeholders** (literal `{{...}}` for child orchestrator to fill), writes atomically, computes sha256 per artifact for `tracking/project.json#artifacts_emitted`.

This is the only prompt that creates the directory structure. After it runs, every other specialist writes into already-existing folders.

## 2. When invoked

- **Phase.** 5 (`scaffold`), after Gate #1 approved.

## 3. Inputs

- `<target_path>/SPEC.json` — for metadata substitution (system_name, domain, risk_class, etc.).
- `templates/**/*.tmpl` — all skeleton files.
- `system_generator.json#/artifacts.mandatory` and `#/artifacts.on_demand` — what to render.

## 4. Outputs

The full child tree:

```
<system_name>/
├── CLAUDE.md
├── README.md
├── SPEC.md
├── SPEC.json (already exists; verified)
├── ARCHITECTURE.md
├── HANDOFF.md
├── prompts/                    (empty; populated by 03_prompt_factory)
├── library_docs/               (empty; populated by 04_library_docs_fetcher)
├── tracking/
│   ├── project.json            (initial state)
│   ├── project.md              (mirror)
│   ├── kpis.json               (11 KPIs initialized)
│   ├── sessions/               (empty; child orchestrator populates)
│   ├── decisions.md            (ADR template)
│   ├── errors.md               (empty narrative)
│   └── errors_catalog.json     (placeholder; 05_error_prevention_seeder fills)
├── memory/
│   ├── MEMORY.md
│   ├── user.md
│   ├── project.md
│   ├── feedback.md
│   └── reference.md
├── audit/
│   ├── eu_ai_act_mapping.md    (placeholder; 06 fills)
│   ├── audit_sheet.xlsx        (placeholder; 07 fills)
│   ├── self_audit.md           (template)
│   ├── reflection_session_0.md (template)
│   └── assumptions.md
└── docs/
    ├── reports/
    │   ├── cumulative.md       (08 fills)
    │   ├── imrad.md            (08 fills)
    │   └── <chosen>.md         (08 fills)
    └── decisions/
        └── _template.md
```

Plus: `tracking/project.json#artifacts_emitted[]` — list of `{path, sha256, session_id, rendered_at}` for every file emitted.

## 5. Tag rationale (~20 tags)

Standard Medium spine plus:
- `<temporal_context>` — `{{TEMPORAL_NOW}}` substituted into headers.
- `<verification>` — read-back sha256 after each write.
- `<fallback>` — partial-emit recovery (resume-from-tracking-log).

## 6. Control flow

```
1. Read SPEC.json → metadata for substitution.
2. Read system_generator.json#/artifacts → list (mandatory + on_demand evaluation).
3. For each artifact:
   a. Evaluate "should emit?":
      - mandatory → yes
      - on_demand → check trigger condition against SPEC.json
   b. If yes:
      i. Read template tmpl.
      ii. Substitute metadata placeholders ({{system_name}}, {{TEMPORAL_NOW}}, etc.).
      iii. PRESERVE content placeholders ({{abstract_background}}, {{session_summary}}) — leave literal.
      iv. Atomic write: target.tmp → target.
      v. Compute sha256.
      vi. Append entry to tracking/project.json#artifacts_emitted.
4. After all rendered:
   - Verify tree completeness against artifacts list.
   - Signal complete with stats.
```

### On-demand evaluation logic

Per `system_generator.json#/artifacts.on_demand[].trigger`:

```python
# pseudo-code
if artifact.id == "static_dashboard":
    emit if SPEC.json["dashboard_required"] == True
elif artifact.id == "tripod_ai_report":
    emit if SPEC.json["report_standard"] in ("tripod_ai", "auto") and SPEC.json["domain"] == "healthcare"
elif artifact.id == "consort_ai_report":
    emit if SPEC.json["report_type"] == "clinical_trial"
# ... etc
```

## 7. Calibration anchors (P2)

- The scaffolder itself doesn't make calibrated estimates (it executes deterministic rendering), but every template it renders contains calibrated fields the child orchestrator will fill (e.g., `confidence_pct` placeholders in tracking/decisions.md).
- `verification` step: count of artifacts emitted vs expected (deterministic, not probabilistic).

## 8. Portability (P1)

- Pure file I/O: `fs.read`, `fs.write` (atomic), `now()`. No network, no proprietary APIs.
- Template format is plain-text with `{{...}}` placeholders — works in any LLM.
- Atomic write pattern documented for every file.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Template file missing | Escalate (generator integrity) |
| SPEC.json field missing for mandatory placeholder | Escalate with diagnostic (which field, which template) |
| Atomic write fails | Cleanup `*.tmp` + retry once → escalate |
| Partial emit (orchestrator crashed mid-scaffold) | Resume from `tracking/project.json#artifacts_emitted` (skip already-emitted) |
| sha256 mismatch on read-back | Halt + escalate (filesystem corruption suspected) |

## 10. HITL escalation triggers

- Mandatory placeholder unresolved → escalate (do NOT emit malformed file).
- Tree depth/complexity exceeds expected (sanity check >100 files) → log warning + proceed.

## 11. Dependency edges

**Upstream:** `01_interview_agent.md` (provides SPEC.json), `00_master_orchestrator.md` (dispatches).
**Downstream:** `03_prompt_factory.md` (fills `prompts/`), `04_library_docs_fetcher.md` (fills `library_docs/`), `05..09_*` (fill various tracking/ and audit/ files).

## 12. Test coverage

- T1 portability — uses only abstract tools.
- T8 atomic-write pattern — explicitly documented.
- T9 prompt-architect linkage — declared in frontmatter.

## 13. Common failure modes

1. **Content placeholders overwritten with empty strings** — preserving `{{abstract_background}}` literally is critical. If the agent "helpfully" renders empty, the child orchestrator can't tell where to fill content.
2. **Partial substitution** — if a metadata placeholder is missed, the file ships with `{{system_name}}` literally in headings. Verification step (read-back regex) catches this.
3. **Forgetting on-demand evaluation** — emitting a tripod_ai.md template for a non-healthcare project pollutes the tree with unused files. Trigger logic must be respected.
4. **sha256 not logged** — `tracking/project.json#artifacts_emitted` must record sha256; reproducibility depends on it.
