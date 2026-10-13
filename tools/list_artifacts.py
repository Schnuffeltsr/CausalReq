# -*- coding: utf-8 -*-
"""List the artefacts produced for every document under an out-root."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

OUT_ROOT = Path(__file__).resolve().parents[1] / "samples"
for doc in sorted(p for p in OUT_ROOT.iterdir() if p.is_dir()):
    print(f"=== {doc.name}")
    for sub in ("graph", "RQ1", "RQ2", "human_review"):
        d = doc / sub
        if d.is_dir():
            files = sorted(f.name for f in d.iterdir() if f.is_file())
            print(f"  {sub}: {len(files)} files -> {', '.join(files[:8])}")
    rq3 = doc / "RQ3"
    if rq3.is_dir():
        for v in sorted(p for p in rq3.iterdir() if p.is_dir()):
            files = sorted(f.name for f in v.iterdir() if f.is_file())
            print(f"  RQ3/{v.name}: {len(files)} files")
