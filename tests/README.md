# system-designer · self-validation suite

> **Purpose.** This suite validates the **generator itself** before any push or release. It is **prompt-driven** (any LLM can run it), with optional `bash` snippets for fast local execution.
>
> **Scope.** It does NOT validate generated child systems (those have their own `audit/self_audit.md`). It validates `system-designer/` integrity: portability, calibration, schemas, prompt-floor compliance, library-manifest sanity, AIE catalog count, EU AI Act mapping, atomic-write convention.

## How to run

### Prompt-driven (any LLM, Tier A)

Open the LLM in this folder and say:

```
Read tests/README.md and run the entire suite. Report each test as
PASS / FAIL / SKIP with calibrated confidence and a one-line rationale.
Halt on any FAIL marked critical=true.
```

### Bash-driven (local, fast)

```bash
bash tests/run_all.sh
```

Exit code: `0` = all critical tests pass; `1` = at least one critical test failed.

### Per-test invocation

```
Run test T3 only and report.
```

## Tests overview

| ID  | Name                       | Critical? | Method                    |
|-----|----------------------------|-----------|---------------------------|
| T1  | Portability scan           | yes       | regex over `prompts/`, `templates/`, `references/` |
| T2  | Calibration scan           | yes       | regex over `references/`, `templates/`, `prompts/`  |
| T3  | Schema validation          | yes       | structural inspection of `templates/tracking/*.json.tmpl` |
| T4  | Prompt-tag floor           | yes       | tag count + presence check on `prompts/*.md`        |
| T5  | Library manifest URLs      | no        | each entry has `primary` + `fallback`               |
| T6  | Error catalog count = 30   | yes       | match between `references/ai_error_catalog.md` + `templates/tracking/errors_catalog.json.tmpl` |
| T7  | EU AI Act mapping          | yes       | `references/eu_ai_act_mapping.md` lists 13 checklists; min_rows sum ≥112 (high-risk) |
| T8  | Atomic-write pattern       | no        | every `fs.write` example uses `*.tmp` + rename      |
| T9  | Prompt-architect linkage   | yes       | every `prompts/*.md` references prompt-architect via Factory or P4 alignment rule |
| T10 | HITL gates non-skip rule   | yes       | every prompt mentioning a gate forbids auto-skip    |

## Test specifications

Each test below tells the LLM (or human) exactly what to check, what counts as PASS/FAIL, and what error message to emit.

---

### T1 · Portability scan

**Goal.** No emitted artifact uses a Claude-Code-only or proprietary token. (Enforces P1.)

**Method.**

```bash
# Forbidden token regex (must NOT appear outside escape contexts):
grep -rEn '\bclaude_code:|\bcursor:|\bcline:|\bmcp__[a-z_]+\(' \
  prompts/ templates/ references/ wizard/ SKILL.md system_generator.json \
  | grep -v 'tests/' | grep -v 'portable_invocation' | grep -v 'ToolSearch'
```

PASS if `grep` returns no lines.
FAIL if any match found outside `references/portable_invocation.md` (which legitimately documents these tokens as escape context).

**Rationale.** Generator is Tier A portable across 6+ LLMs.

---

### T2 · Calibration scan

**Goal.** No forbidden P2 token appears in artifacts that go to users / will be emitted into child systems. (Enforces P2.)

**Forbidden tokens** (any case): `best`, `always`, `never`, `guaranteed`, `certain`, `definitely`, `impossible`.

**Method.**

```bash
grep -rEni '\b(best|always|never|guaranteed|certain|definitely|impossible)\b' \
  prompts/ templates/ wizard/ SKILL.md \
  | grep -v 'references/calibrated_probabilities.md' \
  | grep -v 'forbidden' \
  | grep -v 'best.practice' \
  | grep -v 'tests/'
```

PASS if 0 lines AND every Complex-tier prompt cites `calibrated_probabilities.md` in its `<alignment_rules>`.
FAIL otherwise.

**Rationale.** P2 forbids any uncalibrated assertion in user-facing or child-emitted text. References describing the rule are exempt (escape context).

