# CausalReq 单文档运行结果 — Inventory_MIRC3

## 1. 抽取与图结构

| 项 | 值 |
|---|---:|
| 源 FR 块数 | 27 |
| 抽取元素数 | 155 |
| 有 active_meaning 的元素 | 140 |
| 抽出关系数 | 276 |
| 证据图节点 | 155 |
| 证据图边 | 276 |
| 模拟图节点 | 140 |
| 模拟图边 | 103 |
| 被排除关系 | 51 |
| RQ2 固定候选池 | 20 |
| LLM 调用次数 | 80 |
| 阶段耗时(分钟) | 68.5 |
| 模型版本号 | MODEL-396084324100 |

## 2. RQ2 固定候选池与 ACE 排序（20 条）

| 排名 | 候选 | 源元素 | 目标元素 | ACE | p(do=1) | p(do=0) | 可达性 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | DEP-014 | Update record upon approval | Status Modified | +0.5292 | 0.7982 | 0.2689 | 1 |
| 2 | DEP-007 | Activate Workflow | Workflow Configured | +0.5084 | 0.7773 | 0.2689 | 1 |
| 3 | DEP-009 | Query Approval Status | Approval Status Details | +0.5084 | 0.7773 | 0.2689 | 1 |
| 4 | DEP-010 | Approve Asset Request | Notify Users | +0.5084 | 0.7773 | 0.2689 | 5 |
| 5 | DEP-012 | Transfer form | Transfer Asset | +0.5084 | 0.7773 | 0.2689 | 2 |
| 6 | DEP-017 | Validate Export Request | Generate Export File | +0.4860 | 0.7549 | 0.2689 | 3 |
| 7 | DEP-013 | Admin approval | Operation executed upon approval | +0.3803 | 0.8802 | 0.4999 | 12 |
| 8 | DEP-018 | Export Asset Data | Downloadable Data File | +0.3083 | 0.9356 | 0.6273 | 4 |
| 9 | DEP-005 | Senior Admin Approval Event | Workflow Configured | +0.2690 | 0.6747 | 0.4057 | 2 |
| 10 | DEP-002 | Validate Configuration Details | Activate Workflow | +0.1307 | 0.6112 | 0.4804 | 4 |
| 11 | DEP-001 | Stage change for admin approval | Deletes the Record upon Approval | +0.1196 | 0.8091 | 0.6896 | 13 |
| 12 | DEP-011 | Validate approval-start request | Updated operation status | +0.0875 | 0.7125 | 0.6250 | 14 |
| 13 | DEP-004 | Validates the Request | Update status to Modified | +0.0674 | 0.7218 | 0.6544 | 14 |
| 14 | DEP-016 | Approval-start request | Admin approval | +0.0648 | 0.8100 | 0.7451 | 15 |
| 15 | DEP-019 | Validate modification data | Operation executed upon approval | +0.0605 | 0.8062 | 0.7457 | 14 |
| 16 | DEP-015 | Return Form | Update Asset Status to Returned | +0.0550 | 0.6654 | 0.6103 | 5 |
| 17 | DEP-008 | Validates the Request | Update Status on Approval | +0.0445 | 0.8247 | 0.7802 | 14 |
| 18 | DEP-006 | Asset Request Form | User Notification | +0.0366 | 0.5740 | 0.5374 | 9 |
| 19 | DEP-003 | Approval-start request | Deletes the Record upon Approval | +0.0289 | 0.7675 | 0.7386 | 15 |
| 20 | DEP-020 | Approval-start request | Transferred | +0.0174 | 0.6292 | 0.6118 | 15 |

## 3. 三种排序下的前 5 / 前 10 名（RQ2 预算视角）

**ACE** 前 10：DEP-014(+0.529), DEP-007(+0.508), DEP-009(+0.508), DEP-010(+0.508), DEP-012(+0.508), DEP-017(+0.486), DEP-013(+0.380), DEP-018(+0.308), DEP-005(+0.269), DEP-002(+0.131)

**Reachability** 前 10：DEP-003(+0.029), DEP-016(+0.065), DEP-020(+0.017), DEP-004(+0.067), DEP-008(+0.044), DEP-011(+0.087), DEP-019(+0.060), DEP-001(+0.120), DEP-013(+0.380), DEP-006(+0.037)

**Random** 前 10：DEP-005(+0.269), DEP-001(+0.120), DEP-016(+0.065), DEP-015(+0.055), DEP-007(+0.508), DEP-020(+0.017), DEP-008(+0.044), DEP-019(+0.060), DEP-017(+0.486), DEP-003(+0.029)

## 4. RQ3 五变体结果

| 变体 | 提名数 | dependency | isolated | operation | 补充需求数 | 初步去向分布 |
|---|---:|---:|---:|---:|---:|---|
| Full | 166 | 20 | 70 | 76 | 24 | covered=90, unsupported=48, retained=24, unresolved=4 |
| NoFullDocumentValidation | 181 | 20 | 65 | 96 | 181 | not_checked=181 |
| NoIsolatedReview | 161 | 20 | 0 | 141 | 17 | covered=111, unsupported=30, retained=17, unresolved=3 |
| NoOperationReview | 196 | 20 | 176 | 0 | 12 | covered=99, unsupported=67, unresolved=14, retained=12, out_of_scope=4 |
| NoSignedPropagation | 174 | 20 | 78 | 76 | 15 | covered=92, unsupported=54, retained=15, unresolved=12, out_of_scope=1 |

## 5. Full 变体中被初步保留的补充需求（24 条）

1. **[DEPENDENCY] Validate Export Request → Generate Export File**
   - 审查问题：Does FRBLOCK-018 explicitly require that the system generate the export file only after the export request has been successfully validated, as suggested by the dependency from 'validates the request' to 'generates the file'?
   - 初步理由：The original FRBLOCK-018 states that the system validates the request, generates the file, and provides a download link, but it does not explicitly state that file generation is conditioned on successful validation. The documented ENABLES dependency supports this prerequisite, and no other original FR already covers an equivalent obligation for export file generation.
   - 补充需求：The system shall generate the export file only if the export request has been validated successfully.
   - 证据 FR：FRBLOCK-018

2. **[OPERATION] Search Criteria**
   - 审查问题：Should asset search by name, type, or ID use exact matching, partial matching, or both, and can multiple criteria be combined in a single query?
   - 初步理由：FRBLOCK-003 establishes asset search by name, type, or ID but leaves matching semantics and combinability undefined. No original FR covers these rules, and the obligation is in-scope for asset search.
   - 补充需求：The system shall define and apply consistent matching semantics for asset search by name, type, and ID, including whether matching is exact, partial, or both, and whether multiple criteria can be combined in a single query.
   - 证据 FR：FRBLOCK-003

