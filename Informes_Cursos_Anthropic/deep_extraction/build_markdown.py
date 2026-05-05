#!/usr/bin/env python3
"""Build per-course markdown and master reference from deep_extraction JSON files."""
import json
import glob
import os
from pathlib import Path

BASE = Path("/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction")
JSON_DIR = BASE / "json"
MD_DIR = BASE / "md"
MD_DIR.mkdir(exist_ok=True)

courses = []
for fp in sorted(JSON_DIR.glob("course_*.json")):
    with open(fp, "r", encoding="utf-8") as f:
        courses.append(json.load(f))

def course_md(c):
    lines = []
    lines.append(f"# Course {c['course_num']:02d}: {c['title']}")
    lines.append("")
    lines.append(f"**Source URL:** {c['url']}")
    lines.append(f"**Extraction method:** {c.get('extraction_method','dom_text')}")
    lines.append(f"**Template:** {c.get('template','unknown')}")
    lines.append(f"**Extraction timestamp:** {c.get('extraction_timestamp','2026-04-10')}")
    lines.append(f"**Authentication required for lesson content:** {c.get('auth_required_for_lessons', True)}")
    lines.append("")
    if c.get("subtitle"):
        lines.append(f"> {c['subtitle']}")
        lines.append("")
    if c.get("description"):
        lines.append(f"> {c['description']}")
        lines.append("")
    if c.get("stats"):
        s = c["stats"]
        lines.append("## Stats")
        lines.append("")
        lines.append(f"- Lectures: {s.get('lectures','n/a')}")
        lines.append(f"- Hours of video: {s.get('hours_of_video','n/a')}")
        lines.append(f"- Quizzes: {s.get('quizzes','n/a')}")
        lines.append(f"- Certificate of completion: {s.get('certificate',False)}")
        lines.append("")
    if c.get("about"):
        lines.append("## About this course")
        lines.append("")
        lines.append(c["about"])
        lines.append("")
    if c.get("learning_objectives"):
        lines.append("## Learning objectives")
        lines.append("")
        for lo in c["learning_objectives"]:
            lines.append(f"- {lo}")
        lines.append("")
    if c.get("prerequisites"):
        lines.append("## Prerequisites")
        lines.append("")
        for p in c["prerequisites"]:
            lines.append(f"- {p}")
        lines.append("")
    if c.get("audience"):
        lines.append("## Who this course is for")
        lines.append("")
        lines.append(c["audience"])
        lines.append("")
    # sj template
    if c.get("chapters"):
        lines.append("## Curriculum (lesson-level, public)")
        lines.append("")
        total = 0
        for ch in c["chapters"]:
            title = ch.get("chapter") or ch.get("chapter_title") or "(untitled)"
            lines.append(f"### {ch.get('chapter_num','')} {title}".rstrip())
            lines.append("")
            for l in ch.get("lessons", []):
                time = f" ({l['time']})" if l.get("time") else ""
                ltype = l.get("type","?")
                lines.append(f"- Lesson {l.get('num','?')}: **{l.get('title','(untitled)')}** — type: `{ltype}`{time}")
                total += 1
            lines.append("")
        lines.append(f"**Total lessons (from public curriculum):** {total}")
        lines.append("")
    # clp template
    if c.get("sections"):
        lines.append("## Course sections (marketing page - section-level only)")
        lines.append("")
        for s in c["sections"]:
            lines.append(f"### Section {s['section_num']}: {s['name']} — {s.get('lessonCount','')}")
            lines.append("")
            if s.get("description"):
                lines.append(s["description"])
                lines.append("")
            if s.get("previewImages"):
                lines.append("**Preview images:**")
                for img in s["previewImages"]:
                    lines.append(f"- {img}")
                lines.append("")
        lines.append("")
    if c.get("key_framework"):
        kf = c["key_framework"]
        lines.append("## Key framework")
        lines.append("")
        lines.append(f"**{kf['name']}**")
        lines.append("")
        for p in kf.get("properties", []):
            lines.append(f"- {p}")
        lines.append("")
    if c.get("note"):
        lines.append(f"> Note: {c['note']}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"Extracted as part of the deep_extraction pipeline from `{c['url']}`.")
    lines.append(f"Individual lesson videos, transcripts, slide text, quiz content, and downloadable resources are gated behind Skilljar authentication and were not retrieved in this run.")
    return "\n".join(lines)

for c in courses:
    slug = c["slug"]
    num = c["course_num"]
    outp = MD_DIR / f"course_{num:02d}_{slug}_deep.md"
    outp.write_text(course_md(c), encoding="utf-8")

print(f"Wrote {len(courses)} course markdown files")

# Build master reference
master_lines = ["# Anthropic Academy — Deep Extraction Master Reference (v2)", "",
                f"Generated: 2026-04-10", "",
                "This document aggregates the deepest publicly accessible information for all 17 Anthropic Academy courses on https://anthropic.skilljar.com/. Individual lesson content (videos, transcripts, slide text, quiz questions, code examples) is gated behind Skilljar authentication and was NOT extracted in this run — a LOGIN_REQUIRED.md file documents what remains blocked.", "",
                "## Summary statistics", ""]
total_lectures = 0
total_hours = 0.0
lesson_level = 0
section_level = 0
for c in courses:
    s = c.get("stats") or {}
    if s.get("lectures"): total_lectures += s["lectures"]
    if s.get("hours_of_video"): total_hours += s["hours_of_video"]
    if c.get("chapters"):
        lesson_level += 1
    if c.get("sections"):
        section_level += 1
master_lines.append(f"- Total courses indexed: {len(courses)}")
master_lines.append(f"- Total lectures (from marketing stats): **{total_lectures}**")
master_lines.append(f"- Total hours of video (from marketing stats): **{total_hours:.2f}**")
master_lines.append(f"- Courses with public lesson-level titles (sj template): **{lesson_level}**")
master_lines.append(f"- Courses with only section-level public info (clp template): **{section_level}**")
master_lines.append("")
master_lines.append("## Course index")
master_lines.append("")
master_lines.append("| # | Title | Template | Lectures | Hours | Quizzes | URL |")
master_lines.append("|---|-------|----------|---------:|------:|--------:|-----|")
for c in courses:
    s = c.get("stats") or {}
    master_lines.append(f"| {c['course_num']:02d} | {c['title']} | {c.get('template','?')} | {s.get('lectures','-')} | {s.get('hours_of_video','-')} | {s.get('quizzes','-')} | [{c['slug']}]({c['url']}) |")
master_lines.append("")

for c in courses:
    master_lines.append(f"## {c['course_num']:02d}. {c['title']}")
    master_lines.append("")
    master_lines.append(f"- URL: {c['url']}")
    if c.get("subtitle"): master_lines.append(f"- Subtitle: {c['subtitle']}")
    if c.get("description"): master_lines.append(f"- Description: {c['description']}")
    s = c.get("stats") or {}
    if s: master_lines.append(f"- Stats: {s.get('lectures','?')} lectures, {s.get('hours_of_video','?')}h, {s.get('quizzes','?')} quizzes, certificate: {s.get('certificate',False)}")
    master_lines.append("")
    if c.get("learning_objectives"):
        master_lines.append("**Learning objectives:**")
        for lo in c["learning_objectives"]:
            master_lines.append(f"- {lo}")
        master_lines.append("")
    if c.get("prerequisites"):
        master_lines.append("**Prerequisites:**")
        for p in c["prerequisites"]:
            master_lines.append(f"- {p}")
        master_lines.append("")
    if c.get("chapters"):
        master_lines.append("**Curriculum (lesson-level):**")
        for ch in c["chapters"]:
            master_lines.append(f"- {ch.get('chapter','(untitled)')}")
            for l in ch.get("lessons", []):
                master_lines.append(f"  - {l['num']}. {l['title']}")
        master_lines.append("")
    if c.get("sections"):
        master_lines.append("**Sections (section-level only):**")
        for sec in c["sections"]:
            master_lines.append(f"- Section {sec['section_num']}: {sec['name']} ({sec.get('lessonCount','')}) — {sec.get('description','')[:200]}")
        master_lines.append("")
    master_lines.append("---")
    master_lines.append("")

(BASE / "ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.md").write_text("\n".join(master_lines), encoding="utf-8")
print(f"Wrote master reference: {BASE / 'ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.md'}")

# Master JSON
master_json = {
    "version": "2.0-deep",
    "generated": "2026-04-10",
    "source": "https://anthropic.skilljar.com/",
    "extraction_method": "dom_text via Playwright MCP (public pages only)",
    "auth_state": "not_logged_in",
    "total_courses": len(courses),
    "total_lectures_marketed": total_lectures,
    "total_hours_marketed": total_hours,
    "courses": courses
}
(BASE / "ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.json").write_text(json.dumps(master_json, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote master JSON: {BASE / 'ANTHROPIC_ACADEMY_DEEP_MASTER_REFERENCE.json'}")
