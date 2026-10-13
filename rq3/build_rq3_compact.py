# -*- coding: utf-8 -*-
"""Compact RQ3 worksheet for the simulated human review.

One block per nomination: identity, route, model verdict, the question/draft, the
evidence FRs, and the two most similar reference requirements (id + title + the
first 170 characters of the reference body). Small enough to review in one pass.
"""
import json
import math
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "Inventory_MIRC3"
REF_TXT = Path(sys.argv[3]) if len(sys.argv) > 3 else BASE / "reference_Inventory.txt"

root = OUT_ROOT / DOC_ID
review = root / "review"
review.mkdir(parents=True, exist_ok=True)

raw = REF_TXT.read_text(encoding="utf-8")
lines = [re.sub(r"^\[P\|[^\]]+\]\s*", "", ln) for ln in raw.splitlines()]
lines = [ln for ln in lines if ln.strip()]
HEAD = re.compile(r"^(FR-\d+|\d+\.\d+)\s+(.*)$")
sections, current = [], None
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

STOP = set("the a an of to and or in for on with be is are shall must not no by that "
           "this it its as at from any all each when if then than which who system user "
           "users customer can may should will would".split())


def toks(t):
    return [w for w in re.findall(r"[a-z0-9]+", (t or "").lower())
            if w not in STOP and len(w) > 2]


df = Counter()
sts = []
for s in sections:
    tk = toks(s["text"])
    sts.append(tk)
    for w in set(tk):
        df[w] += 1
N = max(len(sections), 1)
idf = {w: math.log((N + 1) / (c + 1)) + 1 for w, c in df.items()}


def vec(tk):
    tf = Counter(tk)
    v = {w: (1 + math.log(c)) * idf.get(w, 1.0) for w, c in tf.items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {w: x / n for w, x in v.items()}


svs = [vec(tk) for tk in sts]


def clip(t, n):
    t = re.sub(r"\s+", " ", (t or "").strip())
    return t if len(t) <= n else t[:n] + "…"


def refs(text, k=2):
    v = vec(toks(text))
    scored = sorted(((sum(x * sv.get(w, 0.0) for w, x in v.items()), s)
                     for s, sv in zip(sections, svs)), key=lambda x: -x[0])
    return " || ".join(f"{s['id']} ({sc:.2f}) {clip(s['title'], 55)} :: {clip(s['text'], 170)}"
                       for sc, s in scored[:k])


def load(variant):
    d = root / "RQ3" / variant
    return (json.loads((d / "nominations.json").read_text(encoding="utf-8")),
            json.loads((d / "supplements.json").read_text(encoding="utf-8")))


full_noms, full_sups = load("Full")

out = [f"# RQ3 compact worksheet — {DOC_ID}\n",
       f"\nFull: {len(full_noms)} nominations. 每行格式：\n",
       "ID | route | model | subject | question | draft | evidence FRs | reference(top2)\n"]
for n in full_noms:
    text = f"{n.get('question','')} {n.get('draft_obligation','')} {n.get('subject','')}"
    out.append(
        f"\n{n['nomination_id']} | {n['origin']} | {n.get('preliminary_outcome')}\n"
        f"  subj: {clip(n.get('subject'), 80)}\n"
        f"  q:    {clip(n.get('question'), 150)}\n"
        f"  draft:{clip(n.get('draft_obligation'), 200)}\n"
        f"  ev:   {', '.join(n.get('evidence_fr_ids', []))}\n"
        f"  ref:  {refs(text)}\n")
(review / "rq3_full_compact.txt").write_text("".join(out), encoding="utf-8")

# ---- variant diffs -------------------------------------------------------
def norm(t):
    return re.sub(r"[^a-z0-9 ]+", " ", (t or "").lower())


VARIANTS = ["NoSignedPropagation", "NoIsolatedReview", "NoOperationReview",
            "NoFullDocumentValidation"]
full_keys = [(n["nomination_id"], norm(n.get("draft_obligation")),
              norm(n.get("subject")), norm(n.get("question"))) for n in full_noms]
mapping = {}
diff = ["\n# 消融版相对 Full 的新增条目\n"]
for variant in VARIANTS:
    try:
        noms, sups = load(variant)
    except FileNotFoundError:
        diff.append(f"\n## {variant}: not run\n")
        continue
    new_items = []
    for n in noms:
        d = norm(n.get("draft_obligation"))
        best_id, best = None, 0.0
        for fid, fd, fs, fq in full_keys:
            sc = max(SequenceMatcher(None, d, fd).ratio() if d and fd else 0.0,
                     SequenceMatcher(None, norm(n.get("question")), fq).ratio(),
                     SequenceMatcher(None, norm(n.get("subject")), fs).ratio() * 0.9)
            if sc > best:
                best_id, best = fid, sc
        mapping[f"{variant}|{n['nomination_id']}"] = {
            "matched_full": best_id if best >= 0.70 else None,
            "score": round(best, 3), "origin": n["origin"],
            "model_outcome": n.get("preliminary_outcome")}
        if best < 0.70:
            new_items.append((n, best, best_id))
    diff.append(f"\n\n## {variant}: {len(noms)} nominations, {len(new_items)} new vs Full\n")
    for n, sc, bid in new_items:
        text = f"{n.get('question','')} {n.get('draft_obligation','')}"
        diff.append(
            f"\n{n['nomination_id']} | {n['origin']} | {n.get('preliminary_outcome')} "
            f"| best_full={bid} sim={sc:.2f}\n"
            f"  subj: {clip(n.get('subject'), 80)}\n"
            f"  q:    {clip(n.get('question'), 150)}\n"
            f"  draft:{clip(n.get('draft_obligation'), 200)}\n"
            f"  ev:   {', '.join(n.get('evidence_fr_ids', []))}\n"
            f"  ref:  {refs(text)}\n")
(review / "rq3_diff_compact.txt").write_text("".join(diff), encoding="utf-8")
(review / "w_map.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=1),
                                   encoding="utf-8")

for name in ("rq3_full_compact.txt", "rq3_diff_compact.txt"):
    print(f"  {name}: {(review / name).stat().st_size} bytes")
