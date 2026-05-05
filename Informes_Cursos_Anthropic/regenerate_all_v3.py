#!/usr/bin/env python3
"""
Regenerate ALL output files (md, json, master references) with v3 content:
- YouTube transcripts (64 lessons)
- Quiz assessments (12 files, 104 questions)
- Updated stats and metrics

Files regenerated:
1. deep_extraction/md/<slug>_deep_v3.md (17 files) - full transcripts
2. deep_extraction/ENGINEERING_INTELLIGENCE_V3.md - master reference
3. deep_extraction/ENGINEERING_INTELLIGENCE_V3.json - master data
4. md/<slug>.md (17 files) - lightweight engineering intelligence references
5. json/<slug>.json (17 files) - lightweight structured data
6. ANTHROPIC_ACADEMY_MASTER_REFERENCE.md - root master
7. ANTHROPIC_ACADEMY_MASTER_REFERENCE.json - root master JSON
"""

import json
import os
import glob
import re
from datetime import date

BASE = "/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic"
V2_DIR = os.path.join(BASE, "deep_extraction", "json")
QUIZ_DIR = os.path.join(BASE, "deep_extraction", "transcripts", "quizzes")
DEEP_MD_DIR = os.path.join(BASE, "deep_extraction", "md")
ROOT_MD_DIR = os.path.join(BASE, "md")
ROOT_JSON_DIR = os.path.join(BASE, "json")

TODAY = date.today().strftime("%Y-%m-%d")

# Course metadata (categories, domains, learning paths)
COURSE_META = {
    "claude-with-the-anthropic-api": {"order": 1, "category": "core-api", "title": "Building with the Claude API", "difficulty": "intermediate", "tags": ["api","sdk","python","prompt-engineering","tool-use","rag","mcp","agents"], "domain": "Core API Development"},
    "claude-code-in-action": {"order": 2, "category": "developer-tools", "title": "Claude Code in Action", "difficulty": "intermediate", "tags": ["claude-code","cli","git","github","mcp","automation"], "domain": "Developer Tools"},
    "claude-101": {"order": 3, "category": "foundations", "title": "Claude 101", "difficulty": "beginner", "tags": ["introduction","fundamentals","claude-features"], "domain": "Foundations"},
    "introduction-to-claude-cowork": {"order": 4, "category": "developer-tools", "title": "Introduction to Claude Cowork", "difficulty": "beginner-intermediate", "tags": ["cowork","files","plugins","skills","task-loop"], "domain": "Developer Tools"},
    "ai-fluency-framework-foundations": {"order": 5, "category": "fluency-framework", "title": "AI Fluency: Framework & Foundations", "difficulty": "beginner", "tags": ["4d-framework","delegation","description","discernment","diligence","ethics","safety"], "domain": "AI Fluency"},
    "introduction-to-model-context-protocol": {"order": 6, "category": "mcp", "title": "Introduction to Model Context Protocol", "difficulty": "intermediate", "tags": ["mcp","protocol","tools","resources","prompts","python-sdk"], "domain": "Model Context Protocol"},
    "ai-fluency-for-educators": {"order": 7, "category": "fluency-framework", "title": "AI Fluency for Educators", "difficulty": "beginner-intermediate", "tags": ["education","4d-framework","teaching"], "domain": "AI Fluency"},
    "ai-fluency-for-students": {"order": 8, "category": "fluency-framework", "title": "AI Fluency for Students", "difficulty": "beginner", "tags": ["students","4d-framework","learning","career-planning"], "domain": "AI Fluency"},
    "model-context-protocol-advanced-topics": {"order": 9, "category": "mcp", "title": "Model Context Protocol: Advanced Topics", "difficulty": "advanced", "tags": ["mcp","sampling","notifications","transport","stdio","sse","http","production"], "domain": "Model Context Protocol"},
    "claude-in-amazon-bedrock": {"order": 10, "category": "cloud-integration", "title": "Claude with Amazon Bedrock", "difficulty": "intermediate-advanced", "tags": ["aws","bedrock","api","rag","tool-use","agents","mcp"], "domain": "Cloud Integration"},
    "claude-with-google-vertex": {"order": 11, "category": "cloud-integration", "title": "Claude with Google Cloud's Vertex AI", "difficulty": "intermediate-advanced", "tags": ["gcp","vertex-ai","api","rag","tool-use","computer-use"], "domain": "Cloud Integration"},
    "teaching-ai-fluency": {"order": 12, "category": "fluency-framework", "title": "Teaching AI Fluency", "difficulty": "intermediate", "tags": ["teaching","4d-framework","instructor-led","assessment"], "domain": "AI Fluency"},
    "ai-fluency-for-nonprofits": {"order": 13, "category": "fluency-framework", "title": "AI Fluency for Nonprofits", "difficulty": "beginner", "tags": ["nonprofits","4d-framework","fundraising","mission-driven"], "domain": "AI Fluency"},
    "introduction-to-agent-skills": {"order": 14, "category": "agent-development", "title": "Introduction to Agent Skills", "difficulty": "intermediate", "tags": ["skills","claude-code","SKILL.md","plugins","enterprise"], "domain": "Agent Development"},
    "introduction-to-subagents": {"order": 15, "category": "agent-development", "title": "Introduction to Subagents", "difficulty": "intermediate", "tags": ["subagents","claude-code","delegation","context-management"], "domain": "Agent Development"},
    "ai-capabilities-and-limitations": {"order": 16, "category": "fluency-framework", "title": "AI Capabilities and Limitations", "difficulty": "beginner", "tags": ["capabilities","limitations","mental-model","generative-ai"], "domain": "AI Fluency"},
    "claude-code-101": {"order": 17, "category": "developer-tools", "title": "Claude Code 101", "difficulty": "beginner-intermediate", "tags": ["claude-code","agentic-loop","explore-plan-code-commit"], "domain": "Developer Tools"},
}


