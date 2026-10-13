# Causal graph export — Inventory_MIRC3

- model version: `MODEL-396084324100`
- elements: 155 | extracted relations: 276
- evidence graph: 155 nodes, 276 edges (multi-edge, keeps every quotations)
- signed simulation graph: 140 nodes, 103 edges
- excluded from simulation: 51
- parameters: background log-odds -1.0, propagation strength 2.5, max parents 8

## Simulation edges

| source | → | target | sign | weight |
|---|---|---|---:|---:|
| Admin approval | → | Operation executed upon approval | positive | 0.95 |
| Admin approval | → | Update record upon approval | positive | 0.95 |
| Admin approval | → | Update status to Modified | positive | 0.95 |
| Asset Request Form | → | Submit Asset Request | positive | 0.95 |
| Delete user record upon approval | → | User record deleted status | positive | 0.95 |
| Deletes the Record upon Approval | → | Deleted | positive | 0.95 |
| New-User Form | → | Validate New-User Form | positive | 0.95 |
| Notify Users | → | User Notification | positive | 0.95 |
| Query Asset Category | → | Category Details | positive | 0.95 |
| Query Asset Details | → | Detailed Asset Information | positive | 0.95 |
| Query User Details | → | Detailed User Information | positive | 0.95 |
| Register Asset | → | Asset Registered | positive | 0.95 |
| Return Approval | → | Update Asset Status to Returned | positive | 0.95 |
| Senior Admin Approval Event | → | Activate Workflow | positive | 0.95 |
| Senior-admin approval event | → | Delete user record upon approval | positive | 0.95 |
| Store feedback | → | Stored feedback | positive | 0.95 |
| Submit Asset Request | → | Stored Request | positive | 0.95 |
| Update Asset Status to Returned | → | Asset Status Returned | positive | 0.95 |
| Update Ownership Upon Approval | → | Transferred | positive | 0.95 |
| Update Request Status | → | Updated Request Status | positive | 0.95 |
| Update permissions upon approval | → | Permissions Set | positive | 0.95 |
| Update record upon approval | → | Status Modified | positive | 0.95 |
| Update status to Modified | → | Asset record status Modified | positive | 0.95 |
| View Asset Change History | → | Change history | positive | 0.95 |
| Activate Workflow | → | Workflow Configured | positive | 0.90 |
| Admin approval | → | Deletes the Record upon Approval | positive | 0.90 |
| Admin approval | → | Update Ownership Upon Approval | positive | 0.90 |
| Admin approval | → | Update Status on Approval | positive | 0.90 |
| Approval-start request | → | Validate approval-start request | positive | 0.90 |
| Approve Asset Request | → | Notify Users | positive | 0.90 |
| Approve Asset Request | → | Update Request Status | positive | 0.90 |
| Approve Asset Request | → | Update Status on Approval | positive | 0.90 |
| Asset Registered | → | Administrators Notified | positive | 0.90 |
| Data Validation Passed | → | Asset Registered | positive | 0.90 |
| Edit and submit asset details | → | Validate modification data | positive | 0.90 |
| Event Details | → | Send Email Notification | positive | 0.90 |
| Export Asset Data | → | Downloadable Data File | positive | 0.90 |
| Export Asset Data | → | Export Log | positive | 0.90 |
| Export Report | → | Downloadable Data File | positive | 0.90 |
| Export Report | → | Export Log | positive | 0.90 |
| Export Report | → | Export Log Available | positive | 0.90 |
| Export Report | → | Report File Downloadable | positive | 0.90 |
| Generate Export File | → | Downloadable Data File | positive | 0.90 |
| Generate Report | → | Store Report Data | positive | 0.90 |
| Generate Report | → | Stored Report Data and Generated File | positive | 0.90 |
| Import Asset Data | → | Imported Asset Records | positive | 0.90 |
| Initiate Asset Return | → | Validate Return Request | positive | 0.90 |
| Operation executed upon approval | → | Approval-process record | positive | 0.90 |
| Operation executed upon approval | → | Updated operation status | positive | 0.90 |
| Profile Update Event | → | Send Email Notification | positive | 0.90 |
| Query Approval Status | → | Approval Status Details | positive | 0.90 |
| Recipient List | → | Send Email Notification | positive | 0.90 |
| Registration Event | → | Send Email Notification | positive | 0.90 |
| Report Parameters | → | Generate Report | positive | 0.90 |
| Report Parameters | → | Validate Parameters | positive | 0.90 |
| Report Selected | → | Export Report | positive | 0.90 |
| Return Form | → | Initiate Asset Return | positive | 0.90 |
| Selected Assets | → | Export Asset Data | positive | 0.90 |
| Send Email Notification | → | Send Log | positive | 0.90 |
| Send Email Notification | → | Sent Email | positive | 0.90 |
| Stage Return Request for Approval | → | Update Asset Status to Returned | positive | 0.90 |
| Staged for Admin Approval | → | Deletes the Record upon Approval | positive | 0.90 |
| Store Report Data | → | Stored Report Data and Generated File | positive | 0.90 |
| Store User | → | New User Record Activated | positive | 0.90 |
| Submit Asset Request | → | Validate Asset Request | positive | 0.90 |
| Top-level approval | → | Update admin records | positive | 0.90 |
| Transfer Asset | → | Validate Transfer Request | positive | 0.90 |
| Transfer form | → | Transfer Asset | positive | 0.90 |
| Update Category Upon Approval | → | Category Status Modified | positive | 0.90 |
| Update admin records | → | Admin record status replaced | positive | 0.90 |
| Update workflow upon approval | → | Modified workflow status | positive | 0.90 |
| Uploaded Data File | → | Import Asset Data | positive | 0.90 |
| User feedback email | → | Parse feedback content | positive | 0.90 |
| User feedback email received | → | Parse feedback content | positive | 0.90 |
| Validate Configuration Details | → | Stage Setup for Approval | positive | 0.90 |
| Validate New-User Form | → | Store User | positive | 0.90 |
| Validate Parameters | → | Generate Report | positive | 0.90 |
| Validate Return Request | → | Stage Return Request for Approval | positive | 0.90 |
| Validate approval-start request | → | Request staged for admin review | positive | 0.90 |
| Validate deletion request | → | Stage deletion request for senior-admin approval | positive | 0.90 |
| Validate modification data | → | Stage change for admin approval | positive | 0.90 |
| Validates the Request | → | Staged for Admin Approval | positive | 0.90 |
| Edit Asset Category | → | Staged for Approval | positive | 0.85 |
| Export Asset Data | → | Validate Export Request | positive | 0.85 |
| Generate Export File | → | Export Log | positive | 0.85 |
| Parse feedback content | → | Store feedback | positive | 0.85 |
| Register Asset | → | Administrators Notified | positive | 0.85 |
| Request staged for admin review | → | Operation executed upon approval | positive | 0.85 |
| Stage Setup for Approval | → | Senior Admin Approval Event | positive | 0.85 |
| Stage change for admin approval | → | Admin approval | positive | 0.85 |
| Stage deletion request for senior-admin approval | → | Senior-admin approval event | positive | 0.85 |
| Stage replacement request for approval | → | Top-level approval | positive | 0.85 |
| Staged for Admin Approval | → | Admin approval | positive | 0.85 |
| Staged for Approval | → | Update Category Upon Approval | positive | 0.85 |
| Stored Request | → | Approve Asset Request | positive | 0.85 |
| User feedback email | → | User feedback email received | positive | 0.85 |
| Valid Record | → | Store Valid Records | positive | 0.85 |
| Validate Export Request | → | Generate Export File | positive | 0.85 |
| Validate replacement request | → | Stage replacement request for approval | positive | 0.85 |
| Define Workflows | → | Validate Configuration Details | positive | 0.80 |
| Modify existing workflows | → | Validate Configuration Details | positive | 0.80 |
| Request staged for admin review | → | Admin approval | positive | 0.80 |
| Store feedback | → | Notify administrators | positive | 0.80 |

