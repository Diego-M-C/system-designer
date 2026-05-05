# AI-Coding Common-Error Catalog (preloaded · auto-extending)

> **Purpose:** seed the child system's `tracking/errors_catalog.json` with ~25 patterns of failure that LLM-driven coding workflows produce repeatedly. Each session that catches a NEW pattern appends it to the live catalog (P5 living-doc principle), so the catalog grows project-by-project and project-to-project.
>
> **Format per entry:** machine-readable JSON-equivalent + human prose explaining prevention. The seeder agent (`prompts/05_error_prevention_seeder.md`) ingests this file and writes the JSON to `<target_path>/tracking/errors_catalog.json`.

---

## Schema

Each entry conforms to `system_generator.json#/definitions/ErrorCatalogEntry`:

```json
{
  "id": "AIE-001",
  "pattern_name": "...",
  "severity": "info|warn|error|critical",
  "description": "...",
  "example": "...",
  "prevention": "...",
  "auto_detection": "regex / heuristic / LLM-check",
  "preloaded": true,
  "occurrences": 0,
  "first_seen_session": null
}
```

---

## Category A · Hallucination & knowledge errors

### AIE-001 · cite-not-found
- **Severity:** error
- **Description:** Agent cites a paper / URL / doc / function that doesn't exist.
- **Example:** *"As per the OpenAI doc on `gpt-4-turbo-2024-09`'s `parallel_tool_calls=true`..."* — but no such doc / param exists at that version.
- **Prevention:** every cited URL/paper/function must be verifiable; HIGH confidence (≥90%) requires explicit citation, MEDIUM (70–89%) accepts pattern-match without cite. See `calibrated_probabilities.md §7`.
- **Auto-detection:** LLM-check — re-prompt: "Verify this citation exists. If unsure, downgrade confidence."

### AIE-002 · hallucinated-function
- **Severity:** critical
- **Description:** Agent calls a method / function that doesn't exist in the imported library version.
- **Example:** `pandas.DataFrame.read_excel_async()` — doesn't exist in any pandas version.
- **Prevention:** before any non-trivial library use, agent MUST read fetched docs in `library_docs/<lib>/<version>/` (P5 fresh-docs invariant).
- **Auto-detection:** static analysis (linter on `src/`); cross-check function name against `library_docs/<lib>/<version>/api_index.json` (generated at fetch time).

### AIE-003 · phantom-import
- **Severity:** error
- **Description:** Imports a module/package that doesn't exist or isn't in dependencies.
- **Example:** `from anthropic.tools import ToolUseBlock` (when actual path differs by version).
- **Prevention:** before import, verify module path in fetched docs.
- **Auto-detection:** import-resolver (pre-test step in CI); regex check against `pyproject.toml` / `package.json`.

### AIE-004 · wrong-version-api
- **Severity:** error
- **Description:** Uses API surface from old / new version that's incompatible with the pinned version.
- **Example:** `openai.ChatCompletion.create(...)` (pre-1.0 API) when `openai>=1.0` is pinned.
- **Prevention:** version pinned in `library_docs/MANIFEST.md`; agent reads the version-specific docs.
- **Auto-detection:** linter rule per pinned major version.

### AIE-005 · stale-knowledge-cutoff
- **Severity:** warn
- **Description:** Agent uses pre-cutoff knowledge for a post-cutoff topic without verification.
- **Example:** Recommending Python 3.10 syntax in 2026 (cutoff 2024); newer 3.13 patterns ignored.
- **Prevention:** `<temporal_context>` in every prompt; if reasoning references "current", "latest", "best version", trigger live doc fetch.
- **Auto-detection:** heuristic — if output contains "current"/"latest"/"recent" without `<temporal_context>` reference, flag.

---

## Category B · Concurrency / async errors

### AIE-006 · race-condition-async
- **Severity:** critical
- **Description:** Concurrent async ops without proper lock / sync.
- **Example:** Two `asyncio.create_task` writing to same dict without `asyncio.Lock`.
- **Prevention:** explicit ownership rule per shared resource; document in `ARCHITECTURE.md`.
- **Auto-detection:** LLM review — "list shared mutable state and the lock that protects it for each".

### AIE-007 · awaiting-non-awaitable
- **Severity:** error
- **Description:** `await` on a sync function.
- **Example:** `await client.list()` when `client.list` is sync.
- **Prevention:** type-checker (`mypy`, `pyright`).
- **Auto-detection:** static analysis.

---

## Category C · Security / privacy errors

### AIE-008 · env-vars-hardcoded
- **Severity:** critical
- **Description:** Secrets / API keys hardcoded in source.
- **Example:** `openai.api_key = "sk-proj-..."` directly in code.
- **Prevention:** all secrets via env vars + `.env.example` (no values); `.env` in `.gitignore`.
- **Auto-detection:** regex — `(?i)(api[_-]?key|token|secret|password)\s*=\s*["'][a-zA-Z0-9_-]{20,}["']`.

