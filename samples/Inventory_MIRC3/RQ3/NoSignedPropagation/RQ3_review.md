# RQ3 审查材料：Inventory_MIRC3 / NoSignedPropagation

**注意：下列去向只是模型初步筛查，不是人工有效性结论。**

## 运行设置

```json
{
  "signed_propagation": false,
  "isolated_review": true,
  "operation_review": true,
  "full_document_validation": true
}
```

## dependency：20 条提名

### DEP-001
- 主题：Stage change for admin approval → Deletes the Record upon Approval
- 审查问题：Does the requirement specify that, once a change is staged for admin approval, the admin approval event triggers deletion of the associated record, as indicated by the FR phrases 'stages the change for admin approval' and 'deletes the record upon approval'?
- 场景：A change is staged and remains pending admin approval. After the admin approves the staged change, the system is expected to delete the associated obsolete asset record.
- 模型初步去向：covered
- 模型解释：An original FR, FRBLOCK-006, already states that a deletion request is staged for admin approval and the record is deleted upon approval. This is equivalent to the draft obligation; no new business obligation is introduced.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006, FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Upon admin approval of a staged change, the system shall delete the associated obsolete asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Validate Configuration Details → Activate Workflow
- 审查问题：Should Activate Workflow be explicitly conditioned on Validate Configuration Details succeeding, or is the required senior-admin approval alone sufficient to trigger activation?
- 场景：A configuration setup is validated, staged for senior-admin approval, approved by a senior admin, and then the workflow is activated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already specifies that the system validates configuration details, stages the setup for senior-admin approval, and activates the workflow upon approval. This provides the same business obligation as the draft: activation requires prior configuration validation and senior-admin approval.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The workflow shall be activated only after configuration details have been validated and senior-admin approval has been granted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Approval-start request → Deletes the Record upon Approval
- 审查问题：Does the FR specify that the deletion of the record upon approval depends on a validated approval-start request being staged for admin review before admin approval is granted?
- 场景：An approval-start request is submitted; the system validates the request and stages it for admin review; admin approval is then granted.
- 模型初步去向：covered
- 模型解释：The checked original FRBLOCK-006 already states the equivalent obligation: the system validates the request, stages it for admin approval, and deletes the record upon approval. That covers the nominated dependency of deletion upon approval after validation and staging for admin approval. FRBLOCK-010 provides similar coverage for senior-admin approval.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall delete the record upon approval only after the approval-start request has been validated, staged for admin review, and granted admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Validates the Request → Update status to Modified
- 审查问题：Does the requirement clearly state that updating the asset record status to 'Modified' is contingent on admin approval of the validated deletion request, rather than occurring immediately upon validation?
- 场景：A deletion request is validated by the system and staged for admin approval. The requirements state that the system validates the request, stages it for admin approval, and upon approval updates the status to 'Modified'. The dependency shows validation leads to staging, staging enables admin approval, and admin approval triggers the status update.
- 模型初步去向：unsupported
- 模型解释：The draft links approval of a validated deletion request to changing the asset record status to 'Modified'. FRBLOCK-006 covers deletion requests but specifies that admin-approved deletion results in status 'Deleted', not 'Modified'. FRBLOCK-002 covers updating status to 'Modified' upon approval, but for asset modification, not for a deletion request. No original FR supports changing a deletion-requested asset record to 'Modified'.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system shall update the asset record status to 'Modified' only after an admin approves the validated deletion request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Senior Admin Approval Event → Workflow Configured
- 审查问题：Does the requirement need to obligate that a senior-admin approval event results in the workflow being stored with status 'Configured,' or is 'Configured' only an observed outcome of workflow activation?
- 场景：A senior admin approves a workflow. FRBLOCK-011 states that 'senior-admin approval' 'activates the workflow' and that activation produces a 'Stored workflow with status “Configured.”' The review must determine whether the Configured status is a required target state of the approval event or merely an intermediate output.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that senior-admin approval activates the workflow and that the output is a stored workflow with status 'Configured,' which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：When a senior-admin approval event occurs, the workflow shall be activated and the stored workflow shall have status 'Configured.'
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Asset Request Form → User Notification
- 审查问题：Does the requirement set specify that a user who submits an asset request form must receive a notification after that request is approved or rejected?
- 场景：A user submits an asset request form with name, type, quantity, and purpose. An administrator reviews the stored request and approves or rejects it. The system then notifies the user about the request decision.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already specifies that after administrators approve or reject asset requests, the system updates the request status and notifies users, which is equivalent to notifying the requesting user when their submitted asset request is approved or rejected.
- 原文证据 FR：FRBLOCK-021, FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall notify the requesting user when their submitted asset request is approved or rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Activate Workflow → Workflow Configured
- 审查问题：For FRBLOCK-011, should the requirements explicitly state that activating the workflow produces a stored workflow with status “Configured”?
- 场景：A workflow is activated as described in FRBLOCK-011, and the resulting workflow status is reviewed against the documented dependency.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the workflow is activated upon approval and that the output is a stored workflow with status “Configured,” which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：When the workflow is activated, the system shall produce a stored workflow with status “Configured.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Validates the Request → Update Status on Approval
- 审查问题：Does the requirement specify that the system must 'updates status upon approval' only after the request is validated, staged for admin approval, and then receives admin approval?
- 场景：A request is validated, staged for admin approval, and approved by an admin; the system updates status upon approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states the same obligation: 'The system validates the request, stages it for admin approval, and updates status upon approval.' This directly covers the nominated requirement that status is updated upon admin approval only after validation and staging.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system shall update the request status upon admin approval after the request has been validated and staged for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Query Approval Status → Approval Status Details
- 审查问题：Does FRBLOCK-013 define the required contents of 'Approval Status Details' that the Query Approval Status function must produce?
- 场景：A user checks the status of an asset or user operation. The Query Approval Status function is expected to produce Approval Status Details as output, but the requirement may not fully specify what those details include.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already specifies that the Query Approval Status function outputs approval status details when users check the status of asset or user operations, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：When a user queries the approval status of an asset or user operation, the system shall return the approval status details for that operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Approve Asset Request → Notify Users
- 审查问题：Does FRBLOCK-022 specify what the system must communicate when it "notifies users" after an administrator approves or rejects an asset request?
- 场景：An administrator reviews an asset request and makes an approve or reject decision. The requirement states the system "notifies users", but the notification content tied to the decision is not further detailed.
- 模型初步去向：retained
- 模型解释：FRBLOCK-022 requires the system to notify users after an administrator approves or rejects an asset request, but it does not specify that the notification must communicate the request decision. The dependency evidence shows the approval/rejection decision triggers the notification, supporting the more specific obligation that users be notified of the decision. This obligation is in scope and not stated equivalently in the original FRs.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：When an administrator approves or rejects an asset request, the system must notify users of the request decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Validate approval-start request → Updated operation status
- 审查问题：Do the requirements explicitly state that the updated operation status can only be produced after the approval-start request has been validated and subsequently executed upon approval?
- 场景：The FR block describes a sequence where validating the approval-start request stages it for admin review, and upon approval the operation is executed, producing an updated operation status. The dependency analysis shows a positive propagation path from validation to the updated status, but the requirements do not explicitly link the validation outcome to the production of the updated status.
- 模型初步去向：retained
- 模型解释：FRBLOCK-012 describes validation, staging, approval-driven execution, and updated operation status as an output, but does not explicitly state the 'only after' dependency. The dependency evidence establishes a positive propagation chain from validation to the updated status, so the sequencing obligation is supported but not already stated in the original FRs.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall produce the updated operation status only after the approval-start request has been successfully validated and the operation has been executed upon approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Transfer form → Transfer Asset
- 审查问题：Does the Transfer Asset requirement define what constitutes a valid submitted Transfer form (asset ID and new recipient) as the required input for users requesting to transfer assets?
- 场景：A user requests to transfer an asset by submitting the Transfer form with an asset ID and new recipient, and the Transfer Asset workflow depends on that form as its input.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 explicitly specifies the Transfer Asset input as a Transfer form containing an asset ID and new recipient, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The Transfer Asset workflow shall require a Transfer form containing an asset ID and a new recipient as input before processing a user request to transfer assets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Admin approval → Operation executed upon approval
- 审查问题：Does FRBLOCK-012 clearly specify that admin approval is the trigger for executing the requested operation, and does it define the execution outcome for each supported request type?
- 场景：An administrator approves a registration, usage, transfer, or return request; the system is expected to execute that operation upon approval.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-012 already describes the relevant approval-triggered execution obligation: registration, usage, transfer, or return requests are staged for administrator approval and the operation is executed upon approval. The draft restates this existing trigger/execution rule rather than adding a new business obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：When an administrator approves a registration, usage, transfer, or return request, the requested operation shall be executed upon that approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Update record upon approval → Status Modified
- 审查问题：Does the requirement specify that the approval action must update the user record and produce the status 'Modified', rather than only describing an updated record with status 'Modified'?
- 场景：An admin approves staged changes, and the system updates the user record. The source requirement says it 'updates the record upon approval'; the target requirement says the result is an 'Updated user record with status “Modified.”'
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already specifies staging changes for admin approval, updating the user record upon approval, and producing an updated user record with status “Modified.” This is equivalent to the nominated obligation, so no new supplement is needed.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Upon approval of staged changes, the system shall update the user record and set its status to 'Modified'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：Return Form → Update Asset Status to Returned
- 审查问题：Is submission of the Return Form containing asset ID and return date sufficient on its own to update the asset status to 'Returned', or does the requirement require the return request to be validated, staged for approval, and approved first?
- 场景：A user initiates an asset return by submitting the Return Form with asset ID and return date. The system validates the request, stages it for approval, and updates the status to 'Returned' upon approval. The modeled dependency links Return Form to Update Asset Status to Returned, with propagation disabled.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already states the equivalent obligation that a return request is validated, staged for approval, and the asset status is updated to “Returned” only upon approval. FRBLOCK-012 also confirms return operations require approval before execution, so the draft adds no new in-scope obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：When a Return Form with asset ID and return date is submitted and the resulting return request is approved, the system shall update the asset status to 'Returned'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Approval-start request → Admin approval
- 审查问题：Does the requirement define what must occur between an approval-start request being staged for admin review and admin approval triggering the status update?
- 场景：An approval-start request containing an asset ID and operation type is submitted, validated, and staged for admin review. The documented target is admin approval, which triggers a status update.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the validated request is staged for admin review and the operation is executed upon approval, which is equivalent to requiring admin approval before the status update/operation is triggered.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：For an approval-start request that has been validated and staged for admin review, admin approval shall be required before the status update is triggered.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Validate Export Request → Generate Export File
- 审查问题：Does the requirement explicitly connect successful validation of an export request to generation of the export file as the enabled next outcome?
- 场景：The system validates the export request successfully; the documented dependency indicates this validation enables the system to generate the export file.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states the equivalent obligation: after the system validates the request, it prepares the file and provides a download link, connecting successful validation to export file generation. The nominated draft is therefore already covered by an original FR.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：When the export request is validated successfully, the system shall generate the export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Export Asset Data → Downloadable Data File
- 审查问题：Should the requirements explicitly state that a successful 'Export Asset Data' operation results in a 'Downloadable Data File' being generated and made available for download?
- 场景：A requirements reviewer is examining the PRODUCES dependency from 'Export Asset Data' to 'Downloadable Data File' in FRBLOCK-018. The source active meaning is that the user has successfully exported the selected asset data, and the target active meaning is that the data file has been generated and is available for download.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already specifies the equivalent obligation: the system validates the export request, generates the file, and provides a download link, with the output being a downloadable data file.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：When the user successfully exports selected asset data, the system shall produce a downloadable data file and make it available for download.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Validate modification data → Operation executed upon approval
- 审查问题：Do the requirements explicitly define the dependency between successful validation of modification data and execution of the requested operation upon admin approval, including whether validation is a required precondition for the operation to be executed after approval?
- 场景：A modification request is submitted. The system validates the data, stages the change for admin approval, and, upon admin approval, executes the requested operation. The documented dependency links validation of modification data to the operation executed upon approval through staging and admin approval.
- 模型初步去向：covered
- 模型解释：The original FRs already define the equivalent obligation. FRBLOCK-012 states: "The system validates the request, stages it for admin review, and executes the operation upon approval," and FRBLOCK-008 states: "The system validates changes, stages them for admin approval, and updates the record upon approval." Together these establish the same sequence: validation and staging occur before the approved operation is executed. Therefore the nominated dependency is already covered by checked original FRs.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-008, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall execute the requested operation upon admin approval only after the modification data has been successfully validated and the change has been staged for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Approval-start request → Transferred
- 审查问题：Does the requirement set explicitly state that an approval-start request which is validated, staged for admin review, and approved must result in the ownership update and produce status “Transferred,” or is that end-to-end outcome only implied by separate FRBLOCK-012 and FRBLOCK-004 statements?
- 场景：An approval-start request containing an asset ID and operation type is submitted. The system validates the request and stages it for admin review. After admin approval, the system updates ownership upon approval and outputs updated owner information with status “Transferred.”
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already states the same end-to-end obligation: the system validates the request, stages it for admin approval, updates ownership upon approval, and outputs updated owner information with status “Transferred.” The nominated draft obligation is therefore equivalent to an existing original FR requirement.
- 原文证据 FR：FRBLOCK-004, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval of an approval-start request that has been validated and staged for admin review, the system shall update ownership and output updated owner information with status “Transferred.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：78 条提名

