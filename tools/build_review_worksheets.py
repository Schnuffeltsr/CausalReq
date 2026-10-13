# -*- coding: utf-8 -*-
"""Build review worksheets that also shortlist the matching reference FRs.

For every nomination the worksheet lists the three most similar requirements of
the enhanced reference document, so the reviewer can decide "already covered /
genuinely missing / unsupported" without re-reading the whole reference.

Usage: python build_review_worksheets2.py <out_root> <doc_id> <reference_txt>
"""
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "Inventory_MIRC3"
REF_TXT = Path(sys.argv[3]) if len(sys.argv) > 3 else BASE / "reference_Inventory.txt"

root = OUT_ROOT / DOC_ID
review = root / "review"
review.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------- reference split ----
raw = REF_TXT.read_text(encoding="utf-8")
lines = [re.sub(r"^\[P\|[^\]]+\]\s*", "", ln) for ln in raw.splitlines()]
lines = [ln for ln in lines if ln.strip()]
HEAD = re.compile(r"^(FR-\d+|\d+\.\d+)\s+(.*)$")

sections = []
current = None
for line in lines:
    m = HEAD.match(line)
    if m and not line.lower().startswith("description"):
        if current:
            sections.append(current)
        current = {"id": m.group(1), "title": m.group(2).strip(), "body": []}
    elif current is not None:
        current["body"].append(line)
if current:
    sections.append(current)
for s in sections:
    s["text"] = (s["title"] + " " + " ".join(s["body"])).strip()
print(f"reference sections: {len(sections)}")
for s in sections[:3]:
    print("  ", s["id"], s["title"][:70])

STOP = set("the a an of to and or in for on with be is are shall must not no by "
           "that this it its as at from any all each when if then than which who "
           "system user users customer can may should will would".split())


def tokens(text):
    return [w for w in re.findall(r"[a-z0-9]+", (text or "").lower())
            if w not in STOP and len(w) > 2]


# tf-idf over reference sections
df = Counter()
section_tokens = []
for s in sections:
    tk = tokens(s["text"])
    section_tokens.append(tk)
    for w in set(tk):
        df[w] += 1
N = max(len(sections), 1)
idf = {w: math.log((N + 1) / (c + 1)) + 1 for w, c in df.items()}


