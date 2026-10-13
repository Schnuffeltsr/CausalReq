# RQ3 人工判定下的组件贡献（含继承关系）

Full 的 166 条逐条人工审阅；四个消融版只对新增/消失条目单独审阅，其余条目继承其对 Full 匹配项的判定。

| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |
|---|---:|---:|---:|---|---|---|
| NoSignedPropagation | 174 | 6 | 9 | O-01, O-02, O-04, O-06, O-07, O-10, O-12, O-13, O-14 | O-03, O-05, O-08, O-09, O-11 | O-13, O-14 |
| NoIsolatedReview | 161 | 34 | 7 | O-04, O-06, O-07, O-09, O-10, O-12, O-15 | O-01, O-02, O-03, O-05, O-08, O-11 | O-15 |
| NoOperationReview | 196 | 0 | 2 | O-01, O-02 | O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11, O-12 | — |
| NoFullDocumentValidation | 181 | 17 | 7 | O-01, O-02, O-04, O-06, O-07, O-10, O-12 | O-03, O-05, O-08, O-09, O-11 | — |

## 消融时的“补位”检查

- **NoOperationReview**（operation 路线关闭，isolated 由 70 增至 176）：这 176 条 isolated 提名的对齐情况为 与 Full 的 isolated 提名对齐 144 条、与 Full 的 operation 提名对齐 32 条；人工判定下该版本有效义务 2 条（失去 10 条：O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11, O-12，新增 0 条）。

- **NoIsolatedReview**（isolated 路线关闭，operation 由 76 增至 141）：这 141 条 operation 提名的对齐情况为 与 Full 的 operation 提名对齐 86 条、真正的新条目 34 条、与 Full 的 isolated 提名对齐 20 条、与 Full 的依赖提名对齐 1 条；人工判定下该版本有效义务 7 条（失去 6 条：O-01, O-02, O-03, O-05, O-08, O-11，新增 1 条：O-15）。

- **NoSignedPropagation**：有效义务 9 条（失去 5 条：O-03, O-05, O-08, O-09, O-11，新增 2 条：O-13, O-14）。

- **NoFullDocumentValidation**：有效义务 7 条（失去 5 条：O-03, O-05, O-08, O-09, O-11，新增 0 条）。
