# AUDIT REPORT V3 -- Anthropic Academy Deep Extraction Quality Audit

**Version:** 3.0  
**Date:** 2026-04-10  
**Auditor:** Claude Opus 4.6 -- Quality Audit Agent  
**Source:** 17 `*_deep_v2.json` files in `deep_extraction/json/`

---

## Executive Summary

The deep extraction pipeline processed **17 courses** containing **417 lessons** from the Anthropic Academy platform. The audit finds an overall content coverage of **90.9%** (379/417 lessons with extractable content), with **1.78M characters** of video transcripts captured across 266 JW Player lessons. The weighted average quality score across all courses is **69.8/100**.

The primary quality gap is the absence of transcripts for **69 YouTube-hosted videos** across 10 courses (CORS-blocked during browser extraction). Resolving this single gap would raise the average quality score to approximately **85-90/100**.

### Key Metrics at a Glance

| Metric | Value |
|--------|-------|
| Total courses | 17 |
| Total lessons | 417 |
| Lessons with content | 379 (90.9%) |
| Lessons with video | 338 (81.1%) |
| Lessons with transcript | 266 (63.8%) |
| Transcript chars | 1,776,562 |
| Modular text chars | 443,531 |
| Modular HTML chars | 1,149,473 |
| Code blocks | 154 (153 existing + 1 new) |
| Images cataloged | 69 |
| External links cataloged | 188 |
| Quizzes detected | 35 |
| Average quality score | 69.8 / 100 |

---

## Quality Score Methodology

Each course receives a score from 0 to 100 computed as:

```
Quality Score = Content Coverage (0-40) + Transcript Depth (0-30)
              + Resource Richness (0-15) + Structural Integrity (0-15)
```

| Component | Weight | Formula |
|-----------|--------|---------|
| Content Coverage | 40% | (lessons_with_content / total_lessons) * 40 |
| Transcript Depth | 30% | min(avg_transcript_chars / 3000, 1.0) * 30 |
| Resource Richness | 15% | min((code + images + links) / (lessons * 3), 1.0) * 15 |
| Structural Integrity | 15% | (valid_titles + valid_sections + valid_urls) / (lessons * 3) * 15 |

**Content** = lesson has modular_text, modular_html > 50 chars, or transcript chars > 0.  
**Transcript Depth** saturates at 3,000 chars/lesson (approx 3 minutes of speech).  
**Resource Richness** saturates when each lesson averages 3+ resources (code + images + links).

---

## Global Summary Table -- All 17 Courses

```
Rank | Score |  Lessons | Content% | Transc% | Code | Imgs | Links | Course
-----+-------+----------+----------+---------+------+------+-------+--------------------------------
  1  | 95.2  |   21     |  90.5%   | 100.0%  |   51 |    1 |     7 | Claude Code in Action
  2  | 82.3  |   15     |  93.3%   | 100.0%  |    0 |    0 |     0 | MCP: Advanced Topics
  3  | 82.1  |   14     |  92.9%   | 100.0%  |    0 |    0 |     0 | Introduction to MCP
  4  | 81.1  |   85     |  89.4%   | 100.0%  |    0 |    4 |     1 | Building with the Claude API
  5  | 80.8  |   93     |  88.2%   |  98.8%  |    4 |    3 |     2 | Claude with Google Vertex
  6  | 80.2  |   83     |  88.0%   |  97.3%  |    0 |    0 |     0 | Claude with Amazon Bedrock
  7  | 70.0  |   14     | 100.0%   |   0.0%  |    0 |    5 |    55 | Claude 101
  8  | 70.0  |    6     | 100.0%   |   0.0%  |   61 |   12 |     6 | Intro to Agent Skills
  9  | 70.0  |    4     | 100.0%   |   0.0%  |   33 |    7 |     0 | Intro to Subagents
 10  | 66.4  |   11     |  90.9%   |   0.0%  |    5 |   17 |    41 | Intro to Claude Cowork
 11  | 61.1  |   14     |  92.9%   |   0.0%  |    0 |   20 |     9 | AI Capabilities & Limitations
 12  | 61.0  |   15     | 100.0%   |   0.0%  |    0 |    0 |    18 | AI Fluency: Framework
 13  | 59.4  |    8     | 100.0%   |   0.0%  |    0 |    0 |    14 | Teaching AI Fluency
 14  | 59.2  |    6     | 100.0%   |   0.0%  |    0 |    0 |    11 | AI Fluency for Students
 15  | 59.0  |    5     | 100.0%   |   0.0%  |    0 |    0 |    11 | AI Fluency for Educators
 16  | 57.0  |   10     |  90.0%   |   0.0%  |    0 |    0 |    13 | AI Fluency for Nonprofits
 17  | 51.9  |   13     |  92.3%   |   0.0%  |    0 |    0 |     0 | Claude Code 101
```

