# RQ3 人工判定下的组件贡献（含继承关系）

Full 的 54 条逐条人工审阅；四个消融版只新增/消失条目单独审阅，其余条目继承其对 Full 匹配项的判定。

| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |
|---|---:|---:|---:|---|---|---|
| NoSignedPropagation | - | 6 | 6 | O-01, O-03, O-04, O-05, O-06, O-08 | O-02 | O-08 |
| NoIsolatedReview | - | 12 | 8 | O-01, O-03, O-04, O-05, O-06, O-07, O-08, O-09 | O-02 | O-07, O-08, O-09 |
| NoOperationReview | - | 0 | 1 | O-01 | O-02, O-03, O-04, O-05, O-06 | — |
| NoFullDocumentValidation | - | 10 | 6 | O-01, O-04, O-05, O-06, O-10, O-11 | O-02, O-03 | O-10, O-11 |

## 消融时的“补位”检查

- **NoOperationReview**（operation 路线关闭，isolated 由 19 增至 47）：这 47 条 isolated 提名中，0 条与 Full 的 operation 提名语义对齐、47 条与其 isolated 提名对齐、0 条与依赖提名对齐、0 条为真正新条目。人工判定下该版本没有新增有效义务，即 isolated 路线**未能补齐**失去的 operation 覆盖。

- **NoIsolatedReview**（isolated 关闭，operation 由 15 增至 32）：新增的 operation 提名确实带来 3 条新的有效义务（O-07 批式回填去重、O-08 配置变更审批、O-09 报表投递状态），即 operation 路线**部分补齐**了失去的 isolated 覆盖，但 Full 中由 isolated 发现的 O-02（质量异常通知）没有被补回。
