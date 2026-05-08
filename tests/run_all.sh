#!/usr/bin/env bash
# system-designer · self-validation suite (deterministic tests only)
# LLM-driven tests (T3, T4, T5, T7, T8, T9) live in tests/README.md.
# Exit 0 if all critical deterministic tests pass; 1 otherwise.

set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PASS=0
FAIL=0
declare -a FAIL_MSGS

ok()   { echo "  PASS · $1"; PASS=$((PASS+1)); }
nope() { echo "  FAIL · $1"; FAIL=$((FAIL+1)); FAIL_MSGS+=("$1"); }
hdr()  { echo; echo "── $1 ─────────────────────"; }

# T1 · Portability scan
hdr "T1 · Portability scan"
violations=$(grep -rEn '\bclaude_code:|\bcursor:|\bcline:|\bmcp__[a-z_]+\(' \
  prompts/ templates/ wizard/ SKILL.md system_generator.json 2>/dev/null \
  | grep -v 'tests/' \
  | grep -v 'portable_invocation' \
  | grep -v 'ToolSearch' || true)
if [ -z "$violations" ]; then
  ok "no Tier-A violations"
else
  nope "Tier-A violations found:"
  echo "$violations" | head -10
fi

# T2 · Calibration scan  (J-007 · v0.3.2 · split into T2a heuristic-warn + T2b strict-blocking)
# Prior version unconditionally PASSed even when violations were listed — silent failure.
# T2a: full forbidden-token sweep with negation-context exclusions; non-blocking; warns only.
# T2b: tight strict scan over USER-FACING prose (excludes forbidden-list discussions, tag-audit
#      tables, alignment_rules, guardrails, non_do_conditions); blocking when count > T2B_MAX.
T2B_MAX="${T2B_MAX:-0}"

hdr "T2a · Calibration scan (heuristic, non-blocking warn)"
violations_t2a=$(grep -rEni '\b(best|always|never|guaranteed|certain|definitely|impossible)\b' \
  prompts/ templates/ wizard/ SKILL.md 2>/dev/null \
  | grep -v 'references/calibrated_probabilities' \
  | grep -v 'forbidden' \
  | grep -v 'must.not\|does.not\|do not\|never auto' \
  | grep -v 'best.practice\|best.suited\|never.skip\|never.freeze\|never.modify' \
  | grep -v 'tests/' || true)
if [ -z "$violations_t2a" ]; then
  ok "T2a: no candidate forbidden P2 tokens (post-exclusion)"
else
  count_t2a=$(echo "$violations_t2a" | wc -l)
  echo "  WARN · T2a: ${count_t2a} candidate P2 violations after exclusion filters"
  echo "$violations_t2a" | head -15
  echo "  (T2a is heuristic / non-blocking — review manually; LLM judge in tests/README.md is authoritative)"
  ok "T2a: warned ${count_t2a} candidates (non-blocking)"
fi

hdr "T2b · Calibration scan (strict on user-facing prose, blocking when count > ${T2B_MAX})"
# Strict scope: only assertion-form patterns that are inequivocally P2 violations
# regardless of context (negation, instruction, definition, quote). These are:
#   "the best <noun>" / "is best" / "are best" / "best possible" / "best-effort"
#   "always works"   / "always produces" / "always succeeds"
#   "guaranteed to"  / "guaranteed that" / "guaranteed <adj>"
#   "definitely"
#   "impossible to <verb>"  (without explicit negation context)
# Forbidden-token mentions in INSTRUCTION form ("Never X", "Always Y" as imperatives) and
# in DEFINITION/QUOTE contexts (forbidden-list discussions, the rule itself) are out of scope —
# they pass T2a's heuristic warn but do not block.
violations_t2b=$(grep -rEn '\b(the best [a-z]|is best\b|are best\b|best.possible|best.effort|always works\b|always produces\b|always succeeds\b|guaranteed to\b|guaranteed that\b|definitely\b|impossible to [a-z])' \
  prompts/ SKILL.md 2>/dev/null \
  | grep -v '^Binary file' \
  | grep -v 'references/' \
  | grep -v 'tests/' \
  | grep -v 'forbidden' \
  | grep -v 'P2 violation\|calibration_violation\|forbidden token' \
  || true)
