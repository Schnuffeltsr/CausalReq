# -*- coding: utf-8 -*-
"""Regenerate MANIFEST.md for the code/samples split layout."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parents[1]
SKIP = {".git", "__pycache__"}
CODE_DIRS = ["core", "rq1", "rq2", "rq3", "rq4", "tools"]


def files_under(path: Path):
    return sorted(f for f in path.rglob("*")
                  if f.is_file() and not SKIP & set(f.parts))


def mb(n):
    return f"{n/1024/1024:.1f} MB" if n >= 1024 * 1024 else f"{n/1024:.0f} KB"


lines = ["# Repository manifest",
         "",
         "CausalReq — causal dependency-guided requirement gap diagnosis and "
         "evidence-constrained completion.",
         "",
         "Executable code lives in `core/`, `rq1/`–`rq4/` and `tools/`; the case "
         "validation data used as reference samples lives in `samples/`.",
         "",
         "## Summary",
         "",
         "| Area | Files | Size |",
         "|---|---:|---:|"]

areas = [("top-level files", [f for f in REPO.iterdir() if f.is_file()])]
for d in CODE_DIRS:
    areas.append((f"{d}/ (code)", files_under(REPO / d)))
areas += [("docs/", files_under(REPO / "docs")),
          ("figures/", files_under(REPO / "figures")),
          ("samples/ (case data)", files_under(REPO / "samples"))]

total_n = total_b = 0
for label, files in areas:
    size = sum(f.stat().st_size for f in files)
    total_n += len(files)
    total_b += size
    lines.append(f"| `{label}` | {len(files)} | {mb(size)} |")
lines += [f"| **total** | **{total_n}** | **{mb(total_b)}** |", ""]

lines += ["## Executable code", ""]
for folder in CODE_DIRS:
    files = [f for f in files_under(REPO / folder) if f.suffix == ".py"]
    legacy = [f for f in files if "legacy" in f.parts]
    lines += [f"**{folder}/** — {len(files)} Python files"
              + (f" (incl. {len(legacy)} kept-as-shipped)" if legacy else ""), ""]
    for f in files:
        lines.append(f"- `{f.relative_to(REPO).as_posix()}` — {mb(f.stat().st_size)}")
    lines.append("")

lines += ["**top-level files**", ""]
for f in sorted(f for f in REPO.iterdir() if f.is_file() and f.name != "MANIFEST.md"):
    lines.append(f"- `{f.name}` — {mb(f.stat().st_size)}")
lines.append("")

lines += ["## Documentation", ""]
for f in sorted(files_under(REPO / "docs")):
    lines.append(f"- `{f.relative_to(REPO).as_posix()}` — {mb(f.stat().st_size)}")
lines += ["", "## Figures", ""]
for f in sorted(files_under(REPO / "figures")):
    lines.append(f"- `figures/{f.name}` — {mb(f.stat().st_size)}")

lines += ["", "## Case validation data (reference samples)", ""]
ref = files_under(REPO / "samples" / "reference_targets")
lines += [f"**samples/reference_targets/** — {len(ref)} files, "
          f"{mb(sum(f.stat().st_size for f in ref))} "
          "(the validation oracle)", ""]
for f in ref:
    lines.append(f"- `{f.relative_to(REPO).as_posix()}` — {mb(f.stat().st_size)}")
lines.append("")
for doc in sorted(p for p in (REPO / "samples").iterdir() if p.is_dir()
                  and p.name != "reference_targets"):
    fs = files_under(doc)
    lines += [f"**samples/{doc.name}/** — {len(fs)} files, "
              f"{mb(sum(f.stat().st_size for f in fs))}", ""]
    groups = {}
    for f in fs:
        rel = f.relative_to(doc)
        groups.setdefault(rel.parts[0] if len(rel.parts) > 1 else "(root)", []).append(f)
    for key in sorted(groups):
        g = groups[key]
        lines.append(f"- `{key}` — {len(g)} files, {mb(sum(f.stat().st_size for f in g))}")
    lines.append("")

lines += ["## Deliberately excluded",
          "",
          "- **LLM screening cache** — 2,435 JSON files (~33 MB) under "
          "`samples/*/cache/`; a scheduling aid regenerated on demand.",
          "- **Run logs** — per-call traces (`*.log`, `*.err`, ~9 MB).",
          "- **API credentials** — scripts read `CAUSALREQ_API_KEY` from the environment; "
          "the one diagnostic helper that contained a literal key was not added to the "
          "repository.",
          "- **Source specifications (DOCX)** — not redistributed; the text as read by the "
          "pipeline is preserved in each sample folder as `source/original_document.txt`.",
          "",
          "## Pending decisions",
          "",
          "- `CITATION.cff` still carries placeholder authors and repository URL.",
          "- No `LICENSE` file yet — choose one before publishing.",
          "- Optionally add the DOCX specifications under `samples/documents/` with a "
          "redistribution note.",
          ""]

(REPO / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines[:26]))