### ISOLATED-c50c412d193a
- 主题：Admin
- 审查问题：Should the isolated element 'Admin' be documented as an alias of 'Administrators' in FR-01, or as a distinct actor with specific registration-review responsibilities?
- 场景：During model review, the isolated actor 'Admin' appears in the graph, while FR-01 uses 'Administrators' as the notified reviewer. This requires clarification to avoid duplicate or ambiguous actor definitions.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence, FRBLOCK-001, states that 'Administrators are notified for review.' It does not mention an isolated 'Admin' actor, define an alias relationship, or assign distinct asset registration-review responsibilities. The screening notes show that no original FR establishes such an obligation, so the draft's conditional documentation requirement is unsupported.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：If 'Admin' refers to the same role, document the alias relationship; if distinct, document its responsibility in the asset registration review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3db9e5d5948d
- 主题：Approved
- 审查问题：Should the isolated state 'Approved' be documented as a possible outcome of the administrator review mentioned in FR-01?
- 场景：FR-01 sets status to 'Registered' and notifies administrators for review. The model contains an isolated 'Approved' state that may represent the review outcome, but no connection is documented.
- 模型初步去向：unsupported
- 模型解释：The cited FR-001 states only that administrators are notified for review; it does not establish that the review can approve an asset or that the status transitions from 'Registered' to 'Approved'. Other original FRs describe approval outcomes for different workflows (such as request status, transfers, returns, profiles, and permissions) and do not document the specific Registered-to-Approved transition. The draft therefore introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：If administrator review can approve an asset, document the transition from 'Registered' to 'Approved' as part of the registration workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1040964ec0ef
- 主题：Rejected Operation Status
- 审查问题：Should the isolated "Rejected Operation Status" be connected to this modification workflow when admin approval is denied?
- 场景：A staged asset modification is rejected by an admin, and the current FR only describes the approved outcome.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence describes the approved modification path: validation, staging for admin approval, and status 'Modified' upon approval. It does not state that admin approval can be denied or that a rejected modification enters a 'Rejected Operation Status' or affects the asset record. No checked original FR defines that rejection behavior for the modification workflow, so the draft introduces an unsupported policy rather than an existing or evidenced obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should document whether a rejected modification enters a Rejected Operation Status and how that status affects the asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4cc8faa8b568
- 主题：Pending Operation Status
- 审查问题：Should a staged asset modification be represented with the isolated "Pending Operation Status" while awaiting admin approval?
- 场景：A user submits a valid modification; the system stages it for admin approval, and the change is not yet approved.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system stages the request for admin review and outputs an updated operation status, which represents the pending state of a staged asset modification before approval. This is equivalent to the draft obligation to document the pending state before admin approval.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should document the pending state of a staged asset modification before admin approval is granted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-aabc9735bc49
- 主题：Administrator
- 审查问题：Is the "Admin" actor in this FR the same role as the isolated "Administrator" element for approving asset modifications?
- 场景：A staged asset modification requires admin approval, and role names Admin vs Administrator may affect permissions and routing.
- 模型初步去向：unsupported
- 模型解释：The cited evidence only states that changes are staged for 'admin approval'; it does not establish an 'Administrator' role or any requirement to consolidate role naming or explicitly distinguish 'Admin' from 'Administrator'. The draft therefore introduces a role-consistency policy that is not supported by the original FRs.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should use a single documented administrator role for approving asset modifications, or explicitly distinguish Admin from Administrator.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6dab7ad5a264
- 主题：Senior-admin approval required
- 审查问题：Does this modification workflow require Senior-admin approval in addition to Admin approval when the asset change meets certain criteria?
- 场景：A user modifies an asset and the system stages the change for admin approval; a separate "Senior-admin approval required" element exists but is not referenced.
- 模型初步去向：unsupported
- 模型解释：The nomination's evidence (FRBLOCK-002) only states that asset changes are staged for admin approval. No checked original FR describes Senior-admin approval for asset modifications or criteria requiring staged asset changes to be routed to Senior-admin in addition to Admin approval; other Senior-admin approval requirements concern different objects such as user accounts, workflows, permissions, or categories. The draft therefore introduces an unsupported approval policy for asset modifications.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：If senior approval is required for certain asset modifications, the system should document when a staged change must also be routed to Senior-admin.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-365449fb0f4f
- 主题：Approved Operation Status
- 审查问题：Should admin approval transition the staged change through the isolated "Approved Operation Status" before the asset record status becomes "Modified"?
- 场景：Admin approves a staged asset modification; the FR says the asset record status becomes Modified upon approval.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-002 only states that the asset record status is updated to “Modified” upon approval. It does not describe an isolated “Approved Operation Status,” a transition through such an intermediate status, or an obligation to document the approval status transition and its relationship to “Modified.” The draft therefore adds an unsupported requirement.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should document the approval status transition for a staged modification and how it relates to the asset record status “Modified.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-897437c99729
- 主题：Admin
- 审查问题：Does the FR need to document whether an Admin can perform Query Asset Details, or is access limited to the generic Users actor?
- 场景：An administrator needs to search asset details to audit inventory, but FR-03 only mentions Users as the actor.
- 模型初步去向：unsupported
- 模型解释：The original FR-03 only states that Users search for asset details; it does not mention Admin authorization, role-specific permissions, or conditions for Admin access. The draft introduces an Admin role access-control policy that is not supported by the checked source FRs, so it cannot be retained as a supported obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Document whether the Admin role is authorized to query asset details, and if so, under what conditions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-89b92f6bf48e
- 主题：Validate Request
- 审查问题：Should Validate Request be applied to Search Criteria before the system returns matching asset records?
- 场景：A user submits malformed search criteria (e.g., invalid ID format), and the system must decide whether to reject or ignore the request.
- 模型初步去向：unsupported
- 模型解释：The source evidence only lists Search Criteria (name, type, ID) as an input for Query Asset Details. No original FR requires validating those criteria before returning matching asset records or defines applicable validation rules; validation language elsewhere applies to registration, modification, transfer, deletion, configuration, export, and other operations, not search-criteria validation. The draft would therefore introduce a validation/documentation obligation not supported by the source.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Document whether Query Asset Details requires request validation for Search Criteria, and what validation rules apply.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a9ae428335bb
- 主题：Rejected
- 审查问题：Does the isolated 'Rejected' status need a documented connection to the admin approval workflow for transfer requests?
- 场景：An admin rejects a staged transfer request. The system needs to record the rejection and leave ownership unchanged, but FR-04 only describes approval and successful transfer.
- 模型初步去向：retained
- 模型解释：FRBLOCK-004 establishes that transfer requests are staged for admin approval and that ownership is updated upon approval, but it does not explicitly document rejection handling. No checked original FR states an equivalent obligation for rejecting a staged transfer request, recording a 'Rejected' status, and preserving asset ownership. This is an in-scope, supported extension of the transfer approval workflow.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall allow an admin to reject a staged transfer request, record the status as 'Rejected', and leave the asset ownership unchanged.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-73f3eddd9ee6
- 主题：Approved
- 审查问题：Does the isolated 'Approved' status need to be recorded when an admin approves a staged transfer request before ownership is updated?
- 场景：An admin approves a staged transfer request. The system must record the approval decision before updating ownership, but FR-04 does not name the approval status.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-004 only establishes that a transfer request is staged for admin approval and ownership is updated upon approval. It does not require recording an intermediate 'Approved' status for the staged transfer request before ownership is updated, nor does any other original FR establish that specific status/sequencing obligation. The draft therefore introduces an unsupported policy detail.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall record the admin's approval as an 'Approved' status for the staged transfer request before updating asset ownership.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e9251fd4513d
- 主题：Pending Operation Status
- 审查问题：Does the isolated 'Pending Operation Status' need a documented connection when a transfer request is staged for admin approval?
- 场景：A transfer request is staged for admin approval. The system needs to indicate that the request is pending, but FR-04 only says it is staged.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already states that a transfer request is staged for admin approval, which is equivalent to marking the request as pending until an admin approves or rejects it. The nominated obligation does not add a new in-scope business requirement beyond that existing FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall mark a staged transfer request with a pending status until an admin approves or rejects it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-931d9d9aeb0f
- 主题：Admin
- 审查问题：Should the Return Asset workflow document the role authorized to approve a staged return request, such as Admin?
- 场景：A user submits an asset return; the system stages the request for approval, but the FR does not specify who approves it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that Administrators review and approve or reject asset requests, which provides the authorized approver role for asset return requests. The Return Asset workflow stages return requests for approval, so the requested approver-role obligation is covered by the existing FR.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：Specify the authorized approver role for asset return requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e758ee174676
- 主题：Rejected
- 审查问题：Does the Return Asset workflow need a documented connection to the Rejected outcome when a return request is denied?
- 场景：A staged asset return request is not approved; the system must determine the resulting asset status and user notification.
- 模型初步去向：retained
- 模型解释：No checked original FR specifies rejection handling for the Return Asset workflow. FRBLOCK-005/FR-12 stages return requests for approval but only describes execution upon approval. FRBLOCK-013 includes 'rejected' as a queryable approval status but does not define status transition or notification for denied return requests. The obligation is in-scope because return requests are part of the system's approval workflows, but the connection to the Rejected outcome for return denial is missing.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：Define rejection handling for asset returns, including status transition and notification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c359df4e4751
- 主题：Admin
- 审查问题：Does the isolated actor 'Admin' require a documented connection to the approval step in FR-06 beyond the phrase 'admin approval'?
- 场景：A deletion request is staged and the system waits for an admin decision. The FR names 'Admin' but does not specify the admin's role, permissions, or the exact interaction for granting approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that deletion requests are staged for admin approval and that the record is deleted upon approval, which documents the Admin actor's connection to the approval step. The draft obligation is therefore already covered by the original FR.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The Admin actor must be able to review and approve staged deletion requests for obsolete assets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-bf02ea130f99
- 主题：User
- 审查问题：Does the isolated actor 'User' require a documented connection to the initiation of a deletion request in FR-06?
- 场景：A user identifies an obsolete asset and requests its removal. The FR says 'Users request removal' but does not document how the request is submitted or whether any user role restrictions apply.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that users request removal of obsolete assets, which documents the User actor's ability to initiate a deletion request for an obsolete asset. The draft obligation is therefore covered by an existing FR.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The User actor must be able to initiate a deletion request for an obsolete asset.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8b601b5502d9
- 主题：Validate Request
- 审查问题：Does the isolated element 'Validate Request' require a documented connection to the validation step in FR-06?
- 场景：A deletion request is submitted and the system validates it before staging. The FR includes 'validates the request' but the isolated element 'Validate Request' is not explicitly linked to the workflow.
- 模型初步去向：covered
- 模型解释：The checked original FRBLOCK-006 already states that the system validates the deletion request, stages it for admin approval, and deletes the record upon approval. This is equivalent to the draft obligation to validate a deletion request before staging it for admin approval.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must validate a deletion request before staging it for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5c0fb006ed5e
- 主题：Rejected
- 审查问题：Does the isolated element 'Rejected' require a documented connection to FR-06 as the alternative outcome when admin approval is denied?
- 场景：An admin reviews a staged deletion request and does not approve it. The FR only describes deletion upon approval, leaving the rejected outcome unconnected.
- 模型初步去向：retained
- 模型解释：FR-06 only describes staging a deletion request for admin approval and deleting the record upon approval. No checked original FR documents the alternative outcome when approval is denied, such as rejecting the deletion request or preserving the asset record. This is an in-scope business rule that fills the gap left by the approval-only requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：If admin approval is denied, the deletion request must be rejected and the asset record must remain unchanged.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e1a01ac108ae
- 主题：Administrator
- 审查问题：Is the Administrator actor limited to initiating user creation, or does the role also need a documented connection to an approval or review step in the Add User workflow?
- 场景：An administrator opens the Add User form and submits a new user request; the system must determine whether any additional administrative approval is required.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already states that Administrators create new user accounts, covering the core obligation that the Administrator role is responsible for user creation. The original FR does not establish an additional required approval or review step for the Add User workflow, so the draft does not introduce a new supported business obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：Only users with the Administrator role may create new user accounts unless an additional documented approval role or step is introduced.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2fc79c4b633f
- 主题：Send Activation Email
- 审查问题：Is Send Activation Email a mandatory step within the Add User workflow, or may user creation complete successfully without sending the activation email?
- 场景：A new user record is stored successfully, but the activation email service is temporarily unavailable.
- 模型初步去向：covered
- 模型解释：The checked original FRBLOCK-007 already states that the Add User workflow validates the form, stores the user, and sends an activation email, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：After successfully storing a new user, the system must attempt to send an activation email as part of the Add User workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5c1676d97321
- 主题：User
- 审查问题：Is the User element intended to be the same entity as the New User record created by this FR, and does it need an explicit documented connection to the New User Record Activated state?
- 场景：A downstream feature retrieves the newly created user account and checks whether its state is Activated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already states that the system stores the user and outputs a New User record with status “Activated,” which covers the nominated obligation that the created user record carries the Activated state after successful creation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The User entity must represent the persisted new-user record created by Add User and must carry the Activated state after successful creation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-521b6cf12bce
- 主题：Admin
- 审查问题：Does the FR require a documented admin approval operation for staged profile changes, including who can approve and what happens on rejection?
- 场景：A user submits profile edits; the system stages them; an admin reviews the staged changes and either approves or rejects them.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-008 only supports that staged profile changes are sent for admin approval and the record is updated upon approval. It does not support the draft's additional requirement to document the approval operation by recording the approver and approval outcome; the other original FRs likewise do not establish that recording/audit obligation. The draft therefore introduces unsupported policy detail.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must provide an admin approval operation for staged profile changes that records the approver and the approval outcome.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-95fe4a924a59
- 主题：User
- 审查问题：Does the FR restrict profile editing to the authenticated user’s own profile, and are there any role-based exceptions?
- 场景：A user attempts to edit another user’s profile; the system should deny the action unless the user has an admin role.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-008 only states that users edit their own profiles. It does not establish an authenticated-user restriction or any role-based exception allowing authorized admins to edit other users' profiles. The draft's exception for authorized admin operations is an added policy unsupported by the original FRs.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must restrict profile editing to the authenticated user’s own profile, except for authorized admin operations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-69ee826399b7
- 主题：Admin
- 审查问题：Should the isolated 'Admin' role be documented as a valid permission level returned by Query User Details?
- 场景：When Query User Details returns a user's permission level, the value 'Admin' is not defined in the FR, so it is unclear whether 'Admin' is a recognized permission level.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only lists "permission level" as an output field and does not define allowed permission-level values or identify "Admin" as a valid value. The other screened FRs mention administrators/admin approval only in workflow or actor contexts, not as a permission level returned by Query User Details. Therefore the draft requirement to define allowed values including whether "Admin" is valid is not supported by the source evidence.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must define the allowed permission level values, including whether 'Admin' is a valid value.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5a1504a65156
- 主题：Senior Admin
- 审查问题：Should the isolated 'Senior Admin' role be documented as a valid permission level returned by Query User Details?
- 场景：When Query User Details returns a user's permission level, the value 'Senior Admin' is not defined in the FR, so it is unclear whether 'Senior Admin' is a recognized permission level.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only surfaces 'permission level' as an output field. It does not require enumerating allowed permission-level values, and no original FR shows that 'Senior Admin' is a permission level returned by Query User Details; other mentions of senior-admin are approval-actor references. The draft therefore introduces an unsupported documentation requirement and role-to-permission-level linkage.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must define the allowed permission level values, including whether 'Senior Admin' is a valid value.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7b0c6af7d1b9
- 主题：Senior Admin
- 审查问题：Is the isolated element 'Senior Admin' the actor or role that performs the senior-admin approval mentioned in this FR, and if so, how is that role identified in the workflow?
- 场景：Reviewing role assignments for the deletion approval step, since the FR refers to 'senior-admin approval' but does not define a 'Senior Admin' actor element.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already specifies that deletion requests are staged for senior-admin approval, which is equivalent to routing staged deletion requests to the senior-admin approver role. The draft obligation restates this existing business requirement rather than adding a new one.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：If Senior Admin is the approver role, the system must route staged deletion requests to users holding that senior-admin role.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8e7961cb6d38
- 主题：User
- 审查问题：How does the isolated element 'User' relate to the 'user record' and 'user ID' referenced in this deletion workflow?
- 场景：Reviewing the data model for deletion, because the FR deletes a user record and accepts a user ID but the isolated element 'User' is not explicitly connected.
- 模型初步去向：retained
- 模型解释：FRBLOCK-010 is the in-scope deletion workflow and references a supplied user ID, but the screening notes indicate the original FR does not explicitly state the obligation to resolve/identify the target user record from that ID before validation and deletion. The draft obligation is supported by the deletion workflow and does not introduce a new policy.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must identify the target user record from the supplied user ID before validating and deleting it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-38680c770a88
- 主题：Validate Request
- 审查问题：Does the isolated element 'Validate Request' refer to the same validation operation as 'validates the request' in this FR?
- 场景：Reviewing operation naming, because the FR says the system validates the request but an isolated element 'Validate Request' is supplied.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-010 (and FRBLOCK-006) already states that the system validates the deletion request before staging it for approval, which is equivalent to the draft obligation. The obligation is therefore already present in the original FR set and does not require a new supplement.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must apply a validation operation to deletion requests before staging them for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d3813c76a3ed
- 主题：Administrator
- 审查问题：How is the isolated element 'Administrator' related to the 'Administrators' actor that removes user accounts in this FR?
- 场景：Reviewing actor naming consistency, since the FR uses 'Administrators' but an isolated element 'Administrator' is supplied.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already states that Administrators remove user accounts and validates the deletion request, which is equivalent to recognizing administrators as the actor role authorized to initiate user deletion requests.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must recognize administrators as the actor role authorized to initiate user deletion requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8a48af1fe50c
- 主题：Senior Admin
- 审查问题：Does the Senior Admin actor have a documented approval action or decision right for staged workflow configurations?
- 场景：An administrator defines a workflow; the system validates and stages the setup; a senior admin must approve it before activation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that workflow setup is staged for senior-admin approval and activated upon approval, which documents the Senior Admin approval action for staged workflow configurations before activation. FRBLOCK-014 also covers workflow changes staged for senior-admin approval.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must provide senior admins with an approval action for staged workflow configurations before activation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b873d2be629d
- 主题：Senior-admin approval required
- 审查问题：Is 'Senior-admin approval required' a documented gate condition for activating a configured workflow?
- 场景：A workflow configuration is staged; activation should only occur upon senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already documents the same obligation: it stages the workflow setup for senior-admin approval and activates the workflow only upon approval, which is equivalent to enforcing senior-admin approval as a prerequisite to workflow activation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must enforce senior-admin approval as a prerequisite to workflow activation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4e7f0cfa709e
- 主题：Administrator
- 审查问题：Should the isolated 'Administrator' element be explicitly connected to the admin review step in FR-12?
- 场景：A user submits a transfer approval request; the system validates it and stages it for admin review, but the Administrator element is isolated in the model.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that Administrators review and approve or reject asset requests, which directly links the Administrator role to the admin review/approval step. This is equivalent to the nominated connection; required permissions are not separately detailed, but the core obligation is already present in the checked original FRs.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Document the Administrator's role and required permissions for reviewing staged approval requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-010da0364d92
- 主题：Pending Operation Status
- 审查问题：Does the staged-for-review state described in FR-12 map to the isolated 'Pending Operation Status' element, and should that mapping be documented?
- 场景：An approval-start request is validated and staged; while awaiting admin review, the operation status may need to be represented as pending.
- 模型初步去向：unsupported
- 模型解释：The draft obligation introduces a specific mapping between staged approval requests and the isolated element “Pending Operation Status,” but the documented evidence for FR-12 only states that requests are staged for admin review and output includes an updated operation status. No original FR screening confirms that staged requests must be represented as “Pending Operation Status” or that such a mapping must be documented. Therefore the proposed obligation is an unsupported policy addition.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Define whether staged approval requests set the operation status to Pending Operation Status and document the mapping.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8312f85e38e2
- 主题：Validate Request
- 审查问题：Is the isolated 'Validate Request' element the same validation step referenced in FR-12, and should its connection be documented?
- 场景：FR-12 states the system validates the request before staging, while 'Validate Request' appears as an isolated element.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states the validation operation ('The system validates the request' for the approval-start request). The nomination only asks to clarify/document traceability of the isolated 'Validate Request' element to that existing validation step; it does not add a distinct business obligation beyond what FR-12 already covers.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Clarify and document whether 'Validate Request' represents the validation operation in FR-12.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-35d3e6838752
- 主题：Approved Operation Status
- 审查问题：Should the isolated 'Approved Operation Status' element be connected to the operation execution upon approval in FR-12?
- 场景：After admin approval, the requested operation is executed and its status is updated; 'Approved Operation Status' is isolated.
- 模型初步去向：unsupported
- 模型解释：FR-12 supports that the operation is executed upon approval and that an operation status is updated, but it does not specify that the status value is 'Approved Operation Status'. The draft therefore introduces an unsupported status policy rather than an obligation already present in the source.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Define whether execution upon approval sets the operation status to Approved Operation Status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-592e504289c1
- 主题：User
- 审查问题：Should the isolated 'User' element be explicitly connected to the approval-start initiation described in FR-12?
- 场景：Users initiate approval processes for registration, usage, transfer, or return; the User element is isolated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 explicitly states that Users initiate approval processes for registration, usage, transfer, or return, which already covers the User's role in initiating approval-start requests.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Document the User's role in initiating approval-start requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-16529c1dc4d7
- 主题：Admin
- 审查问题：Is there a documented connection between 'Admin' and FR-13 Query Approval Status, or is 'Admin' intentionally outside the scope of this query function?
- 场景：An Admin user needs to check the approval status of an asset or user operation.
- 模型初步去向：unresolved
- 模型解释：FR-13 only states that users can check the status of asset or user operations; it does not identify Admin or state whether Admin is included or excluded. No other original FR addresses Admin querying approval status. The evidence is therefore insufficient to determine whether Admin is in scope for FR-13 or intentionally excluded.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：If Admin is in scope, document that Admin can query approval status; otherwise document that Admin is excluded from FR-13.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7931811720a8
- 主题：Senior-admin approval required
- 审查问题：Does FR-13 Query Approval Status need to expose a 'Senior-admin approval required' status when returning approval status details, or is this state out of scope?
- 场景：A user queries an operation that may require senior-admin approval.
- 模型初步去向：out_of_scope
- 模型解释：FR-13's approval status details are enumerated as pending, in progress, approved, and rejected; a 'Senior-admin approval required' status is not part of the approval-status query and is outside the obligation stated by the source FR.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：If in scope, include Senior-admin approval required in the returned approval status details; otherwise document exclusion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0df89826a7f9
- 主题：Validate Request
- 审查问题：Is there a documented connection between 'Validate Request' and FR-13, such as validating search criteria before querying approval status?
- 场景：A user submits search criteria to query approval status.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-013 only lists search criteria (asset ID, operation type, user ID) as input and approval status as output; it does not document a 'Validate Request' connection or any obligation to validate search criteria before querying approval status. No screened original FR supports that linkage, so the draft's proposed connection is not backed by the supplied evidence.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：If in scope, document that Validate Request applies to FR-13 search criteria; otherwise document exclusion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ecb249648879
- 主题：Asset change
- 审查问题：Does 'Asset change' relate to the operations whose approval status is queried in FR-13, or is it outside this FR's scope?
- 场景：A user queries approval status for an asset change operation.
- 模型初步去向：covered
- 模型解释：FR-13 already covers querying approval status for asset operations and allows searching by operation type; 'Asset change' as an asset operation type is therefore within the existing FR-13 obligation. No new business-level supplement is needed.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：If in scope, clarify that Asset change is an operation type that can be queried; otherwise document exclusion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6c4686cb650c
- 主题：Senior Admin
- 审查问题：Does the FR-14 approval workflow need to document whether the isolated role “Senior Admin” is the same role that performs senior-admin approval?
- 场景：An administrator modifies a workflow; the system stages it for senior-admin approval. The role appears elsewhere as “Senior Admin” but is not explicitly linked in FR-14.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-014 only refers to changes being staged for 'senior-admin approval.' It does not state that the system must consistently identify the senior-admin role, nor does it require documentation that the isolated role 'Senior Admin' is the same role performing senior-admin approval. The draft obligation adds a role-consistency requirement not supported by the cited evidence or any original FR screening.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must consistently identify the senior-admin role responsible for approving workflow modifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-baaf76392c6d
- 主题：Rejected
- 审查问题：Does the FR-14 edit approval workflow need to document the outcome when a senior-admin rejects a staged workflow modification, given the isolated “Rejected” status?
- 场景：An administrator submits a workflow modification; the system stages it for senior-admin approval, but the senior-admin rejects it. FR-14 only describes update upon approval and final status “Modified.”
- 模型初步去向：retained
- 模型解释：FR-14 establishes a senior-admin approval workflow for workflow modifications but only specifies the outcome upon approval. It does not address the rejection outcome or the status of the original workflow after rejection. No other original FR covers this rejection scenario for workflow modifications; related rejection handling exists only for asset requests or status queries, not for workflow edits. The obligation is in-scope and not covered.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must define whether a rejected workflow modification leaves the original workflow unchanged and what status the workflow retains.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ee4c8a8ace04
- 主题：Senior-admin approval required
- 审查问题：Does the FR-14 approval workflow need to document how the isolated condition “Senior-admin approval required” relates to staging a workflow modification for approval?
- 场景：An administrator edits a workflow; the system stages the modified workflow for senior-admin approval. The isolated condition “Senior-admin approval required” may represent the gate for this stage.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already requires workflow modifications to be staged for senior-admin approval and applied only upon approval, which is equivalent to the nominated obligation defining that workflow modifications require senior-admin approval before being applied.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must define the condition under which a workflow modification requires senior-admin approval before being applied.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8028939a7ffc
- 主题：User
- 审查问题：Which user roles or permissions are allowed to create reports on assets, users, or management data?
- 场景：A standard user attempts to generate a report on management data; the system must determine whether the action is authorized or requires elevated permissions.
- 模型初步去向：unsupported
- 模型解释：The cited FRBLOCK-015 only states that users create reports on assets, users, or management data and describes report generation mechanics. It does not specify roles, permissions, report domains, or authorization restrictions for report creation. The draft obligation therefore introduces a role/domain-based access-control policy that is not supported by the checked source FRs.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Restrict report creation to authorized users based on report domain and role.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-35ab06c489d3
- 主题：Admin
- 审查问题：Does generating reports on management data require Admin or comparable elevated privileges?
- 场景：An Admin attempts to generate a management data report; the system must verify whether Admin rights are required and sufficient.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-015 describes generating reports on management data but does not specify whether Admin or comparable elevated privileges are required. No other original FR supplies an equivalent access-control obligation for management data reports. The available evidence is therefore insufficient to determine whether such reports require elevated privileges, so the nomination cannot be retained or marked covered.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Define whether management data reports require Admin privileges.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c59db3bcd7a5
- 主题：Validate Request
- 审查问题：Should a separate request validation step occur before validating report parameters?
- 场景：A malformed report request arrives with missing parameters; the system must decide whether to validate the request envelope before validating the specific report parameters.
- 模型初步去向：unsupported
- 模型解释：The evidence from FRBLOCK-015 only states that the system validates parameters when generating a report. It does not establish a separate validation of the report request envelope before report parameters are processed, and no other original FR covers that ordering obligation. The draft therefore introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Validate report requests before processing report parameters.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-df26119519c0
- 主题：Validate Request
- 审查问题：Does Validate Request have a documented connection to the Export Report operation and Prepare File within FR-16?
- 场景：Validate Request appears in the export workflow but is graph-isolated. Reviewers need to confirm whether it is a mandatory step that feeds into file preparation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that the system validates the request, prepares the file, and provides a download link, which documents request validation as part of the export operation before file preparation.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST perform request validation as part of every export operation before file preparation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a5d5afb3a43b
- 主题：Prepare File
- 审查问题：Does Prepare File have a documented connection to Validate Request (predecessor) and Provide Download Link (successor) in the export workflow?
- 场景：Prepare File appears between validation and link provision but is graph-isolated. Without explicit links, sequencing and data flow cannot be confirmed.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 and FRBLOCK-018 already document the export workflow sequence: the system validates the request, prepares/generates the file, and then provides a download link. This matches the nominated obligation that file preparation follows successful validation and precedes download-link provision.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST prepare the export file only after successful validation and before providing the download link.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5b4b335859fe
- 主题：Provide Download Link
- 审查问题：Does Provide Download Link have a documented connection to Prepare File and the requesting user?
- 场景：Provide Download Link is graph-isolated. The FR states it provides a download link but does not link it to the prepared file or to the user who requested the export.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that users export existing reports, the system validates the request, prepares the file, and provides a download link, which is equivalent to the draft obligation of providing the download link after export file preparation. FRBLOCK-018 also documents a similar export-and-download-link flow.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST provide the download link to the requesting user after the export file is prepared.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-930be53e435b
- 主题：Parse Rows
- 审查问题：What is the documented role of 'Parse Rows' in the import workflow, and how does it connect to validation and storage?
- 场景：A user uploads a CSV file where some rows have malformed columns; the system must decide how parsing interacts with validation and storage.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already states that the system validates format and data, parses rows, and stores valid records with an error report, which documents the row parsing step and its relationship to validation and storage during import.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The system should document the row parsing step and its relationship to validation and storage during asset import.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f8b46587ed60
- 主题：Validate Format and Data
- 审查问题：How does 'Validate Format and Data' connect to the import workflow, and what validation rules apply to CSV/Excel files?
- 场景：A user uploads an Excel file with missing required columns; the system must validate the format and data before storing records.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-017 states that the system validates format and data during import and produces an error report, but it does not require the system to define validation rules or document how validation failures are reported. The draft adds a documentation/definition obligation not supported by the source.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The system should define the validation rules for format and data and document how validation failures are reported.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a473999d7d9c
- 主题：User
- 审查问题：Which user role is documented as authorized to upload asset data files?
- 场景：An administrator attempts to import asset data; the system must determine whether that user role is permitted.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-017 already states that Users upload CSV/Excel files, documenting the user role associated with asset data file imports. The nomination's question and draft obligation are therefore equivalent to an existing original FR.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The system should specify the user role(s) allowed to perform asset data imports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-804849ce265b
- 主题：Admin
- 审查问题：Is 'Admin' included in the 'Users' authorized to export asset data, or is export access limited to non-admin users?
- 场景：An Admin user selects assets and an export format and attempts to export asset data.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-018 states only that 'Users export selected asset data' and does not define whether 'Admin' is included in 'Users' or whether export access is limited to non-admin users. No other original FR clarifies export authorization by role. The evidence is therefore insufficient to determine whether the draft obligation is covered or whether Admin export permission is supported.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：If Admin is an authorized user for export, the system shall permit Admin to export selected asset data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6540c0beabd7
- 主题：Prepare File
- 审查问题：Does 'Prepare File' require a documented connection to this export workflow, or is it an internal implementation detail outside the FR scope?
- 场景：The system prepares the export file after validation and before providing the download link.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already states that the system validates the request, generates the file, and provides a download link. This is equivalent to preparing the export file after validation and before providing the download link, so the nominated obligation is already covered by an original FR.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：If 'Prepare File' is part of the export workflow, the system shall prepare the export file after validation and before providing the download link.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3e6938fdd642
- 主题：Parse Rows
- 审查问题：Is 'Parse Rows' a separate operation for reading selected assets, or is it out of scope for this FR?
- 场景：The system parses selected asset rows from the export request before generating the file.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-018 only covers exporting selected asset data by validating the request, generating the file, and providing a download link. It does not specify a separate 'Parse Rows' operation or any obligation to parse selected asset rows from the export request. The draft therefore introduces an unsupported implementation-level requirement.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：If 'Parse Rows' is required, the system shall parse the selected asset rows from the export request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-57aab582e758
- 主题：Senior-admin
- 审查问题：How should the isolated Senior-admin element be connected to the approval workflow so that the system knows which role is authorized to approve staged permission requests?
- 场景：A staged permission request requires approval; the system must identify the senior-admin role authorized to approve it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies that staged permission requests are staged for senior-admin approval and permissions are updated upon approval, which establishes the senior-admin role as the authorized approver for staged permission requests.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system shall recognize the senior-admin role as authorized to approve staged permission requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8f7da445e167
- 主题：User
- 审查问题：How is the target user identified and connected to the permission assignment workflow, and should this be documented from the supplied User element?
- 场景：An Administrator submits a permission form containing a user ID; the system must resolve that user and apply the approved permissions to the correct user.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies the permission form input as containing a user ID and permission level. That user ID is the identifier used to associate the permission request with the target user, so the draft obligation is equivalent to the existing FR. The additional reference to a supplied User element is not supported by the original FR, but the core obligation is already covered.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system shall use the user ID from the permission form to identify the user whose permissions are being set.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-73b49281e187
- 主题：Senior-admin approval required
- 审查问题：Is the isolated element 'Senior-admin approval required' the same as the top-level approval step in FR-20?
- 场景：Reviewing approval authority and whether top-level approval is synonymous with senior-admin approval.
- 模型初步去向：unsupported
- 模型解释：FR-20 only states that the item is staged for top-level approval. No original FR establishes that senior-admin approval is the same as, required for, or related to top-level approval, and none requires the solution to define such a relationship. The draft obligation therefore introduces an unsupported policy/clarification requirement not grounded in the source FRs.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall define whether senior-admin approval is required and how it relates to top-level approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-bc2f932cecab
- 主题：Validate Request
- 审查问题：Is the isolated element 'Validate Request' the same as the 'Validate replacement request' function in FR-20?
- 场景：Reviewing validation function naming and scope for replacement requests.
- 模型初步去向：covered
- 模型解释：FR-20 already includes validation of the replacement request before staging it for approval, which is equivalent to the nominated obligation. No additional business-level supplement is needed.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall align the validation function for replacement requests to a single defined operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0953f9b9ce8a
- 主题：Administrator
- 审查问题：How should the isolated element 'Administrator' be mapped to the current system admin or senior administrators in FR-20?
- 场景：Reviewing role terminology for the actor and target of replacement.
- 模型初步去向：unsupported
- 模型解释：FR-20 states that senior administrators replace the current system admin, but it does not require documenting how the isolated term 'Administrator' maps to the current system admin, a senior administrator, or a new admin. No checked original FR imposes this role-mapping documentation obligation, so the draft introduces an unsupported policy requirement.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall document whether 'Administrator' refers to the current system admin, a senior administrator, or the new admin.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-fde81fa23cd1
- 主题：Admin
- 审查问题：Should Admin be explicitly modeled as the role authorized to approve or reject a staged asset request?
- 场景：A user submits an asset request; the system stages it for admin approval, but the FR does not identify which admin role, permissions, or notification is required to act on it.
- 模型初步去向：covered
- 模型解释：The checked original FRs already establish the equivalent obligation: FRBLOCK-021 states that asset requests are staged for admin approval and that the stored request status can be “Approved” or “Rejected,” and FRBLOCK-022 states that Administrators review and approve or reject asset requests. Therefore the draft obligation to identify and authorize the Admin role to approve or reject staged asset requests is already covered by the original FRs.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must identify and authorize the Admin role to approve or reject staged asset requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-fd4766d2b379
- 主题：User
- 审查问题：Should User be explicitly identified as the requester role authorized to submit asset requests?
- 场景：Users request assets, but the FR does not say how the requester is identified or linked to the stored request.
- 模型初步去向：unsupported
- 模型解释：The cited evidence only states that Users request assets; it does not require the system to record, link, or associate each asset request with the submitting User. No original FR screening shows an equivalent obligation, and the draft adds a data-association requirement not supported by the source text.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must associate each asset request with the submitting User.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f7328674f8c4
- 主题：Approved
- 审查问题：Should Approved be defined as a terminal request status set only after an admin approval decision?
- 场景：An asset request is approved; the output is a stored request with status Approved, but the FR does not specify state transition rules.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies that the request is staged for admin approval and the status is updated upon approval, with the output including Approved or Rejected. This is equivalent to the draft obligation that the request status is set to Approved only after an admin approval decision.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must set the request status to Approved only following an admin approval decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-33f1c511e7a0
- 主题：Rejected
- 审查问题：Should Rejected be defined as a terminal request status set after an admin rejection decision?
- 场景：An asset request is rejected; the output is a stored request with status Rejected, but the FR does not specify state transition rules.
- 模型初步去向：covered
- 模型解释：The checked original FRs already state that administrators can reject asset requests and that the system updates the request status, with FRBLOCK-021 defining a stored request status of “Approved” or “Rejected.” Together they state the equivalent obligation to set the request status to Rejected following an admin rejection decision.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must set the request status to Rejected following an admin rejection decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6103d7d839e4
- 主题：Validate Request
- 审查问题：Should Validate Request be explicitly linked to the validation step in FR-21?
- 场景：The FR states the system validates the request before staging, but the isolated element Validate Request has no documented connection here.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that the system validates the request before staging it for admin approval, which is equivalent to the nominated draft obligation. Therefore the obligation is not a new in-scope business requirement.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must validate the asset request before staging it for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-33b574e0c4ea
- 主题：Admin
- 审查问题：Should the isolated element 'Admin' be documented as equivalent to, or distinct from, the 'Administrators' actor that reviews and decides asset requests in FR-22?
- 场景：FR-22 describes 'Administrators' reviewing and approving or rejecting asset requests, while the graph lists 'Admin' as isolated. Review whether this role needs an explicit documented connection to the FR-22 approval workflow.
- 模型初步去向：unsupported
- 模型解释：FR-22 only states that Administrators review and decide asset requests. It does not mention the isolated 'Admin' element, define it, or require clarifying whether 'Admin' and 'Administrators' are equivalent. No checked original FR supplies such a clarification obligation, so the draft introduces an unsupported policy/documentation requirement rather than a supported business obligation.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The asset request approval workflow must clarify whether 'Admin' and 'Administrators' refer to the same authorized role.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ee320e277d01
- 主题：Approved
- 审查问题：Should the isolated status value 'Approved' be documented as the resulting request status when an administrator approves an asset request in FR-22?
- 场景：FR-22 updates request status after an approval or rejection decision, while 'Approved' appears isolated in the graph. Review whether 'Approved' should be linked to the updated request status output.
- 模型初步去向：covered
- 模型解释：FR-21 already states an equivalent obligation: after admin approval, the system updates the request status and the output includes status "Approved" or "Rejected." Therefore the draft obligation for setting an approved asset request status is already covered by an original FR, and FR-22 does not add a distinct unsupported obligation.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must set an asset request to an approved status when an administrator approves it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2cf437850a6d
- 主题：Rejected
- 审查问题：Should the isolated status value 'Rejected' be documented as the resulting request status when an administrator rejects an asset request in FR-22?
- 场景：FR-22 says administrators approve or reject asset requests and the system updates the request status, while 'Rejected' appears isolated in the graph. Review whether 'Rejected' should be linked to the updated request status output.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators review and approve or reject asset requests and that the system updates the request status. This is equivalent to setting an asset request to a rejected status upon administrator rejection, so the nominated obligation is already covered by the original FR.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must set an asset request to a rejected status when an administrator rejects it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-913c12c4873f
- 主题：Send Activation Email
- 审查问题：Does the isolated element 'Send Activation Email' have a documented connection to FR-23's automatic email notification workflow, or is it a separate notification process that is intentionally out of scope?
- 场景：FR-23 describes automatic email notifications for registration and profile updates; 'Send Activation Email' is an isolated email-related element that might overlap with or be a specialized instance of this workflow.
- 模型初步去向：unresolved
- 模型解释：FR-23 describes generic automatic email notifications for events such as registration or profile updates, but it does not mention 'Send Activation Email' or state whether that notification is included or excluded. FR-07 separately specifies that Add User sends an activation email, but it does not document a connection to FR-23 or an intentional exclusion from FR-23. The available evidence therefore does not settle the scope relationship.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Confirm and document whether 'Send Activation Email' is in scope for FR-23 or explicitly excluded.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ab026ca8f8ea
- 主题：Admin
- 审查问题：Is 'Admin' intended to be part of the recipient list for FR-23 notifications, or does 'Admin' have no documented role in this email notification flow?
- 场景：FR-23 sends notifications to a recipient list; 'Admin' is an isolated role element that may or may not be a recipient or event trigger.
- 模型初步去向：unresolved
- 模型解释：The only relevant FR (FR-23) mentions a 'recipient list' but does not identify 'Admin' as a recipient or exclude it, and no other original FR establishes Admin's role in FR-23 notifications. The evidence is therefore insufficient to decide whether Admin should be included, excluded, or whether a clarification obligation is supported.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Clarify whether 'Admin' participates in the recipient list or event triggering for FR-23, or document its exclusion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-535766aa61d6
- 主题：Validate Format and Data
- 审查问题：Does 'Validate Format and Data' have a documented connection to FR-23's processing of event details and recipient list, or is it unrelated to this email notification feature?
- 场景：FR-23 takes 'Event details' and 'recipient list' as input; the isolated 'Validate Format and Data' element may indicate required validation but is not referenced in FR-23.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-023 only documents event details and recipient list as inputs and sent email/send log as outputs; it does not state any input-validation obligation or any connection to 'Validate Format and Data.' The screenings also confirm that no original FR establishes such validation for FR-23. Therefore the draft introduces an unsupported validation requirement rather than an obligation evidenced by the source text.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Confirm whether input validation is required for FR-23 and document any connection to 'Validate Format and Data'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-158ed9d52273
- 主题：User
- 审查问题：Does the User need a documented submission or interaction path to provide feedback email, or is email receipt treated as an external channel event?
- 场景：A user wants to send feedback to the system by email; the FR only describes the system receiving and processing that email.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already specifies that the system receives user email feedback as an input event and processes it by parsing, storing, and notifying admins, which is equivalent to accepting user feedback emails through the configured email channel. The draft obligation does not add a new business requirement beyond that covered original FR.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system should accept user feedback emails through the configured email channel so users can submit feedback to be processed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-87cf015af0d6
- 主题：Asset change
- 审查问题：How should the occurrence of an asset change be connected to the change-history entries returned by FR-25?
- 场景：An asset is modified, such as its owner or status changing, and later a user queries the change log by asset ID to see that modification.
- 模型初步去向：retained
- 模型解释：FR-25 defines querying/viewing asset change logs but does not specify recording a change-history entry when an asset change occurs. No other original FR assigns this recording obligation. The draft is an in-scope asset-management requirement supported by the need for FR-25's change-history query to have retrievable entries.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：When an asset change occurs, the system shall record a change-history entry that can be retrieved by the View Asset Change History query.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-373aaa89f56f
- 主题：Asset change
- 审查问题：What change types must be captured when an asset change is recorded so that the change type search criterion is meaningful?
- 场景：A user filters change history by change type to review only ownership changes for an asset.
- 模型初步去向：retained
- 模型解释：The original FR-25 only provides query capability by change type; it does not explicitly require asset change records to capture a change type at the time of the change. The draft obligation is a supported, in-scope data-capture requirement needed to make the change type search criterion meaningful, and it is not stated as a distinct obligation in the checked original FRs.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：Asset change records shall include a change type that can be used as a search criterion in the View Asset Change History query.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e8f5313db810
- 主题：Asset Count
- 审查问题：Is the Asset Count element connected to an operation that computes or updates it when category details are viewed?
- 场景：A user views category details and sees an asset count, but the FR does not document how that count is derived or maintained.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already documents that viewing/querying an asset category returns category details including the asset count, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system must include the current asset count in the category details returned when viewing an asset category.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5992bbd5a238
- 主题：User
- 审查问题：Is the User element connected to an authorization check for viewing asset categories?
- 场景：The FR states that Users query asset categories, but does not specify whether all users or only certain roles may view them.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-026 only states that Users query asset categories; it does not specify or require role-based authorization or define which users may view categories. The draft obligation introduces an access-control policy not supported by the source FRs.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system must define which users or roles are permitted to view asset categories.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-bf7a3c2bb91e
- 主题：Senior Admin
- 审查问题：Is the isolated actor 'Senior Admin' intended to be the same role as the 'senior-admin' referenced in the staged approval workflow?
- 场景：A category edit is staged and waits for approval; the system must route the approval to the correct senior administrator role.
- 模型初步去向：unsupported
- 模型解释：The draft requires the system to identify and authorize a senior-admin role for staged asset-category edits. FRBLOCK-027 only states that category edits are staged for senior-admin approval; it does not define or require role identification/authorization or resolve the isolated actor 'Senior Admin' to 'senior-admin'. No checked original FR establishes that role-authorization policy.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must identify and authorize the senior-admin role responsible for approving staged asset-category edits.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-095617f6236c
- 主题：Admin
- 审查问题：Is the isolated actor 'Admin' meant to be synonymous with the 'Administrators' who modify category information?
- 场景：An administrator opens the edit category form; the system must resolve whether 'Admin' and 'Administrator' are the same permission-bearing role.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-027 only states that 'Administrators modify category information'; it does not mention the isolated actor 'Admin' or require that 'Admin' and 'Administrator' be treated consistently for authorizing asset-category editing. The draft therefore introduces an unsupported policy/obligation not established by the evidence.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must treat 'Admin' and 'Administrator' consistently when authorizing asset-category editing.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：76 条提名