### Quality Distribution (ASCII Histogram)

```
Score Range  | Count | Bar
-------------+-------+--------------------------------------------------
 90 - 100    |   1   | #
 80 -  89    |   5   | #####
 70 -  79    |   3   | ###
 60 -  69    |   3   | ###
 50 -  59    |   5   | #####
  0 -  49    |   0   |
```

---

## Per-Course Detail Sections

### 1. Claude Code in Action (95.2/100) -- HIGHEST

| Metric | Value |
|--------|-------|
| Lessons | 21 (4 sections) |
| Content coverage | 19/21 (90.5%) |
| Video/Transcript | 15 JW Player / 15 transcripts (100%) |
| Avg transcript | 4,837 chars |
| Code blocks | 51 |
| Images | 1 |
| Links | 7 |
| Quizzes | 2 |

**Strengths:** Full JW Player transcript coverage, rich code block extraction (51 blocks). Highest overall score.  
**Gaps:** 2 lessons without content (quiz lessons). Modular text is sparse (5,795 chars).

---

### 2. MCP: Advanced Topics (82.3/100)

| Metric | Value |
|--------|-------|
| Lessons | 15 (4 sections) |
| Content coverage | 14/15 (93.3%) |
| Video/Transcript | 10 JW Player / 10 transcripts (100%) |
| Avg transcript | 6,539 chars |
| Modular HTML | 180,813 chars |
| Code blocks | 0 |

**Strengths:** Full transcript coverage, extensive HTML content (180K chars -- highest HTML volume relative to lesson count).  
**Gaps:** No code blocks extracted despite being a technical course. Code may be embedded in HTML tables or non-standard formatting.

---

### 3. Introduction to MCP (82.1/100)

| Metric | Value |
|--------|-------|
| Lessons | 14 (4 sections) |
| Content coverage | 13/14 (92.9%) |
| Video/Transcript | 12 JW Player / 12 transcripts (100%) |
| Avg transcript | 5,428 chars |

**Strengths:** Complete transcript coverage.  
**Gaps:** No code blocks, images, or links despite being a technical protocol course. 1 quiz lesson without content.

---

### 4. Building with the Claude API (81.1/100)

| Metric | Value |
|--------|-------|
| Lessons | 85 (13 sections) -- second largest course |
| Content coverage | 76/85 (89.4%) |
| Video/Transcript | 75 JW Player / 75 transcripts (100%) |
| Avg transcript | 6,441 chars |
| Total transcript | 483,045 chars |

**Strengths:** Complete transcript coverage for all 75 videos. Massive transcript corpus.  
**Gaps:** 9 quiz lessons without content. Only 4 images and 1 link extracted -- surprisingly low for an API course. Code examples likely discussed in video but not captured as code blocks.

---

### 5. Claude with Google Vertex (80.8/100)

| Metric | Value |
|--------|-------|
| Lessons | 93 (13 sections) -- largest course |
| Content coverage | 82/93 (88.2%) |
| Video/Transcript | 82 JW Player / 81 transcripts (98.8%) |
| Avg transcript | 7,973 chars |
| Total transcript | 645,825 chars -- highest single course |

**Strengths:** Near-complete transcript coverage (81/82). Highest transcript volume overall.  
**Gaps:** 1 video missing transcript. 10 quiz lessons without content. Only 4 code blocks.

---

### 6. Claude with Amazon Bedrock (80.2/100)

| Metric | Value |
|--------|-------|
| Lessons | 83 (11 sections) |
| Content coverage | 73/83 (88.0%) |
| Video/Transcript | 75 JW Player / 73 transcripts (97.3%) |
| Avg transcript | 6,091 chars |
| Total transcript | 444,608 chars |

