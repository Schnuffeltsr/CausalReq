# -*- coding: utf-8 -*-
"""RQ2 figure — distinct valid obligations found under fixed per-document budgets.

Only the three evaluated budgets (5, 10, 20) are plotted; the lines connect the
observed points and do not represent additional measurements. Writes a vector PDF
and a 300 dpi PNG into the repository's figures/ directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
})

BUDGETS = [5, 10, 20]
SERIES = [
    {"label": "Model-based ACE", "values": [26, 45, 64], "color": "#245A81",
     "marker": "o", "linestyle": "-"},
    {"label": "Reachability", "values": [23, 41, 64], "color": "#B46737",
     "marker": "s", "linestyle": "--"},
    {"label": "Random", "values": [20, 36, 64], "color": "#557C61",
     "marker": "^", "linestyle": ":"},
]

fig, ax = plt.subplots(figsize=(5.6, 3.35))
for item in SERIES:
    ax.plot(BUDGETS, item["values"], label=item["label"], color=item["color"],
            marker=item["marker"], linestyle=item["linestyle"], linewidth=1.8,
            markersize=6, markeredgecolor="white", markeredgewidth=0.7)

ax.set_xlabel("Candidates reviewed per document")
ax.set_ylabel("Distinct valid obligations found")
ax.set_xticks(BUDGETS)
ax.set_xlim(3.5, 21.5)
ax.set_ylim(15, 70)
ax.set_yticks([20, 30, 40, 50, 60, 70])
ax.grid(axis="y", color="#D9DEE3", linewidth=0.7)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, loc="upper left", ncol=1)
fig.tight_layout()

for suffix in ("pdf", "png"):
    fig.savefig(OUT / f"rq2_review_prioritization.{suffix}",
                bbox_inches="tight", pad_inches=0.08)
plt.close(fig)
print(f"written: {OUT / 'rq2_review_prioritization.pdf'} and .png")
