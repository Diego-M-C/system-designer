# ENGINEERING INTELLIGENCE V2 — Anthropic Academy Complete Reference

*Generated: 2026-04-11T11:44:19.641426Z*  
*Source: anthropic.skilljar.com — extracted via Playwright with authenticated session*  
*Author of extraction pipeline: Atlas Resumed (Claude Code agent)*

## Pipeline Summary

- **Courses extracted:** 17 / 17
- **Total lessons:** 417
- **Lessons with English video transcript (JW Player):** 266
- **Lessons with rich modular text:** 101
- **Lessons with YouTube embed (metadata only):** 69
- **Total content characters:** 2,220,093
- **Extraction errors:** 0

## Methodology

**Authentication:** Diego Muñoz Casinos (enrolled in all 17 courses).  
**Transport:** Skilljar pages were fetched in-browser via `fetch(url, {credentials:'include'})` so the session cookie authenticates each lesson HTML request. No DRM or video file was downloaded.  
**Lesson types found:** `lesson-modular` (HTML-rich pages or YouTube iframes), `lesson-video` (JW Player), `lesson-quiz` (Skilljar quizzes).  
**Video transcript source:** For JW Player lessons, the embedded `<sjwc-video video-id="...">` element exposes a JW media id. The pipeline calls `https://cdn.jwplayer.com/v2/media/<id>` to retrieve metadata + caption track URLs, then fetches the English `.srt` and strips timestamps to produce the plain-text transcript.  
**Modular content source:** The HTML inside `<sjwc-lesson-content-item>...</sjwc-lesson-content-item>` is parsed with `DOMParser`; `<style>`/`<script>` blocks are stripped. `textContent` is extracted, and `<img>`, `<a>`, `<pre>`, `<code>`, `<iframe>` elements are inventoried.  
**YouTube lessons:** YouTube transcript endpoints CORS-block browser fetches, so for YouTube embeds the pipeline only captures the video id, oEmbed metadata (title + author), and the watch URL. The lesson narrative text (which is rich for these courses) is captured via the surrounding modular HTML.  
**Zero fabrication:** every record traces back to a `source_url` and an `extraction_method`. Empty fields are explicit.  

## Course Index

| # | Slug | Title | Lessons | Transcripts | Modular Text |
|---|------|-------|--------:|------------:|-------------:|
| 1 | `claude-with-the-anthropic-api` | Building with the Claude API | 85 | 75 | 1 |
| 2 | `claude-code-in-action` | Claude Code in Action | 21 | 15 | 4 |
| 3 | `claude-code-101` | Claude Code 101 | 13 | 0 | 0 |
| 4 | `introduction-to-agent-skills` | Introduction to agent skills | 6 | 0 | 6 |
| 5 | `introduction-to-subagents` | Introduction to subagents | 4 | 0 | 4 |
| 6 | `introduction-to-model-context-protocol` | Introduction to Model Context Protocol | 14 | 12 | 1 |
| 7 | `model-context-protocol-advanced-topics` | Model Context Protocol: Advanced Topics | 15 | 10 | 4 |
| 8 | `claude-in-amazon-bedrock` | Claude with Amazon Bedrock | 83 | 73 | 0 |
| 9 | `claude-with-google-vertex` | Claude with Google Cloud's Vertex AI | 93 | 81 | 1 |
| 10 | `introduction-to-claude-cowork` | Introduction to Claude Cowork | 11 | 0 | 10 |
| 11 | `claude-101` | Claude 101 | 14 | 0 | 14 |
| 12 | `ai-fluency-framework-foundations` | AI Fluency: Framework & Foundations | 15 | 0 | 15 |
| 13 | `ai-capabilities-and-limitations` | AI Capabilities and Limitations | 14 | 0 | 13 |
| 14 | `ai-fluency-for-educators` | AI Fluency for educators | 5 | 0 | 5 |
| 15 | `ai-fluency-for-students` | AI Fluency for students | 6 | 0 | 6 |
| 16 | `ai-fluency-for-nonprofits` | AI Fluency for nonprofits | 10 | 0 | 9 |
| 17 | `teaching-ai-fluency` | Teaching AI Fluency | 8 | 0 | 8 |

---

# Group: API & SDK


## Building with the Claude API

`claude-with-the-anthropic-api` — https://anthropic.skilljar.com/claude-with-the-anthropic-api  

**85 lessons** · 75 transcripts · 1 text · 483,045 transcript chars


*See full content in `md/claude-with-the-anthropic-api_deep_v2.md`*


### Lessons


**Introduction**

- 1. Welcome to the course  *[JW, TRANS(2658)]*

**Anthropic overview**

- 2. Overview of Claude models  *[JW, TRANS(4637)]*

**Accessing Claude with the API**