3. **[OPERATION] Detailed Asset Information**
   - 审查问题：Which fields must be returned for detailed asset information, and what does 'etc.' include or exclude?
   - 初步理由：FRBLOCK-003 is the only original FR addressing detailed asset information, and while it lists name, type, quantity, purchase date, status, etc., the 'etc.' leaves the output schema incomplete and no original FR defines the complete field set or clarifies what 'etc.' includes or excludes. The nomination is therefore an in-scope, supported clarification of an existing obligation rather than a duplicate or unsupported policy.
   - 补充需求：The system shall return detailed asset information with a complete and consistent output schema, including at minimum name, type, quantity, purchase date, and status, and shall explicitly define all additional fields represented by 'etc.' for every asset type.
   - 证据 FR：FRBLOCK-003

4. **[OPERATION] Query Asset Details**
   - 审查问题：How should the system respond when no asset matches the search criteria?
   - 初步理由：FRBLOCK-003 establishes the in-scope asset query operation and states that matching records are returned, but no checked FR specifies the empty-result case or the user feedback required when no asset matches the search criteria.
   - 补充需求：The system shall clearly indicate when an asset query returns no matching assets and shall not present an ambiguous empty success response.
   - 证据 FR：FRBLOCK-003

5. **[ISOLATED] Approved Operation Status**
   - 审查问题：Should the isolated Approved Operation Status be connected to the return request's approval state, distinct from the asset status Returned?
   - 初步理由：The relevant original FRs cover the return approval workflow and an operation-status concept, but no checked FR explicitly requires the return request's approval outcome to be represented as an operation status that is distinct from the asset status Returned. This is an in-scope business obligation supported by the return-approval and operation-status context, so it should be retained as a supplement.
   - 补充需求：The system shall record the return request's approval outcome as an operation status that is distinct from the asset status Returned.
   - 证据 FR：FRBLOCK-005

6. **[OPERATION] Validates the Request**
   - 审查问题：What validation rules and failure outcomes apply when the system validates a deletion request?
   - 初步理由：The original FR confirms that deletion requests are validated before staging, but it does not define the validation rules or the failure handling. The nomination's obligation to define these missing details is supported by the in-scope validation operation and is not covered by an equivalent original FR.
   - 补充需求：The system shall validate deletion requests before staging them for approval, applying defined validation criteria and handling invalid requests with appropriate failure outcomes.
   - 证据 FR：FRBLOCK-006

7. **[OPERATION] Deleted**
   - 审查问题：What does the 'Deleted' status mean for the removed asset record, and which operation sets it?
   - 初步理由：The screening notes identify FRBLOCK-006 as the only in-scope source for the Deleted status, but it only states that a removed asset record receives the status 'Deleted' after deletion upon approval. No checked original FR defines the business meaning or lifecycle of that status, so the draft obligation is a supported in-scope gap rather than a duplicate or unsupported policy.
   - 补充需求：The system shall define the 'Deleted' status as the terminal state of an asset record that has been removed by the approved deletion operation; the deletion operation upon approval shall set the asset record's status to 'Deleted'.
   - 证据 FR：FRBLOCK-006

8. **[ISOLATED] Rejected**
   - 审查问题：Should the deletion workflow document a rejected outcome when admin approval is not granted?
   - 初步理由：FRBLOCK-006 covers staging a deletion request for admin approval and deleting the record upon approval, but it does not specify the rejected outcome or next action when approval is not granted. The question concerns the same in-scope deletion approval workflow, and no checked original FR states an equivalent obligation.
   - 补充需求：The system shall specify the outcome and next action when an admin does not approve a deletion request.
   - 证据 FR：FRBLOCK-006

9. **[ISOLATED] Administrator**
   - 审查问题：Does the FR need to document the Administrator's authorization or permission check before creating new user accounts?
   - 初步理由：FRBLOCK-007 identifies Administrators as the actors who create new user accounts, but no checked original FR specifies that the system must verify the acting user's Administrator privileges before allowing account creation. The obligation is in-scope for user account creation and is not covered by any existing FR.
   - 补充需求：The system shall verify that the acting user has Administrator privileges before allowing the creation of a new user account.
   - 证据 FR：FRBLOCK-007

10. **[OPERATION] Validate New-User Form**
   - 审查问题：Should the validation operation specify which fields are mandatory and what format rules apply to the new-user form?
   - 初步理由：FRBLOCK-007 is the only in-scope FR for the new-user form, and it states only that the system validates the form. It does not specify which fields are mandatory or what format rules apply, and the screening confirms this specific validation obligation is not already covered.
   - 补充需求：The system shall enforce required-field and format validation rules for the new-user form, covering username, password, email, phone, and department.
   - 证据 FR：FRBLOCK-007

11. **[OPERATION] Query User Details**
   - 审查问题：What result should the Query User Details operation return when the search criteria match zero users or more than one user?
   - 初步理由：FRBLOCK-009 establishes the Query User Details operation and its search criteria, but no original FR specifies the return cardinality for zero, one, or multiple matching users. The draft obligation identifies an in-scope missing business rule.
   - 补充需求：The Query User Details operation shall return an empty result when no users match, a single user record when exactly one user matches, and a list of user records when multiple users match.
   - 证据 FR：FRBLOCK-009

12. **[ISOLATED] Senior Admin**
   - 审查问题：Does the FR need to document how the 'Senior Admin' approval role is identified and distinguished from the 'Administrators' who initiate deletion?
   - 初步理由：FRBLOCK-010 establishes that a user deletion request is staged for senior-admin approval, but none of the checked original FRs define who qualifies as the Senior Admin approver, how that approver is resolved, or how the approval role is distinguished from the Administrators who initiate deletion. The draft obligation is therefore an in-scope approval-role clarification not covered by the existing FRs.
   - 补充需求：The system shall define the Senior Admin approver role for user deletion requests, including how the approver is identified or resolved, and its authority to approve such requests, distinct from the Administrators who initiate deletion.
   - 证据 FR：FRBLOCK-010

13. **[OPERATION] Stage deletion request for senior-admin approval**
   - 审查问题：Does staging a deletion request require creating a pending approval item, and what status should the request have while awaiting senior-admin approval?
   - 初步理由：FRBLOCK-010 supports staging user deletion requests for senior-admin approval, but it does not define a pending-approval item or the request status while awaiting approval. The nomination is an in-scope refinement of that staging obligation, and no checked original FR covers the missing pending-state behavior.
   - 补充需求：The system shall create a pending approval item for a user deletion request and set the request status to Pending while it awaits senior-admin approval or rejection.
   - 证据 FR：FRBLOCK-010

