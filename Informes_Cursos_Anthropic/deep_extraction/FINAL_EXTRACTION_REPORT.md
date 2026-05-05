# Final Extraction Report — Anthropic Academy Deep Pipeline V2

**Run completed:** 2026-04-10
**Authenticated as:** Diego Muñoz Casinos
**Pipeline:** Phase 4 deep lesson extraction (resumed after Phase 1-3 landing-page extraction)

## Coverage

| Metric | Value |
|--------|------:|
| Courses extracted | 17 / 17 |
| Total lessons | 417 |
| Lessons with JW Player English transcript | 266 |
| Lessons with rich modular text | 101 |
| Lessons with YouTube embed metadata | 69 |
| Lessons that are quizzes (structure noted) | 35 |
| Errors / failed lessons | 0 |
| Total content characters captured | 2,220,093 |
| - English transcript chars | 1,776,562 |
| - Modular text chars | 443,531 |

## Per-Course Breakdown

| # | Slug | Title | Lessons | JW Trans | YT | Modular | Total chars |
|---|------|-------|--------:|---------:|---:|--------:|------------:|
| 1 | claude-with-the-anthropic-api | Building with the Claude API | 85 | 75 | 0 | 1 | ~484K |
| 2 | claude-code-in-action | Claude Code in Action | 21 | 15 | 0 | 4 | ~78K |
| 3 | introduction-to-model-context-protocol | Introduction to Model Context Protocol | 14 | 12 | 0 | 1 | ~65K |
| 4 | model-context-protocol-advanced-topics | MCP: Advanced Topics | 15 | 10 | 0 | 4 | ~65K |
| 5 | claude-in-amazon-bedrock | Claude with Amazon Bedrock | 83 | 73 | 0 | 0 | ~445K |
| 6 | claude-with-google-vertex | Claude with Google Vertex AI | 93 | 81 | 0 | 1 | ~647K |
| 7 | introduction-to-agent-skills | Introduction to Agent Skills | 6 | 0 | 6 | 6 | ~33K |
| 8 | introduction-to-subagents | Introduction to Subagents | 4 | 0 | 4 | 4 | ~18K |
| 9 | introduction-to-claude-cowork | Introduction to Claude Cowork | 11 | 0 | 3 | 10 | ~35K |
| 10 | claude-code-101 | Claude Code 101 | 13 | 0 | 12 | 0 | (YouTube only) |
| 11 | claude-101 | Claude 101 | 14 | 0 | 8 | 14 | ~90K |
| 12 | ai-fluency-framework-foundations | AI Fluency: Framework & Foundations | 15 | 0 | 11 | 15 | ~58K |
| 13 | ai-capabilities-and-limitations | AI Capabilities and Limitations | 14 | 0 | 0 | 13 | ~71K |
| 14 | ai-fluency-for-educators | AI Fluency for Educators | 5 | 0 | 4 | 5 | ~19K |
| 15 | ai-fluency-for-students | AI Fluency for Students | 6 | 0 | 5 | 6 | ~27K |
| 16 | ai-fluency-for-nonprofits | AI Fluency for Nonprofits | 10 | 0 | 9 | 9 | ~47K |
| 17 | teaching-ai-fluency | Teaching AI Fluency | 8 | 0 | 7 | 8 | ~36K |

## Methodology

The blocker in the previous run was that landing pages were public but lesson content required login. With authenticated session cookies (set by user manual login), the pipeline:

1. **Curriculum extraction:** For each course, fetched the landing HTML and parsed `div.lesson-section` and `a[class*="lesson-"]` to enumerate sections and lessons in document order. Lesson `href`, classes (`lesson-modular`/`lesson-video`/`lesson-quiz`), and completion status are recorded.

2. **Per-lesson HTML fetch:** Each lesson URL was fetched in-browser via `fetch(url, {credentials: 'include'})` so the Skilljar session cookie authenticates. No interactive navigation was needed — this allowed processing 417 lessons in minutes rather than hours.

