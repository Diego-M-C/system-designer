# references/ — section-by-section walkthrough

> The `references/` directory holds the **operational rules** that every emitted prompt must respect. These are not documentation of the system's behaviour — they are the **inputs** the prompts read at runtime.

| File | Purpose | Consumed by |
|---|---|---|
| `calibrated_probabilities.md` | P2 enforcement rules | All Complex prompts (alignment_rules), `tests/run_all.sh#T2` |
| `portable_invocation.md` | P1 enforcement rules + per-LLM tooling | Master orchestrator, every prompt's `<tool_selection>` |
| `ai_error_catalog.md` | 30 AIE-NNN preloaded patterns | `05_error_prevention_seeder.md` |
| `eu_ai_act_mapping.md` | 13-checklist → 13-Article master mapping | `06_eu_ai_act_mapper.md` |
| `scientific_report_format.md` | Standard selection tree + section structures | `08_report_writer.md` |

---

## 1. `calibrated_probabilities.md` (P2 rules)

### Sections

1. **Forbidden tokens (7)** — `best, always, never, guaranteed, certain, definitely, impossible`. Any user-facing or child-emitted text containing these is rejected.
2. **Required formats per output type (8)** — Estimates, predictions, alternatives, KPIs, fits, durations, coverage, recommendations all have specific calibration shapes.
3. **Confidence thresholds (4)** — 90–99% / 70–89% / 50–69% / <50% map to behaviours: proceed silently, log, surface in reflection, escalate to HITL.
4. **Anti-overconfidence heuristics** — When in doubt, lower the confidence by 10%.
5. **Citation patterns** — Every claim ≥80% confidence cites a source.
6. **Examples (4 correct / 4 incorrect)** — Concrete cases.

### Why it matters

Without P2, the system would produce confident-but-wrong outputs (the canonical AI failure mode). P2 forces uncertainty to be visible, which makes errors recoverable and gives humans real decisions at HITL gates.

### Key rules

