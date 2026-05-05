# Anthropic Academy Deep Extraction Report

**Run date:** 2026-04-10
**Tool:** Playwright MCP browser, automated by Claude (Opus 4.6, 1M context)
**Output directory:** `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/`
**Source:** https://anthropic.skilljar.com/

## Executive summary

17 of 17 Anthropic Academy courses were discovered and extracted at the public-page level via Playwright DOM scraping. The original task spec listed 16 courses; an additional course (**Claude Code 101**) was discovered on the homepage and also extracted for completeness.

**Deep lesson content (videos, transcripts, slide text, quiz questions, code examples, downloadable resources) could NOT be extracted because Skilljar requires a logged-in account to access individual lesson pages.** The user was not logged in during this run. A `LOGIN_REQUIRED.md` file in `progress/` documents how to unblock the next phase.

## Coverage metrics

| Metric | Value |
|---|---:|
| Courses discovered | 17 |
| Courses in original task list | 16 |
| Courses extracted (public landing) | 17 / 17 |
| Courses extracted (deep lesson content) | 0 / 17 (login required) |
| Total lectures reported by marketing stats | 398 |
| Total hours of video reported by marketing stats | ~32.45 h |
| Total full-page screenshots captured | 17 |
| Total per-course JSON files written | 17 |
| Total per-course Markdown files written | 17 |
| Transcripts extracted (full) | 0 |
| Transcripts extracted (partial) | 0 |
| Transcripts extracted (none - auth blocker) | 398 lectures blocked |
| Errors logged | 0 |
| Browser crashes | 0 |

## Templates discovered

Skilljar courses on this site use TWO different landing-page templates:

- **`sj` (old Skilljar curriculum template)** — Exposes the full list of individual lesson titles on the public landing page via `ul.dp-curriculum > li.section / li.lesson-modular`. 4 courses use this template.
- **`clp` (new custom "course landing page")** — Only exposes section-level info (`clp__section-block` with name, lesson count, and description) plus 3 preview screenshots per section. Individual lesson titles are gated. 13 courses use this template.

## Courses with lesson-level public data (sj template)

| # | Slug | Lessons visible |
|---|------|----------------:|
| 3 | claude-101 | 14 |
| 4 | introduction-to-claude-cowork | 10 |
| 14 | introduction-to-agent-skills | 6 |
| 15 | introduction-to-subagents | 4 |

## Courses with only section-level public data (clp template)

| # | Slug | Sections | Total lectures marketed |
|---|------|---------:|------------------------:|
| 1 | claude-with-the-anthropic-api | 7 | 84 |
| 2 | claude-code-in-action | 1 | 15 |
| 5 | ai-fluency-framework-foundations | 2 | 14 |
| 6 | introduction-to-model-context-protocol | 2 | 16 |
| 7 | ai-fluency-for-educators | 2 | 4 |
| 8 | ai-fluency-for-students | 3 | 5 |
| 9 | model-context-protocol-advanced-topics | 2 | 15 |
| 10 | claude-in-amazon-bedrock | 6 | 85 |
| 11 | claude-with-google-vertex | 7 | 85 |
| 12 | teaching-ai-fluency | 3 | 7 |
| 13 | ai-fluency-for-nonprofits | 4 | 9 |
| 16 | ai-capabilities-and-limitations | 6 | 13 |
| 17 | claude-code-101 | 4 | 12 |

## What was extracted per course (examples of depth)

### Example 1 — AI Fluency: Framework & Foundations (course 05)
Extracted from `clp__main-content`:
- Full multi-paragraph course back-story and partnership history
- Full instructor bios for Drew Bent, Rick Dakan, Joseph Feller, Maggie Vo
- Complete AI diligence statement about Claude 3.7's role in authoring the course
- Saved as `transcripts/course_05_fulltext.md`

### Example 2 — AI Capabilities and Limitations (course 16)
Extracted the full four-property framework for LLMs:
- Next Token Prediction
- Knowledge
- Working Memory
- Steerability

Plus detailed per-section descriptions explaining each property's practical implications.

### Example 3 — Claude Code 101 (course 17, bonus)
Extracted the full agentic loop framework:
- "gather context → take action → verify results"
- The Explore → Plan → Code → Commit rhythm for daily workflows
- CLAUDE.md file role, subagents, skills, MCP servers, hooks

## Files produced

### Root
- `ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.md` — Master aggregated reference (v2 deep)
- `ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.json` — Master aggregated JSON
- `EXTRACTION_REPORT.md` — This file
- `build_markdown.py` — Python script used to compile per-course markdown from JSON

### `json/` — 17 per-course structured JSON files
Names: `course_01_claude-with-the-anthropic-api_curriculum.json` … `course_17_claude-code-101_curriculum.json`

### `md/` — 17 per-course deep markdown files
Names: `course_01_claude-with-the-anthropic-api_deep.md` … `course_17_claude-code-101_deep.md`

### `screenshots/` — 17 full-page PNG screenshots
One full-page PNG per course landing page.

### `transcripts/`
- `course_05_fulltext.md` — Full extracted main content text for AI Fluency: Framework & Foundations (the richest content page).

### `progress/`
- `GLOBAL_PROGRESS.json` — Current pipeline state
- `LOGIN_REQUIRED.md` — Blocker details + unblock instructions
- `course_list.json` — Initial course list

### `errors/`
- (empty — no extraction errors occurred)

## Blockers and next steps

### Blocker
Individual lesson content (the richest and most valuable material: actual video transcripts, slide text, code examples, quiz questions, downloadable resources, CLAUDE.md templates, MCP server code snippets) is behind `auth/login` and can only be retrieved after a human logs in via the Playwright browser window.

### Next recommended actions
1. **User action:** Sign in at https://anthropic.skilljar.com/auth/login in the already-open Playwright browser window, enroll in all 17 courses (free), then reply `logged in`.
2. **Claude action (after login):** Navigate into each lesson page one-by-one via the authenticated session, call `browser_evaluate` to extract transcript text from `.lesson-content`, `.transcript`, `.captions`, Vimeo/Wistia transcript APIs, and `video > track` elements. Capture mid-lesson screenshots for slides, code blocks, and diagrams. Save per-lesson JSON+screenshots under `transcripts/course_XX/lesson_YY.json`.
3. **Claude action:** Once all 398 lectures have been traversed, regenerate the master reference as `ENGINEERING_INTELLIGENCE_V2.md` with the new per-lesson content.

## Self-evaluation

| Criterion | Score | Notes |
|---|---|---|
| Coverage | 17/17 public pages, 0/398 lessons | Public coverage 100%; deep coverage 0% (login blocker) |
| Citation | Every record includes `source_url` and `extraction_timestamp` | 100% |
| Fabrication | Zero invented content. All fields trace to DOM selectors on public pages. | Pass |
| Structure | Per-course MD+JSON, master MD+JSON, progress/errors dirs, screenshots | Pass |
| Useful beyond prior landing-page reports | Yes: adds section descriptions, stats, learning objectives, prerequisites, instructor bios, full AI diligence statement for course 5, four-property framework for course 16, extracted where prior reports only captured course card blurbs. | Pass |

## Sign-off

Extraction pipeline completed Phase 1-5 successfully for all public content. Phase 4 (deep lesson extraction) is blocked on user authentication and is ready to resume immediately upon user providing login.
