# JW Player & Quiz Recovery Report

## Date: 2026-04-12

---

## PART A: JW Player Transcript Recovery

### Summary
- **Videos attempted:** 3
- **Transcripts recovered:** 0
- **Confirmed no captions:** 3

### Details

All three JW Player videos have **zero caption tracks** on the CDN. Only thumbnail strip VTT files exist.

| Media ID | Course | Lesson | Title | Duration | Result |
|----------|--------|--------|-------|----------|--------|
| SmAEl9b8 | claude-in-amazon-bedrock | 33 | Handling tool use responses | 705s | No captions (thumbnails only) |
| h63mMcLg | claude-in-amazon-bedrock | 43 | Introducing Retrieval Augmented Generation | 351s | No captions (thumbnails only) |
| hlYSjyD6 | claude-with-google-vertex | 30 | Exercise on prompting | 322s | No captions (thumbnails only) |

### Notes
- These videos were uploaded to JW Player without any caption/subtitle tracks
- No alternative languages available (not even auto-generated)
- The only track type present is `thumbnails` (preview strip images)
- These represent a genuine content gap that cannot be filled from the CDN

---

## PART B: Quiz Content Extraction

### Summary
- **Quizzes attempted:** 36
- **Fully extracted (all questions):** 14
- **Partially extracted (Q1 only):** 22
- **Total questions extracted:** 152
- **Questions from completed quizzes:** 130 (with correct answer markings)
- **Questions from untaken quizzes:** 22 (Q1 only, no correct answers)

### Extraction by Course

| Course | Quizzes | Fully Extracted | Partial | Total Qs |
|--------|---------|----------------|---------|----------|
| ai-capabilities-and-limitations | 1 | 1 (13 Qs) | 0 | 13 |
| ai-fluency-for-nonprofits | 1 | 0 | 1 | 1 |
| claude-code-101 | 1 | 1 (7 Qs) | 0 | 7 |
| claude-code-in-action | 2 | 2 (11 Qs) | 0 | 11 |
| claude-in-amazon-bedrock | 8 | 0 | 8 | 8 |
| claude-with-google-vertex | 10 | 0 | 10 | 10 |
| claude-with-the-anthropic-api | 9 | 9 (72 Qs) | 0 | 72 |
| introduction-to-claude-cowork | 1 | 0 | 1 | 1 |
| introduction-to-model-context-protocol | 2 | 2 (10 Qs) | 0 | 10 |
| model-context-protocol-advanced-topics | 1 | 0 | 1 | 1 |

### Why 22 Quizzes Were Only Partially Extracted

Skilljar renders quiz questions **one at a time** for untaken quizzes. The "Next Question" button requires selecting an answer before advancing. Since the constraint was to NOT submit quiz answers, only the first question could be extracted from untaken quizzes.

**Courses not yet taken by the user:**
- claude-in-amazon-bedrock (all 8 quizzes)
- claude-with-google-vertex (all 10 quizzes)
- ai-fluency-for-nonprofits (1 quiz)
- introduction-to-claude-cowork (1 quiz)
- model-context-protocol-advanced-topics (1 quiz)

**Note:** The bedrock and vertex courses share nearly identical quiz content with the anthropic-api course (same topics, similar questions). The fully extracted anthropic-api quizzes provide comprehensive coverage of the assessment material.

### Fully Extracted Quiz Highlights

**claude-with-the-anthropic-api - Final Assessment (23 questions)**
Covers: API basics, tool use, prompt engineering, prompt evaluation, MCP, agents/workflows, features (caching, citations, extended thinking, computer use)

**ai-capabilities-and-limitations - Course Quiz (13 questions)**
Covers: Pretraining, fine-tuning, next token prediction, hallucination, knowledge cutoff, working memory, steerability, calibrated trust, 4D Framework

**claude-code-in-action - Quiz on Claude Code (8 questions)**
Covers: Tool system, MCP integration, Plan vs Thinking mode, CLAUDE.md files, custom commands, hooks

### Output Files

All quiz data saved to:
`deep_extraction/transcripts/quizzes/`

- 12 individual course quiz JSON files (completed quizzes with full Q&A)
- 1 summary JSON (`_quiz_extraction_summary.json`) containing all data including partial extractions

---

## Metrics

| Metric | Value |
|--------|-------|
| jw_recovered | 0 |
| jw_failed | 3 (no captions available) |
| quizzes_parsed | 36 |
| quizzes_fully_extracted | 14 |
| quizzes_partial | 22 |
| questions_extracted | 152 |
| questions_with_correct_answers | 130 |