- 3. Accessing the API  *[JW, TRANS(6125)]*
- 4. Getting an API key  *[TEXT(1107)]*
- 5. Making a request  *[JW, TRANS(6892)]*
- 6. Multi-Turn conversations  *[JW, TRANS(10143)]*
- 7. Chat exercise  *[JW, TRANS(4522)]*
- 8. System prompts  *[JW, TRANS(7373)]*
- 9. System prompts exercise  *[JW, TRANS(1718)]*
- 10. Temperature  *[JW, TRANS(6894)]*
- 11. Course satisfaction survey  *[meta]*
- 12. Response streaming  *[JW, TRANS(9543)]*
- 13. Structured data  *[JW, TRANS(6553)]*
- 14. Structured data exercise  *[JW, TRANS(5305)]*
- 15. Quiz on accessing Claude with the API  *[meta]*

**Prompt evaluation**

- 16. Prompt evaluation  *[JW, TRANS(2211)]*
- 17. A typical eval workflow  *[JW, TRANS(5251)]*
- 18. Generating test datasets  *[JW, TRANS(5184)]*
- 19. Running the eval  *[JW, TRANS(6554)]*
- 20. Model based grading  *[JW, TRANS(10197)]*
- 21. Code based grading  *[JW, TRANS(7485)]*
- 22. Exercise on prompt evals  *[JW, TRANS(4879)]*
- 23. Quiz on prompt evaluation  *[meta]*

**Prompt engineering techniques**

- 24. Prompt engineering  *[JW, TRANS(11690)]*
- 25. Being clear and direct  *[JW, TRANS(2258)]*
- 26. Being specific  *[JW, TRANS(5955)]*
- 27. Structure with XML tags  *[JW, TRANS(4388)]*
- 28. Providing examples  *[JW, TRANS(7156)]*
- 29. Exercise on prompting  *[JW, TRANS(5703)]*
- 30. Quiz on prompt engineering techniques  *[meta]*

**Tool use with Claude**

- 31. Introducing tool use  *[JW, TRANS(3402)]*
- 32. Project overview  *[JW, TRANS(2653)]*
- 33. Tool functions  *[JW, TRANS(6189)]*
- 34. Tool schemas  *[JW, TRANS(5225)]*
- 35. Handling message blocks  *[JW, TRANS(6426)]*
- 36. Sending tool results  *[JW, TRANS(10513)]*
- 37. Multi-turn conversations with tools  *[JW, TRANS(10475)]*
- 38. Implementing multiple turns  *[JW, TRANS(17588)]*
- 39. Using multiple tools  *[JW, TRANS(3992)]*
- 40. Fine grained tool calling  *[JW, TRANS(12736)]*
- 41. The text edit tool  *[JW, TRANS(10045)]*
- 42. The web search tool  *[JW, TRANS(7954)]*
- 43. Quiz on tool use with Claude  *[meta]*

**RAG and Agentic Search**

- 44. Introducing Retrieval Augmented Generation  *[JW, TRANS(6525)]*
- 45. Text chunking strategies  *[JW, TRANS(15117)]*
- 46. Text embeddings  *[JW, TRANS(4675)]*
- 47. The full RAG flow  *[JW, TRANS(9295)]*
- 48. Implementing the RAG flow  *[JW, TRANS(5397)]*
- 49. BM25 lexical search  *[JW, TRANS(10551)]*
- 50. A Multi-Index RAG pipeline  *[JW, TRANS(7179)]*

**Features of Claude**

- 51. Extended thinking  *[JW, TRANS(8063)]*
- 52. Image support  *[JW, TRANS(11518)]*
- 53. PDF support  *[JW, TRANS(1623)]*
- 54. Citations  *[JW, TRANS(6113)]*
- 55. Prompt caching  *[JW, TRANS(4171)]*
- 56. Rules of prompt caching  *[JW, TRANS(7950)]*
- 57. Prompt caching in action  *[JW, TRANS(7682)]*
- 58. Code execution and the Files API  *[JW, TRANS(12565)]*
- 59. Quiz on features of Claude  *[meta]*

**Model Context Protocol**

- 60. Introducing MCP  *[JW, TRANS(4874)]*
- 61. MCP clients  *[JW, TRANS(5456)]*
- 62. Project setup  *[JW, TRANS(3542)]*
- 63. Defining tools with MCP  *[JW, TRANS(6637)]*
- 64. The server inspector  *[JW, TRANS(4059)]*
- 65. Implementing a client  *[JW, TRANS(8139)]*
- 66. Defining resources  *[JW, TRANS(10413)]*
- 67. Accessing resources  *[JW, TRANS(4651)]*
- 68. Defining prompts  *[JW, TRANS(8201)]*
- 69. Prompts in the client  *[JW, TRANS(3219)]*
- 70. MCP review  *[JW, TRANS(4648)]*
- 71. Quiz on Model Context Protocol  *[meta]*

**Anthropic apps - Claude Code and computer use**

- 72. Anthropic apps  *[JW, TRANS(921)]*
- 73. Claude Code setup  *[JW, TRANS(1710)]*
- 74. Claude Code in action  *[JW, TRANS(12025)]*
- 75. Enhancements with MCP servers  *[JW, TRANS(2734)]*

**Agents and workflows**

