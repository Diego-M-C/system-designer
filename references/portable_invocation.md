# Portable Invocation — Pattern across LLMs (Principle P1)

> **Why:** the user must be able to drop `Sistem_designer/` into ANY LLM with file-system access and have it run. No installation, no platform-specific config, no proprietary MCP.
>
> **Scope:** the generator itself + every child artifact's runtime contract.

---

## 1 · Universal invocation contract

Three steps, identical across platforms:

1. **Make the folder reachable** — drag-and-drop, paste absolute path, or upload as workspace.
2. **Send a prompt** — *"Use system-designer at `<path>` to scaffold an SDD system that <intent>."*
3. **Respond at HITL gates** — the LLM blocks on `<final_output>` HITL gate brief; user replies with letter or freeform.

The LLM internally:
- Reads `SKILL.md`
- Reads `system_generator.json`
- Reads `prompts/00_master_orchestrator.md`
- Executes the master orchestrator's phase loop
- Uses its native file-system + fetch tools

## 2 · Abstract tool contract (mandatory floor)

The orchestrator describes tools abstractly. Every executor maps these to its native primitives:

| Abstract tool | Purpose | Native equivalents (per platform) |
|---|---|---|
| `fs.read(path)` | Read a file | Claude Code: `Read`. Cursor: `read_file`. Cline: `read_file`. Gemini CLI: `read_file`. Copilot CLI: `read_file`. Codex: built-in. Plain LLM: ask user / use shell. |
| `fs.write(path, content)` | Write a file | Claude Code: `Write` / `Edit`. Cursor: `edit_file` / `create_file`. Cline: `write_to_file`. Gemini CLI: `write_file`. Copilot CLI: `write`. Codex: `apply_patch`. Plain LLM: emit content + ask user to save. |
| `fs.list(path)` | List directory | Claude Code: `LS` / `Bash ls`. Cursor: `list_dir`. Others: equivalent. |
| `fs.mkdir(path, recursive=true)` | Create dirs | Claude Code: `Bash mkdir -p`. Others: equivalent or sequential `fs.write`. |
| `fetch(url, headers?)` | HTTP GET | Claude Code: `WebFetch`. Cursor / Cline / others: built-in browser/fetch. Plain LLM: ask user / out-of-band. |
| `now()` | ISO timestamp | Claude Code: `Bash date -Iseconds`. Cursor / others: shell exec. Plain LLM: ask user at session start. |
| `prompt_architect(intent, tier_hint?, context_refs[])` | Compose audited prompt | Implemented as: load `prompt_architect/SKILL.md`, follow its workflow, return audited XML. Sub-LLM-call if executor supports recursion; otherwise inline-execute the workflow. |
| `xlsx.write(path, sheet_data)` *(optional)* | Write Excel | Claude Code: `Bash python -c "...openpyxl..."` if Python available. Fallback: CSV+MD sidecar. |
| `context7.fetch(library, version)` *(optional)* | Library docs primary | MCP server. Fallback: `fetch()` against URL in `templates/library_docs_manifest.tmpl`. |
| `parallel.spawn(prompts[])` *(optional)* | Parallel sub-agents | Claude Code: parallel `Agent` calls. Fallback: sequential execution; document fallback in `audit/self_audit.md`. |

**Rule:** any tool reference in an emitted child prompt MUST be described in the abstract form. Never as `Skill(...)`, `mcp__...`, `TodoWrite`, `SubagentType`, `EnterPlanMode`, etc.

## 3 · Per-platform notes

### 3.1 · Claude Code

- **Invocation:** drag folder OR `cd` into it OR `/system-designer` slash command (after `.claude/commands/system-designer.md` is created via on-demand artifact).
- **Tools native:** `Read`, `Write`, `Edit`, `Bash`, `WebFetch`, `Agent`, `Skill`.
- **Caveat:** `Skill` tool only available if `Sistem_designer/` is registered as a Claude Code skill via `.claude/settings.json` symlink. Drag-and-drop pattern bypasses this — read `SKILL.md` directly via `Read`.
- **Cache:** Anthropic prompt caching active by default; the orchestrator's `<cache_hint>` block is honoured.

### 3.2 · Cursor

- **Invocation:** add folder to workspace, then prompt with file references via `@<file>`.
- **Tools native:** `read_file`, `edit_file`, `create_file`, `list_dir`, `run_terminal_cmd`.
- **Caveat:** no native `WebFetch` — use `run_terminal_cmd` with `curl` / `wget`.
- **Cache:** Cursor caches independently; `<cache_hint>` is informational only.

### 3.3 · Cline (VS Code extension)

- **Invocation:** open VS Code in folder, ask Cline to "use system-designer".
- **Tools native:** `read_file`, `write_to_file`, `replace_in_file`, `execute_command`, `browser_action`.
- **Caveat:** `execute_command` requires user approval per call; the orchestrator must batch where possible.

