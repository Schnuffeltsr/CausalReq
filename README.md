# CausalReq

> **CausalReq: Causal Dependency-Guided Requirement Gap Diagnosis and Evidence-Constrained Completion**

This file is the map. Every folder and every file in the repository is listed below with
its role.

## Repository layout

| Path | What is there | Files |
|---|---|---:|
| `core/` | The pipeline, the two patches, the stage drivers, the prompt loader | 7 `.py` |
| `rq1/` … `rq4/` | The RQ-specific code, one folder per research question | 6 `.py` |
| `tools/` | Utilities that belong to no single research question | 6 `.py` |
| `prompts/` | Every prompt template as a text file, loaded at run time | 9 files |
| `samples/` | All case data: datasets, processed runs, validation oracle | 221 files |
| `requirements.txt` | Runtime dependencies (needed to run the code) | 1 |
| `.gitignore` | Keeps caches, logs and generated figures out of the repository | 1 |

`samples/` is documented in [`samples/README.md`](samples/README.md); the prompts are
documented in [`prompts/README.md`](prompts/README.md).

## Code — `core/` (shared pipeline)

| File | Role |
|---|---|
| `causalreq_experiment.py` | The whole pipeline: FR partitioning, element and relation extraction, evidence graph, signed acyclic simulation graph, Bayesian simulator, do-operator `ACE_M`, fixed 20-candidate pool, three nomination routes, document-wide validation, RQ1/RQ2/RQ3 export. The ablation switches are in `VARIANTS` at the top. |
| `active_fix.py` | Patch: the shipped element prompt allowed an empty `active_meaning`, which left the simulation graph without nodes. Adds a mandatory instruction to fill it. |
| `element_fix.py` | Patch: the shipped extractor aborted a document on a cross-type duplicate element name; this disambiguates the name and records the rename instead. |
| `run_stage_source.py` | Stage-1 driver: source document → `source/*.json`, graphs, fixed pool, `RQ2/` exports. Applies both patches (`--no-name-fix` disables the second). |
| `run_rq3_fast.py` | Variant driver: one process per variant, parallel validation, bounded retry on an empty response, optional cross-variant cache. |
| `run_rq3_variant.py` | The same schedule written sequentially — the readable reference version. |

## Code — one folder per research question

| Folder | File | Role |
|---|---|---|
| `rq1/` | `export_rq1.py` | Rebuilds `samples/<doc>/RQ1/` (the completed requirement set) from an existing run, without any LLM call |
| `rq2/` | `build_rq2_evidence.py` | Review worksheet for the 20 candidates: source/target evidence plus the relations on the shortest path |
| `rq2/` | `make_figure.py` | RQ2 figure (vector PDF + 300 dpi PNG) → `figures/` |
| `rq3/` | `variant_table.py` | Compact per-variant counter table straight from the run artefacts |
| `rq4/` | `trace_case.py` | Prints the evidence chain of one supplementary requirement (source FR → nomination → validation → retained text) plus a contrasting sibling nomination |
| `rq4/` | `make_figure.py` | RQ4 figure (vector PDF + 300 dpi PNG) → `figures/` |

## Code — `tools/` (cross-cutting)

| File | Role |
|---|---|
| `export_graph.py` | Causal-graph export: `causal_graph.png/json`, `evidence_graph.graphml`, `simulation_graph.graphml`, both `.dot`, `causal_graph_summary.md` |
| `summarize_results.py` | One-document report `RESULTS.md` (extraction and graph, RQ2 pool and rankings, RQ3 variants, retained supplements, nomination detail) |
| `summarize_all_runs.py` | Cross-document table of all variants: nomination counts, route mix, model dispositions |
| `list_artifacts.py` | Prints what exists for every document under a run root |
| `verify_saved.py` | Integrity check of the published artefacts (pool, nominations, supplements, figures) |
| `make_manifest.py` | Regenerates an inventory file `MANIFEST.md` at the repository root if you want one |

## Prompts — `prompts/`

Every prompt the pipeline sends to the model is a text file here, loaded through
`core/prompt_store.py`. The string literals in the code remain as fallbacks, so a missing
file changes nothing. The loaded text is byte-identical to those literals (SHA-256
verified).

| Path | Code constant | Stage |
|---|---|---|
| `prompts/rq1/nomination_dependency.txt` | `DEPENDENCY_PROMPT` | dependency-scenario probe for one pool candidate |
| `prompts/rq1/nomination_complement.txt` | `COMPLEMENT_PROMPT` | isolated-element and operation-coverage review |
| `prompts/rq1/validation_screen.txt` | `SCREEN_PROMPT` | screens one nomination against one original FR |
| `prompts/rq1/validation_final.txt` | `FINAL_SCREEN_PROMPT` | final disposition plus the drafted supplement |
| `prompts/rq1/patch_active_meaning.txt` | `active_fix.ACTIVE_CLAUSE` | appended to the element prompt (mandatory `active_meaning`) |
| `prompts/rq1/patch_unique_element_names.txt` | `element_fix.UNIQUE_CLAUSE` | appended to the element prompt (unique element names) |
| `prompts/shared/element_extraction.txt` | `ELEMENT_PROMPT` | per-FR element extraction |
| `prompts/shared/relation_extraction.txt` | `RELATION_PROMPT` | relation extraction |

The `rq1/` templates are the completion prompts: they produce and filter the completed
requirement set that RQ1 evaluates, and their output is also what RQ2 ranks and RQ3
ablates. `shared/` holds the graph-construction prompts used before any research question.
See [`prompts/README.md`](prompts/README.md) for the call sites and for how to edit a
template safely.

## Case data — `samples/`

| Path | What is there | Files |
|---|---|---:|
| `source_documents/<system>/` | The 42 original test documents (`Document/` only; the delivered `Analysis/` files are excluded — they are not an input to any step) | 42 |
| `reference_documents/<system>/` | The 42 enhanced reference specifications — the oracle for "genuinely missing obligation" | 42 |
| `reference_targets/` | Plain-text extracts of the three reference documents, used as the validation oracle | 3 |
| `MDOT_MDOT_simple2/`, `Inventory_MIRC3/`, `WebStore_MIRC3/` | Fully processed samples: original text, extracted elements and relations, graphs, fixed pool and rankings, five RQ3 variants and `RESULTS.md` | 133 |
| `samples/README.md` | The per-document output contract, the dataset description and how to read a sample | 1 |

## Generated at runtime, not stored here

| Path | Written by | Note |
|---|---|---|
| `figures/` | `rq2/make_figure.py`, `rq4/make_figure.py` | paper figures; the folder is ignored by git |
| `samples/*/cache/` | `run_rq3_fast.py` | LLM screening cache (scheduling aid, ~33 MB, regenerated on demand) |
| `__pycache__/` | Python | ignored |

## Running the code

```bash
pip install -r requirements.txt
export CAUSALREQ_API_KEY="your api key"
export CAUSALREQ_BASE_URL="your url"
export CAUSALREQ_MODEL=deepseek-flash  PYTHONIOENCODING=utf-8

# stage 1 on any of the 42 documents in the repository
python core/run_stage_source.py --doc-id Email_MIRC2 \
    --source samples/source_documents/Email/filtered_Email_MIRC2_doc.docx \
    --out-root samples

# then the five variants (one process each), and the reports
python core/run_rq3_fast.py --variant Full --doc-id Email_MIRC2 --workers 8 --out-root samples
python tools/export_graph.py samples Email_MIRC2
python tools/summarize_results.py samples Email_MIRC2
```

`samples/` is both the input root and the output root: the tools read the case data and
write their reports next to it.
