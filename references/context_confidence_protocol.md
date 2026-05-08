# Context Confidence Protocol · Reference for Phase 1.5 (and per-session living updates)

> Authoritative source-confidence taxonomy used by `prompts/13_context_curator.md`. Every source in `context/context_manifest.json` carries a `confidence_pct` derived from this document. Library docs are explicitly out of scope (phase 7 owns `library_docs/`).
>
> Generator version: `0.2.0` · Last reviewed: `{{TEMPORAL_NOW}}`

## Why source confidence

Different kinds of context carry different epistemic weight. A line in the EU AI Act has near-certain authority; a forum post has near-noise authority. Treating them identically in the corpus pollutes reasoning. Treating them identically in pruning loses durable knowledge. This protocol gives each source an honest, calibrated `confidence_pct` that downstream phases can weight.

## Source-confidence taxonomy

| Category | Default confidence range | Notes |
|---|---|---|
| `legislation_official`           | 95–99 | Provenance: official URL (e.g., EUR-Lex, BOE, government register) + sha256. |
| `regulator_implementation_guide` | 88–95 | AESIA, ICO, NIST, FDA, EMA implementation/AI policy docs. |
| `standards_body_doc`             | 85–92 | ISO/IEC 42001, ISO 13485, ISO 14971, IEEE standards. |
| `vendor_official_docs`           | 85–92 | Anthropic docs, OpenAI policies, Google AI documentation. |
| `peer_reviewed_paper`            | 80–90 | DOI required when available; lower if pre-print only. |
| `industry_standard_doc`          | 80–90 | TRIPOD-AI, CONSORT-AI, STARD-AI, SPIRIT-AI. |
| `expert_blog`                    | 60–75 | Well-known practitioner; recency matters. |
| `forum_discussion`               | 30–50 | Stack Overflow, GitHub issues, Reddit threads. |
| `internet_opinion_general`       | 20–50 | Default `consult_websites_only=true` unless user opts in. |
| `user_uploaded_doc`              | 80 (overridable up or down) | Rationale: user-asserted authoritative. User can lower. |

## Anchoring rules

- A point estimate within a category's range requires a stated rationale (≤200 chars). The rationale is persisted in the source's `manifest.json#confidence_rationale`.
- Going **outside** a category's range requires explicit user override at HITL plus a stronger rationale. Logged in `context/curation_log.jsonl` with `who_decided=user`.
- Recency is a multiplier, not a category demotion. A 10-year-old peer-reviewed paper stays in `peer_reviewed_paper` but its `confidence_pct` may be the bottom of the range (80%).

## Pruning rule (deterministic)

```
Eligible_for_prune = sources WHERE
    confidence_pct <= 50
    AND sha256 NOT in any successful_evidence_link this session
    AND tested_unhelpful_count >= 1 across last 2 sessions
```

A source is **never** pruned solely on age. Aging triggers re-fetch candidacy, not removal.

## Promotion rule (informational)

If a source's `tested_helpful_count` increases consistently across sessions, the curator may **propose** raising its `confidence_pct` by up to +10 within its category range (never crossing categories). The proposal surfaces at the next session-close HITL.

## Internet opinions

By default, `internet_opinion_general` enters with `consult_websites_only=true` — i.e., recorded as a runtime bookmark, not downloaded. The user must explicitly opt-in to download. This protects the corpus from low-quality drift while preserving the user's right to bring in non-authoritative sources.

## Library docs are out of scope

This protocol does not cover library documentation. Library docs live under `library_docs/<lib>/<version>/` and are owned by `prompts/04_library_docs_fetcher.md` (phase 7). This separation prevents version-pin contamination between regulatory/methodological context and runtime library behaviour.

## Tool ladder for fetching

```
Try mcp.playwright.navigate(url) ─► html dump
        │ unavailable / fail
        ▼
Try fetch(url) ────────────────────► raw response
        │ unavailable / fail
        ▼
Emit download_recommendations.md row + flag needs_user_upload=true
```

## What goes where

| Artefact | Purpose | Lifecycle |
|---|---|---|
| `context/context_manifest.json` | High-level source index. | Regenerated atomically each curation run. |
| `context/context_sources/<slug>/manifest.json` | Per-source provenance + confidence. | Append on add; mutate on `tested_*_count` updates. |
| `context/consult_websites.md` | Runtime consult bookmarks. | Regenerated each curation run. |
| `context/download_recommendations.md` | Inaccessible sources awaiting upload. | Append on miss; remove on satisfy. |
| `context/curation_log.jsonl` | Append-only history of add/prune/refetch decisions. | Append-only; never rewritten. |

## Mean-confidence target

The corpus mean `confidence_pct` should trend ≥70%. The `<70%` case at phase 1.5 close surfaces a warning at HITL ("your corpus is dominated by low-confidence sources; consider adding authoritative material").

## Versioning

Adding a new category, changing a default range, or changing the pruning rule requires:
1. A row in `feedback_learning/corrections.db` (`category=tooling` or `documentation`).
2. Approval at phase 13.7.
3. A changelog entry in this file's `## Changelog` section.

## Changelog

- `0.2.0` — initial taxonomy (10 categories) + pruning rule + tool ladder + scope boundary vs library_docs.