### 3.4 · Gemini CLI

- **Invocation:** `gemini -p "Use system-designer at <path>..."` from within the folder.
- **Tools native:** `read_file`, `write_file`, `list_directory`, `run_shell_command`, `web_fetch`.
- **Caveat:** Gemini's instruction-following on long prompts (>100K tokens) degrades faster than Claude — keep child prompts ≤30K tokens; cap context loading per phase.

### 3.5 · Copilot CLI

- **Invocation:** `gh copilot suggest "use system-designer at <path>..."` or interactive shell.
- **Tools native:** `read`, `write`, `list`, `bash`.
- **Caveat:** session memory limited; the orchestrator must persist state aggressively in `tracking/project.json` after every phase.

### 3.6 · Codex (OpenAI)

- **Invocation:** Codex CLI `codex` with the folder mounted.
- **Tools native:** `apply_patch` (write), file reads, shell.
- **Caveat:** `apply_patch` expects unified-diff format; the orchestrator's writes get translated to patches.

### 3.7 · Plain LLM with no native file tools

- **Invocation:** copy-paste contents into chat.
- **Pattern:** the LLM emits each intended write as a fenced code block tagged `WRITE: <path>`; the user manually saves. The orchestrator's `<fallback>` block covers this.
- **Limitation:** no auto-fetch, no auto-execution; HITL becomes the default for everything.

## 4 · Drag-folder pattern (the default)

When the user simply drops the folder into any chat:

1. The LLM detects `Sistem_designer/SKILL.md` in the dropped contents.
2. The LLM reads `SKILL.md` first → understands the meta-skill.
3. The LLM reads `system_generator.json` → understands the spec.
4. The LLM reads `prompts/00_master_orchestrator.md` → enters orchestrator role.
5. The LLM begins phase 1 (`read_context`) and proceeds.

No installation step. No registration step. No MCP setup. The orchestrator self-bootstraps by reading.

## 5 · Fallback hierarchy (when a capability is missing)

| Missing capability | Primary fallback | Secondary fallback | Last resort |
|---|---|---|---|
| `xlsx.write` | CSV + MD sidecar | JSON + MD sidecar | manifest in `<final_output>` asking user to render |
| `context7.fetch` | `fetch()` to official URL | `fetch()` to GitHub README raw | `MISSING.md` + escalate at Gate #2 |
| `parallel.spawn` | sequential execution | partial (1 auditor only) | escalate; ask user how many sequential rounds acceptable |
| `now()` | `Bash date` | shell `date` via run_terminal_cmd | ask user at interview start |
| `fs.write` | manifest emitted to user for manual save | abort with manifest dump | abort |
| `WebFetch` (no network) | `library_docs/OFFLINE.md` | continue with declared but un-fetched docs | escalate at Gate #2 |

Each fallback used MUST be logged to `audit/self_audit.md#portability_fallbacks` with:

```
- capability: <name>
  fallback_used: <name>
  reason: <why primary failed>
  impact: <what degraded>
  timestamp: <iso>
```

## 6 · Portability self-test (in self_audit phase)

Regex scans for platform-only identifiers:

```
\b(mcp__\w+|TodoWrite|SubagentType|Skill\(|EnterPlanMode|claude_code_specific|gh\.copilot|cursor_internal|cline_internal)\b
```

Hit in any emitted runtime artifact (CLAUDE.md, prompts, tools, src/) → portability violation, log + iterate.

Hits in `.claude/commands/`, `.claude/settings.json`, or other clearly-Claude-Code convenience layers are allowed IF an equivalent platform-agnostic alternative is also emitted (Tier B, see `system_generator.json#portability_rules`).

## 7 · Convenience layers (optional, on-demand only)

If the interview confirms Claude Code as primary executor, the generator MAY emit:
- `.claude/commands/<name>.md` — slash commands
- `.claude/settings.json` — settings
- `.claude/agents/<name>.md` — subagent definitions
- `.claude/skills/<name>/SKILL.md` — skills

These are convenience, NOT runtime. The runtime contract (orchestrator + tracking + audit + self-audit) MUST work without them.

## 8 · Common pitfalls

| Pitfall | Fix |
|---|---|
| Hardcoding `Skill("name")` in a child prompt | Replace with abstract `prompt_architect(intent)` reference |
| Assuming `mcp__context7__*` tools available | Wrap in `try { context7.fetch } catch { fetch() }` pseudo-code in tool description |
| Calling `TodoWrite` in a non-Claude-Code-runtime prompt | Replace with `tracking/sessions/<id>/tasks.md` file-based equivalent |
| `EnterPlanMode` in orchestrator | Replace with HITL gate emission via `<final_output>` |
| Hardcoding ISO date in template | Use `{{TEMPORAL_NOW}}` placeholder, resolved at render via `now()` |