## Exclusions

| source | target | reason |
|---|---|---|
| Senior-admin approval | Update Category Upon Approval | undefined_activation_state |
| Senior-admin approval | Update permissions upon approval | undefined_activation_state |
| Administrators | Assign management permissions | undefined_activation_state |
| Administrators | Create New User Accounts | undefined_activation_state |
| Administrators | Define Workflows | undefined_activation_state |
| Administrators | Edit Asset Category | undefined_activation_state |
| Administrators | Modify existing workflows | undefined_activation_state |
| Asset ID | View Asset Change History | unspecified_sign |
| Assign management permissions | Validate permission request | unspecified_sign |
| Category ID | Query Asset Category | unspecified_sign |
| Category Name | Query Asset Category | unspecified_sign |
| Change date | View Asset Change History | unspecified_sign |
| Change type | View Asset Change History | unspecified_sign |
| Deletion Request | Validate deletion request | undefined_activation_state |
| Deletion Request | Validates the Request | undefined_activation_state |
| Modify existing workflows | Stage for senior-admin approval | undefined_activation_state |
| Search Criteria | Query Approval Status | undefined_activation_state |
| Search Criteria | Query Asset Details | undefined_activation_state |
| Senior administrators | Validate replacement request | undefined_activation_state |
| Senior-admin approval | Update workflow upon approval | undefined_activation_state |
| Stage for Admin Approval | Update Ownership Upon Approval | undefined_activation_state |
| Stage for senior-admin approval | Senior-admin approval | undefined_activation_state |
| Users | Edit User Profile | undefined_activation_state |
| Users | Edit and submit asset details | undefined_activation_state |
| Users | Export Report | undefined_activation_state |
| Users | Generate Report | undefined_activation_state |
| Users | Initiate Asset Return | undefined_activation_state |
| Users | Query Approval Status | undefined_activation_state |
| Users | Query Asset Details | undefined_activation_state |
| Users | Query User Details | undefined_activation_state |
| Users | Register Asset | undefined_activation_state |
| Users | Submit Asset Request | undefined_activation_state |
| Users | Transfer Asset | undefined_activation_state |
| Validate Transfer Request | Stage for Admin Approval | undefined_activation_state |
| Validate changes | Stage change for admin approval | undefined_activation_state |
| Administrators | Approve Asset Request | undefined_activation_state |
| Administrators | Validate deletion request | undefined_activation_state |
| Edit User Profile | Validate changes | undefined_activation_state |
| Search Criteria | Query User Details | undefined_activation_state |
| Stage for Admin Approval | Admin approval | undefined_activation_state |
| Users | Export Asset Data | undefined_activation_state |
| Users | Query Asset Category | undefined_activation_state |
| Users | Uploaded Data File | undefined_activation_state |
| Validate Asset Request | Stage for Admin Approval | undefined_activation_state |
| Validate permission request | Stage for senior-admin approval | undefined_activation_state |
| Administrators | Update Ownership Upon Approval | undefined_activation_state |
| Obsolete Asset | Deletion Request | undefined_activation_state |
| Users | Import Asset Data | undefined_activation_state |
| Validate Configuration Details | Stage for senior-admin approval | undefined_activation_state |
| Users | Deletion Request | undefined_activation_state |
| Users | Validate approval-start request | undefined_activation_state |

