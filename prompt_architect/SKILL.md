---
name: prompt-architect
description: Use when building, auditing, refactoring or hardening XML-structured prompts for Claude, agents, or Spec-Driven Development (SDD) systems. Triggers on "use prompt-architect", "architect a prompt", "structure/harden this prompt", "make this production-grade", "audit this system prompt", or when the user is drafting high-stakes prompts where reliability, injection-defense, tag ordering, or Anthropic XML best-practices matter.
---

# Prompt Architect

## Overview

Transform intent into production-grade, XML-tagged prompts using the taxonomy defined in `prompt_editor_skill.json` (co-located — authoritative source for all tag specs, `justification`, `useCases`, `limitations`).

The JSON defines **13 categories**: 12 operational (ordered spine) + `formatting` (horizontal — may appear anywhere inside Output / Style blocks).

**Core principle:** *Structure is leverage. Every well-placed tag buys reliability; every tag without justification buys noise.*

**Progressive disclosure** — heavy reference material lives in `references/` and is read only when composing:

- `references/tag-order.md` — canonical 12-step spine + full per-category tag list
- `references/tier-spines.md` — Simple / Medium / Complex tag menus with rationale
- `references/cache-breakpoints.md` — Anthropic `cache_control` placement model
- `references/thinking-modes.md` — `<thinking>` XML tag vs extended-thinking API in Claude 4.x
- `references/best-practice-anchors.md` — Anthropic prompt-engineering principles

## When to Use

- User explicitly invokes (*"usa prompt-architect"*, *"architect this"*, *"harden this prompt"*)
- Drafting a system prompt, agent loop, evaluation harness, or SDD spec
- High blast-radius prompt (production, agentic, safety-critical, multi-turn)
- Auditing or refactoring an existing prompt

**Do NOT use for:** casual chat, single-turn questions, creative brainstorming, or prompts <150 tokens.

## Complexity Classification — declare BEFORE writing any tag

| Tier | Tag count | Typical use |
|------|----------:|-------------|
| **Simple** | 8–16 | Single-task assistants, scoped chatbots, one-shot extraction |
| **Medium** | 15–30 | Multi-step agents, domain experts, RAG apps, workflows |
| **Complex (SDD)** | 30–50+ | Agent systems, multi-agent, safety-critical, compliance, autonomous |

Announce tier + target count as the first line of output. Tolerance: **±2 absolute for Simple** (% is noisy at low counts); **±20% for Medium / Complex**.

**Complex tier — mandatory floor (irreducible):**

- Safety: `injection_defense` · `alignment_rules` · `capability_boundary`
- Evaluation: `test_cases`
- Control: `stop_condition` · `hitl_conditions`
- Agentic ReAct loop: `tools` · `tool_selection` · `action` · `observation` · `scratchpad`
- Knowledge: `temporal_context`

If any item above is absent from a Complex prompt, the prompt is not Complex — it's either an under-engineered Medium or an incomplete Complex. Re-classify or add.

## Canonical Order (spine)

12-step operational order:

**Identity → Objective → Knowledge → Data → Instruction → Cognition → Agentic → Output → Control → Safety → Evaluation → Meta**

Full per-category tag list: see `references/tag-order.md`. Read before emitting any tag not already in working memory.

**Violating the order is violating the skill.** Re-order — don't skip.

## Workflow

Track the 5 steps explicitly (TodoWrite when available; otherwise numbered internal checklist). Execute sequentially.

### 1 · Classify
State tier + target tag count. No tags yet.

### 2 · Select
- Start from the tier spine (see `references/tier-spines.md`).
- Walk categories 1 → 12. For each unfamiliar candidate tag, open its JSON entry and read `justification` + `limitations` before including. Tags already known to you this session can be emitted without re-read.
- Kill any tag that doesn't earn its tokens. Tag-stuffing is worse than under-tagging.
- For Complex tier, verify the **mandatory floor** before moving to step 3.

### 3 · Compose
- Well-formed XML: `<tag>…</tag>`, one canonical block per tag, no duplicates.
- Stable / reusable content first (cacheable); volatile / user data last.
- Isolate untrusted user data in `<input>`; **always place `<input>` AFTER all instructions** (defensive recency inversion).
- Use `{{double_braces}}` for template variables (skill-local convention, not Anthropic standard — declare in `<metadata>` if exporting).
- Medium+ tier: separate internal reasoning from user-facing `<final_output>`.
- Complex tier: `<injection_defense>` + `<alignment_rules>` + `<capability_boundary>` non-negotiable.

### 4 · Audit
- [ ] Tier declared; count within tolerance
- [ ] Tags in canonical 12-step order
- [ ] Every tag exists in `prompt_editor_skill.json` (no invention)
- [ ] `<task>` starts with an action verb
- [ ] `<constraints>` ≤ 7 items, bulleted
- [ ] `<examples>` 3–5, diverse, include edge cases (for classification / format / style tasks)
- [ ] User data isolated in `<input>` and placed after instructions
- [ ] XML well-formed (no unclosed / mismatched tags)
- [ ] Complex → mandatory floor present (Safety + Eval + Control + Agentic ReAct + `<temporal_context>`)
- [ ] Internal reasoning separated from `<final_output>`
- [ ] `<thinking>` XML tag and extended-thinking API never both enabled
- [ ] No duplicate tags