- 76. Agents and workflows  *[JW, TRANS(5230)]*
- 77. Parallelization workflows  *[JW, TRANS(4548)]*
- 78. Chaining workflows  *[JW, TRANS(5627)]*
- 79. Routing workflows  *[JW, TRANS(3900)]*
- 80. Agents and tools  *[JW, TRANS(5955)]*
- 81. Environment inspection  *[JW, TRANS(3651)]*
- 82. Workflows vs agents  *[JW, TRANS(2178)]*
- 83. Quiz on Agents and Workflows  *[meta]*

**Final assessment**

- 84. Final Assessment  *[meta]*

**Wrapping up!**

- 85. Course Wrap Up  *[JW, TRANS(3831)]*

---

# Group: Claude Code


## Claude Code in Action

`claude-code-in-action` — https://anthropic.skilljar.com/claude-code-in-action  

**21 lessons** · 15 transcripts · 4 text · 72,552 transcript chars


*See full content in `md/claude-code-in-action_deep_v2.md`*


### Lessons


**What is Claude Code?**

- 1. Introduction  *[JW, TRANS(793)]*
- 2. What is a coding assistant?  *[JW, TRANS(6664)]*
- 3. Claude Code in action  *[JW, TRANS(9584)]*

**Getting hands on**

- 4. Claude Code setup  *[TEXT(800)]*
- 5. Project setup  *[TEXT(1118)]*
- 6. Adding context  *[JW, TRANS(6267)]*
- 7. Making changes  *[JW, TRANS(4934)]*
- 8. Course satisfaction survey  *[meta]*
- 9. Controlling context  *[JW, TRANS(4254)]*
- 10. Custom commands  *[JW, TRANS(2097)]*
- 11. MCP servers with Claude Code  *[JW, TRANS(3321)]*
- 12. Github integration  *[JW, TRANS(4282)]*

**Hooks and the SDK**

- 13. Introducing hooks  *[JW, TRANS(3914)]*
- 14. Defining hooks  *[JW, TRANS(4279)]*
- 15. Implementing a hook  *[JW, TRANS(4602)]*
- 16. Gotchas around hooks  *[TEXT(1252)]*
- 17. Useful hooks!  *[JW, TRANS(13481)]*
- 18. Another useful hook  *[TEXT(2625)]*
- 19. The Claude Code SDK  *[JW, TRANS(3010)]*

**Wrapping up**

- 20. Quiz on Claude Code  *[meta]*
- 21. Summary and next steps  *[JW, TRANS(1070)]*

## Claude Code 101

`claude-code-101` — https://anthropic.skilljar.com/claude-code-101  

**13 lessons** · 0 transcripts · 0 text · 0 transcript chars


*See full content in `md/claude-code-101_deep_v2.md`*


### Lessons


**What is Claude Code?**

- 1. What is Claude Code?  *[YT]*
- 2. How Claude Code works  *[YT]*

**Your first prompt**

- 3. Installing Claude Code  *[YT]*
- 4. Your first prompt  *[YT]*

**Daily workflows**

- 5. The explore → plan → code → commit workflow  *[YT]*
- 6. Context management  *[YT]*
- 7. Code review  *[YT]*

**Customizing Claude Code**

- 8. The CLAUDE.md file  *[YT]*
- 9. Subagents  *[YT]*
- 10. Skills  *[YT]*
- 11. MCP  *[meta]*
- 12. Hooks  *[YT]*

**Quiz**

- 13. Course quiz  *[meta]*

---

# Group: Agent Skills & Subagents


## Introduction to agent skills

`introduction-to-agent-skills` — https://anthropic.skilljar.com/introduction-to-agent-skills  

**6 lessons** · 0 transcripts · 6 text · 0 transcript chars


*See full content in `md/introduction-to-agent-skills_deep_v2.md`*


### Lessons


**(uncategorized)**

- 1. What are skills?  *[YT, TEXT(5422)]*
- 2. Creating your first skill  *[YT, TEXT(5443)]*
- 3. Configuration and multi-file skills  *[YT, TEXT(5844)]*
- 4. Skills vs. other Claude Code features  *[YT, TEXT(4813)]*
- 5. Sharing skills  *[YT, TEXT(5750)]*
- 6. Troubleshooting skills  *[YT, TEXT(5519)]*

## Introduction to subagents

`introduction-to-subagents` — https://anthropic.skilljar.com/introduction-to-subagents  

**4 lessons** · 0 transcripts · 4 text · 0 transcript chars


*See full content in `md/introduction-to-subagents_deep_v2.md`*


### Lessons


**(uncategorized)**

- 1. What are subagents?  *[YT, TEXT(3074)]*
- 2. Creating a subagent  *[YT, TEXT(4696)]*
- 3. Designing effective subagents  *[YT, TEXT(5692)]*
- 4. Using subagents effectively  *[YT, TEXT(4806)]*

---

# Group: Model Context Protocol (MCP)


## Introduction to Model Context Protocol

`introduction-to-model-context-protocol` — https://anthropic.skilljar.com/introduction-to-model-context-protocol  

**14 lessons** · 12 transcripts · 1 text · 65,138 transcript chars


*See full content in `md/introduction-to-model-context-protocol_deep_v2.md`*


### Lessons


**Introduction**