**Strengths:** Strong transcript coverage.  
**Gaps:** 2 videos missing transcripts. 8 quiz lessons. Zero code blocks, images, or links.

---

### 7. Claude 101 (70.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 14 (5 sections) |
| Content coverage | 14/14 (100%) |
| Videos | 12 YouTube (0 transcripts) |
| Modular text | 90,201 chars |
| Links | 55 -- highest link count |
| Images | 5 |

**Strengths:** Full content coverage. Rich modular text (90K chars). Extensive external links (55).  
**Gaps:** All 12 videos are YouTube-hosted with CORS-blocked transcripts. This is the single biggest recovery opportunity -- yt-dlp extraction would add ~30 points to transcript depth.

---

### 8. Introduction to Agent Skills (70.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 6 (1 section) |
| Content coverage | 6/6 (100%) |
| Videos | 6 YouTube (0 transcripts) |
| Code blocks | 61 -- highest code density |
| Images | 12 |

**Strengths:** Extremely code-rich (61 blocks in 6 lessons = 10.2 per lesson). Good image coverage.  
**Gaps:** YouTube transcripts blocked. 1 new code block found by re-parsing.

---

### 9. Introduction to Subagents (70.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 4 (1 section) |
| Content coverage | 4/4 (100%) |
| Videos | 4 YouTube (0 transcripts) |
| Code blocks | 33 |
| Images | 7 |

**Strengths:** Dense code (33 blocks in 4 lessons = 8.3 per lesson). Good images.  
**Gaps:** YouTube transcripts blocked.

---

### 10. Introduction to Claude Cowork (66.4/100)

| Metric | Value |
|--------|-------|
| Lessons | 11 (6 sections) |
| Content coverage | 10/11 (90.9%) |
| Videos | 3 YouTube (0 transcripts) |
| Code blocks | 5 |
| Images | 17 |
| Links | 41 |

**Strengths:** Rich visual content (17 images with descriptive alt text). Extensive links (41).  
**Gaps:** YouTube transcripts blocked. 1 quiz lesson without content.

---

### 11. AI Capabilities and Limitations (61.1/100)

| Metric | Value |
|--------|-------|
| Lessons | 14 (6 sections) |
| Content coverage | 13/14 (92.9%) |
| Videos | 0 |
| Modular text | 70,830 chars |
| Modular HTML | 396,805 chars -- highest HTML volume |
| Images | 20 |

**Strengths:** Purely text-based course with massive HTML content (397K chars). 20 images including pictographic icons.  
**Gaps:** No video content at all. 1 quiz lesson without content. Score limited by zero transcript depth.

---

### 12. AI Fluency: Framework & Foundations (61.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 15 (10 sections) |
| Content coverage | 15/15 (100%) |
| Videos | 11 YouTube (0 transcripts) |
| Modular text | 58,428 chars |
| Links | 18 |

**Strengths:** Perfect content coverage. Good modular text volume.  
**Gaps:** All 11 videos YouTube-hosted without transcripts.

---

### 13. Teaching AI Fluency (59.4/100)

| Metric | Value |
|--------|-------|
| Lessons | 8 (4 sections) |
| Content coverage | 8/8 (100%) |
| Videos | 7 YouTube (0 transcripts) |
| Modular text | 36,466 chars |
| Links | 14 |

**Gaps:** YouTube transcripts blocked.

---

### 14. AI Fluency for Students (59.2/100)

| Metric | Value |
|--------|-------|
| Lessons | 6 (3 sections) |
| Content coverage | 6/6 (100%) |
| Videos | 5 YouTube (0 transcripts) |
| Modular text | 27,126 chars |
| Links | 11 |

**Gaps:** YouTube transcripts blocked.

---

### 15. AI Fluency for Educators (59.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 5 (3 sections) |
| Content coverage | 5/5 (100%) |
| Videos | 4 YouTube (0 transcripts) |
| Modular text | 18,950 chars |
| Links | 11 |

**Gaps:** YouTube transcripts blocked.

---

### 16. AI Fluency for Nonprofits (57.0/100)

| Metric | Value |
|--------|-------|
| Lessons | 10 (5 sections) |
| Content coverage | 9/10 (90.0%) |
| Videos | 9 YouTube (0 transcripts) |
| Modular text | 47,033 chars |
| Links | 13 |

