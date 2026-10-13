# prompts — the prompt templates

Every prompt the pipeline sends to the model is stored here as one UTF-8 text file, so a
reviewer can read and edit the wording without touching the code.

```python
# core/prompt_store.py
PROMPT_ROOT = Path(__file__).resolve().parents[1] / "prompts"

def load(relpath, default):      # e.g. load("rq1/nomination_dependency", DEPENDENCY_PROMPT)
    ...                          # missing file -> the built-in default is used
```

`core/causalreq_experiment.py`, `core/active_fix.py` and `core/element_fix.py` each keep
their string literal as a fallback and then rebind the name through `prompt_store.load`,
so the pipeline runs whether or not the files are present. The loaded text is
byte-identical to the literal it replaces (verified by SHA-256 when the files were
created); **leading and trailing newlines are part of a template**, so do not reflow a file.

## `rq1/` — the completion prompts

These produce and filter the completed requirement set that RQ1 evaluates. Their output is
also what RQ2 ranks (the dependency question of the fixed pool) and what RQ3 ablates (the
three routes and the validation stage), which is why the folder is named after the
end-to-end question they serve.

| File | Code constant | Stage | Called at |
|---|---|---|---|
| `nomination_dependency.txt` | `DEPENDENCY_PROMPT` | dependency-scenario probe for one pool candidate | `generate_nominations()` |
| `nomination_complement.txt` | `COMPLEMENT_PROMPT` | isolated-element and operation-coverage review | `generate_nominations()` |
| `validation_screen.txt` | `SCREEN_PROMPT` | screens one nomination against **one** original FR (coverage and out-of-scope evidence) | `preliminarily_validate()` |
| `validation_final.txt` | `FINAL_SCREEN_PROMPT` | final disposition: retained / covered / unsupported / out_of_scope / unresolved, plus the drafted supplement | `preliminarily_validate()` |
| `patch_active_meaning.txt` | `active_fix.ACTIVE_CLAUSE` | appended to the element prompt; requires a non-empty `active_meaning` | `active_fix.patch()` |
| `patch_unique_element_names.txt` | `element_fix.UNIQUE_CLAUSE` | appended to the element prompt; requires globally unique element names | `run_stage_source.py` |

The prompt that was patched is `shared/element_extraction.txt`: `patch_active_meaning.txt`
is appended on every run, and `patch_unique_element_names.txt` is appended unless the
runner is called with `--no-name-fix`.

## `shared/` — graph construction

Used before any research question, by every variant and every route.

| File | Code constant | Stage |
|---|---|---|
| `element_extraction.txt` | `ELEMENT_PROMPT` | per-FR extraction of typed elements (FUNCTION, DATA, ACTOR, CONSTRAINT, STATE, EVENT) with a verbatim quotation and an `active_meaning` |
| `relation_extraction.txt` | `RELATION_PROMPT` | extraction of typed, signed relations between elements, each with source/target quotations |

## Editing a template

1. Edit the `.txt` file (keep the surrounding blank lines).
2. Re-run the pipeline — no code change needed.
3. To confirm that a template still matches its fallback literal:

```bash
python - <<'PY'
import sys, hashlib
sys.path.insert(0, "core")
import causalreq_experiment as M, prompt_store
for name, rel in [("ELEMENT_PROMPT", "shared/element_extraction"),
                  ("RELATION_PROMPT", "shared/relation_extraction"),
                  ("DEPENDENCY_PROMPT", "rq1/nomination_dependency"),
                  ("COMPLEMENT_PROMPT", "rq1/nomination_complement"),
                  ("SCREEN_PROMPT", "rq1/validation_screen"),
                  ("FINAL_SCREEN_PROMPT", "rq1/validation_final")]:
    on_disk = (prompt_store.PROMPT_ROOT / f"{rel}.txt").read_text(encoding="utf-8")
    print(name, "matches file:", on_disk == getattr(M, name))
PY
```