14. **[OPERATION] Updated operation status**
   - 审查问题：Which operation statuses must be supported and how do they transition as an approval process progresses?
   - 初步理由：The original FRs include approval workflows and mention operation statuses in places, such as FRBLOCK-013 listing pending, in progress, approved, and rejected statuses, and FRBLOCK-021/022 updating request status on approval or rejection. However, no original FR defines the full operation-status lifecycle or the transitions from pending review to approval, rejection, or completion. The nominated obligation is in-scope and supported by the approval-process context, but it is not already stated as an equivalent requirement.
   - 补充需求：The system shall maintain operation statuses for approval-driven operations, transitioning from pending review to approved or rejected, and then to completed after the approved operation is executed.
   - 证据 FR：FRBLOCK-012

15. **[ISOLATED] Pending Operation Status**
   - 审查问题：Should the FR define when an operation is in Pending status while an approval process is awaiting review?
   - 初步理由：The original FRs describe approval workflows and note that operation status is updated after approval, but none defines the operation status while an approval process is awaiting administrator review. The Pending status is referenced as a queryable operation status in the source set (FR-013), so the concept is in scope, but no original FR states the equivalent assignment obligation. The draft is therefore an in-scope missing business obligation rather than a covered or out-of-scope requirement.
   - 补充需求：The system shall set the operation status to Pending while an approval process is awaiting administrator review.
   - 证据 FR：FRBLOCK-012

16. **[ISOLATED] In Progress Operation Status**
   - 审查问题：Should the FR specify what causes an operation to enter the in progress state and whether that state is available for both asset and user operations?
   - 初步理由：FRBLOCK-013 establishes that asset and user operations can have an 'in progress' status, but it only supports querying that status and does not define what causes an operation to enter it. No checked original FR specifies the entry or transition condition for the In Progress state, so the draft identifies a missing in-scope lifecycle obligation.
   - 补充需求：The system shall specify the condition(s) under which an operation transitions into the In Progress state.
   - 证据 FR：FRBLOCK-013

17. **[ISOLATED] Rejected Operation Status**
   - 审查问题：Should the FR document why an operation may be rejected and whether rejected status is queryable for both asset and user operations?
   - 初步理由：The source establishes that asset and user operations can have a rejected status (FRBLOCK-013) and that asset requests are approved or rejected (FRBLOCK-021/022), but no original FR defines the conditions under which an operation is rejected. Defining those conditions is an in-scope validation/approval obligation not already stated.
   - 补充需求：The system shall define and document the conditions under which asset and user operations are rejected.
   - 证据 FR：FRBLOCK-013

18. **[OPERATION] Validate Parameters**
   - 审查问题：Does the Validate Parameters operation need a documented failure response?
   - 初步理由：FRBLOCK-015 establishes that report parameters are validated, but it does not document the required failure response for invalid report parameters. No checked original FR specifies that invalid report parameters must be rejected with a clear error, so this is an in-scope missing business obligation.
   - 补充需求：The system shall reject invalid report parameters and return a clear error response.
   - 证据 FR：FRBLOCK-015

19. **[ISOLATED] Validate Format and Data**
   - 审查问题：Is the 'Validate Format and Data' function sufficiently connected to defined validation rules and the error report output?
   - 初步理由：FRBLOCK-017 is the in-scope validation/error-report function, but it only states that the system validates format and data and produces an error report. The screening confirms it does not define validation rules for uploaded CSV/Excel files or specify how validation failures are recorded in the error report. The nominated obligation is therefore a supported, in-scope refinement that is not already covered by the existing FR.
   - 补充需求：The system shall define and apply validation rules for uploaded CSV/Excel files and record each validation failure in the error report.
   - 证据 FR：FRBLOCK-017

20. **[OPERATION] Update Request Status**
   - 审查问题：Should the approval form's reason be stored and associated with the request status update?
   - 初步理由：FRBLOCK-022 shows that the approval form includes a reason, but no original FR requires that reason to be persisted or associated with the request status update. The nomination scenario states the reason must be available for audit or notification, so this is a supported in-scope obligation that is not covered by any checked FR.
   - 补充需求：The system shall persist the reason entered on the approval form and associate it with the updated request status so it remains available for audit or notification.
   - 证据 FR：FRBLOCK-022

21. **[ISOLATED] User**
   - 审查问题：Is the 'User' element the recipient of the user notification, and does it refer to the requestor?
   - 初步理由：The original FR-22 only states that the system notifies users after an asset request decision, without specifying that the recipient is the requestor. The nomination scenario explicitly requires the notification to go to the requestor, so the draft obligation is a supported, in-scope refinement not covered by any original FR.
   - 补充需求：The system shall notify the requestor (User) when an asset request decision is made.
   - 证据 FR：FRBLOCK-022

22. **[OPERATION] Send Email Notification**
   - 审查问题：Should the 'Send Email Notification' operation include a documented retry or fallback process when email delivery fails?
   - 初步理由：FRBLOCK-023 establishes the email notification operation, but none of the checked original FRs specify retry, fallback, or failure handling for email delivery. The nominated obligation is in-scope and not already covered.
   - 补充需求：The system shall define and document a retry or fallback process for the email notification operation when email delivery fails.
   - 证据 FR：FRBLOCK-023

23. **[ISOLATED] Validate Request**
   - 审查问题：Should FR-23 include a validation step for event details and recipient list before sending notifications?
   - 初步理由：FR-23 defines event details and recipient list as notification inputs but does not specify validation of those inputs, and no other original FR covers this notification-input validation obligation. The requirement is in scope for FR-23 and is not already stated.
   - 补充需求：The system shall validate event details and recipient list before sending email notifications, including handling malformed event data and invalid recipient addresses.
   - 证据 FR：FRBLOCK-023

24. **[OPERATION] User feedback email received**
   - 审查问题：Should the receipt event be reviewed to define how incoming feedback emails are recognized as feedback rather than ordinary email?
   - 初步理由：FR-24 covers receiving user email feedback and initiating parsing, storage, and notification, but it does not define how incoming emails are recognized as feedback rather than ordinary email. No other original FR addresses this recognition/detection obligation, so the nomination identifies an in-scope gap.
   - 补充需求：The system shall define and apply criteria for recognizing incoming user feedback emails, distinguishing them from ordinary email, before initiating feedback parsing and storage.
   - 证据 FR：FRBLOCK-024

## 6. Full 变体全部提名的初步去向明细

