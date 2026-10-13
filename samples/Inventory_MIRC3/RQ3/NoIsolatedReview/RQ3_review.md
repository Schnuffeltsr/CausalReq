# RQ3 审查材料：Inventory_MIRC3 / NoIsolatedReview

**注意：下列去向只是模型初步筛查，不是人工有效性结论。**

## 运行设置

```json
{
  "signed_propagation": true,
  "isolated_review": false,
  "operation_review": true,
  "full_document_validation": true
}
```

## dependency：20 条提名

### DEP-001
- 主题：Stage change for admin approval → Deletes the Record upon Approval
- 审查问题：Do the requirements clearly state that once a change is staged for admin approval, admin approval of that staged change triggers deletion of the record?
- 场景：A change is staged for admin approval, and the admin approves it; the documented target behavior is that the system deletes the record upon approval.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-006 already states the equivalent obligation: the system stages the request for admin approval and deletes the record upon approval. FRBLOCK-010 also covers the senior-admin variant. Therefore the nominated obligation is already present in the checked original requirements.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006, FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Upon admin approval of a staged change, the system shall delete the record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Validate Configuration Details → Activate Workflow
- 审查问题：Does the requirements documentation explicitly state that workflow activation is contingent on successful validation of configuration details and on senior-admin approval of the staged setup, rather than only implying this through the staged approval chain?
- 场景：The FR states that the system 'validates configuration details' and 'stages the setup for senior-admin approval.' It also states that 'senior-admin approval' triggers workflow activation, and that the system 'activates the workflow upon approval.' The source–target dependency indicates that 'Validate Configuration Details' ultimately relates to 'Activate Workflow,' but the direct obligation between those endpoints may need review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the system validates configuration details, stages the setup for senior-admin approval, and activates the workflow upon approval, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system shall activate the workflow only after configuration details have been successfully validated and the staged setup has received senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Approval-start request → Deletes the Record upon Approval
- 审查问题：Does the requirements specification explicitly link an approval-start request to deletion of the record upon approval, such that the record deleted is the one associated with the asset ID in the validated approval-start request that was staged for admin review and then approved?
- 场景：An approval-start request containing an asset ID and operation type is submitted, validated, and staged for admin review; admin approval is then granted, which the source-target dependency says deletes the record upon approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states the equivalent obligation: it validates a deletion request containing an asset ID, stages it for admin approval, and deletes the record upon approval. This directly links the approved staged request to deletion of the associated record.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：When an approval-start request containing an asset ID is validated and staged for admin review and admin approval is granted, the system shall delete the record associated with that approval-start request upon approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Validates the Request → Update status to Modified
- 审查问题：Does the requirement explicitly require admin approval to intervene between validating the request and updating the status to “Modified,” rather than allowing validation alone to update the status?
- 场景：The dependency model connects “Validates the Request” to “Update status to Modified” through “Staged for Admin Approval” and “Admin approval.” The supplied FR text states that the system validates the request, stages it for admin approval, and that upon approval it updates the status to “Modified.”
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already explicitly states that the system validates the data, stages the change for admin approval, and updates the status to “Modified” upon approval, which is equivalent to the nominated obligation requiring admin approval between validation and the “Modified” status update.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system shall update the status to “Modified” only upon admin approval of a validated request that has been staged for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Senior Admin Approval Event → Workflow Configured
- 审查问题：Does FRBLOCK-011 explicitly require that a senior-admin approval event activates the workflow and produces a stored workflow with status “Configured,” rather than only implying one side of that dependency?
- 场景：A senior admin approval event occurs for a workflow; the requirement says this “activates the workflow upon approval” and identifies the output as “Stored workflow with status ‘Configured.’”
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already explicitly states that the setup is staged for senior-admin approval, the workflow is activated upon approval, and the output is a stored workflow with status “Configured,” which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：Upon senior-admin approval, the workflow shall be activated and stored with status “Configured.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Asset Request Form → User Notification
- 审查问题：What requirement ensures that a user notification about an asset request decision is traceable to the submitted Asset Request Form and includes the form’s populated details and the stored request’s decision status?
- 场景：A user submits an asset request using the asset-request form with name, type, quantity, and purpose populated. The request is stored with status “Approved” or “Rejected.” Administrators review and approve or reject asset requests, and the system notifies users. The dependency from Asset Request Form to User Notification is enabled through Submit Asset Request, Stored Request, Approve Asset Request, and Notify Users.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-022 states only that the system updates the request status and notifies users, and FRBLOCK-021 covers submitting/validating the request and its stored status. Neither original FR requires the notification to include the form's populated details or the decision status. The draft therefore adds an unsupported notification-content policy rather than stating an obligation already present or directly supported.
- 原文证据 FR：FRBLOCK-021, FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：When the system notifies users about an asset request decision, the user notification shall include the request’s name, type, quantity, purpose, and decision status (“Approved” or “Rejected”).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Activate Workflow → Workflow Configured
- 审查问题：Should FRBLOCK-011 explicitly require that activating the workflow produces a stored workflow with status 'Configured'?
- 场景：The documented dependency shows that 'Activate Workflow' PRODUCES 'Workflow Configured': the source FR says 'activates the workflow' and the target FR says 'Stored workflow with status “Configured.”' This indicates activation is expected to result in the workflow being stored with status 'Configured.'
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already states that the workflow activation output is a stored workflow with status “Configured,” which is equivalent to the drafted obligation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：When the system activates the workflow, the stored workflow shall have status 'Configured.'
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Validates the Request → Update Status on Approval
- 审查问题：When a request has been validated and staged for admin approval, and the admin approves it, what exact request status must the system set, and does the requirement define that status value?
- 场景：A request is validated, staged for admin approval, and then approved by an admin. The FR states that the system "updates status upon approval," but the specific status value is not stated.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies the equivalent obligation by stating that the stored request has status “Approved” or “Rejected” after admin approval, thereby defining the approval status value the draft defers to.
- 原文证据 FR：FRBLOCK-006, FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：Upon admin approval of a validated and staged request, the system shall update the request status to the specific approval status defined by the requirements.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Query Approval Status → Approval Status Details
- 审查问题：What must be included in the 'Approval Status Details' returned by Query Approval Status so users can check the status of asset or user operations?
- 场景：A user uses Query Approval Status to check the status of an asset or user operation and expects approval status details, including whether the operation is pending, in progress, approved, or rejected.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already states that users check the status of asset or user operations across pending, in progress, approved, or rejected, and that the query output is approval status details, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：When a user checks the status of an asset or user operation, Query Approval Status shall return approval status details that include the operation's current status among pending, in progress, approved, or rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Approve Asset Request → Notify Users
- 审查问题：When an administrator approves or rejects an asset request, what must the system do to notify users about the decision?
- 场景：Administrators review and approve or reject asset requests. The documented dependency indicates that the approval or rejection decision positively triggers Notify Users, and the target active meaning is that the system has sent a notification to users about the request decision. The supplied FR states that administrators review and approve or reject asset requests and that the system notifies users.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that after administrators approve or reject asset requests, the system updates the request status and notifies users. This is equivalent to the nominated obligation, so no new supplement is needed.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：When an administrator approves or rejects an asset request, the system shall notify users about the request decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Validate approval-start request → Updated operation status
- 审查问题：Does FRBLOCK-012 specify that a validated approval-start request, after being staged for admin review and having the operation executed upon approval, must result in an updated operation status?
- 场景：A request is validated and staged for admin review. Upon approval, the operation is executed. The expected outcome is that the operation status is updated to reflect the current state of the operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system validates the approval-start request, stages it for admin review, executes the operation upon approval, and outputs an updated operation status. This is equivalent to the nominated draft obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall update the operation status when an operation is executed upon approval following validation and staging of the approval-start request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Transfer form → Transfer Asset
- 审查问题：Does the requirement specify that the Transfer form input must contain both an asset ID and a new recipient before the Transfer Asset workflow can be used?
- 场景：A user requests to transfer an asset, and the Transfer Asset workflow depends on the Transfer form as its input.
- 模型初步去向：covered
- 模型解释：The checked original FR FRBLOCK-004 already states the equivalent obligation: the Transfer Asset workflow's input is specified as a Transfer form containing the asset ID and new recipient ('Input: Transfer form (asset ID, new recipient).'). The screening for FRBLOCK-004 marks this nomination as covered, so the drafted dependency obligation adds nothing beyond what the original requirement block already documents.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The Transfer Asset workflow requires a submitted Transfer form containing the asset ID and the new recipient.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Admin approval → Operation executed upon approval
- 审查问题：Does FRBLOCK-012 require that admin approval directly triggers execution of the requested operation, and is that trigger stated as a verifiable obligation?
- 场景：The source 'Admin approval' is linked to the target 'Operation executed upon approval' via a TRIGGERS relation. The quoted FR text says 'approval' and 'executes the operation upon approval'. A reviewer must confirm whether the requirement captures the obligation that, once admin approval occurs, the requested registration, usage, transfer, or return operation is executed.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system executes the operation upon approval, which is equivalent to the nominated obligation that admin approval triggers execution of the requested operation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval, the system shall execute the requested registration, usage, transfer, or return operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Update record upon approval → Status Modified
- 审查问题：Does FRBLOCK-008 clearly require that approval of staged changes updates the user record and sets its status to 'Modified'?
- 场景：An admin approves staged changes; the system updates the user record upon approval; the updated user record has status 'Modified'.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already states that changes are staged for admin approval, the record is updated upon approval, and the output is an updated user record with status "Modified." This is equivalent to the nominated draft obligation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：Upon admin approval of staged changes, the system shall update the user record and set its status to 'Modified'.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：Return Form → Update Asset Status to Returned
- 审查问题：For the dependency from Return Form to Update Asset Status to Returned, does FRBLOCK-005 sufficiently specify that the status update occurs only after the submitted return request has been validated, staged for approval, and approved?
- 场景：A user submits the Return Form with asset ID and return date. The FR states that users initiate asset returns, the system validates the request and stages it for approval, and updates the status to “Returned” upon approval. The dependency chain indicates that the Return Form alone does not directly cause the status update; validation, staging, and approval intervene.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already specifies that the system validates the return request, stages it for approval, and updates the asset status to “Returned” upon approval, so the nominated obligation is equivalent to an existing original FR.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：When a return request submitted via the Return Form is approved after validation and staging, the system shall update the asset status to “Returned”.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Approval-start request → Admin approval
- 审查问题：What requirement ensures that admin approval depends on an approval-start request being validated and staged for admin review, so that approval can trigger the status update?
- 场景：An approval-start request containing an asset ID and operation type is submitted. The documented dependency path is: the request is validated; validation stages it for admin review; admin approval depends on the request being staged for admin review. Admin approval is the target event that triggers the status update.
- 模型初步去向：covered
- 模型解释：The draft obligation is already stated by original FRs. FRBLOCK-021 explicitly validates a request, stages it for admin approval, and updates status upon approval, and FRBLOCK-004, FRBLOCK-005, and FRBLOCK-006 state the equivalent validate-stage-approve-update pattern for other request types. FRBLOCK-012's screening reason also describes the same approval-start validation and admin-review staging flow.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system shall validate a submitted approval-start request containing an asset ID and operation type and stage it for admin review, enabling admin approval to trigger the status update.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Validate Export Request → Generate Export File
- 审查问题：Does FRBLOCK-018 explicitly specify that successful validation of the export request is a precondition for generating the export file, rather than only describing both actions separately?
- 场景：An export request is successfully validated, and the system is expected to proceed toward generating the export file.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-018 lists validation and file generation as separate/sequential actions but does not explicitly state that successful validation is a precondition for generating the export file. The draft strengthens the source statement into a conditional obligation not directly supported by the original FR text.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system shall generate the export file only after the export request has been successfully validated.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Export Asset Data → Downloadable Data File
- 审查问题：Does the requirement explicitly state that executing 'Export Asset Data' produces a 'Downloadable Data File' as its output?
- 场景：A user successfully executes Export Asset Data; the dependent outcome is that a Downloadable Data File is generated and available for download.
- 模型初步去向：covered
- 模型解释：The draft obligation is already stated by FRBLOCK-018, which specifies the output of Export Asset Data as a downloadable data file and export log. Therefore the nominated requirement is covered by an original FR.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：When Export Asset Data is executed, the system shall produce a Downloadable Data File as the export output.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Validate modification data → Operation executed upon approval
- 审查问题：Does the requirement explicitly define which operation is executed upon admin approval after modification data is validated and staged, and any conditions tied to that execution?
- 场景：A modification is submitted; the system validates the data, stages the change for admin approval, and an admin approves it. The dependency indicates that admin approval should trigger execution of the operation upon approval, but the supplied FR only states that the system validates the data, stages the change for admin approval, and executes the operation upon approval without naming the operation or its execution conditions.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-002 already states the equivalent obligation for modification data: the system validates the data, stages the change for admin approval, and updates the status to "Modified" upon approval. This defines both the execution trigger (admin approval) and the operation performed after approval. FRBLOCK-008 and FRBLOCK-012 also express the same approval-triggered execution pattern.
- 原文证据 FR：FRBLOCK-002, FRBLOCK-008, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval of a validated and staged modification, the system shall execute the operation associated with that approved modification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Approval-start request → Transferred
- 审查问题：Do the requirements explicitly trace how a validated and staged approval-start request, after admin approval, results in the ownership update that produces the asset status “Transferred”?
- 场景：The documented dependency runs from an Approval-start request containing an asset ID and operation type, through Validate approval-start request, Request staged for admin review, Admin approval, and Update Ownership Upon Approval, to the target state Transferred. The supplied FR quotations state that the system 'validates the request', 'stages it for admin review', references 'admin approval', 'updates the ownership upon approval', and defines an output of 'Updated owner information with status “Transferred.”'
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already states the equivalent obligation: the system validates the request, stages it for admin approval, updates ownership upon approval, and outputs updated owner information with status “Transferred.” This covers the nominated approval-to-ownership-update-to-Transferred obligation.
- 原文证据 FR：FRBLOCK-004, FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：Upon admin approval of a validated and staged approval-start request, the system shall update the ownership of the identified asset and produce an output with status “Transferred.”
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：0 条提名

