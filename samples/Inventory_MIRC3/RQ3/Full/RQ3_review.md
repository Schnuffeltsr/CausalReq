# RQ3 审查材料：Inventory_MIRC3 / Full

**注意：下列去向只是模型初步筛查，不是人工有效性结论。**

## 运行设置

```json
{
  "signed_propagation": true,
  "isolated_review": true,
  "operation_review": true,
  "full_document_validation": true
}
```

## dependency：20 条提名

### DEP-001
- 主题：Stage change for admin approval → Deletes the Record upon Approval
- 审查问题：When admin approval is granted for a staged change, does the system delete the asset record associated with that staged change, and is this deletion intended to occur for every approved staged change?
- 场景：FRBLOCK-002 and FRBLOCK-008 state that changes are staged for admin approval. FRBLOCK-006 states that admin approval deletes the record upon approval. The source active meaning is that the change has been staged and is pending admin approval, and the target active meaning is that the system deletes the asset record after admin approval is granted.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-006 already covers deletion of the record upon admin approval for a staged deletion request, but the draft generalizes this to any approved staged change. Other original FRs such as FRBLOCK-002 and FRBLOCK-008 specify updates to the asset/user record upon approval rather than deletion, so the proposed universal deletion policy is not supported.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006, FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：When an admin approves a change that has been staged for admin approval, the system shall delete the asset record associated with that approved staged change.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Validate Configuration Details → Activate Workflow
- 审查问题：Does the documented requirement ensure that Activate Workflow is gated by Validate Configuration Details through the staged senior-admin approval path, so activation does not occur unless configuration validation has succeeded and senior-admin approval has been granted?
- 场景：The FRBLOCK-011 sequence describes validating configuration details, staging the setup for senior-admin approval, and activating the workflow upon approval. The dependency from Validate Configuration Details to Activate Workflow is indirect and depends on the intermediate staging and approval states.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the system validates configuration details, stages the setup for senior-admin approval, and activates the workflow upon approval, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：Workflow activation shall occur only after configuration details have been validated and the staged setup has received senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Approval-start request → Deletes the Record upon Approval
- 审查问题：For an approval-start request that has been validated and staged for admin review, does the requirement explicitly state that admin approval triggers deletion of the record, and is the record-deletion condition unambiguous?
- 场景：An approval-start request containing an asset ID and operation type is submitted; it is validated, staged for admin review, and then admin approval is granted. The documented dependency leads from that approval to deletion of the record upon approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states an equivalent obligation: the request is validated, staged for admin approval, and the record is deleted upon approval. FRBLOCK-010 also provides an equivalent approval-triggered deletion obligation for senior-admin approval. Therefore the draft does not add a new in-scope business obligation.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval of the approval-start request, the system shall delete the record associated with the approved request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Validates the Request → Update status to Modified
- 审查问题：Does the requirement clearly establish that the status update to “Modified” is gated by admin approval after validation and staging, rather than occurring upon validation alone?
- 场景：The dependency links “Validates the Request” to “Update status to Modified” through “Staged for Admin Approval” and “Admin approval.” The supplied FR text states the system “validates the request,” “stages it for admin approval,” and “updates the status to ‘Modified’” “upon approval.”
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already states that the system validates the data, stages the change for admin approval, and updates the status to "Modified" upon approval, which establishes the same approval-gated "Modified" status update. The deletion-specific staging in FRBLOCK-006 is additional context, but the gating obligation is already covered.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：When the system validates a deletion request, it must stage the request for admin approval, and only upon admin approval must the system update the asset record status to “Modified.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Senior Admin Approval Event → Workflow Configured
- 审查问题：Does the requirement set explicitly tie the occurrence of a senior-admin approval event to the workflow being stored with status "Configured" via activation, or does it only describe these as separate outcomes?
- 场景：A senior-admin approval event occurs for a workflow. The supplied FR states that senior-admin approval activates the workflow and that activation produces a stored workflow with status "Configured." The source-target dependency under review is from the approval event to the workflow being in Configured status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the system stages workflow setup for senior-admin approval, activates the workflow upon approval, and outputs a stored workflow with status "Configured," which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：Upon senior-admin approval, the workflow shall be activated and stored with status "Configured."
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Asset Request Form → User Notification
- 审查问题：Does the requirements specification define the user notification obligation that follows an asset request submitted through the Asset Request Form when administrators approve or reject the request, including whether the notification must be produced for the affected user(s) and what request information from the form it must convey?
- 场景：An asset request is submitted using the Asset Request Form with name, type, quantity, and purpose populated. Administrators review and approve or reject asset requests, and the system notifies users. The requirements must clarify whether the User Notification is required after the approval or rejection decision and how it relates to the submitted Asset Request Form data.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that after administrators approve or reject asset requests, the system updates the request status and notifies users, which is equivalent to the nominated obligation to notify affected users of the approval/rejection decision.
- 原文证据 FR：FRBLOCK-021, FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：When an asset request submitted through the Asset Request Form is approved or rejected, the system shall notify the affected user(s) of the decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Activate Workflow → Workflow Configured
- 审查问题：Does FRBLOCK-011 explicitly require that activating the workflow results in the stored workflow having status “Configured,” rather than merely describing that outcome?
- 场景：The source activity is “Activate Workflow,” and the linked target state is “Workflow Configured.” The supplied FR quotations state that the system “activates the workflow” and that the output is a “Stored workflow with status ‘Configured.’”
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that activating the workflow produces a stored workflow with status “Configured,” which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：When the workflow is activated, the system shall set the stored workflow status to “Configured.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Validates the Request → Update Status on Approval
- 审查问题：Does the requirement specify that 'updates status upon approval' applies only after a request has been validated and staged for admin approval, rather than treating admin approval alone as sufficient to trigger the status update?
- 场景：A request is submitted, the system validates the request, stages it for admin approval, and an admin approval decision occurs. The documented dependency shows validation enabling staging and admin approval triggering the status update upon approval; the review must confirm whether the status update is scoped to the validated and staged request path.
- 模型初步去向：covered
- 模型解释：The obligation is already stated equivalently in original FRBLOCK-021: “The system validates the request, stages it for admin approval, and updates status upon approval.” This sequences validation and staging before the approval-triggered status update, matching the nominated condition that admin approval alone is not sufficient.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system shall update the request status upon admin approval only when that request has been validated and staged for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Query Approval Status → Approval Status Details
- 审查问题：When users query approval status for asset or user operations, does the requirement define what approval status details must be provided, including the relevant status values (pending, in progress, approved, rejected)?
- 场景：A user checks the status of an asset or user operation and expects the system to return approval status details.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already states that users check the status of asset or user operations, lists the statuses pending, in progress, approved, and rejected, and defines the output as approval status details. Therefore the nominated obligation is already covered by the checked original FR.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall provide approval status details for asset or user operations, showing the current approval status as pending, in progress, approved, or rejected when a user queries approval status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Approve Asset Request → Notify Users
- 审查问题：Does the requirement for 'Approve Asset Request' explicitly define the notification obligation to 'Notify Users' after an administrator approves or rejects an asset request, including what decision information must be communicated?
- 场景：An administrator reviews an asset request and approves or rejects it. The documented dependency indicates this action triggers the system to notify users about the request decision.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators approve or reject asset requests and that the system updates the request status and notifies users, which is equivalent to the drafted obligation to notify users of the request decision.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：When an administrator approves or rejects an asset request, the system shall notify users of the request decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Validate approval-start request → Updated operation status
- 审查问题：Does FRBLOCK-012 explicitly define that the updated operation status is produced only after an approval-start request is validated, staged for admin review, and the operation is executed upon approval, rather than at an earlier point in the dependency chain?
- 场景：The documented source–target dependency links 'Validate approval-start request' to 'Updated operation status' through intermediate relations: validation stages the request for admin review, staging enables operation execution upon approval, and execution produces the updated operation status. The active meanings are that the request has been validated and is ready for staging, and that the operation status has been updated to reflect the current state of the operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already explicitly states the same obligation: it validates the approval-start request, stages it for admin review, executes the operation upon approval, and outputs an approval-process record and updated operation status. The screening for FRBLOCK-012 marks it as covered, so the nominated dependency does not add a new business obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：When an approval-start request is validated and staged for admin review, the operation must be executed upon approval and the operation status must be updated to reflect the executed operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Transfer form → Transfer Asset
- 审查问题：For the dependency where Transfer Asset relies on Transfer form as input, how do the requirements ensure that a submitted Transfer form with asset ID and new recipient is available before the transfer asset workflow is requested or activated?
- 场景：FRBLOCK-004 lists 'Input: Transfer form (asset ID, new recipient)' for the Transfer Asset workflow, and states that users request to transfer assets. The source active meaning is that the transfer form has been submitted with asset ID and new recipient; the target active meaning is that the transfer asset workflow is active and can be requested by users.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already specifies 'Input: Transfer form (asset ID, new recipient)' for the Transfer Asset workflow, which is equivalent to the draft obligation requiring a submitted Transfer form with asset ID and new recipient as the workflow input condition.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall require a submitted Transfer form containing asset ID and new recipient as the input condition for the Transfer Asset workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Admin approval → Operation executed upon approval
- 审查问题：Does FRBLOCK-012 state that admin approval triggers execution of the operation, or does it leave the execution timing and the specific operation undefined?
- 场景：An admin approval occurs, and the documented dependency indicates that the operation is executed upon approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system “executes the operation upon approval,” which is equivalent to the draft obligation that admin approval triggers execution.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval, the system shall execute the operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Update record upon approval → Status Modified
- 审查问题：Does the requirement need to explicitly state that the user record update performed upon approval results in the updated user record having status 'Modified'?
- 场景：The documented dependency is a positive PRODUCES relation from the source 'Update record upon approval' to the target 'Status Modified'. FRBLOCK-008 quotes 'updates the record upon approval' and 'Updated user record with status "Modified."'. The model ACE is a priority score, not evidence that this obligation is missing.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 explicitly states that profile changes are staged for admin approval, the record is updated upon approval, and the output is an updated user record with status 'Modified,' which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Upon approval of staged changes, the system shall update the user record, and the updated user record shall have the status 'Modified'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：Return Form → Update Asset Status to Returned
- 审查问题：Does the requirement define how a submitted Return Form (asset ID, return date) leads to updating the asset status to “Returned,” including the validated and approval-staged return process in between?
- 场景：A user submits a return form containing the asset ID and return date. The system initiates the asset return, validates the request, stages it for approval, and updates the asset status to “Returned” upon approval. The review question checks whether the requirements make this source-to-target dependency and end-to-end outcome explicit and testable.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already specifies the same obligation: return form with asset ID and return date, return initiation, validation, approval staging, and updating asset status to “Returned” upon approval.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：When a return form containing the asset ID and return date is submitted, the system shall process the return request through validation and approval staging, and shall update the asset status to “Returned” upon approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Approval-start request → Admin approval
- 审查问题：Does the requirement explicitly state that admin approval depends on the approval-start request being validated and staged for admin review?
- 场景：The dependency chain shows the approval-start request is validated, then staged for admin review, and admin approval is reached from that staged state. FRBLOCK-012 uses the phrases 'validates the request', 'stages it for admin review', and 'approval', but the supplied text does not itself state the dependency condition between staging and approval.
- 模型初步去向：covered
- 模型解释：Equivalent obligations are already stated in other checked original FRs. For example, FRBLOCK-004, FRBLOCK-006, FRBLOCK-008, FRBLOCK-010, FRBLOCK-011, FRBLOCK-019, FRBLOCK-020, FRBLOCK-021, and FRBLOCK-027 all specify that the system validates a request, stages it for admin/senior-admin approval, and only then performs the approval-dependent update/action. This establishes the same business dependency: approval follows validation and staging for review. Although FRBLOCK-012 itself is not explicit, the nominated obligation is covered elsewhere.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Admin approval shall occur only after the approval-start request has been validated and staged for admin review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Validate Export Request → Generate Export File
- 审查问题：Does FRBLOCK-018 explicitly require that the system generate the export file only after the export request has been successfully validated, as suggested by the dependency from 'validates the request' to 'generates the file'?
- 场景：Traceability shows Validate Export Request ENABLES Generate Export File. The source active meaning is 'the system has validated the export request successfully'; the target active meaning is 'the system has generated the export file successfully'. The supplied FR quotations are 'validates the request' and 'generates the file'.
- 模型初步去向：retained
- 模型解释：The original FRBLOCK-018 states that the system validates the request, generates the file, and provides a download link, but it does not explicitly state that file generation is conditioned on successful validation. The documented ENABLES dependency supports this prerequisite, and no other original FR already covers an equivalent obligation for export file generation.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system shall generate the export file only if the export request has been validated successfully.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Export Asset Data → Downloadable Data File
- 审查问题：Does the requirement explicitly state that a successful Export Asset Data operation must produce a downloadable data file that is available for download?
- 场景：A user successfully exports the selected asset data.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already explicitly states that the system generates the file and provides a download link, with 'Downloadable data file' as the output. This is equivalent to the nominated obligation that a successful Export Asset Data operation produces a downloadable data file available for download.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：Upon successful export of selected asset data, the system shall generate a downloadable data file that is available for download.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Validate modification data → Operation executed upon approval
- 审查问题：Do the requirements explicitly state that the requested operation is executed only after both successful validation of the modification data and admin approval of the staged change, rather than upon approval alone or upon validation alone?
- 场景：FRBLOCK-002 states the system validates the data and stages the change for admin approval; FRBLOCK-012 states the operation is executed upon approval. This creates an indirect dependency from Validate modification data to Operation executed upon approval through admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already states that the system validates the modification data, stages the change for admin approval, and updates the status upon approval, which is equivalent to requiring both validation and admin approval before executing the operation. FRBLOCK-008 similarly specifies validation, staging for admin approval, and updating the record upon approval.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-008, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall not execute the requested operation unless the submitted modification data has been validated and the staged change has received admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Approval-start request → Transferred
- 审查问题：For the documented dependency from an Approval-start request to Transferred, does the requirements set specify the complete end-to-end obligation that a validated and approved approval-start request results in the ownership update and output status “Transferred”?
- 场景：An approval-start request containing an asset ID and operation type is submitted; the system validates the request, stages it for admin review, approval is given, the system updates the ownership upon approval, and the output is updated owner information with status “Transferred.”
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already specifies the equivalent end-to-end obligation: it validates the request, stages it for admin approval, updates ownership upon approval, and outputs updated owner information with status “Transferred.”
- 原文证据 FR：FRBLOCK-004, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：When an approval-start request is approved, the system shall update the ownership and produce updated owner information with status “Transferred.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：70 条提名

