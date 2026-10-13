# -*- coding: utf-8 -*-
"""Merge the Full review and the ablation-diff review into RQ3_human_review.csv."""
import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "Inventory_MIRC3"

human = OUT_ROOT / DOC_ID / "human_review"
header = ["版本", "提名ID", "路线", "模型初步去向", "人工去向", "义务ID", "原文依据", "理由"]

rows = []
for name in ("RQ3_human_review_full.csv", "RQ3_human_review_diff.csv"):
    path = human / name
    if not path.exists():
        print(f"  (missing: {name})")
        continue
    with path.open(encoding="utf-8-sig") as handle:
        part = list(csv.DictReader(handle))
    print(f"  {name}: {len(part)} rows")
    for r in part:
        rows.append([r.get(c, "") for c in header])

out = human / "RQ3_human_review.csv"
with out.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(header)
    writer.writerows(rows)
print(f"merged -> {out} ({len(rows)} data rows)")

from collections import Counter  # noqa: E402
print("  by 版本:", dict(Counter(r[0] for r in rows)))
print("  by 人工去向:", dict(Counter(r[4] for r in rows)))
print("  obligation IDs:", sorted({r[5] for r in rows if r[5]}))
missing_id = [r[1] for r in rows if r[4] == "有效且缺失" and not r[5]]
print("  有效且缺失 without ID:", missing_id)