### OPERATION-329e747ca072
- 主题：Validate Format and Data
- 审查问题：Should the isolated operation 'Validate Format and Data' be documented as the operation that performs the validation described in FR-01?
- 场景：FR-01 states the system validates data for completeness and accuracy before storing the asset. The model contains an isolated operation 'Validate Format and Data' that may implement this step.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states that the system validates asset registration data for completeness and accuracy, which is equivalent to the draft obligation to document the validation operation before storage. The isolated operation does not add a new business obligation beyond the existing FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：Document the validation operation that checks asset registration data for completeness and accuracy before storage.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6aee27525abb
- 主题：Register Asset
- 审查问题：Does the 'Register Asset' operation require a documented administrator review operation after the asset is stored as 'Registered'?
- 场景：FR-01 stores the asset and notifies administrators for review, but this block does not document a review or approval operation. The workflow may require a specific review operation without implying full CRUD.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states that administrators are notified for review after the asset is stored and marked 'Registered,' which covers the nominated administrator-review obligation for Register Asset.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：Document whether a separate administrator review operation (e.g., review/approve/reject) is applicable after the asset is registered.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5f7aec15067d
- 主题：Admin approval
- 审查问题：Does the documented admin approval event include a rejection path, and should a rejection operation be documented for staged asset modifications?
- 场景：A user edits and submits asset details; the system stages the change for admin approval; the admin does not approve the change.
- 模型初步去向：covered
- 模型解释：The checked original FRs already include the rejection-path obligation: FRBLOCK-022 states that administrators review and approve or reject asset requests, the system updates the request status, and users are notified; FRBLOCK-021 also documents a stored request status of “Approved” or “Rejected.” Thus the denied-approval outcome, rejection status, and follow-up notification are equivalent to the nominated obligation for staged asset requests.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should define and document the outcome when admin approval is denied for a staged asset modification, including any rejection status or follow-up action.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-53f13203fb40
- 主题：Validate modification data
- 审查问题：Does validation of modification data include failure handling and resubmission, and should that operation be documented?
- 场景：A user submits a modification form with invalid data; the system validates the data but the FR does not describe the invalid path.
- 模型初步去向：retained
- 模型解释：FRBLOCK-002 validates modification data and stages the change for admin approval, but it does not specify failure handling or whether the user can correct and resubmit. No other original FR covers this obligation, so the gap is an in-scope, supported requirement.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system should define the behavior when modification data fails validation, including whether the user can correct and resubmit the form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-734adcabaa68
- 主题：Query Asset Details
- 审查问题：Should Query Asset Details support pagination or sorting when returning matching records?
- 场景：A user searches with broad criteria and the system returns a large number of matching asset records.
- 模型初步去向：unresolved
- 模型解释：The only evidence (FRBLOCK-003) states that the system returns matching records but does not mention large result sets, pagination, or sorting. No original FR covers this obligation. The nomination's scenario suggests large result sets, but the documented evidence is insufficient to decide whether pagination or sorting should be a required business obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Specify whether Query Asset Details must paginate or sort matching records for large result sets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f9b5acc5e10c
- 主题：Search Criteria
- 审查问题：Should Search Criteria support partial and case-insensitive matching for name, type, or ID?
- 场景：A user enters a partial asset name or a lowercase type and expects the system to return relevant matches.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 establishes in-scope asset search criteria (name, type, ID) but does not define matching semantics, and no other original FR covers partial/exact or case-sensitive matching for Query Asset Details.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Define matching semantics (exact vs. partial, case sensitivity) for Search Criteria in Query Asset Details.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-563fa168bf39
- 主题：Detailed Asset Information
- 审查问题：Does Detailed Asset Information need a defined field set and role-based visibility beyond the listed examples?
- 场景：A user queries an asset and receives detailed information; the FR lists name, type, quantity, purchase date, status, etc., but not the complete output schema or access restrictions.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-003 only lists examples of detailed asset information and uses 'etc.'; it does not establish an obligation to define a complete output field set or any role-based visibility rules. No other original FR supplies that obligation, and the role-based visibility requirement is introduced without source support.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Define the complete output fields and any role-based visibility rules for Detailed Asset Information.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0cb6326f1c19
- 主题：Transfer Asset
- 审查问题：What asset conditions determine whether a transfer asset operation may be requested, and how should duplicate or conflicting transfer requests be handled?
- 场景：A user requests to transfer an asset that is already pending admin approval or has already been transferred. The system must decide whether to accept, reject, or flag the request before validation and staging.
- 模型初步去向：unsupported
- 模型解释：The draft imposes transfer eligibility conditions and duplicate/conflicting request handling rules that are not supported by the documented evidence. FRBLOCK-004 only states that users request asset transfers to a new user or department; no original FR specifies eligible asset states for transfer or rules for preventing/rejecting duplicate or conflicting transfer requests.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall allow transfer asset requests only for assets in eligible states and shall prevent or reject duplicate or conflicting transfer requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d5163d090e57
- 主题：Validate Transfer Request
- 审查问题：What validation rules must the system apply when validating a transfer request, and what outcome should occur if validation fails?
- 场景：A user submits a transfer form with an invalid asset ID or a new recipient who is inactive. The system validates the request before staging it for admin approval and must determine whether to reject it or return an error.
- 模型初步去向：unsupported
- 模型解释：The source evidence (FRBLOCK-004) only states that the system validates the request; it does not specify transfer-specific validation rules such as asset existence or recipient validity, nor does it specify rejecting or returning invalid requests before staging for admin approval. The draft therefore introduces policy details not supported by the source.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall validate a transfer request against defined rules (e.g., asset exists, recipient is valid) and reject or return invalid requests before staging for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-37ccf0bf72cb
- 主题：Stage for Admin Approval
- 审查问题：Does the staging operation require a documented admin decision step to approve or reject the staged transfer request?
- 场景：A valid transfer request is staged for admin approval. An admin must decide whether to approve or reject it, but FR-04 only describes approval and the subsequent ownership update.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states an equivalent obligation: it stages the request for admin approval and outputs a stored request with status “Approved” or “Rejected,” which covers both the admin decision step and the recording of approval or rejection for a staged request. The draft therefore does not add a distinct in-scope obligation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall present staged transfer requests to an admin and record the admin's approval or rejection decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8a3518addb25
- 主题：Update Ownership Upon Approval
- 审查问题：When ownership is updated upon approval, should the system also set the asset status to 'Transferred' as part of the same operation?
- 场景：An admin approves a transfer. The system updates the owner information and must ensure the asset status becomes 'Transferred' as indicated in the FR output.
- 模型初步去向：covered
- 模型解释：The checked original FR FRBLOCK-004 already specifies that, upon approval, ownership is updated and the output includes status “Transferred,” which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall update the asset's owner and set its status to 'Transferred' upon admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-971fa5983dc8
- 主题：Validate Return Request
- 审查问题：What specific validation rules should the Validate Return Request operation enforce for asset returns?
- 场景：A user submits a return form with asset ID and return date; the system validates the request before staging it for approval.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-005 states only that the system validates the request; it does not specify validation criteria such as asset existence, eligibility, or a valid return date. The draft introduces those specific criteria as policy without supporting evidence, and no other original FR supplies an equivalent obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：Define validation criteria such as asset existence, eligibility, and valid return date for asset returns.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e8bf708331a0
- 主题：Update Asset Status to Returned
- 审查问题：Should the Update Asset Status to Returned operation be constrained to occur only after approval and be idempotent?
- 场景：An asset return request is approved; the system updates the asset status to Returned.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-005 and related return FRs support that an asset status is updated to “Returned” upon approval, but the source evidence does not establish idempotency or status-transition rules for that operation. The draft’s idempotency obligation therefore introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：Define status transition rules and idempotency for marking an asset Returned after approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f6694238c57f
- 主题：Admin
- 审查问题：Given the documented workflow, is an explicit 'Approve' operation applicable to the Admin actor for a staged deletion request?
- 场景：A deletion request is staged for admin approval. The FR states that approval is required but does not define the operation the admin performs to grant it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that deletion is staged for admin approval and deletes the record upon approval, which is equivalent to requiring the Admin actor to approve a staged deletion request. The nominated draft does not add a new in-scope obligation beyond that existing FR.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The Admin actor must be able to perform an approve operation on a staged deletion request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-11c9b1b76745
- 主题：User
- 审查问题：Given the documented workflow, is a 'Cancel' operation applicable to the User actor for a pending deletion request?
- 场景：A user submits a deletion request and then changes their mind before an admin reviews it. The FR does not mention whether the user can cancel the pending request.
- 模型初步去向：unsupported
- 模型解释：The cited deletion workflow only states that users request removal of obsolete assets and that requests are staged for admin approval; it does not grant the User actor any right to cancel a pending deletion request. No original FR establishes this cancellation capability, so the draft introduces an unsupported obligation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The User actor may cancel a pending deletion request before admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-08deb62f06a2
- 主题：Validate New-User Form
- 审查问题：What validation rules apply to the username, password, email, phone, and department fields before the user is stored?
- 场景：An administrator submits a new-user form with an invalid email address and a weak password.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-007 only states that the system validates the new-user form before storing the user and sending an activation email. It does not specify required fields, format checks, or password policy, nor does it identify validation rules for username, password, email, phone, or department fields. The draft obligation therefore introduces specific validation policy not supported by the cited evidence or any other original FR.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system must validate all new-user form fields, including required fields, format checks, and password policy, before storing the user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-51d10671e3e6
- 主题：Store User
- 审查问题：Must the system store the user only after form validation succeeds, and is the store operation atomic with sending the activation email?
- 场景：Form validation fails; the system should not create a user record or send an activation email.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-007 only states that the system validates the form, stores the user, and sends an activation email. It does not require persistence only after successful validation, nor does it require atomicity that would prevent a partially created user record if the activation email fails. The draft therefore introduces failure-handling and transactional guarantees not supported by the original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system must persist a new user record only after successful validation, and a failure to send the activation email must not leave a partially created user record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-45d6f4a1a8db
- 主题：Create New User Accounts
- 审查问题：Does the create operation set the new user record status to Activated immediately, or should it remain pending until the activation email is confirmed?
- 场景：An administrator creates a new user; the system stores the record and sends an activation email, but the user has not yet clicked the activation link.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already specifies that the create operation outputs a New User record with status “Activated,” which is equivalent to the nominated draft obligation that the create operation must set the new user record to Activated unless a pending-activation state is introduced.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The create operation must set the new user record to Activated unless a documented pending-activation state is introduced.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-94ea7b2ce6f8
- 主题：Stage for Admin Approval
- 审查问题：Should the staging operation capture the specific admin responsible for approval and the rejection reason if the changes are not approved?
- 场景：A user edits their profile; the system stages the changes; an admin rejects the staged changes with a reason; the user is notified.
- 模型初步去向：unsupported
- 模型解释：The cited evidence only states that changes are staged for admin approval. None of the original FRs require recording the specific admin approver or capturing a rejection reason for staged profile changes; the draft therefore introduces a new policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must record the admin approver and rejection reason for staged profile changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-85d6f0198fc2
- 主题：Validate changes
- 审查问题：What validation rules apply to the profile-edit form fields (name, username, email, phone), and how are validation errors presented to the user?
- 场景：A user submits a profile edit with an invalid email format; the system validates the changes and prevents staging, showing an error.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-008 only states that the system validates changes and stages them for approval. It does not establish profile-edit field-level validation rules or the presentation of actionable validation errors, so the draft introduces obligations not supported by the documented source evidence.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must validate all profile-edit form fields and present actionable errors without staging invalid changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8119766f82a4
- 主题：Update record upon approval
- 审查问题：Does the update operation occur exclusively after admin approval, and does it set the status to “Modified” as the terminal state of the edit workflow?
- 场景：An admin approves staged profile changes; the system updates the user record and sets its status to “Modified.”
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-008 already states that profile-edit changes are validated, staged for admin approval, updated upon approval, and output as an updated user record with status “Modified.” This is equivalent to the nominated obligation that the user record is updated only after admin approval and set to status “Modified.”
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must update the user record only upon admin approval and set the record status to “Modified.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-de4d5f90023f
- 主题：Query User Details
- 审查问题：Should the Query User Details operation enforce authorization to restrict which actors can query user details, or is it available to any User?
- 场景：A User attempts to search for another user's details by email; the FR does not specify whether any authenticated User can retrieve full details including permission level.
- 模型初步去向：unsupported
- 模型解释：The source FRBLOCK-009 only states that users can search for user information by username, email, or department and does not specify or imply any authorization roles, privileges, or access restriction for querying user details. No other original FR establishes an equivalent obligation. The draft therefore introduces an access-control policy that is not supported by the source text.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must define which user roles or privileges are required to search for and view user details.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cfd3563f71d9
- 主题：Search Criteria
- 审查问题：Should the Search Criteria require at least one of username, email, or department, or can an empty search return all users?
- 场景：A User submits an empty search form; without a minimum criterion, the system might return all user details, which could be a privacy or performance issue.
- 模型初步去向：retained
- 模型解释：FRBLOCK-009 defines the Query User Details search inputs (username, email, department) but does not state whether an empty search is allowed or what default result set is returned. No other original FR covers this. The missing behavior is in-scope for that operation, so the draft obligation is retained as an unresolved specification gap.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must define whether an empty search is allowed and, if so, what default result set is returned.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cd3a6f864081
- 主题：Detailed User Information
- 审查问题：Should the Detailed User Information output include all listed fields for every query result, or can fields such as phone and permission level be conditionally hidden based on requester permissions?
- 场景：A User with basic permissions queries a Senior Admin's details; the FR lists phone and permission level as output, but does not state whether those fields are always visible.
- 模型初步去向：unsupported
- 模型解释：The cited FRBLOCK-009 only lists the Detailed User Information output fields (name, username, email, phone, department, permission level). It does not state that any fields are sensitive, that requester permissions may restrict visibility, or that field-level visibility rules must be defined. The draft therefore introduces an unsupported policy not grounded in the source FRs.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must define field-level visibility rules for sensitive user information.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-74078a8df69e
- 主题：Validate Request
- 审查问题：Should a Validate Request operation be applied to the search criteria before executing Query User Details?
- 场景：A User enters malformed search criteria (e.g., invalid email format); the FR does not specify whether validation occurs before the query runs.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only identifies the Query User Details operation and its input search criteria (username, email, department). It does not state or imply that search criteria must be validated for format or allowed values before query execution, and no other original FR specifies an equivalent obligation for this operation. The draft therefore introduces a validation policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation must validate search criteria for format and allowed values before executing the query.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-76c4061dfb3f
- 主题：Validate deletion request
- 审查问题：What validation criteria must the system apply to a user deletion request before staging it for senior-admin approval?
- 场景：An administrator submits a deletion request for a user account; the system must decide whether the request is valid before moving it to approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already states that the system validates the deletion request before staging it for senior-admin approval, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must validate user deletion requests against defined criteria before staging them for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c6e10a92af28
- 主题：Stage deletion request for senior-admin approval
- 审查问题：How should the system stage a validated deletion request so that a senior admin can review and approve it?
- 场景：A valid user deletion request has been submitted and needs to enter a pending senior-admin approval queue or state.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already specifies that the system validates the deletion request, stages it for senior-admin approval, and deletes the record only upon approval, which is equivalent to the drafted obligation.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must stage validated user deletion requests for senior-admin approval before deletion occurs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-af1c9d11ab62
- 主题：Delete user record upon approval
- 审查问题：What deletion behavior is required once senior-admin approval is recorded—hard delete, soft delete, or status change to Deleted?
- 场景：Senior admin approves a staged user deletion request; the system must remove or mark the user record according to policy.
- 模型初步去向：covered
- 模型解释：The draft obligation ('Upon senior-admin approval, the system must delete the user record and set its status to Deleted') is equivalent to the obligation already stated in original FRBLOCK-010, whose screening records it as covered and quotes: 'The system validates the request, stages it for senior-admin approval, and deletes the record upon approval. Input: Deletion request (user ID). Output: Removed user record with status "Deleted."' The trigger (senior-admin approval), the action (record deletion), and the resulting 'Deleted' status all match, so no new business obligation is introduced.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Upon senior-admin approval, the system must delete the user record and set its status to Deleted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fe884300e664
- 主题：Validate Configuration Details
- 审查问题：Does the Validate Configuration Details operation need to occur before staging a workflow configuration for approval?
- 场景：An administrator submits the workflow configuration form; the system must validate node order, approvers, and conditions before staging.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the system validates configuration details and stages the setup for senior-admin approval, which is equivalent to validating workflow configuration details before staging for approval.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must validate workflow configuration details before staging the setup for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cf2c3d92bf87
- 主题：Activate Workflow
- 审查问题：Does the Activate Workflow operation require senior-admin approval and set the workflow status to Configured?
- 场景：A staged workflow configuration receives senior-admin approval; the system activates it and stores status Configured.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already requires staging the workflow configuration for senior-admin approval, activating the workflow upon approval, and storing it with status “Configured,” which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must activate a workflow only after senior-admin approval and set its status to Configured.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7d5efaed2736
- 主题：Validate approval-start request
- 审查问题：What validation rules and error handling apply to an approval-start request before it is staged for admin review?
- 场景：A user submits an approval-start request with an asset ID and operation type; the system must validate the request and reject invalid inputs.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-012 only states that the system validates the request and stages it for admin review; it does not specify validation rules, required fields, or error responses. The draft obligation to specify those details is not supported by the source evidence.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Specify the validation rules, required fields, and error responses for approval-start requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0c5c11e2547f
- 主题：Operation executed upon approval
- 审查问题：What execution steps and status updates occur when an approval process is approved and the requested operation is executed?
- 场景：An administrator approves a staged registration, usage, transfer, or return request; the system must execute the operation and update its status.
- 模型初步去向：covered
- 模型解释：Multiple original FRs already specify execution upon approval and the resulting operation status for staged requests, such as FRBLOCK-002 (status 'Modified' after approval), FRBLOCK-004 (ownership updated and status 'Transferred'), FRBLOCK-005 (status 'Returned'), and FRBLOCK-006 (record deleted and status 'Deleted'). Therefore the nominated obligation is already covered by existing requirements.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Define the execution sequence and resulting operation status for approved requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8e4b1e713fec
- 主题：Query Approval Status
- 审查问题：Does the documented workflow require the 'Query Approval Status' operation to accept search criteria and return approval status details?
- 场景：A user checks the status of an asset or user operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already specifies the Query Approval Status operation, including acceptance of search criteria (asset ID, operation type, user ID) as input and return of approval status details as output.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：Query Approval Status accepts search criteria and returns approval status details.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f4f8ccb6e615
- 主题：Search Criteria
- 审查问题：Should the 'Search Criteria' operation be applied to filter approval status queries by asset ID, operation type, and user ID?
- 场景：A user searches for approval status using asset ID, operation type, and user ID.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already specifies the Search Criteria input for approval status queries as asset ID, operation type, and user ID, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：Query Approval Status supports search criteria for asset ID, operation type, and user ID.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-be33768b09f7
- 主题：Approval Status Details
- 审查问题：Should the 'Approval Status Details' operation include the states pending, in progress, approved, and rejected?
- 场景：A user views approval status details for an operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already states users check the status of asset or user operations for pending, in progress, approved, and rejected, equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：Approval Status Details includes pending, in progress, approved, and rejected states.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-146143aa7e9d
- 主题：Validate changes
- 审查问题：When an administrator modifies an existing workflow, should Validate changes be performed on the updated nodes, approvers, and conditions before the modification is staged for senior-admin approval?
- 场景：An administrator submits a workflow-edit form containing updated nodes, approvers, and conditions. The system is expected to validate those changes before staging the modification for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that the system validates workflow-edit form changes, including updated nodes, approvers, and conditions, and stages them for senior-admin approval. This is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must validate workflow-edit form changes before staging the modification for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c06907707af8
- 主题：Stage for senior-admin approval
- 审查问题：Should the system stage a validated workflow modification for senior-admin approval before applying any updates to the workflow?
- 场景：An administrator edits an existing workflow; after validation, the modified workflow awaits senior-admin approval and is not yet updated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that the system validates changes, stages them for senior-admin approval, and updates the workflow only upon approval, which is equivalent to the nominated obligation to hold validated workflow modifications pending senior-admin approval before applying updates.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must hold validated workflow modifications in a pending approval state until senior-admin approval is granted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c4b121eb785a
- 主题：Update workflow upon approval
- 审查问题：Upon senior-admin approval, should the system update the workflow as a single operation?
- 场景：A senior-admin approves a staged workflow modification; the system applies the approved changes and the workflow status becomes “Modified.”
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that the system stages changes for senior-admin approval and updates the workflow upon approval, which is equivalent to applying approved workflow modifications upon senior-admin approval.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system must apply approved workflow modifications upon senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-48bba48712bc
- 主题：Validate Parameters
- 审查问题：What specific validation rules must be applied to report parameters such as date range and filters before report generation?
- 场景：A user submits a report request with an invalid date range or an unsupported filter; the system must decide whether to reject, normalize, or partially accept the parameters.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-015 already states that the system validates parameters before generating the report. The draft's additional 'reject or normalize invalid inputs' is a generic elaboration of that validation obligation rather than a distinct business obligation; no other FR addresses report parameter validation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Validate report parameters and reject or normalize invalid inputs before generating the report.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2883dcfbefea
- 主题：Generate Report
- 审查问题：Which report types and data domains must be supported when users create reports on assets, users, or management data?
- 场景：A user requests an asset report using a date range and filters; the system must generate the correct report from the selected domain.
- 模型初步去向：covered
- 模型解释：FRBLOCK-015 explicitly states that users create reports on assets, users, or management data, that the system validates parameters, and that it generates and stores the report. This is equivalent to the draft obligation to generate reports for those domains according to validated parameters.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Generate reports for assets, users, and management data according to validated parameters.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1e48f41c29bb
- 主题：Store Report Data
- 审查问题：What retention, access, and retrieval rules apply to stored report data after generation?
- 场景：A user generates a report and later needs to retrieve the stored report data or regenerate the output file; the system must retain and expose it appropriately.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence, FRBLOCK-015, supports that report data is stored after generation. It does not establish any defined retention rules, access rules, or retrieval rules for stored report data. The draft obligation adds retention and access policy requirements that are not supported by the source evidence, and no other original FR provides an equivalent obligation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Persist report data with defined retention and access rules after successful generation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ba4da686e081
- 主题：Generate Report
- 审查问题：Which output formats must be available for each report type, and how is the generated file delivered?
- 场景：A user selects PDF for a management data report and expects a downloadable file; the system must produce the requested format and provide access.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 and FRBLOCK-018 already specify equivalent obligations: users select an export format and the system outputs a downloadable report/data file. FRBLOCK-015 also confirms generated report files in Excel/PDF. Therefore the draft obligation to produce report files in supported formats and make them available is already stated in the original FRs.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：Produce generated report files in supported formats and make them available to the user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-88383d1629c3
- 主题：Export Report
- 审查问题：Should the Export Report operation be formally documented with its workflow steps, inputs, and outputs?
- 场景：A user selects a report and export format (CSV, Excel). The FR describes the export flow in prose but does not define the operation's preconditions, success criteria, or error handling.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already specifies that users export existing reports, including the export format input (CSV, Excel), so the draft obligation is equivalent to an existing original FR. The nomination's concern about additional workflow documentation does not change the stated obligation into a new one.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST support exporting an existing report in CSV or Excel format upon user request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4f62488a9355
- 主题：Validate Request
- 审查问题：Should Validate Request be documented as a distinct operation with specific validation rules for the selected report and export format?
- 场景：A user requests export. The system validates the request. Without documented validation criteria, invalid formats or missing reports may not be consistently rejected.
- 模型初步去向：unsupported
- 模型解释：The evidence FRBLOCK-016 only states that 'The system validates the request,' without specifying that the selected report must exist or that the requested export format must be supported. Related report/export FRs also do not state these specific validation rules. The draft therefore introduces specific validation criteria that are not supported by the source text.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST validate that the selected report exists and the requested export format is supported before preparing the export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f0ee1d6d0069
- 主题：Prepare File
- 审查问题：Should Prepare File be documented as an operation that generates the export file from the validated request?
- 场景：After validation, the system prepares the file. The FR does not specify file naming, encoding, or handling of large reports, which may lead to inconsistent outputs.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that the system validates the request, prepares the file, and provides a download link. This is equivalent to generating an export file from the validated request, so the nominated obligation is already covered by an original FR.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST generate an export file in the requested format from the selected report after successful validation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c1b67c702558
- 主题：Provide Download Link
- 审查问题：Should Provide Download Link be documented as an operation that delivers the prepared file to the user?
- 场景：After file preparation, the system provides a download link. The FR does not specify link expiry, access control, or delivery method, which may affect security and usability.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-016 already states that the system prepares the file and provides a download link, and FRBLOCK-018 states that the system generates the file and provides a download link. This is equivalent to the draft obligation to provide the requesting user with a download link for the prepared export file.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system MUST provide the requesting user with a download link for the prepared export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3dc0c91f0d99
- 主题：Store Valid Records
- 审查问题：When an import file contains both valid and invalid rows, should the system store valid records and generate an error report, or reject the entire file?
- 场景：A CSV contains 10 valid rows and 5 invalid rows; the user expects to know which rows failed and whether valid rows were imported.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already states the relevant partial-import behavior: it parses rows and stores valid records with an error report, covering the mixed valid/invalid row handling and failure reporting described by the nomination.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The system should define partial-import behavior for mixed valid and invalid rows and how the error report reflects failures.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-774b1808b0d7
- 主题：Import Asset Data
- 审查问题：After an import completes, is there a documented operation for users to retrieve or download the error report?
- 场景：A user needs to correct invalid rows after an import and must access the error report generated by the system.
- 模型初步去向：unsupported
- 模型解释：The evidence only states that an asset import produces an error report as output; it does not establish that users can retrieve, download, or otherwise access that report after import. The draft therefore adds a user-access requirement not supported by the original FRs.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The system should provide a way for users to access the error report after an asset import.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-09112084626c
- 主题：Validate Request
- 审查问题：Is the 'Validate Request' operation applicable to export asset data requests before file generation?
- 场景：A user submits an export request with selected assets and format; the system must decide whether to validate the request before generating the file.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already states that the system validates the request before generating the file and providing a download link, which is equivalent to validating export requests prior to generating export files. FRBLOCK-015 and FRBLOCK-016 also cover validation before report/file generation.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system shall validate export requests prior to generating export files.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-68eaca9f799d
- 主题：Provide Download Link
- 审查问题：Is the 'Provide Download Link' operation applicable after the system generates the export file?
- 场景：After the system generates the export file, the user needs a download link to retrieve the file.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already states that the system generates the file and provides a download link, which is equivalent to the nominated obligation to provide a download link for each successfully generated export file.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system shall provide a download link for each successfully generated export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-adad0a5fe5c8
- 主题：Stage for senior-admin approval
- 审查问题：Should the permission-assignment workflow explicitly include a staging operation before any permission update, and what determines whether a request is staged rather than applied immediately?
- 场景：An Administrator submits a permission form for a user; the system must hold the requested permission change until a senior-admin reviews it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies that permission-assignment requests are validated, staged for senior-admin approval, and permissions are updated only upon approval. This is equivalent to the draft obligation to stage valid permission-assignment requests before applying any permission change.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system shall stage valid permission-assignment requests for senior-admin approval before applying any permission change.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bb9d761e3e42
- 主题：Validate permission request
- 审查问题：Is validation of the permission request an applicable operation in this workflow, and what validation rules or failure outcomes must be specified?
- 场景：An Administrator submits a permission form with an unknown user ID or an invalid permission level; the system must decide whether to reject or stage the request.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that the system validates the request and stages it for senior-admin approval, which is equivalent to the draft obligation to validate permission-assignment requests before staging them for senior-admin approval.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system shall validate permission-assignment requests before staging them for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f51c91484cf2
- 主题：Update permissions upon approval
- 审查问题：Does the documented workflow apply the permission update operation only after senior-admin approval, and what exactly is updated in the user's permissions?
- 场景：A senior-admin approves a staged permission request; the system updates the target user's management permissions and reports the resulting status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that administrators assign management permissions, the request is staged for senior-admin approval, and permissions are updated upon approval. This is equivalent to updating the target user's management permissions only after senior-admin approval.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system shall update the target user's management permissions only after senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5ffa3934caeb
- 主题：Create
- 审查问题：Is a Create operation applicable to add the new administrator's information during replacement?
- 场景：Reviewing whether replacement creates a new admin record or only updates the current record.
- 模型初步去向：unresolved
- 模型解释：The only relevant original FR, FRBLOCK-020, describes administrator replacement as updating admin records and outputting an updated record with status 'Replaced', but it does not state whether the new administrator's information is created as a new record or represented only within the updated record. The nomination's draft obligation asks for that specification, but the evidence does not supply a definite policy or enough detail to determine whether a Create operation is applicable. Therefore a defensible decision to retain, mark covered, or mark unsupported cannot be made from the provided evidence.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall specify whether the new administrator is created as a new record or represented within the updated record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8fdc5f31eb42
- 主题：Read
- 审查问题：Is a Read operation applicable to retrieve the current admin record using the current admin ID before validation?
- 场景：Reviewing whether the system must look up the current administrator before staging the replacement.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-020 lists the current admin ID as input and describes validation, staging, and updating admin records, but it does not specify a Read operation to retrieve the current admin record before validation. The draft introduces a retrieval/replacement-definition requirement not supported by the source FR.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall define how the current admin record is retrieved for replacement.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d0905adcac28
- 主题：Delete
- 审查问题：Is a Delete operation applicable to remove or deactivate the current system admin as part of replacement?
- 场景：Reviewing whether replacement deletes the old admin or only marks the record as Replaced.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already specifies that replacing the current system admin updates the admin record with status "Replaced," which resolves whether the administrator is deleted, deactivated, or marked as Replaced.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The solution shall define whether the current administrator is deleted, deactivated, or marked as Replaced.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-984d9c996403
- 主题：Stage for Admin Approval
- 审查问题：Should staging for admin approval be documented as an operation that creates a pending approval item accessible to admins?
- 场景：A validated asset request is staged for admin approval, but the FR does not describe the pending state or how admins access it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already requires staging the validated request for admin approval, and several other original FRs (e.g., FRBLOCK-004, FRBLOCK-006, FRBLOCK-012) state equivalent staging-for-admin-approval obligations. The pending-queue wording does not create a materially different business obligation.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must stage validated asset requests in a pending queue for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d00a6d855f8a
- 主题：Update Status on Approval
- 审查问题：Should Update Status on Approval be documented as the operation that records the admin decision and updates the request status?
- 场景：After an admin decision, the system updates status upon approval, but the FR does not specify whether rejection follows the same operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies staging an asset request for admin approval, updating status upon approval, and outputting the stored request with status “Approved” or “Rejected.” FRBLOCK-022 also covers administrators reviewing/approving or rejecting asset requests and the system updating request status. The draft obligation is equivalent to these existing FRs.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must update the asset request status to Approved or Rejected based on the admin decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a36c7ffaee5f
- 主题：Submit Asset Request
- 审查问题：Should Submit Asset Request be documented as the initial operation that accepts and persists the asset request form?
- 场景：A user submits the asset-request form, but the FR does not detail the persistence step or confirmation returned.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies the asset-request form as input and a stored request as output, equivalent to accepting and persisting the form as a Stored Request.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must accept the asset request form and persist it as a Stored Request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-38cd4477373c
- 主题：Approve Asset Request
- 审查问题：Should the 'Approve Asset Request' operation explicitly cover rejection decisions, since FR-22 states administrators review and approve or reject asset requests?
- 场景：The operation name implies only approval, but the FR description includes rejection. Review whether the operation must handle both approval and rejection outcomes.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators review and approve or reject asset requests, and its input includes the approval form decision and reason, which covers the draft obligation to support both approval and rejection decisions and record the decision reason.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The asset request decision operation must support both approval and rejection decisions and record the decision reason when provided.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-780d67308c12
- 主题：Update Request Status
- 审查问题：Should the 'Update Request Status' operation record the decision reason from the approval form together with the status change?
- 场景：FR-22 includes 'Approval form (decision, reason)' as input, but the output only mentions updated status and user notification. Review whether the reason must be persisted with the status update.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-022 identifies 'reason' only as part of the approval form input. The screened FR does not require the system to persist or record that reason when updating request status; its described outputs are updated status and user notification. No checked original FR imposes an equivalent persistence obligation, so the draft adds an unsupported policy.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must persist the decision reason when updating an asset request status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-dcfe39e5ac64
- 主题：Notify Users
- 审查问题：Should the 'Notify Users' operation identify which users are notified after an approval or rejection decision?
- 场景：FR-22 says the system notifies users, but does not define whether the requestor, administrators, or other users receive the notification. Review whether the notification audience needs to be specified.
- 模型初步去向：retained
- 模型解释：FR-22 establishes that the system notifies users, but it does not identify which users are notified after an asset request approval or rejection decision. No checked original FR specifies the affected-user notification obligation, so the draft is an in-scope clarification not already covered.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must notify the affected user(s) when an asset request is approved or rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4a77b4af9b35
- 主题：Send Email Notification
- 审查问题：Should the 'Send Email Notification' operation be triggered by both 'Registration Event' and 'Profile Update Event', or is it applicable only to a subset of these documented event types?
- 场景：FR-23 states notifications are sent for events such as registration or profile updates; the exact trigger scope for the send operation is not fully specified.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-023 only states that email notifications are sent for events such as registration or profile updates. It does not specify whether the Send Email Notification operation is triggered by both registration and profile update events or only a subset, and no other original FR defines this trigger scope. The evidence is therefore insufficient to retain a specific trigger obligation or to mark it covered.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Define the event trigger scope for the 'Send Email Notification' operation across supported event types.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5f689980e651
- 主题：Send Log
- 审查问题：Is the 'Send Log' produced by the same 'Send Email Notification' operation, or does it require a separate logging operation in the documented workflow?
- 场景：FR-23 outputs both 'Sent email' and 'send log'; it is unclear whether logging is part of the send operation or a distinct step.
- 模型初步去向：covered
- 模型解释：FRBLOCK-023 already documents both 'Sent email' and 'send log' as outputs of the email notification operation, so the placement of send logging within that operation is already specified and does not require a separate documented logging operation.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Clarify whether send logging is part of the email notification operation or a separate documented operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5ced1cb73c37
- 主题：User feedback email received
- 审查问题：Should receipt of a user feedback email be treated as a distinct operation that triggers parsing, storage, and administrator notification?
- 场景：A user feedback email arrives at the system mailbox; the workflow should begin with a defined receive operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already specifies receiving user email feedback and initiating parsing, storage, and administrator notification, which is equivalent to the nominated draft obligation.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system should receive user feedback emails and initiate the feedback processing workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-568fd8c4eb8e
- 主题：Parse feedback content
- 审查问题：Does the parse operation need to transform every received feedback email into structured content before storage, and how should parse failures be handled?
- 场景：A feedback email arrives with content that must be extracted and structured for later administrator handling.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-024 only evidences that the system "parses the content" of received user feedback and stores it. It does not establish an obligation to transform every received feedback email into structured content before storage, nor does it specify parse-failure handling or preservation of the original email when parsing fails. The draft therefore introduces unsupported policy beyond the source evidence.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system should parse received user feedback email content into a structured form before storing it, with parse failures handled without losing the original email.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1f3aee907525
- 主题：Store feedback
- 审查问题：Is the store operation required for every parsed feedback item, and should it retain the original email along with the parsed content?
- 场景：After parsing, the feedback content must be available for administrators to review and handle.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-024 already covers receiving email feedback, parsing the content, storing the parsed feedback, and notifying administrators. However, the draft's additional requirement to preserve the original email context alongside the parsed content is not supported by FRBLOCK-024 or any other checked original FR.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system should store parsed feedback content and preserve relevant original email context for administrator handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ecafd9203663
- 主题：Notify administrators
- 审查问题：Should the notify operation be triggered after successful storage, and what feedback details should be included for administrator handling?
- 场景：After feedback is stored, administrators need notification so they can handle the feedback.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already requires storing feedback and notifying administrators for handling, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system should notify administrators after storing feedback, including sufficient detail for them to handle the feedback.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-94a6fea46dcb
- 主题：View Asset Change History
- 审查问题：Should the query support combining asset ID, change type, and change date filters in a single request, or only one criterion at a time?
- 场景：A user wants to find all ownership changes for a specific asset during a given date range, providing asset ID, change type, and change date together.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-025 only states that users query asset change logs by asset ID, change type, or change date. It does not establish that multiple criteria can be combined in a single request or that results must match a supplied combination. The draft therefore introduces unsupported combination-search semantics.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The View Asset Change History operation shall accept optional search criteria for asset ID, change type, and change date, and return change-history entries matching the supplied combination.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0918a12abad2
- 主题：View Asset Change History
- 审查问题：What output details must be included for each change-history entry returned by the query?
- 场景：A user reviews an asset's change history and needs to see who made the change, when it happened, what operation was performed, and the before/after values.
- 模型初步去向：covered
- 模型解释：FRBLOCK-025 already explicitly specifies the same output details for change history: time, operation, user, and before/after values. The nominated obligation adds no new business requirement beyond the checked original FR.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The View Asset Change History operation shall return time, operation, user, and before/after values for each matching change-history entry.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3283d95260df
- 主题：View Asset Change History
- 审查问题：How should the input search criteria be validated when the user provides asset ID, type, or date filters?
- 场景：A user submits a change-history query with a malformed asset ID or an invalid date range.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-025 only defines the View Asset Change History query and its search criteria (asset ID, type, date). It does not state any obligation to validate those criteria before executing the query, and no other original FR covers validation for this operation. The draft therefore introduces a validation policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The View Asset Change History operation shall validate supplied search criteria before executing the change-history query.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9c27d76a5c7d
- 主题：Query Asset Category
- 审查问题：Does the Query Asset Category operation support querying by both category name and category ID together, or are the two criteria mutually exclusive?
- 场景：A user enters both a category name and a category ID to narrow results, but the FR only states 'by name or ID'.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-026 only states users query asset categories by name or ID and does not specify whether category name and category ID may be combined or are mutually exclusive. No other original FR addresses this combined-criteria behavior, so there is insufficient evidence to decide whether the draft obligation is supported, covered, or unsupported.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system must allow asset category queries using category name and/or category ID, and define whether combined criteria are accepted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-189cec257b64
- 主题：Search Criteria
- 审查问题：Should the Search Criteria for viewing asset categories support additional fields such as description or asset count, or only category name and ID?
- 场景：A user wants to find categories by description text or by number of assets, but the FR limits input to category name and ID.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already specifies the search criteria for viewing asset categories as category name and category ID, which is equivalent to the draft's accepted criteria and excludes other criteria by enumeration.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system must accept category name and category ID as search criteria for viewing asset categories, and explicitly scope any other criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b0dd914c439f
- 主题：Validate changes
- 审查问题：Should the FR document what happens when the 'Validate changes' operation fails?
- 场景：An administrator submits a category-edit form with invalid name or description; the system must decide whether to stage the change or return validation errors.
- 模型初步去向：retained
- 模型解释：FRBLOCK-027 covers validating changes and staging them for approval but does not specify the failure path for category-edit validation. No original FR states the equivalent obligation to prevent staging and notify the administrator when validation fails, and the screening record treats this failure handling as in scope for FRBLOCK-027 rather than covered or out of scope.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must prevent staging and notify the administrator when category-edit data fails validation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3675def4c6f9
- 主题：Senior-admin approval
- 审查问题：Does the senior-admin approval operation need an explicit rejection outcome?
- 场景：A senior admin declines a staged category edit; the original category data and status must be defined.
- 模型初步去向：retained
- 模型解释：FRBLOCK-027 establishes that category changes are staged for senior-admin approval but does not define the rejection outcome or what happens to the original category data when the senior admin declines. This is an in-scope completeness obligation for the existing approval operation, not an equivalent requirement already stated in the original FRs.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must support senior-admin rejection of staged category changes while preserving the original category data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d5cc31182e3a
- 主题：Update Category Upon Approval
- 审查问题：Should the update operation upon approval be explicitly atomic with setting the status to 'Modified'?
- 场景：Senior-admin approval is received; the system updates the category data and status.
- 模型初步去向：unsupported
- 模型解释：The original FRs, including FRBLOCK-027, state that staged category changes are updated upon approval and may output status 'Modified,' but none requires that the change and status update be atomic or happen in a single approved update. The draft introduces an atomicity constraint not supported by the source requirements.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must apply the staged category changes and set status to 'Modified' in a single approved update.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall notify users of the request decision when an administrator approves or rejects an asset request.