- 1. Welcome to the course  *[JW, TRANS(1195)]*
- 2. Introducing MCP  *[JW, TRANS(4874)]*
- 3. MCP clients  *[JW, TRANS(5460)]*

**Hands-on with MCP servers**

- 4. Project setup  *[JW, TRANS(3543)]*
- 5. Defining tools with MCP  *[JW, TRANS(6678)]*
- 6. The server inspector  *[JW, TRANS(4069)]*
- 7. Course satisfaction survey  *[meta]*

**Connecting with MCP clients**

- 8. Implementing a client  *[JW, TRANS(8158)]*
- 9. Defining resources  *[JW, TRANS(10424)]*
- 10. Accessing resources  *[JW, TRANS(4681)]*
- 11. Defining prompts  *[JW, TRANS(8202)]*
- 12. Prompts in the client  *[JW, TRANS(3207)]*

**Assessment and wrap Up**

- 13. Final assessment on MCP  *[TEXT(10)]*
- 14. MCP review  *[JW, TRANS(4647)]*

## Model Context Protocol: Advanced Topics

`model-context-protocol-advanced-topics` — https://anthropic.skilljar.com/model-context-protocol-advanced-topics  

**15 lessons** · 10 transcripts · 4 text · 65,394 transcript chars


*See full content in `md/model-context-protocol-advanced-topics_deep_v2.md`*


### Lessons


**Introduction**

- 1. Let's get started!  *[JW, TRANS(1613)]*

**Core MCP features**

- 2. Sampling  *[JW, TRANS(6005)]*
- 3. Sampling walkthrough  *[TEXT(17)]*
- 4. Log and progress notifications  *[JW, TRANS(3225)]*
- 5. Notifications walkthrough  *[TEXT(17)]*
- 6. Roots  *[JW, TRANS(8820)]*
- 7. Roots walkthrough  *[TEXT(17)]*
- 8. Survey  *[TEXT(10)]*

**Transports and communication**

- 9. JSON message types  *[JW, TRANS(7769)]*
- 10. The STDIO transport  *[JW, TRANS(10447)]*
- 11. The StreamableHTTP transport  *[JW, TRANS(7319)]*
- 12. StreamableHTTP in depth  *[JW, TRANS(11807)]*
- 13. State and the StreamableHTTP transport  *[JW, TRANS(7482)]*

**Assessment and next steps**

- 14. Assessment on MCP concepts  *[meta]*
- 15. Wrapping up  *[JW, TRANS(907)]*

---

# Group: Cloud Deployments


## Claude with Amazon Bedrock

`claude-in-amazon-bedrock` — https://anthropic.skilljar.com/claude-in-amazon-bedrock  

**83 lessons** · 73 transcripts · 0 text · 444,608 transcript chars


*See full content in `md/claude-in-amazon-bedrock_deep_v2.md`*


### Lessons


**Course introduction**

- 1. Introduction to the course  *[JW, TRANS(1178)]*
- 2. Overview of Claude Models  *[JW, TRANS(4637)]*

**Working with the API**

- 3. Accessing the API  *[JW, TRANS(2748)]*
- 4. Making a request  *[JW, TRANS(8891)]*
- 5. Multi-Turn conversations  *[JW, TRANS(9652)]*
- 6. Chat bot exercise  *[JW, TRANS(5995)]*
- 7. System prompts  *[JW, TRANS(8220)]*
- 8. System prompt exercise  *[JW, TRANS(3100)]*
- 9. Temperature  *[JW, TRANS(8698)]*
- 10. Streaming  *[JW, TRANS(8644)]*
- 11. Controlling model output  *[JW, TRANS(7659)]*
- 12. Structured data  *[JW, TRANS(6753)]*
- 13. Structured data exercise  *[JW, TRANS(5335)]*
- 14. Quiz on working with the API  *[meta]*

**Prompt evaluations**

- 15. Prompt evaluation  *[JW, TRANS(2268)]*
- 16. A typical eval workflow  *[JW, TRANS(5201)]*
- 17. Generating test datasets  *[JW, TRANS(7018)]*
- 18. Running the eval  *[JW, TRANS(6716)]*
- 19. Model based grading  *[JW, TRANS(9523)]*
- 20. Code based grading  *[JW, TRANS(7736)]*
- 21. Exercise on prompt evals  *[JW, TRANS(4906)]*
- 22. Quiz on prompt evaluations  *[meta]*

**Prompt engineering**

- 23. Prompt engineering  *[JW, TRANS(9634)]*
- 24. Being clear and direct  *[JW, TRANS(2307)]*
- 25. Being specific  *[JW, TRANS(5947)]*
- 26. Structure with XML tags  *[JW, TRANS(4493)]*
- 27. Providing examples  *[JW, TRANS(7357)]*
- 28. Exercise on prompting  *[JW, TRANS(5756)]*
- 29. Quiz on prompt engineering  *[meta]*

**Tool use**

