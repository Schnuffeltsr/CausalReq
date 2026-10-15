# -*- coding: utf-8 -*-
"""RQ2 worksheet built from the extracted graph: element evidence + path relations.

For each of the 20 fixed-pool candidates this shows
  * the source/target elements with their type, active meaning and the exact
    quotations (with FR ids) that ground them, and
  * the relations on the shortest source→target path, with their relation type,
    sign, confidence and quotations,
so the reviewer can decide whether the pair is a documented business dependency
and whether it points to a missing obligation.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"

import networkx as nx  # noqa: E402

root = OUT_ROOT / DOC_ID
src = root / "source"
pool = json.loads((root / "RQ2" / "fixed_pool.json").read_text(encoding="utf-8"))
elements = {e["name"]: e for e in json.loads((src / "elements.json").read_text(encoding="utf-8"))}
relations = json.loads((src / "relations.json").read_text(encoding="utf-8"))
exclusions = json.loads((src / "simulation_exclusions.json").read_text(encoding="utf-8"))


def clip(t, n):
    t = re.sub(r"\s+", " ", (t or "").strip())
    return t if len(t) <= n else t[:n] + "…"


def elem_block(name):
    e = elements.get(name)
    if not e:
        return f"      (element not found: {name})"
    lines = [f"      type={e['type']} conf={e['confidence']} "
             f"active=“{clip(e.get('active_meaning'), 110)}”"]
    for ev in e.get("evidence", [])[:2]:
        lines.append(f"        [{ev['fr_id']}] “{clip(ev['quote'], 150)}”")
    return "\n".join(lines)


# build the simulation graph from the retained relations (same rule as CausalModel)
sim = nx.DiGraph()
for r in relations:
    sim.add_edge(r["source"], r["target"])

out = [f"# RQ2 evidence worksheet — {DOC_ID}\n",
       "\n每条的源/目标元素证据与其最短路径上的关系（含原文引文）。\n"]
for rank, item in enumerate(sorted(pool, key=lambda x: -abs(x["ace"])), 1):
    s, t = item["source"], item["target"]
    out.append(f"\n[{rank:2d}] {item['candidate_id']}  ACE={item['ace']:+.4f} "
               f"p1={item['p_do_1']:.3f} p0={item['p_do_0']:.3f} reach={item['reachability']}")
    out.append(f"   SOURCE {s}\n{elem_block(s)}")
    out.append(f"   TARGET {t}\n{elem_block(t)}")
    try:
        path = nx.shortest_path(sim, s, t)
    except Exception:  # noqa: BLE001
        path = [s, t]
    out.append(f"   path: {' → '.join(path)}  (hops={len(path)-1})")
    for a, b in zip(path[:-1], path[1:]):
        rels = [r for r in relations if r["source"] == a and r["target"] == b]
        for r in rels[:2]:
            out.append(f"      rel {r['relation_type']}/{r['propagation_sign']} "
                       f"conf={r['confidence']}: {a} → {b}")
            out.append(f"         src[{r['source_fr_id']}] “{clip(r['source_quote'], 110)}”")
            out.append(f"         tgt[{r['target_fr_id']}] “{clip(r['target_quote'], 110)}”")
            out.append(f"         reason: {clip(r.get('reason'), 130)}")

out.append("\n\n## 被排除的关系（含与本池候选相关的）\n")
for ex in exclusions:
    out.append(f"  {ex['source']} → {ex['target']} : {ex['reason']}")

text = "".join(out)
review = root / "review"
review.mkdir(parents=True, exist_ok=True)
(review / "w_rq2_evidence.txt").write_text(text, encoding="utf-8")
print(f"written: {review / 'w_rq2_evidence.txt'} ({len(text)} chars)")
