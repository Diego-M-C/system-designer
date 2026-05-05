#!/usr/bin/env python3
import json, os, re
from collections import defaultdict

BASE = "/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/json"
PROG = "/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/progress"
os.makedirs(PROG, exist_ok=True)
files = sorted([f for f in os.listdir(BASE) if f.endswith("_deep_v2.json")])

def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()

all_courses = []
image_catalog = []
link_catalog = []
code_enrichment = []

for fname in files:
    with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
    slug = data.get('course_slug', fname.replace('_deep_v2.json',''))
    title = data.get('course_title', slug)
    lessons = data.get('lessons', [])
    tl = len(lessons)
    lwc = 0; lwt = 0; lwv = 0; ttc = 0
    ecb = 0; ecc = 0; ei = 0; el = 0
    vt = 0; vs = 0; vu = 0
    mtc = 0; mhc = 0; ytc = 0; jwc = 0; qc = 0
    secs = set()
    new_code = []
    c_imgs = []
    c_links = []

    for lesson in lessons:
        mt = lesson.get('modular_text','') or ''
        mh = lesson.get('modular_html','') or ''
        videos = lesson.get('videos', [])
        cbs = lesson.get('code_blocks', [])
        imgs = lesson.get('images', [])
        els = lesson.get('external_links', [])
        tc = lesson.get('total_transcript_chars', 0) or 0
        yt_ids = lesson.get('youtube_ids', [])
        lt = lesson.get('title','')
        ls = lesson.get('section','')
        lu = lesson.get('url','')
        li = lesson.get('index','?')
        ltypes = lesson.get('types', [])

        if lt and lt.strip(): vt += 1
        if ls and ls.strip(): vs += 1; secs.add(ls)
        if lu and lu.startswith('http'): vu += 1
        has_content = bool(mt) or (mh and len(mh.strip()) > 50) or tc > 0
        if has_content: lwc += 1
        mtc += len(mt)
        mhc += len(mh)
        hv = len(videos) > 0 or len(yt_ids) > 0
        if hv: lwv += 1
        for v in videos:
            if v.get('platform') == 'youtube': ytc += 1
            elif v.get('platform') == 'jwplayer': jwc += 1
        if yt_ids and not videos: ytc += len(yt_ids)
        if 'lesson-quiz' in str(ltypes): qc += 1
        if tc > 0:
            lwt += 1
            ttc += tc
        ecb += len(cbs)
        for cb in cbs:
            if isinstance(cb, dict): ecc += len(cb.get('code',''))
            elif isinstance(cb, str): ecc += len(cb)
        ei += len(imgs)
        el += len(els)

        # Re-parse for missed code
        existing_set = set()
        for cb in cbs:
            if isinstance(cb, dict): existing_set.add(cb.get('code','')[:50])
            elif isinstance(cb, str): existing_set.add(cb[:50])
        for m in re.finditer(r'<pre[^>]*>(.*?)</pre>', mh, re.DOTALL|re.IGNORECASE):
            content = strip_tags(m.group(1)).strip()
            if len(content) > 10 and content[:50] not in existing_set:
                new_code.append({
                    'language': '', 'code': content[:200], 'chars': len(content),
                    'source': 'pre_tag', 'course': slug, 'lesson_index': li, 'lesson_title': lt
                })
                existing_set.add(content[:50])
        no_pre = re.sub(r'<pre[^>]*>.*?</pre>', '', mh, flags=re.DOTALL|re.IGNORECASE)
        for m in re.finditer(r'<code[^>]*>(.*?)</code>', no_pre, re.DOTALL|re.IGNORECASE):
            content = strip_tags(m.group(1)).strip()
            if len(content) > 30 and content[:50] not in existing_set:
                new_code.append({
                    'language': '', 'code': content[:200], 'chars': len(content),
                    'source': 'code_tag_inline', 'course': slug, 'lesson_index': li, 'lesson_title': lt
                })
                existing_set.add(content[:50])

        # Images
        for m in re.finditer(r'<img[^>]*src="([^"]+)"[^>]*>', mh, re.IGNORECASE):
            alt_m = re.search(r'alt="([^"]*)"', m.group(0))
            c_imgs.append({'url': m.group(1), 'alt': alt_m.group(1) if alt_m else '', 'course': slug, 'lesson_index': li, 'lesson_title': lt})
        for img in imgs:
            u = img.get('url', img.get('src','')) if isinstance(img, dict) else (img if isinstance(img, str) else '')
            if u:
                c_imgs.append({'url': u, 'alt': img.get('alt','') if isinstance(img, dict) else '', 'course': slug, 'lesson_index': li, 'lesson_title': lt})

        # Links
        for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', mh, re.DOTALL|re.IGNORECASE):
            url = m.group(1)
            text = strip_tags(m.group(2))
            dm = re.match(r'https?://([^/]+)', url)
            c_links.append({'url': url, 'text': text, 'domain': dm.group(1) if dm else '', 'course': slug, 'lesson_index': li, 'lesson_title': lt})
        for lnk in els:
            u = lnk.get('url', lnk.get('href','')) if isinstance(lnk, dict) else (lnk if isinstance(lnk, str) else '')
            t = lnk.get('text','') if isinstance(lnk, dict) else ''
            if u:
                dm = re.match(r'https?://([^/]+)', u)
                c_links.append({'url': u, 'text': t, 'domain': dm.group(1) if dm else '', 'course': slug, 'lesson_index': li, 'lesson_title': lt})

    # Dedup
    seen = set()
    di = []
    for img in c_imgs:
        k = (img['url'], str(img['lesson_index']))
        if k not in seen and img['url']:
            seen.add(k)
            di.append(img)
    seen = set()
    dl = []
    for lnk in c_links:
        k = (lnk['url'], str(lnk['lesson_index']))
        if k not in seen and lnk['url']:
            seen.add(k)
            dl.append(lnk)

    image_catalog.extend(di)
    link_catalog.extend(dl)
    code_enrichment.extend(new_code)

    cc_s = (lwc/tl*40) if tl else 0
    avg_tc = (ttc/lwt) if lwt else 0
    td_s = min(avg_tc/3000, 1.0)*30
    tr = ecb + len(new_code) + ei + el
    rr_s = min(tr/(tl*3), 1.0)*15 if tl else 0
    tc3 = tl*3
    si_s = ((vt+vs+vu)/tc3*15) if tc3 else 0
    qs = round(cc_s + td_s + rr_s + si_s, 1)

    all_courses.append({
        'slug': slug, 'title': title, 'file': fname, 'total_lessons': tl,
        'section_count': len(secs), 'lessons_with_content': lwc,
        'content_coverage_pct': round(lwc/tl*100,1) if tl else 0,
        'lessons_with_video': lwv, 'lessons_with_transcript': lwt,
        'transcript_coverage_pct': round(lwt/lwv*100,1) if lwv else 0,
        'total_transcript_chars': ttc, 'avg_transcript_chars': round(avg_tc),
        'modular_text_chars': mtc, 'modular_html_chars': mhc,
        'existing_code_blocks': ecb, 'existing_code_chars': ecc,
        'new_code_blocks_found': len(new_code), 'total_code_blocks': ecb+len(new_code),
        'images_count': len(di), 'links_count': len(dl),
        'youtube_videos': ytc, 'jw_videos': jwc, 'quizzes': qc,
        'quality_scores': {
            'content_coverage': round(cc_s,1), 'transcript_depth': round(td_s,1),
            'resource_richness': round(rr_s,1), 'structural_integrity': round(si_s,1),
            'total': qs
        },
        'valid_titles': vt, 'valid_sections': vs, 'valid_urls': vu,
    })