**Known false positives.** Phrases like "best-practice anchors" inside `prompt_architect/references/best-practice-anchors.md` are part of the upstream skill (treated read-only). The grep filter excludes them.

---

### T3 · Schema validation

**Goal.** Every `templates/tracking/*.json.tmpl` and `templates/audit/*.json.tmpl` validates structurally against `system_generator.json#/definitions/*` when its placeholders are stripped.

**Method (LLM):**

1. List all `*.json.tmpl` files in `templates/tracking/` and `templates/audit/`.
2. For each, read the template and identify which definition in `system_generator.json` it should match (header comment or filename → e.g., `errors_catalog.json.tmpl` → `ErrorCatalogEntry` collection).
3. Verify required fields are present in the template (placeholders allowed).

PASS if every template covers all required schema fields.
FAIL with the first missing-field per file.

**Rationale.** A child system's tracking can't be valid if the templates are missing fields the schema declares required.

---

### T4 · Prompt-tag floor

**Goal.** Every `prompts/*.md` declares its tier and meets the tag floor.

**Tiers and floors** (per `prompt_architect/references/tier-spines.md`):

- **Simple** — ≥10 tags including: role, audience, task, input, output, constraints, verification, stop_condition, version, metadata.
- **Medium** — ≥18 tags adding: context, success_criteria, sub_tasks, error_handling, guardrails, alignment_rules, tools, test_cases.
- **Complex (mandatory floor)** — ≥30 tags AND must include all 13: `injection_defense, alignment_rules, capability_boundary, test_cases, stop_condition, hitl_conditions, tools, tool_selection, action, observation, scratchpad, temporal_context, verification`.

**Method (LLM):**

For each `prompts/NN_*.md`:

