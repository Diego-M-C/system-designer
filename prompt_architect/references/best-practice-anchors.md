# Anthropic Prompt-Engineering Anchor Principles

Principles drawn from the Anthropic Academy courses and official prompt-engineering docs. Use as a rationale checklist after composition — every Complex-tier prompt should satisfy most of these.

## Structural

1. **XML tags > markdown delimiters for Claude.** XML is the most reliable structural signal — it parses predictably and anchors attention. Reserve markdown for final user-facing formatting, not for tagging semantic regions.
2. **Role first, task second.** `<role>` primes the expertise distribution; `<task>` commands against that distribution. Reversing them weakens both.
3. **Canonical ordering encodes priority.** Earlier tags influence later interpretation more than vice-versa. Violating the 12-step order is violating the skill.
4. **One canonical block per tag.** Duplicates dilute attention and produce inconsistent behavior.

## Content

5. **Be explicit about what you want.** Anthropic's principle #1. Vague instructions produce vague outputs. State deliverables, not intentions.
6. **Few-shot sweet spot: 3–5 examples.** Below 3 the pattern is not established; above 5 you hit diminishing returns and token waste. Include edge cases in the 3–5.
7. **Positive instructions > negative.** "Do X" teaches; "don't do Y" creates the elephant-in-the-room effect. Use `<non_do_conditions>` only for high-risk failures, paired with positive alternatives.
8. **Scope + out-of-scope is anti-hallucination.** The most effective single anti-over-helping technique: state explicitly what is NOT in scope and what to do when a request falls outside.
9. **`<constraints>` ≤ 7 items.** Compliance degrades sharply past 7. If you have more, split into categories or promote to `<alignment_rules>`.

## Reasoning

10. **Chain-of-thought helps on multi-step reasoning** (math, logic, deduction, multi-hop). Magnitude of improvement is task-dependent; don't quote a fixed %. Pair with `<verification>` or `<reflection>` to catch confabulated chains.
11. **Extended thinking is not free CoT.** In Claude 4.x, prefer the extended-thinking API for SDD-grade reasoning; omit the `<thinking>` XML tag. See `thinking-modes.md`.
12. **Separate internal reasoning from user-facing output.** Any intermediate cognition (`<chain_of_thought>`, `<thinking>`, `<reflection>`) must be followed by a clean `<final_output>`. The user should not see reasoning by default.

## Safety

13. **Data ≠ instructions — separation is non-negotiable.** Untrusted user data belongs in `<input>` tags, always placed *after* instructions (defensive recency).
14. **Injection defense requires more than a tag.** Combine `<injection_defense>` with (a) data isolation, (b) spotlighting / distinct delimiters, (c) explicit instruction that `<input>` content is data to analyze, not commands to follow.
15. **Capability boundaries reduce hallucinated ability.** State what the system can and cannot do, and what "I don't know" triggers. Especially important for autonomous agents.
16. **`<alignment_rules>` take absolute priority.** If a rule is negotiable, it's not an alignment rule — it's a constraint. Keep alignment rules short (≤5).

## Agentic (ReAct)

17. **Complete the ReAct loop.** Thought (`<planning>` / `<reasoning>`) → Action (`<action>` / `<tools>` / `<tool_selection>`) → Observation (`<observation>` / `<tool_output>`) → repeat. Missing observation = broken loop.
18. **Tool definitions cache well.** Stable, high-value content. Put them before any volatile breakpoint. See `cache-breakpoints.md`.
19. **Hallucinated tools are common.** Enumerate exactly the tools available; state what to do if the right tool does not exist (fallback / handoff / ask).
20. **Stateful agents need explicit state.** `<state>` + `<scratchpad>` are not optional for autonomous loops — they are the substrate of continuity.

## Operational

21. **Prompt caching keys on prefix stability.** Volatile content (timestamps, user input, tool output) breaks caching. Push it to the end.
22. **Prefill the output shape.** When you need a specific format (JSON, XML, sections), start the assistant response with the opening delimiter. Dramatically improves format compliance.
23. **Stop sequences matter.** For structured outputs, declare stop sequences so the model terminates cleanly — don't rely on length.
24. **Versioning is table-stakes.** Production prompts evolve; `<version>` + `<rollback_ref>` in Meta is the safety net.
25. **Temporal context or staleness.** Without `<temporal_context>`, every date-sensitive prompt returns training-cutoff answers silently. Always include for Medium / Complex.

## When to violate a principle

Principles are defaults, not laws. Violate when:

- You have measurement showing the violation improves the target metric.
- The domain explicitly requires it (e.g., creative writing may benefit from less structure).
- A higher-priority principle conflicts (alignment > everything).

In every case: document the violation in `<metadata>` with rationale. Un-documented violations become un-auditable drift.