- 30. Introducing tool use  *[JW, TRANS(5062)]*
- 31. Tool functions  *[JW, TRANS(6378)]*
- 32. JSON Schema for tools  *[JW, TRANS(6079)]*
- 33. Handling tool use responses  *[JW]*
- 34. Running tool functions  *[JW, TRANS(9495)]*
- 35. Sending tool results  *[JW, TRANS(3153)]*
- 36. Multi-Turn conversations with tools  *[JW, TRANS(6391)]*
- 37. Adding multiple tools  *[JW, TRANS(3559)]*
- 38. Batch tool use  *[JW, TRANS(7269)]*
- 39. Structured data with tools  *[JW, TRANS(9437)]*
- 40. Flexible tool extraction  *[JW, TRANS(4661)]*
- 41. The text editor tool  *[JW, TRANS(9547)]*
- 42. Quiz on tool use  *[meta]*

**Retrieval Augmented Generation**

- 43. Introducing Retrieval Augmented Generation  *[JW]*
- 44. Text chunking strategies  *[JW, TRANS(9165)]*
- 45. Text embeddings  *[JW, TRANS(5599)]*
- 46. The full RAG flow  *[JW, TRANS(9354)]*
- 47. Implementing the RAG flow  *[JW, TRANS(5671)]*
- 48. BM25 lexical search  *[JW, TRANS(9398)]*
- 49. A multi-search RAG pipeline  *[JW, TRANS(7294)]*
- 50. Reranking results  *[JW, TRANS(6979)]*
- 51. Contextual retrieval  *[JW, TRANS(7417)]*
- 52. Quiz on Retrieval Augmented Generation  *[meta]*

**Features of Claude**

- 53. Extended thinking  *[JW, TRANS(8776)]*
- 54. Image support  *[JW, TRANS(9798)]*
- 55. PDF support  *[JW, TRANS(2052)]*
- 56. Citations  *[JW, TRANS(2998)]*
- 57. Prompt caching  *[JW, TRANS(4284)]*
- 58. Rules of prompt caching  *[JW, TRANS(7350)]*
- 59. Prompt caching in action  *[JW, TRANS(7573)]*
- 60. Quiz on features of Claude  *[meta]*

**Model Context Protocol**

- 61. Introducing MCP  *[JW, TRANS(4982)]*
- 62. MCP clients  *[JW, TRANS(5438)]*
- 63. Project setup  *[JW, TRANS(3898)]*
- 64. Defining tools with MCP  *[JW, TRANS(6762)]*
- 65. The server inspector  *[JW, TRANS(4152)]*
- 66. Implementing a client  *[JW, TRANS(8999)]*
- 67. Defining resources  *[JW, TRANS(9713)]*
- 68. Accessing resources  *[JW, TRANS(4823)]*
- 69. Defining prompts  *[JW, TRANS(8457)]*
- 70. Prompts in the client  *[JW, TRANS(3261)]*
- 71. MCP review  *[JW, TRANS(4729)]*
- 72. Quiz on Model Context Protocol  *[meta]*

**Agents**

- 73. Agents overview  *[JW, TRANS(1230)]*
- 74. Claude Code setup  *[JW, TRANS(2065)]*
- 75. Claude Code in action  *[JW, TRANS(9195)]*
- 76. Enhancements with MCP servers  *[JW, TRANS(2798)]*
- 77. Parallelizing Claude Code  *[JW, TRANS(8747)]*
- 78. Automated debugging  *[JW, TRANS(5184)]*
- 79. Computer Use  *[JW, TRANS(3734)]*
- 80. How Computer Use works  *[JW, TRANS(4262)]*
- 81. Qualities of agents  *[JW, TRANS(4046)]*

**Final assessment**

- 82. Final assessment quiz  *[meta]*

**Wrap up**

- 83. Course wrap up  *[JW, TRANS(3022)]*

## Claude with Google Cloud's Vertex AI

`claude-with-google-vertex` — https://anthropic.skilljar.com/claude-with-google-vertex  

**93 lessons** · 81 transcripts · 1 text · 645,825 transcript chars


*See full content in `md/claude-with-google-vertex_deep_v2.md`*


### Lessons


**Introduction**

- 1. Welcome to the course  *[JW, TRANS(2562)]*

**Anthropic overview**

- 2. Overview of Claude models  *[JW, TRANS(4637)]*

**Accessing Claude with the API**

- 3. Accessing the API  *[JW, TRANS(6104)]*
- 4. Vertex AI Setup  *[TEXT(1264)]*
- 5. Making a request  *[JW, TRANS(5927)]*
- 6. Multi-turn conversations  *[JW, TRANS(10146)]*
- 7. Chat exercise  *[JW, TRANS(4522)]*
- 8. System prompts  *[JW, TRANS(7373)]*
- 9. System prompts exercise  *[JW, TRANS(1717)]*
- 10. Temperature  *[JW, TRANS(6900)]*
- 11. Course satisfaction survey  *[meta]*
- 12. Response streaming  *[JW, TRANS(9545)]*
- 13. Controlling model output  *[JW, TRANS(7364)]*
- 14. Structured data  *[JW, TRANS(6553)]*
- 15. Structured data exercise  *[JW, TRANS(5305)]*
- 16. Quiz on accessing Claude with the API  *[meta]*