# Save all data
with open(os.path.join(PROG, '_audit_data.json'), 'w', encoding='utf-8') as f:
    json.dump({
        'all_courses': all_courses,
        'image_catalog': image_catalog,
        'link_catalog': link_catalog,
        'code_enrichment': code_enrichment
    }, f, indent=2, ensure_ascii=False)

# Print summary
for c in sorted(all_courses, key=lambda x: x['quality_scores']['total'], reverse=True):
    print(f"{c['quality_scores']['total']:5.1f} | {c['total_lessons']:3d}L | CC={c['content_coverage_pct']:5.1f}% | TR={c['transcript_coverage_pct']:5.1f}% | CB={c['total_code_blocks']:3d} | IM={c['images_count']:3d} | LK={c['links_count']:3d} | {c['slug']}")

gtl = sum(c['total_lessons'] for c in all_courses)
glwc = sum(c['lessons_with_content'] for c in all_courses)
glwt = sum(c['lessons_with_transcript'] for c in all_courses)
glwv = sum(c['lessons_with_video'] for c in all_courses)
gttc = sum(c['total_transcript_chars'] for c in all_courses)
gecb = sum(c['existing_code_blocks'] for c in all_courses)
gncb = sum(c['new_code_blocks_found'] for c in all_courses)
print(f'\nGLOBAL: {gtl} lessons, {glwc} with content ({glwc/gtl*100:.1f}%), {glwv} with video, {glwt} with transcript')
print(f'Transcript chars: {gttc:,} | Code: existing={gecb} new={gncb}')
print(f'Images: {len(image_catalog)} | Links: {len(link_catalog)}')
print(f'Avg quality: {sum(c["quality_scores"]["total"] for c in all_courses)/len(all_courses):.1f}')
