# -*- coding: utf-8 -*-
"""Run ONE RQ3 variant, reusing the extraction artefacts of stage 1.

Scheduling wrapper only: it calls the same functions of causalreq_experiment.py
(CausalModel, build_fixed_pool, produce_variant, export_rq1) without changing any
prompt, threshold or validation rule. Running the five variants as five
concurrent processes reproduces what the sequential loop in run_one() produces,
in about one fifth of the wall time.
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

parser = argparse.ArgumentParser()
parser.add_argument("--variant", required=True, choices=list(M.VARIANTS))
parser.add_argument("--doc-id", default="MDOT_MDOT_simple2")
parser.add_argument("--pool-size", type=int, default=M.POOL_SIZE)
parser.add_argument("--out-root", default="samples")
parser.add_argument(
    "--require-evidence",
    action=argparse.BooleanOptionalAction,
    default=M.REQUIRE_EVIDENCE_DEFAULT,
    help="引文级证据闸门（默认开）：只改标注，不丢弃条目。",
)
parser.add_argument(
    "--drop-non-retained",
    action="store_true",
    default=M.DROP_NON_RETAINED_DEFAULT,
    help="淘汰闸门（默认关）：只输出 retained 的提名。",
)
parser.add_argument(
    "--enforce-validation",
    action="store_true",
    help="同时打开上面两个闸门，即论文评测使用的配置。",
)
parser.add_argument(
    "--refine-output",
    action=argparse.BooleanOptionalAction,
    default=M.REFINE_OUTPUT_DEFAULT,
    help="输出精炼（默认开）：对补充需求做语义级去重/合并/剔除。",
)
parser.add_argument(
    "--iterations",
    type=int,
    default=M.ITERATIONS_DEFAULT,
    help="迭代轮数（默认 2）。>1 时把本轮草稿追加进工作文档再跑一轮。",
)
parser.add_argument(
    "--stop-if-no-new",
    action=argparse.BooleanOptionalAction,
    default=M.STOP_IF_NO_NEW_DEFAULT,
    help="某一轮没有新草稿时提前结束（默认开）。",
)
parser.add_argument(
    "--cross-window",
    type=int,
    default=2,
    help="迭代重建工作文档时，跨 FR 关系抽取的相邻窗口。",
)
args = parser.parse_args()

OUT_ROOT = BASE / args.out_root
root = OUT_ROOT / args.doc_id
src = root / "source"

print(f"[{args.variant}] reading artefacts from {src}", flush=True)
original_doc = (src / "original_document.txt").read_text(encoding="utf-8")
frs = json.loads((src / "fr_blocks.json").read_text(encoding="utf-8"))
elements = json.loads((src / "elements.json").read_text(encoding="utf-8"))
relations = json.loads((src / "relations.json").read_text(encoding="utf-8"))

start = time.time()
model = M.CausalModel(elements, relations)
pool = M.build_fixed_pool(args.doc_id, model, args.pool_size)
print(f"[{args.variant}] model ready in {time.time()-start:.1f}s | "
      f"sim nodes={model.simulation_graph.number_of_nodes()} "
      f"edges={model.simulation_graph.number_of_edges()} pool={len(pool)}", flush=True)

client = M.get_client()
settings = M.VARIANTS[args.variant]

# progress instrumentation: log every LLM call without changing behaviour
_original_ask = M.ask_json
STATE = {"n": 0}


def logged_ask(client_, system_prompt, payload):
    STATE["n"] += 1
    label = system_prompt.strip().splitlines()[0][:40]
    if "REVIEW QUESTION" in system_prompt:
        label = "nomination"
    elif "review QUESTIONS" in system_prompt:
        label = f"complement {payload.get('fr', {}).get('fr_id', '?')}"
    elif "Screen ONE" in system_prompt:
        label = f"screen {payload.get('original_fr', {}).get('fr_id', '?')}"
    elif "PRELIMINARY" in system_prompt:
        label = "final-screen"
    started = time.time()
    result = _original_ask(client_, system_prompt, payload)
    print(f"[{args.variant}] call #{STATE['n']:3d} {label:24s} "
          f"{time.time()-started:6.1f}s", flush=True)
    return result


M.ask_json = logged_ask

nominations, supplements = M.produce_variant(
    client=client,
    doc_id=args.doc_id,
    original_doc=original_doc,
    frs=frs,
    elements=elements,
    relations=relations,
    model=model,
    pool=pool,
    variant_name=args.variant,
    settings=settings,
    output_root=OUT_ROOT,
    require_evidence=(True if args.enforce_validation else args.require_evidence),
    drop_non_retained=(True if args.enforce_validation else args.drop_non_retained),
    refine_output=args.refine_output,
    iterations=args.iterations,
    cross_window=args.cross_window,
    pool_size=args.pool_size,
    stop_if_no_new=args.stop_if_no_new,
)

outcomes = {}
for item in nominations:
    key = item.get("preliminary_outcome", "?")
    outcomes[key] = outcomes.get(key, 0) + 1

print(f"[{args.variant}] DONE in {time.time()-start:.1f}s | "
      f"llm_calls={STATE['n']} nominations={len(nominations)} "
      f"supplements={len(supplements)} outcomes={outcomes}", flush=True)

if args.variant == "Full":
    count = M.export_rq1(args.doc_id, original_doc, supplements, OUT_ROOT)
    print(f"[Full] RQ1 exported; CausalReq supplements: {count}", flush=True)
