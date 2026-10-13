# -*- coding: utf-8 -*-
"""The one documented prompt clarification, isolated so it can be imported.

The shipped ELEMENT_PROMPT tells the model to leave active_meaning empty "if
undefined"; both deepseek-v4-pro and deepseek-flash then leave it empty for every
element (0/16 in a controlled probe), which empties the simulation graph. Adding
the clause below raises the fill rate to 16/16 (see diagnose_active_meaning.py).
"""
ACTIVE_CLAUSE = """
IMPORTANT: for every element you MUST fill active_meaning with a concrete
scenario-level statement of what "active = 1" means for THIS document,
e.g. "the snapshot has been published successfully". Only leave it empty
if the element is an ACTOR. Prefer elements whose active state the
document actually determines (STATE, EVENT, CONSTRAINT, FUNCTION).
"""

# loaded from prompts/rq1/patch_active_meaning.txt (the literal above is the fallback)
try:
    from prompt_store import load as _load
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
    from prompt_store import load as _load
ACTIVE_CLAUSE = _load("rq1/patch_active_meaning", ACTIVE_CLAUSE)


def patch(module):
    """Append the clause to the module-level ELEMENT_PROMPT (idempotent)."""
    if ACTIVE_CLAUSE.strip() not in module.ELEMENT_PROMPT:
        module.ELEMENT_PROMPT = module.ELEMENT_PROMPT + ACTIVE_CLAUSE
    return module.ELEMENT_PROMPT
