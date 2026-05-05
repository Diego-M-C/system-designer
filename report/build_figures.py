"""
Build all figures for the system-designer report.
Pure matplotlib (no network dependencies). Outputs PNG @ 300 DPI.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
from matplotlib.lines import Line2D
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figures"
os.makedirs(OUT, exist_ok=True)

# Palette (cohesive, professional)
NAVY   = "#0e2a47"
TEAL   = "#0a6e7a"
SLATE  = "#3a4a5e"
GOLD   = "#c9a227"
GREEN  = "#2e8b57"
RED    = "#c0392b"
LIGHT  = "#eaf2f8"
GREY   = "#7d8ca0"
WHITE  = "#ffffff"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titleweight": "bold",
})

# ─────────────────────────────────────────────────────────────────────────
# FIG 1 — High-level architecture (layers)
# ─────────────────────────────────────────────────────────────────────────
def fig_architecture():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9.5)
    ax.axis("off")

    layers = [
        ("USER INTENT", 8.4, NAVY, WHITE, "high-level intent · 'build fraud-detection assistant for SEPA'"),
        ("ENTRY  ·  SKILL.md  +  /system-designer", 7.2, TEAL, WHITE,
         "frontmatter triggers · routing · platform detection"),
        ("ORCHESTRATION  ·  00_master_orchestrator.md  (Complex · 46 tags · self-audited)", 6.0, SLATE, WHITE,
         "13-phase state machine · 2 inviolable HITL gates · resumable"),
        ("SPECIALIST AGENTS  ·  01..09  (interview → factory → docs → audit → reports)", 4.8, "#5a6b80", WHITE,
         "single-shot · idempotent · independent · composed via prompt-architect"),
        ("PROMPT ARCHITECT  ·  P4 enforcement (tag taxonomy 97KB · tier spines · cache breakpoints)", 3.6, GOLD, "#1a1a1a",
         "every emitted prompt audited · 14-rubric × ≤3 iterations"),
        ("REFERENCES  +  TEMPLATES  +  WIZARD  +  CHECKLISTS (13 EU AI Act)", 2.4, "#9aa9bd", "#1a1a1a",
         "operational rules + skeletons + interview + regulatory inputs"),
        ("CHILD SYSTEM (deliverable)  ·  CLAUDE.md · SPEC.md · prompts/ · audit/ · tracking/ · docs/", 1.2, GREEN, WHITE,
         "EU AI Act-compliant scaffold · living docs · ≥112 audit rows for high-risk"),
    ]
    for (label, y, fc, tc, sub) in layers:
        box = FancyBboxPatch((0.4, y - 0.4), 11.2, 0.85,
                             boxstyle="round,pad=0.04,rounding_size=0.15",
                             linewidth=1.2, edgecolor="#1a1a1a", facecolor=fc)
        ax.add_patch(box)
        ax.text(6, y + 0.12, label, ha="center", va="center",
                fontsize=11, color=tc, fontweight="bold")
        ax.text(6, y - 0.22, sub, ha="center", va="center",
                fontsize=8, color=tc, style="italic", alpha=0.92)

    # Down arrows between layers
    for y in [7.65, 6.45, 5.25, 4.05, 2.85, 1.65]:
        ax.annotate("", xy=(6, y - 0.25), xytext=(6, y),
                    arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#444"))

    ax.text(6, 9.15, "system-designer · layered architecture",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6, 0.4,
            "P1 Portability · P2 Calibration · P3 On-demand · P4 Prompt-architect · P5 Living docs",
            ha="center", fontsize=9, color=SLATE, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/01_architecture.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 2 — 13-phase orchestration flow
# ─────────────────────────────────────────────────────────────────────────
def fig_phases():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7)
    ax.axis("off")

    phases = [
        ("1\nread\ncontext",     0.6, 5.5, TEAL),
        ("2\ninterview",          1.85, 5.5, TEAL),
        ("3\nplanning\nbrief",    3.1, 5.5, TEAL),
        ("4\nGATE 1\nHITL",       4.35, 5.5, RED),
        ("5\nscaffold",           5.6, 5.5, TEAL),
        ("6\ncompose\nprompts",   6.85, 5.5, TEAL),
        ("7\nfetch\nlib docs",    8.1, 5.5, TEAL),
        ("8\nseed\ntracking",     9.35, 5.5, TEAL),
        ("9\nemit\naudit sheet", 10.6, 5.5, TEAL),
        ("10\nself\naudit",      11.85, 5.5, TEAL),
        ("11\nreflection",       13.1, 5.5, TEAL),
    ]
    bottom = [
        ("12\nGATE 2\nHITL",      11.85, 2.7, RED),
        ("13\nhandoff",           13.1, 2.7, GREEN),
    ]

    def box(label, x, y, fc, w=1.05, h=1.05):
        ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                     boxstyle="round,pad=0.04,rounding_size=0.12",
                     linewidth=1.4, edgecolor="#1a1a1a", facecolor=fc))
        ax.text(x, y, label, ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")

    for (l, x, y, c) in phases: box(l, x, y, c)
    for (l, x, y, c) in bottom: box(l, x, y, c)

    # Top-row arrows
    for i in range(len(phases) - 1):
        x1 = phases[i][1] + 0.55; x2 = phases[i+1][1] - 0.55
        ax.annotate("", xy=(x2, 5.5), xytext=(x1, 5.5),
                    arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#333"))

    # From 11 (reflection) → 12 (Gate 2)
    ax.annotate("", xy=(11.85, 3.3), xytext=(13.1, 4.95),
                arrowprops=dict(arrowstyle="-|>", lw=1.4, color="#333",
                                connectionstyle="arc3,rad=0.25"))
    # 12 → 13
    ax.annotate("", xy=(13.1 - 0.55, 2.7), xytext=(11.85 + 0.55, 2.7),
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#333"))

    # Legend
    ax.text(0.6, 0.9, "■  agent phase", color=TEAL, fontsize=10, fontweight="bold")
    ax.text(3.6, 0.9, "■  HITL gate (inviolable, blocking)", color=RED, fontsize=10, fontweight="bold")
    ax.text(8.5, 0.9, "■  STOP / hand-off to child orchestrator", color=GREEN, fontsize=10, fontweight="bold")

    # Annotations
    ax.text(4.35, 6.8, "blocks\nuntil user\napproves",
            ha="center", fontsize=8, color=RED, style="italic")
    ax.text(11.85, 1.55, "blocks until\napprove + dissents resolved",
            ha="center", fontsize=8, color=RED, style="italic")

    ax.text(7, 6.25, "13-phase orchestration  ·  resumable per current_phase  ·  atomic writes throughout",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/02_phases.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 3 — Module map (memory, task class, error learning, HITL, audit, …)
# ─────────────────────────────────────────────────────────────────────────
def fig_modules():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9)
    ax.axis("off")

    # Center: Master orchestrator
    ax.add_patch(FancyBboxPatch((4.5, 3.85), 3, 1.3,
                 boxstyle="round,pad=0.05,rounding_size=0.2",
                 linewidth=2, edgecolor=NAVY, facecolor=NAVY))
    ax.text(6, 4.7, "Master Orchestrator", ha="center", va="center",
            color="white", fontsize=12, fontweight="bold")
    ax.text(6, 4.25, "13-phase loop · HITL gates", ha="center", va="center",
            color="white", fontsize=8.5, style="italic")

    # Modules around it
    modules = [
        # (label, x, y, color, sub)
        ("Memory module",        1.5, 7.6, "#3498db",
         "4 typed memories\nuser · project · feedback · reference"),
        ("Task classification",   6, 7.6, TEAL,
         "interview wizard\n30 questions · 8 phases · calibrated defaults"),
        ("Error learning",       10.5, 7.6, "#8e44ad",
         "30 AIE preloaded\nauto-extension · per-session catalog"),
        ("HITL gates",           1.5, 4.5, RED,
         "2 inviolable gates\nfit% per option · auto-skip prohibited"),
        ("Audit module",         10.5, 4.5, GOLD,
         "13-sheet xlsx (≥112 rows)\n3-N auditors + jury · dissent → HITL"),
        ("Calibration engine",   1.5, 1.5, "#16a085",
         "P2 — every claim has %\nforbidden tokens scanned"),
        ("Living-docs cadence",   6, 1.5, "#e67e22",
         "tracking/ + audit/ + reports/\nappended every session"),
        ("Library docs fetcher", 10.5, 1.5, "#2980b9",
         "Context7 → primary →\nfallback → gh release API"),
    ]
    for (lbl, x, y, c, sub) in modules:
        ax.add_patch(FancyBboxPatch((x - 1.3, y - 0.65), 2.6, 1.3,
                     boxstyle="round,pad=0.05,rounding_size=0.15",
                     linewidth=1.3, edgecolor="#1a1a1a", facecolor=c))
        ax.text(x, y + 0.3, lbl, ha="center", va="center",
                color="white", fontsize=10, fontweight="bold")
        ax.text(x, y - 0.25, sub, ha="center", va="center",
                color="white", fontsize=7.8, style="italic")
        # connector
        ax.annotate("", xy=(6, 4.5), xytext=(x, y),
                    arrowprops=dict(arrowstyle="-", lw=0.8, color="#888",
                                    alpha=0.55))

    ax.text(6, 8.7, "Module map  ·  every module updates tracking/ on every action (P5)",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/03_modules.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 4 — Data flow (sequence-style)
# ─────────────────────────────────────────────────────────────────────────
def fig_dataflow():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9)
    ax.axis("off")

    actors_x = [1.0, 3.5, 6.0, 8.5, 11.0]
    actors = ["User", "SKILL.md", "Master\nOrchestrator", "Specialists", "Filesystem"]
    colors = [NAVY, TEAL, SLATE, GOLD, GREEN]

    # Lifelines
    for x, name, c in zip(actors_x, actors, colors):
        ax.add_patch(FancyBboxPatch((x - 0.7, 7.8), 1.4, 0.6,
                     boxstyle="round,pad=0.03,rounding_size=0.1",
                     linewidth=1.2, edgecolor="#1a1a1a", facecolor=c))
        ax.text(x, 8.1, name, ha="center", va="center",
                color="white", fontsize=9.5, fontweight="bold")
        ax.plot([x, x], [7.7, 0.5], color=GREY, linestyle="--",
                linewidth=0.8, alpha=0.6)

    def msg(y, x_from, x_to, label, side="up", style="solid", color="#333"):
        arrow_style = "-|>" if style == "solid" else "->"
        lw = 1.4 if style == "solid" else 1.0
        ls = "-" if style == "solid" else ":"
        ax.annotate("", xy=(x_to, y), xytext=(x_from, y),
                    arrowprops=dict(arrowstyle=arrow_style, lw=lw,
                                    linestyle=ls, color=color))
        ax.text((x_from + x_to) / 2, y + 0.13, label,
                ha="center", fontsize=8, color=color, fontweight="bold")

    msg(7.2, 1.0, 3.5, "intent")
    msg(6.7, 3.5, 6.0, "invoke")
    msg(6.2, 6.0, 11.0, "read references/, templates/")
    msg(5.65, 6.0, 8.5, "phase 2 — interview")
    msg(5.15, 8.5, 1.0, "Q i + default + conf%", style="dotted")
    msg(4.65, 1.0, 8.5, "answer", style="dotted")
    msg(4.15, 8.5, 11.0, "atomic write SPEC.json")
    msg(3.65, 6.0, 1.0, "GATE 1 — alts + recommendation", color=RED)
    msg(3.15, 1.0, 6.0, "decision", color=RED, style="dotted")
    msg(2.65, 6.0, 8.5, "phases 5–10 — scaffold, compose, audit")
    msg(2.15, 8.5, 11.0, "child tree + audit + jury")
    msg(1.65, 6.0, 1.0, "GATE 2 — audit summary + dissents", color=RED)
    msg(1.15, 1.0, 6.0, "approve", color=RED, style="dotted")
    msg(0.65, 6.0, 11.0, "write HANDOFF.md → STOP", color=GREEN)

    ax.text(6, 8.75, "End-to-end data flow  ·  HITL gates highlighted in red",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/04_dataflow.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 5 — HITL gate calibration shape
# ─────────────────────────────────────────────────────────────────────────
def fig_hitl():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # Left: gate-decision template
    ax = axes[0]; ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.5, 0.5), 9, 9,
                 boxstyle="round,pad=0.05,rounding_size=0.2",
                 linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT))
    ax.text(5, 9.2, "HITL Gate · standardised template",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)
    lines = [
        ("Calibrated alternatives", "bold"),
        ("[A]  proceed with plan A      fit ~78%", "mono"),
        ("       pros: proven; minimal scope", ""),
        ("       cons: doesn't address X edge case", ""),
        ("[B]  augment with library Y   fit ~14%", "mono"),
        ("[C]  defer to next session    fit  ~8%", "mono"),
        ("[D]  free-form input", "mono"),
        ("[E]  abort", "mono"),
        ("", ""),
        ("Recommendation: A · confidence ~82%", "bold"),
        ("Rationale: minimises rollback risk; …", ""),
        ("", ""),
        ("Auto-skip prohibited (P4 alignment).", "italic"),
    ]
    y = 8.2
    for (txt, st) in lines:
        if st == "bold":
            ax.text(1, y, txt, fontsize=9.5, fontweight="bold", color=NAVY)
        elif st == "mono":
            ax.text(1, y, txt, fontsize=9, fontfamily="monospace", color="#222")
        elif st == "italic":
            ax.text(1, y, txt, fontsize=8.5, style="italic", color=RED)
        else:
            ax.text(1, y, txt, fontsize=8.5, color="#333")
        y -= 0.55

    # Right: distribution of fit% for a sample decision
    ax2 = axes[1]
    options = ["A", "B", "C", "D", "E"]
    fits = [78, 14, 8, 0, 0]
    confs = [82, 70, 65, 0, 0]
    x = np.arange(len(options))
    bars = ax2.bar(x, fits, color=[GREEN, GOLD, GREY, "#cccccc", "#cccccc"],
                   edgecolor="#1a1a1a", linewidth=1)
    ax2.set_xticks(x); ax2.set_xticklabels(options, fontsize=11, fontweight="bold")
    ax2.set_ylabel("fit (%)", fontsize=10)
    ax2.set_ylim(0, 100)
    ax2.set_title("Calibrated alternative fit  ·  sums to 100%",
                  fontsize=11, color=NAVY, fontweight="bold")
    for i, (f, c) in enumerate(zip(fits, confs)):
        if f > 0:
            ax2.text(i, f + 2, f"{f}%\n~{c}% conf", ha="center", fontsize=8.5,
                     color=NAVY, fontweight="bold")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(f"{OUT}/05_hitl.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 6 — EU AI Act mapping (13 checklists ↔ 13 Articles)
# ─────────────────────────────────────────────────────────────────────────
def fig_euaiact():
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 12); ax.set_ylim(0, 14); ax.axis("off")

    rows = [
        ("Risk management",            "Art. 9",     "12+6"),
        ("Risk mgmt. example",         "Art. 9",     " — "),
        ("Data governance",            "Art. 10",    " 14"),
        ("Technical documentation",    "Art. 11",    " 18"),
        ("Record-keeping",             "Art. 12",    "  8"),
        ("Transparency to deployer",   "Art. 13/50", " 10"),
        ("Human oversight",            "Art. 14",    "  8"),
        ("Accuracy",                   "Art. 15",    "  6"),
        ("Robustness",                 "Art. 15",    "  6"),
        ("Cybersecurity",              "Art. 15",    " 10"),
        ("Quality management",         "Art. 17",    " 12"),
        ("Post-market monitoring",     "Art. 72",    " 10"),
        ("Incident reporting",         "Art. 73",    " 10"),
    ]
    # Header
    headers = [("Checklist (Spanish AESIA)", 0.4, 5.4),
               ("EU AI Act Article",          5.6, 8.4),
               ("min rows (high-risk)",       8.6, 11.4)]
    ax.add_patch(Rectangle((0.4, 12.5), 11.0, 0.8, facecolor=NAVY, edgecolor="black"))
    for (lbl, x_l, x_r) in headers:
        ax.text((x_l + x_r) / 2, 12.9, lbl, ha="center", va="center",
                color="white", fontsize=10, fontweight="bold")

    for i, (clist, art, rows_n) in enumerate(rows):
        y = 12.2 - 0.85 - i * 0.78
        bg = LIGHT if i % 2 == 0 else "white"
        ax.add_patch(Rectangle((0.4, y - 0.35), 11.0, 0.78,
                               facecolor=bg, edgecolor="#cccccc", linewidth=0.5))
        ax.text(0.6, y, clist, va="center", fontsize=9.5, color="#222")
        ax.text(7.0, y, art, va="center", fontsize=9.5, color=TEAL,
                fontweight="bold", ha="center")
        ax.text(10.0, y, rows_n, va="center", fontsize=10,
                fontfamily="monospace", color=NAVY, fontweight="bold", ha="center")

    ax.text(6, 13.7, "EU AI Act 2024/1689  ·  high-risk mapping  ·  13 checklists, ≥112 audit rows",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(6, 0.2, "Cross-regulations by domain: GDPR · MDR · DORA · ISO 42001 · ISO 13485",
            ha="center", fontsize=8.5, color=SLATE, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/06_euaiact.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 7 — Memory module
# ─────────────────────────────────────────────────────────────────────────
def fig_memory():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 7); ax.axis("off")

    ax.add_patch(FancyBboxPatch((4.5, 5.5), 3, 1.0,
                 boxstyle="round,pad=0.04,rounding_size=0.15",
                 linewidth=2, edgecolor=NAVY, facecolor=NAVY))
    ax.text(6, 6.1, "MEMORY.md", ha="center", color="white",
            fontsize=11, fontweight="bold")
    ax.text(6, 5.75, "index, ≤200 lines, never truncates",
            ha="center", color="white", fontsize=8, style="italic")

    types = [
        ("user.md", 1.5, 3, "#3498db",
         "role · expertise\npreferences · vocabulary"),
        ("project.md", 4.5, 3, TEAL,
         "facts · constraints\nopen questions · stakeholders"),
        ("feedback.md", 7.5, 3, "#8e44ad",
         "FB-NNN entries\nWhy: + How to apply:"),
        ("reference.md", 10.5, 3, "#e67e22",
         "Linear · Slack\nGrafana · CI/CD pointers"),
    ]
    for (lbl, x, y, c, sub) in types:
        ax.add_patch(FancyBboxPatch((x - 1.3, y - 0.95), 2.6, 1.9,
                     boxstyle="round,pad=0.05,rounding_size=0.15",
                     linewidth=1.3, edgecolor="#1a1a1a", facecolor=c))
        ax.text(x, y + 0.5, lbl, ha="center", color="white",
                fontsize=10.5, fontweight="bold")
        ax.text(x, y - 0.2, sub, ha="center", color="white",
                fontsize=8.5, style="italic")
        ax.annotate("", xy=(x, y + 1), xytext=(6, 5.45),
                    arrowprops=dict(arrowstyle="-", lw=0.9, color="#888"))

    # Below: process
    ax.text(6, 1.4, "Read at session start  ·  update at AUDIT_ROW_APPEND  ·  pruned by orchestrator",
            ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(6, 0.75, "When user explicitly asks: save immediately. When user asks to forget: remove. Verify before recommending.",
            ha="center", fontsize=8.5, color=SLATE, style="italic")
    ax.text(6, 6.55, "Memory module  ·  4 typed files indexed by MEMORY.md",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/07_memory.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 8 — Error learning per session (AIE catalog growth)
# ─────────────────────────────────────────────────────────────────────────
def fig_errors():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    # Left: catalog growth simulation
    sessions = np.arange(0, 21)
    base = 30
    growth = base + np.array([0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11])
    ax = axes[0]
    ax.fill_between(sessions, base, growth, alpha=0.3, color=TEAL,
                    label="auto-extension (post-bootstrap)")
    ax.fill_between(sessions, 0, base, alpha=0.5, color=NAVY,
                    label="preloaded (30 AIE-NNN)")
    ax.plot(sessions, growth, color=NAVY, linewidth=2)
    ax.set_xlabel("session", fontsize=10)
    ax.set_ylabel("entries in errors_catalog.json", fontsize=10)
    ax.set_title("AIE catalog · seeded + auto-extended",
                 fontsize=11, fontweight="bold", color=NAVY)
    ax.legend(loc="lower right", fontsize=8.5)
    ax.grid(linestyle="--", alpha=0.4)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    # Right: category breakdown of seed (30 entries)
    ax2 = axes[1]
    cats = ["hallucination", "concurrency", "security", "logic",
            "reliability", "prompt_eng."]
    counts = [6, 4, 6, 5, 5, 4]
    colors = [TEAL, "#3498db", RED, "#8e44ad", "#16a085", GOLD]
    ax2.barh(cats, counts, color=colors, edgecolor="#1a1a1a", linewidth=1)
    for i, c in enumerate(counts):
        ax2.text(c + 0.1, i, str(c), va="center", fontsize=10,
                 color=NAVY, fontweight="bold")
    ax2.set_xlim(0, 8)
    ax2.set_xlabel("# preloaded patterns (30 total)", fontsize=10)
    ax2.set_title("Distribution by category",
                  fontsize=11, fontweight="bold", color=NAVY)
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)
    ax2.grid(axis="x", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(f"{OUT}/08_errors.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 9 — KPI dashboard preview
# ─────────────────────────────────────────────────────────────────────────
def fig_kpis():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")

    kpis = [
        ("duration\nestim.", "240 min", "~70%", NAVY),
        ("duration\nactual",  "198 min", "—",    "#444"),
        ("errors",            "3",       "—",    RED),
        ("HITL\ndecisions",   "2",       "—",    GOLD),
        ("tests\ncreated",    "14",      "—",    GREEN),
        ("coverage\n+",       "32%",     "~80%", GREEN),
        ("files\nmodified",   "47",      "—",    "#444"),
        ("tokens\n(est.)",    "180k–240k","~75%", "#8e44ad"),
        ("rollbacks",         "0",       "—",    GREEN),
        ("tech-debt\nadded",  "low",     "~65%", GOLD),
        ("EU AI Act\nscore",  "96%",     "~88%", GREEN),
        ("agent\nself-conf",  "78%",     "—",    TEAL),
    ]
    cols = 6; w = 1.7; h = 1.7
    for i, (lbl, val, conf, c) in enumerate(kpis):
        col = i % cols; row = i // cols
        x = 0.6 + col * 1.85; y = 4.0 - row * 2.1
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                     boxstyle="round,pad=0.04,rounding_size=0.12",
                     linewidth=1.2, edgecolor=c, facecolor="white"))
        ax.add_patch(Rectangle((x, y + h - 0.12), w, 0.12, facecolor=c,
                               edgecolor=c))
        ax.text(x + w/2, y + h/2 + 0.1, val, ha="center", va="center",
                fontsize=14, fontweight="bold", color=NAVY)
        ax.text(x + w/2, y + h/2 - 0.35, lbl, ha="center", va="center",
                fontsize=8, color=SLATE)
        ax.text(x + w/2, y + 0.15, f"conf {conf}", ha="center", va="center",
                fontsize=7, color=GREY, style="italic")

    ax.text(6, 5.7, "Per-session KPIs (11)  ·  every value carries calibration when applicable",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/09_kpis.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# FIG 10 — Auditor + jury topology
# ─────────────────────────────────────────────────────────────────────────
def fig_auditors():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 7); ax.axis("off")

    # Audit sheet at top
    ax.add_patch(FancyBboxPatch((4, 5.3), 4, 1,
                 boxstyle="round,pad=0.05,rounding_size=0.15",
                 linewidth=1.5, edgecolor=NAVY, facecolor=GOLD))
    ax.text(6, 5.85, "audit_sheet.xlsx", ha="center", fontsize=11,
            fontweight="bold", color="#1a1a1a")
    ax.text(6, 5.5, "≥112 rows · 14 sheets · read-only", ha="center", fontsize=8,
            color="#1a1a1a", style="italic")

    # 3 auditors
    auditors = [
        ("Auditor 1", 2.0, 3.4, TEAL,    "persona: risk_sme\nArt. 9 focus"),
        ("Auditor 2", 6.0, 3.4, "#8e44ad","persona: ml_lead\nArt. 15a/b focus"),
        ("Auditor 3", 10.0, 3.4, "#16a085","persona: security_lead\nArt. 15c focus"),
    ]
    for (lbl, x, y, c, sub) in auditors:
        ax.add_patch(FancyBboxPatch((x - 1.1, y - 0.6), 2.2, 1.2,
                     boxstyle="round,pad=0.04,rounding_size=0.12",
                     linewidth=1.3, edgecolor="#1a1a1a", facecolor=c))
        ax.text(x, y + 0.25, lbl, ha="center", color="white",
                fontsize=10.5, fontweight="bold")
        ax.text(x, y - 0.25, sub, ha="center", color="white",
                fontsize=8, style="italic")
        # arrows in
        ax.annotate("", xy=(x, y + 0.7), xytext=(6, 5.25),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666"))

    # Wall between auditors
    for x in [3.7, 7.7]:
        ax.plot([x, x], [2.4, 4.4], color=RED, linestyle="--",
                linewidth=1.2, alpha=0.6)
    ax.text(3.7, 4.6, "blind", ha="center", fontsize=8, color=RED, style="italic")
    ax.text(7.7, 4.6, "blind", ha="center", fontsize=8, color=RED, style="italic")

    # Jury at bottom
    ax.add_patch(FancyBboxPatch((4, 0.9), 4, 1.1,
                 boxstyle="round,pad=0.05,rounding_size=0.15",
                 linewidth=1.5, edgecolor=NAVY, facecolor=NAVY))
    ax.text(6, 1.55, "Meta-Jury", ha="center", color="white",
            fontsize=11, fontweight="bold")
    ax.text(6, 1.15, "agreement matrix · dissent flag · HITL escalation",
            ha="center", color="white", fontsize=8, style="italic")

    for (lbl, x, y, c, sub) in auditors:
        ax.annotate("", xy=(6, 2.05), xytext=(x, y - 0.6),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666"))

    ax.text(6, 6.55, "3+ independent auditors  →  meta-jury  →  HITL on dissent",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    plt.savefig(f"{OUT}/10_auditors.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()

# ─────────────────────────────────────────────────────────────────────────
# Build all
# ─────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    funcs = [fig_architecture, fig_phases, fig_modules, fig_dataflow,
             fig_hitl, fig_euaiact, fig_memory, fig_errors,
             fig_kpis, fig_auditors]
    for f in funcs:
        print(f"  · {f.__name__}")
        f()
    print(f"OK → {OUT}")
