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
DARK   = "#1a1a1a"

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
# FIG 11 — v0.2.0 phase map (17 phases · 4 new + cross-phase hook)
# ─────────────────────────────────────────────────────────────────────────
def fig_v02_phase_map():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 17); ax.set_ylim(0, 10)
    ax.axis("off")

    phases = [
        ("1",    "read_context",          1.0, SLATE,  False),
        ("1.5",  "context_setup",         2.0, GOLD,   True),     # NEW
        ("2",    "interview",             3.0, SLATE,  False),
        ("3",    "planning_brief",        4.0, SLATE,  False),
        ("4",    "GATE_1 (HITL)",         5.0, RED,    False),
        ("5",    "scaffold",              6.0, SLATE,  False),
        ("6",    "compose_prompts",       7.0, SLATE,  False),
        ("7",    "fetch_library_docs",    8.0, SLATE,  False),
        ("8",    "seed_tracking",         9.0, SLATE,  False),
        ("9",    "emit_audit_sheet",     10.0, SLATE,  False),
        ("10",   "self_audit",           11.0, SLATE,  False),
        ("11",   "reflection",           12.0, SLATE,  False),
        ("11.5", "structural_consist.",  13.0, GOLD,   True),     # NEW
        ("12",   "GATE_2 (HITL)",        14.0, RED,    False),
        ("13",   "handoff",              15.0, GREEN,  False),
        ("13.5", "feedback_session",     16.0, GOLD,   True),     # NEW
        ("13.7", "improvement_audit",    17.0, GOLD,   True),     # NEW
    ]
    # Snake layout: 17 phases in 2 rows of ~9 each
    cols = 9
    cell_w, cell_h = 1.7, 1.6
    x0, y0 = 0.4, 6.4
    coords = []
    for i, (num, name, _idx, color, is_new) in enumerate(phases):
        row = i // cols
        col = i % cols if row == 0 else (cols - 1) - (i % cols)
        x = x0 + col * cell_w
        y = y0 - row * (cell_h + 0.4)
        coords.append((x, y))
        # Highlight ring for NEW
        if is_new:
            ring = FancyBboxPatch((x - 0.05, y - 0.05), cell_w - 0.1 + 0.1, cell_h - 0.05 + 0.1,
                                  boxstyle="round,pad=0.04,rounding_size=0.18",
                                  linewidth=2.5, edgecolor=GOLD, facecolor="none")
            ax.add_patch(ring)
        # Phase tile
        tile = FancyBboxPatch((x, y), cell_w - 0.15, cell_h - 0.15,
                              boxstyle="round,pad=0.03,rounding_size=0.13",
                              linewidth=1.2, edgecolor="#1a1a1a", facecolor=color)
        ax.add_patch(tile)
        ax.text(x + (cell_w - 0.15) / 2, y + cell_h - 0.45, num,
                ha="center", va="center", fontsize=11, fontweight="bold",
                color="white" if color != GOLD else DARK)
        ax.text(x + (cell_w - 0.15) / 2, y + 0.30, name,
                ha="center", va="center", fontsize=8,
                color="white" if color != GOLD else DARK)

    # Snake arrows (very simplified)
    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        ax.annotate("", xy=(x2 + 0.4, y2 + 0.7), xytext=(x1 + 0.4, y1 + 0.7),
                    arrowprops=dict(arrowstyle="-|>", lw=0.9, color="#888", alpha=0.6))

    # Cross-phase adaptive_audit_meta band
    band = FancyBboxPatch((0.4, 1.7), 16.4, 1.0,
                          boxstyle="round,pad=0.05,rounding_size=0.18",
                          linewidth=2, edgecolor=GOLD, facecolor="#fff7d6")
    ax.add_patch(band)
    ax.text(8.6, 2.45, "Cross-phase  ·  adaptive_audit_meta  (v0.2.0)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(8.6, 2.05, "fires at end of every task and every session  ·  n=3..10 dynamic panel  ·  per-scope persona-fit  ·  inherited by child",
            ha="center", va="center", fontsize=9, color=SLATE, style="italic")

    # Legend
    legend_items = [
        ("base v0.1.0 phase",    SLATE),
        ("HITL gate",            RED),
        ("v0.2.0 NEW phase",     GOLD),
        ("STOP / handoff",       GREEN),
    ]
    for i, (label, color) in enumerate(legend_items):
        x = 0.5 + i * 4.2
        sw = FancyBboxPatch((x, 0.5), 0.4, 0.4,
                            boxstyle="round,pad=0.02,rounding_size=0.06",
                            linewidth=1, edgecolor="#1a1a1a", facecolor=color)
        ax.add_patch(sw)
        ax.text(x + 0.55, 0.7, label, va="center", fontsize=9, color=SLATE)

    ax.text(8.6, 9.4, "v0.2.0  ·  17-phase orchestration  +  cross-phase adaptive audit hook",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(8.6, 9.0, "13 base phases preserved verbatim  ·  4 new phases inserted at fixed points  ·  backward-compatible flag available",
            ha="center", fontsize=9, color=SLATE, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/11_v02_phase_map.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 12 — Feedback learning loop (SQLite + MD mirror + per-correction HITL)
# ─────────────────────────────────────────────────────────────────────────
def fig_v02_feedback_loop():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9)
    ax.axis("off")

    # Title
    ax.text(6, 8.5, "Phase 13.5  ·  feedback_learning_loop",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6, 8.1, "capture · classify · per-correction HITL · persist (DB + MD) · trigger improvement at threshold",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # User feedback box (top-left)
    user = FancyBboxPatch((0.4, 6.0), 2.8, 1.5,
                          boxstyle="round,pad=0.05,rounding_size=0.15",
                          linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT)
    ax.add_patch(user)
    ax.text(1.8, 6.95, "USER", ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(1.8, 6.55, "free-text feedback\nat session close",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Auto-classifier box
    cls = FancyBboxPatch((4.2, 6.0), 3.0, 1.5,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.5, edgecolor=TEAL, facecolor="#d6eaef")
    ax.add_patch(cls)
    ax.text(5.7, 6.95, "AUTO-CLASSIFY", ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(5.7, 6.55, "severity × category × recurrence\n+ confidence%",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # HITL box (red)
    hitl = FancyBboxPatch((8.2, 6.0), 3.4, 1.5,
                          boxstyle="round,pad=0.05,rounding_size=0.15",
                          linewidth=2.0, edgecolor=RED, facecolor="#fdebe9")
    ax.add_patch(hitl)
    ax.text(9.9, 7.05, "HITL · per correction", ha="center", fontsize=11, fontweight="bold", color=RED)
    ax.text(9.9, 6.55, "[Y]  promote to queue\n[N]  record only\n[SKIP]  defer",
            ha="center", fontsize=9, color=SLATE, style="italic")

    for x1, x2 in [(3.2, 4.2), (7.2, 8.2)]:
        ax.annotate("", xy=(x2, 6.75), xytext=(x1, 6.75),
                    arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#444"))

    # SQLite (DB) box
    db = FancyBboxPatch((1.5, 3.0), 3.6, 1.8,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=1.5, edgecolor=NAVY, facecolor=NAVY)
    ax.add_patch(db)
    ax.text(3.3, 4.40, "corrections.db", ha="center", color="white",
            fontsize=11, fontweight="bold")
    ax.text(3.3, 4.05, "SQLite + FTS5 (recurrence search)\nauthoritative · parameterised SQL\nlifecycle via status (no deletes)",
            ha="center", color="white", fontsize=8, style="italic")

    # MD mirror box
    md = FancyBboxPatch((6.5, 3.0), 4.4, 1.8,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=1.5, edgecolor=TEAL, facecolor=LIGHT)
    ax.add_patch(md)
    ax.text(8.7, 4.40, "corrections.md  ·  pending_review.md",
            ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(8.7, 4.05, "auto-regenerated each run from DB\nMarkdown table for git-diff visibility\nDB is single source of truth",
            ha="center", fontsize=8, color=SLATE, style="italic")

    # HITL → DB/MD arrows
    ax.annotate("", xy=(3.3, 4.85), xytext=(9.0, 6.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=NAVY,
                                connectionstyle="arc3,rad=-0.2"))
    ax.annotate("", xy=(8.7, 4.85), xytext=(10.5, 6.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=TEAL,
                                connectionstyle="arc3,rad=-0.1"))

    # Threshold check (bottom)
    th = FancyBboxPatch((1.5, 0.7), 9.4, 1.6,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=2.0, edgecolor=GOLD, facecolor="#fff7d6")
    ax.add_patch(th)
    ax.text(6.2, 1.85, "THRESHOLD  ·  count(learn=Y AND status=pending_review) ≥ 15  OR  user types  TRIGGER",
            ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(6.2, 1.40, "→  emit improvement_proposal.md  →  signal phase 13.7  →  5-axis jury + mandatory HITL gate",
            ha="center", fontsize=9, color=SLATE, style="italic")
    ax.text(6.2, 1.00, "no source change merges without explicit human approval",
            ha="center", fontsize=8, color=RED, style="italic")

    # arrow DB → threshold
    ax.annotate("", xy=(6.2, 2.30), xytext=(3.3, 3.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666",
                                connectionstyle="arc3,rad=-0.15"))

    plt.tight_layout()
    plt.savefig(f"{OUT}/12_v02_feedback_loop.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 13 — Adaptive audit meta (3-10 dynamic panel · per-task / per-session)
# ─────────────────────────────────────────────────────────────────────────
def fig_v02_adaptive_meta():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(6, 9.4, "Cross-phase  ·  adaptive_audit_meta",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6, 9.0, "fires at end of every task and every session  ·  in both the generator and the inherited child",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Top-left: scope envelope
    sc = FancyBboxPatch((0.4, 6.5), 3.8, 2.0,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT)
    ax.add_patch(sc)
    ax.text(2.3, 8.15, "SCOPE ENVELOPE", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(2.3, 7.45, "scope_kind (task | session)\nartifacts_in_scope[]\neu_risk · touched_modules\nimportance_signals",
            ha="center", fontsize=8, color=SLATE)

    # Importance score formula (center top)
    fm = FancyBboxPatch((4.6, 6.5), 3.6, 2.0,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=1.5, edgecolor=GOLD, facecolor="#fff7d6")
    ax.add_patch(fm)
    ax.text(6.4, 8.15, "IMPORTANCE SCORE  (0..100)", ha="center",
            fontsize=10, fontweight="bold", color=NAVY)
    ax.text(6.4, 7.50, "30 if eu_risk=high, 15 if limited\n+15 per touched safety module\n+ ceil(artifacts/5)\nclamp [0, 100]",
            ha="center", fontsize=8, color=SLATE)

    # n_auditors box
    nb = FancyBboxPatch((8.6, 6.5), 3.0, 2.0,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=2.0, edgecolor=TEAL, facecolor="#d6eaef")
    ax.add_patch(nb)
    ax.text(10.1, 8.15, "n_auditors  ∈  [3, 10]", ha="center",
            fontsize=11, fontweight="bold", color=TEAL)
    ax.text(10.1, 7.50, "round(importance / 10)\nclamp [3, 10]",
            ha="center", fontsize=8, color=SLATE, style="italic")
    ax.text(10.1, 6.95, "every auditor freshly\ncomposed via prompt-architect\n(persona TAILORED to scope)",
            ha="center", fontsize=8, color=NAVY)

    # Connectors
    ax.annotate("", xy=(4.6, 7.5), xytext=(4.2, 7.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#444"))
    ax.annotate("", xy=(8.6, 7.5), xytext=(8.2, 7.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#444"))

    # 5 example auditors row
    auditors = [
        ("regulatory_archivist",      0.6, NAVY),
        ("calibration_skeptic",       2.7, TEAL),
        ("portability_engineer",      4.8, SLATE),
        ("memory_steward",            6.9, "#5a6b80"),
        ("simulation_designer",       9.0, GREEN),
    ]
    for (lbl, x, color) in auditors:
        b = FancyBboxPatch((x, 4.0), 2.0, 1.4,
                           boxstyle="round,pad=0.04,rounding_size=0.12",
                           linewidth=1.2, edgecolor=color, facecolor=color)
        ax.add_patch(b)
        # split slug at underscore for layout
        words = lbl.split("_")
        line1 = words[0]
        line2 = " ".join(words[1:]) if len(words) > 1 else ""
        ax.text(x + 1.0, 4.95, line1, ha="center", color="white",
                fontsize=9, fontweight="bold")
        ax.text(x + 1.0, 4.55, line2, ha="center", color="white",
                fontsize=8, style="italic")
        ax.text(x + 1.0, 4.20, "+ self KPIs",
                ha="center", color="white", fontsize=7, style="italic")

    # arrows from n_auditors → panel
    for (_, x, _) in auditors:
        ax.annotate("", xy=(x + 1.0, 5.4), xytext=(10.1, 6.5),
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, color="#888", alpha=0.6))

    ax.text(6.0, 5.65, "panel composed (parallel · blind)",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Triage row (errors vs improvements)
    err = FancyBboxPatch((0.6, 1.6), 5.2, 1.8,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.5, edgecolor=RED, facecolor="#fdebe9")
    ax.add_patch(err)
    ax.text(3.2, 3.05, "ERRORS path", ha="center", fontsize=11,
            fontweight="bold", color=RED)
    ax.text(3.2, 2.45, "any auditor conf ≥ 70  →  BLOCKER\n2+ auditors conf 50-69  →  WARNING\nelse  →  WEAK (logged, no action)",
            ha="center", fontsize=8, color=SLATE)
    ax.text(3.2, 1.90, "BLOCKERs pause next task  ·  surface immediately",
            ha="center", fontsize=8, color=RED, style="italic")

    imp = FancyBboxPatch((6.2, 1.6), 5.2, 1.8,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.5, edgecolor=GREEN, facecolor="#e7f4ec")
    ax.add_patch(imp)
    ax.text(8.8, 3.05, "IMPROVEMENTS path", ha="center", fontsize=11,
            fontweight="bold", color=GREEN)
    ax.text(8.8, 2.45, "weighted-mean ≥70 + spread ≤30  →  QUEUE_FOR_HITL\nweighted-mean ≥70 + spread >30  →  DISSENT_HITL_NOW\nelse  →  DEFER",
            ha="center", fontsize=8, color=SLATE)
    ax.text(8.8, 1.90, "queued rows feed phase 13.5  →  human Y/N",
            ha="center", fontsize=8, color=GREEN, style="italic")

    # arrows panel → triage
    ax.annotate("", xy=(3.2, 3.40), xytext=(4.6, 4.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666"))
    ax.annotate("", xy=(8.8, 3.40), xytext=(7.4, 4.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666"))

    # bottom strip
    ax.text(6, 0.7, "persona-fit enforced (generic personas trigger re-composition)  ·  every auditor composed via prompt-architect",
            ha="center", fontsize=9, color=NAVY, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/13_v02_adaptive_meta.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 14 — Improvement jury (fixed 5 axes · confidence-weighted consensus)
# ─────────────────────────────────────────────────────────────────────────
def fig_v02_improvement_jury():
    fig, ax = plt.subplots(figsize=(12, 7.2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(6, 9.45, "Phase 13.7  ·  improvement_jury  ·  fixed 5-axis consensus",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6, 9.05, "audits any improvement_proposal.md emitted by phase 13.5  ·  no source change merges without explicit human approval",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # 5 auditor axes (top row)
    axes = [
        ("regression",        "no AIE-NNN re-introduced",                    0.6,  NAVY),
        ("calibration",       "P2 preserved · no forbidden tokens",          2.85, TEAL),
        ("portability",       "P1 preserved · no platform leakage",          5.10, SLATE),
        ("eu_ai_act_drift",   "mapping coverage not weakened",               7.35, GOLD),
        ("memory_integrity",  "no pollution · index ↔ files coherent",       9.60, GREEN),
    ]
    for (lbl, sub, x, color) in axes:
        b = FancyBboxPatch((x, 5.6), 2.05, 2.1,
                           boxstyle="round,pad=0.05,rounding_size=0.15",
                           linewidth=1.5, edgecolor=color, facecolor=color)
        ax.add_patch(b)
        # darker text for gold
        text_color = "white" if color != GOLD else DARK
        ax.text(x + 1.025, 7.10, lbl, ha="center", color=text_color,
                fontsize=11, fontweight="bold")
        ax.text(x + 1.025, 6.55, sub, ha="center", color=text_color,
                fontsize=7.5, style="italic", wrap=True)
        ax.text(x + 1.025, 6.00, "approve · awc · dissent\nreject · n/a + conf%",
                ha="center", color=text_color, fontsize=7, style="italic")

    # Consensus rule box
    cb = FancyBboxPatch((1.0, 2.7), 10.0, 1.9,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT)
    ax.add_patch(cb)
    ax.text(6, 4.30, "CONFIDENCE-WEIGHTED CONSENSUS  (per row)",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(6, 3.85, "any axis  reject  with conf ≥ 70  →  REJECTED",
            ha="center", fontsize=9, color=SLATE)
    ax.text(6, 3.50, "any axis  dissent  →  DISSENT",
            ha="center", fontsize=9, color=SLATE)
    ax.text(6, 3.15, "≥ 4 axes approve / approve_with_caveat  AND  mean conf ≥ 75  →  APPROVED",
            ha="center", fontsize=9, color=SLATE)
    ax.text(6, 2.80, "otherwise  →  AMBIGUOUS",
            ha="center", fontsize=9, color=SLATE)

    # arrows from each axis → consensus
    for (_, _, x, color) in axes:
        ax.annotate("", xy=(x + 1.025, 4.6), xytext=(x + 1.025, 5.6),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666", alpha=0.7))

    # HITL gate (mandatory)
    hb = FancyBboxPatch((1.0, 0.5), 10.0, 1.7,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=2.5, edgecolor=RED, facecolor="#fdebe9")
    ax.add_patch(hb)
    ax.text(6, 1.85, "HITL GATE  (mandatory  ·  even on APPROVED batch)",
            ha="center", fontsize=11, fontweight="bold", color=RED)
    ax.text(6, 1.45, "[A] approve all   ·   [B] approve subset   ·   [C] reject batch   ·   [D] send back to phase 13.5",
            ha="center", fontsize=9, color=SLATE)
    ax.text(6, 1.05, "no auto-merge  ·  DB statuses updated transactionally on user decision",
            ha="center", fontsize=8.5, color=RED, style="italic")

    # arrow consensus → HITL
    ax.annotate("", xy=(6, 2.2), xytext=(6, 2.7),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color=NAVY))

    plt.tight_layout()
    plt.savefig(f"{OUT}/14_v02_improvement_jury.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 15 — Phase 4.5 memory schema negotiation (v0.3.0)
# ─────────────────────────────────────────────────────────────────────────
def fig_v03_phase45():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(6, 9.4, "Phase 4.5  ·  memory_schema_setup  (v0.3.0)",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6, 9.0, "negotiate per-project memory contract  ·  HITL on every change  ·  inherited by child for living re-negotiation",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Inputs box
    inputs = FancyBboxPatch((0.4, 6.5), 3.2, 2.2,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT)
    ax.add_patch(inputs)
    ax.text(2.0, 8.30, "INPUTS", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(2.0, 7.85, "SPEC.json (post-Gate#1)\ndomain · eu_risk · stack\ngranularity · regulations",
            ha="center", fontsize=8, color=SLATE)
    ax.text(2.0, 7.05, "→ pick per-domain starter",
            ha="center", fontsize=8, color=NAVY, style="italic")

    # 6 starters strip
    starters = [
        ("informatics_dev",     "test_outcomes\ndecision_logs",         0.4),
        ("healthcare_clinical", "patient_cohort\nadverse_events",       2.40),
        ("fintech",             "transactions\nregulatory",             4.40),
        ("legal",               "case_law\nprecedent_chains",           6.40),
        ("public_sector",       "policy_changes\nfeedback",             8.40),
        ("research",            "hypothesis\nexperiment_runs",          10.40),
    ]
    for (slug, mods, x) in starters:
        b = FancyBboxPatch((x, 4.5), 1.45, 1.5,
                           boxstyle="round,pad=0.04,rounding_size=0.12",
                           linewidth=1.1, edgecolor=TEAL, facecolor="#d6eaef")
        ax.add_patch(b)
        ax.text(x + 0.725, 5.65, slug.replace("_", "\n"),
                ha="center", fontsize=8, fontweight="bold", color=NAVY)
        ax.text(x + 0.725, 4.80, mods,
                ha="center", fontsize=6.5, color=SLATE, style="italic")

    ax.text(6, 4.20, "starters preloaded (6) · architect augments per project signals · domain=other → hybrid composition",
            ha="center", fontsize=8.5, color=NAVY, style="italic")

    # arrow inputs → starters
    ax.annotate("", xy=(6, 6.0), xytext=(2.0, 6.4),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666",
                                connectionstyle="arc3,rad=-0.1"))

    # Negotiation box (right)
    neg = FancyBboxPatch((4.0, 6.5), 5.0, 2.2,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=2.0, edgecolor=RED, facecolor="#fdebe9")
    ax.add_patch(neg)
    ax.text(6.5, 8.30, "HITL · negotiation",
            ha="center", fontsize=11, fontweight="bold", color=RED)
    ax.text(6.5, 7.75, "[A] accept all   ·   [B] edit module   ·   [C] add module   ·   [D] skip",
            ha="center", fontsize=9, color=SLATE)
    ax.text(6.5, 7.10, "every keystroke logged in negotiation_session_<id>.md\nbaseline 4-typed Anthropic memory always preserved",
            ha="center", fontsize=8, color=SLATE, style="italic")

    # Output box (bottom)
    out = FancyBboxPatch((1.0, 1.7), 10.0, 2.0,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.5, edgecolor=GREEN, facecolor="#e7f4ec")
    ax.add_patch(out)
    ax.text(6, 3.30, "OUTPUTS  (memory_schema/)", ha="center",
            fontsize=11, fontweight="bold", color=GREEN)
    ax.text(6, 2.85, "manifest.json (authoritative · sha256-tracked)\n"
                     "manifest.md (regenerable mirror · git-diffable)\n"
                     "modules/<name>.json (one per agreed module · field flags + audit rules)\n"
                     "negotiation_session_<id>.md (HITL audit trail · architect's reflection)",
            ha="center", fontsize=8.5, color=SLATE)

    ax.annotate("", xy=(6, 3.7), xytext=(6, 4.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=NAVY))

    # Footer note
    ax.text(6, 0.65, "the contract becomes the audit subject of the MANDATORY memory_completeness_auditor inside prompts/14_adaptive_audit_meta.md",
            ha="center", fontsize=9, color=NAVY, style="italic")
    ax.text(6, 0.30, "child orchestrator inherits the architect; re-negotiation possible at every session boundary (living_update mode)",
            ha="center", fontsize=8, color=SLATE, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/15_v03_phase45.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 16 — 8-format memory taxonomy + selection logic (v0.3.1)
# ─────────────────────────────────────────────────────────────────────────
def fig_v03_format_taxonomy():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13); ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(6.5, 9.45, "v0.3.1  ·  8-format memory taxonomy  ·  always pick the best per module",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(6.5, 9.05, "the architect proposes the recommended format + 2 calibrated alternatives at HITL  ·  no blanket choice",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Tier A row (5 formats)
    tier_a = [
        ("structured_md",  "narrative + fields\ngit-diffable\n≤500 entries",          0.4,  TEAL),
        ("csv",            "tabular\nspreadsheet-friendly\n≤10k rows",                 2.85, TEAL),
        ("json",           "index-style\nrewrite-each-update\n≤1k entries",            5.30, TEAL),
        ("jsonl",          "append-only event log\n>1k entries\nflat schema",          7.75, TEAL),
        ("sqlite",         "FTS5 similarity · joins\ntransactions\nstdlib + CLI",     10.20, NAVY),
    ]
    ax.text(0.4, 7.85, "Tier A  ·  no soft deps",
            fontsize=10, fontweight="bold", color=NAVY)
    for (lbl, sub, x, color) in tier_a:
        b = FancyBboxPatch((x, 6.0), 2.30, 1.6,
                           boxstyle="round,pad=0.05,rounding_size=0.13",
                           linewidth=1.4, edgecolor=color, facecolor=color)
        ax.add_patch(b)
        ax.text(x + 1.15, 7.20, lbl, ha="center", color="white",
                fontsize=10, fontweight="bold")
        ax.text(x + 1.15, 6.40, sub, ha="center", color="white",
                fontsize=7, style="italic")

    # Tier B row (3 formats)
    tier_b = [
        ("parquet",     "columnar analytics\n>100k rows · OLAP\npyarrow / fastparquet",  2.0,  GOLD),
        ("vector_db",   "semantic similarity\nembeddings · RAG\nsqlite-vss / faiss",     5.5,  GOLD),
        ("graph_db",    "high relationship density\nmulti-hop traversal\nkuzu / networkx", 9.0, GOLD),
    ]
    ax.text(0.4, 4.95, "Tier B  ·  soft deps with documented Tier-A fallback",
            fontsize=10, fontweight="bold", color=NAVY)
    for (lbl, sub, x, color) in tier_b:
        b = FancyBboxPatch((x, 3.1), 2.6, 1.6,
                           boxstyle="round,pad=0.05,rounding_size=0.13",
                           linewidth=1.6, edgecolor=color, facecolor=color)
        ax.add_patch(b)
        ax.text(x + 1.3, 4.30, lbl, ha="center", color=DARK,
                fontsize=10, fontweight="bold")
        ax.text(x + 1.3, 3.50, sub, ha="center", color=DARK,
                fontsize=7.5, style="italic")

    # Selection arrows (illustrative)
    sel_box = FancyBboxPatch((0.4, 0.6), 12.2, 1.8,
                             boxstyle="round,pad=0.05,rounding_size=0.15",
                             linewidth=1.5, edgecolor=NAVY, facecolor=LIGHT)
    ax.add_patch(sel_box)
    ax.text(6.5, 2.05, "SELECTION  (deterministic first, calibrated second)",
            ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(6.5, 1.65,
            "audit needs FTS5 similarity → sqlite (or vector_db if semantic)   ·   multi-hop traversal → graph_db (sqlite recursive CTE if ≤2-hop)",
            ha="center", fontsize=8, color=SLATE)
    ax.text(6.5, 1.35,
            ">100k columnar OLAP → parquet   ·   joins ≥2 modules → sqlite   ·   <100 + index lookup → json   ·   ≤500 + human review → structured_md",
            ha="center", fontsize=8, color=SLATE)
    ax.text(6.5, 1.00,
            ">1k append-only flat → jsonl   ·   semantic similarity → vector_db   ·   else → jsonl (safest event log)",
            ha="center", fontsize=8, color=SLATE)

    # Anti-patterns note
    ax.text(6.5, 8.55,
            "anti-patterns refused: vector_db <100 entries · graph_db on flat data · parquet for human-review modules · json single-object >1k entries · all 6 starters same format",
            ha="center", fontsize=8, color=RED, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/16_v03_format_taxonomy.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 17 — Two-tier memory completeness audit (v0.3.0)
# ─────────────────────────────────────────────────────────────────────────
def fig_v03_two_tier_audit():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(6, 8.5, "memory_completeness_auditor  ·  MANDATORY persona inside adaptive_audit_meta",
            ha="center", fontsize=13, fontweight="bold", color=NAVY)
    ax.text(6, 8.1, "added on top of n_auditors (analogous to simulation_agent in phase 11.5)  ·  reads memory_schema/manifest.json as audit contract",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Contract box (top center)
    contract = FancyBboxPatch((4.0, 6.0), 4.0, 1.5,
                              boxstyle="round,pad=0.05,rounding_size=0.15",
                              linewidth=1.5, edgecolor=NAVY, facecolor=NAVY)
    ax.add_patch(contract)
    ax.text(6, 7.10, "memory_schema/manifest.json", ha="center",
            color="white", fontsize=10, fontweight="bold")
    ax.text(6, 6.65, "the contract  ·  what THIS project must remember\nnegotiated at phase 4.5",
            ha="center", color="white", fontsize=8, style="italic")

    # Particular tier (left)
    p = FancyBboxPatch((0.4, 2.5), 5.2, 3.0,
                       boxstyle="round,pad=0.05,rounding_size=0.15",
                       linewidth=1.8, edgecolor=TEAL, facecolor="#d6eaef")
    ax.add_patch(p)
    ax.text(3.0, 5.10, "PARTICULAR audit", ha="center",
            fontsize=11, fontweight="bold", color=TEAL)
    ax.text(3.0, 4.65, "for THIS scope (one task / one session)",
            ha="center", fontsize=8.5, color=SLATE, style="italic")
    ax.text(3.0, 4.20, "• every contracted trigger produced its entry?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(3.0, 3.85, "• mandatory fields populated (incl. mandatory_if_<cond>)?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(3.0, 3.50, "• each entry validates against module schema?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(3.0, 3.00, "example finding:",
            ha="center", fontsize=7.5, color=SLATE, style="italic")
    ax.text(3.0, 2.70,
            "Test #14 attempt 2 status=fail but suggested_solution missing → BLOCKER (conf 92%)",
            ha="center", fontsize=7, color=RED, style="italic")

    # Global tier (right)
    g = FancyBboxPatch((6.4, 2.5), 5.2, 3.0,
                       boxstyle="round,pad=0.05,rounding_size=0.15",
                       linewidth=1.8, edgecolor=GOLD, facecolor="#fff7d6")
    ax.add_patch(g)
    ax.text(9.0, 5.10, "GLOBAL audit", ha="center",
            fontsize=11, fontweight="bold", color=NAVY)
    ax.text(9.0, 4.65, "across all sessions (the project's lifetime)",
            ha="center", fontsize=8.5, color=SLATE, style="italic")
    ax.text(9.0, 4.20, "• missing-thresholds breached on any module?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(9.0, 3.85, "• empty modules across N sessions (drift signal)?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(9.0, 3.50, "• schema-evolution candidates (re-negotiate)?",
            ha="center", fontsize=8, color=SLATE)
    ax.text(9.0, 3.00, "example finding:",
            ha="center", fontsize=7.5, color=SLATE, style="italic")
    ax.text(9.0, 2.70,
            "decision_logs.violation_pct = 8% (threshold 5%) → BLOCKER (conf 88%)",
            ha="center", fontsize=7, color=RED, style="italic")

    # contract → both tiers arrows
    ax.annotate("", xy=(3.0, 5.5), xytext=(5.0, 6.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#666"))
    ax.annotate("", xy=(9.0, 5.5), xytext=(7.0, 6.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#666"))

    # Both → triage box
    tri = FancyBboxPatch((2.0, 0.5), 8.0, 1.5,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.5, edgecolor=GREEN, facecolor="#e7f4ec")
    ax.add_patch(tri)
    ax.text(6, 1.55, "FINDINGS TRIAGE  (same paths as the rest of the panel)",
            ha="center", fontsize=10, fontweight="bold", color=GREEN)
    ax.text(6, 1.10, "errors: BLOCKER (conf ≥70) · WARNING (2+ at 50-69) · WEAK\n"
                     "improvements: QUEUE_FOR_HITL · DISSENT_HITL_NOW · DEFER",
            ha="center", fontsize=8, color=SLATE, style="italic")

    ax.annotate("", xy=(6, 2.0), xytext=(3.0, 2.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666",
                                connectionstyle="arc3,rad=0.15"))
    ax.annotate("", xy=(6, 2.0), xytext=(9.0, 2.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666",
                                connectionstyle="arc3,rad=-0.15"))

    plt.tight_layout()
    plt.savefig(f"{OUT}/17_v03_two_tier_audit.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 18 — External-audit topology + 21-finding closure pipeline (v1.0.0)
# ─────────────────────────────────────────────────────────────────────────
def fig_v10_external_audit():
    fig, ax = plt.subplots(figsize=(13, 7.5))
    ax.set_xlim(0, 13); ax.set_ylim(0, 9.5)
    ax.axis("off")

    ax.text(6.5, 9.0, "v1.0.0  ·  external-audit closure  ·  3 specialist auditors  →  consensus jury  →  21 findings  →  P1/P2/P3 batches",
            ha="center", fontsize=12, fontweight="bold", color=NAVY)
    ax.text(6.5, 8.6, "blind 3-axis panel · independent Opus context windows · jury_consensus_protocol applied · 21/21 closed",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Stage 1: 3 parallel auditors
    auditors = [
        ("Auditor 1\nai_systems_architect",   "orchestration · P4\ndependency graph\ndoc-drift",         0.5,  NAVY),
        ("Auditor 2\nregulatory_compliance",  "EU AI Act · AESIA\nArt.14 HITL\nArt.12 audit-trail",     5.0,  TEAL),
        ("Auditor 3\ncalibration_memory",     "P2 forbidden-tokens\n8-format taxonomy\nfeedback loop",   9.5,  GOLD),
    ]
    for (lbl, sub, x, color) in auditors:
        b = FancyBboxPatch((x, 6.2), 3.0, 1.7,
                           boxstyle="round,pad=0.05,rounding_size=0.13",
                           linewidth=1.5, edgecolor=color, facecolor=color)
        ax.add_patch(b)
        text_color = "white" if color != GOLD else DARK
        ax.text(x + 1.5, 7.50, lbl, ha="center", color=text_color,
                fontsize=10, fontweight="bold")
        ax.text(x + 1.5, 6.65, sub, ha="center", color=text_color,
                fontsize=8, style="italic")

    ax.text(2.0, 5.85, "verdict: APPROVED_WITH_MINOR · 82%",   ha="center", fontsize=8, color=NAVY)
    ax.text(6.5, 5.85, "verdict: APPROVED_WITH_MINOR · 84%",   ha="center", fontsize=8, color=TEAL)
    ax.text(11.0, 5.85, "verdict: APPROVED_WITH_MINOR · 84%",  ha="center", fontsize=8, color=NAVY)

    # Stage 2: jury
    jury = FancyBboxPatch((4.0, 4.0), 5.0, 1.4,
                          boxstyle="round,pad=0.05,rounding_size=0.13",
                          linewidth=2, edgecolor=NAVY, facecolor=NAVY)
    ax.add_patch(jury)
    ax.text(6.5, 4.85, "Consensus Jury",
            ha="center", color="white", fontsize=11, fontweight="bold")
    ax.text(6.5, 4.40, "jury_consensus_protocol · dedup 33→21 · 1 dissent (D1) preserved",
            ha="center", color="white", fontsize=8, style="italic")
    ax.text(6.5, 4.10, "BATCH VERDICT  ·  APPROVED_WITH_MINOR · 83%",
            ha="center", color=GOLD, fontsize=9, fontweight="bold")

    # arrows from auditors to jury
    for (_, _, x, _) in auditors:
        ax.annotate("", xy=(6.5, 5.4), xytext=(x + 1.5, 6.2),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666", alpha=0.7))

    # Stage 3: 3 release batches
    batches = [
        ("P1 → v0.3.2",  "9 items · ≈9h\nJ-001..J-009 + J-018",  GREEN, 0.5,  "#e7f4ec"),
        ("P2 → v0.4.0",  "8 items · ≈12h\nJ-010 (D1) + J-011..J-019", GOLD, 5.0,  "#fff7d6"),
        ("P3 → v1.0.0",  "2 items · ≈4.7h\nJ-020 + J-021 · MATURE", "#5a6b80", 9.5, LIGHT),
    ]
    for (lbl, sub, color, x, bgcolor) in batches:
        b = FancyBboxPatch((x, 1.6), 3.0, 1.6,
                           boxstyle="round,pad=0.05,rounding_size=0.13",
                           linewidth=1.5, edgecolor=color, facecolor=bgcolor)
        ax.add_patch(b)
        ax.text(x + 1.5, 2.75, lbl,
                ha="center", color=color, fontsize=11, fontweight="bold")
        ax.text(x + 1.5, 2.10, sub,
                ha="center", color=NAVY, fontsize=8, style="italic")

    # arrow jury → batches
    for (_, _, _, x, _) in batches:
        rad = 0.15 if x < 5 else (-0.15 if x > 6 else 0)
        ax.annotate("", xy=(x + 1.5, 3.2), xytext=(6.5, 4.0),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#666",
                                    connectionstyle=f"arc3,rad={rad}"))

    # Bottom strip — closure status
    closure = FancyBboxPatch((0.5, 0.4), 12.0, 0.95,
                             boxstyle="round,pad=0.04,rounding_size=0.12",
                             linewidth=1.5, edgecolor=GREEN, facecolor="#e7f4ec")
    ax.add_patch(closure)
    ax.text(6.5, 0.95,
            "21/21 consolidated findings closed  ·  calibrated APPROVED_AS_MATURE re-run probability ≈92%  (range 85–96%)",
            ha="center", color=GREEN, fontsize=9.5, fontweight="bold")
    ax.text(6.5, 0.55,
            "residual ~8% covers heuristic items the panel could not fully verify in their sandbox (e.g., AESIA xlsx contents)",
            ha="center", color=SLATE, fontsize=8, style="italic")

    plt.tight_layout()
    plt.savefig(f"{OUT}/18_v10_external_audit.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# FIG 19 — SHA256 tamper-evident hash-chain (v0.4.0 J-010, ratified at v1.0.0)
# ─────────────────────────────────────────────────────────────────────────
def fig_v10_hash_chain():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 13); ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6.5, 7.5, "INV-LIF-004  ·  tamper-evident sha256 hash-chain  (J-010 · v0.4.0)",
            ha="center", fontsize=13, fontweight="bold", color=NAVY)
    ax.text(6.5, 7.10, "every entry N≥2 in observations.jsonl carries  prior_hash = sha256(entry[N-1])  ·  entry 1 uses literal 'genesis'",
            ha="center", fontsize=9, color=SLATE, style="italic")

    # Top row — clean chain
    ax.text(0.5, 5.95, "CLEAN CHAIN  (audited · T23 PASS)", fontsize=10, fontweight="bold", color=GREEN)
    entries_clean = [
        ("entry 1",       "prior=genesis",              0.7),
        ("entry 2",       "prior=sha256(1)",            3.0),
        ("entry 3",       "prior=sha256(2)",            5.3),
        ("entry 4",       "prior=sha256(3)",            7.6),
        ("entry 5",       "prior=sha256(4)",            9.9),
    ]
    for i, (lbl, prior, x) in enumerate(entries_clean):
        b = FancyBboxPatch((x, 4.3), 2.0, 1.3,
                           boxstyle="round,pad=0.04,rounding_size=0.10",
                           linewidth=1.3, edgecolor=GREEN, facecolor="#e7f4ec")
        ax.add_patch(b)
        ax.text(x + 1.0, 5.10, lbl, ha="center", fontsize=9, fontweight="bold", color=NAVY)
        ax.text(x + 1.0, 4.55, prior, ha="center", fontsize=7, color=SLATE, style="italic")

    # arrows clean
    for i in range(len(entries_clean) - 1):
        x1 = entries_clean[i][2] + 2.0
        x2 = entries_clean[i+1][2]
        ax.annotate("", xy=(x2, 4.95), xytext=(x1, 4.95),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color=GREEN))

    # Verify badge
    ax.text(12.4, 4.95, "✓\nverify\nOK", ha="center", va="center", fontsize=9,
            color=GREEN, fontweight="bold")

    # Bottom row — tampered chain
    ax.text(0.5, 3.05, "TAMPERED CHAIN  (T23 detects break at entry 3)", fontsize=10, fontweight="bold", color=RED)
    entries_tamp = [
        ("entry 1",        "prior=genesis",              0.7,  False),
        ("entry 2",        "prior=sha256(1)",            3.0,  False),
        ("entry 3 ⚠",      "EDITED IN PLACE",            5.3,  True),
        ("entry 4",        "prior=sha256(3) ✗",          7.6,  True),
        ("entry 5",        "prior=sha256(4)",            9.9,  False),
    ]
    for i, (lbl, prior, x, tampered) in enumerate(entries_tamp):
        edge = RED if tampered else GREEN
        face = "#fdebe9" if tampered else "#e7f4ec"
        b = FancyBboxPatch((x, 1.4), 2.0, 1.3,
                           boxstyle="round,pad=0.04,rounding_size=0.10",
                           linewidth=1.5 if tampered else 1.3, edgecolor=edge, facecolor=face)
        ax.add_patch(b)
        text_color = RED if tampered else NAVY
        ax.text(x + 1.0, 2.20, lbl, ha="center", fontsize=9, fontweight="bold", color=text_color)
        ax.text(x + 1.0, 1.65, prior, ha="center", fontsize=7,
                color=RED if tampered else SLATE, style="italic")

    # arrows tampered (red break at 2→3 mismatch)
    for i in range(len(entries_tamp) - 1):
        x1 = entries_tamp[i][2] + 2.0
        x2 = entries_tamp[i+1][2]
        is_break = (i == 1)  # arrow from entry 2 to entry 3 — that's where the break is detected
        ax.annotate("", xy=(x2, 2.05), xytext=(x1, 2.05),
                    arrowprops=dict(arrowstyle="-|>", lw=1.5 if is_break else 1.0,
                                    color=RED if is_break else "#888"))
        if is_break:
            ax.text((x1 + x2) / 2, 2.50, "⚡ BREAK",
                    ha="center", fontsize=8, color=RED, fontweight="bold")

    # Reject badge
    ax.text(12.4, 2.05, "✗\nreject\nFAIL", ha="center", va="center", fontsize=9,
            color=RED, fontweight="bold")

    # Bottom note
    ax.text(6.5, 0.5,
            "T23 deterministic test in tests/run_all.sh builds a synthetic 5-entry chain, verifies it, then injects tamper at n=3 and confirms the chain breaks. Resolves disagreement D1 (Art. 12 audit-trail integrity).",
            ha="center", fontsize=8, color=NAVY, style="italic", wrap=True)

    plt.tight_layout()
    plt.savefig(f"{OUT}/19_v10_hash_chain.png", dpi=300, bbox_inches="tight",
                facecolor="white")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────
# Build all
# ─────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    funcs = [fig_architecture, fig_phases, fig_modules, fig_dataflow,
             fig_hitl, fig_euaiact, fig_memory, fig_errors,
             fig_kpis, fig_auditors,
             fig_v02_phase_map, fig_v02_feedback_loop,
             fig_v02_adaptive_meta, fig_v02_improvement_jury,
             fig_v03_phase45, fig_v03_format_taxonomy,
             fig_v03_two_tier_audit,
             fig_v10_external_audit, fig_v10_hash_chain]
    for f in funcs:
        print(f"  · {f.__name__}")
        f()
    print(f"OK → {OUT}")
