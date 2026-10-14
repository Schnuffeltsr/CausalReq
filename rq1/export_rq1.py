# -*- coding: utf-8 -*-
"""Regenerate the RQ1 folder from an existing run (no LLM calls).

Uses the Full variant's supplements.json, so the RQ1 deliverable reflects the
baseline-free version of export_rq1().
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "core"))
import causalreq_experiment as M  # noqa: E402

OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"

root = OUT_ROOT / DOC_ID
original_doc = (root / "source" / "original_document.txt").read_text(encoding="utf-8")
supplements = json.loads((root / "RQ3" / "Full" / "supplements.json").read_text(encoding="utf-8"))

count = M.export_rq1(DOC_ID, original_doc, supplements, OUT_ROOT)
print(f"export_rq1 -> {count} CausalReq supplements")

out = root / "RQ1"
for path in sorted(out.iterdir()):
    print(f"  {path.name}  {path.stat().st_size}")

print("\n--- manifest.json ---")
print((out / "manifest.json").read_text(encoding="utf-8"))

print("--- causalreq_supplements_only.txt (head) ---")
text = (out / "causalreq_supplements_only.txt").read_text(encoding="utf-8")
print(text[:900])
print("...")
print(text[-700:])