**Prompt evaluation**

- 17. Prompt evaluation  *[JW, TRANS(2214)]*
- 18. A typical eval workflow  *[JW, TRANS(5251)]*
- 19. Generating test datasets  *[JW, TRANS(5184)]*
- 20. Running the eval  *[JW, TRANS(6554)]*
- 21. Model based grading  *[JW, TRANS(10229)]*
- 22. Code based grading  *[JW, TRANS(7485)]*
- 23. Exercise on prompt evals  *[JW, TRANS(4879)]*
- 24. Quiz on prompt evaluation  *[meta]*

**Prompt engineering techniques**

- 25. Prompt engineering  *[JW, TRANS(11708)]*
- 26. Being clear and direct  *[JW, TRANS(2260)]*
- 27. Being specific  *[JW, TRANS(5958)]*
- 28. Structure with XML tags  *[JW, TRANS(4388)]*
- 29. Providing examples  *[JW, TRANS(7159)]*
- 30. Exercise on prompting  *[JW]*
- 31. Quiz on prompt engineering techniques  *[meta]*

**Tool use with Claude**

- 32. Introducing tool use  *[JW, TRANS(3402)]*
- 33. Project overview  *[JW, TRANS(2653)]*
- 34. Tool functions  *[JW, TRANS(6202)]*
- 35. Tool schemas  *[JW, TRANS(5225)]*
- 36. Handling message blocks  *[JW, TRANS(6426)]*
- 37. Sending tool results  *[JW, TRANS(10520)]*
- 38. Multi-turn conversations with tools  *[JW, TRANS(10526)]*
- 39. Implementing multiple turns  *[JW, TRANS(17543)]*
- 40. Using multiple tools  *[JW, TRANS(3936)]*
- 41. The batch tool  *[JW, TRANS(9588)]*
- 42. Tools for structured data  *[JW, TRANS(8704)]*
- 43. The text edit tool  *[JW, TRANS(10036)]*
- 44. The web search tool  *[JW, TRANS(7975)]*
- 45. Quiz on tool use with Claude  *[meta]*

**Retrieval Augmented Generation**

- 46. Introducing Retrieval Augmented Generation  *[JW, TRANS(6525)]*
- 47. Text chunking strategies  *[JW, TRANS(15118)]*
- 48. Text embeddings  *[JW, TRANS(4397)]*
- 49. The full RAG flow  *[JW, TRANS(9298)]*
- 50. Implementing the RAG flow  *[JW, TRANS(5054)]*
- 51. BM25 lexical search  *[JW, TRANS(10540)]*
- 52. A Multi-index RAG pipeline  *[JW, TRANS(7180)]*
- 53. Reranking results  *[JW, TRANS(6949)]*
- 54. Contextual retrieval  *[JW, TRANS(7197)]*
- 55. Quiz on Retrieval Augmented Generation  *[meta]*

**Features of Claude**

- 56. Extended thinking  *[JW, TRANS(8063)]*
- 57. Image support  *[JW, TRANS(11501)]*
- 58. PDF support  *[JW, TRANS(1623)]*
- 59. Citations  *[JW, TRANS(6103)]*
- 60. Prompt caching  *[JW, TRANS(4176)]*
- 61. Rules of prompt caching  *[JW, TRANS(7951)]*
- 62. Prompt caching in action  *[JW, TRANS(7682)]*
- 63. Quiz on features of Claude  *[meta]*

**Model Context Protocol**

- 64. Introducing MCP  *[JW, TRANS(4874)]*
- 65. MCP clients  *[JW, TRANS(5458)]*
- 66. Project setup  *[JW, TRANS(3544)]*
- 67. Defining tools with MCP  *[JW, TRANS(6623)]*
- 68. The server inspector  *[JW, TRANS(4065)]*
- 69. Implementing a client  *[JW, TRANS(8132)]*
- 70. Defining resources  *[JW, TRANS(144597)]*
- 71. Accessing resources  *[JW, TRANS(4682)]*
- 72. Defining prompts  *[JW, TRANS(8204)]*
- 73. Prompts in the client  *[JW, TRANS(3217)]*
- 74. MCP review  *[JW, TRANS(4649)]*
- 75. Quiz on Model Context Protocol  *[meta]*

**Anthropic apps - Claude Code and computer use**

- 76. Anthropic apps  *[JW, TRANS(921)]*
- 77. Claude Code setup  *[JW, TRANS(1709)]*
- 78. Claude Code in action  *[JW, TRANS(12033)]*
- 79. Enhancements with MCP servers  *[JW, TRANS(2734)]*
- 80. Parallelizing Claude Code  *[JW, TRANS(8544)]*
- 81. Automated debugging  *[JW, TRANS(5162)]*
- 82. Computer use  *[JW, TRANS(3644)]*
- 83. How computer use works  *[JW, TRANS(4094)]*

**Agents and workflows**

