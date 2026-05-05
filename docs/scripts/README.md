# Per-script deep-dive

> One MD per `prompts/NN_*.md`. Each file follows the same structure so reading any one gives you a full operating mental model.

## Index

| #  | File | Tier | Tags | Role |
|----|------|------|------|------|
| 00 | [`00_master_orchestrator.md`](00_master_orchestrator.md) | Complex | 46 | Drives the 13-phase loop, owns HITL gates, dispatches specialists |
| 01 | [`01_interview_agent.md`](01_interview_agent.md) | Medium | ~22 | Wizard: one-question-per-turn, atomic persist to SPEC.json |
| 02 | [`02_scaffolder.md`](02_scaffolder.md) | Medium | ~20 | Renders templates → child tree, sha256-logs every emit |
| 03 | [`03_prompt_factory.md`](03_prompt_factory.md) | Complex | ~32 | P4 enforcer: composes & audits every emitted prompt via prompt-architect |
| 04 | [`04_library_docs_fetcher.md`](04_library_docs_fetcher.md) | Medium | ~22 | Context7 → primary → fallback → github_release_api chain |
| 05 | [`05_error_prevention_seeder.md`](05_error_prevention_seeder.md) | Simple | ~12 | Seeds 30 AIE-NNN entries into child tracking |
| 06 | [`06_eu_ai_act_mapper.md`](06_eu_ai_act_mapper.md) | Medium | ~22 | Risk-class → applicable Articles → checklist references |
| 07 | [`07_audit_designer.md`](07_audit_designer.md) | Medium | ~24 | 13-sheet xlsx (or csv+md) with ≥112 rows for high-risk |
| 08 | [`08_report_writer.md`](08_report_writer.md) | Medium | ~22 | IMRaD/TRIPOD-AI/CONSORT-AI/STARD-AI/SPIRIT-AI selector + scaffolder |
| 09 | [`09_three_auditors_jury.md`](09_three_auditors_jury.md) | Complex | ~36 | N independent auditors + meta-jury, dissent → HITL |

## Reading order

If you're new: read `00_master_orchestrator.md` first (the conductor), then `01_interview_agent.md` and `02_scaffolder.md` (the first two in execution order). Then `03_prompt_factory.md` (because everything else passes through it).

If you're debugging a specific phase: jump to the matching script doc.

If you're extending the generator: read `00_master_orchestrator.md#extension-points` and the script doc closest to your change.

## Doc structure (consistent across all 10 scripts)

Each doc has these sections:

1. **Purpose** — what the prompt accomplishes in one paragraph.
2. **When invoked** — phase + trigger.
3. **Inputs** — files read, fields consumed.
4. **Outputs** — files written, signal returned.
5. **Tag rationale** — why each `<tag>` is present (Complex floor justified).
6. **Control flow** — step-by-step with branch points.
7. **Calibration anchors** — where P2 is enforced.
8. **Portability** — Tier-A degradation paths.
9. **Error handling & fallbacks** — what fails and what kicks in.
10. **HITL escalation triggers** — when this prompt blocks for human.
11. **Dependency edges** — upstream and downstream prompts.
12. **Test coverage** — which `tests/*` validate this prompt.
13. **Common failure modes** — what to look for during review.
