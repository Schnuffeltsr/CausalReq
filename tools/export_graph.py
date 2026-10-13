# -*- coding: utf-8 -*-
"""Export the CausalReq causal graphs (evidence + signed simulation) to disk.

Reads the artefacts written by causalreq_experiment.py and produces:
  causal_graph.json          machine-readable nodes/edges/exclusions
  evidence_graph.graphml     evidence graph (all extracted relations)
  simulation_graph.graphml   signed simulation graph actually used for ACE
  causal_graph.dot           Graphviz source for both graphs
  causal_graph.png           rendered overview (evidence | simulation)
  causal_graph_summary.md    human-readable summary
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "core"))
import causalreq_experiment as M  # noqa: E402

OUT_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "samples"
DOC_ID = sys.argv[2] if len(sys.argv) > 2 else "MDOT_MDOT_simple2"
SRC = OUT_ROOT / DOC_ID / "source"
OUT = OUT_ROOT / DOC_ID / "graph"
OUT.mkdir(parents=True, exist_ok=True)

elements = json.loads((SRC / "elements.json").read_text(encoding="utf-8"))
relations = json.loads((SRC / "relations.json").read_text(encoding="utf-8"))
exclusions_path = SRC / "simulation_exclusions.json"
exclusions = (
    json.loads(exclusions_path.read_text(encoding="utf-8"))
    if exclusions_path.exists() else []
)

model = M.CausalModel(elements, relations)
ev = model.evidence_graph
sim = model.simulation_graph

print(f"elements={len(elements)} relations={len(relations)}")
print(f"evidence graph: {ev.number_of_nodes()} nodes / {ev.number_of_edges()} edges")
print(f"simulation graph: {sim.number_of_nodes()} nodes / {sim.number_of_edges()} edges")
print(f"exclusions: {len(model.exclusions)}")

# ---------------------------------------------------------------- JSON ----
def node_payload(graph):
    out = []
    for name, data in graph.nodes(data=True):
        out.append({
            "name": name,
            "type": data.get("type", ""),
            "active_meaning": data.get("active_meaning", ""),
            "confidence": data.get("confidence"),
            "evidence": data.get("evidence", []),
            "in_simulation": name in sim,
            "simulation_variable": model.name_to_variable.get(name),
        })
    return out


def edge_payload(graph, signed):
    out = []
    if signed:
        for u, v, data in graph.edges(data=True):
            out.append({
                "source": u, "target": v,
                "sign": data.get("sign"),
                "direction": data.get("direction"),
                "weight": data.get("weight"),
                "relation_ids": data.get("relation_ids", []),
            })
    else:
        for u, v, key, data in graph.edges(keys=True, data=True):
            out.append({
                "source": u, "target": v,
                "relation_id": data.get("relation_id"),
                "relation_type": data.get("relation_type"),
                "propagation_sign": data.get("propagation_sign"),
                "confidence": data.get("confidence"),
                "reason": data.get("reason", ""),
                "source_fr_id": data.get("source_fr_id"),
                "target_fr_id": data.get("target_fr_id"),
                "source_quote": data.get("source_quote"),
                "target_quote": data.get("target_quote"),
            })
    return out


payload = {
    "doc_id": DOC_ID,
    "model_version": model.model_version,
    "settings": {
        "background_log_odds": M.BACKGROUND_LOG_ODDS,
        "propagation_strength": M.PROPAGATION_STRENGTH,
        "max_parents": M.MAX_PARENTS,
    },
    "counts": {
        "elements": len(elements),
        "relations": len(relations),
        "evidence_nodes": ev.number_of_nodes(),
        "evidence_edges": ev.number_of_edges(),
        "simulation_nodes": sim.number_of_nodes(),
        "simulation_edges": sim.number_of_edges(),
        "exclusions": len(model.exclusions),
    },
    "evidence_nodes": node_payload(ev),
    "evidence_edges": edge_payload(ev, signed=False),
    "simulation_nodes": node_payload(sim),
    "simulation_edges": edge_payload(sim, signed=True),
    "exclusions": model.exclusions,
}
(OUT / "causal_graph.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

# ------------------------------------------------------------- GraphML ----
def to_graphml(graph, path, multigraph):
    import networkx as nx

    g = nx.MultiDiGraph() if multigraph else nx.DiGraph()
    for name, data in graph.nodes(data=True):
        g.add_node(name, type=str(data.get("type", "")),
                   confidence=str(data.get("confidence", "")),
                   active_meaning=str(data.get("active_meaning", ""))[:400])
    if multigraph:
        for u, v, key, data in graph.edges(keys=True, data=True):
            g.add_edge(u, v, key=str(key),
                       relation_type=str(data.get("relation_type", "")),
                       sign=str(data.get("propagation_sign", "")),
                       confidence=str(data.get("confidence", "")))
    else:
        for u, v, data in graph.edges(data=True):
            g.add_edge(u, v, sign=str(data.get("sign", "")),
                       direction=str(data.get("direction", "")),
                       weight=str(data.get("weight", "")))
    nx.write_graphml(g, path)


to_graphml(ev, OUT / "evidence_graph.graphml", multigraph=True)
to_graphml(sim, OUT / "simulation_graph.graphml", multigraph=False)

# ----------------------------------------------------------------- DOT ----
def esc(text):
    return str(text).replace('"', "'")


lines = ["digraph evidence_graph {", '  rankdir=LR;', '  node [shape=box, fontsize=10];']
for name, data in ev.nodes(data=True):
    lines.append(f'  "{esc(name)}" [label="{esc(name)}\\n({data.get("type","")})"];')
for u, v, key, data in ev.edges(keys=True, data=True):
    sign = data.get("propagation_sign", "?")
    lines.append(
        f'  "{esc(u)}" -> "{esc(v)}" [label="{data.get("relation_type","")}/{sign}"];')
lines.append("}")
(OUT / "evidence_graph.dot").write_text("\n".join(lines), encoding="utf-8")

lines = ["digraph simulation_graph {", '  rankdir=LR;', '  node [shape=box, fontsize=10];']
for name in sim.nodes():
    lines.append(f'  "{esc(name)}";')
for u, v, data in sim.edges(data=True):
    color = "green" if data.get("sign") == 1 else "red"
    lines.append(
        f'  "{esc(u)}" -> "{esc(v)}" [color={color}, '
        f'label="{data.get("direction","")} {data.get("weight",0):.2f}"];')
lines.append("}")
(OUT / "simulation_graph.dot").write_text("\n".join(lines), encoding="utf-8")

# ----------------------------------------------------------------- PNG ----
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import networkx as nx

    fig, axes = plt.subplots(1, 2, figsize=(22, 10))

    type_colors = {
        "FUNCTION": "#4C72B0", "DATA": "#DD8452", "ACTOR": "#55A868",
        "CONSTRAINT": "#C44E52", "STATE": "#8172B3", "EVENT": "#937860",
    }

    ax = axes[0]
    ax.set_title(f"Evidence graph — {ev.number_of_nodes()} nodes / "
                 f"{ev.number_of_edges()} relations", fontsize=13)
    pos = nx.spring_layout(ev, k=1.1, seed=7)
    colors = [type_colors.get(ev.nodes[n].get("type"), "#999999") for n in ev.nodes()]
    nx.draw_networkx_edges(ev, pos, ax=ax, arrows=True, alpha=0.35,
                           connectionstyle="arc3,rad=0.08")
    nx.draw_networkx_nodes(ev, pos, ax=ax, node_color=colors, node_size=1400,
                           alpha=0.9, linewidths=0.5, edgecolors="white")
    nx.draw_networkx_labels(ev, pos, ax=ax, font_size=6,
                            labels={n: (n[:26] + "…" if len(n) > 27 else n)
                                    for n in ev.nodes()})
    ax.axis("off")

    ax = axes[1]
    if sim.number_of_nodes() == 0:
        ax.set_title("Signed simulation graph — EMPTY\n"
                     "(no element has a defined active state)", fontsize=13)
        ax.text(0.5, 0.5, "0 simulation variables\nACE / RQ2 pool cannot be built",
                ha="center", va="center", fontsize=14, color="#B00020")
        ax.axis("off")
    else:
        ax.set_title(f"Signed simulation graph — {sim.number_of_nodes()} nodes / "
                     f"{sim.number_of_edges()} edges", fontsize=13)
        pos2 = nx.spring_layout(sim, k=1.1, seed=7)
        colors2 = [type_colors.get(sim.nodes[n].get("type"), "#999999") for n in sim.nodes()]
        pos_edges = [(u, v) for u, v, d in sim.edges(data=True) if d.get("sign") == 1]
        neg_edges = [(u, v) for u, v, d in sim.edges(data=True) if d.get("sign") != 1]
        nx.draw_networkx_edges(sim, pos2, edgelist=pos_edges, ax=ax, edge_color="#2E7D32",
                               arrows=True, width=1.6, connectionstyle="arc3,rad=0.08")
        nx.draw_networkx_edges(sim, pos2, edgelist=neg_edges, ax=ax, edge_color="#C62828",
                               arrows=True, width=1.6, style="dashed",
                               connectionstyle="arc3,rad=0.08")
        nx.draw_networkx_nodes(sim, pos2, ax=ax, node_color=colors2, node_size=1400,
                               alpha=0.9, linewidths=0.5, edgecolors="white")
        nx.draw_networkx_labels(sim, pos2, ax=ax, font_size=6,
                                labels={n: (n[:26] + "…" if len(n) > 27 else n)
                                        for n in sim.nodes()})
        ax.axis("off")

    handles = [plt.Line2D([], [], color=c, marker="o", linestyle="",
                          label=t) for t, c in type_colors.items()]
    fig.legend(handles=handles, loc="lower center", ncol=6, fontsize=11, frameon=False)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUT / "causal_graph.png", dpi=150)
    print("png written")
except Exception as exc:  # noqa: BLE001
    print("png export skipped:", type(exc).__name__, exc)

# ------------------------------------------------------------- summary ----
pool_path = OUT_ROOT / DOC_ID / "RQ2" / "fixed_pool.json"
pool = json.loads(pool_path.read_text(encoding="utf-8")) if pool_path.exists() else []

lines = [
    f"# Causal graph export — {DOC_ID}\n",
    f"\n- model version: `{model.model_version}`",
    f"\n- elements: {len(elements)} | extracted relations: {len(relations)}",
    f"\n- evidence graph: {ev.number_of_nodes()} nodes, {ev.number_of_edges()} edges (multi-edge, keeps every quotations)",
    f"\n- signed simulation graph: {sim.number_of_nodes()} nodes, {sim.number_of_edges()} edges",
    f"\n- excluded from simulation: {len(model.exclusions)}",
    f"\n- parameters: background log-odds {M.BACKGROUND_LOG_ODDS}, propagation strength {M.PROPAGATION_STRENGTH}, max parents {M.MAX_PARENTS}\n",
]

if sim.number_of_nodes() == 0:
    lines.append(
        "\n> **模拟图为空**：本次抽取的 "
        f"{sum(1 for e in elements if not (e.get('active_meaning') or '').strip())}"
        f"/{len(elements)} 个元素的 `active_meaning` 为空，"
        "因此没有任何变量进入模拟图，ACE 与 RQ2 固定候选池无法构建。\n"
        "> 证据图与关系表完整可用；模型/提示词需要保证至少部分元素具有"
        "可定义的二值激活语义后才能继续 RQ2/RQ3。\n")

lines += [
    "\n## Simulation edges\n",
]
if sim.number_of_edges():
    lines += ["\n| source | → | target | sign | weight |", "\n|---|---|---|---:|---:|"]
    for u, v, d in sorted(sim.edges(data=True), key=lambda e: (-e[2]["weight"], e[0])):
        lines.append(f"\n| {u} | → | {v} | {d['direction']} | {d['weight']:.2f} |")
else:
    lines.append("(none — no element has a defined activation state)\n")

lines.append("\n\n## Exclusions\n")
if model.exclusions:
    lines.append("\n| source | target | reason |")
    lines.append("\n|---|---|---|")
    for item in model.exclusions:
        lines.append(f"\n| {item['source']} | {item['target']} | {item['reason']} |")
else:
    lines.append("\n(none)\n")

if pool:
    lines.append("\n\n## Fixed RQ2 pool (top 10 by |ACE|)\n")
    lines.append("\n| candidate | source | target | ACE | p(do=1) | p(do=0) | reachability |")
    lines.append("\n|---|---|---|---:|---:|---:|---:|")
    for item in sorted(pool, key=lambda x: -abs(x["ace"]))[:10]:
        lines.append(
            f"\n| {item['candidate_id']} | {item['source']} | {item['target']} | "
            f"{item['ace']:.3f} | {item['p_do_1']:.3f} | {item['p_do_0']:.3f} | "
            f"{item['reachability']} |")

(OUT / "causal_graph_summary.md").write_text("".join(lines), encoding="utf-8")
print("written to", OUT)