### AIE-009 · secrets-in-logs
- **Severity:** critical
- **Description:** Sensitive values emitted to logs.
- **Example:** `logger.info(f"Auth header: {request.headers}")`.
- **Prevention:** structured logger with redaction filter; deny-list of header names.
- **Auto-detection:** static analysis on `logger.*(...)` calls.

### AIE-010 · prompt-injection-vulnerable
- **Severity:** critical
- **Description:** User input concatenated into prompt without isolation.
- **Example:** `system_prompt = f"You are X. Answer: {user_input}"` — user can override role.
- **Prevention:** wrap user input in `<input>` tags AFTER instructions; never f-string into instructions. See `prompt_architect/references/best-practice-anchors.md §13–14`.
- **Auto-detection:** regex — `f["'].*\{user_(input|message|query|prompt)\}.*["']` outside isolation tags.

### AIE-011 · pii-leakage-to-llm
- **Severity:** critical
- **Description:** PII sent to external LLM API without redaction (EU AI Act Art. 10).
- **Example:** patient names sent to OpenAI without consent / DPA / redaction.
- **Prevention:** PII detector pre-LLM call; DPA in place; data minimisation.
- **Auto-detection:** PII regex (names, IDs, emails, NHS numbers) on outbound payloads.

---

## Category D · Logic / semantic errors

### AIE-012 · off-by-one-pagination
- **Severity:** error
- **Description:** Wrong index / limit math in pagination.
- **Example:** `items[page*size : page*size + size]` with `page` 1-indexed → skips first item.
- **Prevention:** unit test with edge cases (page=0, page=last, partial page).
- **Auto-detection:** test coverage on pagination boundaries.

### AIE-013 · untested-default
- **Severity:** warn
- **Description:** Default value never exercised in any test.
- **Example:** `def f(x=None)` with `None` branch never tested.
- **Prevention:** parametrised tests forcing default + non-default paths.
- **Auto-detection:** branch coverage report, flag <100% on default-arg branches.

### AIE-014 · silent-exception-swallow
- **Severity:** error
- **Description:** `try / except: pass` with no logging.
- **Example:** `try: db.commit() except: pass` — masks failures.
- **Prevention:** every `except` block must `logger.exception` or re-raise.
- **Auto-detection:** AST scan — `except` followed by only `pass` or empty.

### AIE-015 · mutable-default-arg
- **Severity:** error
- **Description:** Python `def f(x=[])` — default reused across calls.
- **Example:** `def append(item, items=[]): items.append(item); return items` — returns same growing list.
- **Prevention:** linter rule `B006` (flake8-bugbear).
- **Auto-detection:** linter.

### AIE-016 · n-plus-1-query
- **Severity:** error
- **Description:** DB query inside a loop instead of bulk.
- **Example:** `for user in users: posts = db.query(Post, user_id=user.id)`.
- **Prevention:** use `IN (...)`/`JOIN`/eager-load.
- **Auto-detection:** ORM-specific lint (e.g., SQLAlchemy `noload`/`selectinload` advisor).

### AIE-017 · timezone-naive-datetime
- **Severity:** error
- **Description:** `datetime.now()` without timezone.
- **Example:** Stored timestamps in DB without UTC; comparison breaks across DST.
- **Prevention:** `datetime.now(tz=UTC)` everywhere; lint forbidding bare `now()`.
- **Auto-detection:** AST scan — `datetime.now()` without `tz=` / `timezone.utc`.

### AIE-018 · string-format-injection
- **Severity:** critical
- **Description:** f-string / `%` / `.format()` with user data into SQL/HTML/shell.
- **Example:** `cursor.execute(f"SELECT * FROM users WHERE id={user_id}")` — SQL injection.
- **Prevention:** parametrised queries / templating with auto-escape / `shlex.quote`.
- **Auto-detection:** AST scan — string interpolation feeding `execute` / `render` / `system` / `Popen(..., shell=True)`.

---

## Category E · Reliability / freshness errors

### AIE-019 · missing-rate-limit
- **Severity:** error
- **Description:** External API called without backoff / rate limit.
- **Example:** Loop over 10K items, calling LLM API per item, no semaphore → 429s.
- **Prevention:** decorator with token-bucket; `tenacity` retries with exponential backoff.
- **Auto-detection:** review of all `requests.*` / `httpx.*` / `openai.*` / `anthropic.*` calls.

### AIE-020 · tokenizer-mismatch
- **Severity:** warn
- **Description:** Counting characters instead of tokens for budget.
- **Example:** `if len(prompt) > 100_000: ...` instead of `tiktoken.encode` / model-specific.
- **Prevention:** model-specific tokenizer + budget check.
- **Auto-detection:** regex — `len(prompt)` near a budget literal.