### ISOLATED-d1066142271d
- 主题：Admin
- 审查问题：Should 'Admin' have a documented connection to the 'Administrators' actor in FR-01, or is it intentionally a separate administrative role?
- 场景：Reviewer sees 'Admin' as a graph-isolated actor while FR-01 uses 'Administrators' to receive notification for review.
- 模型初步去向：unsupported
- 模型解释：No original FR mentions the actor 'Admin' or any alias relationship between 'Admin' and 'Administrators'. FRBLOCK-001 only states that Administrators are notified for review. The draft obligation to clarify whether 'Admin' is an alias is therefore not supported by the source evidence.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall clarify whether 'Admin' is an alias for the administrator role notified during asset registration.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-044802effbcc
- 主题：Administrator
- 审查问题：Does 'Administrator' refer to the same actor as 'Administrators' in FR-01, or is it a distinct role requiring its own documented connection?
- 场景：Reviewer sees 'Administrator' as a graph-isolated actor while FR-01 documents 'Administrators' being notified for review.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-001 only states that 'Administrators are notified for review'; it does not introduce or define a singular 'Administrator' role, nor does any checked original FR require the asset registration workflow to clarify role equivalence. The draft therefore adds a clarification obligation without source support.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall clarify whether 'Administrator' is the same role as 'Administrators' responsible for reviewing registered assets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9149814de7ba
- 主题：Approved
- 审查问题：Does 'Approved' represent a state that follows 'Registered' after administrator review, or is it unrelated to this FR?
- 场景：FR-01 sets status to Registered and notifies administrators for review, but does not mention an Approved state.
- 模型初步去向：unsupported
- 模型解释：The source FR only states that submitted assets are stored with status "Registered" and that administrators are notified for review. It does not mention an "Approved" state or a transition from "Registered" to "Approved" after administrator review, and no other original FR defines such a transition for the asset registration workflow. The draft therefore introduces a workflow decision not supported by the source.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall define whether a Registered asset can transition to Approved after administrator review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-daaeb9300bbd
- 主题：Rejected
- 审查问题：Should 'Rejected' be a possible outcome of administrator review in this workflow, and if so, how is it reached from Registered?
- 场景：FR-01 notifies administrators for review but does not document rejection handling or a Rejected status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators review and approve or reject asset requests, and that the system updates the request status and notifies users. This is an equivalent business obligation covering whether administrator review can result in Rejected and the resulting status update.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall define whether administrator review can result in a Rejected status and the required transition.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f5224f8482e4
- 主题：Pending Operation Status
- 审查问题：Does 'Pending Operation Status' apply to the administrator review prompted by FR-01, or is it unrelated to asset registration?
- 场景：FR-01 notifies administrators for review, which may imply a pending review state not currently documented.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-001 only states that administrators are notified for review and does not mention a pending operation status or require the workflow to define whether review creates one. Other original FRs mention pending status only for querying or other operation statuses, not for asset registration administrator review. The draft therefore introduces an unsupported policy/definition requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall define whether administrator review creates a pending status for the asset or operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ba6a57af5568
- 主题：Senior-admin approval required
- 审查问题：Does 'Senior-admin approval required' apply to the administrator review prompted by FR-01, or is senior approval out of scope?
- 场景：FR-01 notifies administrators for review, but does not mention senior administrator approval requirements.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-001 only states that administrators are notified for review; it does not establish or support any senior-administrator approval requirement for asset registration. No original FR provides an equivalent obligation or otherwise supports adding a clarification obligation about senior-admin approval before registration.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The asset registration workflow shall clarify whether senior administrator approval is required before an asset is registered.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d358ae02cf93
- 主题：Asset change
- 审查问题：Should the staged asset change be represented as a distinct business entity with its own lifecycle, rather than only as a transient step in the modification workflow?
- 场景：A user submits a modification and the system stages the change for admin approval. If the change is not recorded as an entity, approvals and rejections may not be auditable.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already obligates the system to stage a submitted operation for admin review and produce an approval-process record with updated operation status, which is functionally equivalent to creating an asset change record upon modification submission and tracking its approval status. The staged asset-change obligation is therefore already covered by an existing FR.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall create an asset change record when a user submits a modification and track its approval status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-459a1ecfc528
- 主题：Pending Operation Status
- 审查问题：Should a staged asset modification be assigned a pending status while awaiting admin approval?
- 场景：A user submits a valid modification. The change is staged, but the FR does not define the status of the change request during the approval wait.
- 模型初步去向：unsupported
- 模型解释：The cited FR stages the change for admin approval but does not specify a Pending status while approval is outstanding; it only mentions updating status to Modified upon approval. The draft adds a new status policy not supported by the source.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall mark a staged asset modification as Pending until an Admin approves or rejects it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f67005874d69
- 主题：Rejected
- 审查问题：How should the system handle an admin rejection of a staged asset modification?
- 场景：An admin reviews a staged modification and does not approve it. The FR only describes the approval path and status Modified.
- 模型初步去向：unsupported
- 模型解释：The cited FRBLOCK-002 only states that a staged change is approved and status becomes “Modified”; it does not specify admin rejection or recording a rejection outcome for staged asset modifications. Other original FRs may mention rejection for separate workflows such as asset requests, but none covers rejection of a staged asset modification. Therefore the draft introduces an unsupported obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall allow an Admin to reject a staged asset modification and record the rejection outcome.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-20384ad562a3
- 主题：User
- 审查问题：Is the isolated 'User' role the same actor as the 'Users' referenced in FR-03, and if so what query permissions does it have for asset details?
- 场景：An authenticated end user attempts to search asset details; the system needs to know whether 'User' is a recognized role with the same access as the FR-03 'Users' actor.
- 模型初步去向：unsupported
- 模型解释：The draft asks to clarify an isolated 'User' role and its mapping/query permissions relative to the FR-03 'Users' actor. No original FR defines an isolated 'User' role or maps it to 'Users.' FR-03 only states that 'Users' can search for asset details by name, type, or ID; it does not support adding or resolving a separate role mapping or permission clarification.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Clarify the mapping and query permissions of the isolated 'User' role relative to the FR-03 'Users' actor.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e007997cbd37
- 主题：Admin
- 审查问题：Should the isolated 'Admin' role also be able to query asset details, or is FR-03 intentionally limited to non-admin users?
- 场景：An administrator needs to look up asset details for support or audit purposes, but the FR only mentions Users as the querying actor.
- 模型初步去向：unresolved
- 模型解释：FR-03 only states that 'Users search for asset details using name, type, or ID' and does not define whether the isolated Admin/Administrator role is included or excluded from that actor scope. No other original FR defines asset query permissions for Admin. Because the role taxonomy and the intended scope of 'Users' are not specified, the evidence is insufficient to decide whether Admin asset querying is a supported new obligation or already covered.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Clarify whether Admin/Administrator roles are included in the asset query actor scope.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-825837f19fdf
- 主题：Admin
- 审查问题：Is the Admin's role in the transfer approval workflow documented beyond the phrase 'admin approval'?
- 场景：A user submits a transfer request. The request is staged for admin approval, but the FR does not define which Admin actions (approve, reject, or request more information) are available.
- 模型初步去向：unsupported
- 模型解释：The only relevant evidence states that a transfer request is staged for admin approval and ownership is updated upon approval. It does not specify which Admin actions are available (e.g., approve, reject, request more information), so the draft obligation to document those actions goes beyond the source evidence.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：Document the Admin action(s) that can be taken on a staged transfer request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7a23cce0e16e
- 主题：User
- 审查问题：Are any constraints on which User may request an asset transfer documented?
- 场景：A user wants to transfer an asset. The FR states 'Users request to transfer assets' but does not specify whether any user can transfer any asset or only assets they own.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-004 only states that users request asset transfers and does not specify eligibility, ownership, or department constraints. None of the screened original FRs documents such constraints. The draft obligation to define which users may request transfers and any ownership/department constraints would introduce a new policy rather than document an existing source obligation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：Define which users may request transfers and any ownership or department constraints.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c388417a50b6
- 主题：Admin
- 审查问题：Is the isolated Admin element the intended actor for the approval mentioned in FR-05, and should that connection be documented?
- 场景：A return request is staged for approval; an Admin may be the role that approves it, causing the asset status to become Returned.
- 模型初步去向：unsupported
- 模型解释：The cited FR-05 only states that return requests require approval ('upon approval'); it does not identify or require definition of an authorized approver role. The screenings show no original FR defines Admin (or any role) as the approver for asset return requests; FR-22 concerns asset requests generally, while other admin approval statements concern different workflows. The draft therefore introduces a new approver-role policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system must define the authorized approver role (e.g., Admin) for asset return requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-859c44819ae0
- 主题：Approved Operation Status
- 审查问题：Should the isolated Approved Operation Status be connected to the return request's approval state, distinct from the asset status Returned?
- 场景：A return request is approved; the system records the request as Approved and then updates the asset status to Returned.
- 模型初步去向：retained
- 模型解释：The relevant original FRs cover the return approval workflow and an operation-status concept, but no checked FR explicitly requires the return request's approval outcome to be represented as an operation status that is distinct from the asset status Returned. This is an in-scope business obligation supported by the return-approval and operation-status context, so it should be retained as a supplement.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system must represent the return request's approval outcome as an operation status before or alongside updating the asset status to Returned.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-33bad7fff5d4
- 主题：Admin
- 审查问题：What documented connection should exist between the Admin actor and the deletion approval step in FR-06?
- 场景：An admin reviews a staged deletion request for an obsolete asset.
- 模型初步去向：unsupported
- 模型解释：FR-06 only documents that deletion requests are staged for generic admin approval and deleted upon approval. It does not establish or support a requirement to identify which specific admin role is authorized to approve deletion requests for obsolete assets, so the draft introduces a policy beyond the source evidence.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must identify which admin role is authorized to approve deletion requests for obsolete assets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ede671a617dc
- 主题：User
- 审查问题：Is the User actor intended to submit deletion requests, and what connection to the Deletion Request input must be documented?
- 场景：A user identifies an obsolete asset and requests its removal.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already specifies that Users request removal of obsolete assets and identifies Deletion request (asset ID) as the input, which is equivalent to defining the user role permitted to submit deletion requests and its connection to the Deletion Request input.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must define the user role permitted to submit deletion requests for obsolete assets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-957727eced12
- 主题：Rejected
- 审查问题：Should the deletion workflow document a rejected outcome when admin approval is not granted?
- 场景：An admin does not approve a staged deletion request.
- 模型初步去向：retained
- 模型解释：FRBLOCK-006 covers staging a deletion request for admin approval and deleting the record upon approval, but it does not specify the rejected outcome or next action when approval is not granted. The question concerns the same in-scope deletion approval workflow, and no checked original FR states an equivalent obligation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must specify the outcome and next action when an admin does not approve a deletion request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c8b4649552bc
- 主题：Senior Admin
- 审查问题：Does FR-06 require senior-admin approval for deletion requests, or is any admin sufficient?
- 场景：A deletion request is staged for approval, and the available roles include Admin and Senior Admin.
- 模型初步去向：covered
- 模型解释：An original FR (FRBLOCK-010) explicitly states that deletion requests are staged for senior-admin approval, so the approval-role ambiguity is already resolved by the source requirements.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must clarify whether deletion approval requires a senior admin role or any admin role.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b16c4e46d5b9
- 主题：Administrator
- 审查问题：Does the FR need to document the Administrator's authorization or permission check before creating new user accounts?
- 场景：An Administrator is the actor for adding a user, but the FR does not state whether the system must verify that the acting user has Administrator privileges.
- 模型初步去向：retained
- 模型解释：FRBLOCK-007 identifies Administrators as the actors who create new user accounts, but no checked original FR specifies that the system must verify the acting user's Administrator privileges before allowing account creation. The obligation is in-scope for user account creation and is not covered by any existing FR.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system may need to verify that the acting user has Administrator privileges before allowing new-user creation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c5dde45e21d1
- 主题：Send Activation Email
- 审查问题：Does the Send Activation Email function need a documented connection to an email template or delivery service in this FR?
- 场景：The FR states that the system sends an activation email, but it does not specify the email content, sender, or delivery channel.
- 模型初步去向：unsupported
- 模型解释：The only relevant original FR, FRBLOCK-007, states that an activation email is sent but does not require documenting its sender, template, or delivery channel. No other original FR imposes that obligation. The draft's 'may need to document' language introduces a speculative requirement that is not supported by the source text.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system may need to document the activation email's sender, template, and delivery channel.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-724f07c00d89
- 主题：Admin
- 审查问题：Should the Admin actor be explicitly connected to the profile-edit approval step, or is the phrase 'admin approval' sufficient?
- 场景：A user edits their profile; the system validates and stages the changes for admin approval, but FR-08 names an admin only within that approval phrase.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already states that profile changes are staged for admin approval and the record is updated upon approval, which is equivalent to the nominated obligation. The Admin actor is connected through the stated admin approval step in the profile-edit workflow.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must route staged profile edits to an Admin for approval before the user record is updated.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e9e8dfe097d3
- 主题：User
- 审查问题：Should the User actor be documented as the initiator of the profile-edit workflow, or is the plural 'Users' sufficient?
- 场景：A user edits their own profile; FR-08 describes the action but does not define the actor as a distinct connected element.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already states 'Users edit their own profiles,' which is equivalent to the draft obligation that Users can initiate editing of their own profile. The plural actor 'Users' is sufficient; no separate singular User actor requirement is introduced.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Users must be able to initiate editing of their own profile.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3e58f0e17748
- 主题：Senior Admin
- 审查问题：Does the FR need to document how the 'Senior Admin' approval role is identified and distinguished from the 'Administrators' who initiate deletion?
- 场景：An administrator submits a user deletion request; the system stages it for senior-admin approval, but the FR only says 'senior-admin approval' without defining the role, identifier, or authorization source.
- 模型初步去向：retained
- 模型解释：FRBLOCK-010 establishes that a user deletion request is staged for senior-admin approval, but none of the checked original FRs define who qualifies as the Senior Admin approver, how that approver is resolved, or how the approval role is distinguished from the Administrators who initiate deletion. The draft obligation is therefore an in-scope approval-role clarification not covered by the existing FRs.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Define the senior-admin approver role, how it is resolved, and its authority to approve user deletion requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5e5d6c90b522
- 主题：Senior-admin approval required
- 审查问题：Should the FR document whether senior-admin approval is a mandatory precondition that must be recorded before the delete operation can run?
- 场景：The FR states deletion occurs upon approval; without a documented connection between the approval constraint and the delete operation, the workflow may not enforce that approval precedes deletion.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already states that the record is staged for senior-admin approval and deletes the record upon approval. This is equivalent to requiring senior-admin approval as a precondition for user record deletion, and the staged approval workflow implies the approval is recorded.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Require a recorded senior-admin approval as a precondition to executing user record deletion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-14a701f1d88e
- 主题：Senior Admin
- 审查问题：How does the Senior Admin actor receive or access a staged workflow configuration to provide approval, and what documented connection exists between the Senior Admin and the approval step beyond the phrase 'senior-admin approval'?
- 场景：An administrator has submitted a valid workflow configuration, and the system stages it for senior-admin approval before activation.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-011 only states that the setup is staged for senior-admin approval and activated upon approval. It does not document how the Senior Admin receives or accesses the staged workflow configuration, nor does it define a review, approve, or reject mechanism. No checked original FR supplies that equivalent obligation, so the draft adds an unsupported mechanism/policy.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must provide a documented mechanism for Senior Admin to review and approve or reject a staged workflow configuration.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-83757b27b91c
- 主题：Senior-admin approval required
- 审查问题：Is 'Senior-admin approval required' a distinct state or condition that the workflow configuration enters after validation and before activation, and how is this state represented in the system?
- 场景：An administrator submits a valid workflow configuration; the system stages it and awaits senior-admin approval before activation.
- 模型初步去向：covered
- 模型解释：The obligation is already stated by original FRBLOCK-011, which specifies that the system stages the workflow setup for senior-admin approval and activates it upon approval. This covers the requested pending-approval state for staged workflow configurations awaiting senior-admin approval.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must represent a pending-approval state for workflow configurations that are staged and awaiting senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-db8ac57b8543
- 主题：Administrator
- 审查问题：Does the FR need to document the Administrator actor as the reviewer of staged approval requests?
- 场景：A request is staged for admin review, but the FR text uses 'admin review' without explicitly linking the staged state to the Administrator actor; the Administrator element is supplied as isolated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the request is staged for admin review, which is equivalent to making staged approval requests available to Administrators for review. Several other original FRs also specify staging for admin approval or Administrators reviewing/approving requests, so the draft obligation is already covered.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall make staged approval requests available to Administrators for review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4a224f68464a
- 主题：Pending Operation Status
- 审查问题：Should the FR define when an operation is in Pending status while an approval process is awaiting review?
- 场景：The FR describes starting an approval process and updating operation status, but the isolated Pending Operation Status element is not referenced; the FR does not specify the operation status during admin review.
- 模型初步去向：retained
- 模型解释：The original FRs describe approval workflows and note that operation status is updated after approval, but none defines the operation status while an approval process is awaiting administrator review. The Pending status is referenced as a queryable operation status in the source set (FR-013), so the concept is in scope, but no original FR states the equivalent assignment obligation. The draft is therefore an in-scope missing business obligation rather than a covered or out-of-scope requirement.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall set the operation status to Pending while the approval process is awaiting administrator review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-911630959b5e
- 主题：Approved Operation Status
- 审查问题：Should the FR define the Approved operation status after an administrator approves the request?
- 场景：The FR says the operation executes upon approval, but it does not specify whether the operation status becomes Approved or another status; the Approved Operation Status element is supplied as isolated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that upon administrator approval the request status is updated and stored as “Approved” (or “Rejected”). This is equivalent to the nominated obligation to mark the approved operation/request status as Approved after administrator approval.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall mark the operation status as Approved when the administrator approves the request and the operation is executed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-42f3bcbd7ee5
- 主题：Pending Operation Status
- 审查问题：Does the pending status apply to all asset and user operations, or only certain operation types, and should the FR document which operations can be pending?
- 场景：A user queries approval status and sees an operation marked pending; reviewers need to know whether every asset or user operation can be pending or only specific operation types.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already enumerates the operation types that enter approval status (registration, usage, transfer, return) and describes staging them for admin review and status updates, which is equivalent to identifying which asset/user operation types can have a pending approval status. Therefore the draft obligation is already covered by an original FR.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall identify which asset or user operation types can have a pending approval status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e9103c4532c9
- 主题：In Progress Operation Status
- 审查问题：Should the FR specify what causes an operation to enter the in progress state and whether that state is available for both asset and user operations?
- 场景：A user queries an operation that shows in progress; without transition rules, the meaning of in progress is ambiguous.
- 模型初步去向：retained
- 模型解释：FRBLOCK-013 establishes that asset and user operations can have an 'in progress' status, but it only supports querying that status and does not define what causes an operation to enter it. No checked original FR specifies the entry or transition condition for the In Progress state, so the draft identifies a missing in-scope lifecycle obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall define the entry condition for an operation to be in progress.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a4f24f32cb8c
- 主题：Approved Operation Status
- 审查问题：Does approved status require a documented approval action or rule, and should the FR state which roles can query or rely on it?
- 场景：A user queries approval status and sees approved; the FR does not state who approves or how approved is set.
- 模型初步去向：covered
- 模型解释：Original FRs already state equivalent approval actions/rules that set an operation/request to approved, e.g., FRBLOCK-021 stages for admin approval and updates status upon approval; FRBLOCK-022 states administrators review and approve or reject asset requests and the system updates the request status; FRBLOCK-019 stages permission changes for senior-admin approval and updates permissions upon approval. The nominated evidence FRBLOCK-013 only lists 'approved' as a queryable status, but other checked FRs cover the approval-action obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall define the approval action or rule that sets an operation to approved.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-adb9b108359a
- 主题：Rejected Operation Status
- 审查问题：Should the FR document why an operation may be rejected and whether rejected status is queryable for both asset and user operations?
- 场景：A user queries a rejected operation and needs to know the rejection scope or reason.
- 模型初步去向：retained
- 模型解释：The source establishes that asset and user operations can have a rejected status (FRBLOCK-013) and that asset requests are approved or rejected (FRBLOCK-021/022), but no original FR defines the conditions under which an operation is rejected. Defining those conditions is an in-scope validation/approval obligation not already stated.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall define the conditions under which an operation is rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e3ada15f48b2
- 主题：Administrator
- 审查问题：Is the isolated actor 'Administrator' the same role as the 'Administrators' who modify existing workflows in FR-14, and should the FR document that this actor supplies the workflow-edit form?
- 场景：An Administrator submits the Workflow-edit form with updated nodes, approvers, and conditions to modify an existing workflow.
- 模型初步去向：covered
- 模型解释：FR-14 already states that Administrators modify existing workflows and identifies the Workflow-edit form as the input for those modifications, so the draft obligation is equivalent to an existing FR.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The workflow-edit form should be available to the Administrator actor who performs workflow modifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-fb4d19aab360
- 主题：Senior Admin
- 审查问题：Is the isolated actor 'Senior Admin' the same role as the 'senior-admin' referenced in FR-14, and should FR-14 document that this actor performs the approval of staged workflow edits?
- 场景：After an Administrator modifies a workflow, the system stages the changes for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that staged workflow edits are submitted for senior-admin approval, which explicitly identifies the senior-admin actor as the approver for those staged workflow edits. The nominated obligation is therefore already covered by the original FR.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The senior-admin actor who approves staged workflow edits should be explicitly identified.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f37902da5a23
- 主题：User
- 审查问题：Does the User actor require a documented permission check before report creation?
- 场景：A user attempts to generate a report on management data without authorization.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence (FRBLOCK-015) states that users create reports on assets, users, or management data, but it does not state that the system must verify authorization or perform a permission check before report creation. None of the checked original FRs specify an equivalent permission-check obligation for report generation; related authorization or approval steps apply to other actions, not report creation. The draft therefore introduces a permission-check policy not supported by the source text.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system should verify the user's authorization before generating reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1622a28977c8
- 主题：Validate Format and Data
- 审查问题：Should validation of format and data be part of the export request validation described in FR-16?
- 场景：A user requests export in CSV or Excel, and the selected report contains data that may be invalid for the chosen format.
- 模型初步去向：unsupported
- 模型解释：FR-16 describes validating the export request and lists CSV/Excel as export format inputs, but it does not state that report data must be validated before preparing the file. The draft’s explicit obligation to validate both requested format and report data adds a data-validation policy not supported by the cited FR-16 evidence; general request validation is not equivalent to that specific combined validation.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall validate both the requested export format and the report data before preparing the file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6c6c597c46ef
- 主题：Admin
- 审查问题：Are Admin users included among the Users who can export existing reports?
- 场景：An Admin attempts to export an existing report.
- 模型初步去向：unresolved
- 模型解释：The only relevant original FR states that Users export existing reports, but it does not define whether Admin is a separate role excluded from Users or whether Admin users are included among report exporters. No original FR specifies Admin report-export permission or conditions, so the evidence is insufficient to determine whether the draft obligation is supported, already covered, or unsupported.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall define whether Admin users may export reports and under what conditions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-34923dc6563b
- 主题：User
- 审查问题：Does the 'User' actor need a documented connection to the FR-17 import workflow, such as which user role can upload asset data files?
- 场景：A user uploads a CSV/Excel file to import asset data; review whether the authorized role and permission are documented for this workflow.
- 模型初步去向：unsupported
- 模型解释：FR-17 only states that Users upload CSV/Excel files; it does not establish that specific User role(s), permission grants, or documentation of upload authorization are required. No other original FR supplies that obligation, so the draft adds an unsupported policy rather than restating a covered or retained requirement.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：Document which User role(s) are authorized to upload asset data files and how that permission is granted for FR-17.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a0386616efc8
- 主题：Validate Format and Data
- 审查问题：Is the 'Validate Format and Data' function sufficiently connected to defined validation rules and the error report output?
- 场景：During import, the system validates file format and data; invalid rows should be reported back to the user.
- 模型初步去向：retained
- 模型解释：FRBLOCK-017 is the in-scope validation/error-report function, but it only states that the system validates format and data and produces an error report. The screening confirms it does not define validation rules for uploaded CSV/Excel files or specify how validation failures are recorded in the error report. The nominated obligation is therefore a supported, in-scope refinement that is not already covered by the existing FR.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：Define validation rules for uploaded CSV/Excel files and specify how validation failures are recorded in the error report.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-edf318343ab2
- 主题：Parse Rows
- 审查问题：Does the 'Parse Rows' function have a documented connection to handling malformed or partially valid rows?
- 场景：The system parses rows from an uploaded CSV/Excel file and stores valid records while generating an error report.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already documents parsing rows and storing valid records with an error report, which covers the nominated obligation for malformed or partially valid rows and partial import handling.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：Specify row parsing behavior for malformed rows and clarify how partial imports are handled.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8fd3b0b29f60
- 主题：User
- 审查问题：What documented role or authorization level must a 'User' have to export selected asset data in FR-18, and does this align with the isolated 'User' element?
- 场景：A user attempts to export asset data but lacks a defined role; reviewer must confirm whether the FR permits any authenticated user or only specific roles.
- 模型初步去向：unsupported
- 模型解释：FR-18 only states that Users export selected asset data. It does not state that only authorized users may export, nor does it require documenting permitted roles or authorization conditions. The draft therefore introduces an authorization restriction not supported by the source evidence.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：Only authorized users may export asset data; the FR should document the permitted role(s) or authorization condition.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-56af8b264615
- 主题：Provide Download Link
- 审查问题：What is the documented trigger and active meaning for 'Provide Download Link' in FR-18, and how should its activation conflict be resolved?
- 场景：The system generates an export file and must decide when to expose the download link; the element currently has an activation conflict and no active meaning.
- 模型初步去向：unsupported
- 模型解释：FR-18 only states that the system generates an export file and provides a download link. It does not require the link to be provided only after successful generation, does not document an exact trigger, and does not resolve any activation conflict. The draft therefore introduces conditions and documentation requirements not supported by the original FR evidence.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must provide a download link only after the export file is successfully generated, with the exact trigger documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-491af8fdbe13
- 主题：Senior-admin
- 审查问题：What documented connection should relate the isolated Senior-admin element to the staged permission-approval workflow in FR-19?
- 场景：An administrator submits a permission update; the system validates and stages it, and senior-admin approval is required before permissions are updated.
- 模型初步去向：covered
- 模型解释：FR-19 already documents the Senior-admin approval role in the permission-update workflow: the request is validated, staged for senior-admin approval, and permissions are updated upon approval. This is equivalent to the nominated obligation, so no new supplement is needed.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：Document the Senior-admin approval role, including what must be reviewed before a staged permission update can be applied.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ebbea5ee7893
- 主题：Validate Request
- 审查问题：What documented connection should exist between the isolated Validate Request element and the permission form inputs in FR-19?
- 场景：An administrator submits a permission form containing user ID and permission level; the system validates the request before staging it for senior-admin approval.
- 模型初步去向：unsupported
- 模型解释：The evidence only states that the system validates the request and that the permission form is an input. It does not establish an obligation to document validation scope or an explicit relationship between the Validate Request element and permission form fields. The draft adds a documentation requirement not supported by FR-19.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：Document the validation scope and any documented relationship between Validate Request and the permission form fields.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1c338daa0efb
- 主题：Validate Request
- 审查问题：Does the isolated element 'Validate Request' correspond to the 'Validate replacement request' function in FR-20, or does it represent a separate validation operation that requires a documented connection to this workflow?
- 场景：FR-20 describes validation of a replacement request, while the graph contains an isolated 'Validate Request' element; determine whether they are the same operation or need explicit linking.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that the system validates the replacement request as part of the replacement workflow, so the isolated 'Validate Request' element is equivalent to the existing 'Validate replacement request' obligation and does not require a new or separate documented obligation.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system should validate replacement requests using the applicable validation operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2d882721a3d3
- 主题：Senior Admin
- 审查问题：Is the isolated element 'Senior Admin' a distinct actor from the 'Senior administrators' actor in FR-20, and if so, what connection or role mapping should be documented?
- 场景：FR-20 names 'Senior administrators' as the actor who performs replacement, while the graph contains an isolated 'Senior Admin' element; review whether they are the same actor or require a documented relationship.
- 模型初步去向：covered
- 模型解释：FR-20 already states that 'Senior administrators replace the current system admin,' which is equivalent to authorizing them to initiate the replacement. The draft obligation adds no distinct business obligation beyond what FRBLOCK-020 already specifies.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：Senior administrators are authorized to initiate the replacement of the current system admin.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-70d8c1e78f80
- 主题：Admin
- 审查问题：Should the 'Admin' element be explicitly documented as the approving actor in the asset-request workflow?
- 场景：A reviewer sees that FR-21 stages a request for 'admin approval' but the isolated element 'Admin' is not named as the role responsible for the decision. They need to decide whether to document that role connection.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that asset requests are staged for admin approval, which documents the Admin role as the approving actor in the asset-request workflow. Other original FRs also explicitly cover this obligation, such as FRBLOCK-022, which states that Administrators review and approve or reject asset requests.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Document that asset requests are staged for approval by an Admin role.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e2f6b0c7c3fb
- 主题：Approved
- 审查问题：Should the 'Approved' state be explicitly linked to the stored asset request in FR-21?
- 场景：The FR output says a stored request has status 'Approved', and the isolated element 'Approved' exists separately. A reviewer needs to know whether to document the state-to-request linkage.
- 模型初步去向：covered
- 模型解释：FR-21 already states that a stored asset request has status “Approved” or “Rejected,” which explicitly links the Approved state to the stored request; FR-22 also requires updating the request status upon approval. The draft obligation is therefore already covered by the original functional requirements.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Document that an approved asset request is stored with the Approved status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3e8a39ec0a22
- 主题：Rejected
- 审查问题：Should the 'Rejected' state be explicitly linked to the stored asset request in FR-21?
- 场景：The FR output says a stored request has status 'Rejected', and the isolated element 'Rejected' exists separately. A reviewer needs to know whether to document the state-to-request linkage.
- 模型初步去向：covered
- 模型解释：FR-21 already states that the output is a stored request with status “Approved” or “Rejected,” which covers the draft obligation that a rejected asset request is stored with the Rejected status.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Document that a rejected asset request is stored with the Rejected status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-32fea840faa7
- 主题：User
- 审查问题：Should the 'User' element be documented as the actor who submits the asset request in FR-21?
- 场景：The FR says 'Users request assets', but the isolated element 'User' is not explicitly named as the submitting actor. A reviewer needs to decide whether to document that actor connection.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that Users request assets, which is equivalent to documenting that a User submits the asset request form. The nominated obligation is therefore already present in the checked original FRs.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Document that a User submits the asset request form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0ba7c4b2ad70
- 主题：Validate Request
- 审查问题：Should the isolated 'Validate Request' element be documented as the validation function invoked when an asset request is submitted?
- 场景：The FR says the system 'validates the request' but does not name 'Validate Request'. A reviewer needs to decide whether to document this function connection.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that the system validates the request and stages it for admin approval, so the draft obligation that asset request submission invokes validation before staging is already covered. Naming the internal function 'Validate Request' does not add a new business obligation.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Document that asset request submission invokes Validate Request before staging for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-67108fa4ecd4
- 主题：Approved
- 审查问题：Should the 'Approved' status be documented as the resulting status when an administrator approves an asset request?
- 场景：An administrator approves an asset request; the system updates the request status. The status value 'Approved' must be set.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies that an asset request is staged for admin approval and that the stored request has status “Approved” or “Rejected,” which covers the proposed obligation to set the status to “Approved” when an administrator approves an asset request.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall set the request status to 'Approved' when an administrator approves an asset request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-911872c414fc
- 主题：Rejected
- 审查问题：Should the 'Rejected' status be documented as the resulting status when an administrator rejects an asset request?
- 场景：An administrator rejects an asset request; the system updates the request status. The status value 'Rejected' must be set.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already documents that a stored request can have the status “Approved” or “Rejected,” and FRBLOCK-022 states administrators review and approve or reject asset requests. Together these cover the nominated obligation that a rejected asset request results in the “Rejected” status.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall set the request status to 'Rejected' when an administrator rejects an asset request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9ec0bc10d57e
- 主题：User
- 审查问题：Is the 'User' element the recipient of the user notification, and does it refer to the requestor?
- 场景：An administrator approves an asset request; the system notifies users. The notification should go to the requestor.
- 模型初步去向：retained
- 模型解释：The original FR-22 only states that the system notifies users after an asset request decision, without specifying that the recipient is the requestor. The nomination scenario explicitly requires the notification to go to the requestor, so the draft obligation is a supported, in-scope refinement not covered by any original FR.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall notify the requestor (User) when an asset request decision is made.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2e022473533a
- 主题：Send Activation Email
- 审查问题：Is 'Send Activation Email' a separate requirement from FR-23, or is it an example of a registration-triggered notification within FR-23?
- 场景：A user registers, and the system may need to send an activation email.
- 模型初步去向：covered
- 模型解释：FR-23 already obligates the system to send email notifications for events such as registration; an activation email is a registration-triggered notification. FR-07 also explicitly mentions sending an activation email for admin-created users, so the draft does not introduce a separate or unsupported obligation.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Clarify whether activation emails are covered by FR-23 or another requirement.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5c7e2cede559
- 主题：Validate Request
- 审查问题：Should FR-23 include a validation step for event details and recipient list before sending notifications?
- 场景：An event details input contains malformed data or invalid recipient addresses.
- 模型初步去向：retained
- 模型解释：FR-23 defines event details and recipient list as notification inputs but does not specify validation of those inputs, and no other original FR covers this notification-input validation obligation. The requirement is in scope for FR-23 and is not already stated.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Define validation requirements for email notification inputs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-872365a48ac4
- 主题：User
- 审查问题：Should the graph-isolated actor 'User' have a documented connection to FR-24's feedback submission flow, or is the existing 'User feedback email' input sufficient to establish that connection?
- 场景：A user sends an email to provide feedback. FR-24 states the system receives user email feedback but does not explicitly tie this input to the graph-isolated 'User' element.
- 模型初步去向：covered
- 模型解释：FR-24 already specifies 'User feedback email' as the input, which is equivalent to accepting feedback emails from users as the initiating input for the feedback handling workflow. The existing FR therefore covers the draft obligation.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must accept feedback emails from users as the initiating input for the feedback handling workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-df354a020ab0
- 主题：Admin
- 审查问题：Should the graph-isolated element 'Admin' have a documented connection to the output 'admin notification' in FR-24, or is it a duplicate/alias of the 'Administrators' actor?
- 场景：After feedback is stored, FR-24 requires an admin notification. The isolated 'Admin' element may need clarification as the recipient role for that notification.
- 模型初步去向：covered
- 模型解释：FR-24 already states that the system notifies administrators for handling, which is equivalent to directing feedback notifications to the administrator role for handling. The nominated draft obligation is therefore already covered by an original FR.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must direct feedback notifications to the administrator role for handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f936d48eb19f
- 主题：Asset change
- 审查问题：How is the Asset change event connected to the View Asset Change History function, and what ensures each asset change is recorded with time, operation, user, and before/after values?
- 场景：An asset is modified; a change log entry should be available later for query through View Asset Change History.
- 模型初步去向：covered
- 模型解释：FRBLOCK-025 already requires asset change logs to be queryable and includes change history output with time, operation, user, and before/after values, which is equivalent to the drafted obligation.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should record each asset change event with time, operation, user, and before/after values so it can be retrieved via View Asset Change History.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-966b14fa047d
- 主题：Admin
- 审查问题：Should the change history user field identify the acting user or role (e.g., Admin) for each asset change operation?
- 场景：An Admin changes an asset; the change history should show which user or role made the change.
- 模型初步去向：covered
- 模型解释：FR-025 already specifies that the change history output includes the user field, which covers the obligation to include the user who performed each asset change operation.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The change history should include the user who performed the operation for each asset change.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8f17339ab982
- 主题：Approved
- 审查问题：Should approval status changes (e.g., Approved) be captured as a change type that can be queried in asset change history?
- 场景：An asset's operation status changes to Approved; a user queries change history by change type.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-025 already supports filtering asset change history by change type, but neither it nor any other screened original FR requires approval-related status changes to be captured or included as a filterable change type. The draft adds an approval-specific requirement not supported by the source requirements.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should allow filtering asset change history by change type, including approval-related status changes when applicable.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-26e934f42fb0
- 主题：Asset Count
- 审查问题：How is Asset Count produced and included when a user views an asset category?
- 场景：A user searches for a category by name or ID and the result shows an asset count; the reviewer needs to know the count's source or definition.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already specifies that category details output for the View Asset Category feature includes 'asset count'. This is an equivalent obligation to documenting Asset Count as an output of the feature, so no new supplement is needed.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The View Asset Category feature should document Asset Count as a derived output representing the number of assets associated with the retrieved category.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6deda0548adc
- 主题：User
- 审查问题：How should the User actor be documented in relation to the Query Asset Category operation?
- 场景：A user performs a search for an asset category by name or ID and views the resulting category details.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already states that Users query asset categories by name or ID, which documents the User actor as the initiator of the Query Asset Category operation. The draft obligation is therefore equivalent to the existing original FR.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The View Asset Category feature should document the User actor as the initiator of the Query Asset Category operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-fd0f340f94bd
- 主题：Administrator
- 审查问题：Should the isolated element Administrator have a documented connection to the Edit Asset Category workflow, or does the FR text's mention of Administrators already establish the authorized actor?
- 场景：An administrator opens the category-edit form and submits changes; a reviewer needs to confirm whether that actor-role link is sufficiently documented.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 already states that Administrators modify category information, which is equivalent to authorizing an Administrator to initiate edits to existing asset categories. The original FR therefore establishes the authorized actor for this workflow; no new obligation is needed.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must authorize an Administrator to initiate edits to existing asset categories.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-11e12d4a820b
- 主题：Admin
- 审查问题：Is the isolated term Admin intended as a synonym for Administrator in FR-27, and should the FR use a single role name?
- 场景：A reviewer sees both Admin and Administrator in the model and cannot tell whether they refer to the same role for category editing.
- 模型初步去向：unsupported
- 模型解释：FR-27 only states that Administrators modify category information; it does not define 'Admin' as a synonym or require documentation to use a consistent role name. No checked original FR imposes such a naming-consistency obligation, so the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system documentation must use a consistent name for the actor authorized to edit asset categories.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a1679bb4f05e
- 主题：Senior Admin
- 审查问题：Does the isolated actor Senior Admin need a documented connection to the senior-admin approval step, or is the approval phrase in FR-27 sufficient?
- 场景：A senior admin receives a staged category edit for approval and a reviewer checks whether the approving role is explicitly linked to this FR.
- 模型初步去向：covered
- 模型解释：The draft obligation is equivalent to the obligation already stated in original FR-27, which provides that administrators modify category information and the system stages the changes for senior-admin approval and updates the category only upon approval. The checked original FRs therefore already state the routing of staged category modifications to a Senior Admin for approval before applying them, so no new business obligation is introduced.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must route staged category modifications to a Senior Admin for approval before applying them.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-928137178aed
- 主题：Senior-admin
- 审查问题：Does the isolated term Senior-admin need a documented connection to the approval workflow, or is it just an adjective in senior-admin approval?
- 场景：A reviewer sees senior-admin approval in FR-27 but no separate Senior-admin actor element linked to the workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 explicitly states that category changes are staged for senior-admin approval and the category is updated upon approval, which is equivalent to the draft obligation requiring senior-admin approval before applying staged category changes.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must require senior-admin approval before applying staged category changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e35ce530cb8c
- 主题：Approved
- 审查问题：Does the isolated state Approved need to be connected to the post-approval update in FR-27, or is upon approval enough to define the trigger?
- 场景：A senior admin approves a staged category edit; a reviewer checks whether the Approved state is explicitly tied to the update operation.
- 模型初步去向：covered
- 模型解释：FR-27 already states that category edits are staged for senior-admin approval and the category is updated upon approval. That is equivalent to the draft obligation requiring staged category updates to be applied only after approval.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must apply staged category updates only after the changes reach an approved state.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：76 条提名

