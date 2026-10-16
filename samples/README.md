# samples — case data and the execution sample

These are the artefacts produced by running the code in `core/` and `rq1/`–`rq4/`
end to end on one specification. They are kept as an **execution example**: they
show that the released pipeline runs, and they define the exact output contract of the
released pipeline. They are not the runs behind the quantitative evaluation
reported in the paper. The sample was produced with document-wide validation filtering
enabled (`--enforce-validation`), i.e. the configuration used for the paper.

```
samples/
├── source_documents/            the original test dataset: 42 DOCX files
│   ├── CCTNS/        (6)         7 systems x 6 variants
│   ├── CityMapper/   (6)           filtered_<system>_<variant>_doc.docx
│   ├── Email/        (6)           variants: MIRC1-3, simple1-3
│   ├── Inventory/    (6)
│   ├── MDOT/         (6)
│   ├── QuickEats/    (6)
│   └── WebStore/     (6)
├── reference_documents/         the reference dataset: 42 DOCX files
│   ├── CCTNS/        (6)         7 systems x 6 variants
│   ├── CityMapper/   (6)           <system>_requirements_FINAL_clean_<variant>-Reference.docx
│   ├── Emial/        (6)           variants: MIRC1-3, Simple1-3
│   ├── Inventory/    (6)
│   ├── MDOT/         (6)
│   ├── QuickEats/    (6)
│   └── WebStore/     (6)
├── reference_targets/           plain-text extract used as the validation oracle
│   └── reference_MDOT.txt          (MDOT-Simple2, FR-001 … FR-084)
└── MDOT_MDOT_simple2/
```

## The original test dataset

`source_documents/` holds the specifications under evaluation: **7 software-system cases ×
6 document variants = 42 documents**, the input corpus of the paper. These are the files the
pipeline reads (`--source`); stage 1 also stores the text it read in each sample folder as
`source/original_document.txt`.

The delivered dataset contains a second sub-folder per system (`Analysis/`, 42 further
DOCX files) which is **not** part of this repository: it is not an input to any step of the
method.

## The reference dataset

`reference_documents/` holds the enhanced reference specifications for the whole
evaluation: **7 software-system cases × 6 document variants = 42 documents**, matching the
42-document corpus of the paper. Each reference document is the original specification
plus the requirements added by the annotators, and it is the oracle that decides whether a
nomination is a genuinely missing obligation.

Both datasets are byte-identical copies of the delivered files (SHA-256 verified on
import). Folder names follow the original delivery, which is why the source folder is
`Email/` while the reference folder is `Emial/` (both contain `Email_*` files).

| Processed sample | Source document | Reference document |
|---|---|---|
| `samples/MDOT_MDOT_simple2/` | `source_documents/MDOT/filtered_MDOT_simple2_doc.docx` | `reference_documents/MDOT/MDOT_requirements_FINAL_clean_Simple2-Reference.docx` |

The other 41 document pairs are published so the dataset can be reused for the remaining
variants of the corpus.

```bash
# rerun stage 1 on any of the 42 documents straight from the repository
python core/run_stage_source.py --doc-id Email_MIRC2 \
    --source samples/source_documents/Email/filtered_Email_MIRC2_doc.docx \
    --out-root samples
```


## Per-document folder contract

```
samples/<DOC_ID>/
├── stage1_summary.json         counts, timings, model version of stage 1
├── source/                     original_document.txt, frs.json, elements.json,
│                               relations.json, simulation_exclusions.json
│                               (plus name_collisions.json where relevant)
├── graph/                      causal_graph.{png,json}, evidence_graph.graphml + .dot,
│                               simulation_graph.graphml + .dot, causal_graph_summary.md
├── RQ1/                        causalreq_supplements_only.txt, causalreq_complete_document.txt,
│                               manifest.json, 00_original_document.txt
├── RQ2/                        fixed_pool.json, ACE_review.csv, Reachability_review.csv,
│                               Random_review.csv, manifest.json, original_document.txt
├── RQ3/<variant>/              nominations.json, supplements.json,
│                               run_settings.json, manifest.json
└── RESULTS.md                  single-document report (sections 1-6)
```

The five `RQ3/<variant>/` folders are `Full`, `NoSignedPropagation`, `NoIsolatedReview`,
`NoOperationReview` and `NoFullDocumentValidation`.

`RQ2/fixed_pool.json` records, for every candidate, the computed effect (`ace`, `p_do_1`,
`p_do_0`), the reachability count, and the interpretation aids of Section 3.3 of the paper:
`shared_upstream` (upstream elements that reach the target without passing through the
source, each with both paths), `p_observed_1` (the target's probability given that the
source is observed active), and `association_gap` (that conditional probability minus
`p_do_1`). None of these three fields enters the pool selection or the rankings.

## What the samples contain

| Document | FR blocks | Elements (active) | Relations | Simulation graph | Pool | RQ3 variants |
|---|---:|---:|---:|---:|---:|---:|
| MDOT_MDOT_simple2 | 8 | 50 (45) | 56 | 45 n / 14 e | 20 | 5 |

## Reading a sample

```bash
# the headline record of one document
less samples/MDOT_MDOT_simple2/RESULTS.md

# the fixed candidate pool and the three rankings
column -s, -t < samples/MDOT_MDOT_simple2/RQ2/fixed_pool.json

# one nomination end to end (question, evidence FRs, FR-by-FR screenings, verdict, draft)
python - <<'PY'
import json, pathlib
p = pathlib.Path("samples/MDOT_MDOT_simple2/RQ3/Full/nominations.json")
n = json.loads(p.read_text(encoding="utf-8"))[0]
print(n["nomination_id"], n["origin"], n["preliminary_outcome"])
print("question:", n["question"])
print("screened FRs:", len(n["checked_fr_ids"]))
PY
```

## Source specifications

The DOCX specifications are not redistributed. The text as read by the pipeline is
preserved in every sample folder as `source/original_document.txt`, so the validation data
is self-contained. To re-run stage 1 on a document:

```bash
python core/run_stage_source.py --doc-id MDOT_MDOT_simple2 \
    --source /path/to/filtered_MDOT_simple2_doc.docx --out-root samples
```

## Note on the LLM screening cache

`cache/validation/` is excluded from the repository: it is a scheduling aid keyed by (document, model, question, draft) and is regenerated on demand.
Measured hit rate across concurrently running variants was 0, because the model does not
reproduce identical nomination wording across runs.
