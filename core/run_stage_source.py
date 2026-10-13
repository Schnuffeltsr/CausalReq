# -*- coding: utf-8 -*-
"""Stage 1 for one document: extraction, signed graph, RQ2 fixed pool.

Parameterised version of the original run_one() prefix:
  read_docx_in_order -> split_frs -> extract_elements -> extract_relations ->
  CausalModel -> build_fixed_pool -> export_rq2
with the documented ELEMENT_PROMPT clarification (active_fix.py) and a per-call
progress log. The shipped script is not modified.
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "core"))
import causalreq_experiment as M  # noqa: E402
import active_fix  # noqa: E402
import element_fix  # noqa: E402

parser = argparse.ArgumentParser()
parser.add_argument("--doc-id", required=True)
parser.add_argument("--source", required=True)
parser.add_argument("--out-root", default="samples")
parser.add_argument("--pool-size", type=int, default=20)
parser.add_argument("--cross-window", type=int, default=2)
parser.add_argument("--seed", type=int, default=20261010)
parser.add_argument("--no-name-fix", action="store_true",
                    help="disable cross-type name-collision resolution")
args = parser.parse_args()

OUT_ROOT = BASE / args.out_root
SOURCE = Path(args.source)

active_fix.patch(M)
if not args.no_name_fix:
    M.ELEMENT_PROMPT = M.ELEMENT_PROMPT + element_fix.UNIQUE_CLAUSE
    element_fix.install(M)
print(f"[{args.doc_id}] ELEMENT_PROMPT patched: len={len(M.ELEMENT_PROMPT)} | "
      f"name-collision fix: {not args.no_name_fix}", flush=True)

_original_ask = M.ask_json
STATE = {"n": 0, "t0": time.time()}


def logged_ask(client, system_prompt, payload):
    STATE["n"] += 1
    label = system_prompt.strip().splitlines()[0][:44]
    if "COMPLETE" in system_prompt:
        label = f"elements {payload.get('fr', {}).get('fr_id', '?')}"
    elif "causal or dependency" in system_prompt:
        label = "relations " + "+".join(fr.get("fr_id", "?") for fr in payload.get("frs", []))
    start = time.time()
    try:
        result = _original_ask(client, system_prompt, payload)
    except Exception as exc:  # noqa: BLE001
        print(f"[{args.doc_id}] call #{STATE['n']} {label} FAILED after "
              f"{time.time()-start:.0f}s: {type(exc).__name__} {exc}", flush=True)
        raise
    print(f"[{args.doc_id}] call #{STATE['n']:3d} {label:34s} {time.time()-start:6.1f}s "
          f"(total {(time.time()-STATE['t0'])/60:.1f} min)", flush=True)
    return result


M.ask_json = logged_ask

client = M.get_client()
original_doc = M.read_docx_in_order(SOURCE)
frs = M.split_frs(original_doc)
print(f"[{args.doc_id}] FR blocks: {len(frs)}", flush=True)

root = OUT_ROOT / args.doc_id
M.write_text(root / "source" / "original_document.txt", original_doc)
M.write_json(root / "source" / "fr_blocks.json", frs)

elements = M.extract_elements(client, frs)
print(f"[{args.doc_id}] elements: {len(elements)} | with active_meaning: "
      f"{sum(1 for e in elements if (e.get('active_meaning') or '').strip())}", flush=True)

relations = M.extract_relations(client, frs, elements, args.cross_window)
print(f"[{args.doc_id}] relations: {len(relations)}", flush=True)

model = M.CausalModel(elements, relations)
print(f"[{args.doc_id}] evidence graph: {model.evidence_graph.number_of_nodes()} nodes / "
      f"{model.evidence_graph.number_of_edges()} edges | simulation graph: "
      f"{model.simulation_graph.number_of_nodes()} nodes / "
      f"{model.simulation_graph.number_of_edges()} edges | exclusions "
      f"{len(model.exclusions)}", flush=True)

M.write_json(root / "source" / "elements.json", elements)
M.write_json(root / "source" / "relations.json", relations)
M.write_json(root / "source" / "simulation_exclusions.json", model.exclusions)
resolutions = getattr(M, "_LAST_NAME_RESOLUTIONS", [])
if resolutions:
    M.write_json(root / "source" / "name_collisions.json", resolutions)
    print(f"[{args.doc_id}] cross-type name collisions resolved: {len(resolutions)}", flush=True)

pool = M.build_fixed_pool(args.doc_id, model, args.pool_size)
M.export_rq2(args.doc_id, original_doc, pool, root, args.seed)
print(f"[{args.doc_id}] fixed pool: {len(pool)} candidates", flush=True)

summary = {
    "doc_id": args.doc_id,
    "source_path": str(SOURCE),
    "source_fr_count": len(frs),
    "element_count": len(elements),
    "elements_with_active_meaning": sum(
        1 for e in elements if (e.get("active_meaning") or "").strip()),
    "evidence_relation_count": len(relations),
    "evidence_nodes": model.evidence_graph.number_of_nodes(),
    "evidence_edges": model.evidence_graph.number_of_edges(),
    "simulation_nodes": model.simulation_graph.number_of_nodes(),
    "simulation_edges": model.simulation_graph.number_of_edges(),
    "exclusions": len(model.exclusions),
    "fixed_pool_count": len(pool),
    "model_version": model.model_version,
    "llm_calls": STATE["n"],
    "minutes": round((time.time() - STATE["t0"]) / 60, 1),
}
M.write_json(root / "stage1_summary.json", summary)
print(f"[{args.doc_id}] DONE {json.dumps(summary, ensure_ascii=False)}", flush=True)
