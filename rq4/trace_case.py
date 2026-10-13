# -*- coding: utf-8 -*-
"""RQ4 — print the evidence chain of one supplementary requirement.

The paper's traceability case is the MDOT-Simple2 report-delivery obligation. This
tool resolves the chain from the run artefacts:

    source requirement  ->  nomination  ->  document-wide validation
                        ->  retained supplement  ->  human verdict

and, when a sibling nomination is given, shows the contrasting verdict that makes the
case auditable (a provisional "retained" decision that human review classified as
already covered).

Usage:
    python rq4/trace_case.py [OUT_ROOT] [DOC_ID] [NOMINATION_ID] [SIBLING_ID]

Defaults reproduce the paper case:
    OUT_ROOT=results  DOC_ID=MDOT_MDOT_simple2
    NOMINATION_ID=OPERATION-bfe2c70a5486  SIBLING_ID=DEP-014
"""
import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]

OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"
NOMINATION = sys.argv[3] if len(sys.argv) > 3 else "OPERATION-bfe2c70a5486"
SIBLING = sys.argv[4] if len(sys.argv) > 4 else "DEP-014"

root = OUT_ROOT / DOC_ID
full = root / "RQ3" / "Full"
nominations = {n["nomination_id"]: n
               for n in json.loads((full / "nominations.json").read_text(encoding="utf-8"))}
supplements = {s["source_nomination_id"]: s
               for s in json.loads((full / "supplements.json").read_text(encoding="utf-8"))}
original = (root / "source" / "original_document.txt").read_text(encoding="utf-8")

# the human verdict table is not part of the published repository; the trace
# then stops at the retained supplement
verdicts = {}
verdict_path = root / "human_review" / "RQ3_human_review.csv"
if verdict_path.exists():
    with verdict_path.open(encoding="utf-8-sig") as handle:
        verdicts = {r["提名ID"]: r for r in csv.DictReader(handle)}


def source_excerpt(fr_ids):
    lines = []
    for fr_id in fr_ids:
        for paragraph in original.split("\n\n"):
            if fr_id in paragraph or fr_id.replace("FRBLOCK-", "FR-") in paragraph:
                lines.append(paragraph.strip()[:400])
                break
    return lines or ["(no excerpt found for %s)" % ", ".join(fr_ids)]


def show(nomination_id, heading):
    print(f"\n{'=' * 78}\n{heading}: {nomination_id}\n{'=' * 78}")
    nomination = nominations.get(nomination_id)
    if nomination is None:
        print("  not present in the Full variant of this document")
        return
    print(f"  route            : {nomination['origin']}")
    print(f"  evidence FRs     : {', '.join(nomination.get('evidence_fr_ids', []))}")
    print(f"  model outcome    : {nomination.get('preliminary_outcome')}")
    print(f"  FRs screened     : {len(nomination.get('checked_fr_ids', []))} "
          f"({', '.join(nomination.get('checked_fr_ids', []))})")
    print(f"  question         : {nomination.get('question', '')[:220]}")
    print(f"  draft obligation : {nomination.get('draft_obligation', '')[:220]}")
    supplement = supplements.get(nomination_id)
    print(f"  retained text    : "
          f"{supplement['text'][:220] if supplement else '(not retained)'}"
          + (f"   [{supplement['output_id']}]" if supplement else ""))
    verdict = verdicts.get(nomination_id)
    if verdict is None:
        print("  human verdict    : (not published with this repository)")
    else:
        print(f"  human verdict    : {verdict['人工去向']}"
              f"   obligation {verdict['义务ID'] or '-'}"
              f"   support {verdict['原文依据']}")
        print(f"  human reason     : {verdict['理由'][:220]}")
    print("  source excerpt:")
    for line in source_excerpt(nomination.get("evidence_fr_ids", [])):
        print(f"    {line}")


print(f"document: {DOC_ID}   (run root: {root})")
print(f"original FR blocks: "
      f"{len(json.loads((root / 'source' / 'frs.json').read_text(encoding='utf-8')))}"
      if (root / "source" / "frs.json").exists() else "")

show(NOMINATION, "main nomination")
if SIBLING:
    show(SIBLING, "contrasting sibling nomination")

print(f"\n{'=' * 78}")
print("Reading: the main nomination is the one the paper follows; the sibling shows the "
      "provisional-retained / judged-covered contrast that makes the record auditable.")