| 提名 | 来源 | 主题 | 去向 | 检查 FR 数 |
|---|---|---|---|---:|
| DEP-001 | dependency | Stage change for admin approval → Deletes the Record upon Ap | unsupported | 27 |
| DEP-002 | dependency | Validate Configuration Details → Activate Workflow | covered | 27 |
| DEP-003 | dependency | Approval-start request → Deletes the Record upon Approval | covered | 27 |
| DEP-004 | dependency | Validates the Request → Update status to Modified | covered | 27 |
| DEP-005 | dependency | Senior Admin Approval Event → Workflow Configured | covered | 27 |
| DEP-006 | dependency | Asset Request Form → User Notification | covered | 27 |
| DEP-007 | dependency | Activate Workflow → Workflow Configured | covered | 27 |
| DEP-008 | dependency | Validates the Request → Update Status on Approval | covered | 27 |
| DEP-009 | dependency | Query Approval Status → Approval Status Details | covered | 27 |
| DEP-010 | dependency | Approve Asset Request → Notify Users | covered | 27 |
| DEP-011 | dependency | Validate approval-start request → Updated operation status | covered | 27 |
| DEP-012 | dependency | Transfer form → Transfer Asset | covered | 27 |
| DEP-013 | dependency | Admin approval → Operation executed upon approval | covered | 27 |
| DEP-014 | dependency | Update record upon approval → Status Modified | covered | 27 |
| DEP-015 | dependency | Return Form → Update Asset Status to Returned | covered | 27 |
| DEP-016 | dependency | Approval-start request → Admin approval | covered | 27 |
| DEP-017 | dependency | Validate Export Request → Generate Export File | retained | 27 |
| DEP-018 | dependency | Export Asset Data → Downloadable Data File | covered | 27 |
| DEP-019 | dependency | Validate modification data → Operation executed upon approva | covered | 27 |
| DEP-020 | dependency | Approval-start request → Transferred | covered | 27 |
| ISOLATED-d1066142271d | isolated | Admin | unsupported | 27 |
| ISOLATED-044802effbcc | isolated | Administrator | unsupported | 27 |
| ISOLATED-9149814de7ba | isolated | Approved | unsupported | 27 |
| ISOLATED-daaeb9300bbd | isolated | Rejected | covered | 27 |
| ISOLATED-f5224f8482e4 | isolated | Pending Operation Status | unsupported | 27 |
| ISOLATED-ba6a57af5568 | isolated | Senior-admin approval required | unsupported | 27 |
| OPERATION-b807960581b0 | operation | Validate Format and Data | covered | 27 |
| OPERATION-98825bf8189d | operation | Validate Request | unsupported | 27 |
| OPERATION-2ea44500eb25 | operation | Register Asset | covered | 27 |
| ISOLATED-d358ae02cf93 | isolated | Asset change | covered | 27 |
| ISOLATED-459a1ecfc528 | isolated | Pending Operation Status | unsupported | 27 |
| ISOLATED-f67005874d69 | isolated | Rejected | unsupported | 27 |
| OPERATION-ea6286e46001 | operation | Admin approval | covered | 27 |
| OPERATION-ff6b3834715d | operation | Validate modification data | unsupported | 27 |
| OPERATION-0ed356b48243 | operation | Search Criteria | retained | 27 |
| OPERATION-2d97fdd0a6fa | operation | Detailed Asset Information | retained | 27 |
| OPERATION-c843a38b171b | operation | Query Asset Details | retained | 27 |
| ISOLATED-20384ad562a3 | isolated | User | unsupported | 27 |
| ISOLATED-e007997cbd37 | isolated | Admin | unresolved | 27 |
| ISOLATED-825837f19fdf | isolated | Admin | unsupported | 27 |
| ISOLATED-7a23cce0e16e | isolated | User | unsupported | 27 |
| OPERATION-adfb4fa116e9 | operation | Stage for Admin Approval | covered | 27 |
| OPERATION-68d62426114c | operation | Validate Transfer Request | unsupported | 27 |
| OPERATION-4195d119d49c | operation | Validate Return Request | covered | 27 |
| OPERATION-83347e845ab7 | operation | Stage Return Request for Approval | covered | 27 |
| ISOLATED-c388417a50b6 | isolated | Admin | unsupported | 27 |
| ISOLATED-859c44819ae0 | isolated | Approved Operation Status | retained | 27 |
| ISOLATED-33bad7fff5d4 | isolated | Admin | unsupported | 27 |
| ISOLATED-ede671a617dc | isolated | User | covered | 27 |
| OPERATION-d5ba3481d03e | operation | Validates the Request | retained | 27 |
| OPERATION-708054f5e4c9 | operation | Staged for Admin Approval | covered | 27 |
| OPERATION-d36187c6c802 | operation | Deletes the Record upon Approval | covered | 27 |
| OPERATION-9a439ea4fd4a | operation | Deleted | retained | 27 |
| ISOLATED-957727eced12 | isolated | Rejected | retained | 27 |
| ISOLATED-c8b4649552bc | isolated | Senior Admin | covered | 27 |
| ISOLATED-b16c4e46d5b9 | isolated | Administrator | retained | 27 |
| OPERATION-6dad9e4442d3 | operation | Create New User Accounts | covered | 27 |
| ISOLATED-c5dde45e21d1 | isolated | Send Activation Email | unsupported | 27 |
| OPERATION-0248a93d5d86 | operation | Validate New-User Form | retained | 27 |
| ISOLATED-724f07c00d89 | isolated | Admin | covered | 27 |
| ISOLATED-e9e8dfe097d3 | isolated | User | covered | 27 |
| OPERATION-341281d8626e | operation | Edit User Profile | covered | 27 |
| OPERATION-8f9b6d7a98f0 | operation | Validate changes | covered | 27 |
| OPERATION-fc9d11336064 | operation | Stage for Admin Approval | covered | 27 |
| OPERATION-c0abc85e62f9 | operation | Update record upon approval | covered | 27 |
| OPERATION-221783513b36 | operation | Query User Details | retained | 27 |
| OPERATION-8b23751e0fd5 | operation | Search Criteria | unresolved | 27 |
| OPERATION-24e3fbca4beb | operation | Detailed User Information | unsupported | 27 |
| ISOLATED-3e58f0e17748 | isolated | Senior Admin | retained | 27 |
| ISOLATED-5e5d6c90b522 | isolated | Senior-admin approval required | covered | 27 |
| OPERATION-32a2091203d4 | operation | Validate deletion request | unsupported | 27 |
| OPERATION-b9d92b5b9e9c | operation | Stage deletion request for senior-admin approval | retained | 27 |
| OPERATION-cb8d7532ff04 | operation | Delete user record upon approval | unresolved | 27 |
| ISOLATED-14a701f1d88e | isolated | Senior Admin | unsupported | 27 |
| OPERATION-56bc2510007a | operation | Stage Setup for Approval | unsupported | 27 |
| OPERATION-3708a8a4d2ac | operation | Activate Workflow | unsupported | 27 |
| ISOLATED-83757b27b91c | isolated | Senior-admin approval required | covered | 27 |
| OPERATION-d1e4bd1519a0 | operation | Validate Configuration Details | unsupported | 27 |
| OPERATION-d28b19313156 | operation | Validate approval-start request | unsupported | 27 |
| OPERATION-b5b29818d27f | operation | Request staged for admin review | unsupported | 27 |
| OPERATION-93b036c2ad5b | operation | Operation executed upon approval | unsupported | 27 |
| OPERATION-2b96ddcf61b1 | operation | Approval-process record | unsupported | 27 |
| OPERATION-a52fa15b6dfc | operation | Updated operation status | retained | 27 |
| ISOLATED-db8ac57b8543 | isolated | Administrator | covered | 27 |
| ISOLATED-4a224f68464a | isolated | Pending Operation Status | retained | 27 |
| ISOLATED-911630959b5e | isolated | Approved Operation Status | covered | 27 |
| ISOLATED-42f3bcbd7ee5 | isolated | Pending Operation Status | covered | 27 |
| ISOLATED-e9103c4532c9 | isolated | In Progress Operation Status | retained | 27 |
| ISOLATED-a4f24f32cb8c | isolated | Approved Operation Status | covered | 27 |
| ISOLATED-adb9b108359a | isolated | Rejected Operation Status | retained | 27 |
| OPERATION-bc3c4ea6b068 | operation | Query Approval Status | covered | 27 |
| ISOLATED-e3ada15f48b2 | isolated | Administrator | covered | 27 |
| ISOLATED-fb4d19aab360 | isolated | Senior Admin | covered | 27 |
| OPERATION-6f552f59b619 | operation | Validate changes | unsupported | 27 |
| OPERATION-bc681d787c40 | operation | Stage for senior-admin approval | unsupported | 27 |
| OPERATION-99ef3818d8be | operation | Update workflow upon approval | unsupported | 27 |
| OPERATION-cbfa2784d062 | operation | Generate Report | covered | 27 |
| OPERATION-8de292cc0fc2 | operation | Validate Parameters | retained | 27 |
| OPERATION-a11d4f07827f | operation | Store Report Data | covered | 27 |
| ISOLATED-f37902da5a23 | isolated | User | unsupported | 27 |
| OPERATION-5667d580877a | operation | Export Report | unsupported | 27 |
| OPERATION-7d40820a4dfe | operation | Validate Request | covered | 27 |
| OPERATION-f85309d51fe8 | operation | Prepare File | covered | 27 |
| OPERATION-d37190e3c728 | operation | Provide Download Link | unsupported | 27 |
| ISOLATED-1622a28977c8 | isolated | Validate Format and Data | unsupported | 27 |
| ISOLATED-6c6c597c46ef | isolated | Admin | unresolved | 27 |
| ISOLATED-34923dc6563b | isolated | User | unsupported | 27 |
| ISOLATED-a0386616efc8 | isolated | Validate Format and Data | retained | 27 |
| ISOLATED-edf318343ab2 | isolated | Parse Rows | covered | 27 |
| OPERATION-5aed8aeb7583 | operation | Store Valid Records | covered | 27 |
| OPERATION-5687cabe9346 | operation | Import Asset Data | covered | 27 |
| ISOLATED-8fd3b0b29f60 | isolated | User | unsupported | 27 |
| ISOLATED-56af8b264615 | isolated | Provide Download Link | unsupported | 27 |
| OPERATION-c659aea78e2b | operation | Validate Export Request | covered | 27 |
| OPERATION-631356f984fd | operation | Generate Export File | unsupported | 27 |
| OPERATION-5971ac5c5791 | operation | Export Log | unsupported | 27 |
| ISOLATED-491af8fdbe13 | isolated | Senior-admin | covered | 27 |
| ISOLATED-ebbea5ee7893 | isolated | Validate Request | unsupported | 27 |
| OPERATION-2fe03193e418 | operation | Stage for senior-admin approval | covered | 27 |
| OPERATION-3db9604ac109 | operation | Update permissions upon approval | unsupported | 27 |
| OPERATION-81a9c2e5c7e3 | operation | Validate replacement request | covered | 27 |
| OPERATION-1bd9143950bf | operation | Stage replacement request for approval | covered | 27 |
| OPERATION-05728143a641 | operation | Update admin records | covered | 27 |
| ISOLATED-1c338daa0efb | isolated | Validate Request | covered | 27 |
| ISOLATED-2d882721a3d3 | isolated | Senior Admin | covered | 27 |
| ISOLATED-70d8c1e78f80 | isolated | Admin | covered | 27 |
| ISOLATED-e2f6b0c7c3fb | isolated | Approved | covered | 27 |
| ISOLATED-3e8a39ec0a22 | isolated | Rejected | covered | 27 |
| ISOLATED-32fea840faa7 | isolated | User | covered | 27 |
| ISOLATED-0ba7c4b2ad70 | isolated | Validate Request | covered | 27 |
| OPERATION-75d55acc1863 | operation | Stage for Admin Approval | covered | 27 |
| OPERATION-75e2194992f5 | operation | Update Status on Approval | covered | 27 |
| OPERATION-77973b511a41 | operation | Validate Asset Request | covered | 27 |
| OPERATION-6316cf9ef179 | operation | Approve Asset Request | covered | 27 |
| OPERATION-440049b1120b | operation | Update Request Status | retained | 27 |
| OPERATION-d3de97a97598 | operation | Notify Users | unsupported | 27 |
| ISOLATED-67108fa4ecd4 | isolated | Approved | covered | 27 |
| ISOLATED-911872c414fc | isolated | Rejected | covered | 27 |
| ISOLATED-9ec0bc10d57e | isolated | User | retained | 27 |
| OPERATION-379748a60e49 | operation | Send Email Notification | retained | 27 |
| OPERATION-870acc45a56e | operation | Send Log | unsupported | 27 |
| ISOLATED-2e022473533a | isolated | Send Activation Email | covered | 27 |
| ISOLATED-5c7e2cede559 | isolated | Validate Request | retained | 27 |
| OPERATION-9e191a5ec509 | operation | Registration Event | covered | 27 |
| ISOLATED-872365a48ac4 | isolated | User | covered | 27 |
| ISOLATED-df354a020ab0 | isolated | Admin | covered | 27 |
| OPERATION-c3bd71e959c6 | operation | Parse feedback content | unsupported | 27 |
| OPERATION-630126661d60 | operation | Store feedback | unsupported | 27 |
| OPERATION-bfe98507bbf7 | operation | Notify administrators | unsupported | 27 |
| OPERATION-6b332b76a110 | operation | User feedback email received | retained | 27 |
| OPERATION-8e17c4a9b1c8 | operation | View Asset Change History | covered | 27 |
| ISOLATED-f936d48eb19f | isolated | Asset change | covered | 27 |
| ISOLATED-966b14fa047d | isolated | Admin | covered | 27 |
| ISOLATED-8f17339ab982 | isolated | Approved | unsupported | 27 |
| ISOLATED-26e934f42fb0 | isolated | Asset Count | covered | 27 |
| ISOLATED-6deda0548adc | isolated | User | covered | 27 |
| OPERATION-dab987d864c0 | operation | Query Asset Category | covered | 27 |
| OPERATION-31fd992bafac | operation | Query Asset Category | covered | 27 |
| ISOLATED-fd0f340f94bd | isolated | Administrator | covered | 27 |
| ISOLATED-11e12d4a820b | isolated | Admin | unsupported | 27 |
| ISOLATED-a1679bb4f05e | isolated | Senior Admin | covered | 27 |
| ISOLATED-928137178aed | isolated | Senior-admin | covered | 27 |
| ISOLATED-e35ce530cb8c | isolated | Approved | covered | 27 |
| OPERATION-261c34d149c8 | operation | Validate changes | covered | 27 |
| OPERATION-ff88523ca27e | operation | Edit Asset Category | covered | 27 |
| OPERATION-ef10e457aa3d | operation | Update Category Upon Approval | covered | 27 |