### OPERATION-b807960581b0
- 主题：Validate Format and Data
- 审查问题：Should 'Validate Format and Data' be treated as an applicable operation in this FR because the system validates submitted data for completeness and accuracy?
- 场景：FR-01 describes validation of data for completeness and accuracy before storing the asset; 'Validate Format and Data' is an isolated operation-like element.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already requires the system to validate asset data for completeness and accuracy before storing the record, which is equivalent to the nominated validation obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：Asset registration shall perform validation of submitted asset data for completeness and accuracy before storing the record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-98825bf8189d
- 主题：Validate Request
- 审查问题：Is 'Validate Request' the operation that performs the completeness and accuracy check described in FR-01, or is it a separate validation step?
- 场景：FR-01 states the system validates the data, and 'Validate Request' is an isolated operation that may correspond to that check.
- 模型初步去向：unsupported
- 模型解释：FR-01 requires the system to validate registration data for completeness and accuracy before storing the asset, but it does not name a 'Validate Request' operation, define such an operation, or require the workflow to identify whether that operation is required before asset data is stored. The other original FRs likewise do not establish this obligation. The draft therefore introduces a process-identification requirement not supported by the source evidence.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The registration workflow shall identify whether a Validate Request operation is required before asset data is stored.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2ea44500eb25
- 主题：Register Asset
- 审查问题：Does the 'Register Asset' operation include validation, storage, status setting, and administrator notification, or are these separate operations in the workflow?
- 场景：FR-01 is titled Register Asset and describes validation, storage, status setting, and notification in one paragraph.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already describes the Register Asset process as encompassing validation, storage, status assignment to “Registered,” and administrator notification for review, matching the draft obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The Register Asset operation shall encompass validation, storage, status assignment, and administrator notification as documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ea6286e46001
- 主题：Admin approval
- 审查问题：Is there a documented approval operation that allows an Admin to approve a staged asset modification?
- 场景：A user submits a modification; the system stages it for admin approval. The FR mentions upon approval but does not specify the approval action.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already documents that an asset modification change is staged for admin approval and that the status is updated upon approval, which is equivalent to providing an Admin approval operation for a staged asset modification.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall provide an approval operation for Admin to approve a staged asset modification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ff6b3834715d
- 主题：Validate modification data
- 审查问题：Should the validation operation check both format and data correctness before staging the modification?
- 场景：A user submits a modification form with invalid type, quantity, or purchase date. The FR says the system validates the data but does not define validation rules.
- 模型初步去向：unsupported
- 模型解释：The cited FR only states that the system generically 'validates the data' before staging a change. It does not define validation rules or require checking both format and data correctness for modification form fields. No original FR establishes that specific obligation, so the draft introduces an unsupported policy refinement.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall validate modification form fields for format and data correctness before staging the change.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0ed356b48243
- 主题：Search Criteria
- 审查问题：Should asset search by name, type, or ID use exact matching, partial matching, or both, and can multiple criteria be combined in a single query?
- 场景：A user enters a partial asset name and selects a type in the query form; the system must decide whether to return only exact matches or also partial matches, and how to combine both criteria.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 establishes asset search by name, type, or ID but leaves matching semantics and combinability undefined. No original FR covers these rules, and the obligation is in-scope for asset search.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Define the matching semantics and combinability rules for asset search criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2d97fdd0a6fa
- 主题：Detailed Asset Information
- 审查问题：Which fields must be returned for detailed asset information, and what does 'etc.' include or exclude?
- 场景：A user opens the results for a matching asset and expects name, type, quantity, purchase date, and status; the response must be complete and consistent across all asset types.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 is the only original FR addressing detailed asset information, and while it lists name, type, quantity, purchase date, status, etc., the 'etc.' leaves the output schema incomplete and no original FR defines the complete field set or clarifies what 'etc.' includes or excludes. The nomination is therefore an in-scope, supported clarification of an existing obligation rather than a duplicate or unsupported policy.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Specify the complete output schema for detailed asset information.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c843a38b171b
- 主题：Query Asset Details
- 审查问题：How should the system respond when no asset matches the search criteria?
- 场景：A user searches for an asset ID that does not exist; the system should clearly indicate zero matches rather than returning an empty or ambiguous success response.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 establishes the in-scope asset query operation and states that matching records are returned, but no checked FR specifies the empty-result case or the user feedback required when no asset matches the search criteria.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：Define the empty-result behavior and user feedback for the asset query operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-adfb4fa116e9
- 主题：Stage for Admin Approval
- 审查问题：Does the 'Stage for Admin Approval' operation require a corresponding admin decision operation (approve/reject) to complete the workflow?
- 场景：A transfer request is validated and staged. The FR states ownership updates upon approval, but the approval operation itself is not explicitly documented.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already requires administrators to review and approve or reject asset requests and update request status, and FRBLOCK-021 already stages requests for admin approval with statuses Approved or Rejected. These original FRs state an equivalent admin approval/rejection decision obligation, so the draft does not add a new business requirement.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：Define the admin approval/rejection operation that transitions a staged transfer request to approved or rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-68d62426114c
- 主题：Validate Transfer Request
- 审查问题：What validation rules apply during 'Validate Transfer Request'?
- 场景：A user submits a transfer form. The system validates the request, but the FR does not list validation criteria such as asset existence or recipient validity.
- 模型初步去向：unsupported
- 模型解释：The original FRs only state that the system validates the transfer request (FRBLOCK-004) without specifying any validation rules or criteria. The draft introduces specific validation rules such as asset ID existence and recipient validity, which are not supported by the source text.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：Specify validation rules for transfer requests (e.g., asset ID exists, recipient is valid).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4195d119d49c
- 主题：Validate Return Request
- 审查问题：Does the documented return workflow require a distinct validation operation for the return request, or is validation embedded in submission?
- 场景：A user submits a Return form with asset ID and return date; the system must validate the request before staging it for approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already states that the system validates the return request and stages it for approval, and the screening identifies the return form input as including asset ID and return date, making it equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system must validate the asset ID and return date of a return request before staging it for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-83347e845ab7
- 主题：Stage Return Request for Approval
- 审查问题：What approval operation is applicable after a return request is staged, and who is authorized to perform it?
- 场景：A validated return request is staged for approval; an approver reviews and approves it, triggering the asset status update to Returned.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that users initiate approval processes for return requests, the system validates and stages the request for admin review, and executes the operation upon approval. This provides an equivalent obligation to the nominated draft and identifies admin review/approval as the authorized approval operation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system must support an approval operation for staged asset return requests before updating asset status to Returned.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d5ba3481d03e
- 主题：Validates the Request
- 审查问题：What validation rules and failure outcomes apply when the system validates a deletion request?
- 场景：A deletion request for an asset ID is submitted.
- 模型初步去向：retained
- 模型解释：The original FR confirms that deletion requests are validated before staging, but it does not define the validation rules or the failure handling. The nomination's obligation to define these missing details is supported by the in-scope validation operation and is not covered by an equivalent original FR.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must define validation rules and failure handling for deletion requests before they are staged.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-708054f5e4c9
- 主题：Staged for Admin Approval
- 审查问题：What operation transitions a validated deletion request into the staged-for-admin-approval state?
- 场景：A valid deletion request is waiting for an admin decision.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that, after validation, the system stages the deletion request for admin approval and deletes the record upon approval. This is equivalent to defining the staging operation and pending approval state for validated deletion requests.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must define the staging operation and pending approval state for validated deletion requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d36187c6c802
- 主题：Deletes the Record upon Approval
- 审查问题：What operation is triggered after admin approval, and does it hard-delete or mark the asset record as deleted?
- 场景：An admin approves a staged deletion request.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that the asset deletion request is staged for admin approval and the system deletes the record upon approval, defining the approved deletion operation and its effect on the asset record.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must define the approved deletion operation and its effect on the asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9a439ea4fd4a
- 主题：Deleted
- 审查问题：What does the 'Deleted' status mean for the removed asset record, and which operation sets it?
- 场景：A deletion request is approved and the asset record is removed.
- 模型初步去向：retained
- 模型解释：The screening notes identify FRBLOCK-006 as the only in-scope source for the Deleted status, but it only states that a removed asset record receives the status 'Deleted' after deletion upon approval. No checked original FR defines the business meaning or lifecycle of that status, so the draft obligation is a supported in-scope gap rather than a duplicate or unsupported policy.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The solution must define the business meaning and lifecycle of the 'Deleted' status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6dad9e4442d3
- 主题：Create New User Accounts
- 审查问题：Does the create operation need a documented update or deactivation operation to manage user lifecycle after activation?
- 场景：The FR creates a new user and sends an activation email, but it does not describe how to update or deactivate an existing user account.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already documents an update operation for user profiles, and FRBLOCK-020 documents updating admin records. Because the draft obligation only says the system may need an update or deactivation operation and does not make deactivation mandatory, the update obligation is already covered by existing FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system may need a documented operation to update or deactivate user accounts, but this is not mandatory.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0248a93d5d86
- 主题：Validate New-User Form
- 审查问题：Should the validation operation specify which fields are mandatory and what format rules apply to the new-user form?
- 场景：The new-user form includes username, password, email, phone, and department, and the FR says the form is validated, but it does not list validation rules.
- 模型初步去向：retained
- 模型解释：FRBLOCK-007 is the only in-scope FR for the new-user form, and it states only that the system validates the form. It does not specify which fields are mandatory or what format rules apply, and the screening confirms this specific validation obligation is not already covered.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system may need to document required-field and format validation rules for the new-user form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-341281d8626e
- 主题：Edit User Profile
- 审查问题：Does the Edit User Profile operation require an authorization rule that the authenticated user may edit only their own profile?
- 场景：A user submits the profile-edit form; FR-08 states users edit their own profiles but does not specify a system-enforced ownership check.
- 模型初步去向：covered
- 模型解释：FR-08 already states that users edit their own profiles, which is equivalent to requiring that profile-edit authorization be limited to the authenticated user's own profile.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must authorize profile-edit requests only for the authenticated user's own profile.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8f9b6d7a98f0
- 主题：Validate changes
- 审查问题：Which validation rules must be applied to the profile-edit form fields, and what is the required system response when validation fails?
- 场景：A user submits name, username, email, and phone; the system validates changes before staging them for admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already requires the system to validate profile-edit changes for the fields name, username, email, and phone and to stage them for admin approval before updating the record, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must validate name, username, email, and phone before staging profile changes for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fc9d11336064
- 主题：Stage for Admin Approval
- 审查问题：What pending state and admin-approval path must be documented for staged profile changes?
- 场景：After validation, the system stages profile changes for admin approval; FR-08 does not define the staged state or approval decision.
- 模型初步去向：covered
- 模型解释：FR-08 already states that validated changes are staged for admin approval and only updated upon approval, which is equivalent to holding validated profile changes in a pending-approval state until an Admin approves them.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must hold validated profile changes in a pending-approval state until an Admin approves them.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c0abc85e62f9
- 主题：Update record upon approval
- 审查问题：When an admin approves staged changes, what record fields must be updated and what status transition must occur?
- 场景：Upon approval, the system updates the user record and outputs status 'Modified'; FR-08 does not specify whether all submitted fields are applied or whether approval metadata is stored.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already specifies that after admin approval the system updates the user record, with output status “Modified.” This is equivalent to applying approved staged profile changes to the user record and setting status to “Modified.”
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must apply the approved staged profile changes to the user record and set the record status to 'Modified'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-221783513b36
- 主题：Query User Details
- 审查问题：What result should the Query User Details operation return when the search criteria match zero users or more than one user?
- 场景：A user searches by department, and either no user has that department or several users share it; the system must decide whether to return an empty result, a single record, or a list.
- 模型初步去向：retained
- 模型解释：FRBLOCK-009 establishes the Query User Details operation and its search criteria, but no original FR specifies the return cardinality for zero, one, or multiple matching users. The draft obligation identifies an in-scope missing business rule.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation should define its return behavior for zero, one, and multiple matching users.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8b23751e0fd5
- 主题：Search Criteria
- 审查问题：Are username, email, and department all optional, or are certain combinations required to execute a user-details query?
- 场景：A user provides only a department as search criteria; the system must determine whether that is sufficient to perform the query.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-009 is the relevant in-scope FR and lists username, email, and department as search criteria, but it does not state whether each criterion is optional or whether any combination is mandatory. The draft's requirement to document mandatory combinations cannot be verified from the available evidence, so the decision is unresolved.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The system should accept username, email, and/or department as search criteria and document any mandatory combination.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-24e3fbca4beb
- 主题：Detailed User Information
- 审查问题：Which fields in Detailed User Information are mandatory in the query output, and are sensitive fields such as phone and permission level restricted by the requester's permission level?
- 场景：A user searches by email and receives detailed user information; the system must decide whether phone and permission level are always returned or only to authorized users.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only lists detailed user information output fields (name, username, email, phone, department, permission level). It does not state which fields are mandatory or impose any requester-authorization restriction on sensitive fields such as phone or permission level. No other original FR supplies that obligation, so the draft introduces an unsupported authorization policy.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The query should return the specified detailed user information fields, with sensitive fields subject to the requester's authorization.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-32a2091203d4
- 主题：Validate deletion request
- 审查问题：What validation rules and failure outcomes must apply when the system validates a user deletion request before staging it for approval?
- 场景：An administrator submits a deletion request with user ID; the system validates the request, but the FR does not state what makes the request invalid or what happens on validation failure.
- 模型初步去向：unsupported
- 模型解释：The source FRs only state that the system validates a user deletion request before staging it for approval. They do not specify validation criteria, invalid conditions, or rejection/failure outcomes. The draft introduces a requirement to define rejection behavior and validation criteria that is not supported by the source text.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Specify validation criteria and rejection behavior for user deletion requests before they are staged for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b9d92b5b9e9c
- 主题：Stage deletion request for senior-admin approval
- 审查问题：Does staging a deletion request require creating a pending approval item, and what status should the request have while awaiting senior-admin approval?
- 场景：An administrator submits a valid deletion request; the system stages it for senior-admin approval, but the FR does not define the staged state or how long it remains pending.
- 模型初步去向：retained
- 模型解释：FRBLOCK-010 supports staging user deletion requests for senior-admin approval, but it does not define a pending-approval item or the request status while awaiting approval. The nomination is an in-scope refinement of that staging obligation, and no checked original FR covers the missing pending-state behavior.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Define the pending-approval state and staging behavior for user deletion requests awaiting senior-admin action.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cb8d7532ff04
- 主题：Delete user record upon approval
- 审查问题：What deletion semantics are required after approval: hard delete, soft delete, or status change to 'Deleted'?
- 场景：The FR output says a removed user record with status 'Deleted', which may imply both removal and status retention; the delete operation needs clear post-approval behavior.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-010 indicates approved deletion of a user record and a 'Deleted' status, but the evidence does not establish whether this means hard delete, soft delete, or both, nor does it define retention. The draft is a clarification request rather than a supported concrete obligation, and the source is too ambiguous to decide the required semantics.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：Clarify whether approved deletion removes the user record, marks it Deleted, or both, and define resulting data retention.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-56bc2510007a
- 主题：Stage Setup for Approval
- 审查问题：What specific operation does the system perform when staging the setup for approval—does it create a pending approval record, update the workflow status to pending, or generate a notification for the Senior Admin?
- 场景：An administrator submits a workflow configuration that passes validation, and the system stages it for senior-admin approval.
- 模型初步去向：unsupported
- 模型解释：The cited evidence, FRBLOCK-011, only states that the system 'stages the setup for senior-admin approval.' It does not specify creating a pending approval record or setting the workflow configuration to a pending state. Those are added implementation details not supported by the source FR.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must create a pending approval record and set the workflow configuration to a pending state when staging for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3708a8a4d2ac
- 主题：Activate Workflow
- 审查问题：Upon senior-admin approval, what operation activates the workflow—is it updating the workflow status to active, enabling it for use, or publishing the configuration?
- 场景：Senior Admin approves a staged workflow configuration, and the system activates the workflow.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence, FRBLOCK-011, states that the workflow is activated upon approval. It does not specify that activation means updating the workflow status to active or enabling the workflow for use. The draft obligation adds specific activation mechanisms not supported by the cited evidence.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must update the workflow status to active and enable the workflow for use upon senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d1e4bd1519a0
- 主题：Validate Configuration Details
- 审查问题：What validation operation is performed on the configuration details—e.g., checking node order, approvers, and conditions—and what happens if validation fails?
- 场景：An administrator submits a workflow configuration form, and the system validates the configuration details before staging it for approval.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-011 only states that the system validates configuration details. It does not specify that invalid configurations are rejected or that staging is blocked on validation failure. The draft adds a failure-handling obligation that is not supported by the cited evidence or any other original FR.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system must validate the workflow configuration details and reject invalid configurations before staging for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d28b19313156
- 主题：Validate approval-start request
- 审查问题：What validation criteria and failure handling must the system apply when validating an approval-start request?
- 场景：A user submits an approval-start request with an asset ID and operation type; the FR says the system validates the request but does not define the validation rules or what happens if validation fails.
- 模型初步去向：unsupported
- 模型解释：The cited FRBLOCK-012 only states that the system validates the request and stages it for admin review. It does not establish the specific approval-start validation criteria in the draft, such as required asset ID, operation type, or user authorization, nor does it define failure handling. The draft therefore introduces an unsupported policy rather than restating an existing obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall validate the approval-start request against required asset ID, operation type, and user authorization before staging it for admin review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b5b29818d27f
- 主题：Request staged for admin review
- 审查问题：How is a validated approval-start request staged for admin review, and what information must be available to the reviewer?
- 场景：A user starts an approval process; the system validates the request and stages it for admin review, but the FR does not specify the staging state or reviewer-visible details.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-012 already covers validating and staging an approval-start request for admin review and lists asset ID and operation type as inputs, but the draft additionally requires requester information to be available to the reviewer. That requirement is not supported by the cited source or any original FR screening.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall stage validated approval-start requests for admin review and make the asset ID, operation type, and requester information available to the reviewer.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-93b036c2ad5b
- 主题：Operation executed upon approval
- 审查问题：What events or status changes trigger execution of the requested operation after approval, and how are execution failures handled?
- 场景：An administrator approves a staged request; the FR says the system executes the operation upon approval but does not define the execution trigger, failure handling, or whether rejection or cancellation prevents execution.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-012 states that the operation is executed upon approval, but the draft adds a prohibition on execution upon rejection or cancellation that is not supported by the cited evidence or any original FR. No original FR defines cancellation behavior or an equivalent non-execution obligation, so the added policy is unsupported.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall execute the approved registration, usage, transfer, or return operation upon approval and shall not execute it upon rejection or cancellation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2b96ddcf61b1
- 主题：Approval-process record
- 审查问题：What fields and lifecycle states must the approval-process record contain?
- 场景：A user initiates an approval process; the output includes an approval-process record, but the FR does not specify its contents, status values, or retention rules.
- 模型初步去向：unsupported
- 模型解释：The evidence only establishes that an approval-process record is an output for an approval-start operation (FRBLOCK-012). No checked original FR specifies the required fields in the draft obligation (asset ID, operation type, requester, current status, review outcome) or its lifecycle states. Therefore, the draft introduces unsupported record-field policy rather than restating an existing obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall create an approval-process record for each approval-start request containing the asset ID, operation type, requester, current status, and review outcome.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a52fa15b6dfc
- 主题：Updated operation status
- 审查问题：Which operation statuses must be supported and how do they transition as an approval process progresses?
- 场景：The approval process output includes updated operation status, but the FR does not define the possible statuses or transitions from pending review to approval, rejection, or completion.
- 模型初步去向：retained
- 模型解释：The original FRs include approval workflows and mention operation statuses in places, such as FRBLOCK-013 listing pending, in progress, approved, and rejected statuses, and FRBLOCK-021/022 updating request status on approval or rejection. However, no original FR defines the full operation-status lifecycle or the transitions from pending review to approval, rejection, or completion. The nominated obligation is in-scope and supported by the approval-process context, but it is not already stated as an equivalent requirement.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall update the operation status to reflect pending review, approval, rejection, or completion of the requested operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bc3c4ea6b068
- 主题：Query Approval Status
- 审查问题：Should the Query Approval Status operation support filtering by operation type in addition to asset ID and user ID, so users can retrieve only asset or user operation statuses?
- 场景：A user enters search criteria with operation type to narrow results, but the FR lists operation type as an input without stating whether it is a required or optional filter.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already specifies that Query Approval Status search criteria include asset ID, operation type, and user ID, which is equivalent to allowing filtering approval status queries by those fields.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system shall allow users to filter approval status queries by asset ID, operation type, and user ID.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6f552f59b619
- 主题：Validate changes
- 审查问题：Should the 'Validate changes' operation define what validation failures prevent staging, and how those failures are reported before the workflow is sent for senior-admin approval?
- 场景：An Administrator submits an edited workflow; the system validates the updated nodes, approvers, and conditions before staging them for approval.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-014 establishes that the system validates changes and stages them for senior-admin approval, but it does not specify that invalid workflow modifications must be prevented from staging or that validation failures must be documented. The draft adds these policy details without source support.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：Invalid workflow modifications should not be staged for senior-admin approval, and validation failure should be documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bc681d787c40
- 主题：Stage for senior-admin approval
- 审查问题：Does staging create a persistent pending-approval record for the modified workflow, or is it only a transient step before the senior-admin acts?
- 场景：The system stages an Administrator's validated workflow changes for senior-admin approval.
- 模型初步去向：unsupported
- 模型解释：The documented evidence only shows that workflow changes are 'staged for senior-admin approval.' The screening for FRBLOCK-014 specifically notes that the original FR does not require a persistent pending-approval record or retention until approval/rejection, and no other original FR covers modified workflow staging. The draft therefore adds an unsupported persistence/pending-status policy.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：Staged workflow edits should be retained with a pending-approval status until senior-admin approval or rejection.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-99ef3818d8be
- 主题：Update workflow upon approval
- 审查问题：Is the workflow update operation triggered exclusively by senior-admin approval, and how should staged changes be handled if approval is not granted?
- 场景：A senior-admin approves the staged workflow changes, and the system updates the existing workflow.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-014 already covers the approval-gated workflow update (workflow changes are staged for senior-admin approval and updated upon approval), but no checked original FR supports a separate obligation to define or specify non-approval handling for staged workflow changes. The draft therefore adds a requirement beyond the evidence.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system should apply staged workflow changes only after senior-admin approval and define non-approval handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cbfa2784d062
- 主题：Generate Report
- 审查问题：Does the Generate Report operation need a documented step for delivering the generated file to the user?
- 场景：A user generates an Excel report and expects to receive or access the file.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already documents delivery of the generated report to the user by specifying that the system validates the request, prepares the file, and provides a download link. This is an equivalent obligation to delivering the generated report file to the requesting user, so the draft is covered by an original FR.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system should deliver the generated report file to the requesting user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8de292cc0fc2
- 主题：Validate Parameters
- 审查问题：Does the Validate Parameters operation need a documented failure response?
- 场景：A user submits an invalid date range for a report.
- 模型初步去向：retained
- 模型解释：FRBLOCK-015 establishes that report parameters are validated, but it does not document the required failure response for invalid report parameters. No checked original FR specifies that invalid report parameters must be rejected with a clear error, so this is an in-scope missing business obligation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system should reject invalid report parameters with a clear error.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a11d4f07827f
- 主题：Store Report Data
- 审查问题：Does the Store Report Data operation need a documented retrieval or retention rule?
- 场景：A user needs to access a previously generated report.
- 模型初步去向：covered
- 模型解释：FRBLOCK-015 already states that the system stores the data and lists stored report data as an output, covering the obligation to retain stored report data for later retrieval.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system should retain stored report data for later retrieval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5667d580877a
- 主题：Export Report
- 审查问题：Does the export operation apply only to existing reports, or can users also export reports in draft or otherwise unavailable states?
- 场景：A user selects a report and chooses CSV or Excel to export it.
- 模型初步去向：unsupported
- 模型解释：The evidence FRBLOCK-016 only states 'Users export existing reports', which supports limiting export to existing reports but does not support the additional condition that reports must be available to the user. No other original FR addresses report export availability. Therefore the draft obligation introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall limit report export to reports that exist and are available to the user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7d40820a4dfe
- 主题：Validate Request
- 审查问题：What validation rules must the export request satisfy before the system prepares the file?
- 场景：A user submits an export request for a selected report and requested format.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that the system validates the request before preparing the file, and identifies the request inputs as the selected report and export format. This is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall validate the selected report and requested export format before preparing the export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f85309d51fe8
- 主题：Prepare File
- 审查问题：What format-specific preparation is required for CSV versus Excel exports?
- 场景：A user chooses CSV for one export and Excel for another.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that the system prepares the file and accepts the selected export format (CSV, Excel) as input, which is equivalent to the nominated obligation to prepare the export file according to the selected format.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall prepare the export file according to the selected export format.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d37190e3c728
- 主题：Provide Download Link
- 审查问题：What access, expiration, and reuse rules apply to the download link?
- 场景：A user receives a download link and may share or reopen it later.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-016 only supports that a download link is provided; it does not support a 'secure' download link or any access, expiration, or reuse rules. The draft adds an unsupported security qualifier and does not answer the requested link-governance rules, so no equivalent obligation is found in the checked original FRs.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：System shall provide a secure download link for the prepared export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5aed8aeb7583
- 主题：Store Valid Records
- 审查问题：Is a 'Store Valid Records' operation applicable for persisting valid imported asset records after validation and parsing?
- 场景：The system stores valid records from the uploaded file; review whether this persistence step should be documented as a distinct business operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already specifies that the system validates format and data, parses rows, and stores valid records with an error report. This is equivalent to the nominated obligation to persist valid imported asset records after validation and parsing, including validation gating and error handling.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：Document the operation that persists valid imported asset records, including validation gating and error handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5687cabe9346
- 主题：Import Asset Data
- 审查问题：Does the 'Import Asset Data' function require a documented operation for initiating an import?
- 场景：Users upload CSV/Excel files to import asset data; the workflow begins with an upload action.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already documents the import initiation operation: users upload CSV/Excel files, and it identifies the accepted CSV/Excel file formats. The nominated question's core obligation is therefore already stated in an original FR.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：Define the import initiation operation, including accepted file formats and user permissions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c659aea78e2b
- 主题：Validate Export Request
- 审查问题：What specific validation rules apply to 'Validate Export Request' before generating an export file (e.g., selected assets non-empty, supported format CSV/Excel, permissions)?
- 场景：A user submits an export request with no selected assets or an unsupported format; the system must validate and respond consistently.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already states that the system validates the export request before generating the export file. The draft obligation is therefore an equivalent restatement of an existing FR requirement, not a new in-scope obligation.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must validate the export request against documented rules before generating the file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-631356f984fd
- 主题：Generate Export File
- 审查问题：What should happen if 'Generate Export File' fails or is interrupted, and should the user be able to retry the export operation?
- 场景：The system encounters an error while generating the CSV/Excel file; the user needs clear feedback and a defined recovery path.
- 模型初步去向：unsupported
- 模型解释：The cited evidence and relevant export FRs (FRBLOCK-015, FRBLOCK-016, FRBLOCK-018) describe only successful export/report generation and do not state failure/interruption handling, error reporting, withholding a download link on failure, or retry behavior. The draft therefore introduces policy not supported by the checked original FRs.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：If export file generation fails, the system must report an error and must not provide a download link; retry behavior is documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5971ac5c5791
- 主题：Export Log
- 审查问题：What operations, if any, should be supported on the 'Export Log' beyond creation (e.g., view, retrieve, or export the log)?
- 场景：An administrator wants to audit export activity; the FR only states an export log is output.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-018, and also FRBLOCK-016, only lists 'export log' as an output of the export operation. No original FR requires that any read/retrieval operation on the export log be explicitly documented if required. The draft adds this documentation policy without source support.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must create an export log entry for each export; any read/retrieval operation must be explicitly documented if required.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2fe03193e418
- 主题：Stage for senior-admin approval
- 审查问题：What operation-level behavior should be documented for Stage for senior-admin approval between validation and the senior-admin decision?
- 场景：The system validates a permission request, then stages it for senior-admin approval before any permission update is applied.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that the validated permission request is staged for senior-admin approval and that permissions are updated upon approval, which is equivalent to the draft's staging-pending state and approval condition.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：Define the staging operation's pending state and the conditions under which the staged request proceeds to approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3db9604ac109
- 主题：Update permissions upon approval
- 审查问题：What operation-level preconditions and effects should be documented for Update permissions upon approval?
- 场景：After senior-admin approval, the system updates permissions and returns status 'Permissions Set'.
- 模型初步去向：unsupported
- 模型解释：The original FRBLOCK-019 already covers the permission update upon approval and the resulting 'Permissions Set' status. The draft adds a meta-requirement to document operation-level preconditions and effects, which is not a system business obligation and is not supported by the source FRs.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：Document the post-approval permission-update operation's preconditions, applied changes, and resulting Permissions Set state.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-81a9c2e5c7e3
- 主题：Validate replacement request
- 审查问题：What specific validation rules or checks must the system apply when validating a replacement request (e.g., current admin ID existence, completeness of new admin info, authorization of the senior administrator), and should the validation outcome be recorded?
- 场景：A senior administrator submits a replacement form with current admin ID and new admin info; the system must validate the request before staging it for top-level approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that the system validates the replacement request and stages it for top-level approval, which is equivalent to the nominated draft obligation. No additional supplement is needed.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must validate the replacement request against defined rules before staging it for top-level approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1bd9143950bf
- 主题：Stage replacement request for approval
- 审查问题：How should the system stage a validated replacement request for top-level approval—what data is persisted, what status is assigned, and how is the top-level approver notified or given access?
- 场景：After validation, the system stages the replacement request so that a top-level approver can review and approve it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that the system validates the replacement request and stages it for top-level approval, which is equivalent to staging a validated replacement request and making it available to the approver.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must stage a validated replacement request for top-level approval and make it available to the approver.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-05728143a641
- 主题：Update admin records
- 审查问题：Which admin record fields must be updated upon top-level approval, and should the update and status change to 'Replaced' be performed atomically to avoid inconsistent states?
- 场景：Top-level approval occurs for a staged replacement request; the system then updates the admin record with the new admin information.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that the system stages the replacement for top-level approval, updates admin records upon approval, and outputs the updated admin record with status 'Replaced', which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：Upon top-level approval, the system must update the admin record with the new admin information and set its status to 'Replaced'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-75d55acc1863
- 主题：Stage for Admin Approval
- 审查问题：Is the 'Stage for Admin Approval' operation applicable as the handoff step from request submission to admin decision, or should separate approval/rejection operations also be documented?
- 场景：FR-21 describes staging for admin approval and updating status upon approval, but does not name an admin decision operation. A reviewer needs to determine which operations are applicable.
- 模型初步去向：covered
- 模型解释：FR-21 already documents that submitted asset requests are staged for admin approval and status is updated upon approval, with Approved/Rejected statuses, while FR-22 documents that administrators review and approve or reject asset requests and the system updates request status and notifies users. Together these original FRs cover both the staging handoff and the explicit approval/rejection operations, so no additional business obligation is needed.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Define whether staging for admin approval is the only required operation or whether explicit approve/reject operations are also needed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-75e2194992f5
- 主题：Update Status on Approval
- 审查问题：Should 'Update Status on Approval' be treated as a distinct operation triggered by an admin's decision?
- 场景：The FR says the system 'updates status upon approval', but it is unclear whether this is a separate operation or part of the approval action. A reviewer needs to clarify the operation boundary.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that the system updates status upon approval, and its screening is marked covered. The nomination asks only whether this status update should be modeled as a distinct operation or included within the approval operation, which is a design/modeling clarification rather than an uncovered business obligation.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Clarify whether status update is a separate operation or included in the approval operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-77973b511a41
- 主题：Validate Asset Request
- 审查问题：Is 'Validate Asset Request' an applicable operation before the request is staged for admin approval?
- 场景：FR-21 says the system validates the request before staging it. A reviewer needs to confirm whether this validation is a named operation in the workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already states that the system validates the request and stages it for admin approval, establishing that validation occurs before staging for approval. This is equivalent to the nominated operation and obligation.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Confirm that Validate Asset Request is an operation performed before staging for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6316cf9ef179
- 主题：Approve Asset Request
- 审查问题：Does the 'Approve Asset Request' operation need to explicitly cover a rejection decision, or is rejection a separate operation?
- 场景：An administrator reviews an asset request and decides to reject it with a reason; the system must update the request status to rejected and notify the user.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already specifies that administrators review and approve or reject asset requests, that the approval form includes the decision and reason, and that the system updates the request status and notifies users. This covers the draft obligation to support a reject decision, capture the reason, and update the request status.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall support a reject decision for an asset request, capturing the reason and updating the request status accordingly.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-440049b1120b
- 主题：Update Request Status
- 审查问题：Should the approval form's reason be stored and associated with the request status update?
- 场景：An administrator approves or rejects a request and enters a reason; the system updates the request status. The reason must be available for audit or notification.
- 模型初步去向：retained
- 模型解释：FRBLOCK-022 shows that the approval form includes a reason, but no original FR requires that reason to be persisted or associated with the request status update. The nomination scenario states the reason must be available for audit or notification, so this is a supported in-scope obligation that is not covered by any checked FR.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall persist the reason from the approval form with the updated request status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d3de97a97598
- 主题：Notify Users
- 审查问题：Does the notification operation apply to both approval and rejection outcomes, and should it include the decision reason?
- 场景：An administrator rejects an asset request with a reason; the system updates status and notifies the user. The user should receive the reason.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-022 confirms an existing obligation to notify users for both approval and rejection decisions, but no original FR requires including the decision reason in the notification; the reason is only identified as an approval-form input. The draft therefore adds an unsupported policy element.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system shall send a user notification for both approval and rejection decisions, including the decision reason when provided.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-379748a60e49
- 主题：Send Email Notification
- 审查问题：Should the 'Send Email Notification' operation include a documented retry or fallback process when email delivery fails?
- 场景：An event triggers an email notification, but the email service is temporarily unavailable.
- 模型初步去向：retained
- 模型解释：FRBLOCK-023 establishes the email notification operation, but none of the checked original FRs specify retry, fallback, or failure handling for email delivery. The nominated obligation is in-scope and not already covered.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Define failure handling for the email notification operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-870acc45a56e
- 主题：Send Log
- 审查问题：Does the 'Send Log' need to record failed attempts as well as successful sends?
- 场景：A notification attempt fails, and the system still needs to log the outcome.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-023 only identifies 'Sent email and send log' as an output. It does not state that the send log records failed attempts or captures both successful and failed email notifications, so the draft obligation introduces a requirement not supported by the source evidence.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Specify that the send log captures both successful and failed email notifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9e191a5ec509
- 主题：Registration Event
- 审查问题：Should the list of triggering events be exhaustive, or can additional events trigger email notifications?
- 场景：A new event type, such as a password reset, needs to send an email notification.
- 模型初步去向：covered
- 模型解释：FRBLOCK-023 already uses 'events such as registration or profile updates,' which establishes that the triggering event list is illustrative rather than exhaustive, so the draft obligation is equivalent to an existing FR and does not need a supplement.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：Specify whether the event list is illustrative or exhaustive.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c3bd71e959c6
- 主题：Parse feedback content
- 审查问题：Should the parsing operation be reviewed to define what feedback content is extracted and how parse failures are handled?
- 场景：A user feedback email is received and the system parses the content. FR-24 does not specify parsing rules, fields, or failure behavior.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-024 only states that the system parses the content; it does not establish an obligation to extract defined feedback fields or to handle unparseable content by any rule. The draft therefore adds policy details not supported by the source evidence.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must parse feedback email content into defined feedback fields and handle unparseable content according to a specified rule.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-630126661d60
- 主题：Store feedback
- 审查问题：Should the storage operation be reviewed to define which feedback attributes and metadata are persisted?
- 场景：Parsed feedback content is stored by the system. FR-24 only states 'stores it' without specifying the stored data structure or retention.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-024 only states that parsed feedback is stored and does not specify which feedback attributes or associated metadata must be persisted. The draft adds a new requirement to persist 'sufficient associated metadata to support administrator handling,' which is not supported by the cited FR or screening evidence.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must persist parsed feedback and sufficient associated metadata to support administrator handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bfe98507bbf7
- 主题：Notify administrators
- 审查问题：Should the administrator notification operation be reviewed to define channel, timing, and notification content?
- 场景：After storing feedback, the system notifies administrators for handling. FR-24 does not specify how or when notification occurs or what information it contains.
- 模型初步去向：unsupported
- 模型解释：FR-24 only establishes that administrators are notified for handling; it does not require notification via a defined channel or with sufficient context. The draft adds these specifics without source support.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must notify administrators of newly stored feedback through a defined channel with enough context to handle it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6b332b76a110
- 主题：User feedback email received
- 审查问题：Should the receipt event be reviewed to define how incoming feedback emails are recognized as feedback rather than ordinary email?
- 场景：A user feedback email arrives at the system. FR-24 treats this as the trigger for parsing, storage, and notification but does not define detection criteria.
- 模型初步去向：retained
- 模型解释：FR-24 covers receiving user email feedback and initiating parsing, storage, and notification, but it does not define how incoming emails are recognized as feedback rather than ordinary email. No other original FR addresses this recognition/detection obligation, so the nomination identifies an in-scope gap.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must detect incoming user feedback emails and use that event to initiate feedback parsing and storage.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8e17c4a9b1c8
- 主题：View Asset Change History
- 审查问题：Does the View Asset Change History operation need to support filtering by user or operation in addition to asset ID, change type, and change date, or is the documented search scope complete?
- 场景：An auditor wants to find all changes made by a specific user or all occurrences of a particular operation across assets.
- 模型初步去向：covered
- 模型解释：FRBLOCK-025 already specifies that users query asset change logs by asset ID, change type, or change date. The draft obligation does not add filtering by user or operation; it matches the documented search scope. No additional filtering requirement is supported by the evidence.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The View Asset Change History operation should allow users to query asset change logs by the documented search criteria and return matching change history.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-dab987d864c0
- 主题：Query Asset Category
- 审查问题：Is the Query Asset Category operation intended to be a read-only retrieval operation, consistent with the View Asset Category title?
- 场景：A user searches for a category and views its details; no create, update, or delete action is described.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already defines the View Asset Category feature as a query/view operation where users query asset categories by name or ID, which is equivalent to documenting Query Asset Category as a read-only retrieval operation.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The View Asset Category feature should document Query Asset Category as a read-only retrieval operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-31fd992bafac
- 主题：Query Asset Category
- 审查问题：Does the Query Asset Category operation treat category name and category ID as alternative or conjunctive search criteria?
- 场景：A user searches by category name only, or by category ID only, and expects the operation to return matching category details.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already states that users query asset categories by name or ID, which establishes that category name and category ID are alternative search criteria. The nominated draft does not introduce a new business obligation beyond documenting that existing behavior.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The View Asset Category feature should document whether category name and category ID are alternative or conjunctive inputs for the Query Asset Category operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-261c34d149c8
- 主题：Validate changes
- 审查问题：Should the Validate changes operation define what validation rules apply to the category-edit form, such as name and description constraints?
- 场景：An administrator submits a category edit with invalid data; the system should reject or flag it before staging for approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 already specifies that the system validates changes and stages them for senior-admin approval, which is equivalent to the nominated obligation to validate submitted category changes before staging them for senior-admin approval.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must validate submitted category changes before staging them for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ff88523ca27e
- 主题：Edit Asset Category
- 审查问题：Does the Edit Asset Category operation need documented preconditions and postconditions, such as authorized actor and resulting status?
- 场景：An administrator edits a category and expects the output to be an updated category with status Modified.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 already specifies administrators modifying category information, validation and senior-admin approval, and the resulting category status 'Modified', covering the nominated Edit Asset Category operation and its preconditions/postconditions.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must provide an Edit Asset Category operation that allows administrators to modify existing category information.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ef10e457aa3d
- 主题：Update Category Upon Approval
- 审查问题：Should the Update Category Upon Approval operation be documented as applying only staged changes after senior-admin approval?
- 场景：A senior admin approves a staged category edit; the system updates the category and sets status Modified.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 already specifies staging category changes for senior-admin approval, updating the category upon approval, and setting status to Modified, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：Upon senior-admin approval, the system must apply the staged category changes and set the category status to Modified.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall generate the export file only if the export request has been validated successfully.