2. [model_preliminarily_retained] The system shall produce the updated operation status only after the approval-start request has been successfully validated and the operation has been executed upon approval.

3. [model_preliminarily_retained] The system shall define and handle the behavior when modification data fails validation, including whether the user can correct and resubmit the modification form.

4. [model_preliminarily_retained] The system shall apply defined matching semantics for asset name, type, and ID search criteria in Query Asset Details, specifying whether matching is exact or partial and case-sensitive or case-insensitive.

5. [model_preliminarily_retained] The system shall allow an administrator to reject a staged transfer request, record the request status as 'Rejected', and leave the asset ownership unchanged.

6. [model_preliminarily_retained] When an asset return request is denied, the system shall set the return request to the Rejected outcome and notify the requesting user of the denial.

7. [model_preliminarily_retained] The system shall, when an administrator denies approval of a staged deletion request, set the deletion request status to Rejected and leave the asset record unchanged.

8. [model_preliminarily_retained] The system shall enforce a defined empty-search policy for Query User Details, including whether at least one of username, email, or department is required and, if empty searches are allowed, the default result set returned.

9. [model_preliminarily_retained] The system shall resolve the supplied user ID to the corresponding target user record before validating and processing the deletion request.

10. [model_preliminarily_retained] The system shall define and document the outcome of a senior-admin rejection of a staged workflow modification, including whether the original workflow remains unchanged and the status retained by the workflow.

11. [model_preliminarily_retained] The system shall notify the affected user(s) when an asset request is approved or rejected.

12. [model_preliminarily_retained] The system shall record a change-history entry when an asset change occurs, associating it with the asset ID and change details, so that it can be retrieved by the View Asset Change History query.

13. [model_preliminarily_retained] The system shall record a change type for each asset change event so that the change type can be used as a search criterion in the View Asset Change History query.

14. [model_preliminarily_retained] The system shall prevent category-edit changes that fail validation from being staged for approval and shall notify the administrator of the validation errors.

15. [model_preliminarily_retained] The system shall support senior-admin rejection of staged category changes, preserve the original category data, and record the rejection status.