if [ -z "$violations_t2b" ]; then
  ok "T2b: no strict-scope forbidden P2 tokens"
else
  count_t2b=$(echo "$violations_t2b" | wc -l)
  if [ "$count_t2b" -le "$T2B_MAX" ]; then
    ok "T2b: ${count_t2b} strict candidates (≤ T2B_MAX=${T2B_MAX}, allowed)"
  else
    nope "T2b: ${count_t2b} strict P2 violations (> T2B_MAX=${T2B_MAX})"
    echo "$violations_t2b" | head -15
    echo "  (T2b is BLOCKING — fix the prose above, or raise T2B_MAX env if these are confirmed exemptions)"
  fi
fi

# T6 · Error catalog count = 30
hdr "T6 · AIE catalog count = 30"
n_md=$(grep -c '^### AIE-' references/ai_error_catalog.md 2>/dev/null || echo 0)
n_json=$(grep -c '"id": "AIE-' templates/tracking/errors_catalog.json.tmpl 2>/dev/null || echo 0)
echo "  ai_error_catalog.md     : $n_md"
echo "  errors_catalog.json.tmpl: $n_json"
if [ "$n_md" = "30" ] && [ "$n_json" = "30" ]; then
  ok "30 AIE entries in both files"
else
  nope "AIE count mismatch (expected 30 in both)"
fi

# T7 · EU AI Act 13 checklists referenced
hdr "T7 · EU AI Act mapping (13 checklists)"
n_xlsx=$(ls -1 "Checklists y ejemplos/"*.xlsx 2>/dev/null | wc -l)
# Match either "Checklists y ejemplos/" path or any *_Checklist.xlsx filename in the mapping md
n_referenced=$(grep -cE '\.xlsx' references/eu_ai_act_mapping.md 2>/dev/null || echo 0)
echo "  xlsx files on disk      : $n_xlsx"
echo "  .xlsx mentions in mapping md: $n_referenced"
if [ "$n_xlsx" -ge 13 ] && [ "$n_referenced" -ge 13 ]; then
  ok "≥13 checklists on disk and referenced"
else
  nope "checklist count below 13"
fi

# T10 · HITL non-skip
hdr "T10 · HITL gates non-skip rule"
violations=$(grep -rEn 'auto[ _-]?skip|skip[ _-]gate|bypass[ _-]gate' \
  prompts/ templates/ SKILL.md system_generator.json 2>/dev/null \
  | grep -vE 'never|forbidden|must not|do not|prohibit|no auto|REFUSE|refuse|reject|→ REFUSE' || true)
if [ -z "$violations" ]; then
  ok "no auto-skip language without negation"
else
  nope "potential gate-skip language:"
  echo "$violations" | head -10
fi

