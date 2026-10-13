# -*- coding: utf-8 -*-
"""Corrected RQ3 contribution analysis.

For Full we reviewed every nomination. For the four ablations the CSV contains
only the nominations that are semantically NEW relative to Full; the rest are
inherited, so their human verdict and obligation ID come from the Full row of the
matched nomination (w_map.json). This script recomputes each variant's valid set
under that rule and reports what is lost or gained.
"""
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


rq3 = read_csv(human / "RQ3_human_review.csv")
mapping = json.loads((root / "review" / "w_map.json").read_text(encoding="utf-8"))

full_rows = {r["提名ID"]: r for r in rq3 if r["版本"] == "Full"}
new_rows = defaultdict(dict)
for r in rq3:
    if r["版本"] != "Full":
        new_rows[r["版本"]][r["提名ID"]] = r

# inherit: variant nomination -> matched Full nomination (threshold 0.70)
inherit = defaultdict(dict)
for key, info in mapping.items():
    variant, nid = key.split("|", 1)
    inherit[variant][nid] = info["matched_full"] if info["score"] >= 0.70 else None

VARIANTS = ["Full", "NoSignedPropagation", "NoIsolatedReview",
            "NoOperationReview", "NoFullDocumentValidation"]

summary = {}
totals = {}
lines = ["# RQ3 人工判定下的组件贡献（含继承关系）\n",
         f"\nFull 的 {len(full_rows)} 条逐条人工审阅；四个消融版只对新增/消失条目单独审阅，"
         "其余条目继承其对 Full 匹配项的判定。\n",
         "\n| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |\n",
         "|---|---:|---:|---:|---|---|---|\n"]

for variant in VARIANTS:
    noms = json.loads((root / "RQ3" / variant / "nominations.json").read_text(encoding="utf-8"))
    total = len(noms)
    valid_ids = set()
    outcomes = Counter()
    for nom in noms:
        nid = nom["nomination_id"]
        if variant == "Full":
            row = full_rows.get(nid)
        else:
            row = new_rows[variant].get(nid)
            if row is None:
                matched = inherit[variant].get(nid)
                row = full_rows.get(matched) if matched else None
        if row is None:
            outcomes["未审阅"] += 1
            continue
        outcomes[row["人工去向"]] += 1
        if row["义务ID"]:
            valid_ids.add(row["义务ID"])
    summary[variant] = valid_ids
    totals[variant] = total
    print(f"{variant:26s} total={total:3d} valid={len(valid_ids)} "
          f"ids={sorted(valid_ids)} outcomes={dict(outcomes)}")

for variant in VARIANTS[1:]:
    lost = sorted(summary["Full"] - summary[variant])
    gained = sorted(summary[variant] - summary["Full"])
    lines.append(f"| {variant} | {totals[variant]} | {len(new_rows[variant])} | {len(summary[variant])} "
                 f"| {', '.join(sorted(summary[variant])) or '—'} "
                 f"| {', '.join(lost) or '—'} | {', '.join(gained) or '—'} |\n")
    print(f"  {variant:26s} lost={lost} gained={gained}")

# ---- did the enlarged route compensate for the removed one? ----------------
full_noms = json.loads((root / "RQ3" / "Full" / "nominations.json").read_text(encoding="utf-8"))
full_origins = Counter(n["origin"] for n in full_noms)

comp_lines = ["\n## 消融时的“补位”检查\n"]
for variant, removed, enlarged in (("NoOperationReview", "operation", "isolated"),
                                   ("NoIsolatedReview", "isolated", "operation"),
                                   ("NoSignedPropagation", None, None),
                                   ("NoFullDocumentValidation", None, None)):
    noms = json.loads((root / "RQ3" / variant / "nominations.json").read_text(encoding="utf-8"))
    origins = Counter(n["origin"] for n in noms)
    valid = sorted(summary.get(variant, set()))
    lost = sorted(summary["Full"] - summary.get(variant, set()))
    gained = sorted(summary.get(variant, set()) - summary["Full"])
    if removed:
        dist = Counter()
        for nom in noms:
            if nom["origin"] != enlarged:
                continue
            matched = inherit[variant].get(nom["nomination_id"])
            if matched and matched.startswith("OPERATION"):
                dist["与 Full 的 operation 提名对齐"] += 1
            elif matched and matched.startswith("ISOLATED"):
                dist["与 Full 的 isolated 提名对齐"] += 1
            elif matched:
                dist["与 Full 的依赖提名对齐"] += 1
            else:
                dist["真正的新条目"] += 1
        comp_lines.append(
            f"\n- **{variant}**（{removed} 路线关闭，{enlarged} 由 "
            f"{full_origins.get(enlarged, 0)} 增至 {origins.get(enlarged, 0)}）："
            f"这 {origins.get(enlarged, 0)} 条 {enlarged} 提名的对齐情况为 "
            + "、".join(f"{k} {v} 条" for k, v in dist.most_common())
            + f"；人工判定下该版本有效义务 {len(valid)} 条"
              f"（失去 {len(lost)} 条{('：' + ', '.join(lost)) if lost else ''}，"
              f"新增 {len(gained)} 条{('：' + ', '.join(gained)) if gained else ''}）。\n")
    else:
        comp_lines.append(
            f"\n- **{variant}**：有效义务 {len(valid)} 条"
            f"（失去 {len(lost)} 条{('：' + ', '.join(lost)) if lost else ''}，"
            f"新增 {len(gained)} 条{('：' + ', '.join(gained)) if gained else ''}）。\n")

report = human / "RQ3_COMPONENT_CONTRIBUTION.md"
report.write_text("".join(lines) + "".join(comp_lines), encoding="utf-8")
print(f"\nwritten: {report}")
