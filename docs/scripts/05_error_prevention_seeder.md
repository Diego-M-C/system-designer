# 05 · Error Prevention Seeder

> **File.** `prompts/05_error_prevention_seeder.md`
> **Tier.** Simple (~12 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Seeds the child system's error catalog with **30 preloaded AIE-NNN entries** drawn from `references/ai_error_catalog.md`. After this phase, the child orchestrator has a ready-made catalog of common AI-coding pitfalls (hallucination, concurrency, security, logic, reliability, prompt_engineering) and an auto-extension protocol for new patterns observed during sessions.

## 2. When invoked

- **Phase.** 8 (`seed_tracking`).

## 3. Inputs

- `references/ai_error_catalog.md` — master catalog (30 entries).
- `templates/tracking/errors_catalog.json.tmpl` — JSON skeleton with all 30 entries hardcoded for fast-path.
- `templates/tracking/errors.md.tmpl` — empty narrative shell.

## 4. Outputs

- `<target_path>/tracking/errors_catalog.json` — 30 AIE entries, each with: id, name, category, severity, description, example, prevention, auto_detection, occurrences=0, first_seen_session=null, preloaded=true.
- `<target_path>/tracking/errors.md` — empty narrative ready for child orchestrator to append ERR-NNN entries on first occurrence.

## 5. Tag rationale (~12 tags)

Simple-tier minimum: `<role>`, `<task>`, `<context>`, `<input>`, `<constraints>`, `<verification>`, `<tools>`, `<output>`, `<stop_condition>`, `<test_cases>`, `<version>`, `<metadata>`. Plus `<non_do_conditions>` and `<guardrails>` for safety.

## 6. Control flow

```
1. Read references/ai_error_catalog.md → parse 30 ### AIE-NNN blocks.
2. Read templates/tracking/errors_catalog.json.tmpl (preloaded with 30).
3. Verify count == 30 in both → if drift, halt + escalate.
4. Substitute system_name in template header.
5. Atomic write → <target>/tracking/errors_catalog.json.
6. Atomic write → <target>/tracking/errors.md (empty shell).
7. Read-back verify: count == 30; every entry validates against ErrorCatalogEntry schema.
8. Signal complete.
```

## 7. Calibration anchors (P2)

- Each AIE entry carries: severity (low/med/high/critical) + auto_detection feasibility (deterministic / heuristic / unfeasible) — both calibrated.
- The 30 entries themselves were calibrated at catalog-design time; the seeder doesn't add calibration.

## 8. Portability (P1)

- Pure file I/O. No network. No proprietary tools.
- Atomic writes for both output files.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Master catalog count != 30 | Halt + escalate (catalog drift; fix at generator level) |
| Schema validation fails on any entry | Halt + escalate |
| Atomic write fails | Cleanup `*.tmp` + retry once |

## 10. HITL escalation triggers

- Catalog drift (≠30) → halt and escalate to fix the master catalog before proceeding.

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md`, `references/ai_error_catalog.md` (master), `templates/tracking/errors_catalog.json.tmpl` (preloaded JSON).
**Downstream:** Child orchestrator's `AUDIT_ROW_APPEND` step writes to these files when AIE patterns are observed; auto-extension protocol adds new AIE-NNN entries beyond 30 over time.

## 12. Test coverage

- T6 error catalog count == 30 in both files (markdown + JSON).
- T1 portability — abstract tools.

## 13. Common failure modes

1. **Drift between md and json** — if a contributor adds AIE-031 to references/ai_error_catalog.md but forgets templates/tracking/errors_catalog.json.tmpl (or vice versa), T6 catches it.
2. **`preloaded: true` flag dropped** — distinguishing preloaded vs auto-extended entries is important for catalog stats. Verification step must check.
3. **`occurrences: 0` overridden** — if the seeder reads a previously-populated catalog, it must NOT reset occurrences. Resumability case.