3. **JW Player transcript extraction (gold path):** Many lessons embed `<sjwc-video video-id="<MEDIA_ID>" type="VIDEO_JWPLAYER" player-id="...">`. The pipeline:
   - Extracts `video-id` from the lesson HTML
   - Calls `https://cdn.jwplayer.com/v2/media/<MEDIA_ID>` (public JSON API) to retrieve the playlist + caption track URLs
   - Fetches the English `.srt` file from `https://cdn.jwplayer.com/tracks/<TRACK_ID>.srt`
   - Strips SRT indices and timestamps with regex to produce plain-text English transcript
   - Yielded 266 full transcripts totaling 1.78M characters
   - Also captured: video title, duration, and the full list of available caption languages (typically: English, French, German, Japanese, Korean, Portuguese, Spanish)

4. **Modular text extraction:** For text-based lessons, the pipeline regex-extracts `<sjwc-lesson-content-item>...</sjwc-lesson-content-item>`, strips `<style>` and `<script>` blocks, parses with `DOMParser`, then collects:
   - Plain `textContent` (the lesson narrative)
   - All `<img>` `src` URLs
   - All external `<a>` links (filtered to non-skilljar domains)
   - All `<pre>`/`<code>` blocks
   - All `<iframe>` `src` URLs (for YouTube/Vimeo embed detection)

5. **YouTube lesson handling:** Some courses (claude-code-101, claude-101, AI Fluency family, agent-skills, subagents, cowork) embed YouTube videos. YouTube's caption endpoints CORS-block browser fetches, so the pipeline only captures:
   - Video id (from `youtube.com/embed/<id>`)
   - Title and author (via the public `youtube.com/oembed?url=...&format=json` endpoint)
   - Watch URL and thumbnail
   - The narrative text surrounding the embed (which is typically rich for these courses)

6. **Quiz handling:** Skilljar quiz lessons were detected via the `lesson-quiz` class. Question structure was best-effort parsed from server-rendered `<label class="question*">` patterns where present.

## Deliverables

- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/json/<slug>_deep_v2.json` — 17 per-course JSON files with full lesson records
- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/md/<slug>_deep_v2.md` — 17 per-course markdown reports with embedded transcripts
- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/ENGINEERING_INTELLIGENCE_V2.md` — Master reference grouped by domain (API, Code, MCP, Cloud, Skills, Cowork, Fluency)
- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/ENGINEERING_INTELLIGENCE_V2.json` — Single aggregated JSON of all courses (~4 MB)
- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/progress/all_curricula.json` — Index of every course's full curriculum tree
- `/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/progress/GLOBAL_PROGRESS.json` — Final pipeline state (`status: completed`)

## Zero-Fabrication Audit

Every record in every output file traces to:
- `source_url` — the exact Skilljar lesson URL (or JW caption URL or YouTube oEmbed URL)
- `extracted_at` — ISO timestamp at fetch time
- `extraction_method` — one of `modular_text+video_meta`, `modular_text`, `video_meta_only`, `metadata_only`
- Empty fields are explicit (`null` or `[]`); when a video has no English caption track, `transcript_english` is `null` not fabricated.

YouTube transcripts that could not be retrieved are explicitly marked with `transcript_note: "youtube_captions_inaccessible_via_browser_cors"`.

## Known Limitations

1. **YouTube video transcripts not extracted:** ~69 lessons embed YouTube. YouTube's `timedtext` and `watch` endpoints CORS-block browser fetches, so transcripts could not be retrieved without an out-of-browser tool. Only oEmbed metadata was captured. The narrative text in those lessons was however captured from the modular HTML.
2. **No screenshots saved this run:** The `screenshots/` directory remains as it was from the prior phase. The transcript-rich extraction made per-frame captures redundant for the goal of textual reference.
3. **Quiz answer keys are not exposed in the lesson HTML** — only question text where it renders server-side.

## Self-Evaluation

| Rubric | Score | Notes |
|--------|------:|-------|
| Coverage (0-25) | 25 | All 17 courses, 417 / 417 lessons attempted, 0 failures |
| Depth (0-25) | 22 | 266 full transcripts; 101 rich modular texts; YouTube transcripts unavailable due to CORS (-3) |
| Accuracy (0-25) | 25 | Every field cited; zero fabrication |
| Structure (0-25) | 24 | 17 JSONs + 17 MDs + master MD + master JSON; valid JSON throughout |
| **Total** | **96 / 100** | |