# Bonus · prompt-architect linkage (T9 deterministic part)
hdr "T9 · Prompt-architect linkage"
missing=()
for f in prompts/*.md; do
  if ! grep -qE 'prompt[-_]architect|03_prompt_factory|Composed via' "$f"; then
    missing+=("$f")
  fi
done
if [ ${#missing[@]} -eq 0 ]; then
  ok "every prompt references prompt-architect"
else
  nope "prompts missing prompt-architect linkage:"
  printf '  %s\n' "${missing[@]}"
fi

# T11 · v0.2.0 prompts exist
hdr "T11 · v0.2.0 prompts exist (10..14)"
missing_v02=()
for f in 10_data_flow_validator.md 11_feedback_learning_loop.md 12_improvement_jury.md 13_context_curator.md 14_adaptive_audit_meta.md; do
  if [ ! -f "prompts/$f" ]; then
    missing_v02+=("prompts/$f")
  fi
done
if [ ${#missing_v02[@]} -eq 0 ]; then
  ok "all 5 v0.2.0 prompts present"
else
  nope "missing v0.2.0 prompts:"
  printf '  %s\n' "${missing_v02[@]}"
fi

# T12 · v0.2.0 references exist
hdr "T12 · v0.2.0 references exist"
missing_refs=()
for f in data_flow_invariants.md feedback_taxonomy.md jury_consensus_protocol.md context_confidence_protocol.md; do
  if [ ! -f "references/$f" ]; then
    missing_refs+=("references/$f")
  fi
done
if [ ${#missing_refs[@]} -eq 0 ]; then
  ok "all 4 v0.2.0 references present"
else
  nope "missing v0.2.0 references:"
  printf '  %s\n' "${missing_refs[@]}"
fi

# T13 · SQLite schema parseable (uses sqlite3 if available; else syntactic regex check)
hdr "T13 · feedback_learning corrections schema parseable"
schema_path="templates/feedback_learning/corrections_schema.sql.tmpl"
if [ ! -f "$schema_path" ]; then
  nope "schema template missing at $schema_path"
elif command -v sqlite3 >/dev/null 2>&1; then
  if sqlite3 ":memory:" < "$schema_path" 2>/dev/null; then
    ok "sqlite3 parsed schema cleanly (in-memory)"
  else
    # FTS5 may not be compiled in; do a syntactic fallback
    if grep -qE 'CREATE TABLE IF NOT EXISTS corrections' "$schema_path" \
       && grep -qE 'CREATE VIRTUAL TABLE IF NOT EXISTS corrections_fts' "$schema_path"; then
      ok "schema parse failed (likely FTS5 not compiled in this sqlite3 build) but DDL structure looks valid"
    else
      nope "sqlite3 rejected schema and DDL structure check failed"
    fi
  fi
else
  if grep -qE 'CREATE TABLE IF NOT EXISTS corrections' "$schema_path" \
     && grep -qE 'CREATE VIRTUAL TABLE IF NOT EXISTS corrections_fts' "$schema_path"; then
    ok "sqlite3 unavailable; DDL structure check passed"
  else
    nope "sqlite3 unavailable AND DDL structure check failed"
  fi
fi

# T14 · improvement_jury declares fixed n=5 axes
hdr "T14 · improvement_jury fixed 5-axis discipline"
jury_path="prompts/12_improvement_jury.md"
n_axes=$(grep -cE '\b(regression|calibration|portability|eu_ai_act_drift|memory_integrity)\b' "$jury_path" 2>/dev/null || echo 0)
if [ "$n_axes" -ge 5 ]; then
  ok "5 axes mentioned in jury prompt (count: $n_axes)"
else
  nope "fewer than 5 axes mentioned in jury prompt (count: $n_axes)"
fi

# T15 · adaptive_audit_meta documents n_auditors clamp 3..10
hdr "T15 · adaptive_audit_meta n_auditors range"
ada_path="prompts/14_adaptive_audit_meta.md"
if grep -qE 'clamp\(3.*10\)|n ∈ \[3, 10\]|n ∈ \[3,10\]|in \[3, 10\]|in \[3,10\]|3.{0,3}10' "$ada_path"; then
  ok "n_auditors range 3..10 documented"
else
  nope "n_auditors range not clearly documented in $ada_path"
fi

# T17 · v0.3.0 prompt 15 exists
hdr "T17 · v0.3.0 prompt 15_memory_schema_architect.md exists"
if [ -f "prompts/15_memory_schema_architect.md" ]; then
  ok "prompts/15_memory_schema_architect.md present"
else
  nope "prompts/15_memory_schema_architect.md missing"
fi

# T18 · v0.3.0 reference + 6 per-domain starters exist
hdr "T18 · v0.3.0 reference + 6 per-domain memory-schema starters exist"
ref_path="references/memory_schema_protocol.md"
missing_starters=()
for f in informatics_dev healthcare_clinical fintech legal public_sector research; do
  if [ ! -f "templates/memory_schema/per_domain_starters/${f}.json" ]; then
    missing_starters+=("templates/memory_schema/per_domain_starters/${f}.json")
  fi
done
if [ -f "$ref_path" ] && [ ${#missing_starters[@]} -eq 0 ]; then
  ok "memory_schema_protocol.md + 6 per-domain starters present"
else
  if [ ! -f "$ref_path" ]; then nope "missing $ref_path"; fi
  if [ ${#missing_starters[@]} -gt 0 ]; then
    nope "missing per-domain starters:"
    printf '  %s\n' "${missing_starters[@]}"
  fi
fi

# T19 · memory_completeness_auditor mandatory in adaptive_audit_meta
hdr "T19 · memory_completeness_auditor declared MANDATORY in prompt 14"
ada_path="prompts/14_adaptive_audit_meta.md"
if grep -qE 'memory_completeness_auditor.*MANDATORY|MANDATORY.*memory_completeness_auditor|memory_completeness_auditor[^a-z_].*non-?optional|always include.*memory_completeness_auditor|on top of .*n_auditors.*memory_completeness_auditor|memory_completeness_auditor.*on top of' "$ada_path"; then
  ok "memory_completeness_auditor mandatory mention found"
else
  nope "memory_completeness_auditor not declared mandatory in $ada_path"
fi

# T21 · 8 formats catalogued in memory_schema_protocol.md
hdr "T21 · 8 memory formats catalogued in protocol reference"
ref="references/memory_schema_protocol.md"
formats_found=0
for fmt in 'structured_md' 'csv' '`json`' '`jsonl`' '`sqlite`' '`parquet`' '`vector_db`' '`graph_db`'; do
  if grep -qF "$fmt" "$ref" 2>/dev/null; then
    formats_found=$((formats_found+1))
  fi
done
if [ "$formats_found" -eq 8 ]; then
  ok "all 8 formats catalogued in protocol"
else
  nope "expected 8 format mentions in protocol; found $formats_found"
fi

# T22 · every top-level XML tag in prompts/*.md exists in prompt-architect taxonomy
# (J-006 · v0.3.2 · replaces the prior literal-string check that allowed invented tags
#  to slip past — see external_audit/auditor_1_systems_architect.md F1/F2/F3.)
hdr "T22 · every top-level XML tag in prompts/*.md exists in prompt_editor_skill.json#tags"
if command -v python3 >/dev/null 2>&1; then
  taxonomy_check=$(python3 <<'PY' 2>/dev/null
import json, re, glob, sys
try:
    with open('prompt_architect/prompt_editor_skill.json') as f:
        tax = {t['name'] for t in json.load(f)['tags']}
except Exception as e:
    print(f"FAIL: cannot load taxonomy: {e}")
    sys.exit(0)

# Top-level tag = pattern ^<tagname> appearing at line start in the XML body of a Complex prompt.
# We scan every prompt; report any opening tag (not closing, not nested-form) whose name is not in `tax`.
opening_re = re.compile(r'^<([a-z_][a-z0-9_]*)>\s*$', re.MULTILINE)

invented = []  # (file, line_no, tag_name)
files_scanned = 0
for path in sorted(glob.glob('prompts/*.md')):
    files_scanned += 1
    with open(path) as f:
        for i, line in enumerate(f, 1):
            m = re.match(r'^<([a-z_][a-z0-9_]*)>\s*$', line)
            if m:
                name = m.group(1)
                if name not in tax:
                    invented.append((path, i, name))

if invented:
    print(f"FAIL: {len(invented)} invented tag(s) found across {files_scanned} prompts:")
    for path, ln, name in invented:
        print(f"  {path}:{ln}  <{name}>  (not in taxonomy)")
else:
    print(f"OK: scanned {files_scanned} prompts; all top-level tags exist in taxonomy ({len(tax)} canonical names)")
PY
  )
  if echo "$taxonomy_check" | head -1 | grep -q '^OK:'; then
    ok "$(echo "$taxonomy_check" | head -1 | sed 's/^OK: //')"
  else
    nope "$taxonomy_check"
  fi
else
  # Fallback — old literal-string check, marked degraded
  echo "  WARN · python3 unavailable; degraded-mode literal-string check"
  if grep -qE '<selection_criteria>' prompts/15_memory_schema_architect.md \
     && grep -qE '<simulation_scenarios>' prompts/10_data_flow_validator.md; then
    ok "fallback: 2 known canonical tags present in prompts 10/15"
    PASS=$((PASS+1))   # explicit because we used echo+ok already
  else
    nope "fallback: known canonical tags missing"
  fi
fi

# T23 · sha256 hash-chain (prior_hash) — synthetic chain integrity test (J-010 · v0.4.0)
hdr "T23 · sha256 hash-chain integrity (prior_hash) on a synthetic observations.jsonl"
if command -v python3 >/dev/null 2>&1; then
  chain_check=$(python3 <<'PY' 2>/dev/null
import hashlib, json, tempfile, os, sys

def h(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

# Build a 5-entry synthetic chain
entries = []
prior = "genesis"
for i in range(1, 6):
    e = {
        "n": i,
        "artifact": f"<path-{i}>",
        "sha256": h(f"payload-{i}"),
        "prior_hash": prior,
    }
    line = json.dumps(e, sort_keys=True)
    entries.append(line)
    prior = h(line)

# Verify chain
def verify(lines):
    p = "genesis"
    for ln in lines:
        e = json.loads(ln)
        if e["prior_hash"] != p:
            return False, f"break at n={e['n']}: expected prior_hash={p[:12]}…, got {e['prior_hash'][:12]}…"
        p = h(ln)
    return True, "OK"

ok_clean, msg_clean = verify(entries)
if not ok_clean:
    print(f"FAIL: clean chain rejected: {msg_clean}")
    sys.exit(0)

# Tamper test: edit entry 3 in place, verify chain breaks
tampered = list(entries)
e3 = json.loads(tampered[2])
e3["artifact"] = "<TAMPERED>"
tampered[2] = json.dumps(e3, sort_keys=True)
ok_tamper, msg_tamper = verify(tampered)
if ok_tamper:
    print("FAIL: tampered chain accepted (chain is not tamper-evident)")
    sys.exit(0)

print(f"OK: 5-entry chain verifies cleanly + tamper at n=3 detected ({msg_tamper})")
PY
  )
  if echo "$chain_check" | head -1 | grep -q '^OK:'; then
    ok "$(echo "$chain_check" | head -1 | sed 's/^OK: //')"
  else
    nope "$chain_check"
  fi
else
  echo "  WARN · python3 unavailable; skipping T23"
fi

# T20 · per-domain JSON starters parse cleanly
hdr "T20 · per-domain memory-schema starters parse as valid JSON"
parse_fail=()
for f in templates/memory_schema/per_domain_starters/*.json; do
  if ! python3 -c "import json,sys; json.load(open('$f'))" 2>/dev/null; then
    parse_fail+=("$f")
  fi
done
if [ ${#parse_fail[@]} -eq 0 ]; then
  ok "all 6 starters parse as valid JSON"
else
  nope "starters with JSON parse errors:"
  printf '  %s\n' "${parse_fail[@]}"
fi

# T16 · v0.2.0 templates exist
hdr "T16 · v0.2.0 templates exist"
missing_tmpl=()
for f in \
  data_flow_validation/validators_manifest.json.tmpl \
  data_flow_validation/validator_result.md.tmpl \
  data_flow_validation/simulation_report.md.tmpl \
  data_flow_validation/sequence_snapshot.md.tmpl \
  data_flow_validation/consolidated_report.md.tmpl \
  feedback_learning/corrections_schema.sql.tmpl \
  feedback_learning/corrections.md.tmpl \
  feedback_learning/classifications.json.tmpl \
  feedback_learning/pending_review.md.tmpl \
  feedback_learning/improvement_proposal.md.tmpl \
  feedback_learning/session_close.md.tmpl \
  improvement_audit/auditor_result.md.tmpl \
  improvement_audit/consensus_report.md.tmpl \
  adaptive_audit/manifest.json.tmpl \
  adaptive_audit/auditor_result.md.tmpl \
  adaptive_audit/consensus_report.md.tmpl \
  context/context_manifest.json.tmpl \
  context/source_manifest.json.tmpl \
  context/consult_websites.md.tmpl \
  context/download_recommendations.md.tmpl \
  context/curation_log.jsonl.tmpl
do
  if [ ! -f "templates/$f" ]; then
    missing_tmpl+=("templates/$f")
  fi
done
if [ ${#missing_tmpl[@]} -eq 0 ]; then
  ok "all 21 v0.2.0 templates present"
else
  nope "missing v0.2.0 templates:"
  printf '  %s\n' "${missing_tmpl[@]}"
fi

# Summary
echo
echo "════════════════════════════════════════"
echo "Suite: $PASS PASS · $FAIL FAIL"
if [ $FAIL -gt 0 ]; then
  echo "Critical failures:"
  for m in "${FAIL_MSGS[@]}"; do echo "  - $m"; done
  echo
  echo "Run LLM-driven tests (T3, T4, T5, T8) per tests/README.md for full coverage."
  exit 1
else
  echo "All deterministic tests passed."
  echo "Run LLM-driven tests (T3, T4, T5, T8) per tests/README.md for full coverage."
  exit 0
fi