- **Alternatives sum to 100%** (or are explicitly noted as non-exclusive).
- **Estimates carry confidence_pct or range[lo, hi]**.
- **Recommendations include the rationale** (why this option, what's lost).
- **Refuse to commit on <50% confidence** — surface ambiguity instead.

### How prompts consume it

Every Complex prompt's `<alignment_rules>` block contains a line like:

> P2 calibration — see `references/calibrated_probabilities.md`. Forbidden tokens rejected; estimates carry confidence%.

`tests/run_all.sh#T2` validates that the rules are actually applied (no forbidden tokens leak into emissions).

---

## 2. `portable_invocation.md` (P1 rules)

### Sections

1. **Abstract tool contract** — `fs.read`, `fs.write` (atomic), `fetch`, `now`, `prompt_architect`, optional `xlsx.write`, optional `context7.fetch`, optional `parallel.spawn`.
2. **Per-platform notes** — Claude Code, Cursor, Cline, Gemini CLI, Copilot CLI, Codex, plain LLM.
3. **Drag-folder pattern** — How the user invokes on each platform.
4. **6-entry fallback hierarchy** — Tier A degradation order.
5. **Portability self-test regex** — Forbidden token list.
6. **Tier A vs Tier B** — Distinction and impact.

### Why it matters

Without P1, the system would only run on Claude Code. The whole point of being a meta-skill is to be droppable into any LLM with file-system access.

### Per-platform mapping table

| Abstract | Claude Code | Cursor | Cline | Gemini CLI | Copilot CLI | Codex |
|---|---|---|---|---|---|---|
| `fs.read` | `Read` | `read_file` | `read_file` | builtin | builtin | builtin |
| `fs.write` | `Write` | `write_file` | `write_file` | builtin | builtin | builtin |
| `fetch` | `WebFetch` | `web_fetch` | `browser_action` | `fetch` | builtin | builtin |
| `now` | `Bash date` | builtin | builtin | builtin | builtin | builtin |
| `prompt_architect` | nested skill | manual | manual | activate_skill | `skill` tool | manual |
| `xlsx.write` (opt) | none → CSV+MD | optional MCP | none | none | none | none |
| `context7.fetch` (opt) | MCP | none | none | none | none | none |
| `parallel.spawn` (opt) | `Agent` bg | seq | seq | seq | seq | seq |

### Tier definitions

- **Tier A** — full automation, no manual paste. 6 platforms supported.
- **Tier B** — manual file presentation needed. Plain ChatGPT / Claude.ai web.

### How prompts consume it

Every prompt's `<tools>` lists abstract names. `<tool_selection>` may include conditional logic per platform. The master orchestrator probes the platform at phase 1 (`read_context`) and picks the right concrete tool.

---

## 3. `ai_error_catalog.md` (30 AIE patterns)

### Structure

```markdown
### AIE-001 · Hallucinated function signature
Category: hallucination
Severity: high
Description: ...
Example: ...
Prevention: Always read library_docs/<lib>/<version>/api_index.json before referencing.
Auto-detection: regex on function calls vs api_index.json
```

### 6 categories

1. **hallucination** (e.g., AIE-001 hallucinated API, AIE-002 fabricated dependency)
2. **concurrency** (e.g., AIE-009 race condition in async, AIE-010 missing await)
3. **security** (e.g., AIE-013 SQL injection, AIE-014 hardcoded secret, AIE-015 XSS)
4. **logic** (e.g., AIE-019 off-by-one, AIE-020 inverted condition)
5. **reliability** (e.g., AIE-024 silent retry storm, AIE-025 missing timeout)
6. **prompt_engineering** (e.g., AIE-028 instruction leakage, AIE-029 token-budget overrun, AIE-030 forbidden P2 token)

### Auto-extension protocol

Once seeded, the child orchestrator extends the catalog as new patterns are observed. Each new entry gets `AIE-NNN` (next available), `preloaded: false`, `first_seen_session: <id>`.

### How prompts consume it

`05_error_prevention_seeder.md` reads this file and emits `<target>/tracking/errors_catalog.json` with all 30 entries. The child orchestrator's `AUDIT_ROW_APPEND` step matches observed errors against `auto_detection` patterns.

### Why exactly 30

Calibrated tradeoff: enough to cover the major categories (~85% of common AI-coding failures by frequency in observed sessions), few enough to keep the catalog maintainable. Auto-extension allows organic growth.

---

## 4. `eu_ai_act_mapping.md` (13 checklists → 13 Articles)

### Structure

1. **Risk classification** — prohibited / high / limited / minimal with definitions.
2. **13 checklists table** — checklist file → Article → area → min_rows per risk class.
3. **Article → audit-sheet mapping algorithm** — for `07_audit_designer.md` to follow.
4. **Auditor configuration** — persona library (10 personas) + recommended trios.
5. **Living-doc rhythm** — how the audit sheet evolves session by session.
6. **Cross-regulation table** — domain → additional regulations (GDPR/MDR/DORA/ISO 42001/...).

### The 13 mappings

| Checklist file | Article | Area | min_rows (high) |
|---|---|---|---|
| 01 Riesgos AI ACT.xlsx | Art. 9 | risk management | 12 |
| 02 Datos AI ACT.xlsx | Art. 10 | data governance | 10 |
| 03 Documentación AI ACT.xlsx | Art. 11 | technical documentation | 8 |
| 04 Mantenimiento AI ACT.xlsx | Art. 12 | record-keeping | 8 |
| 05 Transparencia AI ACT.xlsx | Art. 13 | transparency to users | 6 |
| 06 Supervisión Humana AI ACT.xlsx | Art. 14 | human oversight | 8 |
| 07 Precisión Robustez AI ACT.xlsx | Art. 15a/b | accuracy + robustness | 12 |
| 08 Ciberseguridad AI ACT.xlsx | Art. 15c | cybersecurity | 10 |
| 09 Calidad AI ACT.xlsx | Art. 17 | QMS | 12 |
| 10 Transparencia Públicos AI ACT.xlsx | Art. 50 | transparency to public | 6 |
| 11 Seguimiento AI ACT.xlsx | Art. 72 | post-market monitoring | 10 |
| 12 Incidentes AI ACT.xlsx | Art. 73 | serious incident reporting | 10 |

Total floor for high-risk: ≥112 rows.

### Cross-regulations

| Domain | Regulations |
|---|---|
| healthcare | GDPR + MDR 2017/745 + ISO 13485 + ISO 42001 |
| fintech | GDPR + DORA 2022/2554 + PSD2/PSD3 + ISO 42001 |
| legal / public_sector | GDPR + ISO 42001 + national e-gov |
| research | GDPR (if personal data) + Helsinki (if human subjects) |

### How prompts consume it

`06_eu_ai_act_mapper.md` reads this master and instantiates a child-specific version at `<target>/audit/eu_ai_act_mapping.md`. `07_audit_designer.md` reads the child mapping to know which checklists to extract rows from.

---

## 5. `scientific_report_format.md` (5 standards)

### Sections

1. **Standard selection decision tree** — domain + sub-condition → standard.
2. **IMRaD** (universal fallback) — full section structure.
3. **TRIPOD-AI** (predictive systems) — 33-item checklist with AI/ML-specific additions.
4. **CONSORT-AI** (clinical trials of AI) — overview.
5. **STARD-AI** (diagnostic studies) — overview.
6. **SPIRIT-AI** (protocols) — overview.
7. **Calibration rules** — every claim has CI/range.
8. **Reproducibility statement** — required content (random seeds, env, etc.).
9. **Cumulative vs final cadence** — when to update each.
10. **Quality gate** — pre-submission checklist.

### Decision tree

```
domain == healthcare:
  ├── predictive system → TRIPOD-AI
  ├── clinical trial → CONSORT-AI
  ├── diagnostic study → STARD-AI
  └── protocol → SPIRIT-AI
else: → IMRaD
```

### How prompts consume it

`08_report_writer.md` reads this and applies the tree to `SystemSpec.domain` + `SystemSpec.report_standard` (with `auto` triggering the tree).

---

## 6. Why references/ exists separate from prompts/

A common alternative is to inline these rules in every prompt. That fails for two reasons:

1. **Drift.** Updating "forbidden tokens" in 10 prompts is a recipe for inconsistency. Single source of truth.
2. **Auditability.** Reviewers can read `references/` standalone to understand the rule system. Prompts cite the references — they don't replace them.

The cost is one extra `fs.read` per prompt at runtime. Acceptable.

## 7. What goes in references/ vs templates/

- **`references/`** — operational rules + master data. Read at runtime, never copied.
- **`templates/`** — file skeletons rendered into the child tree. Read once at scaffold time, copied (with substitutions).

Test: if you'd update the file in a future PR to fix a rule, it goes in `references/`. If you'd update it to add a section in the child tree, it goes in `templates/`.
