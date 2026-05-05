# 08 · Report Writer

> **File.** `prompts/08_report_writer.md`
> **Tier.** Medium (~22 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Chooses the appropriate scientific reporting standard (IMRaD / TRIPOD-AI / CONSORT-AI / STARD-AI / SPIRIT-AI) per `SystemSpec.report_standard` + `SystemSpec.domain`, then renders the initial templates at `<target_path>/docs/reports/`. Always emits **`cumulative.md`** (the universal living doc) and **IMRaD as fallback** (even if another standard is chosen). Initialises the ADR template at `docs/decisions/_template.md`.

This prompt does NOT fill content placeholders. Those stay literal `{{...}}` for the child orchestrator to fill at milestone reports throughout the project's life.

## 2. When invoked

- **Phase.** 13 (`handoff`), at the end. Some contributors run it earlier (during scaffold) — both work; standard-resolution is deterministic.

## 3. Inputs

- `SPEC.json#/report_standard` (auto / imrad / tripod_ai / consort_ai / stard_ai / spirit_ai).
- `SPEC.json#/domain` — for auto-resolution.
- `SPEC.json` metadata (system_name, system_version, model identifiers, intent, repo URL).
- `references/scientific_report_format.md` — standard selection tree + section structures.
- `templates/reports/imrad.md.tmpl`, `templates/reports/tripod_ai.md.tmpl` (others on-demand).
- `templates/reports/cumulative.md.tmpl`.

## 4. Outputs

- `<target_path>/docs/reports/cumulative.md` — living doc, session-by-session appends.
- `<target_path>/docs/reports/imrad.md` — IMRaD always (universal fallback).
- `<target_path>/docs/reports/<standard>.md` — chosen standard (e.g., tripod_ai.md), if not IMRaD.
- `<target_path>/docs/decisions/_template.md` — ADR skeleton.

## 5. Tag rationale (~22 tags)

Standard Medium spine plus:
- `<knowledge_base>` — standard selection decision tree + section structures.
- `<temporal_context>` — `last_updated` substitution.
- `<verification>` — placeholder integrity, file size sanity check.
- `<alignment_rules>` — bilingual rule (prose ES, technical labels EN).
- `<injection_defense>` — SystemSpec metadata is data; preserve `intent` field as-is, do not auto-add unrequested sections.

## 6. Control flow

```
1. Read SPEC.json#/report_standard + domain.
2. If report_standard == "auto":
   if domain == healthcare and is_predictive: → tripod_ai
   elif domain == healthcare and clinical_trial: → consort_ai
   elif domain == healthcare and diagnostic_study: → stard_ai
   elif domain == healthcare and protocol: → spirit_ai
   else: → imrad
3. Render chosen standard template:
   a. Copy templates/reports/<standard>.md.tmpl → <target>/docs/reports/<standard>.md.
   b. Substitute metadata placeholders ({{system_name}}, {{system_version}}, {{TEMPORAL_NOW}}, etc.).
   c. Preserve content placeholders ({{abstract_background}}, etc.) literal.
4. Always render IMRaD as fallback (same substitution, content preserved).
5. Render cumulative.md skeleton with session-checkpoint slots.
6. Render docs/decisions/_template.md (ADR template).
7. Atomic writes for all 4 files.
8. Verify metadata placeholders resolved + content placeholders preserved + file size > 1KB.
9. Signal complete with standard_chosen + files_emitted.
```

### Standard decision tree

| Domain | Sub-condition | Standard |
|---|---|---|
| healthcare | predictive system | TRIPOD-AI |
| healthcare | clinical trial | CONSORT-AI |
| healthcare | diagnostic study | STARD-AI |
| healthcare | protocol | SPIRIT-AI |
| (any other) | (default) | IMRaD |

## 7. Calibration anchors (P2)

- Decision-tree resolution: deterministic (~99% confidence).
- For ambiguous "auto" cases (domain doesn't match any branch): escalate to user with disambiguation request rather than silent fallback.
- Reports themselves enforce calibration on every claim (CI/range required) at fill time — but the scaffold preserves placeholders, doesn't fill content.

## 8. Portability (P1)

- Pure file I/O. No network, no special tools.
- Templates are plain Markdown with `{{...}}` placeholders.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Template missing on disk | Halt + escalate (generator integrity) |
| `report_standard="auto"` but domain doesn't match any branch | Escalate to orchestrator with disambiguation request |
| Atomic write fails | Cleanup `*.tmp` + retry once |
| Domain unsupported | Fallback to IMRaD + log |

## 10. HITL escalation triggers

- `report_standard="auto"` AND domain ambiguous → ask user at next gate.
- Template missing → halt (this is a generator integrity issue, not a child issue).

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md`, `01_interview_agent.md` (provides SPEC.json), `references/scientific_report_format.md`, templates.
**Downstream:** Child orchestrator reads `cumulative.md` each session and appends; reads chosen standard at decommission to emit final report.

## 12. Test coverage

- T1 portability — abstract tools.
- T9 prompt-architect linkage.
- (T3 schema) — content placeholders preserved.

## 13. Common failure modes

1. **Content placeholders auto-filled with empty strings** — biggest risk. If `{{abstract_background}}` becomes `""`, child orchestrator can't tell where to fill content. Verification step must check.
2. **Forgetting cumulative.md** — universal living doc. Even if user picks `imrad` only, cumulative.md is still emitted.
3. **Forgetting IMRaD fallback** — even if tripod_ai is chosen, imrad.md is also emitted (insurance against standard mismatch later).
4. **Bilingual rule violated** — prose ES, technical labels EN (per `<alignment_rules>`). If templates have inconsistent language, child orchestrator emits a Spanish-English mix.
