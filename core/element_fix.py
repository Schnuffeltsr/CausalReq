# -*- coding: utf-8 -*-
"""Name-collision resolution for element extraction (WebStore hit this).

The shipped extract_elements() raises
    ValueError: 跨类型出现同名元素，无法安全建图
whenever the model returns the same element name under two different types
(e.g. "Purchase History" as both DATA and FUNCTION). That check protects node
identity in the graph, but it aborts the whole document.

This module reimplements exactly that loop with one change: instead of raising,
a colliding name is disambiguated by appending its type ("Purchase History
(FUNCTION)"), so both elements survive and node identity stays unique. Every
rename is recorded for the audit trail. Nothing else (thresholds, quotation
check, merge rules) is modified.
"""
from __future__ import annotations

UNIQUE_CLAUSE = """
Element names MUST be unique across the whole document. If you would otherwise
use the same name for two elements of different types, make the names distinct
(e.g. "Purchase History" for DATA and "View Purchase History" for FUNCTION).
"""

# loaded from prompts/rq1/patch_unique_element_names.txt (the literal above is the fallback)
try:
    from prompt_store import load as _load
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
    from prompt_store import load as _load
UNIQUE_CLAUSE = _load("rq1/patch_unique_element_names", UNIQUE_CLAUSE)


def install(module):
    """Replace module.extract_elements with the collision-resolving version."""
    original = module.extract_elements

    def extract_elements_resolving(client, frs):
        merged: dict[tuple[str, str], dict] = {}

        for fr in frs:
            response = module.ask_json(client, module.ELEMENT_PROMPT, {"fr": fr})

            for raw in response.get("elements", []):
                if not isinstance(raw, dict):
                    continue

                name = str(raw.get("name", "")).strip()
                kind = str(raw.get("type", "")).upper().strip()
                quote = str(raw.get("quote", "")).strip()
                meaning = str(raw.get("active_meaning", "")).strip()

                try:
                    confidence = float(raw.get("confidence", 0))
                except (TypeError, ValueError):
                    continue

                if not (
                    name
                    and kind in module.ELEMENT_TYPES
                    and 0.75 <= confidence <= 1
                    and module.exact_quote(fr["text"], quote)
                ):
                    continue

                key = (name.casefold(), kind)
                evidence = {"fr_id": fr["fr_id"], "quote": quote}

                if key not in merged:
                    merged[key] = {
                        "name": name,
                        "type": kind,
                        "active_meaning": meaning,
                        "confidence": confidence,
                        "evidence": [evidence],
                    }
                else:
                    previous = merged[key]
                    previous["confidence"] = max(confidence, previous["confidence"])
                    if evidence not in previous["evidence"]:
                        previous["evidence"].append(evidence)
                    if (
                        meaning
                        and previous["active_meaning"]
                        and meaning != previous["active_meaning"]
                    ):
                        previous["active_meaning"] = ""
                        previous["activation_conflict"] = True

        result = list(merged.values())

        # ---- the one behavioural difference: resolve, do not abort ----
        by_name: dict[str, list[dict]] = {}
        for item in result:
            by_name.setdefault(item["name"], []).append(item)

        resolutions = []
        for name, items in by_name.items():
            if len(items) < 2:
                continue
            for item in sorted(items, key=lambda x: (-x["confidence"], x["type"])):
                new_name = f"{name} ({item['type']})"
                resolutions.append({
                    "original_name": name,
                    "resolved_name": new_name,
                    "type": item["type"],
                    "confidence": item["confidence"],
                })
                item["name"] = new_name
                item["name_collision_resolved"] = True

        if resolutions:
            module._LAST_NAME_RESOLUTIONS = resolutions

        return result

    module.extract_elements = extract_elements_resolving
    module._ORIGINAL_EXTRACT_ELEMENTS = original
    return module