## operation：141 条提名

### OPERATION-b9b00e33e40c
- 主题：Register Asset
- 审查问题：Does the 'Register Asset' operation encompass the entire workflow of form submission, validation, storage, status setting, and administrator notification, or should some of these steps be modeled as separate operations?
- 场景：A user submits a completed asset registration form. The system processes it, stores the asset, sets its status to 'Registered', and notifies administrators for review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states the equivalent end-to-end asset registration workflow: form submission, validation for completeness and accuracy, storage, status set to 'Registered', and administrator notification. The draft obligation does not add a new business obligation beyond that original FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The system must provide a Register Asset operation that accepts a completed asset registration form and processes it through validation, storage, status setting, and administrator notification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9ecbd7f7be9f
- 主题：Validate Format and Data
- 审查问题：Is a distinct 'Validate Format and Data' operation applicable before storing the asset, given the FR requires validation for completeness and accuracy?
- 场景：A user submits the asset registration form; the system must check the data for completeness and accuracy before storing it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already requires the system to validate submitted asset registration data for completeness and accuracy before storing the asset record. This is an equivalent business obligation to performing format and data validation on the submitted asset registration form before persisting the asset record, even though 'format' is not named separately in the original FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The system must perform format and data validation on the submitted asset registration form before persisting the asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7c6ef12afa8f
- 主题：Administrators Notified
- 审查问题：Should the notification of administrators be treated as a separate operation triggered after asset registration, rather than an event embedded within the Register Asset operation?
- 场景：After an asset is stored and its status set to 'Registered', administrators need to be notified for review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states that administrators are notified for review after the asset is stored and its status is set to 'Registered', which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The system must notify administrators after an asset is registered and status set to 'Registered', to trigger review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e689d1e977ca
- 主题：Asset Registered
- 审查问题：Does setting the asset status to 'Registered' require a distinct operation, or is it a side effect of the Register Asset operation?
- 场景：Upon successful storage of the asset record, the system sets the asset status to 'Registered'.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-001 already states that the system stores the asset record and sets the asset status to “Registered,” which is equivalent to the nominated draft obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：27
- 草案：The system must set the asset status to 'Registered' upon successful storage of the asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-07691bf8ecbd
- 主题：Edit and submit asset details
- 审查问题：Does the asset modification operation need to define which fields Users can edit and submit, given the listed editable fields?
- 场景：A User opens a registered asset and edits name, type, quantity, or purchase date, then submits the modification.
- 模型初步去向：retained
- 模型解释：FRBLOCK-002 covers an asset modification form with example editable fields and submission for validation/approval, but it does not define the complete permitted editable field set or establish that editing is restricted to only those permitted fields. The remaining original FRs address unrelated operations and are out of scope.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：Users shall be able to edit only the permitted asset fields and submit the modification for validation and approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-36446775fe1b
- 主题：Validate modification data
- 审查问题：Should the validation operation specify the rules and outcomes applied to submitted modification data before it is staged for approval?
- 场景：A User submits changed asset details; the system validates the data before staging it.
- 模型初步去向：covered
- 模型解释：The checked original FRs already include equivalent validation obligations. FRBLOCK-002 states that the system validates submitted asset modification data and stages the change for admin approval, and FRBLOCK-027 similarly states that the system validates changes and stages them for senior-admin approval. The draft’s added reference to defined business rules does not create a materially distinct business obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall validate submitted asset modification data against defined business rules before staging the change for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-33f1e2107efc
- 主题：Stage change for admin approval
- 审查问题：Does the staging operation need to document how a modification is held pending Admin approval and what states or actions are available while staged?
- 场景：After validation, the modification is staged and awaits an Admin decision.
- 模型初步去向：retained
- 模型解释：FRBLOCK-002 supports staging a changed asset for admin approval, but the original FRs do not explicitly define a pending-approval state for validated asset modifications or the Admin approve/reject decision for that staged change. No original FR covers this specific asset-modification staging obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall stage validated asset modifications in a pending-approval state until an Admin approves or rejects the change.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7be45fb1f6ae
- 主题：Admin approval
- 审查问题：Should the Admin approval operation be explicitly defined, including how an Admin approves a staged modification and how rejection is handled?
- 场景：An Admin reviews a staged asset modification and either approves it, triggering the Modified status, or rejects it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already defines the Admin approval operation: administrators review and approve or reject asset requests, and the system updates request status and notifies users, which covers explicit approval and rejection handling.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall require an explicit Admin approval operation before applying a staged asset modification; rejection handling shall be defined.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a9bb3b717f7e
- 主题：Update status to Modified
- 审查问题：Does the status update operation need to be conditional on Admin approval and specify the resulting state if approval is not granted?
- 场景：A staged asset modification receives Admin approval, and the system updates the asset record status to Modified.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already states that the system stages the modification for admin approval and updates the status to “Modified” upon approval, which is equivalent to the draft obligation that the asset record status becomes Modified only after Admin approval of the staged modification.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：27
- 草案：The system shall update the asset record status to Modified only after Admin approval of the staged modification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-df864be7e14b
- 主题：Query Asset Details
- 审查问题：Does the query operation need documented matching rules for each search criterion, including whether name/type/ID matching is exact, partial, or case-insensitive?
- 场景：A User searches by name or type using a partial value; the FR says the system returns matching records but does not define matching semantics.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 establishes that users search asset details by name, type, or ID and that the system returns matching records, but none of the checked original FRs define matching semantics such as exact, partial, or case-insensitive behavior. The obligation is therefore in scope and not covered by an existing FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：The system shall define and apply matching semantics for name, type, and ID searches, including exact, partial, or case-insensitive behavior.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5d7accf82c4a
- 主题：Search Criteria
- 审查问题：Should the query operation define whether multiple search criteria can be combined in one request, or whether only one of name, type, or ID is allowed at a time?
- 场景：A User submits a search with both name and type; the FR says 'using name, type, or ID' but does not clarify if criteria can be combined.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 lists name, type, and ID as search criteria but does not specify whether they can be combined in one request or whether only one criterion is allowed. No other original FR covers this asset detail query combination behavior, so the clarification is in-scope and not covered.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：The system shall define whether asset detail queries accept one criterion or a combination of name, type, and ID.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a4f8609d18ff
- 主题：Search Criteria
- 审查问题：Should the query operation define the expected behavior when no asset matches the supplied search criteria?
- 场景：A User searches for a non-existent asset ID; the FR states that matching records are returned but does not specify the no-match response.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 is the asset query operation and states only that matching records are returned; none of the original FRs defines the no-match response. The draft obligation is in scope and is the natural completion of the query behavior when no matching records exist.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：The system shall return a defined empty-result response when no asset matches the search criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-15e57aecdad8
- 主题：Detailed Asset Information
- 审查问题：Does the query operation need to specify the complete set of asset details returned, since the FR lists name, type, quantity, purchase date, status, etc.?
- 场景：A User queries an asset and receives a subset of fields; the FR's 'etc.' leaves the output scope ambiguous.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 is the relevant in-scope asset-detail query output, and it lists example fields such as name, type, quantity, purchase date, and status with 'etc.' However, it does not already require a defined complete set of returned asset detail fields. The draft obligation is supported by that source but is not equivalent to any checked original FR, so it is retained to resolve the output-scope ambiguity.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：The system shall return a defined complete set of asset detail fields for matching records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1310ac5e8182
- 主题：Users
- 审查问题：Is the query operation applicable to any User without restriction, or is there a documented access condition for performing asset detail queries?
- 场景：A User attempts to query asset details; the FR names Users as the actor but does not define any access restrictions for this operation.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-003 only states that Users search for asset details using name, type, or ID. It does not impose or imply a requirement to define which users may perform the query or under what access conditions. No other original FR supplies that obligation. The draft therefore introduces a new access-control policy not evidenced in the source text.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：27
- 草案：The system shall define which users may perform the asset detail query operation and under what access conditions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-919c4f866bfc
- 主题：Transfer Asset
- 审查问题：Should the Transfer Asset operation be defined as a user-initiated transfer request that stages the change rather than immediately reassigning ownership?
- 场景：A User submits a transfer for an asset; the reviewer needs to confirm the operation boundary is request creation and admin approval, not direct ownership mutation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already states that users request asset transfers, the system stages the request for admin approval, and ownership is updated only upon approval; FRBLOCK-012 likewise covers staging transfer approval processes and executing only upon approval. This is equivalent to allowing users to initiate a transfer request without immediate ownership reassignment.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall allow Users to initiate an asset transfer request without immediately changing ownership.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ca6f9571cd83
- 主题：Validate Transfer Request
- 审查问题：Is the Validate Transfer Request operation required before the transfer is staged for Admin approval, and what validation rules apply to the asset ID and new recipient?
- 场景：A User submits the transfer form; the system must validate the request before an Admin sees it.
- 模型初步去向：covered
- 模型解释：The draft obligation is already stated by original FRBLOCK-004 and FRBLOCK-012, which both describe validating the request and staging it for admin approval/review before approval. The nomination’s core obligation to validate a transfer request before staging for Admin approval is therefore equivalent to existing FR coverage. The more specific validation rules for asset ID and new recipient are not part of the draft obligation itself.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall validate a transfer request before staging it for Admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3b2fd4429d3b
- 主题：Stage for Admin Approval
- 审查问题：Does the Stage for Admin Approval operation require an explicit approval decision step that can approve or reject the staged transfer?
- 场景：A transfer request is staged; an Admin reviews it and must record an approval or rejection before ownership changes.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already requires staging for admin approval and updating ownership only upon approval, which is equivalent to requiring an approval decision before ownership update. Screening notes for FRBLOCK-004 mark it covered, and other original FRs also describe approval/rejection decisions for staged requests.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall stage transfer requests for Admin approval and support an approval decision before ownership update.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fb15f0d854e3
- 主题：Update Ownership Upon Approval
- 审查问题：Should the Update Ownership Upon Approval operation update the asset owner and set status to Transferred only after an Admin approves the staged request?
- 场景：An Admin approves a staged transfer; the system updates ownership and status.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-004 already specifies that the system validates the transfer request, stages it for admin approval, and updates ownership upon approval, with output status “Transferred.” FRBLOCK-012 also covers executing the transfer operation only upon approval. The draft obligation is therefore already stated by the original requirements.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall update asset ownership only after Admin approval of the staged transfer.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f88cf049e31c
- 主题：Transfer form
- 审查问题：Should the Transfer form operation require asset ID and new recipient as inputs for every transfer request?
- 场景：A User initiates a transfer; the form must capture asset ID and new recipient before validation and staging.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 explicitly specifies the Transfer form with inputs asset ID and new recipient, which is equivalent to requiring those fields for transfer requests.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall require asset ID and new recipient on the Transfer form for transfer requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3a81eacb8f28
- 主题：Admin
- 审查问题：Does the Admin operation include reviewing staged transfers and approving or rejecting them?
- 场景：A transfer request is staged; an Admin is responsible for the approval decision.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already stages requests for admin approval and records Approved/Rejected statuses, which the original FR screening treats as equivalent to an Admin approving or rejecting staged requests. Thus the nominated obligation is already stated in an original FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall allow an Admin to review and approve or reject staged transfer requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-79f8bd5d48b2
- 主题：Transferred
- 审查问题：Should the workflow set the asset status to Transferred as the output of a successfully approved ownership update?
- 场景：After Admin approval and ownership update, the asset status is expected to show Transferred.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already states that ownership is updated upon approval and that the output includes status “Transferred,” which is equivalent to setting the asset status to Transferred after a successfully approved ownership update.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：27
- 草案：The system shall set the asset status to Transferred after a successfully approved ownership update.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-071eac7f9c57
- 主题：Initiate Asset Return
- 审查问题：Does initiating an asset return require the user to submit a return form containing the asset ID and return date?
- 场景：A user begins the return process by providing the asset ID and return date.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already states the equivalent obligation: initiating an asset return uses a return form containing the asset ID and return date.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system shall accept a return form with asset ID and return date to initiate an asset return.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ad888718c9d4
- 主题：Validate Return Request
- 审查问题：What validation must the system perform on the return request before staging it for approval?
- 场景：A user submits a return form, and the system validates the request.
- 模型初步去向：covered
- 模型解释：The checked original FRs already state the equivalent obligation: FRBLOCK-005 provides that the system validates the request and stages it for approval, and FRBLOCK-012 confirms this applies to return operations. No new business obligation is introduced by the draft.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system shall validate a return request before it can be staged for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6d8af98d6d5a
- 主题：Stage Return Request for Approval
- 审查问题：Does staging a return request for approval require the system to hold the request in a pending approval state before any asset status change?
- 场景：A validated return request is staged for approval but has not yet been approved.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-005 already states that the system validates the return request, stages it for approval, and updates status to “Returned” only upon approval, which is equivalent to holding a validated return request in a pending approval state before any asset status change. FRBLOCK-012 also confirms return operations are staged for review and executed only upon approval.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system shall stage a validated return request for approval and hold it in a pending approval state until a decision is made.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4c4b5003111a
- 主题：Update Asset Status to Returned
- 审查问题：Is approval a mandatory precondition for updating the asset status to Returned?
- 场景：A staged return request receives approval, and the system then updates the asset status.
- 模型初步去向：covered
- 模型解释：The nominated obligation is already stated by original FRBLOCK-005, which specifies that the return request is staged for approval and the asset status is updated to “Returned” upon approval. This establishes approval as a mandatory precondition equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：27
- 草案：The system shall update the asset status to Returned only after the staged return request is approved.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9c4d2801a63f
- 主题：Staged for Admin Approval
- 审查问题：Does the workflow require a distinct admin approval operation for a staged deletion request?
- 场景：An admin reviews a staged deletion request and must approve it to trigger deletion; the FR describes staging and deletion upon approval but does not explicitly name the approval operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that the deletion request is staged for admin approval and that the record is deleted upon approval, which is equivalent to the draft obligation requiring an admin approval operation for a staged deletion request.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must provide an admin operation to approve a staged deletion request, which triggers deletion of the asset record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b813815c941e
- 主题：Validates the Request
- 审查问题：Should request validation be modeled as a separate operation before staging?
- 场景：A user submits a deletion request for an obsolete asset; the system must validate it before it can be staged for admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already specifies the equivalent obligation: the system validates the deletion request, stages it for admin approval, and deletes the record upon approval. Therefore the draft does not add a new business obligation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must perform validation on a deletion request before staging it for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-24fa97f37662
- 主题：Deletion Request
- 审查问题：Is an explicit operation needed for a user to submit a deletion request?
- 场景：A user identifies an obsolete asset and initiates a removal request; the FR mentions users request removal but does not define the submission operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that users request removal of obsolete assets, which is equivalent to allowing a user to submit a deletion request for an obsolete asset. The nominated obligation adds no distinct business requirement beyond this existing FR.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must allow a user to submit a deletion request for an obsolete asset.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1f7565eb81e5
- 主题：Deleted
- 审查问题：Is a specific operation required to update the asset record status to 'Deleted' after approval?
- 场景：Upon admin approval, the asset record is removed and its status becomes 'Deleted'; the FR lists the output but not the operation that sets the status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-006 already states that the asset record is deleted upon approval and that the output is a removed asset record with status “Deleted,” which is equivalent to the nominated obligation to update the asset record status to “Deleted” after approval.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must update the asset record status to 'Deleted' when the deletion is performed after approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c99973e73d87
- 主题：Admin
- 审查问题：Does the admin approval workflow require an operation for an admin to reject a staged deletion request?
- 场景：An admin reviews a staged deletion request and decides not to approve it; the FR only describes deletion upon approval and does not mention rejection.
- 模型初步去向：retained
- 模型解释：The source describes staged deletion requests for admin approval and deletion only upon approval, but no original FR provides an admin operation to reject such a request or update its status on rejection. This is an in-scope gap in the deletion approval workflow, supported by the existing approval/rejection context (e.g., status values including rejected and admin rejection of other requests).
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：27
- 草案：The system must provide an admin operation to reject a staged deletion request, updating its status accordingly.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-44bb79b9da0a
- 主题：Administrator
- 审查问题：Should the Administrator actor be the only role authorized to perform the Create New User Accounts operation?
- 场景：A non-administrator attempts to create a new user account through the new-user form.
- 模型初步去向：unsupported
- 模型解释：The cited evidence (FRBLOCK-007) states that Administrators create new user accounts, but it does not state that only Administrators may perform this operation or that other roles are prohibited. The draft adds an exclusivity restriction that is not supported by the source text.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：Only an Administrator may perform the Create New User Accounts operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d46720a1de65
- 主题：Create New User Accounts
- 审查问题：Should the Create New User Accounts operation be triggered by an Administrator submitting the New-User Form?
- 场景：An Administrator submits a completed New-User Form to create a new user account.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already specifies that Administrators create new user accounts and that the input is a New-user form, which is equivalent to the nominated obligation that the Create New User Accounts operation is initiated by an Administrator submitting a New-User Form.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The Create New User Accounts operation must be initiated by an Administrator submitting a New-User Form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2986e000b869
- 主题：Validate New-User Form
- 审查问题：Should validation of the New-User Form be a required operation before the user is stored?
- 场景：An Administrator submits a New-User Form with missing or malformed fields.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already specifies that the system validates the form, stores the user, and sends an activation email, which establishes the equivalent obligation that form validation precedes storing the user.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The Validate New-User Form operation must succeed before the Store User operation executes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5bd87b29836a
- 主题：Store User
- 审查问题：Should the Store User operation persist the new user as a New User Record with status Activated?
- 场景：An Administrator submits a valid New-User Form.
- 模型初步去向：covered
- 模型解释：The nominated obligation is already stated by an original FR: FRBLOCK-007's screening confirms that FR-07 stores the user and specifies the output as a New User record with status "Activated," which is equivalent to requiring the Store User operation to persist a new user with Activated status. No new business obligation is introduced.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The Store User operation must create a New User Record with status Activated.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6f9753e57e5f
- 主题：Send Activation Email
- 审查问题：Should the Send Activation Email operation be automatically triggered after the Store User operation succeeds?
- 场景：A new user record is successfully stored.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-007 already states that the system stores the user and sends an activation email within the same Add User workflow, which covers the nominated obligation. FRBLOCK-023 also states that the system automatically sends email notifications for registration events.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The system must send an activation email after successfully storing the new user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-77a6205a2afc
- 主题：New User Record Activated
- 审查问题：Should the New User Record Activated state be the required output of the Create New User Accounts operation?
- 场景：An Administrator completes the new-user creation workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already specifies the output of the relevant operation as a New User record with status “Activated,” which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：27
- 草案：The Create New User Accounts operation must produce a New User Record with status Activated.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-94d247f587b8
- 主题：Edit User Profile
- 审查问题：Does the 'Edit User Profile' operation apply only to a User editing their own profile, or should it also apply to an Admin editing another user's profile?
- 场景：A user submits a profile-edit form; an admin may need to correct another user's profile directly.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 already states that users edit their own profiles, which is equivalent to the draft obligation restricting profile-edit operations to self-editing unless a separate admin-edit operation is documented.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must restrict the profile-edit operation to a user editing their own profile unless a separate admin-edit operation is documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f3cb7aa48bf7
- 主题：Validate changes
- 审查问题：Is the 'Validate changes' operation applicable to all fields in the profile-edit form (name, username, email, phone), or only to a subset of those fields?
- 场景：A user changes username and email; the system must decide which fields require validation before staging.
- 模型初步去向：unresolved
- 模型解释：The only potentially relevant original FR, FRBLOCK-008, establishes that the system validates profile changes and stages them for admin approval, but the screening states it does not specify whether validation applies to every submitted profile field or only a subset. No other FR addresses profile-edit validation. Therefore the draft's all-fields obligation cannot be confirmed as covered or retained, nor clearly rejected as unsupported from the supplied evidence.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must validate every submitted profile field before staging changes for admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7514663babec
- 主题：Stage for Admin Approval
- 审查问题：Does the 'Stage for Admin Approval' operation apply immediately after validation, and does it require an Admin actor to be notified or assigned for approval?
- 场景：A user saves valid profile changes; the system stages them and an admin must later approve or reject.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-008 already states that validated changes are staged for admin approval and the record is updated only upon approval, which is equivalent to placing validated profile changes into a pending admin-approval state before updating the user record.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must place validated profile changes into a pending admin-approval state before updating the user record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e8babc1e0219
- 主题：Update record upon approval
- 审查问题：Is the 'Update record upon approval' operation applicable only after an Admin explicitly approves the staged changes, and should it be blocked if no approval exists?
- 场景：A staged profile change awaits admin decision; the system should not update the user record until approval is recorded.
- 模型初步去向：covered
- 模型解释：The checked original FRBLOCK-008 already states that changes are staged for admin approval and the record is updated upon approval, which is equivalent to the nominated obligation that the user record update occur only after an admin approval action has been recorded.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：27
- 草案：The system must update the user record only after an admin approval action has been recorded for the staged changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e93d9a5a0185
- 主题：Query User Details
- 审查问题：Does the documented workflow permit the Query User Details operation to support combining username, email, and department criteria in one search, or is each criterion a separate operation?
- 场景：A user searches for a person by entering a username and selecting a department at the same time, expecting a single filtered result set.
- 模型初步去向：unsupported
- 模型解释：FR-009 states that users search for user information by username, email, or department, indicating alternative individual search criteria. It does not state that criteria can be combined or that results must match all supplied criteria. The draft obligation adds a conjunctive multi-criteria search policy that is not supported by the source.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation should accept any combination of username, email, and department as search criteria and return users matching all supplied criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-12002c912634
- 主题：Search Criteria
- 审查问题：Should the query operation validate and normalize Search Criteria before executing the user search?
- 场景：A user submits an email with mixed case and surrounding whitespace, and the system must decide whether the search operation treats it as valid and equivalent to the stored email.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only identifies Search Criteria as an input for a user search and does not specify any obligation to validate or normalize username, email, or department criteria or define accepted formats. The draft therefore introduces a validation/normalization policy not supported by the cited source, and no checked original FR states an equivalent obligation.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation should validate and normalize Search Criteria according to the accepted username, email, and department formats before querying user records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7560f37b6b46
- 主题：Detailed User Information
- 审查问题：Does the Query User Details operation need to return every listed output field for each matched user, or can fields be omitted based on permissions?
- 场景：A user searches by department and receives multiple matches; the system must decide whether phone and permission level are always included in each result.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only lists the output fields for Query User Details; it does not require every field to be returned for each matched user, nor does it provide a permission-based exception for suppressing fields. The draft therefore adds an unsupported policy condition.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation should return name, username, email, phone, department, and permission level for each matched user unless an explicit permission rule suppresses a field.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-02c599612e11
- 主题：User
- 审查问题：Is the User actor allowed to invoke the Query User Details operation across all departments, or is the operation scoped to the user's own department?
- 场景：A user in one department searches by another department name and expects to see matching users from that department.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-009 only states that users can search for user information by username, email, or department. It does not specify any department-based access scope or enforcement rule for the Query User Details operation, and no other original FR screening establishes that the User actor is restricted to their own department. The draft obligation therefore introduces an unsupported policy choice.
- 原文证据 FR：FRBLOCK-009
- 全文已检查 FR 数：27
- 草案：The Query User Details operation should enforce the department scope applicable to the User actor when returning user information.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-461564ae4012
- 主题：Validate deletion request
- 审查问题：Should the user deletion workflow require validating the deletion request before it is staged for senior-admin approval?
- 场景：An Administrator submits a deletion request (user ID); the system must check whether the request is valid before proceeding to approval staging.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already specifies the same obligation: the system validates the deletion request and stages it for senior-admin approval. Therefore the draft is covered by an original FR.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must validate a user deletion request before staging it for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a87c738426c2
- 主题：Stage deletion request for senior-admin approval
- 审查问题：Is staging the deletion request for senior-admin approval an applicable operation in the user deletion workflow?
- 场景：After validation, an Administrator's deletion request must be held pending senior-admin approval rather than deleted immediately.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already states that the system validates the request, stages it for senior-admin approval, and deletes the record upon approval, which is equivalent to staging a validated deletion request for senior-admin approval before deletion occurs.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must stage a validated user deletion request for senior-admin approval before deletion occurs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-539cbfe5b7e2
- 主题：Delete user record upon approval
- 审查问题：Should the system delete the user record only upon senior-admin approval as part of the user deletion workflow?
- 场景：A senior admin approves the staged deletion request; the system then removes the user record and marks it Deleted.
- 模型初步去向：covered
- 模型解释：FRBLOCK-010 already specifies the equivalent obligation: the deletion request is staged for senior-admin approval and the record is deleted upon approval. The nominated draft therefore duplicates an existing original FR, rather than adding a new in-scope business obligation.
- 原文证据 FR：FRBLOCK-010
- 全文已检查 FR 数：27
- 草案：The system must delete the user record after senior-admin approval and set its status to Deleted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-df96e4190369
- 主题：Define Workflows
- 审查问题：Does the documented define->validate->stage->approve->activate workflow require an update operation for an existing workflow definition?
- 场景：An administrator has previously defined a workflow, and business rules change so node order, approvers, or conditions need to be edited without creating a duplicate workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states an equivalent obligation: administrators modify existing workflows, changes are validated, staged for senior-admin approval, and the workflow is updated upon approval. This covers the nominated workflow-definition update operation.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to support updating an existing workflow definition, with changes revalidated and staged for senior-admin approval before activation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-47fdf93806dd
- 主题：Validate Configuration Details
- 审查问题：Should validation be invokable as a standalone operation before staging, so administrators can read validation results and correct errors?
- 场景：An administrator enters workflow configuration details and wants to validate them without immediately submitting the setup for senior-admin approval.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-011 supports only that the system validates configuration details as part of workflow setup before staging. The nomination asks for validation to be invokable as a standalone operation before staging so administrators can read results and correct errors; that standalone pre-staging capability is not stated or supported by the cited evidence or any checked original FR.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to provide a validation operation for workflow configuration details that returns success or error information to the administrator before staging.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-742c691e5835
- 主题：Stage Setup for Approval
- 审查问题：Does the senior-admin approval workflow require a read operation for reviewing the staged setup before approval?
- 场景：A senior admin receives a pending approval request and needs to inspect the staged node order, approvers, and conditions before deciding.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already stages the request for admin review, which entails enabling the admin to review/view the staged setup before approval. This is equivalent to the nominated read/view obligation, so the draft is covered by an original FR.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to allow senior admins to read/view the staged workflow configuration as part of the approval workflow.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3ab3eed55a39
- 主题：Senior Admin Approval Event
- 审查问题：What operation records a senior admin's approval decision on a staged workflow configuration to trigger activation?
- 场景：A senior admin reviews a staged workflow and approves it; the system must capture that approval and transition the workflow toward activation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-011 already requires staging the workflow setup for senior-admin approval and activating the workflow upon approval; FRBLOCK-014 similarly stages workflow changes for senior-admin approval and updates the workflow upon approval. This is equivalent to the nominated senior-admin approval operation triggering activation/update, so no new obligation is needed.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to provide a senior-admin approval operation that records the decision and supports the activation step.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2ff8ae9732b9
- 主题：Activate Workflow
- 审查问题：Does the workflow lifecycle require a deactivation or retirement operation after a workflow has been activated?
- 场景：An activated workflow is superseded or must be stopped, and an administrator needs to deactivate it while preserving its configuration and history.
- 模型初步去向：unsupported
- 模型解释：The only documented workflow lifecycle evidence, FRBLOCK-011, states that the system activates the workflow upon approval. No original FR specifies deactivating or retiring an active workflow, nor preserving configuration and audit history during deactivation. The draft therefore introduces a policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to support deactivating an active workflow without deleting its configuration or audit history.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d22a3b987107
- 主题：Workflow Configured
- 审查问题：Should the system support a read operation to retrieve a workflow's configuration and status after it reaches Configured?
- 场景：Administrators need to verify that a workflow is configured and view its node order, approvers, and conditions after approval and activation.
- 模型初步去向：unsupported
- 模型解释：The checked original FRs, including FRBLOCK-011, describe defining, validating, staging, activating, and storing workflows with status 'Configured,' but none specify a read/retrieval operation for a configured workflow's configuration or status. The draft therefore introduces an authorized read-access obligation not supported by the source evidence.
- 原文证据 FR：FRBLOCK-011
- 全文已检查 FR 数：27
- 草案：The system may need to allow authorized users to read a configured workflow's details and status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-519ff8239204
- 主题：Approval-start request
- 审查问题：Is an operation to submit an approval-start request applicable in this workflow?
- 场景：A user initiates an approval process for asset registration, usage, transfer, or return by providing an asset ID and operation type.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already specifies an approval-start request with asset ID and operation type, which is equivalent to the nominated draft obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should provide an operation for users to submit an approval-start request containing the asset ID and operation type.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6aa0b9e20059
- 主题：Validate approval-start request
- 审查问题：Is a validation operation applicable to an approval-start request before it is staged for review?
- 场景：After a user submits an approval-start request, the system must validate it before administrator review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system validates the request and stages it for admin review, which is equivalent to validating an approval-start request before staging it for administrator review. The nomination is therefore already covered by an original FR.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should validate approval-start requests before staging them for administrator review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-66376de2ce05
- 主题：Request staged for admin review
- 审查问题：Is an operation to stage an approval request for admin review applicable?
- 场景：A validated approval-start request is held in a staged state awaiting administrator action.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already requires the system to validate the request, stage it for admin review, and execute it upon approval, which is equivalent to staging validated approval-start requests for administrator review.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should stage validated approval-start requests for administrator review.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f028dececedc
- 主题：Administrator
- 审查问题：Is an operation for an administrator to review a staged approval request applicable?
- 场景：An administrator reviews an approval request that has been staged, and the system executes the requested operation upon approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already states that the system stages the request for admin review and executes the operation upon approval, which is equivalent to providing an administrator operation to review a staged approval request and record an approval decision. Other original FRs also cover staged admin approval.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should provide an operation for administrators to review staged approval requests and record an approval decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9c27061b3c8e
- 主题：Operation executed upon approval
- 审查问题：Is an operation to execute the requested registration, usage, transfer, or return after approval applicable?
- 场景：After an administrator approves a staged request, the system executes the corresponding asset operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already specifies that the system stages the request for admin review and executes the operation upon approval, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should execute the requested operation upon administrator approval of the staged request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-98828fcbc31e
- 主题：Approval-process record
- 审查问题：Is an operation to create an approval-process record applicable when an approval process starts?
- 场景：When a user initiates an approval process, the system outputs an approval-process record for tracking.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already specifies that an approval-start request produces an approval-process record as output, which is equivalent to the draft obligation to create an approval-process record when an approval-start request is submitted.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should create an approval-process record when an approval-start request is submitted.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a6b8d328561f
- 主题：Updated operation status
- 审查问题：Is an operation to update operation status applicable during the approval workflow?
- 场景：The system outputs an updated operation status to reflect the current state of the requested operation as it moves through approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-012 already requires that the approval process output an updated operation status, which is equivalent to updating operation status as the approval workflow progresses. The nomination is therefore covered by an existing original FR and does not need a new supplement.
- 原文证据 FR：FRBLOCK-012
- 全文已检查 FR 数：27
- 草案：The system should update operation status as the approval process progresses and upon execution.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4a7c26d026e3
- 主题：Search Criteria
- 审查问题：Does the Query Approval Status workflow require a dedicated search operation that accepts asset ID, operation type, and user ID to locate approval status records?
- 场景：A user needs to find the approval status of a specific asset or user operation by entering the asset ID, operation type, and user ID.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 already defines a Query Approval Status workflow whose input is search criteria consisting of asset ID, operation type, and user ID, which is equivalent to the nominated search operation requirement.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system must provide a search operation for approval status using asset ID, operation type, and user ID.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-19b48a1bc782
- 主题：Approval Status Details
- 审查问题：Does the workflow require an operation to retrieve the complete approval status details for a selected operation?
- 场景：After a search, the user selects an operation and needs to view its detailed approval status information.
- 模型初步去向：covered
- 模型解释：FRBLOCK-013 (FR-13 Query Approval Status) already specifies that users check operational status and that the output is approval status details, using search criteria that can identify the operation. This is equivalent to allowing retrieval of approval status details for a selected operation. The nominated draft obligation is therefore already covered by an original FR.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system must allow retrieval of approval status details for a selected operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-032892b7f6ef
- 主题：Pending Operation Status
- 审查问题：Does the workflow require a query operation that filters approval status records by status (pending, in progress, approved, or rejected)?
- 场景：A user wants to list only operations that are currently pending, in progress, approved, or rejected.
- 模型初步去向：unsupported
- 模型解释：The draft requires filtering approval status queries by operation status, but the cited FRBLOCK-013 only lists status values and otherwise uses asset ID, operation type, and user ID as search criteria. No screened original FR specifies filtering approval status records by pending, in progress, approved, or rejected status, so the obligation introduces a policy not supported by the source requirements.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system must support filtering approval status queries by operation status.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-89574a809b4c
- 主题：Query Approval Status
- 审查问题：Does the Query Approval Status function need to support pagination or sorting when returning approval status details?
- 场景：A user queries approval status for many operations and needs to navigate or sort the results.
- 模型初步去向：unsupported
- 模型解释：The only relevant original FR (FR-13/FRBLOCK-013) establishes a Query Approval Status function but does not specify pagination or sorting of results. No checked FR states an equivalent obligation, and the draft's mandatory pagination/sorting requirement is not supported by the source material.
- 原文证据 FR：FRBLOCK-013
- 全文已检查 FR 数：27
- 草案：The system must allow pagination and sorting of approval status query results.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fecc4ed301f7
- 主题：Modify existing workflows
- 审查问题：Should the workflow support an operation for an administrator to modify an existing workflow?
- 场景：An administrator needs to change nodes, approvers, or conditions in an existing workflow and submits the workflow-edit form.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that administrators modify existing workflows and specifies the workflow-edit form as input, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall provide an operation for administrators to modify an existing workflow via the workflow-edit form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0405f5fe8208
- 主题：Validate changes
- 审查问题：Should the workflow-edit operation validate submitted changes before staging them for approval?
- 场景：An administrator submits updated nodes, approvers, or conditions that may violate workflow rules.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already specifies that the system validates changes and stages them for senior-admin approval, which is equivalent to validating workflow-edit changes before staging them for approval.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall validate workflow-edit changes before staging them for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-136d9881e0fc
- 主题：Stage for senior-admin approval
- 审查问题：Should validated workflow modifications be staged as a pending approval operation?
- 场景：An administrator submits a valid edit to an existing workflow, and the change must await senior-admin review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that the system validates workflow changes, stages them for senior-admin approval, and updates the workflow upon approval, which is equivalent to staging validated workflow modifications for senior-admin approval.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall stage validated workflow modifications for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-48491ac08e5a
- 主题：Senior-admin approval
- 审查问题：Should the senior-admin approval step be supported by an explicit approval operation on staged workflow edits?
- 场景：A senior administrator reviews a staged workflow edit and needs to approve or reject it.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already specifies that staged workflow edits undergo senior-admin approval and are updated upon approval, which is equivalent to the nominated obligation for a senior-admin approval operation on staged workflow modifications. FRBLOCK-011 and FRBLOCK-027 also describe the same senior-admin approval step for staged workflow changes.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall provide a senior-admin operation to approve staged workflow modifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d924e79bcdeb
- 主题：Update workflow upon approval
- 审查问题：Should the system apply the staged workflow changes as an update operation upon senior-admin approval?
- 场景：A senior administrator approves a staged workflow edit, and the pending changes must become effective.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that changes are staged for senior-admin approval and the workflow is updated upon approval, which is equivalent to applying approved staged workflow changes as an update operation. FRBLOCK-011 also covers staging workflow setup for senior-admin approval and activating the workflow upon approval.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall update the workflow with approved changes upon senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-478322edfe89
- 主题：Modified workflow status
- 审查问题：Should the update operation set the workflow status to Modified after approved changes are applied?
- 场景：A senior administrator approves a staged workflow edit, and the updated workflow needs a clear status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-014 already states that an approved workflow edit updates the workflow and produces an output workflow with status “Modified,” which is equivalent to setting the workflow status to Modified after approved workflow changes are applied.
- 原文证据 FR：FRBLOCK-014
- 全文已检查 FR 数：27
- 草案：The system shall set the workflow status to Modified after applying approved workflow changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1addb8092dfa
- 主题：Generate Report
- 审查问题：Should 'Generate Report' be explicitly modeled as an operation with validated parameters as preconditions and stored report data plus generated file as postconditions?
- 场景：A user submits valid report parameters and the system must produce a report file and store the data; the FR describes generation but does not name an operation boundary.
- 模型初步去向：covered
- 模型解释：FRBLOCK-015 already specifies validated report parameters, report generation/storage, and stored report data plus generated file, which is equivalent to the nominated Generate Report operation obligation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall provide a Generate Report operation that accepts validated report parameters and produces a stored report and generated file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f5808b188c59
- 主题：Validate Parameters
- 审查问题：Should 'Validate Parameters' be defined as a separate operation that runs before generation, with explicit rules for date range and filters?
- 场景：A user submits report parameters including a date range and filters; the system must reject invalid parameters before generating the report.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-015 already states that the system validates parameters and that inputs include date range and filters, so the draft obligation to validate report parameters before generation is equivalent to the existing FR. The nomination's added emphasis on a separate operation or explicit rules is either implied by the existing validation step or a design detail, not a new business obligation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall validate report parameters against defined date-range and filter rules before generating a report.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-070f4a515a2d
- 主题：Store Report Data
- 审查问题：Should 'Store Report Data' be modeled as an operation that persists the generated report data and associates it with the generated file?
- 场景：After a report is generated, the system must store the report data and make the generated Excel/PDF file available.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-015 supports storing report data and outputting stored data with a generated file, but it does not support an obligation to associate the stored report data with the generated file. The draft adds this association requirement without evidence from the checked original FRs.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall store generated report data and associate it with the generated file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0ebb4544e449
- 主题：Report Parameters
- 审查问题：Does the workflow require an operation to capture or submit 'Report Parameters' (e.g., Submit Report Parameters) before validation?
- 场景：A user provides date range and filters as input to the report generation workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-015 already specifies report parameters (date range, filters) as an input and validates them, which is equivalent to accepting/capturing report parameters before validation. The draft adds no new business obligation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall accept report parameters including date range and filters from the user.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a0d23b5c2bd1
- 主题：Stored Report Data and Generated File
- 审查问题：Should an operation be defined to retrieve or download 'Stored Report Data and Generated File' after the report is generated?
- 场景：A user needs to access the stored report data and generated Excel/PDF file after generation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already requires the system to validate the request, prepare the file, and provide a download link for report export, which covers making the generated report file available for retrieval/download after report generation.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall make stored report data and generated file available for retrieval after report generation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7784438203ac
- 主题：User
- 审查问题：Should the user's action 'create reports' be modeled as an operation (e.g., Create Report Request) that triggers validation, generation, and storage?
- 场景：A user initiates a report creation request by providing report parameters.
- 模型初步去向：covered
- 模型解释：FRBLOCK-015 already states that users create reports and that the system validates parameters, generates the report, and stores the data, which covers the nominated obligation for a user to initiate a report creation request with report parameters.
- 原文证据 FR：FRBLOCK-015
- 全文已检查 FR 数：27
- 草案：The system shall allow a user to initiate a report creation request with report parameters.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1c99c9b8989b
- 主题：Validate Request
- 审查问题：Should the Validate Request operation verify that the selected report exists and that the requested export format is one of the supported formats (CSV or Excel) before proceeding?
- 场景：A user requests export of a report that no longer exists or requests an unsupported export format.
- 模型初步去向：covered
- 模型解释：FRBLOCK-016 already states that users export existing reports; the system validates the request, prepares the file, and provides a download link. Its input is explicitly the selected report and export format (CSV, Excel), which covers validating the selected report's existence and the requested format against CSV/Excel before preparing the file.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system should validate the selected report's existence and the requested export format against CSV and Excel before preparing the file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fd651e5f4780
- 主题：Prepare File
- 审查问题：Should the Prepare File operation generate the export file in the exact format selected by the user, rather than defaulting to one format?
- 场景：A user selects Excel as the export format but the system prepares a CSV file.
- 模型初步去向：covered
- 模型解释：The checked original FRBLOCK-016 already specifies that the Prepare File operation takes the selected report and export format (CSV, Excel) as input and prepares the file, which is equivalent to the nominated obligation to generate the export file in the user-selected format.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system should prepare the export file in the user-selected format (CSV or Excel).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f1510f26f367
- 主题：Provide Download Link
- 审查问题：Should the Provide Download Link operation restrict the download link to the user who requested the export?
- 场景：A user shares a generated download link with another user who did not request the export.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-016 and FRBLOCK-018 describe exporting/generating a report and providing a download link, but neither states that the link must be restricted to the user who requested the export. The draft introduces an access-control policy not supported by the supplied evidence or original FRs.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system should provide the download link only to the user who requested the export.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4776a2385047
- 主题：Export Report
- 审查问题：Should the Export Report operation support exporting only one selected report per request, or is batch export required?
- 场景：A user attempts to select multiple reports for a single export request.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-016 already defines the Export Report operation as taking a single selected report and export format as input and producing one downloadable report file. This is equivalent to supporting export of one selected report per request, and no batch export is specified.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system should support export of a single selected report per request unless batch export is explicitly required.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7f5dbf742a8e
- 主题：Export Report
- 审查问题：Should the Export Report operation create an export log entry for every export attempt, including failed validation?
- 场景：A user requests an export but validation fails before a file is prepared.
- 模型初步去向：unsupported
- 模型解释：The checked FRs mention an export log only as an output for report/data export (FRBLOCK-016 and FRBLOCK-018). Neither establishes an obligation to log every export attempt, and neither addresses failed validation. The draft therefore adds a policy not supported by the source text.
- 原文证据 FR：FRBLOCK-016
- 全文已检查 FR 数：27
- 草案：The system should create an export log entry for every export attempt, including failed validation, unless logging only successful exports is specified.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4d3894584b05
- 主题：Validate Format and Data
- 审查问题：Should validation of format and data occur as a distinct operation before any rows are parsed and stored, and should a validation failure prevent the import from storing records?
- 场景：A user uploads a CSV file whose header format is invalid; the system needs to know whether to stop the import or continue with row parsing and storage.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already states that the system validates format and data, parses rows, and stores valid records with an error report. This covers the nominated obligation that validation occurs before parsing/storage, that validation failures are reported, and that invalid records are not stored.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The import operation shall perform format and data validation before parsing and storage, and shall produce an error report for validation failures.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-94eef8106cdb
- 主题：Store Valid Records
- 审查问题：Should the import operation only create new asset records, or can it also update or skip existing asset records when a valid record matches an existing asset?
- 场景：A user imports a CSV containing an asset ID that already exists; the system must decide whether to create a duplicate, update the existing asset, or reject the row.
- 模型初步去向：retained
- 模型解释：FRBLOCK-017 establishes an in-scope import operation that stores valid records, but it does not specify how valid imported records matching existing assets are handled. No other original FR states an equivalent obligation. The draft clarifies this missing import matching behavior.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The import operation shall define how valid records matching existing assets are handled, such as create, update, skip, or reject.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-97b94a480f30
- 主题：Parse Rows
- 审查问题：Should row parsing be a separate operation that produces an intermediate parsed-row set before validation and storage, so that invalid rows can be excluded while valid rows proceed?
- 场景：A user uploads a file where some rows have missing required fields; the system must decide whether parsing succeeds partially and valid rows are stored while invalid rows appear in the error report.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already states the equivalent obligation: the system parses rows and stores valid records with an error report, which covers parsing rows, separating valid from invalid records, storing valid records, and reporting invalid ones.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The import operation shall parse rows and separate valid from invalid records, storing only valid records and reporting invalid ones.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c42cfa59ce27
- 主题：User
- 审查问题：Should the user be able to trigger the import operation and receive the error report as part of the same workflow?
- 场景：A user uploads a CSV/Excel file and expects to see which rows failed; the system must decide whether the user receives the error report after the import completes.
- 模型初步去向：covered
- 模型解释：FRBLOCK-017 already specifies the same obligation: users upload CSV/Excel files, the system validates/parses/stores valid records, and the output includes imported asset records and an error report. This covers triggering the import operation and receiving the resulting outcome, including the error report.
- 原文证据 FR：FRBLOCK-017
- 全文已检查 FR 数：27
- 草案：The import operation shall allow the user to upload a file and receive the resulting import outcome, including the error report.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4a23d8d4f44b
- 主题：Validate Export Request
- 审查问题：Should the system validate the export request before generating the export file?
- 场景：A user selects assets and chooses CSV or Excel as the export format; before any file is generated, the request must be checked for a valid format and valid selected assets.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-018 already states that the system validates the request, with selected assets and export format as inputs, before generating the file and providing a download link. This is equivalent to the nominated obligation to validate the export request before generating the export file.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must validate the export request, including selected assets and export format, before generating the export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a8c495996eec
- 主题：Generate Export File
- 审查问题：Should the system generate the export file after a valid export request?
- 场景：A user submits a valid export request with selected assets and CSV format; the next observable workflow step is creation of the downloadable file.
- 模型初步去向：covered
- 模型解释：The checked original FR FRBLOCK-018 already states that the system validates the export request, generates the file, and provides a download link, with export format (CSV, Excel) as input. That is equivalent to the draft obligation to generate the export file in the requested format after validation succeeds.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must generate the export file in the requested format after validation succeeds.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a6386ac728fb
- 主题：Provide Download Link
- 审查问题：Should the system provide a download link once the export file has been generated?
- 场景：After the system generates the export file, the user needs a way to retrieve the file; the FR states that the system provides a download link.
- 模型初步去向：covered
- 模型解释：The checked original FRs already contain an equivalent obligation. FRBLOCK-018 states that the system validates the request, generates the file, and provides a download link, and FRBLOCK-016 also states the system provides a download link after preparing the export file. Therefore the draft obligation is covered, not retained.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must provide a download link for the generated export file.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-484dc8d675b2
- 主题：Export Asset Data
- 审查问题：Should users be able to export selected asset data in CSV or Excel?
- 场景：A user selects one or more assets and chooses CSV or Excel; this begins the documented export workflow.
- 模型初步去向：covered
- 模型解释：FRBLOCK-018 already states the equivalent obligation: users export selected asset data, with CSV and Excel explicitly named as export format inputs. Therefore the nominated draft is covered by an original FR.
- 原文证据 FR：FRBLOCK-018
- 全文已检查 FR 数：27
- 草案：The system must allow users to export selected asset data in CSV or Excel.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8ed7d441ef9d
- 主题：Assign management permissions
- 审查问题：Should the documented administrator workflow define a specific assignment operation for management permissions, rather than assuming full CRUD on permissions?
- 场景：An administrator fills the permission form with a user ID and permission level; the system must decide whether this action is an update to existing permissions, a new assignment request, or another operation before staging for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies that administrators assign management permissions using a permission form, with validation and staging for senior-admin approval. This is equivalent to the draft obligation to provide an administrator operation for submitting a management permission assignment request via the permission form.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must provide an operation for an administrator to submit a management permission assignment request using the permission form.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fdfe426ad59f
- 主题：Validate permission request
- 审查问题：Should the validation step described in the workflow be modeled as a distinct operation that the system performs before staging the request for senior-admin approval?
- 场景：An administrator submits a permission form; the system validates the request and, if valid, stages it for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that the system validates the request and stages it for senior-admin approval, which is equivalent to the drafted obligation to validate a submitted permission request before staging it for senior-admin approval.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must perform a validation operation on a submitted permission request before the request can be staged for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3d6293441b29
- 主题：Stage for senior-admin approval
- 审查问题：Does the workflow require an explicit staging operation to place a validated permission request into a pending senior-admin approval queue?
- 场景：After validation, the permission request is not applied immediately; it must wait for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that the system validates the request, stages it for senior-admin approval, and updates permissions upon approval. This is equivalent to the nominated obligation to stage a validated permission request for senior-admin approval, so the draft is covered by an original FR.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must provide an operation to stage a validated permission request for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8a9596024fb7
- 主题：Senior-admin approval
- 审查问题：Should the approval event have a corresponding senior-admin decision operation (approve or reject) that releases the staged permission update?
- 场景：A permission request is staged; a senior-admin reviews it and approves, after which the system updates permissions.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies that a staged permission request requires senior-admin approval and that permissions are updated upon approval, which is equivalent to the nominated senior-admin decision operation releasing the staged permission update.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must provide a senior-admin approval operation that determines whether a staged permission request proceeds to applied permissions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6f2d66e9146b
- 主题：Update permissions upon approval
- 审查问题：Should the system expose an update operation that applies the staged permission changes only after senior-admin approval?
- 场景：The permission request has been validated and staged; upon senior-admin approval, the system updates the user's permissions and sets the output status.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that the system validates the request, stages it for senior-admin approval, and updates permissions upon approval, which is equivalent to the nominated obligation to provide a permission-update operation after senior-admin approval of a staged request.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must provide an operation to update user permissions after senior-admin approval of a staged request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-49179b44501b
- 主题：Permissions Set
- 审查问题：Does the workflow require a status-setting operation that transitions the permission request to 'Permissions Set' after the update is applied?
- 场景：After senior-admin approval and permission update, the output reports updated permissions with status 'Permissions Set.'
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already specifies the equivalent obligation: after approval, updated permissions have status “Permissions Set.” Therefore the nominated status-setting operation is covered by an original FR.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must provide an operation to set the permission request outcome to 'Permissions Set' after approved permissions are applied.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-74dbe5d3f053
- 主题：Administrators
- 审查问题：Should the assign-management-permissions operation be restricted to the administrator actor as documented, without requiring separate create/read/update/delete operations for every permission record?
- 场景：An administrator uses the permission form to request a permission assignment; the request then follows validation, staging, and senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that Administrators assign management permissions, which directly covers the draft obligation that the Administrators actor can initiate a management permission assignment operation.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must allow the Administrators actor to initiate a management permission assignment operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e3abe996a085
- 主题：Senior-admin
- 审查问题：Should the senior-admin actor have a specific approval operation in the permission workflow, rather than being treated only as an isolated role?
- 场景：A validated permission request is staged for senior-admin approval; senior-admin must be able to act on it for the workflow to proceed.
- 模型初步去向：covered
- 模型解释：FRBLOCK-019 already states that permission requests are staged for senior-admin approval and that permissions are updated upon approval, which is equivalent to the nominated obligation allowing the Senior-admin actor to perform the approval operation for staged permission requests.
- 原文证据 FR：FRBLOCK-019
- 全文已检查 FR 数：27
- 草案：The system must allow the Senior-admin actor to perform the approval operation for staged permission requests.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0342a9da2adf
- 主题：Validate replacement request
- 审查问题：What validation operation applies to a replacement request before it is staged for approval?
- 场景：A senior administrator submits a replacement form with current admin ID and new admin info.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that the system validates the request and stages it for top-level approval, which is equivalent to the nominated obligation to validate a replacement request before staging it for approval.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must validate the replacement request before staging it for top-level approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b70f58fbb0b6
- 主题：Stage replacement request for approval
- 审查问题：What operation stages a validated replacement request for top-level approval, and what status does the staged request have?
- 场景：The system has validated a replacement request but it has not yet been approved.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states the equivalent obligation: the system stages a validated replacement request for top-level approval before the admin record is updated upon approval. The draft obligation matches this staging operation. The question's additional status detail for the staged request is not part of the draft obligation and is not specified by the cited evidence, so no new business obligation is introduced.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must stage validated replacement requests for top-level approval before they can update admin records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1196292a28d7
- 主题：Update admin records
- 审查问题：What specific admin record update operation occurs after top-level approval, and which fields are changed?
- 场景：Top-level approval is granted for a staged replacement request.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already specifies that a staged replacement request is approved at top level and the system then updates admin records upon approval, producing an updated admin record with status “Replaced.” This is equivalent to the draft obligation to update the admin record after top-level approval to reflect the replacement.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must update the admin record after top-level approval to reflect the replacement.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a7b865be756f
- 主题：Top-level approval
- 审查问题：Is top-level approval an operation or event that the system must capture to authorize the admin record update?
- 场景：A validated replacement request is staged and awaits top-level approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already specifies that the request is staged for top-level approval and admin records are updated upon approval, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must capture top-level approval before updating admin records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-437f7d193091
- 主题：Admin record status replaced
- 审查问题：Does the update operation set the admin record status to 'Replaced' as part of the same workflow step?
- 场景：A replacement request has been approved and the system updates the admin record.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 explicitly specifies an updated admin record with status “Replaced” upon approval, which is equivalent to the nominated obligation to set the admin record status to 'Replaced' when applying an approved replacement.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：The system must set the admin record status to 'Replaced' when applying an approved replacement.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2d7549fa4011
- 主题：Senior administrators
- 审查问题：Which replacement operation can senior administrators initiate, and does it require a submitted replacement form?
- 场景：A senior administrator initiates replacement of the current system admin.
- 模型初步去向：covered
- 模型解释：FRBLOCK-020 already states that senior administrators replace the current system admin, which is equivalent to authorizing senior administrators to initiate the replacement operation for the current system admin. The draft adds no distinct in-scope obligation.
- 原文证据 FR：FRBLOCK-020
- 全文已检查 FR 数：27
- 草案：Senior administrators must be authorized to initiate the replacement operation for the current system admin.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c99df48e3eac
- 主题：Submit Asset Request
- 审查问题：What trigger, actor, and entry conditions must be documented for the asset request submission operation so that the workflow from 'Users request assets' is operable?
- 场景：A user initiates an asset request; without a defined trigger and authorized actor, requests may be submitted inconsistently or bypass validation and staging.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-021 only states that users request assets; it does not require a documented asset request submission operation, nor does it define its trigger, authorized actor, or entry conditions. The draft adds documentation and entry-condition requirements not present in the original FRs, so it is unsupported rather than retained or covered.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must provide a documented asset request submission operation that an authorized user can trigger according to the defined entry conditions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-61dbeac78878
- 主题：Validate Asset Request
- 审查问题：Which validation rules and failure behavior should apply when the system validates an asset request before staging it for admin approval?
- 场景：A user submits an asset request with invalid or missing name, type, quantity, or purpose; the validation operation must decide whether to reject or route it for correction.
- 模型初步去向：retained
- 模型解释：FRBLOCK-021 only establishes that the system validates the request before staging for admin approval; it does not specify validation criteria or failure behavior. The nomination is in scope for asset-request validation and adds a supported obligation to validate against documented criteria and handle failures before staging, which no original FR covers.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must validate the asset request against documented criteria and handle validation failures before staging for approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d363c885e196
- 主题：Stage for Admin Approval
- 审查问题：What does the staging operation require in terms of admin identity, notification, and data visibility before an admin approval decision is made?
- 场景：A validated asset request is staged; if the staging operation lacks a defined admin recipient or review state, it may remain unprocessed.
- 模型初步去向：covered
- 模型解释：Original FRs already specify staging validated requests for admin approval and approval/rejection (e.g., FRBLOCK-004, FRBLOCK-021, FRBLOCK-022), so the draft obligation is equivalent to existing obligations and does not require a new supplement.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must stage validated asset requests in a state accessible to an authorized admin for approval or rejection.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6bc757fa9f75
- 主题：Update Status on Approval
- 审查问题：How should the status update operation distinguish between an approval and a rejection decision, and what status value must be recorded for each outcome?
- 场景：An admin approves or rejects a staged asset request; the update operation must set the correct status and preserve the decision.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies that the stored request status is set to “Approved” or “Rejected,” and its screening marks the nominated approval/rejection status update obligation as covered.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must update the stored request status to Approved or Rejected based on the admin's decision.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2f803be801cd
- 主题：Stored Request
- 审查问题：What persistence and retrieval requirements must the stored request operation satisfy so that status 'Approved' or 'Rejected' remains available after the workflow completes?
- 场景：A request has been approved or rejected; the system must retain the request and its final status for later reference or audit.
- 模型初步去向：covered
- 模型解释：FRBLOCK-021 already specifies a stored request with status “Approved” or “Rejected,” which covers the draft obligation to persist the asset request and its final status as retrievable data after approval or rejection.
- 原文证据 FR：FRBLOCK-021
- 全文已检查 FR 数：27
- 草案：The system must persist the asset request and its final status as retrievable data after approval or rejection.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c8a69c3629e1
- 主题：Approve Asset Request
- 审查问题：Should the Approve Asset Request operation handle both approval and rejection as one decision operation, or should rejection be modeled as a separate operation?
- 场景：An administrator reviews a pending asset request and selects reject with a reason; the system must record the rejection decision and proceed to status update and notification.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators review and approve or reject asset requests, which is equivalent to providing a single asset-request decision operation that accepts either an approve or reject decision.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must provide an asset-request decision operation that accepts an approve or reject decision from an administrator.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1bef665124e7
- 主题：Update Request Status
- 审查问题：Should the Update Request Status operation run immediately upon decision submission and persist the status even if user notification later fails?
- 场景：An administrator approves an asset request; the system updates the request status to approved, but the notification service is temporarily unavailable.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-022 only states that the system updates the request status and notifies users. It does not establish that the status update must persist independently of notification delivery or survive a later notification failure. The draft therefore adds a failure-isolation policy not supported by the checked original FRs.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must persist the updated request status when an administrator submits a decision, independent of notification delivery.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-eacf99a26cfc
- 主题：Notify Users
- 审查问题：Should the Notify Users operation be triggered for every decision outcome, including both approval and rejection?
- 场景：An administrator rejects an asset request; the requesting user should receive a notification about the rejection.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that administrators review and approve or reject asset requests and the system updates the request status and notifies users, which covers notification for both approval and rejection outcomes.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must notify the requesting user whenever an administrator approves or rejects an asset request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-8aa100f9fb69
- 主题：Administrators
- 审查问题：Should the approve/reject operation be restricted to the Administrators actor, and what authorization check must occur before the decision is applied?
- 场景：A non-administrator attempts to submit an approval decision for an asset request; the system should deny the operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-022 already states that Administrators review and approve or reject asset requests, which is equivalent to restricting the asset-request approve/reject operation to Administrators.
- 原文证据 FR：FRBLOCK-022
- 全文已检查 FR 数：27
- 草案：The system must authorize only Administrators to perform the asset-request approve/reject operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-aa71838ad799
- 主题：Send Email Notification
- 审查问题：Does the Send Email Notification operation need a documented trigger policy for event types beyond registration and profile updates?
- 场景：A new event type such as password reset occurs, and the workflow must decide whether an email notification is automatically sent.
- 模型初步去向：retained
- 模型解释：FRBLOCK-023 supports that automatic email notifications are sent, but its screening shows it only covers examples such as registration and profile updates and does not define a trigger policy for other event types. No checked original FR states an equivalent obligation to define which event types trigger automatic notifications, and the Send Email Notification operation is in scope. This is therefore a retained gap.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD define which event types trigger automatic email notifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-17cc05402162
- 主题：Registration Event
- 审查问题：Should the system support an operation to re-send a notification when a Registration Event is reprocessed?
- 场景：A registration event is received twice due to a retry from an upstream system.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-023 only requires automatic email notifications for events such as registration/profile updates and a sent email log. No checked original FR specifies idempotent notification delivery, duplicate suppression, or behavior for repeated/reprocessed Registration Events. The draft therefore introduces an unsupported policy rather than restating an existing obligation.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD make notification delivery idempotent for repeated Registration Events or log duplicate suppression.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-dc0d4816ef2d
- 主题：Profile Update Event
- 审查问题：Should the system support an operation to re-send a notification when a Profile Update Event is reprocessed?
- 场景：A profile update event is delivered again after a transient system failure.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-023 establishes automatic email notifications for profile updates but does not specify behavior for reprocessed Profile Update Events or preventing duplicate notifications. No other screened original FR addresses duplicate-notification suppression or notification re-send semantics. The draft therefore introduces a new policy not supported by the source requirements.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD prevent unintended duplicate notifications for repeated Profile Update Events.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-66a3478a8081
- 主题：Event Details
- 审查问题：Does the workflow require an operation to validate or normalize Event Details before generating the notification content?
- 场景：Event Details contain missing or malformed fields that would produce an invalid email.
- 模型初步去向：unsupported
- 模型解释：The cited FRBLOCK-023 only states that the system automatically sends email notifications using event details and a recipient list, producing a sent email and send log. It does not require validation or normalization of Event Details before generating notification content. No screened original FR establishes an equivalent obligation, so the draft introduces a validation policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD validate required Event Details before sending an email notification.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a70fbe903513
- 主题：Recipient List
- 审查问题：Should the Recipient List be deduplicated before the Send Email Notification operation executes?
- 场景：The recipient list contains the same email address more than once for a single event.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-023 identifies the recipient list only as input to the Send Email Notification operation and does not require deduplication or avoiding duplicate notifications. The draft adds a SHOULD policy that is not stated or implied by the source FRs, so it is unsupported.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD deduplicate recipient addresses before sending to avoid duplicate notifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1ff22603207a
- 主题：Sent Email
- 审查问题：Should the system provide a resend operation for a Sent Email when delivery is later reported as failed?
- 场景：The email provider reports a bounce after a Sent Email record was created.
- 模型初步去向：retained
- 模型解释：FRBLOCK-023 establishes the outbound notification capability and Sent Email/send log records, but no original FR specifies resending a notification after a later delivery failure while preserving the original Sent Email and logging the new attempt. This is an in-scope notification obligation not covered by the checked FRs.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD support resending a notification while preserving the original Sent Email and logging the new attempt.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-973f507780ab
- 主题：Send Log
- 审查问题：Should the Send Log record both successful and failed send attempts as part of the notification operation?
- 场景：The email provider returns a temporary failure and the system retries the send.
- 模型初步去向：unsupported
- 模型解释：The only cited evidence, FRBLOCK-023, merely lists a send log as an output. It does not state that the log records every send attempt or includes failed attempts. No reviewed original FR establishes an obligation to log successful and failed notification sends, so the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-023
- 全文已检查 FR 数：27
- 草案：The system SHOULD append a Send Log entry for every send attempt, including failures.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c6713585b7b0
- 主题：Parse feedback content
- 审查问题：Should 'Parse feedback content' be reviewed as an applicable operation in the feedback intake workflow?
- 场景：FR-24 states that the system receives user email feedback, parses the content, stores it, and notifies administrators for handling. This documents parsing as a step between email receipt and storage, so its operational treatment may need explicit review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already states that the system parses the content of received user email feedback, which is equivalent to the nominated draft obligation to parse feedback email content.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must parse the content of received user feedback emails.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-72edc2023004
- 主题：Store feedback
- 审查问题：Should 'Store feedback' be reviewed as an applicable operation in the feedback handling workflow?
- 场景：FR-24 documents that after parsing the content, the system stores it and then notifies administrators. This makes storage a distinct step in the feedback workflow that may need operational review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already specifies that the system receives email feedback, parses the content, stores it, and lists stored feedback as output. This is equivalent to the draft obligation to store parsed user feedback.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must store parsed user feedback.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-94271dea1ea7
- 主题：Notify administrators
- 审查问题：Should 'Notify administrators' be reviewed as an applicable operation in the feedback handling workflow?
- 场景：FR-24 states that the system notifies administrators for handling after receiving and storing user feedback. This documents notification as a workflow step that may need operational review.
- 模型初步去向：covered
- 模型解释：FRBLOCK-024 already states that the system notifies administrators after storing feedback for handling, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-024
- 全文已检查 FR 数：27
- 草案：The system must notify administrators when user feedback is received and stored for handling.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-10239c6267ea
- 主题：View Asset Change History
- 审查问题：Should the View Asset Change History operation support sorting the returned change history by change time, and if so, what default order should be applied?
- 场景：A user queries an asset's change log expecting to review the most recent changes first; the FR describes the query but does not define result ordering.
- 模型初步去向：retained
- 模型解释：The View Asset Change History operation exists in FRBLOCK-025, but the original FR only describes query criteria and output fields; it does not specify sorting behavior or a default order. The draft obligation is therefore an in-scope gap rather than an existing obligation.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should define a default sort order (e.g., change time descending) for asset change history query results.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bdd4ed01c145
- 主题：Search Criteria
- 审查问题：Should the query operation allow combining multiple search criteria (asset ID, change type, and change date) in a single request?
- 场景：A user wants to narrow the change history to a specific asset, a specific change type, and a specific date; the FR lists criteria but does not state whether they can be combined.
- 模型初步去向：retained
- 模型解释：FRBLOCK-025 lists search criteria (asset ID, change type, date) but does not explicitly state whether multiple criteria can be combined. The draft obligation to support any combination is in-scope for asset change history queries and is not already covered by any original FR.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should support filtering asset change history by any combination of asset ID, change type, and change date.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4756f87ae918
- 主题：Change history
- 审查问题：Should the View Asset Change History operation support pagination or a maximum result limit for returned change history records?
- 场景：An asset may have a long change log; without pagination or a limit, the user may receive an unwieldy result set and system performance may degrade.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-025 is the relevant View Asset Change History requirement, but its evidence only specifies the output fields for change history records. It does not require pagination, a maximum result limit, or any equivalent control. No other original FR supports the draft obligation, so the proposed pagination/limit policy is not grounded in the source requirements.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should define pagination or a result limit for asset change history queries.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-75f30bc6faa5
- 主题：Change date
- 审查问题：Should the change date search criterion support a date range (start and end date) rather than only a single date?
- 场景：A user may need to review all changes that occurred over a period (e.g., last month); the FR mentions 'change date' but does not clarify range support.
- 模型初步去向：retained
- 模型解释：FRBLOCK-025 establishes that users query asset change logs by change date, making date-based change-history filtering in scope. No checked original FR specifies that the change date search criterion must support a start-and-end date range, so the range capability is not already covered.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should support filtering asset change history by a date range when start and end dates are provided.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fef904856305
- 主题：Change type
- 审查问题：Should the change type criterion be restricted to a defined enumeration of change types, and if so, how are those types maintained?
- 场景：Users filter by change type, but the FR does not list valid change types; undefined values could cause inconsistent filtering.
- 模型初步去向：retained
- 模型解释：FRBLOCK-025 supports change type as an asset change history query criterion but does not define or maintain the allowed change type values. No other original FR states an equivalent obligation, and the requirement is in scope for asset change history filtering.
- 原文证据 FR：FRBLOCK-025
- 全文已检查 FR 数：27
- 草案：The system should define and maintain the allowed change type values for filtering asset change history.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c76dfc2a1fee
- 主题：Query Asset Category
- 审查问题：Does the Query Asset Category operation support querying by both category name and category ID simultaneously?
- 场景：A user wants to narrow results by entering both a category name and a category ID in the search criteria.
- 模型初步去向：unsupported
- 模型解释：The only relevant original FR (FRBLOCK-026) states that users query asset categories by name or ID. It does not establish that category name and category ID can be used simultaneously as combined search criteria, so the draft adds an obligation beyond the supported source text.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should allow asset categories to be queried using both category name and category ID as combined search criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f66f7b42e455
- 主题：Category Name
- 审查问题：Does the Query Asset Category operation support partial or exact matching on Category Name?
- 场景：A user enters only part of a category name and expects matching categories to be returned.
- 模型初步去向：retained
- 模型解释：FRBLOCK-026 establishes that users can query asset categories by name or ID, so Category Name matching in asset category queries is in scope. However, it does not define whether matching is partial or exact, leaving the draft obligation as an in-scope gap not covered by the original FRs.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should define and support the matching behavior for Category Name in asset category queries.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-cc5458413151
- 主题：Category ID
- 审查问题：Does the Query Asset Category operation require an exact match on Category ID?
- 场景：A user enters a category ID that is slightly different from an existing ID to see if any results are returned.
- 模型初步去向：unsupported
- 模型解释：The evidence from FRBLOCK-026 only indicates that asset categories can be queried by name or ID. It does not establish that Category ID must be validated or that Category ID querying must use exact matching. The screening notes confirm that merely mentioning category ID does not create an exact-match obligation, so the draft introduces a policy not supported by the original requirements.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should validate Category ID and use exact matching when querying asset categories by ID.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f07b9d91aaef
- 主题：Asset Count
- 审查问题：Does the Query Asset Category operation return Asset Count for each matching category?
- 场景：A user queries a category to assess how many assets it contains before taking further action.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already specifies that the asset category query output includes category details with asset count, which is equivalent to the nominated obligation to include Asset Count in the category details returned by the asset category query operation.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should include Asset Count in the category details returned by the asset category query operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-199b67e11c28
- 主题：Category Details
- 审查问题：Does the Query Asset Category operation return Category Details including name, description, and asset count?
- 场景：A user selects a category from the query results and expects to see full details.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already specifies that viewing/querying asset categories outputs category details including name, description, and asset count, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should return Category Details comprising name, description, and asset count for each queried asset category.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-be84278507df
- 主题：Search Criteria
- 审查问题：Does the Query Asset Category operation allow an empty Search Criteria to return all categories?
- 场景：A user wants to browse all asset categories without specifying a category name or ID.
- 模型初步去向：unresolved
- 模型解释：FRBLOCK-026 confirms an in-scope Query Asset Category operation with search criteria, but it does not specify whether an empty Search Criteria returns all categories or is rejected. No other original FR defines this behavior, so the evidence is insufficient to determine the expected obligation.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should define whether an empty Search Criteria returns all asset categories or is rejected.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c3fa1888fe7e
- 主题：User
- 审查问题：Does the Query Asset Category operation require a User to be authenticated before querying asset categories?
- 场景：An unauthenticated user attempts to query asset categories by name or ID.
- 模型初步去向：unsupported
- 模型解释：The nominated evidence from FRBLOCK-026 only states that users query asset categories by name or ID and receive category details. It does not state or imply that authentication is required before performing the Query Asset Category operation. None of the checked original FRs establishes an equivalent authentication obligation for this operation, so the draft introduces a policy not supported by the source requirements.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should enforce authentication for Users performing the asset category query operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4628cdda165d
- 主题：Query Asset Category
- 审查问题：Is the Query Asset Category operation read-only, or can it modify category data as part of the workflow?
- 场景：A user performs a query and then attempts to update a category detail from the same operation.
- 模型初步去向：covered
- 模型解释：FRBLOCK-026 already specifies the View Asset Category operation as users querying asset categories by name or ID, which is equivalent to restricting Query Asset Category to viewing/querying. Modification of category data is separately handled by FRBLOCK-027 Edit Asset Category, so the draft obligation is already covered by the original FRs.
- 原文证据 FR：FRBLOCK-026
- 全文已检查 FR 数：27
- 草案：The system should restrict the Query Asset Category operation to viewing/querying and not allow category modifications.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6ea83a96fd00
- 主题：Validate changes
- 审查问题：In the Edit Asset Category workflow, should the Validate changes operation run before staging for senior-admin approval, and what validation rules apply to the category name and description?
- 场景：An administrator submits a category-edit form with a duplicate name or missing description; the system must decide whether to reject it immediately or stage it for senior-admin approval.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 already states the system validates changes, stages them for senior-admin approval, and updates the category upon approval, with the category-edit form including name and description. This covers the nominated obligation to validate category name and description before staging the edit for senior-admin approval.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The system must validate category name and description before staging an edit for senior-admin approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-14dcb4fa119f
- 主题：Senior-admin approval
- 审查问题：When Senior-admin approval is required, should the approval operation include a reject or return outcome that prevents the category update?
- 场景：A senior admin reviews a staged category edit and determines it should not be applied; the system needs a documented outcome for rejection.
- 模型初步去向：retained
- 模型解释：FRBLOCK-027 establishes senior-admin approval for staged category changes and applies the update upon approval, but it does not document a rejection/return outcome or explicitly prevent the category update when approval is denied. This is an in-scope missing approval-workflow obligation rather than an already covered requirement.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The approval operation must define both approval and rejection outcomes before any category update is applied.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b089ad769d7c
- 主题：Update Category Upon Approval
- 审查问题：After senior-admin approval, should the Update Category Upon Approval operation re-check that the staged category data is still valid before applying the update?
- 场景：The category data changes between staging and approval, and the system must avoid applying stale or conflicting edits.
- 模型初步去向：unsupported
- 模型解释：The closest source, FRBLOCK-027, only establishes that category changes are validated, staged for senior-admin approval, and updated upon approval. It does not require re-checking staged category data after approval or handling validation conflicts at commit time. The draft therefore introduces an unsupported commit-time validation/conflict-handling policy beyond the original FR.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The update operation must apply only approved category changes and handle any validation conflicts at commit time.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-dc168f2cfe53
- 主题：Staged for Approval
- 审查问题：While a category edit is Staged for Approval, should the submitting administrator be able to withdraw or cancel the staged operation before senior-admin approval?
- 场景：An administrator realizes a mistake after submitting a category edit but before senior-admin approval; the system needs a defined withdrawal operation.
- 模型初步去向：unsupported
- 模型解释：The cited evidence from FRBLOCK-027 only establishes that category edits are staged for senior-admin approval; it does not state or imply that the submitting administrator may withdraw or cancel the staged operation before approval. No other original FR screening covers or supports this withdrawal/cancellation right. The draft therefore introduces a policy not supported by the source evidence.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：Staged category edits should support cancellation or withdrawal by the submitting administrator before approval.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4d044556a99f
- 主题：Edit Asset Category
- 审查问题：Does the Edit Asset Category operation allow updates only to the documented name and description fields, or can other category data be modified?
- 场景：An administrator opens the category-edit form and the system receives fields beyond name and description; the operation scope must be clear.
- 模型初步去向：covered
- 模型解释：FRBLOCK-027 explicitly documents the category-edit form input as name and description, which already defines the editable fields for the Edit Asset Category operation and is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The edit operation should be limited to the category name and description unless additional fields are explicitly documented.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7ab44a8756e9
- 主题：Category Status Modified
- 审查问题：When the category update operation succeeds, should the system set Category Status Modified as part of the same operation and record who approved the change?
- 场景：A senior admin approves a category edit; the system applies the update and must produce the Modified status for audit and display.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-027 supports setting the updated category status to 'Modified' and staging category edits for senior-admin approval, but no original FR specifies recording or retaining who approved the change. The draft's requirement to retain the senior-admin approval record is therefore an unsupported policy addition.
- 原文证据 FR：FRBLOCK-027
- 全文已检查 FR 数：27
- 草案：The update operation must set the category status to Modified and retain the senior-admin approval record.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall define and enforce the permitted asset fields that Users may edit during an asset modification and shall allow the modification to be submitted for validation and approval.

