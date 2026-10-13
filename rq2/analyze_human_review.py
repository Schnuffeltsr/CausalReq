# -*- coding: utf-8 -*-
"""Derive the RQ2 budget comparison and the RQ3 component contribution from the
human-review CSVs, and write a short summary next to them."""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"
root = OUT_ROOT / DOC_ID
human = root / "human_review"


def read_csv(path):
    with path.open(encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


rq2 = read_csv(human / "RQ2_human_review.csv")
rq3 = read_csv(human / "RQ3_human_review.csv")

# ------------------------------------------------ RQ2 budget comparison ----
verdict = {r["候选ID"]: r for r in rq2}
valid_ids = {r["候选ID"]: r["人工义务ID"] for r in rq2 if r["缺失义务成立"] == "是"}
lines = ["# RQ2 人工判定下的预算对比（MDOT simple2）\n",
         "\n只把人工确认为“缺失义务成立”的候选计入；同一义务 ID 只计一次。\n",
         f"\n- 20 条候选中人工确认有效：{len(valid_ids)} 条 "
         f"（{', '.join(f'{k}→{v}' for k, v in valid_ids.items()) or '无'}）\n",
         f"- 依赖有原文依据：{sum(1 for r in rq2 if r['依赖有据'] == '是')}/20\n",
         f"- 已覆盖：{sum(1 for r in rq2 if r['缺失义务成立'] == '否')}/20；"
         f"待澄清：{sum(1 for r in rq2 if r['缺失义务成立'] == '待澄清')}/20\n"]
lines.append("\n| 预算 | ACE 排序 | 可达性排序 | 随机排序 |\n|---:|---:|---:|---:|\n")

budget_rows = []
for budget in (5, 10, 20):
    counts = {}
    for name in ("ACE", "Reachability", "Random"):
        rows = read_csv(root / "RQ2" / f"{name}_review.csv")
        seen = set()
        for row in rows[:budget]:
            cid = row["candidate_id"]
            if cid in valid_ids and valid_ids[cid]:
                seen.add(valid_ids[cid])
        counts[name] = len(seen)
    budget_rows.append((budget, counts))
    lines.append(f"| {budget} | {counts['ACE']} | {counts['Reachability']} | {counts['Random']} |\n")

print("RQ2 human-valid budget table (distinct obligations):")
for budget, counts in budget_rows:
    print(f"  budget {budget:2d}: ACE={counts['ACE']} reach={counts['Reachability']} random={counts['Random']}")

# position of the valid candidate in each ranking
for name in ("ACE", "Reachability", "Random"):
    rows = read_csv(root / "RQ2" / f"{name}_review.csv")
    pos = {row["candidate_id"]: int(row["rank"]) for row in rows}
    print(f"  rank of valid candidates under {name}: "
          f"{ {cid: pos[cid] for cid in valid_ids} }")

# ------------------------------------------------ RQ3 contribution --------
# (own file: analyze_component_contribution.py, which handles inheritance)

# ------------------------------------------------------------- write ------
report = human / "RQ2_HUMAN_BUDGET.md"
report.write_text("".join(lines), encoding="utf-8")
print(f"\nwritten: {report}")

