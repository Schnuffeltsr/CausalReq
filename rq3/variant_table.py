# -*- coding: utf-8 -*-
"""Print the five-variant comparison table for the MDOT simple2 run."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RQ3 = Path(__file__).resolve().parents[1] / "samples" / "MDOT_MDOT_simple2" / "RQ3"
ORDER = ["Full", "NoSignedPropagation", "NoIsolatedReview", "NoOperationReview",
         "NoFullDocumentValidation"]

print(f"{'variant':26s} {'noms':>5s} {'sups':>5s}  origins                       outcomes")
for name in ORDER:
    d = RQ3 / name
    if not d.exists():
        print(f"{name:26s}   -- missing --")
        continue
    noms = json.loads((d / "nominations.json").read_text(encoding="utf-8"))
    sups = json.loads((d / "supplements.json").read_text(encoding="utf-8"))
    origins = Counter(n["origin"] for n in noms)
    outcomes = Counter(n.get("preliminary_outcome", "?") for n in noms)
    org = "dep={dependency} iso={isolated} op={operation}".format(
        dependency=origins.get("dependency", 0),
        isolated=origins.get("isolated", 0),
        operation=origins.get("operation", 0))
    out = " ".join(f"{k}={v}" for k, v in outcomes.most_common())
    print(f"{name:26s} {len(noms):5d} {len(sups):5d}  {org:28s}  {out}")

print("\nFull variant supplements by origin:")
full = RQ3 / "Full"
sups = json.loads((full / "supplements.json").read_text(encoding="utf-8"))
print(" ", dict(Counter(s["origin"] for s in sups)))

print("\nRQ2 fixed pool (all 20, by |ACE|):")
pool = json.loads((RQ3.parent / "RQ2" / "fixed_pool.json").read_text(encoding="utf-8"))
for rank, item in enumerate(sorted(pool, key=lambda x: -abs(x["ace"])), 1):
    print(f"  {rank:2d}. {item['candidate_id']} |ACE|={abs(item['ace']):.4f} "
          f"reach={item['reachability']}  {item['source'][:44]} -> {item['target'][:44]}")
