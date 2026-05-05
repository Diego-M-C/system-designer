# system-designer

> **Portable, LLM-agnostic meta-generator** that scaffolds EU AI Act-compliant SDD projects from a single user intent.
> Drop this folder into any LLM (Claude Code, Cursor, Cline, Gemini CLI, Copilot CLI, Codex) and run.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Portable](https://img.shields.io/badge/portable-Tier_A-blue.svg)](references/portable_invocation.md)
[![EU AI Act](https://img.shields.io/badge/EU_AI_Act-2024%2F1689-brightgreen.svg)](references/eu_ai_act_mapping.md)
[![Calibrated](https://img.shields.io/badge/calibration-mandatory-orange.svg)](references/calibrated_probabilities.md)
[![Prompt tier](https://img.shields.io/badge/tier-Complex_(46_tags)-purple.svg)](prompt_architect/SKILL.md)

---

## What this is

A **generator of systems**, not a system. Same backbone every time — Spec-Driven Development + tracking + KPIs + HITL gates + memory + error catalog + EU AI Act audit + scientific reports — **particularised per intent** through a structured interview.

You give it: `"build a clinical-decision-support assistant for oncology triage"`.
It gives you: a complete project tree with master orchestrator, living tracking, calibrated planning, HITL governance, 30 pre-loaded AI-error patterns, audit Excel sheets per the 13 EU AI Act checklists, IMRaD/TRIPOD-AI report templates, and **every prompt composed through the co-located `prompt_architect/`** skill.

It then **stops**. Handoff is explicit; the generator does not continue developing the child system.

## Core principles (non-negotiable)

| # | Principle | What it means |
|---|---|---|
| **P1** | Portability | Every artifact runs in any LLM with file-system access. No proprietary APIs in runtime. Fallbacks mandatory. See [`references/portable_invocation.md`](references/portable_invocation.md). |
| **P2** | Calibrated probabilities | Every output carries confidence % or range. `"X is the best"` → forbidden. `"X has ~75% fit; Y 15%; Z 10%"` → required. See [`references/calibrated_probabilities.md`](references/calibrated_probabilities.md). |
| **P3** | On-demand generation | Nothing emitted for show — only what the interview confirmed is needed. |
| **P4** | Prompt-architect dependency | Every emitted prompt — including the orchestrator's own — is composed through `prompt_architect/SKILL.md`. No raw prompts exit. |
| **P5** | Living documentation | Every artifact is updated session by session. Static docs are forbidden. |

## Quickstart

### Claude Code

```bash
# 1. Clone next to your workspace (or anywhere on disk):
git clone https://github.com/Diego-M-C/system-designer.git

# 2. Drop a CLAUDE.md alias in your project root, OR install as plugin, OR:
claude
> /system-designer
```

Or invoke directly with the slash command (auto-installed if you place this repo under `.claude/`):

```
/system-designer build a fraud-detection system for SEPA transfers
```

### Cursor / Cline / Gemini CLI / Copilot CLI / Codex / plain LLM

Drop the folder into the chat / project root and say:

```
Read SKILL.md and run the system-designer workflow for me. Project: <your intent>.
```

The skill self-loads, runs the interview, and produces the child system. See [`references/portable_invocation.md`](references/portable_invocation.md) for per-platform notes.

## What it produces

A complete child-system tree, by default at `<cwd>/<system_name>/`:

```
<system_name>/
├── CLAUDE.md                    # Child orchestrator contract
├── README.md
├── SPEC.md / SPEC.json          # 17-section SDD spec
├── ARCHITECTURE.md              # Mermaid diagrams + per-Article compliance arch
├── HANDOFF.md                   # How to resume + first 3 sessions planned
├── prompts/                     # All composed via prompt_architect (Simple/Medium/Complex)
├── library_docs/                # Fresh fetched docs (per chosen lib + version)
├── tracking/                    # project.json, sessions/, decisions, errors_catalog (30 AIE)
├── memory/                      # 4 typed memories (user/project/feedback/reference)
├── audit/                       # 13-sheet xlsx + EU AI Act mapping + self_audit + reflection
├── docs/reports/                # cumulative.md + standard (IMRaD/TRIPOD-AI/CONSORT-AI/STARD-AI/SPIRIT-AI)
└── docs/decisions/              # ADR log
```

Plus: 2 mandatory **HITL gates** (no auto-skip ever), 11 session KPIs, calibration & portability self-scans, and a self-audit pass (the generator's own master orchestrator is audited by the prompt-architect at G9=A level).

## Why bother

| Pain | Without `system-designer` | With `system-designer` |
|---|---|---|
| Cold start | Hours of "what scaffolding do I need?" | Calibrated interview + plan in 1 session |
| EU AI Act compliance | Manual mapping of 13 Articles → 13 checklists → audit rows | Auto-generated with min_rows + ≥95% completeness gate |
| Calibration discipline | Forgotten by session 3 | Enforced by P2 scans on every emitted artifact |
| Library doc rot | "It worked in training data" | Always fetches fresh per chosen lib + version |
| AI error patterns | Stumble into them, fix, repeat | 30 AIE-NNN preloaded with auto-extension protocol |
| Session granularity | Vague | Hybrid B+D: 1 deliverable + mandatory HITL checkpoint |
| Reproducibility | Ad-hoc | Atomic writes, sha256 logging, versioned scaffolds |

## Repository structure

```
system-designer/
├── SKILL.md                          # Entry-point meta-skill
├── system_generator.json             # Machine-readable spec (5 principles, 13 phases, schemas, KPIs)
├── prompts/                          # 10 agent prompts (00_master_orchestrator → 09_three_auditors_jury)
├── references/                       # 6 reference docs (P2 rules, P1 contract, AI errors, EU AI Act, scientific reports)
├── templates/                        # ~25 *.tmpl files (renders the child tree)
├── wizard/                           # interview_questions.json + defaults.json
├── prompt_architect/                 # Co-located dependency (read-only)
├── Checklists y ejemplos/            # 13 EU AI Act Excel checklists
├── EU_AI_Act_guides/                 # Regulatory PDFs (OJ_L_202401689_EN_TXT.pdf + AESIA guides)
├── Informes_Cursos_Anthropic/        # Anthropic course material referenced by the architect
├── tests/                            # Self-validation test cases (see "Testing")
├── dashboard/                        # Static HTML dashboard for live tracking visualisation
└── .claude/commands/                 # Slash command convenience layer (Claude Code only)
```

## Testing

The generator self-validates. From any LLM:

```
Read tests/README.md and run the suite.
```

Tests cover:
- **T1** Portability scan — no `claude_code:`, `cursor:`, `mcp__` references in `prompts/` or `templates/`.
- **T2** Calibration scan — no forbidden tokens (best, always, never, guaranteed, certain, definitely, impossible) in references/templates outside escape contexts.
- **T3** Schema validation — all `templates/tracking/*.json.tmpl` validate against `system_generator.json#/definitions/*`.
- **T4** Prompt floor — every Complex-tier prompt has the 13 mandatory tags.
- **T5** Library manifest URLs — every entry has `primary` + `fallback` + (optional) `github_release_api`.
- **T6** Error catalog count — exactly 30 AIE-NNN entries match between `references/ai_error_catalog.md` and `templates/tracking/errors_catalog.json.tmpl`.
- **T7** EU AI Act mapping — for high-risk, all 13 checklists are referenced + min_rows sum ≥112.
- **T8** Atomic-write pattern — every `fs.write` example uses `*.tmp` + rename.

See [`tests/README.md`](tests/README.md).

## Dashboard

Static HTML dashboard at [`dashboard/index.html`](dashboard/index.html). Open in any browser, drop a `tracking/project.json` from a generated child system, and visualise: phase progression, KPI trend, HITL gate status, audit completeness, error catalog coverage. No build step, no server.

## Compatibility matrix

| LLM platform | Tier | Notes |
|---|---|---|
| Claude Code | A | Slash command + sub-agents available |
| Cursor | A | Drop folder → ask to read SKILL.md |
| Cline | A | Same |
| Gemini CLI | A | `activate_skill` route or read SKILL.md directly |
| Copilot CLI | A | `skill` tool route |
| Codex | A | Read SKILL.md → execute |
| Plain ChatGPT / Claude.ai | B | Manual: paste SKILL.md, then provide files on demand |

Tier A = full automation. Tier B = manual file presentation needed.

## Versioning

`v0.1.0` — initial release.
Schema versions for child artifacts are stable from `v0.1.0`; behaviour stable across LLMs (Tier A) but exact prompt phrasing may evolve as `prompt_architect` evolves.

See [`system_generator.json#/changelog`](system_generator.json).

## Contributing

PRs welcome for:
- New report standards in `references/scientific_report_format.md` + `templates/reports/`.
- New error patterns in `references/ai_error_catalog.md` (keep AIE-NNN IDs stable).
- New domain branches in `wizard/defaults.json`.
- Per-LLM platform notes in `references/portable_invocation.md`.

**Not** accepted:
- Modifications to `prompt_architect/` (upstream skill, treat as read-only here).
- Removing P1–P5 enforcement.
- Auto-skipping HITL gates.

## Acknowledgements

- **EU AI Act Regulation 2024/1689** + AESIA implementation guides — [`EU_AI_Act_guides/`](EU_AI_Act_guides/).
- **prompt_architect** skill (co-located) — supplies the 12-step canonical spine + 13-tag Complex floor + tag taxonomy.
- **Anthropic course material** — [`Informes_Cursos_Anthropic/`](Informes_Cursos_Anthropic/) — best-practice anchors for prompt composition.
- TRIPOD-AI / CONSORT-AI / STARD-AI / SPIRIT-AI consortia — for the AI-aware reporting standards templated under `templates/reports/`.

## License

MIT — see [LICENSE](LICENSE).

---

Built calibrated. Confidence in this README's accuracy: ~85%; gaps possible in per-LLM tooling notes (Tier B details may evolve).