1. Read the front-matter (the line `> **Tier:** Simple | Medium | Complex`).
2. Count `<...>` opening tags inside the embedded ```xml block.
3. For Complex, additionally check the 13 mandatory tags are all present.

PASS table:

| File | Declared tier | Tag count | 13-floor (Complex only) |
|---|---|---|---|
| `00_master_orchestrator.md` | Complex | ≥30 | all 13 ✓ |
| `01_interview_agent.md`     | Medium  | ≥18 | n/a |
| `02_scaffolder.md`          | Medium  | ≥18 | n/a |
| `03_prompt_factory.md`      | Complex | ≥30 | all 13 ✓ |
| `04_library_docs_fetcher.md`| Medium  | ≥18 | n/a |
| `05_error_prevention_seeder.md` | Simple | ≥10 | n/a |
| `06_eu_ai_act_mapper.md`    | Medium  | ≥18 | n/a |
| `07_audit_designer.md`      | Medium  | ≥18 | n/a |
| `08_report_writer.md`       | Medium  | ≥18 | n/a |
| `09_three_auditors_jury.md` | Complex | ≥30 | all 13 ✓ |

FAIL with the violating file + which tag is missing.

---

### T5 · Library manifest URLs

**Goal.** Every entry in `templates/library_docs_manifest.tmpl` has `primary` URL + `fallback` URL.

**Method (LLM):**

1. Open `templates/library_docs_manifest.tmpl`.
2. For each library entry, verify keys `primary` and `fallback` are present and non-empty.
3. Optional: `github_release_api` is recommended for last-resort version pinning.

PASS if every entry has both `primary` and `fallback`.
FAIL with the first entry missing one.

Non-critical: github_release_api absence is a warning, not a failure.

---

### T6 · Error catalog count = 30

**Goal.** AIE catalog has exactly 30 entries everywhere it appears.

**Method.**

```bash
n_md=$(grep -c '^### AIE-' references/ai_error_catalog.md)
n_json=$(grep -c '"id": "AIE-' templates/tracking/errors_catalog.json.tmpl)
[ "$n_md" -eq 30 ] && [ "$n_json" -eq 30 ] && [ "$n_md" -eq "$n_json" ]
```

PASS if both files report exactly 30 AIE-NNN entries.
FAIL with both counts.

**Rationale.** Drift between the master catalog and the seeded JSON template would corrupt every child system's preloaded errors.

---

### T7 · EU AI Act mapping completeness

**Goal.** For high-risk, mapping references all 13 checklists, and the sum of `min_rows` ≥112.

**Method (LLM):**

1. Open `references/eu_ai_act_mapping.md`.
2. Verify the table lists 13 checklist files matched to Articles (9, 10, 11, 12, 13, 14, 15a, 15b, 15c, 17, 50, 72, 73).
3. For each checklist file, confirm it exists at `Checklists y ejemplos/<file>`.
4. Sum `min_rows_high_risk` for the 13 → must be ≥ 112.

PASS if 13 listed + 13 files exist + sum ≥ 112.
FAIL with the missing checklist or insufficient row total.

---

### T8 · Atomic-write pattern

**Goal.** Every prompt that writes files documents an atomic-write pattern (`fs.write` to `*.tmp` + rename).

**Method.**

```bash
grep -L 'atomic\|\.tmp.*rename\|atomic write\|atomic_write' prompts/*.md
```

PASS if every prompt that lists `fs.write` in `<tools>` also mentions `atomic`.
FAIL with the prompt missing the pattern.

Non-critical: warning only; reflection should add it on next iteration.

---

### T9 · Prompt-architect linkage

**Goal.** Every emitted prompt routes through prompt-architect (P4 enforcement).

**Method (LLM):**

For each `prompts/NN_*.md`:

- File must contain at least one of:
  - `> **Composed via:** prompt-architect` (front-matter line).
  - `prompt_architect/SKILL.md` reference in `<context>` or `<tools>`.
  - `03_prompt_factory.md` invocation in `<delegation>`.
- AND `<alignment_rules>` mentions either P4 or "prompt-architect dependency".

PASS if every prompt has at least one anchor + P4 alignment rule.
FAIL with the offending file.

---

### T10 · HITL gates non-skip rule

**Goal.** No prompt instructs auto-skipping of HITL gates.

**Method.**

```bash
grep -rEn 'auto.skip|auto_skip|skip.gate|bypass.gate' \
  prompts/ templates/ SKILL.md system_generator.json \
  | grep -v 'never\|forbidden\|must not\|do not'
```

PASS if zero matches.
FAIL with the offending line.

**Rationale.** HITL gates are inviolable by P4-derived alignment.

---

## Output format

Each test reports:

```
T<N> · <name> · <PASS|FAIL|SKIP> · confidence ~XX%
  rationale: <one line>
  details: <optional, only on FAIL>
```

End with a summary:

```
Suite: X/10 PASS, Y FAIL (critical: Z), W SKIP.
Overall confidence: ~AA%.
Recommendation: <merge | block until X-Y resolved | iterate at gate G2>.
```

## Calibration of the suite itself

- T1, T2, T6, T7, T9, T10: **deterministic** (regex / structural). Confidence ~95%.
- T3, T4, T8: **LLM-judged structural** (placeholders / tag presence). Confidence ~85%.
- T5: **manifest sanity**. Confidence ~92%.

Overall suite confidence (when all PASS): ~90%.

## When to run

- **Pre-push** to GitHub.
- **Pre-release** (version bump).
- **Post-major-edit** to `prompt_architect/` (re-validate downstream linkage T9).
- **Post-EU-AI-Act-mapping update** (re-validate T7).
- **CI hook** (optional): `.github/workflows/validate.yml` calls `bash tests/run_all.sh`.

## Files in this directory

- `README.md` — this file (specs).
- `run_all.sh` — convenience runner (executes the regex-driven tests).
- `t01_portability.sh` — T1 standalone.
- `t02_calibration.sh` — T2 standalone.
- `t06_aie_count.sh` — T6 standalone.
- `t10_hitl_skip.sh` — T10 standalone.

LLM-driven tests (T3, T4, T5, T7, T8, T9) live entirely in this README — they are run by reading these specs and executing them.
