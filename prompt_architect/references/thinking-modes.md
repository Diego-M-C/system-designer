# Thinking Modes in Claude 4.x — disambiguation

Two distinct mechanisms exist for intermediate reasoning. Conflating them doubles cost and leaks internal thought into user-visible output. Pick one.

## Mechanism A — `<thinking>` XML tag (prompt-level)

An in-prompt scratchpad you instruct the model to write into. Works on any model (Claude 3.x, Claude 4.x, others).

- **What it is:** an XML tag the model emits as part of its normal response text.
- **Cost:** counts as regular output tokens.
- **Visibility:** present in the response body. You filter it out downstream if you don't want the user to see it.
- **When appropriate:** prompt-engineered CoT on models without native extended thinking; debugging reasoning externally; any case where you want the reasoning captured in the output stream.

Typical usage:

```xml
<instructions>
Think through the problem inside <thinking> tags first, then output the final answer inside <final_output> tags.
</instructions>
…
<thinking>
step-by-step reasoning …
</thinking>
<final_output>
answer …
</final_output>
```

## Mechanism B — Extended thinking API (request-level, Claude 4.x native)

A request parameter that enables an internal reasoning phase with its own token budget. The model emits dedicated `thinking` content blocks *before* the main `text` blocks.

- **What it is:** API parameter: `thinking: { type: "enabled", budget_tokens: N }`.
- **Cost:** billed separately (thinking tokens distinct from output tokens); budget bounded by `budget_tokens`.
- **Visibility:** returned as structured `thinking` content blocks in the response — easy to strip programmatically, distinct from user-facing `text` blocks.
- **When appropriate:** Claude 4.x SDD / agent work where high-stakes reasoning is warranted; when you want reasoning cleanly separated from delivery at the API level; when you need budget control.
- **Interleaved thinking (Claude 4.x):** with some Claude 4.x models, thinking blocks can appear interleaved with tool-use turns, allowing the model to reason between observations and next actions.

## Never both simultaneously

Running `<thinking>` XML-tag instructions while `thinking.type = "enabled"` at the API level produces:

- Duplicated reasoning cost (internal budget + output tokens).
- Reasoning content appearing twice (once in native blocks, once in the text body).
- Higher chance of internal reasoning leaking into `<final_output>`.

**Rule:** decide at build time which mechanism governs this prompt, and remove the other.

## Decision guide for Claude 4.x SDD

| Situation | Pick |
|-----------|------|
| Claude 4.x, agent loop, high-stakes reasoning | Extended thinking API + `<final_output>` framing; omit `<thinking>` tag |
| Claude 4.x, simple structured output | No extended thinking, no `<thinking>` tag (avoid overhead) |
| Claude 3.x or non-Anthropic model | `<thinking>` XML tag (API extended thinking unavailable) |
| Need reasoning visible in the output for user inspection | `<thinking>` XML tag — extended thinking blocks are structurally separate |
| Cost-sensitive batch work | Avoid both unless reasoning demonstrably improves accuracy on the task |

## Audit implications

In the Workflow §4 audit, verify:

- [ ] Either `<thinking>` tag OR extended thinking is active, never both.
- [ ] If extended thinking is enabled, `<final_output>` is the sole user-facing deliverable framing.
- [ ] If `<thinking>` tag is used, a paired `<final_output>` is always present to cut reasoning leak.

## Red flag

Seeing both `<thinking>` inside the prompt body AND a request configured with `thinking.type = "enabled"` → STOP, pick one, re-architect.
