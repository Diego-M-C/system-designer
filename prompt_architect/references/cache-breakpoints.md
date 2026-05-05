# Cache Breakpoints — Anthropic prompt caching, operational model

The `cache_hint` tag in `prompt_editor_skill.json` is a **documentation marker** — it does not perform caching. Actual caching is configured via the API request body, independent of prompt XML content.

## Mechanism

Anthropic prompt caching uses `cache_control: { type: "ephemeral" }` set on specific content blocks. Claude reads the request and caches the prefix up to each breakpoint. Subsequent requests with the same prefix reuse the cached compute.

- **Maximum breakpoints per request:** 4
- **Minimum cache-eligible length:** varies by model (typically 1024+ tokens for Sonnet/Opus, higher for Haiku — check current model docs)
- **TTL:** 5 minutes by default; longer TTL available as a paid feature
- **Cost model:** writes cost ~1.25× base input token cost; reads cost ~0.1× — break-even around the 2nd–3rd hit

## The 4-breakpoint placement model

Map breakpoints to structural boundaries in the prompt, from most-stable (first) to least-stable (last):

| # | Breakpoint location | What it caches | Invalidated by |
|--:|---------------------|----------------|----------------|
| 1 | End of system prompt (Identity + Objective + baseline Instruction) | Role, task spec, canonical constraints, non-volatile behavior | System prompt edits |
| 2 | End of tool definitions (`<tools>` block) | Full tool schemas, selection rules | Tool additions / signature changes |
| 3 | End of static knowledge (`<knowledge_base>`, long `<context>`, curated `<examples>`) | Domain reference, few-shot exemplars | Knowledge base versioning |
| 4 | End of last stable conversation turn | Historical turns that won't change | New user turn |

## What goes AFTER the last breakpoint (never cached)

- `<input>` — current user query / payload
- `<observation>` / `<tool_output>` — runtime tool results
- `<scratchpad>` — model working memory within this turn
- Timestamped data (prices, stock, news, `<temporal_context>` current-time fields)
- Any field referencing a moving target (now, today, latest)

## Layout template (conceptual)

```
<system>
  <role>…</role>
  <task>…</task>
  <constraints>…</constraints>
  <instructions>…</instructions>
</system>
[BREAKPOINT 1]

<tools>…complete tool schemas…</tools>
[BREAKPOINT 2]

<knowledge_base>…static reference…</knowledge_base>
<examples>…few-shot…</examples>
[BREAKPOINT 3]

<history>…stable prior turns…</history>
[BREAKPOINT 4]

<!-- everything below is volatile, not cached -->
<temporal_context>now = {{iso_timestamp}}</temporal_context>
<input>{{user_query}}</input>
<observation>{{latest_tool_result}}</observation>
```

## Anti-patterns

| Anti-pattern | Why it breaks caching |
|--------------|----------------------|
| Date injected into the system prompt | Invalidates breakpoint 1 every day |
| User name interpolated into role/persona | Kills cache per-user |
| Tool list re-ordered between requests | Breakpoint 2 misses |
| Examples shuffled / hot-swapped | Breakpoint 3 misses |
| Volatile input placed *before* any breakpoint | All downstream cache invalidated |

## Rule of thumb

**Place breakpoints greedily at the latest point that is still stable.** One well-placed breakpoint beats four placed too early.

If you only have budget for one breakpoint (single-turn API call), put it at the end of the system prompt (breakpoint 1) — it gives the highest hit rate per dollar.

## Relationship to JSON `cache_hint` tag

Use `<cache_hint>` in the prompt body as **annotation for humans** — a visible marker that a section is intended to be stable / cacheable. It signals intent to whoever edits the prompt next, but it does not alter API behavior. The actual `cache_control` goes into the API request, outside the prompt XML.
