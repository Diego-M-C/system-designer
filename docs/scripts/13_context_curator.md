# 13 · Context Curator

> **File.** `prompts/13_context_curator.md`
> **Tier.** Complex (~40 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **Version.** 0.2.0

## 1. Purpose

Builds the project's **task-specific context corpus** before the interview, and keeps it living across sessions. Sources include implementation guides, legislation (when applicable), non-library documentation, peer-reviewed papers, expert blogs, forum threads, and curated internet opinions. **Each source carries a calibrated `confidence_pct`.** Library docs are explicitly **out of scope** (phase 7 owns those).

## 2. When invoked

- **Phase 1.5** — strictly after `read_context` (phase 1) and before `interview` (phase 2). Mode = `bootstrap`.
- Inherited by the child orchestrator: re-runs at every session boundary. Mode = `living_update`.
- Skipped only if `SystemSpec.compatibility.v0_1_0 == true` OR the user opts out at wizard Q31.

## 3. Inputs

- `<target_path>/SPEC.json` (if present) — domain / risk hints.
- `<target_path>/tracking/project.json` — invocation mode + history.
- `<target_path>/context/context_manifest.json` (if present) — living state.
- `<target_path>/tracking/sessions/<id>/observations.jsonl` (living mode) — `tested_unhelpful` flags.
- `references/context_confidence_protocol.md` — taxonomy.

## 4. Outputs (under `<target_path>/context/`)

- `context_manifest.json` — index regenerated each run.
- `context_sources/<slug>/<file>` + `manifest.json` — per-source provenance.
- `consult_websites.md` — runtime bookmarks (NOT downloaded).
- `download_recommendations.md` — sources awaiting user upload.
- `curation_log.jsonl` — append-only history (add/prune/refetch).

## 5. Source-confidence taxonomy (10 categories)

| Category | Default range | Notes |
|---|---|---|
| `legislation_official`            | 95–99 | EUR-Lex, BOE, official registers |
| `regulator_implementation_guide`  | 88–95 | AESIA, ICO, NIST, FDA, EMA |
| `standards_body_doc`              | 85–92 | ISO/IEC 42001, ISO 13485, IEEE |
| `vendor_official_docs`            | 85–92 | Anthropic, OpenAI, Google AI |
| `peer_reviewed_paper`             | 80–90 | DOI required when available |
| `industry_standard_doc`           | 80–90 | TRIPOD-AI, CONSORT-AI, STARD-AI, SPIRIT-AI |
| `expert_blog`                     | 60–75 | Practitioner-authored |
| `forum_discussion`                | 30–50 | SO, GitHub issues, Reddit |
| `internet_opinion_general`        | 20–50 | default `consult_websites_only=true` |
| `user_uploaded_doc`               | 80 (overridable) | "user-asserted authoritative" |

## 6. Fetch tool ladder

```
Try mcp.playwright.navigate(url) ─► html dump
        │ unavailable / fail
        ▼
Try fetch(url) ────────────────────► raw response
        │ unavailable / fail
        ▼
Emit download_recommendations.md row + needs_user_upload=true
```

## 7. Pruning rule (deterministic, living mode only)

```
Eligible_for_prune = sources WHERE
  confidence_pct <= 50
  AND sha256 NOT in any successful_evidence_link this session
  AND tested_unhelpful_count >= 1 across last 2 sessions
```

A source is **never** pruned solely on age. Aging triggers re-fetch candidacy, not removal.

## 8. Calibration & portability anchors

- Every source carries confidence%; rationale ≤200 chars persisted.
- `mcp.playwright` is soft (recommended, not required); `fetch()` is universal; user-upload always works offline.
- Library docs explicitly excluded — phase 7 owns `library_docs/`.

## 9. HITL escalation triggers

- **Bootstrap fetch plan** — ALWAYS approve before any fetch.
- **Living add/prune review** — ALWAYS approve before any change.
- **Internet opinion not user-listed** — confirm inclusion.
- **Confidence override outside taxonomy range** — require rationale.
- **A user-upload remains pending across 2 sessions** — re-prompt.
- **Corpus mean confidence < 70%** — flag at run close.

## 10. Dependency edges

- ↑ called by `prompts/00_master_orchestrator.md` at phase 1.5 (bootstrap) and by child orchestrator at session boundaries (living update).
- ↓ delegates source-classifier and confidence-rationaliser sub-prompts to `prompts/03_prompt_factory.md`.
- → reads `references/context_confidence_protocol.md`, `templates/context/*.tmpl`.
- ← consumed by interview (phase 2), planning (phase 3), every downstream phase that consults the corpus.

## 11. Modes — bootstrap vs. living_update

| | bootstrap | living_update |
|---|---|---|
| When | Phase 1.5 (fresh project) | Every session boundary |
| Initial corpus state | empty | non-empty |
| User surface | full questionnaire | add/prune review |
| Pruning | not applicable | gated to ≤50% conf + tested-unhelpful |
| Promotion proposal | n/a | offered when consistent helpfulness |

## 12. Test coverage

- T11 / T16 confirm prompt + templates exist.
- 7 in-prompt `<test_cases>`: high-risk legal / healthcare / living-update prune / playwright unavailable / no-network / confidence override / opinion auto-include blocked.

## 13. Common failure modes

- **All-low-confidence corpus** — mean <70% at end of bootstrap; surfaces a warning; user can add authoritative material before phase 2.
- **Pending uploads forever** — `pending_user_uploads` not decreasing across 3 sessions; surfaces meta-warning to phase 13.5.
- **Confidence drift** — a source's `tested_helpful_count` grows but no promotion proposal fires (e.g., user dismissed the proposal); logged in `curation_log.jsonl` for retrospection.
- **Sanitiser strips a legitimate URL** — JS pseudo-URL filter is conservative; user can override at HITL with rationale.
