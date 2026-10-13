# -*- coding: utf-8 -*-
"""Load prompt templates from the repository's prompts/ directory.

Each template is stored as one UTF-8 text file (leading and trailing newlines are
part of the template). Loading is best-effort: when a file is missing the caller's
built-in default is used, so the pipeline always runs.
"""
from pathlib import Path

PROMPT_ROOT = Path(__file__).resolve().parents[1] / "prompts"


def load(relpath, default):
    """Return prompts/<relpath>.txt, or `default` when the file is absent."""
    path = PROMPT_ROOT / f"{relpath}.txt"
    if not path.exists():
        return default
    text = path.read_text(encoding="utf-8")
    return text if text.strip() else default