## 7. 人工判定：RQ2 固定候选池

- 候选数 **20**；依赖有原文依据 **13/20**；缺失义务成立 **0/20**
- 人工义务 ID：**无**

| 候选ID | 依赖有据 | 缺失义务成立 | 人工义务ID | 依据／否决原因 |
|---|---|---|---|---|
| DEP-001 | 否 | 否 |  | 原文 FR-02 只要求“暂存资产修改以等待管理员审批”、FR-06 只要求“经管理员批准后删除记录”，两条义务互不相干，原文从未规定修改暂存会触发记录删除；该边仅经通用“admin approval”事件在图上跨 FR-02/FR-06 可达，参考基准亦无此义务。 |
| DEP-002 | 是 | 否 |  | 原文 FR-11 的义务句已完整规定“校验配置详情→报上级管理员审批→批准后激活工作流”，校验作为激活的前置已属原文义务，源与目标同属 FR-11；参考基准 FR-45 新增的是激活被拒时保留原状态并给出原因，本候选未涉及。 |
| DEP-003 | 否 | 否 |  | 关键动作“批准后删除记录”已由原文 FR-06 的义务句规定（暂存待管理员审批、批准后删除记录），源元素却取自原文 FR-12 的“Approval-start request”，原文 FR-12 的操作清单只有 registration、usage、transfer、return，跨 FR-12→FR-06 的这层依赖原文未直接规定；参考基准 FR-27 只是把删除并入审批发起操作清单，删除义务本身原文已覆盖。 |
| DEP-004 | 否 | 否 |  | 源为原文 FR-06 资产删除请求的校验、目标为 FR-02 修改后的状态“Modified”，原文与参考基准均未把“删除请求校验”与“修改状态更新”相连，属跨 FR 的图上可达路径。 |
| DEP-005 | 是 | 否 |  | 原文 FR-11 的义务句已规定经上级管理员批准后激活工作流并输出状态“Configured”，源（senior-admin approval）与目标（Configured）的关系已在 FR-11 内声明；参考基准 FR-44 与原 FR-11 一致，无新增义务。 |
| DEP-006 | 否 | 否 |  | 源为原文 FR-21 的“Asset-request form”输入、目标为 FR-22 Output 的“user notification”，分属两条 FR；原文只分别规定“提交资产申请并存储”与“审批后更新状态并通知用户”，该 5 跳链路属图上可达，非同一 FR 内的义务依赖。 |
| DEP-007 | 是 | 否 |  | 原文 FR-11 的义务句已规定“activates the workflow upon approval”并以状态“Configured”作为输出，激活—状态关系已在原文；参考基准 FR-45 新增的是激活失败的降级处理，本候选未涉及。 |
| DEP-008 | 否 | 否 |  | 源为原文 FR-06 资产删除请求的校验、目标为 FR-21 资产申请的状态更新，两者对象不同（资产删除 vs 资产申请），原文与参考基准均未建立该依赖关系。 |
| DEP-009 | 是 | 否 |  | 原文 FR-13 的义务句已规定用户按资产 ID、操作类型、用户 ID 查询审批状态并输出“Approval status details”，查询—状态详情关系已在原文；参考基准 FR-39 至 FR-43 新增的是失败态、检索授权与未命中处理，本候选未涉及。 |
| DEP-010 | 是 | 否 |  | 原文 FR-22 的义务句已写明管理员审批后“updates the request status and notifies users”，通知用户的义务已在原文；参考基准 FR-48 细化的是审批结果通知对象，本候选未提出新义务。 |
| DEP-011 | 是 | 否 |  | 原文 FR-12 的义务句已包含“校验请求→暂存待管理员复核→批准后执行操作”并输出更新后的操作状态，源与目标同属 FR-12；参考基准 FR-28/FR-29 新增的是审批记录创建失败与工作流配置缺失的处理，本候选未涉及。 |
| DEP-012 | 是 | 否 |  | 原文 FR-04 的 Input 行已声明“Transfer form（asset ID、new recipient）”为转移功能的输入，输入—功能的数据流已由原文声明覆盖；参考基准 FR-13 即原 FR-04，无新增义务。 |
| DEP-013 | 是 | 否 |  | 原文 FR-12 的义务句已规定“executes the operation upon approval”（注册、使用、转移、归还四类操作），审批触发操作执行已在原文；参考基准 FR-27 仅把操作清单扩展到修改与删除，触发关系本身未变。 |
| DEP-014 | 是 | 否 |  | 原文 FR-08 的义务句已规定批准后更新用户记录，Output 行明确该记录状态为“Modified”，义务与状态均已在原文；参考基准 FR-61 与原 FR-08 一致，无新增义务。 |
| DEP-015 | 是 | 否 |  | 原文 FR-05 的义务句已含 Return form 输入与“updates the status to Returned upon approval”，归还表单——归还状态的关系已在原文；参考基准 FR-20 新增的是归还结果终态收敛，本候选未涉及。 |
| DEP-016 | 是 | 否 |  | 原文 FR-12 的义务句已规定审批发起请求经校验后“stages it for admin review”（即进入管理员审批），输入—审批前置关系已在 FR-12 内声明；参考基准 FR-28/FR-29 新增的是审批记录创建与工作流配置缺失的失败处理。 |
| DEP-017 | 是 | 否 |  | 原文 FR-18 的义务句已写明先校验导出请求再生成导出文件，校验作为生成文件的前置已在原文规定；参考基准 FR-88 新增的是导出数据范围授权，本候选未涉及。 |
| DEP-018 | 是 | 否 |  | 原文 FR-18 的义务句与 Output 行已规定校验请求、生成文件并提供下载链接、输出“Downloadable data file”，导出功能—数据文件关系已覆盖；参考基准 FR-87 与原 FR-18 一致，无新增义务。 |
| DEP-019 | 否 | 否 |  | 源为原文 FR-02 的修改数据校验、目标为 FR-12 的“批准后执行操作”，两元素分属两条 FR；原文 FR-02 已规定修改经批准后生效、FR-12 已规定批准后执行操作，此跨 FR 组合不构成参考基准新增义务（FR-27 只是把修改并入审批发起操作清单）。 |
| DEP-020 | 否 | 否 |  | 源为原文 FR-12 的审批发起请求、目标为 FR-04 的状态“Transferred”，分属两条 FR；原文已分别规定转移属审批发起的操作之一（FR-12）与批准后更新归属、状态为 Transferred（FR-04），参考基准 FR-16 新增的是转移状态生命周期，本候选未涉及。 |