### 5 · Deliver

```
Tier: <simple|medium|complex> · target <N> · actual <M>

<prompt>…</prompt>

Audit: <✅ all pass | list of ❌>
Rationale: <≤3 bullets>
```

Single fenced XML block. Copy-pasteable.

## Cache Breakpoints (Claude prompt caching)

The `cache_hint` tag in the JSON is a **marker**, not the real mechanism. Actual caching happens via API `cache_control: { type: "ephemeral" }` at up to **4 breakpoints per request**.

Recommended placement:

| # | Place at end of |
|--:|-----------------|
| 1 | System prompt (Identity + Objective + canonical instructions) |
| 2 | Tool definitions (`<tools>` block end) |
| 3 | Static knowledge (`<knowledge_base>` / long `<context>` / `<examples>`) |
| 4 | Last stable turn in multi-turn conversation |

**Volatile content** — user `<input>`, `<observation>`, `<scratchpad>`, timestamped data — **goes AFTER the last breakpoint**. Never cached.

Full placement model, examples, and cost math: `references/cache-breakpoints.md`.

## Thinking Modes in Claude 4.x

Two distinct mechanisms — do NOT conflate:

| Mechanism | What it is | When to use |
|-----------|------------|-------------|
| `<thinking>` XML tag | In-prompt scratchpad you instruct the model to write into | Prompt-engineered CoT for any model; explicit intermediate reasoning emitted as part of the response |
| Extended thinking API | `thinking: { type: "enabled", budget_tokens: N }` request parameter | Claude 4.x native; internal reasoning with its own token budget; returned as dedicated `thinking` content blocks |

**Do not use both simultaneously** — duplicates reasoning cost and leaks internal thought into the user-visible output.

Rule of thumb for Claude 4.x SDD: prefer extended-thinking API + `<final_output>` framing. Omit `<thinking>` XML tag.

Details + interleaved-thinking guidance: `references/thinking-modes.md`.

## Quick Reference — Tier Spines (summary only)

Full menus with rationale in `references/tier-spines.md`.

- **Simple (8–16):** `role` · `task` · `context` · `format` · `constraints` · `examples` · `output` · `final_output`
  *Optional:* `audience` · `steps` · `scope` · `non_do_conditions`
- **Medium (15–30):** Simple spine + `domain` · `audience` · `sub_tasks` · `success_criteria` · `scope` · `temporal_context` · `chain_of_thought` · `reflection` · `response_length` · `stop_condition` · `error_handling` · `guardrails` · `evaluation`
- **Complex (30–50+):** Medium spine + **mandatory floor** (13 tags — see above) + menu picks (`priority`, `knowledge_base`, `definitions`, `schema`, `planning`, `verification`, `self_critique`, `citations`, `confidence`, `fallback`, `retry`, `orchestration`, `rubric`, `metrics`, `version`, `model_config`)

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Inventing tags not in JSON | Use only tags present in `prompt_editor_skill.json`. |
| Skipping canonical order | Re-order — the order encodes priority signal for the model. |
| Tag-stuffing ("more = better") | Each tag must earn tokens. Simple tier tops at 16. |
| Mixing user input with instructions | Isolate in `<input>`, placed AFTER all instructions. |
| Complex tier missing mandatory floor | Add Safety + Eval + Control + ReAct loop + `<temporal_context>`. |
| `<constraints>` as prose | Bullet / number. ≤7 items. |
| Classification task without examples | 3–5 diverse few-shot `<examples>` with edge cases. |
| `<thinking>` XML tag + extended-thinking API together | Pick one. Never both. |
| Reasoning leaking into user-facing output | Always wrap deliverable in `<final_output>`. |
| Using `cache_hint` as if it performed caching | Caching is API-level `cache_control`. See Cache Breakpoints. |

## Red Flags — STOP and re-architect

- Tag used without reading its JSON entry (when unfamiliar this session).
- `<constraints>` > 7 items.
- Jumped from Identity to Output, skipping Objective + Knowledge.
- Complex prompt missing any mandatory-floor tag.
- ≥30 tags without a `<priority>` to break ties.
- User data and instructions share a tag.
- Same tag emitted twice.
- `<thinking>` XML tag present while extended-thinking API is enabled.
- Multiple `chain_of_thought` + `reflection` + `reasoning` stacked without distinct roles.

## Integration Pattern

The user invokes this skill inside their own prompts:

> *"usa prompt-architect para estructurar un agente de análisis legal SDD…"*

On invocation:
1. Read `prompt_editor_skill.json` only if unfamiliar tags are needed.
2. Classify tier.
3. Build per Workflow §1–4.
4. Deliver per Workflow §5 — single fenced XML block + audit + rationale.

If tier is ambiguous from the request, ask ONE clarifying question (*"¿simple / medium / SDD-complex?"*) before building. Otherwise default to the smallest tier that covers stated requirements.

Anchor principles — prefill, few-shot sizing, role-first, cache stability, injection defense, scope discipline, extended-thinking separation — in `references/best-practice-anchors.md`.