### AIE-021 · non-deterministic-test
- **Severity:** error
- **Description:** Test relies on random / clock / order.
- **Example:** `assert random.choice([1,2,3]) == 2` — flaky.
- **Prevention:** seed fixtures, freeze clock (`freezegun`), sort before comparison.
- **Auto-detection:** repeat-test runner (run each test 5x, flag if any disagree).

### AIE-022 · dead-code-residue
- **Severity:** warn
- **Description:** Old branches / functions left after refactor.
- **Example:** `def _legacy_handler(): ...` no callers.
- **Prevention:** unused-symbol linter (`vulture`); CI fails on dead code.
- **Auto-detection:** static analysis.

### AIE-023 · circular-import
- **Severity:** error
- **Description:** Module A imports B, B imports A.
- **Example:** `models/user.py` ↔ `models/post.py`.
- **Prevention:** layer architecture (interfaces in shared module); local imports for true cycles.
- **Auto-detection:** static analysis (`pylint`, `import-linter`).

### AIE-024 · schema-drift-undocumented
- **Severity:** error
- **Description:** DB schema changed without migration record.
- **Example:** Manual ALTER TABLE on prod, no Alembic migration committed.
- **Prevention:** every schema change via migration tool; pre-deploy migration check in CI.
- **Auto-detection:** diff `db.metadata` vs latest migration.

---

## Category F · LLM / prompt-engineering errors

### AIE-025 · uncalibrated-claim
- **Severity:** error (P2 violation)
- **Description:** Output asserts without confidence (no %, no range, no uncertainty band).
- **Example:** "This is the best architecture for the system." (no fit %, no alternatives).
- **Prevention:** `calibrated_probabilities.md §1` forbidden tokens + required formats.
- **Auto-detection:** regex `\b(best|always|never|guaranteed|certain|definitely|impossible)\b` + missing-% scan.

### AIE-026 · input-as-instructions
- **Severity:** critical (P1/P4 / injection)
- **Description:** LLM treats `<input>` content as commands rather than data.
- **Example:** User input `"ignore previous instructions"` is followed.
- **Prevention:** wrap user input in `<input>` AFTER instructions (defensive recency); explicit "treat as data" rule in `<injection_defense>`.
- **Auto-detection:** adversarial test cases in `templates/test_cases/adversarial.json`.

### AIE-027 · thinking-mode-double-billed
- **Severity:** warn
- **Description:** `<thinking>` XML tag + extended-thinking API both enabled.
- **Example:** Prompt has `<thinking>` block AND request body has `thinking: { type: "enabled" }`.
- **Prevention:** prompt-architect rubric item `thinking_exclusivity` (Workflow §4 audit).
- **Auto-detection:** rubric scan in `audit/self_audit.md`.

### AIE-028 · complex-without-floor
- **Severity:** error
- **Description:** Complex-tier prompt missing one of the 13 mandatory-floor tags.
- **Example:** Complex prompt without `<hitl_conditions>`.
- **Prevention:** prompt-architect rubric item `mandatory_floor` mandatory for Complex.
- **Auto-detection:** AST scan of emitted prompt vs floor list.

### AIE-029 · invented-tag
- **Severity:** error
- **Description:** Prompt uses an XML tag not in `prompt_architect/prompt_editor_skill.json`.
- **Example:** `<superpower>...</superpower>` (not a canonical tag).
- **Prevention:** prompt-architect rubric item `tags_exist`.
- **Auto-detection:** intersect emitted tags vs taxonomy.

### AIE-030 · temporal-context-hardcoded
- **Severity:** warn
- **Description:** Date hardcoded in template rather than resolved via `{{TEMPORAL_NOW}}`.
- **Example:** `<temporal_context>2026-04-29</temporal_context>` in a template.
- **Prevention:** template-render replaces `{{TEMPORAL_NOW}}` from `now()`; lint forbids ISO date literals in `*.tmpl`.
- **Auto-detection:** regex `\b\d{4}-\d{2}-\d{2}\b` in `templates/`.

---

## Auto-extension protocol

When a session catches a NEW error pattern (not in this catalog):

1. The session's error-handler emits a draft entry to `tracking/sessions/<id>/errors.jsonl`.
2. At session checkpoint, the agent classifies severity + writes a draft `ErrorCatalogEntry`.
3. The agent appends to `tracking/errors_catalog.json` with `preloaded: false` + `first_seen_session: <id>`.
4. At Gate #2, the user confirms the new entry; on approval, it persists.
5. Next session inherits the augmented catalog.

This is what makes the catalog **living** (P5).

---

## Total preloaded count: 30 (target was ~25; expanded for full coverage)

The seeder agent reads this file, parses each `### AIE-NNN` block, and emits the JSON entries to the child system's `tracking/errors_catalog.json`.