## 8. 人工判定：RQ3 提名去向

- 审阅行数 **223**（Full 166，NoFullDocumentValidation 17，NoIsolatedReview 34，NoSignedPropagation 6）

| 人工去向 | 行数 |
|---|---:|
| 已覆盖·语义重复 | 176 |
| 有效且缺失 | 20 |
| 缺乏依据·过度推断 | 20 |
| 待澄清 | 7 |

- 有效且缺失 **20** 行，对应 **15** 个义务 ID：O-01, O-02, O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11, O-12, O-13, O-14, O-15

| 义务ID | 版本 | 提名ID | 路线 | 原文依据 | 理由 |
|---|---|---|---|---|---|
| O-01 | Full | ISOLATED-9149814de7ba | isolated | 参考基准 FR-25 | 参考基准 FR-25 要求定义资产或用户状态的允许转换，原文 FR-01 未规定 Registered 之后可否转为 Approved。 |
| O-01 | Full | ISOLATED-daaeb9300bbd | isolated | 参考基准 FR-25; 参考基准 FR-38 | 参考基准 FR-25 要求定义状态转换、FR-38 要求被拒请求有明确终态，原文 FR-01 未规定注册审核可致 Rejected。 |
| O-02 | Full | ISOLATED-d358ae02cf93 | isolated | 参考基准 FR-90; 原文 FR-02 | 参考基准 FR-90 要求为所有改变资产状态的操作记录变更历史，原文只规定修改暂存待批。 |
| O-03 | Full | ISOLATED-f67005874d69 | isolated | 参考基准 FR-38; 参考基准 FR-07 | 参考基准 FR-38 与 FR-07 要求被拒请求及修改请求有明确终态，原文 FR-02 未规定管理员拒绝及其结果。 |
| O-04 | Full | OPERATION-c843a38b171b | operation | 参考基准 FR-10; 参考基准 FR-11 | 参考基准 FR-10 与 FR-11 要求资产检索无匹配或条件无效时给出确定结果与改进指引，原文 FR-03 未规定。 |
| O-05 | Full | ISOLATED-7a23cce0e16e | isolated | 参考基准 FR-14 | 参考基准 FR-14 要求转移请求仅来自获授权主体，原文 FR-04 只说 Users 可请求，未设授权约束。 |
| O-06 | Full | OPERATION-adfb4fa116e9 | operation | 参考基准 FR-16 | 参考基准 FR-16 要求转移操作具备明确的状态生命周期（含批准与拒绝去向），原文 FR-04 只提批准后更新归属。 |
| O-07 | Full | OPERATION-68d62426114c | operation | 参考基准 FR-12 | 参考基准 FR-12 要求转移等资产操作前校验资产标识并阻止无效记录下游操作，原文 FR-04 仅泛称校验请求。 |
| O-08 | Full | ISOLATED-957727eced12 | isolated | 参考基准 FR-23 | 参考基准 FR-23 要求删除无法完成时给出阻塞原因与允许的下一步，原文 FR-06 未规定未获批准时的结果。 |
| O-09 | Full | ISOLATED-b16c4e46d5b9 | isolated | 参考基准 FR-77; 参考基准 FR-78 | 参考基准 FR-77 与 FR-78 要求核验身份并按角色做操作级授权，原文 FR-07 只写管理员建号而未规定权限核验。 |
| O-10 | Full | OPERATION-8de292cc0fc2 | operation | 参考基准 FR-83 | 参考基准 FR-83 要求报表参数缺失或无效时记录明确失败结果，原文 FR-15 未规定。 |
| O-09 | Full | ISOLATED-f37902da5a23 | isolated | 参考基准 FR-77; 参考基准 FR-78 | 参考基准 FR-77 与 FR-78 要求先核验身份再做操作授权，原文 FR-15 未规定报表生成的权限核验。 |
| O-09 | Full | ISOLATED-34923dc6563b | isolated | 参考基准 FR-77 | 参考基准 FR-77 要求按授权角色限制操作并做后端授权，原文 FR-17 只说 Users 上传文件而未规定导入权限授予。 |
| O-11 | Full | ISOLATED-8fd3b0b29f60 | isolated | 参考基准 FR-88 | 参考基准 FR-88 要求按请求主体限定资产导出范围，原文 FR-18 未设导出授权条件。 |
| O-12 | Full | OPERATION-870acc45a56e | operation | 参考基准 FR-53 | 参考基准 FR-53 要求记录通知投递尝试（含失败尝试），原文 FR-23 只声明发送日志。 |
| O-02 | Full | ISOLATED-f936d48eb19f | isolated | 参考基准 FR-90; 参考基准 FR-94; 原文 FR-25 | 参考基准 FR-90 要求为所有改动资产状态的操作记录变更历史、FR-94 要求记录准确的变更日期，原文 FR-25 仅规定可查询。 |
| O-13 | NoSignedPropagation | OPERATION-0cb6326f1c19 | operation | 参考基准 FR-24; 参考基准 FR-26 | 参考基准 FR-24 要求按资产当前状态判定操作资格、FR-26 防止并发请求产生非法状态，原文 FR-04 只泛称“校验请求”。 |
| O-14 | NoSignedPropagation | OPERATION-51d10671e3e6 | operation | 参考基准 FR-60; 参考基准 FR-55 | 参考基准 FR-60 要求账户相关更新无法完成时一致恢复状态、FR-55 要求记录激活邮件投递尝试，原文 FR-07 未规定邮件失败不得留下部分创建的用户记录。 |
| O-09 | NoIsolatedReview | OPERATION-c99df48e3eac | operation | 参考基准 FR-77; 参考基准 FR-78 | 参考基准 FR-77/FR-78 要求每个操作按角色授权并先核验身份，原文 FR-21 只说 Users 可提交资产申请。 |
| O-15 | NoIsolatedReview | OPERATION-fef904856305 | operation | 参考基准 FR-96 | 参考基准 FR-96 要求按已配置的允许集合校验变更类型，原文 FR-25 只声明可按变更类型查询。 |

