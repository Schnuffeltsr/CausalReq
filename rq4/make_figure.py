# -*- coding: utf-8 -*-
"""RQ4 figure — evidence chain of the MDOT-Simple2 recipient-configuration case.

Boxes follow the run records printed by `trace_case.py`:

    FR-REP-002  ->  OPERATION-bfe2c70a5486  ->  document-wide validation
                ->  retained supplement  ->  human assessment (O-06 / FR-066)

with the contrasting, already-covered dependency-route nomination (DEP-014) drawn as a
separate branch of the validation decision. No ACE value appears: the case comes from
operation-coverage review, not from intervention-effect ranking.

Writes a vector PDF and a 300 dpi PNG into the repository's figures/ directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
})

EDGE = "#34495A"
COLORS = {"source": "#EAF2F8", "nomination": "#EEF6EE", "validation": "#F3F0FA",
          "output": "#FFF4E8", "assessment": "#EAF2F8", "covered": "#F1F3F5"}

fig, ax = plt.subplots(figsize=(9.4, 3.35))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def add_box(x, y, w, h, text, fill, fontsize=8):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.008,rounding_size=0.018",
        facecolor=fill, edgecolor=EDGE, linewidth=1.0, transform=ax.transAxes))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, linespacing=1.35, color="#202A33",
            transform=ax.transAxes)


def add_arrow(start, end):
    ax.annotate("", xy=end, xytext=start, xycoords=ax.transAxes,
                textcoords=ax.transAxes,
                arrowprops={"arrowstyle": "-|>", "color": EDGE, "lw": 1.25,
                            "mutation_scale": 11, "shrinkA": 2, "shrinkB": 2})


y, h = 0.57, 0.28
boxes = [
    (0.02, 0.16, "Source requirement\nFR-REP-002\nScheduled report\nemail delivery",
     COLORS["source"]),
    (0.22, 0.17, "Operation-coverage\nnomination\nRecipient configuration\nquestion",
     COLORS["nomination"]),
    (0.43, 0.18, "Document-wide\nvalidation\nAll 8 original FRs\nchecked",
     COLORS["validation"]),
    (0.65, 0.16, "Supplementary FR\nSpecify and update\nscheduled-report\nrecipients",
     COLORS["output"]),
    (0.835, 0.16, "Human assessment\nValid\nO-06 / FR-066", COLORS["assessment"]),
]
for x, w, text, color in boxes:
    add_box(x, y, w, h, text, color,
            fontsize=7.5 if color is COLORS["assessment"] else 8)
for left, right in zip(boxes[:-1], boxes[1:]):
    add_arrow((left[0] + left[1] + 0.009, y + h / 2), (right[0] - 0.009, y + h / 2))

ax.text(0.305, 0.50, "OPERATION-bfe2c70a5486", ha="center", va="top",
        fontsize=7.2, color="#52616B", transform=ax.transAxes)

add_box(0.395, 0.115, 0.25, 0.155,
        "Separate nomination: DEP-014\nDelivery to designated recipients\n\u2192 Covered",
        COLORS["covered"], fontsize=7.2)
add_arrow((0.52, y - 0.01), (0.52, 0.28))
ax.text(0.655, 0.1925, "No equivalent recipient-\nconfiguration obligation found",
        ha="left", va="center", fontsize=7.2, color="#52616B", transform=ax.transAxes)

for suffix in ("pdf", "png"):
    fig.savefig(OUT / f"rq4_traceable_completion.{suffix}",
                bbox_inches="tight", pad_inches=0.08)
plt.close(fig)
print(f"written: {OUT / 'rq4_traceable_completion.pdf'} and .png")