- 84. Agents and workflows  *[JW, TRANS(5235)]*
- 85. Parallelization workflows  *[JW, TRANS(4548)]*
- 86. Chaining workflows  *[JW, TRANS(5627)]*
- 87. Routing workflows  *[JW, TRANS(3900)]*
- 88. Agents and tools  *[JW, TRANS(5953)]*
- 89. Environment inspection  *[JW, TRANS(3650)]*
- 90. Workflows vs agents  *[JW, TRANS(2178)]*
- 91. Quiz on agents and workflows  *[meta]*

**Final assessment**

- 92. Final assessment quiz  *[meta]*

**Wrapping up!**

- 93. Course Wrap Up  *[JW, TRANS(3831)]*

---

# Group: Claude Cowork & Product


## Introduction to Claude Cowork

`introduction-to-claude-cowork` — https://anthropic.skilljar.com/introduction-to-claude-cowork  

**11 lessons** · 0 transcripts · 10 text · 0 transcript chars


*See full content in `md/introduction-to-claude-cowork_deep_v2.md`*


### Lessons


**Meet Claude Cowork**

- 1. What is Cowork?  *[YT, TEXT(4616)]*
- 2. Getting set up  *[TEXT(3065)]*

**Running your first task**

- 3. The task loop  *[TEXT(5143)]*
- 4. Giving Cowork context  *[TEXT(3208)]*

**Making Claude Cowork yours**

- 5. Plugins: Cowork as a specialist  *[YT, TEXT(3504)]*
- 6. Scheduled tasks  *[TEXT(2427)]*

**Claude Cowork in practice**

- 7. File & document tasks  *[YT, TEXT(2446)]*
- 8. Research & analysis at scale  *[TEXT(3898)]*

**Working responsibly**

- 9. Permissions, usage, & choosing your model  *[TEXT(3554)]*
- 10. Troubleshooting & next steps  *[TEXT(3340)]*

**Check your understanding**

- 11. Quiz on Claude Cowork  *[meta]*

## Claude 101

`claude-101` — https://anthropic.skilljar.com/claude-101  

**14 lessons** · 0 transcripts · 14 text · 0 transcript chars


*See full content in `md/claude-101_deep_v2.md`*


### Lessons


**Meet Claude**

- 1. What is Claude?  *[YT, TEXT(6589)]*
- 2. Your first conversation with Claude  *[YT, TEXT(7314)]*
- 3. Getting better results  *[YT, TEXT(7628)]*
- 4. Claude desktop app: Chat, Cowork, Code  *[TEXT(11613)]*

**Organizing your work and knowledge**

- 5. Introduction to projects  *[YT, TEXT(10056)]*
- 6. Creating with artifacts  *[TEXT(6148)]*
- 7. Working with skills  *[YT, TEXT(8632)]*

**Expanding Claude's reach**

- 8. Connecting your tools  *[YT, YT, TEXT(6159)]*
- 9. Enterprise search  *[TEXT(5160)]*
- 10. Research mode for deep dives  *[YT, TEXT(8627)]*

**Putting it all together**

- 11. Claude in action: use-cases by role  *[TEXT(3360)]*
- 12. Other ways to work with Claude  *[YT, YT, YT, YT, TEXT(5471)]*

**Conclusion & certificate**

- 13. What's next?  *[TEXT(3434)]*
- 14. Certificate of completion  *[TEXT(10)]*

---

# Group: AI Fluency Curriculum


## AI Fluency: Framework & Foundations

`ai-fluency-framework-foundations` — https://anthropic.skilljar.com/ai-fluency-framework-foundations  

**15 lessons** · 0 transcripts · 15 text · 0 transcript chars


*See full content in `md/ai-fluency-framework-foundations_deep_v2.md`*


### Lessons


**Introduction to AI Fluency**

- 1. Introduction to AI Fluency  *[YT, TEXT(3573)]*

**The AI Fluency Framework**

- 2. Why do we need AI Fluency?  *[YT, TEXT(1478)]*
- 3. The 4D Framework  *[YT, TEXT(6060)]*

**Deep Dive 1: What is Generative AI? (Part 1)**

- 4. Generative AI fundamentals  *[YT, TEXT(1326)]*
- 5. Capabilities & limitations  *[YT, TEXT(3021)]*

**Delegation**

- 6. A closer look at Delegation  *[YT, TEXT(4210)]*
- 7. Project planning and Delegation  *[TEXT(4247)]*

**Description**

- 8. A closer look at Description  *[YT, TEXT(3670)]*

**Deep Dive 2: Effective prompting techniques**

- 9. Effective prompting techniques  *[YT, TEXT(3464)]*

**Discernment**

- 10. A closer look at Discernment  *[YT, TEXT(5547)]*

**The Description-Discernment loop**

- 11. The Description-Discernment loop  *[TEXT(4038)]*

**Diligence**

- 12. A closer look at Diligence  *[YT, TEXT(5668)]*

**Conclusion & certificate**

- 13. Conclusion  *[YT, TEXT(5445)]*
- 14. Certificate of completion  *[TEXT(10)]*
- 15. Additional activities  *[TEXT(6671)]*

## AI Capabilities and Limitations

`ai-capabilities-and-limitations` — https://anthropic.skilljar.com/ai-capabilities-and-limitations  

