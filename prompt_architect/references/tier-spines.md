# Tier Spines — full menus with rationale

Announce the tier before selecting tags. Land within tolerance: ±2 for Simple, ±20% for Medium / Complex.

---

## Simple — 8–16 tags

**Use for:** single-task prompts, scoped chatbots, one-shot extraction / classification / summarization, well-bounded assistants.

**Core spine (required — 8 tags):**
`role` · `task` · `context` · `format` · `constraints` · `examples` · `output` · `final_output`

**Common additions (optional — up to 8 more):**
`audience` · `steps` · `scope` · `non_do_conditions` · `reasoning` · `response_length` · `style` · `language`

**Rationale:**
- `format` is in the core spine (not optional) — even the simplest task benefits from explicit output shape.
- `examples` is core because few-shot (3–5) dominates zero-shot for formatting / classification / style.
- `steps` is optional because linear tasks don't need procedural scaffolding.
- No Safety / Evaluation / Meta at this tier unless the surface justifies it.

---

## Medium — 15–30 tags

**Use for:** multi-step agents, domain experts, RAG applications, analytical workflows, production chatbots with real blast-radius.

**Spine = Simple core + these:**
`domain` · `audience` · `sub_tasks` · `success_criteria` · `scope` · `temporal_context` · `chain_of_thought` · `reflection` · `response_length` · `stop_condition` · `error_handling` · `guardrails` · `evaluation`

**Additions by need:**
- RAG → `reference` · `retrieval` · `knowledge_base` · `citations` · `grounding`
- Multi-turn → `history` · `memory`
- Code generation → `code_spec` · `schema` · `test_strategy`
- Structured output → `schema` · `output_mapping`

**Rationale:**
- Choose **one** of `chain_of_thought` / `reasoning` / `reflection` as primary cognition tag; stacking all three is redundancy, not rigor.
- `temporal_context` is always in Medium — production prompts without explicit date produce silent staleness.
- `guardrails` + `evaluation` enter Medium as a floor; Complex adds structure on top.

---

## Complex (SDD) — 30–50+ tags

**Use for:** agent systems, multi-agent orchestration, safety-critical applications, compliance-bound deployments, autonomous loops.

### Mandatory floor (13 tags, irreducible)

| Category | Tags |
|----------|------|
| Safety | `injection_defense` · `alignment_rules` · `capability_boundary` |
| Evaluation | `test_cases` |
| Control | `stop_condition` · `hitl_conditions` |
| Agentic (ReAct loop) | `tools` · `tool_selection` · `action` · `observation` · `scratchpad` |
| Knowledge | `temporal_context` |
| Cognition | `verification` (paired with ReAct loop) |

**Missing any one** → the prompt is not Complex. Downgrade to Medium or complete the floor.

### Menu on top of mandatory floor (pick what the surface requires)

| Purpose | Candidates |
|---------|------------|
| Identity depth | `persona` · `perspective` |
| Objective precision | `priority` · `goal` · `instructions` |
| Knowledge authority | `knowledge_base` · `definitions` · `assumptions` · `grounding` · `reference` |
| Data specs | `schema` · `code_spec` · `structured_input` |
| Cognition | `planning` · `decomposition` · `self_critique` · `metacognition` · `tree_of_thought` (expensive — opt-in only) |
| Agentic | `state` · `routing` · `delegation` · `handoff` · `tool_output` |
| Output | `citations` · `confidence` · `explanation` · `artifact` · `multimodal_output` |
| Control | `fallback` · `retry` · `orchestration` · `timeout` · `feature_flag` · `conditional` |
| Safety extras | `content_policy` · `pii_handling` · `ethical_guidelines` · `compliance` · `constitution` · `red_team` |
| Evaluation | `rubric` · `metrics` · `baseline` · `adversarial_examples` · `test_strategy` |
| Meta | `version` · `metadata` · `model_config` · `token_budget` · `cache_hint` · `rollback_ref` |

**Rationale:**
- The mandatory floor encodes the three non-negotiables of agentic production: (a) a complete ReAct loop, (b) hard safety boundaries, (c) observable termination + HITL escalation.
- Menu is **not aditive-by-default** — pick surgically. 50 tags with purpose beats 50 tags for show.
- Complex without `<priority>` when tag count ≥ 30 is a red flag — multiple objectives will collide.

---

## Tier selection heuristic

Ask yourself, before declaring tier:

1. **Does the prompt call tools or run in a loop?** → Complex.
2. **Does failure have production / user / compliance consequences?** → Complex.
3. **Is it multi-step with >2 distinct cognitive operations?** → Medium minimum.
4. **Is there RAG / multi-turn memory / domain specialization?** → Medium minimum.
5. **Otherwise** → Simple.

When in doubt between adjacent tiers, **pick the smaller one**. Over-tagging is a common failure mode; under-tagging is caught by the audit.