2. [model_preliminarily_retained] The system shall stage validated asset modifications in a pending-approval state until an Admin approves or rejects the change.

3. [model_preliminarily_retained] The system shall define and apply documented matching rules for asset detail searches by name, type, and ID, specifying whether each criterion is matched exactly, partially, and/or case-insensitively.

4. [model_preliminarily_retained] The system shall define whether asset detail queries accept a single search criterion or a combination of name, type, and ID.

5. [model_preliminarily_retained] The system shall return a defined empty-result response when no asset matches the supplied search criteria.

6. [model_preliminarily_retained] The system shall return a defined complete set of asset detail fields for each matching asset record, including at least name, type, quantity, purchase date, and status.

7. [model_preliminarily_retained] The system shall provide an admin operation to reject a staged deletion request and update its status to rejected.

8. [model_preliminarily_retained] The system shall define and implement the handling of valid imported asset records that match an existing asset, specifying whether such records are created, updated, skipped, or rejected.

9. [model_preliminarily_retained] The system shall validate asset requests against documented criteria, including required name, type, quantity, and purpose, and shall handle validation failures by rejecting or routing the request for correction before staging it for admin approval.

10. [model_preliminarily_retained] The system shall define and document which event types trigger automatic email notifications, including event types beyond registration and profile updates.

11. [model_preliminarily_retained] The system shall support resending a Sent Email when delivery is later reported as failed, preserving the original Sent Email record and logging the new resend attempt.

12. [model_preliminarily_retained] The system shall sort asset change history query results by change time in descending order by default.

13. [model_preliminarily_retained] The system shall allow users to filter asset change history by any combination of asset ID, change type, and change date.

14. [model_preliminarily_retained] The system shall allow users to filter asset change history by a change date range using start and end dates when provided.

15. [model_preliminarily_retained] The system shall define and maintain an enumeration of allowed change type values used for filtering asset change history, and shall restrict the change type filter to those defined values.

16. [model_preliminarily_retained] The system shall define and support the matching behavior for Category Name in asset category queries.

17. [model_preliminarily_retained] The system shall provide both approval and rejection outcomes for senior-admin review of staged category changes, and shall not apply the category update when the senior admin rejects it.
