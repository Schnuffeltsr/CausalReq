# RQ3 人工判定下的组件贡献（含继承关系）

Full 的 215 条逐条人工审阅；四个消融版只对新增/消失条目单独审阅，其余条目继承其对 Full 匹配项的判定。

| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |
|---|---:|---:|---:|---|---|---|
| NoSignedPropagation | 219 | 17 | 4 | O-01, O-02, O-07, O-08 | O-03, O-04, O-05, O-06 | O-08 |
| NoIsolatedReview | 196 | 26 | 6 | O-01, O-02, O-03, O-05, O-07, O-09 | O-04, O-06 | O-09 |
| NoOperationReview | 191 | 0 | 2 | O-01, O-02 | O-03, O-04, O-05, O-06, O-07 | — |
| NoFullDocumentValidation | 214 | 14 | 8 | O-01, O-02, O-03, O-05, O-07, O-08, O-10, O-11 | O-04, O-06 | O-08, O-10, O-11 |

## 消融时的“补位”检查

- **NoOperationReview**（operation 路线关闭，isolated 由 77 增至 171）：这 171 条 isolated 提名的对齐情况为 与 Full 的 isolated 提名对齐 150 条、与 Full 的 operation 提名对齐 21 条；人工判定下该版本有效义务 2 条（失去 5 条：O-03, O-04, O-05, O-06, O-07，新增 0 条）。

- **NoIsolatedReview**（isolated 路线关闭，operation 由 118 增至 176）：这 176 条 operation 提名的对齐情况为 与 Full 的 operation 提名对齐 139 条、真正的新条目 26 条、与 Full 的 isolated 提名对齐 10 条、与 Full 的依赖提名对齐 1 条；人工判定下该版本有效义务 6 条（失去 2 条：O-04, O-06，新增 1 条：O-09）。

- **NoSignedPropagation**：有效义务 4 条（失去 4 条：O-03, O-04, O-05, O-06，新增 1 条：O-08）。

- **NoFullDocumentValidation**：有效义务 8 条（失去 2 条：O-04, O-06，新增 3 条：O-08, O-10, O-11）。