---

## 9. RQ2 预算对比（人工判定）

判定依据：只比较 `source/original_document.txt`（原文 FR-01…FR-27）与`reference_Inventory.txt`（参考基准 FR-01…FR-107）。20 条候选各判一次，三条排序复用同一套判定。

### 1. 判定汇总

- 依赖有原文依据（依赖有据=是）：13/20（其余 7 条为跨 FR 的图上可达路径：DEP-001、DEP-003、DEP-004、DEP-006、DEP-008、DEP-019、DEP-020）
- 缺失义务成立=是：**0 条**；=否：20/20；=待澄清：0/20
- 因此人工确认的有效缺失义务共 **0 个**（人工义务ID 集合为空：无）。

判为“否”的理由分两类：（a）13 条候选的源与目标同属一个原文 FR，该 FR 的义务句（Description）已直接规定关键动作与结果状态（如 FR-08 更新用户记录并置“Modified”、FR-11 激活工作流并置“Configured”、FR-12 批准后执行操作、FR-18 校验后生成导出文件、FR-22 审批后通知用户）；（b）7 条候选的源与目标分属两个 FR，原文没有任何义务句把两者相连，只是抽取图上经通用“Admin approval”“Staged for Admin Approval”等节点可达，而它们各自的目标义务又已被原文覆盖（FR-06 批准后删除记录、FR-02 批准后置“Modified”、FR-04 批准后置“Transferred”、FR-22 通知用户等）。