def load_quiz_for_lesson(slug, lesson_idx):
    """Load quiz JSON for a specific lesson if it exists."""
    quiz_path = os.path.join(QUIZ_DIR, f"{slug}_lesson_{lesson_idx}.json")
    if os.path.exists(quiz_path):
        try:
            with open(quiz_path) as f:
                return json.load(f)
        except Exception:
            return None
    return None


def get_quiz_count(slug):
    if not os.path.isdir(QUIZ_DIR):
        return 0
    return len([f for f in os.listdir(QUIZ_DIR) if f.startswith(slug + "_lesson_") and f.endswith(".json")])


def regenerate_deep_md(course_data):
    """Generate the FULL deep .md file with all content (transcripts, quizzes, etc)."""
    slug = course_data["course_slug"]
    title = course_data["course_title"]
    meta = COURSE_META.get(slug, {})
    stats = course_data.get("stats", {})

    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> **Source:** [{course_data['course_url']}]({course_data['course_url']})")
    lines.append(f"> **Category:** {meta.get('category','N/A')} | **Difficulty:** {meta.get('difficulty','N/A')} | **Domain:** {meta.get('domain','N/A')}")
    lines.append(f"> **Tags:** {', '.join(meta.get('tags',[]))}")
    lines.append(f"> **Extracted:** {course_data.get('extracted_at','')[:10]} | **Version:** v3 (with YouTube transcripts + quiz content)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Stats summary
    lines.append("## Extraction Statistics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Total Lessons | {stats.get('total_lessons',0)} |")
    lines.append(f"| Sections | {len(course_data.get('sections',[]))} |")
    lines.append(f"| JW Player Transcripts | {stats.get('lessons_with_transcript',0)} |")
    lines.append(f"| YouTube Transcripts | {stats.get('lessons_with_youtube_transcript',0)} |")
    lines.append(f"| Modular Text Lessons | {stats.get('lessons_with_modular_text',0)} |")
    lines.append(f"| Quiz Assessments | {get_quiz_count(slug)} |")

    jw_chars = sum(l.get("total_transcript_chars",0) for l in course_data["lessons"] if not l.get("youtube_transcript"))
    yt_chars = stats.get("youtube_transcript_chars",0)
    mod_chars = sum(len(l.get("modular_text","") or "") for l in course_data["lessons"])
    total_chars = jw_chars + yt_chars + mod_chars

    lines.append(f"| JW Transcript Chars | {jw_chars:,} |")
    lines.append(f"| YouTube Transcript Chars | {yt_chars:,} |")
    lines.append(f"| Modular Text Chars | {mod_chars:,} |")
    lines.append(f"| **Total Content** | **{total_chars:,}** |")
    lines.append("")

    # Curriculum
    lines.append("## Curriculum Structure")
    lines.append("")
    for sec in course_data.get("sections", []):
        if isinstance(sec, dict):
            lines.append(f"- **{sec.get('title','?')}** ({sec.get('lesson_count',0)} lessons)")
        else:
            lines.append(f"- {sec}")
    lines.append("")

    # Full lessons
    lines.append("---")
    lines.append("")
    lines.append("## Complete Lesson Content")
    lines.append("")

    current_section = None
    for lesson in course_data.get("lessons", []):
        section_name = lesson.get("section", "Uncategorized")
        idx = lesson.get("index", 0)
        l_title = lesson.get("title", "Untitled")
        l_url = lesson.get("url", "")

        if section_name != current_section:
            current_section = section_name
            lines.append(f"### {section_name}")
            lines.append("")

        lines.append(f"#### Lesson {idx}: {l_title}")
        lines.append("")
        lines.append(f"*Source:* [{l_url}]({l_url})")
        lines.append("")

        # Video metadata
        videos = lesson.get("videos", [])
        if videos:
            for v in videos:
                meta_parts = []
                if v.get("video_title"):
                    meta_parts.append(f"**Video:** {v['video_title']}")
                if v.get("duration_s"):
                    d = v["duration_s"]
                    meta_parts.append(f"**Duration:** {d//60}m {d%60}s")
                if v.get("platform"):
                    meta_parts.append(f"**Platform:** {v['platform']}")
                if v.get("available_caption_languages"):
                    meta_parts.append(f"**Captions:** {', '.join(v['available_caption_languages'])}")
                if meta_parts:
                    lines.append(" | ".join(meta_parts))
                    lines.append("")

        # Modular text
        mt = lesson.get("modular_text")
        if mt and mt.strip():
            lines.append(mt.strip())
            lines.append("")

        # JW Player transcript
        if videos:
            for v in videos:
                tr = v.get("transcript_english", "")
                if tr and tr.strip():
                    lines.append("**Video Transcript (JW Player):**")
                    lines.append("")
                    # Clean up multiple newlines
                    cleaned = re.sub(r'\n{3,}', '\n\n', tr.strip())
                    lines.append(cleaned)
                    lines.append("")

        # YouTube transcript
        yt_tr = lesson.get("youtube_transcript", "")
        if yt_tr and yt_tr.strip():
            lines.append("**Video Transcript (YouTube via yt-dlp):**")
            lines.append("")
            lines.append(yt_tr.strip())
            lines.append("")

        # Code blocks
        code_blocks = lesson.get("code_blocks", [])
        if code_blocks:
            lines.append("**Code Examples:**")
            lines.append("")
            for cb in code_blocks:
                if isinstance(cb, dict):
                    text = cb.get("text", str(cb))
                else:
                    text = str(cb)
                lines.append("```")
                lines.append(text)
                lines.append("```")
                lines.append("")

        # External links
        ext = lesson.get("external_links", [])
        if ext:
            lines.append("**Resources & Links:**")
            lines.append("")
            for link in ext[:20]:
                if isinstance(link, dict):
                    text = link.get("text", "")
                    url = link.get("url", "")
                    if text and url:
                        lines.append(f"- [{text}]({url})")
                    elif url:
                        lines.append(f"- {url}")
                else:
                    lines.append(f"- {link}")
            lines.append("")

        # Quiz content
        quiz = load_quiz_for_lesson(slug, idx)
        if quiz and quiz.get("questions"):
            lines.append(f"**Assessment ({len(quiz['questions'])} questions):**")
            lines.append("")
            for qi, q in enumerate(quiz["questions"], 1):
                lines.append(f"**Q{qi}:** {q.get('question_text','')}")
                lines.append("")
                for opt in q.get("options", []):
                    if isinstance(opt, dict):
                        marker = "**[CORRECT]**" if opt.get("is_correct") else "[ ]"
                        lines.append(f"- {marker} {opt.get('text','')}")
                    else:
                        lines.append(f"- {opt}")
                lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(f"*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | {TODAY}*")
    lines.append("")
    return "\n".join(lines)


def regenerate_lightweight_md(course_data):
    """Generate the lightweight engineering intelligence .md (no full transcripts, just key insights)."""
    slug = course_data["course_slug"]
    title = course_data["course_title"]
    meta = COURSE_META.get(slug, {})
    stats = course_data.get("stats", {})

    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> **Source:** [{course_data['course_url']}]({course_data['course_url']})")
    lines.append(f"> **Category:** {meta.get('category','N/A')} | **Difficulty:** {meta.get('difficulty','N/A')}")
    lines.append(f"> **Tags:** {', '.join(meta.get('tags',[]))}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Quick Stats")
    lines.append("")

    yt_count = stats.get("lessons_with_youtube_transcript", 0)
    jw_count = stats.get("lessons_with_transcript", 0)
    quiz_count = get_quiz_count(slug)

    lines.append(f"- **Total lessons:** {stats.get('total_lessons',0)}")
    lines.append(f"- **JW Player transcripts:** {jw_count}")
    lines.append(f"- **YouTube transcripts (v3):** {yt_count}")
    lines.append(f"- **Quiz assessments (v3):** {quiz_count}")
    lines.append(f"- **Sections:** {len(course_data.get('sections',[]))}")
    lines.append("")

    lines.append("## Curriculum Structure")
    lines.append("")
    for sec in course_data.get("sections", []):
        if isinstance(sec, dict):
            lines.append(f"### {sec.get('title','?')}")
            lines.append("")
            # List lessons in this section
            for lesson in course_data.get("lessons", []):
                if lesson.get("section") == sec.get("title"):
                    has_jw = any(v.get("transcript_english") for v in lesson.get("videos",[]))
                    has_yt = bool(lesson.get("youtube_transcript"))
                    has_mod = bool(lesson.get("modular_text"))
                    quiz = load_quiz_for_lesson(slug, lesson["index"])
                    badges = []
                    if has_jw: badges.append("JW")
                    if has_yt: badges.append("YT")
                    if has_mod: badges.append("MOD")
                    if quiz: badges.append(f"QUIZ({len(quiz.get('questions',[]))})")
                    badge_str = f" `[{', '.join(badges)}]`" if badges else ""
                    lines.append(f"- **Lesson {lesson['index']}:** {lesson.get('title','?')}{badge_str}")
            lines.append("")

    lines.append("## Engineering Intelligence Highlights")
    lines.append("")
    lines.append(f"This course contains {stats.get('total_lessons',0)} lessons with comprehensive coverage of {meta.get('domain','its domain')}. ")
    lines.append("Full lesson transcripts, code examples, and quiz assessments are available in the deep_extraction reports.")
    lines.append("")

    lines.append("## See Also")
    lines.append("")
    lines.append(f"- Full deep extraction: `deep_extraction/md/{slug}_deep_v2.md`")
    lines.append(f"- Structured data: `deep_extraction/json/{slug}_deep_v2.json`")
    lines.append(f"- Professional report: `{meta.get('order',0):02d}_*.docx`")
    lines.append("")
    lines.append(f"---")
    lines.append(f"*Engineering Intelligence v3 | Updated {TODAY}*")
    lines.append("")
    return "\n".join(lines)


def regenerate_lightweight_json(course_data):
    """Generate the lightweight structured JSON."""
    slug = course_data["course_slug"]
    meta = COURSE_META.get(slug, {})
    stats = course_data.get("stats", {})

    yt_count = stats.get("lessons_with_youtube_transcript", 0)
    jw_count = stats.get("lessons_with_transcript", 0)
    quiz_count = get_quiz_count(slug)
    yt_chars = stats.get("youtube_transcript_chars", 0)
    jw_chars = sum(l.get("total_transcript_chars",0) for l in course_data["lessons"] if not l.get("youtube_transcript"))
    mod_chars = sum(len(l.get("modular_text","") or "") for l in course_data["lessons"])

    return {
        "id": f"{meta.get('order',0):02d}",
        "slug": slug,
        "title": course_data["course_title"],
        "url": course_data["course_url"],
        "category": meta.get("category"),
        "difficulty": meta.get("difficulty"),
        "domain": meta.get("domain"),
        "tags": meta.get("tags", []),
        "stats": {
            "total_lessons": stats.get("total_lessons", 0),
            "sections": len(course_data.get("sections", [])),
            "jw_transcripts": jw_count,
            "youtube_transcripts": yt_count,
            "modular_text_lessons": stats.get("lessons_with_modular_text", 0),
            "quiz_assessments": quiz_count,
            "jw_chars": jw_chars,
            "youtube_chars": yt_chars,
            "modular_chars": mod_chars,
            "total_content_chars": jw_chars + yt_chars + mod_chars,
        },
        "sections": course_data.get("sections", []),
        "lessons_index": [
            {
                "index": l.get("index"),
                "section": l.get("section"),
                "title": l.get("title"),
                "url": l.get("url"),
                "has_jw_transcript": any(v.get("transcript_english") for v in l.get("videos",[])),
                "has_youtube_transcript": bool(l.get("youtube_transcript")),
                "has_modular_text": bool(l.get("modular_text")),
                "has_quiz": bool(load_quiz_for_lesson(slug, l.get("index"))),
            }
            for l in course_data.get("lessons", [])
        ],
        "extracted_at": course_data.get("extracted_at"),
        "version": "v3",
        "v3_updates": {
            "youtube_transcripts_added": yt_count,
            "quiz_extractions_added": quiz_count,
        },
    }


def generate_master_md(all_data):
    """Generate the master ENGINEERING_INTELLIGENCE_V3.md."""
    lines = []
    lines.append("# Anthropic Academy - Engineering Intelligence v3")
    lines.append("")
    lines.append(f"> **Generated:** {TODAY} | **Courses:** {len(all_data)} | **Version:** v3")
    lines.append("> **New in v3:** YouTube transcripts (yt-dlp) + Quiz assessments + Updated metrics")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Global stats
    total_lessons = sum(d.get("stats",{}).get("total_lessons",0) for d in all_data)
    total_jw = sum(d.get("stats",{}).get("lessons_with_transcript",0) for d in all_data)
    total_yt = sum(d.get("stats",{}).get("lessons_with_youtube_transcript",0) for d in all_data)
    total_quiz = sum(get_quiz_count(d["course_slug"]) for d in all_data)

    total_chars = 0
    for d in all_data:
        jw = sum(l.get("total_transcript_chars",0) for l in d["lessons"] if not l.get("youtube_transcript"))
        yt = d.get("stats",{}).get("youtube_transcript_chars",0)
        mod = sum(len(l.get("modular_text","") or "") for l in d["lessons"])
        total_chars += jw + yt + mod

    lines.append("## Global Statistics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Courses | {len(all_data)} |")
    lines.append(f"| Total Lessons | {total_lessons} |")
    lines.append(f"| JW Player Transcripts | {total_jw} |")
    lines.append(f"| YouTube Transcripts (NEW v3) | {total_yt} |")
    lines.append(f"| Quiz Assessments (NEW v3) | {total_quiz} |")
    lines.append(f"| **Total Content Characters** | **{total_chars:,}** |")
    lines.append("")

    # Course index
    lines.append("## Course Index")
    lines.append("")
    lines.append("| # | Course | Category | Difficulty | Lessons | JW | YT | Quiz |")
    lines.append("|---|--------|----------|------------|---------|----|----|------|")

    sorted_data = sorted(all_data, key=lambda d: COURSE_META.get(d["course_slug"], {}).get("order", 99))
    for d in sorted_data:
        slug = d["course_slug"]
        meta = COURSE_META.get(slug, {})
        s = d.get("stats", {})
        order = meta.get("order", 0)
        lines.append(
            f"| {order:02d} | [{d['course_title']}](deep_extraction/md/{slug}_deep_v2.md) | "
            f"{meta.get('category','-')} | {meta.get('difficulty','-')} | "
            f"{s.get('total_lessons',0)} | {s.get('lessons_with_transcript',0)} | "
            f"{s.get('lessons_with_youtube_transcript',0)} | {get_quiz_count(slug)} |"
        )
    lines.append("")

    # By domain
    lines.append("## Courses by Domain")
    lines.append("")
    domains = {}
    for d in sorted_data:
        slug = d["course_slug"]
        domain = COURSE_META.get(slug, {}).get("domain", "Other")
        domains.setdefault(domain, []).append(d)
    for domain, courses in domains.items():
        lines.append(f"### {domain}")
        lines.append("")
        for c in courses:
            s = c.get("stats", {})
            total = (
                s.get("total_transcript_chars", 0)
                + s.get("youtube_transcript_chars", 0)
                + sum(len(l.get("modular_text","") or "") for l in c["lessons"])
            )
            lines.append(f"- **{c['course_title']}** — {s.get('total_lessons',0)} lessons, {total:,} chars")
        lines.append("")

    lines.append("## v3 Improvements vs v2")
    lines.append("")
    lines.append("| Improvement | v2 | v3 | Delta |")
    lines.append("|---|---:|---:|---:|")
    lines.append(f"| YouTube transcripts | 0 | {total_yt} | **+{total_yt}** |")
    lines.append(f"| Quiz assessments | 0 | {total_quiz} | **+{total_quiz}** |")
    lines.append(f"| Total content chars | 2,220,093 | {total_chars:,} | **+{total_chars-2220093:,}** |")
    lines.append("")

    lines.append("## Methodology")
    lines.append("")
    lines.append("1. **JW Player transcripts:** Extracted via the public CDN caption endpoint (English SRT tracks)")
    lines.append("2. **YouTube transcripts (NEW v3):** Extracted via yt-dlp CLI with auto-generated English captions")
    lines.append("3. **Quiz assessments (NEW v3):** Extracted via Playwright DOM parsing of authenticated quiz pages")
    lines.append("4. **Modular text:** Parsed from Skilljar lesson HTML via DOMParser")
    lines.append("")
    lines.append("All content extracted from authenticated Skilljar sessions. Zero fabrication.")
    lines.append("")
    lines.append("---")
    lines.append(f"*Anthropic Academy Engineering Intelligence v3 | {TODAY}*")
    return "\n".join(lines)


def generate_master_json(all_data):
    """Generate master ENGINEERING_INTELLIGENCE_V3.json (lightweight, not 4MB)."""
    sorted_data = sorted(all_data, key=lambda d: COURSE_META.get(d["course_slug"], {}).get("order", 99))

    total_lessons = sum(d.get("stats",{}).get("total_lessons",0) for d in all_data)
    total_jw = sum(d.get("stats",{}).get("lessons_with_transcript",0) for d in all_data)
    total_yt = sum(d.get("stats",{}).get("lessons_with_youtube_transcript",0) for d in all_data)
    total_quiz = sum(get_quiz_count(d["course_slug"]) for d in all_data)

    total_chars = 0
    for d in all_data:
        jw = sum(l.get("total_transcript_chars",0) for l in d["lessons"] if not l.get("youtube_transcript"))
        yt = d.get("stats",{}).get("youtube_transcript_chars",0)
        mod = sum(len(l.get("modular_text","") or "") for l in d["lessons"])
        total_chars += jw + yt + mod

    return {
        "metadata": {
            "title": "Anthropic Academy Engineering Intelligence v3",
            "generated": TODAY,
            "version": "v3",
            "total_courses": len(all_data),
            "v3_improvements": [
                "YouTube transcripts via yt-dlp (64 lessons, +310K chars)",
                "Quiz assessments via Playwright DOM (12 files, 104 questions)",
                "Updated stats and quality metrics",
            ],
        },
        "global_stats": {
            "total_courses": len(all_data),
            "total_lessons": total_lessons,
            "jw_transcripts": total_jw,
            "youtube_transcripts": total_yt,
            "quiz_assessments": total_quiz,
            "total_content_chars": total_chars,
        },
        "courses": [
            regenerate_lightweight_json(d) for d in sorted_data
        ],
    }


# ========== EXECUTION ==========
print("=" * 100)
print("  REGENERATING ALL OUTPUT FILES (v3)")
print("=" * 100)

# Load all course data
all_courses = []
for f in sorted(glob.glob(os.path.join(V2_DIR, "*_deep_v2.json"))):
    with open(f, 'r', encoding='utf-8') as fh:
        all_courses.append(json.load(fh))

print(f"Loaded {len(all_courses)} course JSONs\n")

# 1. Regenerate deep_extraction/md/<slug>_deep_v2.md (full content)
print("[1/5] Regenerating deep_extraction/md/ (full content)...")
for d in all_courses:
    slug = d["course_slug"]
    md = regenerate_deep_md(d)
    out_path = os.path.join(DEEP_MD_DIR, f"{slug}_deep_v2.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  [OK] {slug:<50} {size_kb:>5} KB")

# 2. Regenerate root /md/ lightweight engineering intelligence
print("\n[2/5] Regenerating md/ (lightweight engineering intelligence)...")
for d in all_courses:
    slug = d["course_slug"]
    meta = COURSE_META.get(slug, {})
    md = regenerate_lightweight_md(d)
    fname = f"{meta.get('order',0):02d}_{slug}.md"
    out_path = os.path.join(ROOT_MD_DIR, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  [OK] {fname:<55} {size_kb:>4} KB")

# 3. Regenerate root /json/ lightweight structured data
print("\n[3/5] Regenerating json/ (lightweight structured)...")
for d in all_courses:
    slug = d["course_slug"]
    meta = COURSE_META.get(slug, {})
    js = regenerate_lightweight_json(d)
    fname = f"{meta.get('order',0):02d}_{slug}.json"
    out_path = os.path.join(ROOT_JSON_DIR, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(js, f, indent=2, ensure_ascii=False)
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  [OK] {fname:<55} {size_kb:>4} KB")

# 4. Regenerate ENGINEERING_INTELLIGENCE_V3.md
print("\n[4/5] Regenerating master ENGINEERING_INTELLIGENCE_V3.md/.json...")
master_md = generate_master_md(all_courses)
master_md_path = os.path.join(BASE, "deep_extraction", "ENGINEERING_INTELLIGENCE_V3.md")
with open(master_md_path, 'w', encoding='utf-8') as f:
    f.write(master_md)
print(f"  [OK] deep_extraction/ENGINEERING_INTELLIGENCE_V3.md ({os.path.getsize(master_md_path)//1024} KB)")

master_json = generate_master_json(all_courses)
master_json_path = os.path.join(BASE, "deep_extraction", "ENGINEERING_INTELLIGENCE_V3.json")
with open(master_json_path, 'w', encoding='utf-8') as f:
    json.dump(master_json, f, indent=2, ensure_ascii=False)
print(f"  [OK] deep_extraction/ENGINEERING_INTELLIGENCE_V3.json ({os.path.getsize(master_json_path)//1024} KB)")

# 5. Regenerate root ANTHROPIC_ACADEMY_MASTER_REFERENCE.md/.json
print("\n[5/5] Regenerating root ANTHROPIC_ACADEMY_MASTER_REFERENCE.md/.json...")
root_master_md = os.path.join(BASE, "ANTHROPIC_ACADEMY_MASTER_REFERENCE.md")
with open(root_master_md, 'w', encoding='utf-8') as f:
    f.write(master_md)
print(f"  [OK] ANTHROPIC_ACADEMY_MASTER_REFERENCE.md ({os.path.getsize(root_master_md)//1024} KB)")

root_master_json = os.path.join(BASE, "ANTHROPIC_ACADEMY_MASTER_REFERENCE.json")
with open(root_master_json, 'w', encoding='utf-8') as f:
    json.dump(master_json, f, indent=2, ensure_ascii=False)
print(f"  [OK] ANTHROPIC_ACADEMY_MASTER_REFERENCE.json ({os.path.getsize(root_master_json)//1024} KB)")

print("\n" + "=" * 100)
print(f"  ALL FILES REGENERATED v3 | {TODAY}")
print("=" * 100)
