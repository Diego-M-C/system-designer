# 03 · Prompt Factory

> **File.** `prompts/03_prompt_factory.md`
> **Tier.** Complex (~32 tags) — meets the 13-tag mandatory floor.
> **Composed via.** prompt-architect (self-applied).
> **The P4 enforcer.** Without this prompt, P4 is a slogan; with it, every emitted prompt actually passes through the architect.

## 1. Purpose

Composes every emitted prompt for the child system through the co-located `prompt_architect/SKILL.md`, then runs a 14-rubric audit, with up to 3 iteration cycles. If the audit can't pass after 3 iterations, escalates to Gate #2.

This is the only prompt that talks to `prompt_architect/`. Other specialists never invoke the architect directly — they always go through the Factory.

## 2. When invoked

- **Phase.** 6 (`compose_prompts`).
- **Trigger.** Master orchestrator iterates over the role list (from SPEC.json), invoking the Factory once per role.

## 3. Inputs

- `prompt_architect/SKILL.md` — the architect's entry-point.
- `prompt_architect/prompt_editor_skill.json` — 97KB tag taxonomy.
- `prompt_architect/references/*.md` — tag-order, tier-spines, cache-breakpoints, thinking-modes, best-practice-anchors.
- Role spec from master orchestrator: `{role_name, tier, target_path, dependencies}`.
- `references/calibrated_probabilities.md` — for P2 enforcement.
- `references/portable_invocation.md` — for P1 enforcement.

## 4. Outputs

- `<target_path>/prompts/<role>.md` — audited prompt.
- `tracking/sessions/<id>/factory_audit_<role>.md` — audit log per role.
- Signal: composition complete + audit score.

## 5. Tag rationale (~32 tags, Complex floor)

All 13 mandatory Complex tags must be present:

| Tag | Why |
|---|---|
| `<injection_defense>` | Role specs may contain user-controlled strings; treat as data |
| `<alignment_rules>` | P4 dependency declared; downstream prompts inherit |
| `<capability_boundary>` | CAN compose + audit; CANNOT skip architect, modify architect |
| `<test_cases>` | 5 test cases (happy path, audit fail, iteration cap, etc.) |
| `<stop_condition>` | Audit pass OR 3-iteration cap reached |
| `<hitl_conditions>` | Escalate to Gate #2 on persistent audit failure |
| `<tools>` | `prompt_architect()` invocation, `fs.read/write atomic` |
| `<tool_selection>` | Architect always; rerun on fail |
| `<action>` / `<observation>` | ReAct-style discipline |
| `<scratchpad>` | Failed iterations stored for review |
| `<temporal_context>` | Iteration timestamps |
| `<verification>` | Re-read emitted prompt and re-audit |

Plus standard Medium spine. Total: ~32 tags.

## 6. Control flow

```
For each role in <input.roles>:
  iter = 0
  while iter < 3:
    1. Invoke prompt_architect(role_spec) → draft prompt P_iter.
    2. Run 14-rubric audit on P_iter:
       - Coverage of mandatory tags for tier
       - Calibration scan (P2)
       - Portability scan (P1)
       - Capability-boundary present
       - Injection defense present
       - HITL conditions documented
       - Stop conditions clear
       - Tools abstract
       - Test cases ≥3
       - ... (full list in audit checklist)
    3. If pass → write to <target>/prompts/<role>.md atomically; break.
    4. Else → log failure reasons to scratchpad → iter += 1; loop.

  If iter == 3 → escalate to master orchestrator → Gate #2 (with role + audit details).
```

### 14-rubric audit detail

The Factory's audit is **stricter** than the architect's own audit:

| # | Rubric item | Pass criterion |
|---|---|---|
| 1 | Tier-floor tags | All mandatory tags for the declared tier are present |
| 2 | Tag count | ≥10 (Simple) / ≥18 (Medium) / ≥30 (Complex) |
| 3 | Calibration (P2) | No forbidden tokens; estimates carry confidence |
| 4 | Portability (P1) | No proprietary tool names; abstract tools only |
| 5 | Capability boundary | Explicit CAN / CANNOT |
| 6 | Injection defense | Treat external input as data |
| 7 | HITL conditions | Documented gates / escalation triggers |
| 8 | Stop conditions | Termination rules clear |
| 9 | Tools | Abstract names; fallbacks listed |
| 10 | Action / Observation | ReAct-style if any external action taken |
| 11 | Test cases | ≥3 (Simple) / ≥4 (Medium) / ≥5 (Complex) |
| 12 | Atomic-write pattern | If `fs.write` is in tools |
| 13 | Cache-hint | `<cache_hint>` for Complex |
| 14 | Frontmatter | Tier + composed-via declared |

## 7. Calibration anchors (P2)

- Audit results carry confidence: each rubric item passes/fails with confidence 90–99% (deterministic) or lower (LLM-judged).
- Iteration estimates: `~75% chance of passing on iteration 1, ~92% by iteration 3, residual ~8% needs HITL`.
- Escalation rationale always includes calibration of why the prompt won't converge.

## 8. Portability (P1)

- The Factory itself is portable (uses abstract tools).
- Enforces P1 on every prompt it audits.
- `prompt_architect()` invocation is the one platform-specific call — implementations vary per LLM but the contract is stable.

## 9. Error handling & fallbacks

| Failure | Behaviour |
|---|---|
| Architect skill unavailable | Halt + escalate (P4 unenforceable) |
| Architect returns malformed prompt | Iterate (up to 3) |
| Audit infrastructure error | Retry once → escalate |
| Atomic write fails | Cleanup `*.tmp` + retry once |
| Iteration cap reached | Escalate to Gate #2 with all 3 iterations + audit failures attached |

## 10. HITL escalation triggers

- 3-iteration cap → Gate #2.
- Architect skill missing or version mismatch → halt + escalate.
- Persistent calibration leaks even after architect fixes → Gate #2 with note "P2 enforcement may need new rule".

## 11. Dependency edges

**Upstream:** `00_master_orchestrator.md`, `prompt_architect/SKILL.md`.
**Downstream:** All `<target>/prompts/*.md` — every emitted prompt for the child system.

## 12. Test coverage

- T4 prompt-tag floor (this prompt itself is Complex, must satisfy floor).
- T9 prompt-architect linkage (this is the linkage).
- Indirectly: T2 calibration (Factory enforces it).
- Indirectly: T1 portability (Factory enforces it).

## 13. Common failure modes

1. **Architect bypassed for "simple" prompts** — tempting to skip Factory for trivial prompts. P4 says no. The orchestrator MUST go through Factory for every prompt.
2. **14 rubrics softened to 7** — if a future PR drops rubric items "for speed", calibration and portability quality silently degrades. Reviewers must keep all 14.
3. **Iteration cap raised silently** — 3 is the cap. Going to 5 means the Factory tolerates worse drafts. Push back.
4. **Audit log not written** — `tracking/sessions/<id>/factory_audit_<role>.md` is the audit trail. Without it, you can't reproduce why a prompt was accepted.