参考基准中确有针对这些功能的新增义务（如 FR-27 把 modification、deletion 并入审批发起操作清单、FR-16 转移状态生命周期、FR-45 工作流激活失败降级、FR-48 审批结果通知、FR-20 归还结果终态、FR-88 导出范围授权、FR-28/FR-29 审批记录与工作流配置失败处理），但 20 条候选的关键动作与对象均未落在这些新增义务上，故本池无有效候选。

### 2. 预算对比（不同人工预算下发现的**去重**缺失义务数）

| 审查预算（候选数） | ACE 排序 | 可达性排序 | 随机排序 |
|---:|---:|---:|---:|
| 5 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |

注：三个预算下三条排序的有效缺失义务数均为 **0**（人工义务ID 集合为空，任何一个预算都不可能出现非零计数），三者无差异。

### 3. 有效候选在各排序中的位次

人工确认的有效候选数为 0，故每条排序都不存在“有效候选位次”可列。

为便于核对，下表给出最接近参考基准新增义务的 7 条“图上可达”候选在三条排序中的位次（它们全部被判为依赖无据、缺失不成立）：

| 候选ID | 源→目标 | ACE 位次 | 可达性位次 | 随机位次 |
|---|---|---:|---:|---:|
| DEP-003 | Approval-start request → Deletes the Record upon Approval | 19 | 1 | 10 |
| DEP-019 | Validate modification data → Operation executed upon approval | 15 | 7 | 8 |
| DEP-020 | Approval-start request → Transferred | 20 | 3 | 6 |
| DEP-001 | Stage change for admin approval → Deletes the Record upon Approval | 11 | 8 | 2 |
| DEP-004 | Validates the Request → Update status to Modified | 13 | 4 | 20 |
| DEP-006 | Asset Request Form → User Notification | 18 | 10 | 12 |
| DEP-008 | Validates the Request → Update Status on Approval | 17 | 5 | 7 |

结论：在本固定池上，三条排序在任何预算下都未能发现人工确认的缺失义务（有效数 = 0），本文件据实记录该零结果，不做外推。

---

## 10. RQ3 组件贡献（人工判定）

Full 的 166 条逐条人工审阅；四个消融版只对新增/消失条目单独审阅，其余条目继承其对 Full 匹配项的判定。

| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |
|---|---:|---:|---:|---|---|---|
| NoSignedPropagation | 174 | 6 | 9 | O-01, O-02, O-04, O-06, O-07, O-10, O-12, O-13, O-14 | O-03, O-05, O-08, O-09, O-11 | O-13, O-14 |
| NoIsolatedReview | 161 | 34 | 7 | O-04, O-06, O-07, O-09, O-10, O-12, O-15 | O-01, O-02, O-03, O-05, O-08, O-11 | O-15 |
| NoOperationReview | 196 | 0 | 2 | O-01, O-02 | O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11, O-12 | — |
| NoFullDocumentValidation | 181 | 17 | 7 | O-01, O-02, O-04, O-06, O-07, O-10, O-12 | O-03, O-05, O-08, O-09, O-11 | — |

### 消融时的“补位”检查

- **NoOperationReview**（operation 路线关闭，isolated 由 70 增至 176）：这 176 条 isolated 提名的对齐情况为 与 Full 的 isolated 提名对齐 144 条、与 Full 的 operation 提名对齐 32 条；人工判定下该版本有效义务 2 条（失去 10 条：O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11, O-12，新增 0 条）。

- **NoIsolatedReview**（isolated 路线关闭，operation 由 76 增至 141）：这 141 条 operation 提名的对齐情况为 与 Full 的 operation 提名对齐 86 条、真正的新条目 34 条、与 Full 的 isolated 提名对齐 20 条、与 Full 的依赖提名对齐 1 条；人工判定下该版本有效义务 7 条（失去 6 条：O-01, O-02, O-03, O-05, O-08, O-11，新增 1 条：O-15）。

- **NoSignedPropagation**：有效义务 9 条（失去 5 条：O-03, O-05, O-08, O-09, O-11，新增 2 条：O-13, O-14）。

- **NoFullDocumentValidation**：有效义务 7 条（失去 5 条：O-03, O-05, O-08, O-09, O-11，新增 0 条）。
