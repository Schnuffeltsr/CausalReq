# -*- coding: utf-8 -*-
"""Summarise all five variants for every document under an out-root."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
ORDER = ["Full", "NoSignedPropagation", "NoIsolatedReview", "NoOperationReview",
         "NoFullDocumentValidation"]

for doc_dir in sorted(
    p for p in OUT_ROOT.iterdir()
    if p.is_dir() and (p / "stage1_summary.json").exists()
):
    doc_id = doc_dir.name
    stage1 = doc_dir / "stage1_summary.json"
    if stage1.exists():
        s = json.loads(stage1.read_text(encoding="utf-8"))
        print(f"\n### {doc_id}")
        print(f"  stage1: FR={s['source_fr_count']} elements={s['element_count']} "
              f"(active {s['elements_with_active_meaning']}) relations="
              f"{s['evidence_relation_count']} sim={s['simulation_nodes']}n/"
              f"{s['simulation_edges']}e exclusions={s['exclusions']} "
              f"pool={s['fixed_pool_count']} calls={s['llm_calls']} {s['minutes']}min")
    print(f"  {'variant':26s} {'noms':>5s} {'sups':>5s}  origins                        outcomes")
    for v in ORDER:
        d = doc_dir / "RQ3" / v
        if not (d / "nominations.json").exists():
            print(f"  {v:26s}   -- missing --")
            continue
        noms = json.loads((d / "nominations.json").read_text(encoding="utf-8"))
        sups = json.loads((d / "supplements.json").read_text(encoding="utf-8"))
        org = Counter(n["origin"] for n in noms)
        out = Counter(n.get("preliminary_outcome", "?") for n in noms)
        o = "dep={} iso={} op={}".format(org.get("dependency", 0),
                                         org.get("isolated", 0),
                                         org.get("operation", 0))
        print(f"  {v:26s} {len(noms):5d} {len(sups):5d}  {o:30s} "
              + " ".join(f"{k}={val}" for k, val in out.most_common()))
