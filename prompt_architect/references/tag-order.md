# Canonical Tag Order — full per-category list

Emit every section in this order. The order mirrors `recommended_tag_order` in `prompt_editor_skill.json`. Violating the order is violating the skill.

## 1 · Identity — *who the AI is*
`role` · `persona` · `system` · `audience` · `domain` · `perspective`

## 2 · Objective — *what to accomplish*
`task` · `goal` · `sub_tasks` · `success_criteria` · `scope` · `priority` · `instructions`

## 3 · Knowledge — *what context / info to ground on*
`context` · `examples` · `reference` · `memory` · `retrieval` · `knowledge_base` · `history` · `definitions` · `assumptions` · `grounding` · `temporal_context`

## 4 · Data — *input and specs*
`input` · `schema` · `variables` · `multi_modal_input` · `structured_input` · `user_preferences` · `code_spec` · `translation_config` · `data_spec`

## 5 · Instruction — *how to do it*
`constraints` · `steps` · `non_do_conditions` · `negative_examples` · `simplification` · `recency_bias`

## 6 · Cognition — *how to think*
`reasoning` · `chain_of_thought` · `tree_of_thought` · `self_consistency` · `planning` · `decomposition` · `reflection` · `verification` · `self_critique` · `analogical_reasoning` · `metacognition` · `thinking` · `debate` · `simulation` · `critique_protocol`

## 7 · Agentic — *tools and workflows*
`tools` · `tool_selection` · `tool_output` · `action` · `observation` · `scratchpad` · `delegation` · `state` · `speaker` · `turn` · `conversation` · `routing`

## 8 · Output — *deliverable format*
`output` · `format` · `style` · `final_output` · `output_mapping` · `response_length` · `citations` · `confidence` · `explanation` · `artifact` · `multimodal_output` · `language` · `reading_level` · `creative_direction`

## 9 · Control — *flow and conditions*
`stop_condition` · `hitl_conditions` · `fallback` · `retry` · `conditional` · `loop` · `branching` · `error_handling` · `handoff` · `orchestration` · `timeout` · `feature_flag`

## 10 · Safety — *boundaries and guardrails*
`guardrails` · `validation` · `content_policy` · `pii_handling` · `injection_defense` · `ethical_guidelines` · `compliance` · `constitution` · `alignment_rules` · `capability_boundary` · `red_team`

## 11 · Evaluation — *quality criteria*
`evaluation` · `test_cases` · `rubric` · `baseline` · `metrics` · `reward_signal` · `test_strategy` · `adversarial_examples`

## 12 · Meta — *prompt management*
`version` · `metadata` · `dependencies` · `model_config` · `abbreviations` · `token_budget` · `cache_hint` · `variant` · `experiment` · `rollback_ref` · `expiry`

## 13 (horizontal) · Formatting
Visual / style directives — may appear inside Output or Style blocks. Not part of the spine order.

---

**Rule:** open `prompt_editor_skill.json` for any tag whose `justification` / `limitations` you have not internalized this session. Do not invent tags. Do not guess snippets.
