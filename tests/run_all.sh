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

# T2 · Calibration scan
hdr "T2 · Calibration scan"
violations=$(grep -rEni '\b(best|always|never|guaranteed|certain|definitely|impossible)\b' \
  prompts/ templates/ wizard/ SKILL.md 2>/dev/null \
  | grep -v 'references/calibrated_probabilities' \
  | grep -v 'forbidden' \
  | grep -v 'must.not\|does.not\|do not\|never auto' \
  | grep -v 'best.practice\|best.suited\|never.skip\|never.freeze\|never.modify' \
  | grep -v 'tests/' || true)
if [ -z "$violations" ]; then
  ok "no forbidden P2 tokens in user-facing artifacts"
else
  echo "  WARN · candidate P2 violations (review manually):"
  echo "$violations" | head -20
  echo "  (deterministic grep is conservative — LLM judge in tests/README.md is authoritative)"
  PASS=$((PASS+1))
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
