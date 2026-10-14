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

report = "".join(lines)
out_md = root / "RESULTS.md"
out_md.write_text(report, encoding="utf-8")
print(f"written: {out_md} ({len(report)} chars)")
print(report[:2500])
