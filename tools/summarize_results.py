# -*- coding: utf-8 -*-
"""Summarise a finished CausalReq run into a readable Markdown report.

Usage: python summarize_results.py <out_root> [doc_id]
"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"

root = OUT_ROOT / DOC_ID
if not root.exists():
    raise SystemExit(f"missing run directory: {root}")

lines = [f"# CausalReq 单文档运行结果 — {DOC_ID}\n"]
summary_path = root / "stage1_summary.json"
stage1 = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {}

lines.append("\n## 1. 抽取与图结构\n")
if stage1:
    lines.append("\n| 项 | 值 |\n|---|---:|\n")
    for key, label in [
        ("source_fr_count", "源 FR 块数"),
        ("element_count", "抽取元素数"),
        ("elements_with_active_meaning", "有 active_meaning 的元素"),
        ("evidence_relation_count", "抽出关系数"),
        ("evidence_nodes", "证据图节点"),
        ("evidence_edges", "证据图边"),
        ("simulation_nodes", "模拟图节点"),
        ("simulation_edges", "模拟图边"),
        ("exclusions", "被排除关系"),
        ("fixed_pool_count", "RQ2 固定候选池"),
        ("llm_calls", "LLM 调用次数"),
        ("minutes", "阶段耗时(分钟)"),
        ("model_version", "模型版本号"),
    ]:
        if key in stage1:
            lines.append(f"| {label} | {stage1[key]} |\n")

pool_path = root / "RQ2" / "fixed_pool.json"
if pool_path.exists():
    pool = json.loads(pool_path.read_text(encoding="utf-8"))
    lines.append(f"\n## 2. RQ2 固定候选池与 ACE 排序（{len(pool)} 条）\n")
    lines.append("\n| 排名 | 候选 | 源元素 | 目标元素 | ACE | p(do=1) | p(do=0) | 可达性 |\n")
    lines.append("|---:|---|---|---|---:|---:|---:|---:|\n")
    for rank, item in enumerate(sorted(pool, key=lambda x: -abs(x["ace"])), 1):
        lines.append(
            f"| {rank} | {item['candidate_id']} | {item['source']} | {item['target']} "
            f"| {item['ace']:+.4f} | {item['p_do_1']:.4f} | {item['p_do_0']:.4f} "
            f"| {item['reachability']} |\n")

    lines.append("\n## 3. 三种排序下的前 5 / 前 10 名（RQ2 预算视角）\n")
    for name in ("ACE", "Reachability", "Random"):
        csv_path = root / "RQ2" / f"{name}_review.csv"
        if not csv_path.exists():
            continue
        import csv as _csv
        with csv_path.open(encoding="utf-8-sig") as handle:
            rows = list(_csv.DictReader(handle))
        lines.append(f"\n**{name}** 前 10：")
        lines.append(", ".join(
            f"{r['candidate_id']}({float(r['ace']):+.3f})" for r in rows[:10]))
        lines.append("\n")

rq3 = root / "RQ3"
if rq3.exists():
    lines.append("\n## 4. RQ3 五变体结果\n")
    lines.append("\n| 变体 | 提名数 | dependency | isolated | operation | 补充需求数 | 初步去向分布 |\n")
    lines.append("|---|---:|---:|---:|---:|---:|---|\n")
    for variant_dir in sorted(p for p in rq3.iterdir() if p.is_dir()):
        nom_path = variant_dir / "nominations.json"
        sup_path = variant_dir / "supplements.json"
        if not nom_path.exists():
            continue
        nominations = json.loads(nom_path.read_text(encoding="utf-8"))
        supplements = json.loads(sup_path.read_text(encoding="utf-8")) if sup_path.exists() else []
        origins = Counter(n["origin"] for n in nominations)
        outcomes = Counter(n.get("preliminary_outcome", "?") for n in nominations)
        lines.append(
            f"| {variant_dir.name} | {len(nominations)} | {origins.get('dependency', 0)} "
            f"| {origins.get('isolated', 0)} | {origins.get('operation', 0)} "
            f"| {len(supplements)} | "
            + ", ".join(f"{k}={v}" for k, v in outcomes.most_common()) + " |\n")

    full = rq3 / "Full"
    if full.exists():
        nominations = json.loads((full / "nominations.json").read_text(encoding="utf-8"))
        retained = [n for n in nominations if n.get("preliminary_outcome") == "retained"]
        lines.append(f"\n## 5. Full 变体中被初步保留的补充需求（{len(retained)} 条）\n")
        for index, item in enumerate(retained, 1):
            lines.append(
                f"\n{index}. **[{(item.get('origin') or '').upper()}] "
                f"{item.get('subject', '')}**\n"
                f"   - 审查问题：{item.get('question', '')}\n"
                f"   - 初步理由：{item.get('preliminary_reason', '')}\n"
                f"   - 补充需求：{item.get('supplement', '')}\n"
                f"   - 证据 FR：{', '.join(item.get('evidence_fr_ids', []))}\n")

        lines.append("\n## 6. Full 变体全部提名的初步去向明细\n")
        lines.append("\n| 提名 | 来源 | 主题 | 去向 | 检查 FR 数 |\n|---|---|---|---|---:|\n")
        for item in nominations:
            lines.append(
                f"| {item['nomination_id']} | {item['origin']} | "
                f"{(item.get('subject') or '')[:60]} | "
                f"{item.get('preliminary_outcome', '?')} | "
                f"{len(item.get('checked_fr_ids', []))} |\n")

# ---------------------------------------------------- human review ----
hr = root / "human_review"
if hr.is_dir():
    import csv as _csv

    rq2p = hr / "RQ2_human_review.csv"
    if rq2p.exists():
        with rq2p.open(encoding="utf-8-sig") as handle:
            rq2 = list(_csv.DictReader(handle))
        dep_yes = sum(1 for r in rq2 if r["依赖有据"] == "是")
        mis_yes = sum(1 for r in rq2 if r["缺失义务成立"] == "是")
        valid_ids = sorted({r["人工义务ID"] for r in rq2 if r["人工义务ID"]})
        lines.append("\n## 7. 人工判定：RQ2 固定候选池\n")
        lines.append(f"\n- 候选数 **{len(rq2)}**；依赖有原文依据 **{dep_yes}/{len(rq2)}**；"
                     f"缺失义务成立 **{mis_yes}/{len(rq2)}**\n")
        lines.append(f"- 人工义务 ID：**{', '.join(valid_ids) if valid_ids else '无'}**\n")
        lines.append("\n| 候选ID | 依赖有据 | 缺失义务成立 | 人工义务ID | 依据／否决原因 |\n")
        lines.append("|---|---|---|---|---|\n")
        for r in rq2:
            lines.append(f"| {r['候选ID']} | {r['依赖有据']} | {r['缺失义务成立']} | "
                         f"{r['人工义务ID']} | {r['依据／否决原因']} |\n")

    rq3p = hr / "RQ3_human_review.csv"
    if rq3p.exists():
        with rq3p.open(encoding="utf-8-sig") as handle:
            rq3 = list(_csv.DictReader(handle))
        by_variant = Counter(r["版本"] for r in rq3)
        outcomes = Counter(r["人工去向"] for r in rq3)
        lines.append("\n## 8. 人工判定：RQ3 提名去向\n")
        lines.append(f"\n- 审阅行数 **{len(rq3)}**（"
                     + "，".join(f"{k} {v}" for k, v in sorted(by_variant.items())) + "）\n")
        lines.append("\n| 人工去向 | 行数 |\n|---|---:|\n")
        for key, value in outcomes.most_common():
            lines.append(f"| {key} | {value} |\n")
        valid_rows = [r for r in rq3 if r["义务ID"]]
        ids = sorted({r["义务ID"] for r in valid_rows})
        lines.append(f"\n- 有效且缺失 **{len(valid_rows)}** 行，对应 **{len(ids)}** 个义务 ID："
                     f"{', '.join(ids) if ids else '无'}\n")
        lines.append("\n| 义务ID | 版本 | 提名ID | 路线 | 原文依据 | 理由 |\n|---|---|---|---|---|---|\n")
        for r in valid_rows:
            lines.append(f"| {r['义务ID']} | {r['版本']} | {r['提名ID']} | {r['路线']} | "
                         f"{r['原文依据']} | {r['理由']} |\n")

    for name, title in (("RQ2_HUMAN_BUDGET.md", "9. RQ2 预算对比（人工判定）"),
                        ("RQ3_COMPONENT_CONTRIBUTION.md", "10. RQ3 组件贡献（人工判定）")):
        p = hr / name
        if p.exists():
            lines.append(f"\n---\n\n## {title}\n\n")
            body_lines = []
            for ln in p.read_text(encoding="utf-8").splitlines():
                if ln.startswith("# "):
                    continue          # drop the report's own H1
                if ln.startswith("## "):
                    ln = "#" + ln      # demote H2 -> H3 so numbering stays inside this section
                body_lines.append(ln)
            lines.append("\n".join(body_lines).strip() + "\n")

report = "".join(lines)
out_md = root / "RESULTS.md"
out_md.write_text(report, encoding="utf-8")
print(f"written: {out_md} ({len(report)} chars)")
print(report[:2500])
