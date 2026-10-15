#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CausalReq：依赖关系驱动的需求缺口诊断与证据约束补全（RQ1–RQ3 产物生成器）。

有效性判定与论文质量指标由评测环节完成，不由本脚本给出。

输入：
  Data/<case>/Document/*.docx

输出：
  out/<doc_id>/source/
  out/<doc_id>/RQ1/
  out/<doc_id>/RQ2/
  out/<doc_id>/RQ3/
  out/batch_manifest.json

依赖：
  pip install openai python-docx networkx pgmpy

环境变量：
  CAUSALREQ_API_KEY     your api key
  CAUSALREQ_BASE_URL    your url（可选；不设置则使用客户端默认地址）
  CAUSALREQ_MODEL       your model（可选；不设置则使用代码内置的默认模型）
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import os
import random
import re
import sys
import traceback
from collections import defaultdict
from pathlib import Path
from typing import Any

import networkx as nx
from docx import Document
from docx.document import Document as DocxDocument
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
from openai import OpenAI
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import DiscreteBayesianNetwork


# ============================================================
# 实验配置
# ============================================================

CASES = (
    "CityMapper",
    "Email",
    "Inventory",
    "MDOT",
    "QuickEats",
    "WebStore",
    "CCTNS",
)

VARIANTS = {
    "Full": {
        "signed_propagation": True,
        "isolated_review": True,
        "operation_review": True,
        "full_document_validation": True,
    },
    "NoSignedPropagation": {
        "signed_propagation": False,
        "isolated_review": True,
        "operation_review": True,
        "full_document_validation": True,
    },
    "NoIsolatedReview": {
        "signed_propagation": True,
        "isolated_review": False,
        "operation_review": True,
        "full_document_validation": True,
    },
    "NoOperationReview": {
        "signed_propagation": True,
        "isolated_review": True,
        "operation_review": False,
        "full_document_validation": True,
    },
    "NoFullDocumentValidation": {
        "signed_propagation": True,
        "isolated_review": True,
        "operation_review": True,
        "full_document_validation": False,
    },
}

ELEMENT_TYPES = {
    "FUNCTION", "DATA", "ACTOR",
    "CONSTRAINT", "STATE", "EVENT",
}

RELATION_TYPES = {
    "ENABLES", "TRIGGERS", "PREVENTS",
    "MODIFIES", "DEPENDS_ON", "CONTROLS", "PRODUCES",
}

VALIDATION_OUTCOMES = {
    "retained",
    "covered",
    "unsupported",
    "out_of_scope",
    "unresolved",
}

BACKGROUND_LOG_ODDS = -1.0
PROPAGATION_STRENGTH = 2.5
MAX_PARENTS = 8
POOL_SIZE = 20

# 全文验证的两处拦截，分开控制，默认只保留副作用小的那一处：
#
#   require_evidence（默认开）—— 引文级证据闸门。
#       covered / out_of_scope 必须有引文级逐段证据，retained 必须有补充需求
#       和证据 FR，否则该条目的去向记为 unresolved。它只改**标注**，不丢东西。
#
#   drop_non_retained（默认关）—— 淘汰闸门。
#       只输出 retained 的提名，其余全部丢弃。副作用最大（会把真实缺口一起丢掉），
#       因此默认关闭：默认配置下每条提名都会产出，并带上 disposition。
#
# 论文报告的评测使用两者都开（--enforce-validation）。
REQUIRE_EVIDENCE_DEFAULT = os.getenv(
    "CAUSALREQ_REQUIRE_EVIDENCE",
    "1",
).strip().lower() in {"1", "true", "yes", "on"}

DROP_NON_RETAINED_DEFAULT = os.getenv(
    "CAUSALREQ_DROP_NON_RETAINED",
    "",
).strip().lower() in {"1", "true", "yes", "on"}


# ============================================================
# 通用工具
# ============================================================

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, value: Any) -> None:
    write_text(
        path,
        json.dumps(value, ensure_ascii=False, indent=2),
    )


def write_csv(
    path: Path,
    columns: list[str],
    rows: list[dict],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=columns,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return prefix + "-" + hashlib.sha256(payload).hexdigest()[:12]


def stable_seed(seed: int, doc_id: str) -> int:
    payload = f"{seed}:{doc_id}".encode("utf-8")
    return int.from_bytes(
        hashlib.sha256(payload).digest()[:8],
        "big",
    )


def exact_quote(text: str, quote: str) -> bool:
    return bool(quote and quote.strip() in text)


def cleaned_filename(stem: str) -> str:
    stem = re.sub(r"^filtered_", "", stem, flags=re.I)
    stem = re.sub(r"_doc$", "", stem, flags=re.I)
    return stem


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def read_docx_in_order(path: Path) -> str:
    """
    按 DOCX 正文中的实际出现顺序读取段落与表格。
    表格每行用竖线连接单元格。
    """
    document: DocxDocument = Document(path)
    lines: list[str] = []

    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            paragraph = Paragraph(child, document)
            text = paragraph.text.strip()
            if text:
                lines.append(text)

        elif child.tag == qn("w:tbl"):
            table = Table(child, document)
            for row in table.rows:
                cells = [
                    cell.text.strip().replace("\n", " ")
                    for cell in row.cells
                ]
                if any(cells):
                    lines.append(" | ".join(cells))

    return "\n".join(lines)


def split_frs(text: str) -> list[dict]:
    """
    按源文档的六种常见编号格式切分。
    检测不到编号时直接报错，避免把整篇文档当一条 FR。
    """
    patterns = (
        r"(?m)^Function Requirement\s+\d+\b",
        r"(?m)^#{1,3}\s+\d+\.\d+\b",
        r"(?m)^\d+\.\d+\b",
        r"(?mi)^FR-\d+\b",
        r"(?mi)^F\d+\b",
        r"(?mi)^FR\s+\d+\s*:",
    )

    selected = None

    for pattern in patterns:
        if re.search(pattern, text):
            selected = pattern
            break

    if selected is None:
        raise ValueError(
            "未识别出 FR 编号；请检查 DOCX 提取结果和 split_frs()。"
        )

    starts = [match.start() for match in re.finditer(selected, text)]
    records = []

    for index, start in enumerate(starts):
        end = (
            starts[index + 1]
            if index + 1 < len(starts)
            else len(text)
        )
        block = text[start:end].strip()
        if block:
            records.append({
                "fr_id": f"FRBLOCK-{index + 1:03d}",
                "heading": block.splitlines()[0],
                "text": block,
            })

    return records


def get_client() -> OpenAI:
    key = os.getenv("CAUSALREQ_API_KEY")

    if not key:
        raise RuntimeError(
            "缺少 CAUSALREQ_API_KEY 环境变量。"
        )

    options: dict[str, Any] = {
        "api_key": key,
        "timeout": 120.0,
        "max_retries": 2,
    }

    base_url = os.getenv("CAUSALREQ_BASE_URL")

    if base_url:
        options["base_url"] = base_url

    return OpenAI(**options)


def ask_json(
    client: OpenAI,
    system_prompt: str,
    payload: dict,
) -> dict:
    response = client.chat.completions.create(
        model=os.getenv("CAUSALREQ_MODEL", "gpt-5.5"),
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": json.dumps(
                    payload,
                    ensure_ascii=False,
                ),
            },
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError("模型返回了空响应。")

    value = json.loads(content)

    if not isinstance(value, dict):
        raise ValueError("模型响应不是 JSON 对象。")

    return value


# ============================================================
# Stage 1：元素抽取
# ============================================================

ELEMENT_PROMPT = """
Extract document-grounded elements from the supplied COMPLETE
functional requirement block, including its Description.

Allowed types:
FUNCTION, DATA, ACTOR, CONSTRAINT, STATE, EVENT.

Do not apply a data-object lifecycle test to actors, events,
states, conditions, or functions.

Return JSON:
{
  "elements": [
    {
      "name": "stable concise name",
      "type": "STATE",
      "quote": "exact contiguous substring of the FR",
      "active_meaning": "what binary active=1 means; empty if undefined",
      "confidence": 0.90
    }
  ]
}

No invented quotations. Return no more than 8 elements per FR.
"""


def extract_elements(
    client: OpenAI,
    frs: list[dict],
) -> list[dict]:
    merged: dict[tuple[str, str], dict] = {}

    for fr in frs:
        response = ask_json(
            client,
            ELEMENT_PROMPT,
            {"fr": fr},
        )

        for raw in response.get("elements", []):
            if not isinstance(raw, dict):
                continue

            name = str(raw.get("name", "")).strip()
            kind = str(raw.get("type", "")).upper().strip()
            quote = str(raw.get("quote", "")).strip()
            meaning = str(
                raw.get("active_meaning", "")
            ).strip()

            try:
                confidence = float(
                    raw.get("confidence", 0)
                )
            except (TypeError, ValueError):
                continue

            if not (
                name
                and kind in ELEMENT_TYPES
                and 0.75 <= confidence <= 1
                and exact_quote(fr["text"], quote)
            ):
                continue

            key = (name.casefold(), kind)
            evidence = {
                "fr_id": fr["fr_id"],
                "quote": quote,
            }

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
                previous["confidence"] = max(
                    confidence,
                    previous["confidence"],
                )

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
    names = [item["name"] for item in result]

    if len(names) != len(set(names)):
        raise ValueError(
            "跨类型出现同名元素，无法安全建图："
            f"{names}"
        )

    return result


# ============================================================
# Stage 2：有原文位置的关系抽取
# ============================================================

RELATION_PROMPT = """
Extract causal or dependency relations justified by the supplied FRs.

Allowed relation_type:
ENABLES, TRIGGERS, PREVENTS, MODIFIES,
DEPENDS_ON, CONTROLS, PRODUCES.

source is ALWAYS the upstream element;
target is ALWAYS the downstream element.
If "Y depends on X", return source=X, target=Y.
Do not generate CONFOUNDS as a binary edge.
Chronology alone is not causation.
Do not connect elements merely because they are isolated.

propagation_sign is positive, negative, or unknown.
Use unknown if the document does not establish whether activating
source increases or decreases the SPECIFIED target active state.

Return JSON:
{
  "relations": [
    {
      "source": "exact element name",
      "target": "exact element name",
      "relation_type": "ENABLES",
      "propagation_sign": "positive",
      "confidence": 0.85,
      "source_fr_id": "FRBLOCK-001",
      "source_quote": "exact quotation",
      "target_fr_id": "FRBLOCK-002",
      "target_quote": "exact quotation",
      "reason": "why this is a dependency"
    }
  ]
}

Both quotations must be exact contiguous substrings of the
corresponding supplied FR blocks.
"""


def extract_relations(
    client: OpenAI,
    frs: list[dict],
    elements: list[dict],
    cross_window: int,
) -> list[dict]:
    if cross_window < 2:
        raise ValueError("--cross-window 必须至少为 2")

    names = {item["name"] for item in elements}
    fr_text = {
        item["fr_id"]: item["text"]
        for item in frs
    }
    accepted: dict[tuple, dict] = {}

    def process(
        selected_frs: list[dict],
        threshold: float,
    ) -> None:
        response = ask_json(
            client,
            RELATION_PROMPT,
            {
                "elements": [
                    {
                        "name": item["name"],
                        "type": item["type"],
                        "active_meaning": item["active_meaning"],
                    }
                    for item in elements
                ],
                "frs": selected_frs,
            },
        )

        allowed_ids = {
            fr["fr_id"] for fr in selected_frs
        }

        for raw in response.get("relations", []):
            if not isinstance(raw, dict):
                continue

            source = str(raw.get("source", "")).strip()
            target = str(raw.get("target", "")).strip()
            kind = str(
                raw.get("relation_type", "")
            ).upper().strip()
            sign = str(
                raw.get("propagation_sign", "unknown")
            ).lower().strip()
            source_id = str(
                raw.get("source_fr_id", "")
            ).strip()
            target_id = str(
                raw.get("target_fr_id", "")
            ).strip()
            source_quote = str(
                raw.get("source_quote", "")
            ).strip()
            target_quote = str(
                raw.get("target_quote", "")
            ).strip()

            try:
                confidence = float(
                    raw.get("confidence", 0)
                )
            except (TypeError, ValueError):
                continue

            if not (
                source in names
                and target in names
                and source != target
                and kind in RELATION_TYPES
                and sign in {
                    "positive",
                    "negative",
                    "unknown",
                }
                and threshold <= confidence <= 1
                and source_id in allowed_ids
                and target_id in allowed_ids
                and exact_quote(
                    fr_text[source_id],
                    source_quote,
                )
                and exact_quote(
                    fr_text[target_id],
                    target_quote,
                )
            ):
                continue

            key = (
                source,
                target,
                kind,
                source_id,
                target_id,
                source_quote,
                target_quote,
            )

            relation = {
                "relation_id": stable_id(
                    "REL",
                    *(str(value) for value in key),
                ),
                "source": source,
                "target": target,
                "relation_type": kind,
                "propagation_sign": sign,
                "confidence": confidence,
                "source_fr_id": source_id,
                "source_quote": source_quote,
                "target_fr_id": target_id,
                "target_quote": target_quote,
                "reason": str(
                    raw.get("reason", "")
                ).strip(),
            }

            if (
                key not in accepted
                or confidence > accepted[key]["confidence"]
            ):
                accepted[key] = relation

    # FR 内部
    for fr in frs:
        process([fr], 0.75)

    # 跨 FR：窗口是显式实验参数，不假装一次调用读遍全文。
    for start in range(len(frs) - 1):
        window = frs[start:start + cross_window]

        if len(window) >= 2:
            process(window, 0.60)

    return list(accepted.values())


# ============================================================
# Stage 3：证据图与有符号模拟图
# ============================================================

class CausalModel:
    def __init__(
        self,
        elements: list[dict],
        relations: list[dict],
    ):
        self.evidence_graph = nx.MultiDiGraph()
        self.simulation_graph = nx.DiGraph()
        self.exclusions: list[dict] = []
        self.name_to_variable: dict[str, str] = {}
        self.model: DiscreteBayesianNetwork | None = None

        for element in elements:
            self.evidence_graph.add_node(
                element["name"],
                **element,
            )

            if element.get("active_meaning"):
                self.simulation_graph.add_node(
                    element["name"],
                    **element,
                )

        for relation in relations:
            self.evidence_graph.add_edge(
                relation["source"],
                relation["target"],
                key=relation["relation_id"],
                **relation,
            )

        grouped: dict[tuple[str, str], list[dict]] = (
            defaultdict(list)
        )

        for relation in relations:
            grouped[
                (relation["source"], relation["target"])
            ].append(relation)

        # 处理顺序固定，保证 cycle / parent-budget 排除可复现。
        pairs = sorted(
            grouped,
            key=lambda pair: (
                -max(
                    item["confidence"]
                    for item in grouped[pair]
                ),
                pair[0],
                pair[1],
            ),
        )

        for source, target in pairs:
            support = grouped[(source, target)]
            signs = {
                item["propagation_sign"]
                for item in support
            }
            reason = None

            if (
                source not in self.simulation_graph
                or target not in self.simulation_graph
            ):
                reason = "undefined_activation_state"
            elif "unknown" in signs:
                reason = "unspecified_sign"
            elif len(signs) != 1:
                reason = "conflicting_signs"
            elif (
                self.simulation_graph.in_degree(target)
                >= MAX_PARENTS
            ):
                reason = "parent_budget"
            else:
                trial = self.simulation_graph.copy()
                trial.add_edge(source, target)

                if not nx.is_directed_acyclic_graph(trial):
                    reason = "cycle_requires_review"

            if reason:
                self.exclusions.append({
                    "source": source,
                    "target": target,
                    "reason": reason,
                    "relation_ids": [
                        item["relation_id"]
                        for item in support
                    ],
                })
                continue

            sign = next(iter(signs))
            self.simulation_graph.add_edge(
                source,
                target,
                sign=1 if sign == "positive" else -1,
                direction=sign,
                weight=max(
                    item["confidence"]
                    for item in support
                ),
                relation_ids=[
                    item["relation_id"]
                    for item in support
                ],
            )

        self.name_to_variable = {
            name: f"N{index:04d}"
            for index, name in enumerate(
                sorted(self.simulation_graph.nodes()),
                1,
            )
        }

        self.model_version = stable_id(
            "MODEL",
            json.dumps(
                {
                    "nodes": sorted(
                        self.simulation_graph.nodes()
                    ),
                    "edges": sorted(
                        (
                            u,
                            v,
                            data["sign"],
                            data["weight"],
                        )
                        for u, v, data in
                        self.simulation_graph.edges(
                            data=True
                        )
                    ),
                    "background_log_odds": (
                        BACKGROUND_LOG_ODDS
                    ),
                    "propagation_strength": (
                        PROPAGATION_STRENGTH
                    ),
                    "max_parents": MAX_PARENTS,
                },
                sort_keys=True,
            ),
        )

        self._build_bn()

    def _build_bn(self) -> None:
        graph = self.simulation_graph

        if not graph.nodes:
            return

        model = DiscreteBayesianNetwork([
            (
                self.name_to_variable[source],
                self.name_to_variable[target],
            )
            for source, target in graph.edges()
        ])

        model.add_nodes_from(
            self.name_to_variable.values()
        )

        cpds = []

        for node in nx.topological_sort(graph):
            parents = sorted(graph.predecessors(node))
            values = []

            for states in itertools.product(
                (0, 1),
                repeat=len(parents),
            ):
                log_odds = BACKGROUND_LOG_ODDS

                for parent, state in zip(
                    parents,
                    states,
                ):
                    edge = graph[parent][node]

                    log_odds += (
                        edge["sign"]
                        * PROPAGATION_STRENGTH
                        * edge["weight"]
                        * state
                    )

                values.append(sigmoid(log_odds))

            kwargs: dict[str, Any] = {}

            if parents:
                kwargs["evidence"] = [
                    self.name_to_variable[parent]
                    for parent in parents
                ]
                kwargs["evidence_card"] = (
                    [2] * len(parents)
                )

            cpds.append(
                TabularCPD(
                    variable=self.name_to_variable[node],
                    variable_card=2,
                    values=[
                        [1.0 - value for value in values],
                        values,
                    ],
                    **kwargs,
                )
            )

        model.add_cpds(*cpds)
        model.check_model()
        self.model = model

    def probability_do(
        self,
        source: str,
        target: str,
        state: int,
    ) -> float:
        if self.model is None:
            raise ValueError("模拟网络为空。")

        variable = self.name_to_variable[source]
        target_variable = self.name_to_variable[target]

        intervened = self.model.copy()
        intervened.remove_cpds(
            intervened.get_cpds(variable)
        )
        intervened.remove_edges_from(
            list(intervened.in_edges(variable))
        )
        intervened.add_cpds(
            TabularCPD(
                variable=variable,
                variable_card=2,
                values=[
                    [float(1 - state)],
                    [float(state)],
                ],
            )
        )
        intervened.check_model()

        result = VariableElimination(
            intervened
        ).query(
            variables=[target_variable],
            show_progress=False,
        )

        return float(result.values[1])

    def ace(
        self,
        source: str,
        target: str,
    ) -> tuple[float, float, float]:
        graph = self.simulation_graph

        if (
            source not in graph
            or target not in graph
            or source == target
            or not nx.has_path(graph, source, target)
        ):
            raise ValueError(
                f"模拟图没有 {source} → {target} 的下游路径。"
            )

        p1 = self.probability_do(
            source,
            target,
            1,
        )
        p0 = self.probability_do(
            source,
            target,
            0,
        )

        return p1 - p0, p1, p0

    def shared_upstream(
        self,
        source: str,
        target: str,
    ) -> list[dict]:
        """
        共享上游条件：既能到达 source、又能不经过 source 到达 target 的元素。

        这是 X 与 Y 在构造图中的共同原因（混淆候选）。只做图检索，
        不进入任何模型提示词，也不参与 ACE、可达性与排序计算。
        """
        graph = self.simulation_graph

        if (
            source not in graph
            or target not in graph
            or source == target
        ):
            return []

        without_source = graph.copy()
        without_source.remove_node(source)

        if target not in without_source:
            return []

        candidates = nx.ancestors(graph, source) & nx.ancestors(
            without_source,
            target,
        )

        return [
            {
                "element": element,
                "path_to_source": nx.shortest_path(
                    graph,
                    element,
                    source,
                ),
                "path_to_target": nx.shortest_path(
                    without_source,
                    element,
                    target,
                ),
            }
            for element in sorted(candidates)
        ]

    def probability_observed(
        self,
        source: str,
        target: str,
        state: int,
    ) -> float:
        """
        P(target active | source OBSERVED in `state`)。

        与 probability_do() 的区别：这里保留 source 的入边，因此共同原因
        会通过 source 传入信息；两者之差即该模型内部的混淆偏差。
        """
        if self.model is None:
            raise ValueError("模拟网络为空。")

        source_variable = self.name_to_variable[source]
        target_variable = self.name_to_variable[target]

        result = VariableElimination(self.model).query(
            variables=[target_variable],
            evidence={source_variable: state},
            show_progress=False,
        )

        return float(result.values[1])


# ============================================================
# RQ2：先固定候选池，之后才计算排序
# ============================================================

def build_fixed_pool(
    doc_id: str,
    model: CausalModel,
    pool_size: int,
) -> list[dict]:
    graph = model.simulation_graph

    pairs = [
        (source, target)
        for source in graph.nodes()
        for target in nx.descendants(
            graph,
            source,
        )
    ]

    # 入池规则与 ACE 和 reachability 无关。
    pairs.sort(
        key=lambda pair: hashlib.sha256(
            (
                doc_id
                + "\x1f"
                + pair[0]
                + "\x1f"
                + pair[1]
            ).encode("utf-8")
        ).hexdigest()
    )

    if len(pairs) < pool_size:
        raise ValueError(
            f"{doc_id} 只有 {len(pairs)} 个可查询源–目标对，"
            f"不足固定池 {pool_size} 条；不能补造候选。"
        )

    pool = []

    for index, (source, target) in enumerate(
        pairs[:pool_size],
        1,
    ):
        ace, p1, p0 = model.ace(
            source,
            target,
        )

        # 条件关联：观测 source 与干预 source 之差，以及共享上游条件。
        # 这是解释性记录，不参与入池与排序。
        p_observed = model.probability_observed(
            source,
            target,
            1,
        )

        pool.append({
            "candidate_id": f"DEP-{index:03d}",
            "source": source,
            "target": target,
            "ace": ace,
            "p_do_1": p1,
            "p_do_0": p0,
            # 可达性口径：源节点的所有下游节点数量。
            "reachability": len(
                nx.descendants(graph, source)
            ),
            "model_version": model.model_version,
            "shared_upstream": model.shared_upstream(
                source,
                target,
            ),
            "p_observed_1": p_observed,
            "association_gap": p_observed - p1,
        })

    return pool


def export_rq2(
    doc_id: str,
    original_doc: str,
    pool: list[dict],
    root: Path,
    seed: int,
) -> None:
    out = root / "RQ2"
    write_text(
        out / "original_document.txt",
        original_doc,
    )
    write_json(out / "fixed_pool.json", pool)

    rankings = {
        "ACE": sorted(
            pool,
            key=lambda item: (
                -abs(item["ace"]),
                item["candidate_id"],
            ),
        ),
        "Reachability": sorted(
            pool,
            key=lambda item: (
                -item["reachability"],
                item["candidate_id"],
            ),
        ),
    }

    random_order = sorted(
        pool,
        key=lambda item: item["candidate_id"],
    )

    random.Random(
        stable_seed(seed, doc_id)
    ).shuffle(random_order)

    rankings["Random"] = random_order

    original_ids = {
        item["candidate_id"] for item in pool
    }

    for name, ordered in rankings.items():
        if {
            item["candidate_id"] for item in ordered
        } != original_ids:
            raise AssertionError(
                "RQ2 排序改变了固定候选池。"
            )

        rows = []

        for rank, item in enumerate(ordered, 1):
            rows.append({
                "rank": rank,
                **item,
            })

        write_csv(
            out / f"{name}_review.csv",
            [
                "rank",
                "candidate_id",
                "source",
                "target",
                "ace",
                "p_do_1",
                "p_do_0",
                "reachability",
                "model_version",
            ],
            rows,
        )

    write_json(
        out / "manifest.json",
        {
            "doc_id": doc_id,
            "pool_size": len(pool),
            "candidate_ids": sorted(original_ids),
            "pool_selection": (
                "stable SHA-256 ordering of reachable "
                "source–target pairs, before scoring"
            ),
            "reachability_definition": (
                "number of descendants of source node"
            ),
            "random_seed": seed,
        },
    )


# ============================================================
# Stage 4：三路提名
# ============================================================

DEPENDENCY_PROMPT = """
Generate ONE requirements REVIEW QUESTION for this documented
source–target dependency.

The ACE is a model-based PRIORITY SCORE, not evidence that an
obligation is missing.

Use the supplied FR quotations. Do not invent retry intervals,
rollback policies, user roles, payment rules, or implementation
guarantees.

Return JSON:
{
  "question": "...",
  "scenario": "...",
  "draft_obligation": "a focused provisional business obligation"
}
"""


COMPLEMENT_PROMPT = """
Propose review QUESTIONS about the supplied original FR block.

Allowed routes:
- isolated: a supplied graph-isolated element might need a
  documented connection, but isolation alone proves no gap;
- operation: a specific operation might be applicable because
  of the documented workflow; full CRUD is NOT mandatory.

Return JSON:
{
  "questions": [
    {
      "route": "isolated",
      "subject": "exact supplied element name",
      "question": "...",
      "scenario": "...",
      "evidence_fr_id": "FRBLOCK-001",
      "evidence_quote": "exact contiguous substring",
      "draft_obligation": "focused provisional business obligation"
    }
  ]
}

Only return routes enabled in the supplied settings.
Do not propose integration solely because an element is isolated.
Do not mandate Create/Read/Update/Delete by default.
"""


def path_evidence(
    model: CausalModel,
    relations: list[dict],
    source: str,
    target: str,
) -> list[dict]:
    by_id = {
        item["relation_id"]: item
        for item in relations
    }
    path = nx.shortest_path(
        model.simulation_graph,
        source,
        target,
    )
    result = []

    for left, right in zip(
        path[:-1],
        path[1:],
    ):
        for relation_id in (
            model.simulation_graph[left][right]
            ["relation_ids"]
        ):
            result.append(by_id[relation_id])

    return result


def generate_nominations(
    client: OpenAI,
    frs: list[dict],
    elements: list[dict],
    relations: list[dict],
    model: CausalModel,
    pool: list[dict],
    settings: dict,
) -> list[dict]:
    fr_by_id = {
        fr["fr_id"]: fr["text"]
        for fr in frs
    }
    nominations = []

    for candidate in pool:
        source = candidate["source"]
        target = candidate["target"]
        evidence = path_evidence(
            model,
            relations,
            source,
            target,
        )

        payload = {
            "source": source,
            "target": target,
            "evidence": evidence,
            "source_active_meaning": (
                model.simulation_graph.nodes[source]
                ["active_meaning"]
            ),
            "target_active_meaning": (
                model.simulation_graph.nodes[target]
                ["active_meaning"]
            ),
            "propagation_enabled": settings[
                "signed_propagation"
            ],
        }

        # 真正的消融：关闭传播时不给 ACE、干预概率、
        # 模型效应名次；不拿 0 冒充 ACE。
        if settings["signed_propagation"]:
            payload["model_ace"] = (
                candidate["ace"]
            )
            payload["p_do_1"] = (
                candidate["p_do_1"]
            )
            payload["p_do_0"] = (
                candidate["p_do_0"]
            )

        response = ask_json(
            client,
            DEPENDENCY_PROMPT,
            payload,
        )

        nominations.append({
            "nomination_id": (
                candidate["candidate_id"]
            ),
            "origin": "dependency",
            "subject": f"{source} → {target}",
            "question": str(
                response.get("question", "")
            ).strip(),
            "scenario": str(
                response.get("scenario", "")
            ).strip(),
            "draft_obligation": str(
                response.get("draft_obligation", "")
            ).strip(),
            "evidence_fr_ids": sorted({
                item["source_fr_id"]
                for item in evidence
            } | {
                item["target_fr_id"]
                for item in evidence
            }),
            "evidence": evidence,
            "ace_visible_to_nomination": (
                candidate["ace"]
                if settings["signed_propagation"]
                else None
            ),
        })

    isolated = {
        node
        for node in model.evidence_graph.nodes()
        if model.evidence_graph.degree(node) == 0
    }

    if (
        settings["isolated_review"]
        or settings["operation_review"]
    ):
        for fr in frs:
            response = ask_json(
                client,
                COMPLEMENT_PROMPT,
                {
                    "fr": fr,
                    "elements_in_or_supported_by_fr": [
                        element
                        for element in elements
                        if any(
                            evidence["fr_id"]
                            == fr["fr_id"]
                            for evidence
                            in element["evidence"]
                        )
                    ],
                    "isolated_elements": sorted(
                        isolated
                    ),
                    "enabled_routes": [
                        route
                        for route, enabled in (
                            (
                                "isolated",
                                settings[
                                    "isolated_review"
                                ],
                            ),
                            (
                                "operation",
                                settings[
                                    "operation_review"
                                ],
                            ),
                        )
                        if enabled
                    ],
                },
            )

            for raw in response.get(
                "questions", []
            ):
                if not isinstance(raw, dict):
                    continue

                route = str(
                    raw.get("route", "")
                ).strip().lower()
                subject = str(
                    raw.get("subject", "")
                ).strip()
                fr_id = str(
                    raw.get("evidence_fr_id", "")
                ).strip()
                quote = str(
                    raw.get("evidence_quote", "")
                ).strip()
                question = str(
                    raw.get("question", "")
                ).strip()

                if route == "isolated":
                    if (
                        not settings[
                            "isolated_review"
                        ]
                        or subject not in isolated
                    ):
                        continue
                elif route == "operation":
                    if not settings[
                        "operation_review"
                    ]:
                        continue
                else:
                    continue

                if (
                    fr_id != fr["fr_id"]
                    or fr_id not in fr_by_id
                    or not exact_quote(
                        fr_by_id[fr_id],
                        quote,
                    )
                    or not question
                ):
                    continue

                nominations.append({
                    "nomination_id": stable_id(
                        route.upper(),
                        fr_id,
                        subject,
                        question,
                    ),
                    "origin": route,
                    "subject": subject,
                    "question": question,
                    "scenario": str(
                        raw.get("scenario", "")
                    ).strip(),
                    "draft_obligation": str(
                        raw.get(
                            "draft_obligation",
                            "",
                        )
                    ).strip(),
                    "evidence_fr_ids": [fr_id],
                    "evidence": [{
                        "fr_id": fr_id,
                        "quote": quote,
                    }],
                    "ace_visible_to_nomination": (
                        None
                    ),
                })

    ids = [
        item["nomination_id"]
        for item in nominations
    ]

    if len(ids) != len(set(ids)):
        raise ValueError(
            "同一次运行出现重复 nomination_id；"
            "需要检查候选去重规则。"
        )

    return nominations


# ============================================================
# Stage 4：全文逐 FR 检查——仅模型初步验证
# ============================================================

SCREEN_PROMPT = """
Screen ONE review question against THIS supplied original FR.

Return JSON:
{
  "covered": true or false,
  "out_of_scope_evidence": true or false,
  "reason": "...",
  "quote": "exact contiguous substring supporting the finding,
            or empty string"
}

"covered" means the FR already specifies an equivalent business
obligation. Do not call something covered just because the same
entity name appears.

Only mark a positive finding if quote is an exact substring.
"""


FINAL_SCREEN_PROMPT = """
This is a PRELIMINARY model screening, not a human validity label.

You are given:
- the nominated question and draft;
- screening notes from EVERY original FR;
- the nomination's documented evidence.

Return one outcome:
retained, covered, unsupported, out_of_scope, unresolved.

retained: supported, in-scope business obligation not found in
the checked original FRs;
covered: an original FR already states an equivalent obligation;
unsupported: the draft introduces an unsupported policy;
out_of_scope: source text assigns it outside this system;
unresolved: evidence is insufficient for a defensible decision.

If retained, return a concise business-level supplement.
Otherwise return an empty supplement.

Return JSON:
{
  "outcome": "retained",
  "reason": "...",
  "supplement": "The system shall ..."
}

Do not claim this is an independent human evaluation.
"""

# ---------------------------------------------------------------------------
# Prompt templates live in ../prompts (one text file per template) so they can be
# reviewed and edited without touching the pipeline code. The literals above stay
# as the fallback: if a file is missing, the built-in default is used.
# ---------------------------------------------------------------------------
try:
    from prompt_store import load as _load_prompt
except ImportError:                      # module imported from another directory
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from prompt_store import load as _load_prompt

ELEMENT_PROMPT = _load_prompt("shared/element_extraction", ELEMENT_PROMPT)
RELATION_PROMPT = _load_prompt("shared/relation_extraction", RELATION_PROMPT)
DEPENDENCY_PROMPT = _load_prompt("rq1/nomination_dependency", DEPENDENCY_PROMPT)
COMPLEMENT_PROMPT = _load_prompt("rq1/nomination_complement", COMPLEMENT_PROMPT)
SCREEN_PROMPT = _load_prompt("rq1/validation_screen", SCREEN_PROMPT)
FINAL_SCREEN_PROMPT = _load_prompt("rq1/validation_final", FINAL_SCREEN_PROMPT)


def preliminarily_validate(
    client: OpenAI,
    frs: list[dict],
    nomination: dict,
    require_evidence: bool | None = None,
) -> dict:
    """
    逐 FR 筛查 + 汇总初判。

    require_evidence=False 时只记录模型给出的去向，不因缺少引文级证据而降级；
    True（默认）时启用引文级证据闸门。
    """
    if require_evidence is None:
        require_evidence = REQUIRE_EVIDENCE_DEFAULT
    notes = []

    # 一次检查一条完整 FR。不能使用 safe_truncate_doc。
    for fr in frs:
        response = ask_json(
            client,
            SCREEN_PROMPT,
            {
                "nomination": {
                    "question": nomination["question"],
                    "draft_obligation": (
                        nomination[
                            "draft_obligation"
                        ]
                    ),
                },
                "original_fr": fr,
            },
        )

        quote = str(
            response.get("quote", "")
        ).strip()
        valid_positive_quote = exact_quote(
            fr["text"],
            quote,
        )

        notes.append({
            "fr_id": fr["fr_id"],
            "covered": (
                response.get("covered")
                is True
                and valid_positive_quote
            ),
            "out_of_scope_evidence": (
                response.get(
                    "out_of_scope_evidence"
                )
                is True
                and valid_positive_quote
            ),
            "quote": (
                quote
                if valid_positive_quote
                else ""
            ),
            "reason": str(
                response.get("reason", "")
            ).strip(),
        })

    response = ask_json(
        client,
        FINAL_SCREEN_PROMPT,
        {
            "nomination": nomination,
            "all_original_fr_screenings": notes,
            "total_original_frs": len(frs),
        },
    )

    outcome = str(
        response.get("outcome", "unresolved")
    ).strip().lower()

    if outcome not in VALIDATION_OUTCOMES:
        outcome = "unresolved"

    supplement = str(
        response.get("supplement", "")
    ).strip()

    # 引文级证据闸门（默认开启，只改标注、不丢条目）。
    if require_evidence:
        if (
            outcome == "covered"
            and not any(
                item["covered"] for item in notes
            )
        ):
            outcome = "unresolved"

        if (
            outcome == "out_of_scope"
            and not any(
                item["out_of_scope_evidence"]
                for item in notes
            )
        ):
            outcome = "unresolved"

        if outcome == "retained" and (
            not supplement
            or not nomination[
                "evidence_fr_ids"
            ]
        ):
            outcome = "unresolved"

    return {
        "preliminary_outcome": outcome,
        "preliminary_reason": str(
            response.get("reason", "")
        ).strip(),
        "supplement": (
            supplement
            if (outcome == "retained" or not require_evidence)
            else ""
        ),
        "evidence_gate_applied": require_evidence,
        "checked_fr_ids": [
            item["fr_id"] for item in notes
        ],
        "fr_screenings": notes,
        "validation_status": (
            "model_preliminary_not_human"
        ),
    }


def produce_variant(
    client: OpenAI,
    doc_id: str,
    original_doc: str,
    frs: list[dict],
    elements: list[dict],
    relations: list[dict],
    model: CausalModel,
    pool: list[dict],
    variant_name: str,
    settings: dict,
    output_root: Path,
    require_evidence: bool | None = None,
    drop_non_retained: bool | None = None,
) -> tuple[list[dict], list[dict]]:
    if require_evidence is None:
        require_evidence = REQUIRE_EVIDENCE_DEFAULT

    if drop_non_retained is None:
        drop_non_retained = DROP_NON_RETAINED_DEFAULT

    nominations = generate_nominations(
        client,
        frs,
        elements,
        relations,
        model,
        pool,
        settings,
    )

    for nomination in nominations:
        if settings[
            "full_document_validation"
        ]:
            nomination.update(
                preliminarily_validate(
                    client,
                    frs,
                    nomination,
                    require_evidence=require_evidence,
                )
            )
        else:
            # 真实关闭该组件：不调用全文检查。
            nomination.update({
                "preliminary_outcome": (
                    "not_checked"
                ),
                "preliminary_reason": (
                    "Full-document validation "
                    "disabled in this ablation."
                ),
                "supplement": (
                    nomination[
                        "draft_obligation"
                    ]
                ),
                "checked_fr_ids": [],
                "fr_screenings": [],
                "validation_status": (
                    "unchecked_draft"
                ),
            })

    supplements = []
    seen_exact_text = set()

    for nomination in nominations:
        validated = settings["full_document_validation"]
        reported_only = validated and not drop_non_retained

        if validated and drop_non_retained:
            if nomination["preliminary_outcome"] != "retained":
                continue

        text = nomination["supplement"].strip()

        # 只记录不淘汰时，没有 supplement 的提名回落到提名阶段的草案，
        # 这样默认配置不会因为验证结论而丢掉任何一条提名。
        if not text and reported_only:
            text = str(nomination.get("draft_obligation", "")).strip()

        if not text:
            continue

        key = re.sub(
            r"\s+",
            " ",
            text.casefold(),
        )

        if key in seen_exact_text:
            continue

        seen_exact_text.add(key)

        supplements.append({
            "output_id": stable_id(
                "OUT",
                doc_id,
                variant_name,
                nomination[
                    "nomination_id"
                ],
                text,
            ),
            "source_nomination_id": (
                nomination[
                    "nomination_id"
                ]
            ),
            "origin": nomination[
                "origin"
            ],
            "text": text,
            "status": (
                "model_preliminarily_retained"
                if (validated and drop_non_retained)
                else (
                    "unchecked_draft"
                    if not validated
                    else "model_preliminary_reported"
                )
            ),
            "disposition": nomination.get(
                "preliminary_outcome",
                "not_checked",
            ),
        })

    out = (
        output_root
        / doc_id
        / "RQ3"
        / variant_name
    )

    write_json(
        out / "run_settings.json",
        {
            "doc_id": doc_id,
            "variant": variant_name,
            **settings,
            "require_evidence": require_evidence,
            "drop_non_retained": drop_non_retained,
            "model_version": (
                model.model_version
            ),
            "source_document_fixed": True,
        },
    )
    write_text(
        out / "original_document.txt",
        original_doc,
    )
    write_json(
        out / "nominations.json",
        nominations,
    )
    write_json(
        out / "supplements.json",
        supplements,
    )

    return nominations, supplements


# ============================================================
# RQ1：整理原文与 CausalReq 生成的新增需求
# ============================================================

def export_rq1(
    doc_id: str,
    original_doc: str,
    full_supplements: list[dict],
    output_root: Path,
) -> int:
    out = output_root / doc_id / "RQ1"

    write_text(
        out / "00_original_document.txt",
        original_doc,
    )

    causalreq_text = "\n\n".join(
        f"{index}. {item['text']}"
        for index, item in enumerate(
            full_supplements,
            1,
        )
    )

    write_text(
        out / "causalreq_supplements_only.txt",
        causalreq_text,
    )

    write_text(
        out / "causalreq_complete_document.txt",
        original_doc.rstrip()
        + "\n\nSUPPLEMENTARY REQUIREMENTS\n\n"
        + causalreq_text,
    )


    write_json(
        out / "manifest.json",
        {
            "doc_id": doc_id,
            "causalreq_supplement_count": (
                len(full_supplements)
            ),
            "human_assessment_completed": (
                False
            ),
        },
    )

    return len(full_supplements)


# ============================================================
# 批量运行
# ============================================================

def discover_documents(
    data_root: Path,
    expect_42: bool,
) -> list[tuple[str, Path]]:
    documents = []

    for case in CASES:
        folder = (
            data_root
            / case
            / "Document"
        )

        if not folder.is_dir():
            if expect_42:
                raise FileNotFoundError(
                    f"缺少目录：{folder}"
                )
            continue

        files = sorted(
            path
            for path in folder.glob("*.docx")
            if not path.name.startswith("~$")
        )

        if expect_42 and len(files) != 6:
            raise ValueError(
                f"{case} 发现 {len(files)} 份 DOCX，"
                "预期 6 份。"
            )

        for path in files:
            doc_id = (
                case
                + "_"
                + cleaned_filename(
                    path.stem
                )
            )

            documents.append(
                (doc_id, path)
            )

    ids = [
        doc_id
        for doc_id, _ in documents
    ]

    if len(ids) != len(set(ids)):
        raise ValueError(
            "生成的 doc_id 重复，"
            "请修改 cleaned_filename()。"
        )

    if expect_42 and len(documents) != 42:
        raise ValueError(
            f"发现 {len(documents)} 份文档，"
            "预期 42 份。"
        )

    if not documents:
        raise ValueError(
            "没有发现任何 DOCX。"
        )

    return documents


def run_one(
    client: OpenAI,
    doc_id: str,
    source_path: Path,
    output_root: Path,
    pool_size: int,
    random_seed: int,
    cross_window: int,
    require_evidence: bool | None = None,
    drop_non_retained: bool | None = None,
) -> dict:
    if require_evidence is None:
        require_evidence = REQUIRE_EVIDENCE_DEFAULT

    if drop_non_retained is None:
        drop_non_retained = DROP_NON_RETAINED_DEFAULT
    original_doc = read_docx_in_order(
        source_path
    )
    frs = split_frs(original_doc)

    root = output_root / doc_id

    write_text(
        root / "source"
        / "original_document.txt",
        original_doc,
    )
    write_json(
        root / "source"
        / "fr_blocks.json",
        frs,
    )

    elements = extract_elements(
        client,
        frs,
    )
    relations = extract_relations(
        client,
        frs,
        elements,
        cross_window,
    )
    model = CausalModel(
        elements,
        relations,
    )

    write_json(
        root / "source"
        / "elements.json",
        elements,
    )
    write_json(
        root / "source"
        / "relations.json",
        relations,
    )
    write_json(
        root / "source"
        / "simulation_exclusions.json",
        model.exclusions,
    )

    pool = build_fixed_pool(
        doc_id,
        model,
        pool_size,
    )

    export_rq2(
        doc_id,
        original_doc,
        pool,
        root,
        random_seed,
    )

    variant_counts = {}
    full_supplements = []

    for variant_name, settings in (
        VARIANTS.items()
    ):
        print(
            f"    RQ3 {variant_name}",
            flush=True,
        )

        nominations, supplements = (
            produce_variant(
                client=client,
                doc_id=doc_id,
                original_doc=original_doc,
                frs=frs,
                elements=elements,
                relations=relations,
                model=model,
                pool=pool,
                variant_name=variant_name,
                settings=settings,
                output_root=output_root,
                require_evidence=require_evidence,
                drop_non_retained=drop_non_retained,
            )
        )

        variant_counts[variant_name] = {
            "nomination_count": (
                len(nominations)
            ),
            "supplement_count": (
                len(supplements)
            ),
        }

        if variant_name == "Full":
            full_supplements = (
                supplements
            )

    export_rq1(
        doc_id,
        original_doc,
        full_supplements,
        output_root,
    )

    return {
        "doc_id": doc_id,
        "source_path": str(
            source_path
        ),
        "source_fr_count": len(frs),
        "element_count": len(
            elements
        ),
        "evidence_relation_count": len(
            relations
        ),
        "simulation_edge_count": (
            model.simulation_graph
            .number_of_edges()
        ),
        "fixed_pool_count": len(
            pool
        ),
        "model_version": (
            model.model_version
        ),
        "variant_counts": (
            variant_counts
        ),
        "human_assessment_completed": (
            False
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data-root",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "--pool-size",
        type=int,
        default=POOL_SIZE,
    )
    parser.add_argument(
        "--random-seed",
        type=int,
        default=20261010,
    )
    parser.add_argument(
        "--cross-window",
        type=int,
        default=2,
    )
    parser.add_argument(
        "--require-evidence",
        action=argparse.BooleanOptionalAction,
        default=REQUIRE_EVIDENCE_DEFAULT,
        help="引文级证据闸门（默认开）：covered / out_of_scope 需要引文级"
             "逐段证据，retained 需要补充需求与证据 FR，否则记为 unresolved。"
             "只改标注，不丢弃条目。",
    )
    parser.add_argument(
        "--drop-non-retained",
        action="store_true",
        default=DROP_NON_RETAINED_DEFAULT,
        help="淘汰闸门（默认关）：只输出 retained 的提名，其余全部丢弃。"
             "副作用最大，会把真实缺口一起丢掉。",
    )
    parser.add_argument(
        "--enforce-validation",
        action="store_true",
        help="等价于同时打开 --require-evidence 与 --drop-non-retained，"
             "即论文评测使用的配置。",
    )
    parser.add_argument(
        "--allow-partial-dataset",
        action="store_true",
        help="调试少量文档时使用",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="单文档失败时继续其余文档；"
             "失败文档不得计入完整实验",
    )

    args = parser.parse_args()

    if args.pool_size < 20:
        parser.error(
            "RQ2 包含前 20 条预算，"
            "--pool-size 不能小于 20"
        )

    if args.cross_window < 2:
        parser.error(
            "--cross-window 不能小于 2"
        )

    documents = discover_documents(
        args.data_root,
        expect_42=(
            not args.allow_partial_dataset
        ),
    )
    client = get_client()

    args.output_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    completed = []
    failed = []

    for index, (
        doc_id,
        source_path,
    ) in enumerate(
        documents,
        1,
    ):
        print(
            f"[{index}/{len(documents)}] "
            f"{doc_id}",
            flush=True,
        )

        try:
            result = run_one(
                client=client,
                doc_id=doc_id,
                source_path=source_path,
                output_root=(
                    args.output_root
                ),
                pool_size=(
                    args.pool_size
                ),
                random_seed=(
                    args.random_seed
                ),
                cross_window=(
                    args.cross_window
                ),
                require_evidence=(
                    True if args.enforce_validation
                    else args.require_evidence
                ),
                drop_non_retained=(
                    True if args.enforce_validation
                    else args.drop_non_retained
                ),
            )
            completed.append(result)
            write_json(
                args.output_root
                / doc_id
                / "run_manifest.json",
                result,
            )

        except Exception as exc:
            failure = {
                "doc_id": doc_id,
                "source_path": str(
                    source_path
                ),
                "error": str(exc),
                "traceback": (
                    traceback.format_exc()
                ),
            }
            failed.append(failure)

            write_json(
                args.output_root
                / doc_id
                / "FAILED.json",
                failure,
            )

            print(
                f"  FAILED: {exc}",
                file=sys.stderr,
                flush=True,
            )

            if not args.continue_on_error:
                write_json(
                    args.output_root
                    / "batch_manifest.json",
                    {
                        "completed": completed,
                        "failed": failed,
                        "complete_experiment": (
                            False
                        ),
                    },
                )
                raise

    total_frs = sum(
        item["source_fr_count"]
        for item in completed
    )

    manifest = {
        "documents_discovered": (
            len(documents)
        ),
        "documents_completed": (
            len(completed)
        ),
        "source_fr_total": total_frs,
        "completed": completed,
        "failed": failed,
        "settings": {
            "pool_size": (
                args.pool_size
            ),
            "random_seed": (
                args.random_seed
            ),
            "cross_fr_window": (
                args.cross_window
            ),
            "background_log_odds": (
                BACKGROUND_LOG_ODDS
            ),
            "propagation_strength": (
                PROPAGATION_STRENGTH
            ),
            "max_parents": (
                MAX_PARENTS
            ),
            "model": os.getenv(
                "CAUSALREQ_MODEL",
                "gpt-5.5",
            ),
        },
        "complete_experiment": (
            len(failed) == 0
            and len(completed) == 42
            and total_frs == 984
        ),
        "human_assessment_completed": (
            False
        ),
    }

    write_json(
        args.output_root
        / "batch_manifest.json",
        manifest,
    )

    print(
        f"\n完成：{len(completed)}/"
        f"{len(documents)}；"
        f"失败：{len(failed)}；"
        f"源 FR 合计：{total_frs}。"
    )

    if (
        not args.allow_partial_dataset
        and not manifest[
            "complete_experiment"
        ]
    ):
        raise RuntimeError(
            "批量运行尚不能标记为完整的"
            "42 文档、984 FR 实验；"
            "请检查 batch_manifest.json。"
        )


if __name__ == "__main__":
    main()
