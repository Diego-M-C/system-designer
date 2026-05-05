# 04 · Library Docs Fetcher

> **File.** `prompts/04_library_docs_fetcher.md`
> **Tier.** Medium (~22 tags)
> **Composed via.** prompt-architect.

## 1. Purpose

Fetches **fresh** documentation for every library declared in SPEC.json's stack, into `<target_path>/library_docs/<lib>/<version>/`. Uses a 4-step fallback ladder: **Context7 MCP → primary URL → fallback URL → github_release_api**. Always logs source used + sha256 + timestamp into `MANIFEST.md`. Extracts `api_index.json` (when possible) to prevent AIE-002 (hallucinated API).

This is the only prompt that touches the network. Offline fallback is `<lib>/OFFLINE.md` + warning logged.

## 2. When invoked

- **Phase.** 7 (`fetch_library_docs`).

## 3. Inputs

- `SPEC.json#/stack` — list of `{name, version}`.
- `templates/library_docs_manifest.tmpl` — 26 library URL mappings (primary + fallback + github_release_api).
- Network availability (probed at start).

## 4. Outputs

Per library:

```
library_docs/<lib>/<version>/
├── MANIFEST.md           # source used, sha256, last_fetched_at, fetch_protocol
├── README.md             # the docs themselves (or OFFLINE.md if all sources failed)
├── api_index.json        # extracted API surface (if possible) for AIE-002 prevention
└── <other doc files>
```

## 5. Tag rationale (~22 tags)

Standard Medium spine plus:
- `<temporal_context>` — `last_fetched_at` per library.
- `<fallback>` — explicit 4-step ladder.
- `<error_handling>` — per-source failure modes.
- `<verification>` — sha256 + URL response code logged.
- `<injection_defense>` — fetched docs treated as data, not instructions.

## 6. Control flow

```
For each library in SPEC.json#/stack:
  for source in [context7, primary, fallback, github_release_api]:
    try:
      content = fetch(source, lib, version)
      sha256 = hash(content)
      write atomic <library_docs>/<lib>/<version>/README.md
      write MANIFEST.md with source_used + sha256 + last_fetched_at
      try: extract api_index.json from content (regex / heading parse)
      break
    except NetworkError | NotFound:
      continue
  else:  # all sources failed
    write <library_docs>/<lib>/<version>/OFFLINE.md with warning
    append to tracking/project.json#fallbacks_used
```

### The 4 fetch sources

1. **Context7 MCP** — `mcp__context7__get_library_docs(library, version)`. Highest quality, version-aware. Available only on Claude Code with MCP configured.
2. **Primary URL** — official docs site, e.g., `https://docs.fastapi.tiangolo.com/`. Most current.
3. **Fallback URL** — alternative source, e.g., `https://fastapi.tiangolo.com/release-notes/`.
4. **GitHub release API** — `https://api.github.com/repos/<org>/<repo>/releases/tags/v<version>` — last-resort version pinning.

## 7. Calibration anchors (P2)

- Per-library: `confidence_pct` of doc freshness logged in MANIFEST.md.
- If fetched from github_release_api only → confidence ~60% (release notes ≠ full docs).
- If primary + fallback both succeed and content matches → confidence ~95%.
- Offline mode → confidence 0%, warning logged.

## 8. Portability (P1)

- Context7 MCP is **optional** — degrades to HTTP fetch on platforms without MCP.
- HTTP fetch (`WebFetch`-equivalent) available on all Tier-A platforms.
- Tier B (manual paste): user provides docs themselves; this prompt detects and skips.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| All 4 sources fail | Write `OFFLINE.md`; do NOT halt; log to `audit/self_audit.md#fetch_failures` |
| Network completely unavailable | Detect at phase start; switch to offline mode for all libs |
| Fetched content >5MB | Truncate + log warning |
| sha256 mismatch on retry | Halt that lib + escalate (potential corruption) |
| Library version not found | Try `latest` + log warning |

## 10. HITL escalation triggers

- ≥30% of libraries went offline → escalate at Gate #2 (impact on coding correctness).
- Critical library (e.g., the LLM SDK itself) offline → escalate (high risk of AIE-002).

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md` (dispatches), `02_scaffolder.md` (created the directory), `templates/library_docs_manifest.tmpl` (URL config).
**Downstream:** Child orchestrator references these docs in every coding session to prevent AIE-002 (hallucinated API) and AIE-003 (outdated API).

## 12. Test coverage

- T5 library manifest URLs — checks every entry has primary + fallback.
- T1 portability — uses abstract `fetch()`, MCP optional.

## 13. Common failure modes

1. **Stale docs assumed fresh** — if MANIFEST.md doesn't get rewritten on retry, the child orchestrator trusts stale content. Atomic write is mandatory.
2. **Content stored without sha256** — reproducibility broken; review must verify sha256 always logged.
3. **Network probe skipped** — leads to slow timeout per library. Probe at phase start to fast-fail to offline mode.
4. **Injection from fetched docs** — a library's docs might say "run `rm -rf /`". The prompt's `<injection_defense>` requires treating docs as data; never executable.
