# -*- coding: utf-8 -*-
"""Run ONE RQ3 variant with concurrency, without changing any experiment logic.

Why: produce_variant() validates every nomination with one screening call per
original FR (8 FRs here) plus a final call. With 71 nominations that is ~640
sequential calls per variant. This wrapper

  1. calls the *same* M.generate_nominations() once,
  2. calls the *same* M.preliminarily_validate() for every nomination, but
     across a thread pool (validation of one nomination does not depend on any
     other nomination),
  3. monkey-patches those two functions to return the already-computed values,
     then calls the *same* M.produce_variant(), which therefore writes exactly
     the files the sequential run would write, in the original order.

No prompt, threshold, filter, deduplication or write path is modified.
"""
import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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
parser.add_argument("--workers", type=int, default=6)
args = parser.parse_args()

OUT_ROOT = BASE / args.out_root
root = OUT_ROOT / args.doc_id
src = root / "source"

original_doc = (src / "original_document.txt").read_text(encoding="utf-8")
frs = json.loads((src / "fr_blocks.json").read_text(encoding="utf-8"))
elements = json.loads((src / "elements.json").read_text(encoding="utf-8"))
relations = json.loads((src / "relations.json").read_text(encoding="utf-8"))

start = time.time()
model = M.CausalModel(elements, relations)
pool = M.build_fixed_pool(args.doc_id, model, args.pool_size)
client = M.get_client()
settings = M.VARIANTS[args.variant]
print(f"[{args.variant}] model ready | sim={model.simulation_graph.number_of_nodes()}n/"
      f"{model.simulation_graph.number_of_edges()}e pool={len(pool)}", flush=True)

# --- 1. nominations (the same call produce_variant would make) --------------
t0 = time.time()
nominations = M.generate_nominations(client, frs, elements, relations, model, pool, settings)
origins = {}
for item in nominations:
    origins[item["origin"]] = origins.get(item["origin"], 0) + 1
print(f"[{args.variant}] nominations={len(nominations)} {origins} "
      f"in {time.time()-t0:.0f}s (total {(time.time()-start)/60:.1f} min)", flush=True)

# --- 2. validation, across nominations --------------------------------------
results = {}
if settings["full_document_validation"]:
    import hashlib
    import os

    CACHE = OUT_ROOT / args.doc_id / "cache" / "validation"
    CACHE.mkdir(parents=True, exist_ok=True)
    MODEL = os.getenv("CAUSALREQ_MODEL", "unknown")
    STATS = {"hit": 0, "miss": 0}

    def cache_path(nomination):
        payload = "\x1f".join([
            args.doc_id, MODEL, nomination.get("question", ""),
            nomination.get("draft_obligation", ""),
        ])
        key = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        return CACHE / f"{key}.json"

    def validate_with_retry(nomination, attempts=3):
        """Same call as the shipped pipeline, with two scheduling aids only.

        1. cross-variant cache: identical (document, model, question, draft)
           means an identical screening job, so the result is reused instead of
           recomputed for every ablation variant;
        2. bounded retry on an empty/failed model response (the shipped
           ask_json raises on an empty response).
        The validation logic itself is untouched.
        """
        path = cache_path(nomination)
        if path.exists():
            try:
                STATS["hit"] += 1
                return json.loads(path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001  (corrupt cache entry -> recompute)
                pass

        last = None
        for attempt in range(attempts):
            try:
                result = M.preliminarily_validate(client, frs, nomination)
                tmp = path.with_suffix(".tmp")
                tmp.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
                tmp.replace(path)
                STATS["miss"] += 1
                return result
            except Exception as exc:  # noqa: BLE001
                last = exc
                print(f"[{args.variant}] retry {attempt + 1}/{attempts} for "
                      f"{nomination['nomination_id']}: {type(exc).__name__} {exc}",
                      flush=True)
                time.sleep(3 + 4 * attempt)
        raise last

    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool_ex:
        futures = {pool_ex.submit(validate_with_retry, n): n for n in nominations}
        for future in as_completed(futures):
            nomination = futures[future]
            try:
                results[nomination["nomination_id"]] = future.result()
            except Exception as exc:  # noqa: BLE001
                print(f"[{args.variant}] validation FAILED for "
                      f"{nomination['nomination_id']}: {type(exc).__name__} {exc}", flush=True)
                raise
            done += 1
            if done % 5 == 0 or done == len(futures):
                print(f"[{args.variant}] validated {done}/{len(futures)} "
                      f"({(time.time()-t0)/60:.1f} min, "
                      f"total {(time.time()-start)/60:.1f} min) "
                      f"cache hit={STATS['hit']} miss={STATS['miss']}", flush=True)
    outcomes = {}
    for value in results.values():
        key = value.get("preliminary_outcome", "?")
        outcomes[key] = outcomes.get(key, 0) + 1
    print(f"[{args.variant}] validation outcomes={outcomes}", flush=True)

# --- 3. reuse them inside the untouched produce_variant ---------------------
_original_generate = M.generate_nominations
_original_validate = M.preliminarily_validate

M.generate_nominations = lambda *a, **k: nominations
if settings["full_document_validation"]:
    def cached_validate(client_, frs_, nomination_):
        cached = results.get(nomination_["nomination_id"])
        if cached is None:
            return _original_validate(client_, frs_, nomination_)
        return cached
    M.preliminarily_validate = cached_validate

nominations_out, supplements = M.produce_variant(
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
)

print(f"[{args.variant}] DONE in {(time.time()-start)/60:.1f} min | "
      f"nominations={len(nominations_out)} supplements={len(supplements)}", flush=True)

if args.variant == "Full":
    count = M.export_rq1(args.doc_id, original_doc, supplements, OUT_ROOT)
    print(f"[Full] RQ1 exported; CausalReq supplements: {count}", flush=True)