**Gaps:** 1 quiz lesson without content. YouTube transcripts blocked.

---

### 17. Claude Code 101 (51.9/100) -- LOWEST

| Metric | Value |
|--------|-------|
| Lessons | 13 (5 sections) |
| Content coverage | 12/13 (92.3%) |
| Videos | 12 YouTube (0 transcripts) |
| Modular text | 0 chars |
| Modular HTML | 2,605 chars |
| Code blocks | 0 |
| Links | 0 |

**Assessment:** This is the weakest extraction. The course is entirely video-based (12 YouTube videos) with no modular text content. The HTML is minimal (just iframe embeds). Without YouTube transcripts, there is almost no textual content captured. This course has the highest ROI for yt-dlp transcript recovery.

---

## Gap Analysis

### Gap 1: YouTube Transcript Absence (Critical)

- **69 YouTube videos** across 10 courses have zero transcript content
- All marked with `transcript_note: "youtube_captions_inaccessible_via_browser_cors"`
- Affected courses: Claude Code 101 (12 videos), Claude 101 (12), AI Fluency Framework (11), AI Fluency Nonprofits (9), Teaching AI Fluency (7), Intro Agent Skills (6), AI Fluency Students (5), AI Fluency Educators (4), Intro Subagents (4), Intro Claude Cowork (3)
- **Impact:** These 10 courses score 0/30 on Transcript Depth. Filling this gap would add ~30 points to each course's quality score
- **Status:** Agent 1 is extracting via yt-dlp

### Gap 2: Quiz Content (Medium)

- **35 quiz lessons** across 11 courses contain no extractable content
- Quiz questions are dynamically loaded via JavaScript and not present in static HTML
- **Impact:** Reduces Content Coverage by 1-10% depending on course quiz density
- **Status:** Agent 2 is attempting DOM-based quiz extraction

### Gap 3: Code Blocks in JW Transcript Courses (Low)

- The three largest courses (API, Bedrock, Vertex) have 0-4 code blocks despite being programming courses
- Code examples are spoken/shown in video but captured only as transcript text, not structured code blocks
- **Impact:** Low resource richness scores for these courses
- **Remediation:** Post-process transcripts to identify and extract code snippets

### Gap 4: Non-Full-URL Images (Low)

- 8 images in the catalog have partial URLs (e.g., `pictoInference`, `ed975e22-...`) rather than full HTTPS URLs
- These appear to be Skilljar CMS references that were not resolved to full paths
- All occur in the AI Capabilities and Limitations course

---

## Code Block Enrichment Results

Re-parsing all modular_html and modular_text fields with aggressive selectors found **1 additional code block** not captured in the original extraction:

- **Course:** introduction-to-agent-skills
- **Source:** `code_tag_inline` (inline `<code>` block > 30 chars)

This indicates the original extraction was thorough -- only 1 missed block out of 154 total. The original pipeline captured 99.4% of detectable code blocks.

Full results: `deep_extraction/progress/code_enrichment.json`

---

## Image Catalog Summary

**69 images** cataloged across 7 courses:

| Course | Images | Notes |
|--------|--------|-------|
| AI Capabilities & Limitations | 20 | Pictographic icons (inference, globe, chip, knobs) |
| Intro to Claude Cowork | 17 | Slide screenshots with descriptive alt text |
| Intro to Agent Skills | 12 | Skill architecture slides |
| Intro to Subagents | 7 | Subagent design slides |
| Claude 101 | 5 | App screenshots |
| Claude with the Anthropic API | 4 | API key setup screenshots |
| Claude with Google Vertex | 3 | Vertex AI setup screenshots |
| Claude Code in Action | 1 | Hook screenshot |

10 courses have **zero images** -- expected for video-heavy and text-only courses.

Full catalog: `deep_extraction/progress/image_catalog.json`

---

## External Link Catalog Summary

**188 links** cataloged across 14 courses. Top domains:

