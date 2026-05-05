# LOGIN REQUIRED - Deep Lesson Extraction

## Status
All 17 Anthropic Academy course landing pages have been successfully extracted from public pages (no login required). However, **individual lesson content (videos, transcripts, slides, code examples, quiz questions) is gated behind authentication** and is NOT accessible without logging in.

## What was extracted WITHOUT login
- Course titles, subtitles, and URLs (17/17 courses, including the bonus Claude Code 101)
- Course-level statistics (lectures, hours of video, quizzes, certificate)
- Section/chapter names and descriptions
- Section-level lesson counts
- Learning objectives, prerequisites, target audience (where present)
- Individual lesson titles for "sj" template courses (Claude 101, Cowork, Agent Skills, Subagents)
- Instructor bios (Drew Bent, Rick Dakan, Joseph Feller, Maggie Vo) for AI Fluency: Framework & Foundations
- Full AI diligence statement for AI Fluency: Framework & Foundations
- Full-page screenshots of every course landing page

## What CANNOT be extracted without login
- Individual lesson page content (video players, transcripts, captions)
- Exact lesson titles for "clp" template courses (12 of 17 courses use this template)
- Code examples shown inside lessons
- Slide contents beyond the 3 preview images per section
- Quiz questions and answers
- Downloadable resources (PDFs, sample code repos)
- Any content behind the `Enroll in Course` / `Sign In` buttons

## How to unblock deep extraction
1. In the already-open Playwright browser window, click **Sign In** (top right).
2. Create a free Skilljar account for `anthropic.skilljar.com` OR log in if you already have one.
3. After successful login, enroll in each of the 17 courses (they are all FREE).
4. Reply in the main chat with "**logged in**" and the extraction pipeline will resume, navigating into each lesson and pulling DOM-level transcripts, captions, code blocks, and slide screenshots.

## Courses discovered (17 total)
| # | Slug | Title | Template | Lectures | Hours |
|---|------|-------|----------|---------:|------:|
| 1 | claude-with-the-anthropic-api | Building with the Claude API | clp | 84 | 8.1 |
| 2 | claude-code-in-action | Claude Code in Action | clp | 15 | 1.0 |
| 3 | claude-101 | Claude 101 | sj | 14 | n/a |
| 4 | introduction-to-claude-cowork | Introduction to Claude Cowork | sj | 10 | n/a |
| 5 | ai-fluency-framework-foundations | AI Fluency: Framework & Foundations | clp | 14 | 1.1 |
| 6 | introduction-to-model-context-protocol | Introduction to MCP | clp | 16 | 1.0 |
| 7 | ai-fluency-for-educators | AI Fluency for Educators | clp | 4 | 0.4 |
| 8 | ai-fluency-for-students | AI Fluency for Students | clp | 5 | 0.5 |
| 9 | model-context-protocol-advanced-topics | MCP: Advanced Topics | clp | 15 | 1.1 |
| 10 | claude-in-amazon-bedrock | Claude with Amazon Bedrock | clp | 85 | 8.0 |
| 11 | claude-with-google-vertex | Claude with Google Cloud's Vertex AI | clp | 85 | 8.0 |
| 12 | teaching-ai-fluency | Teaching AI Fluency | clp | 7 | 0.6 |
| 13 | ai-fluency-for-nonprofits | AI Fluency for Nonprofits | clp | 9 | 0.9 |
| 14 | introduction-to-agent-skills | Introduction to Agent Skills | sj | 6 | n/a |
| 15 | introduction-to-subagents | Introduction to Subagents | sj | 4 | n/a |
| 16 | ai-capabilities-and-limitations | AI Capabilities and Limitations | clp | 13 | 0.25 |
| 17 | claude-code-101 | Claude Code 101 (bonus, not in original 16) | clp | 12 | 1.5 |

**Total lectures across all courses: 398**
**Total hours of video (where reported): ~32.5 hours**

## Template legend
- **sj**: Old Skilljar curriculum template — exposes individual lesson titles on the public landing page
- **clp**: New custom landing page template — only section-level info public; individual lesson titles are behind login