2. [model_preliminarily_retained] The system shall define and apply consistent matching semantics for asset search by name, type, and ID, including whether matching is exact, partial, or both, and whether multiple criteria can be combined in a single query.

3. [model_preliminarily_retained] The system shall return detailed asset information with a complete and consistent output schema, including at minimum name, type, quantity, purchase date, and status, and shall explicitly define all additional fields represented by 'etc.' for every asset type.

4. [model_preliminarily_retained] The system shall clearly indicate when an asset query returns no matching assets and shall not present an ambiguous empty success response.

5. [model_preliminarily_retained] The system shall record the return request's approval outcome as an operation status that is distinct from the asset status Returned.

6. [model_preliminarily_retained] The system shall validate deletion requests before staging them for approval, applying defined validation criteria and handling invalid requests with appropriate failure outcomes.

7. [model_preliminarily_retained] The system shall define the 'Deleted' status as the terminal state of an asset record that has been removed by the approved deletion operation; the deletion operation upon approval shall set the asset record's status to 'Deleted'.

8. [model_preliminarily_retained] The system shall specify the outcome and next action when an admin does not approve a deletion request.

9. [model_preliminarily_retained] The system shall verify that the acting user has Administrator privileges before allowing the creation of a new user account.

10. [model_preliminarily_retained] The system shall enforce required-field and format validation rules for the new-user form, covering username, password, email, phone, and department.