## Fixed RQ2 pool (top 10 by |ACE|)

| candidate | source | target | ACE | p(do=1) | p(do=0) | reachability |
|---|---|---|---:|---:|---:|---:|
| DEP-014 | Update record upon approval | Status Modified | 0.529 | 0.798 | 0.269 | 1 |
| DEP-007 | Activate Workflow | Workflow Configured | 0.508 | 0.777 | 0.269 | 1 |
| DEP-009 | Query Approval Status | Approval Status Details | 0.508 | 0.777 | 0.269 | 1 |
| DEP-010 | Approve Asset Request | Notify Users | 0.508 | 0.777 | 0.269 | 5 |
| DEP-012 | Transfer form | Transfer Asset | 0.508 | 0.777 | 0.269 | 2 |
| DEP-017 | Validate Export Request | Generate Export File | 0.486 | 0.755 | 0.269 | 3 |
| DEP-013 | Admin approval | Operation executed upon approval | 0.380 | 0.880 | 0.500 | 12 |
| DEP-018 | Export Asset Data | Downloadable Data File | 0.308 | 0.936 | 0.627 | 4 |
| DEP-005 | Senior Admin Approval Event | Workflow Configured | 0.269 | 0.675 | 0.406 | 2 |
| DEP-002 | Validate Configuration Details | Activate Workflow | 0.131 | 0.611 | 0.480 | 4 |