**14 lessons** · 0 transcripts · 13 text · 0 transcript chars


*See full content in `md/ai-capabilities-and-limitations_deep_v2.md`*


### Lessons


**Getting started**

- 1. Intro to AI Capabilities and Limitations  *[TEXT(4270)]*
- 2. What We Mean by AI  *[TEXT(5806)]*
- 3. How AI Gets Its Character  *[TEXT(6193)]*

**Next Token Prediction**

- 4. Next Token Prediction  *[TEXT(6610)]*
- 5. Try it out  *[TEXT(4999)]*

**Knowledge**

- 6. Knowledge  *[TEXT(7012)]*
- 7. Try it out  *[TEXT(6107)]*

**Working Memory**

- 8. Working Memory  *[TEXT(6966)]*
- 9. Try it out  *[TEXT(4496)]*

**Steerability**

- 10. Steerability  *[TEXT(7424)]*
- 11. Try it out  *[TEXT(529)]*

**Putting it all together and next steps**

- 12. When Properties Collide  *[TEXT(5098)]*
- 13. Next Steps  *[TEXT(5320)]*
- 14. Course Quiz  *[meta]*

## AI Fluency for educators

`ai-fluency-for-educators` — https://anthropic.skilljar.com/ai-fluency-for-educators  

**5 lessons** · 0 transcripts · 5 text · 0 transcript chars


*See full content in `md/ai-fluency-for-educators_deep_v2.md`*


### Lessons


**Introduction and AI Fluency Framework**

- 1. Introduction to AI Fluency for Educators  *[YT, TEXT(4642)]*
- 2. AI Fluency Framework review  *[YT, TEXT(2413)]*

**AI Fluency applications for educators**

- 3. Applying AI Fluency to course design and learning outcomes  *[YT, TEXT(5245)]*
- 4. Applying AI Fluency to learning materials and assignments  *[YT, TEXT(6640)]*

**Conclusion & certificate**

- 5. Certificate of completion  *[TEXT(10)]*

## AI Fluency for students

`ai-fluency-for-students` — https://anthropic.skilljar.com/ai-fluency-for-students  

**6 lessons** · 0 transcripts · 6 text · 0 transcript chars


*See full content in `md/ai-fluency-for-students_deep_v2.md`*


### Lessons


**Introduction and AI Fluency Framework**

- 1. Welcome to AI Fluency for students  *[YT, TEXT(1772)]*
- 2. AI Fluency Framework  *[YT, TEXT(5618)]*

**AI Fluency Framework applications for students**

- 3. AI as a learning partner  *[YT, TEXT(6377)]*
- 4. AI in career planning  *[YT, TEXT(7341)]*

**Conclusion & certificate**

- 5. Being the human in the loop  *[YT, TEXT(6008)]*
- 6. Certificate of completion  *[TEXT(10)]*

## AI Fluency for nonprofits

`ai-fluency-for-nonprofits` — https://anthropic.skilljar.com/ai-fluency-for-nonprofits  

**10 lessons** · 0 transcripts · 9 text · 0 transcript chars


*See full content in `md/ai-fluency-for-nonprofits_deep_v2.md`*


### Lessons


**Introduction and AI Fluency framework**

- 1. Welcome to AI Fluency for nonprofits  *[YT, TEXT(4719)]*
- 2. The 4D Framework  *[YT, TEXT(4403)]*

**The Description-Discernment loop**

- 3. Researching with AI  *[YT, TEXT(5388)]*
- 4. Writing with AI  *[YT, TEXT(5747)]*

**The Delegation-Diligence loop**

- 5. Understanding privacy and data  *[YT, TEXT(5101)]*
- 6. Data analysis with AI  *[YT, TEXT(6464)]*

**Putting it all together**

- 7. Workflow augmentation  *[YT, TEXT(5531)]*
- 8. Integration  *[YT, TEXT(5111)]*

**Conclusion and certificate**

- 9. Next steps  *[YT, TEXT(4569)]*
- 10. Course Quiz  *[meta]*

## Teaching AI Fluency

`teaching-ai-fluency` — https://anthropic.skilljar.com/teaching-ai-fluency  

**8 lessons** · 0 transcripts · 8 text · 0 transcript chars


*See full content in `md/teaching-ai-fluency_deep_v2.md`*


### Lessons


**Introduction and approaches to teaching AI Fluency**

- 1. Welcome & approaches to teaching AI Fluency  *[YT, TEXT(5785)]*
- 2. The Delegation-Diligence loop  *[YT, TEXT(4436)]*
- 3. The Description-Discernment loop  *[YT, TEXT(5032)]*

**Assessing AI Fluency**

- 4. How do we assess the 4Ds?  *[YT, TEXT(5438)]*
- 5. Designing assignments for AI Fluency  *[YT, TEXT(4683)]*

**AI's Impact on disciplinary content**

- 6. AI's impact and your discipline  *[YT, TEXT(6070)]*
- 7. Applying discipline expertise to AI Fluency  *[YT, TEXT(5012)]*

**Conclusion & certificate**

- 8. Certificate of completion  *[TEXT(10)]*