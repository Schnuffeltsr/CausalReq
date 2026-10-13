# -*- coding: utf-8 -*-
"""Final integrity check of the saved human-review deliverables."""
import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
TARGETS = [
    ("MDOT", BASE / "samples" / "MDOT_MDOT_simple2"),
    ("Inventory", BASE / "samples" / "Inventory_MIRC3"),
    ("WebStore", BASE / "samples" / "WebStore_MIRC3"),
]

for label, root in TARGETS:
    print(f"=== {label}  ({root})")
    s1 = root / "stage1_summary.json"
    if s1.exists():
        d = json.loads(s1.read_text(encoding="utf-8"))
        print(f"  stage1_summary.json : FR={d['source_fr_count']} elements={d['element_count']} "
              f"relations={d['evidence_relation_count']} sim={d['simulation_nodes']}n/"
              f"{d['simulation_edges']}e pool={d['fixed_pool_count']}")
    hr = root / "human_review"
    for name, expect in (("RQ2_human_review.csv", 20), ("RQ3_human_review.csv", None)):
        p = hr / name
        if not p.exists():
            print(f"  {name:26s} MISSING")
            continue
        with p.open(encoding="utf-8-sig") as h:
            rows = list(csv.DictReader(h))
        flag = "" if expect is None or len(rows) == expect else f"  <-- expected {expect}"
        valid = sum(1 for r in rows if r.get("人工去向") == "有效且缺失")
        print(f"  {name:26s} rows={len(rows):4d} valid={valid:3d} "
              f"cols={len(rows[0])}{flag}")
    for name in ("RQ2_HUMAN_BUDGET.md", "RQ3_COMPONENT_CONTRIBUTION.md"):
        p = hr / name
        print(f"  {name:26s} {'OK ' + str(p.stat().st_size) + ' B' if p.exists() else 'MISSING'}")
    for name in ("causal_graph.png", "causal_graph.json", "evidence_graph.graphml",
                 "simulation_graph.graphml", "causal_graph_summary.md"):
        p = root / "graph" / name
        if p.exists():
            print(f"  graph/{name:31s} {p.stat().st_size:>9,} B")
    rq3 = sorted(p.name for p in (root / "RQ3").iterdir() if p.is_dir())
    print(f"  RQ3 variants: {', '.join(rq3)}")
