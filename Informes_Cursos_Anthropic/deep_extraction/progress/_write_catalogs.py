#!/usr/bin/env python3
import json, os

PROG = "/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic/deep_extraction/progress"

with open(os.path.join(PROG, "_audit_data.json"), 'r', encoding='utf-8') as f:
    data = json.load(f)

# Write code enrichment
with open(os.path.join(PROG, "code_enrichment.json"), 'w', encoding='utf-8') as f:
    json.dump({
        "audit_version": "3.0",
        "generated_at": "2026-04-10",
        "total_new_code_blocks": len(data["code_enrichment"]),
        "note": "Code blocks found via re-parsing HTML that were not in the original code_blocks arrays",
        "code_blocks": data["code_enrichment"]
    }, f, indent=2, ensure_ascii=False)
print(f"code_enrichment.json: {len(data['code_enrichment'])} blocks")

# Write image catalog
with open(os.path.join(PROG, "image_catalog.json"), 'w', encoding='utf-8') as f:
    json.dump({
        "audit_version": "3.0",
        "generated_at": "2026-04-10",
        "total_images": len(data["image_catalog"]),
        "images": data["image_catalog"]
    }, f, indent=2, ensure_ascii=False)
print(f"image_catalog.json: {len(data['image_catalog'])} images")

# Write link catalog
with open(os.path.join(PROG, "link_catalog.json"), 'w', encoding='utf-8') as f:
    # Compute domain stats
    domains = {}
    for l in data["link_catalog"]:
        d = l.get("domain", "")
        domains[d] = domains.get(d, 0) + 1
    domain_stats = [{"domain": d, "count": c} for d, c in sorted(domains.items(), key=lambda x: -x[1])]

    json.dump({
        "audit_version": "3.0",
        "generated_at": "2026-04-10",
        "total_links": len(data["link_catalog"]),
        "domain_distribution": domain_stats,
        "links": data["link_catalog"]
    }, f, indent=2, ensure_ascii=False)
print(f"link_catalog.json: {len(data['link_catalog'])} links")

# Print domain stats
print("\nDomain distribution:")
for ds in domain_stats[:15]:
    print(f"  {ds['count']:3d} | {ds['domain']}")