11. [model_preliminarily_retained] The Query User Details operation shall return an empty result when no users match, a single user record when exactly one user matches, and a list of user records when multiple users match.

12. [model_preliminarily_retained] The system shall define the Senior Admin approver role for user deletion requests, including how the approver is identified or resolved, and its authority to approve such requests, distinct from the Administrators who initiate deletion.

13. [model_preliminarily_retained] The system shall create a pending approval item for a user deletion request and set the request status to Pending while it awaits senior-admin approval or rejection.

14. [model_preliminarily_retained] The system shall maintain operation statuses for approval-driven operations, transitioning from pending review to approved or rejected, and then to completed after the approved operation is executed.

15. [model_preliminarily_retained] The system shall set the operation status to Pending while an approval process is awaiting administrator review.

16. [model_preliminarily_retained] The system shall specify the condition(s) under which an operation transitions into the In Progress state.

17. [model_preliminarily_retained] The system shall define and document the conditions under which asset and user operations are rejected.

18. [model_preliminarily_retained] The system shall reject invalid report parameters and return a clear error response.

19. [model_preliminarily_retained] The system shall define and apply validation rules for uploaded CSV/Excel files and record each validation failure in the error report.

20. [model_preliminarily_retained] The system shall persist the reason entered on the approval form and associate it with the updated request status so it remains available for audit or notification.

21. [model_preliminarily_retained] The system shall notify the requestor (User) when an asset request decision is made.

22. [model_preliminarily_retained] The system shall define and document a retry or fallback process for the email notification operation when email delivery fails.

23. [model_preliminarily_retained] The system shall validate event details and recipient list before sending email notifications, including handling malformed event data and invalid recipient addresses.

24. [model_preliminarily_retained] The system shall define and apply criteria for recognizing incoming user feedback emails, distinguishing them from ordinary email, before initiating feedback parsing and storage.