| Domain | Count | Purpose |
|--------|-------|---------|
| docs.google.com | 52 | Feedback forms |
| forms.gle | 42 | Feedback forms (short URLs) |
| claude.com | 39 | Product links |
| anthropic.skilljar.com | 11 | Cross-course links |
| support.claude.com | 9 | Help center |
| www.anthropic.com | 7 | Company site |
| support.anthropic.com | 4 | API support |
| code.claude.com | 3 | Claude Code product |
| github.com | 3 | Code repositories |
| claude.ai | 2 | Product links |
| console.anthropic.com | 2 | Developer console |

3 courses have **zero links**: Claude Code 101, Claude in Amazon Bedrock, Introduction to MCP.

Full catalog: `deep_extraction/progress/link_catalog.json`

---

## Extraction Quality Comparison

### Before vs After vs Theoretical Maximum

```
                        Before (Landing)    After (Deep V2)     Theoretical Max
                        ----------------    ---------------     ---------------
Content chars           ~50,000             3,369,566           ~3,600,000
Transcript chars        0                   1,776,562           ~2,200,000
Code blocks             0                   154                 ~200
Images                  0                   69                  ~80
Links                   0                   188                 ~200
Quality score (avg)     ~15                 69.8                ~92
Completeness %          ~5%                 75.9%               100%
```

### Improvement Factor

- Content volume: **67x** increase (50K to 3.37M chars)
- From zero transcripts to **1.78M chars** of video transcripts
- From zero code blocks to **154 structured code blocks**
- Quality score: **4.7x** increase (15 to 69.8)

---

## Structural Integrity

All 17 courses achieve **15.0/15.0** structural integrity:
- All 417 lessons have valid titles
- All 417 lessons have valid section assignments
- All 417 lessons have valid URLs

This indicates the extraction pipeline correctly captured metadata for every lesson.

---

## Content Volume by Type

```
Type                    | Chars       | % of Total
------------------------+-------------+-----------
JW Player Transcripts   | 1,776,562   | 52.7%
Modular HTML            | 1,149,473   | 34.1%
Modular Text            |   443,531   | 13.2%
------------------------+-------------+-----------
Total                   | 3,369,566   | 100.0%
```

---

## Recommendations (Priority Ordered)

### Priority 1: YouTube Transcript Recovery (In Progress)
- **Action:** Extract transcripts via yt-dlp for 69 YouTube videos
- **Expected impact:** +25-30 points on 10 courses, global avg from 69.8 to ~85
- **Status:** Agent 1 active

### Priority 2: Quiz Content Extraction (In Progress)
- **Action:** Extract quiz questions from 35 quiz lessons via DOM interaction
- **Expected impact:** +2-5 points on 11 courses
- **Status:** Agent 2 active

### Priority 3: Code Block Extraction from Transcripts
- **Action:** Post-process JW Player transcripts to identify code snippets discussed in API/Bedrock/Vertex courses
- **Expected impact:** +1-3 points on 3 courses
- **Status:** Not started

### Priority 4: Image URL Resolution
- **Action:** Resolve 8 partial image URLs (Skilljar CMS references) to full HTTPS paths
- **Expected impact:** Data quality improvement, no score change
- **Status:** Not started

### Priority 5: Image Download and Local Archival
- **Action:** Download all 69 cataloged images for offline preservation
- **Expected impact:** Data preservation
- **Status:** Not started

---

## Conclusion

The deep extraction achieved **75.9% of theoretical maximum quality**, a significant achievement given the constraints of browser-based extraction. The pipeline successfully captured:

- **90.9%** lesson content coverage (379/417)
- **100%** structural integrity across all courses
- **78.7%** of video transcripts (266/338 videos)
- **99.4%** of detectable code blocks (153/154)

The single biggest quality improvement available is YouTube transcript extraction (Priority 1), which would close approximately 60% of the remaining quality gap. With YouTube transcripts added, the estimated global quality score would rise from **69.8 to approximately 87/100**, representing **94.6%** of theoretical maximum.

---

## Output Files

| File | Location | Contents |
|------|----------|----------|
| AUDIT_REPORT_V3.md | `deep_extraction/` | This report |
| AUDIT_DATA_V3.json | `deep_extraction/` | Structured metrics, per-course data, methodology |
| code_enrichment.json | `deep_extraction/progress/` | 1 newly found code block |
| image_catalog.json | `deep_extraction/progress/` | 69 images with URLs and context |
| link_catalog.json | `deep_extraction/progress/` | 188 links with domains and context |