def vec(tk):
    tf = Counter(tk)
    v = {w: (1 + math.log(c)) * idf.get(w, 1.0) for w, c in tf.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {w: x / norm for w, x in v.items()}


section_vecs = [vec(tk) for tk in section_tokens]


def top_matches(text, k=3):
    v = vec(tokens(text))
    scored = []
    for s, sv in zip(sections, section_vecs):
        score = sum(x * sv.get(w, 0.0) for w, x in v.items())
        scored.append((score, s))
    scored.sort(key=lambda x: -x[0])
    return scored[:k]


def clip(text, n):
    text = re.sub(r"\s+", " ", (text or "").strip())
    return text if len(text) <= n else text[:n] + "…"


pool = json.loads((root / "RQ2" / "fixed_pool.json").read_text(encoding="utf-8"))


def load(variant):
    d = root / "RQ3" / variant
    noms = json.loads((d / "nominations.json").read_text(encoding="utf-8"))
    sups = json.loads((d / "supplements.json").read_text(encoding="utf-8"))
    return noms, sups


full_noms, full_sups = load("Full")
by_id = {n["nomination_id"]: n for n in full_noms}


def ref_block(text):
    out = []
    for score, s in top_matches(text):
        out.append(f"      ref {s['id']} (sim {score:.2f}) {clip(s['title'], 70)}"
                   f"\n         {clip(s['text'], 240)}")
    return "\n".join(out)


# ------------------------------------------------------------------ RQ2 ----
lines_out = [f"# RQ2 fixed pool — {DOC_ID} (20 candidates + reference shortlist)\n"]
for rank, item in enumerate(sorted(pool, key=lambda x: -abs(x["ace"])), 1):
    nom = by_id.get(item["candidate_id"], {})
    text = f"{nom.get('question','')} {nom.get('draft_obligation','')}"
    lines_out.append(
        f"\n[{rank:2d}] {item['candidate_id']} ACE={item['ace']:+.4f} reach={item['reachability']}"
        f"\n   source: {item['source']}\n   target: {item['target']}"
        f"\n   question: {clip(nom.get('question'), 200)}"
        f"\n   draft: {clip(nom.get('draft_obligation'), 240)}"
        f"\n   evidence FRs: {', '.join(nom.get('evidence_fr_ids', []))}"
        f"\n   reference shortlist:\n{ref_block(text)}")
(review / "w_rq2.txt").write_text("".join(lines_out), encoding="utf-8")

# ----------------------------------------------------------------- Full ----
out = [f"# RQ3 Full — {DOC_ID} ({len(full_noms)} nominations + reference shortlist)\n"]
for n in full_noms:
    text = f"{n.get('question','')} {n.get('draft_obligation','')} {n.get('subject','')}"
    out.append(
        f"\n{n['nomination_id']} [{n['origin']}] model={n.get('preliminary_outcome')}"
        f"\n   subject: {clip(n.get('subject'), 110)}"
        f"\n   question: {clip(n.get('question'), 220)}"
        f"\n   draft: {clip(n.get('draft_obligation'), 280)}"
        f"\n   evidence FRs: {', '.join(n.get('evidence_fr_ids', []))}"
        f"\n   reference shortlist:\n{ref_block(text)}")
(review / "w_full.txt").write_text("".join(out), encoding="utf-8")

# ---------------------------------------------------------- variant diff ----
from difflib import SequenceMatcher  # noqa: E402


def norm(t):
    return re.sub(r"[^a-z0-9 ]+", " ", (t or "").lower())


VARIANTS = ["NoSignedPropagation", "NoIsolatedReview", "NoOperationReview",
            "NoFullDocumentValidation"]
full_keys = [(n["nomination_id"], norm(n.get("draft_obligation")),
              norm(n.get("subject")), norm(n.get("question"))) for n in full_noms]
mapping = {}
diff = []
for variant in VARIANTS:
    try:
        noms, _ = load(variant)
    except FileNotFoundError:
        diff.append(f"\n## {variant}: not run\n")
        continue
    new_items = []
    for n in noms:
        d = norm(n.get("draft_obligation"))
        best_id, best = None, 0.0
        for fid, fd, fs, fq in full_keys:
            score = max(
                SequenceMatcher(None, d, fd).ratio() if d and fd else 0.0,
                SequenceMatcher(None, norm(n.get("question")), fq).ratio(),
                SequenceMatcher(None, norm(n.get("subject")), fs).ratio() * 0.9)
            if score > best:
                best_id, best = fid, score
        mapping[f"{variant}|{n['nomination_id']}"] = {
            "matched_full": best_id if best >= 0.70 else None,
            "score": round(best, 3), "origin": n["origin"],
            "model_outcome": n.get("preliminary_outcome")}
        if best < 0.70:
            new_items.append((n, best, best_id))
    diff.append(f"\n\n## {variant}: {len(noms)} nominations, {len(new_items)} new vs Full\n")
    for n, score, best_id in new_items:
        text = f"{n.get('question','')} {n.get('draft_obligation','')}"
        diff.append(
            f"\n{n['nomination_id']} [{n['origin']}] model={n.get('preliminary_outcome')} "
            f"best_full={best_id} sim={score:.2f}"
            f"\n   subject: {clip(n.get('subject'), 110)}"
            f"\n   question: {clip(n.get('question'), 200)}"
            f"\n   draft: {clip(n.get('draft_obligation'), 260)}"
            f"\n   evidence FRs: {', '.join(n.get('evidence_fr_ids', []))}"
            f"\n   reference shortlist:\n{ref_block(text)}")
(review / "w_diff.txt").write_text("".join(diff), encoding="utf-8")
(review / "w_map.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=1),
                                   encoding="utf-8")

for name in ("w_rq2.txt", "w_full.txt", "w_diff.txt"):
    print(f"  {name}: {(review / name).stat().st_size} bytes")
