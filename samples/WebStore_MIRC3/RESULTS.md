# CausalReq 单文档运行结果 — WebStore_MIRC3

## 1. 抽取与图结构

| 项 | 值 |
|---|---:|
| 源 FR 块数 | 33 |
| 抽取元素数 | 140 |
| 有 active_meaning 的元素 | 118 |
| 抽出关系数 | 387 |
| 证据图节点 | 140 |
| 证据图边 | 387 |
| 模拟图节点 | 118 |
| 模拟图边 | 92 |
| 被排除关系 | 109 |
| RQ2 固定候选池 | 20 |
| LLM 调用次数 | 98 |
| 阶段耗时(分钟) | 83.2 |
| 模型版本号 | MODEL-ed936aeafef8 |

## 2. RQ2 固定候选池与 ACE 排序（20 条）

| 排名 | 候选 | 源元素 | 目标元素 | ACE | p(do=1) | p(do=0) | 可达性 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | DEP-003 | User Interface Specification Compliance Checking Function | Compliance Report | +0.5292 | 0.7982 | 0.2689 | 2 |
| 2 | DEP-011 | Order Cancellation | Cancelled Order Status | +0.5292 | 0.7982 | 0.2689 | 3 |
| 3 | DEP-016 | Checkout Function | Order Created | +0.5292 | 0.7982 | 0.2689 | 5 |
| 4 | DEP-018 | Checkout Function | Payment Processed | +0.5292 | 0.7982 | 0.2689 | 5 |
| 5 | DEP-020 | Payment Processing | Successful Payment | +0.5292 | 0.7982 | 0.2689 | 4 |
| 6 | DEP-019 | Inventory Management Function | Inventory Levels Stored | +0.5290 | 0.9286 | 0.3996 | 4 |
| 7 | DEP-002 | Customer Login Function | Personalized Dashboard | +0.5084 | 0.7773 | 0.2689 | 3 |
| 8 | DEP-004 | Order Cancellation | Cancellation Event Recorded | +0.5084 | 0.7773 | 0.2689 | 3 |
| 9 | DEP-006 | Customer Registration Function | Customer Account Created | +0.5084 | 0.7773 | 0.2689 | 1 |
| 10 | DEP-007 | Order Confirmation Email Sending Function | Confirmation Event | +0.5084 | 0.7773 | 0.2689 | 2 |
| 11 | DEP-010 | Product Addition Function | Product Data Entity | +0.5084 | 0.7773 | 0.2689 | 3 |
| 12 | DEP-005 | Shopping Cart Creation Function | Product Added to Shopping Cart | +0.4449 | 0.8446 | 0.3996 | 3 |
| 13 | DEP-015 | Product Categorization Function | Product Assigned to Selected Category | +0.4378 | 0.9480 | 0.5102 | 3 |
| 14 | DEP-001 | Check Product Availability | Shopping Cart Creation Function | +0.4063 | 0.8119 | 0.4057 | 4 |
| 15 | DEP-017 | Management Event Recording | Purchase History Recorded | +0.4063 | 0.8119 | 0.4057 | 1 |
| 16 | DEP-012 | Payment Processing | Inventory Levels | +0.3154 | 0.8877 | 0.5722 | 4 |
| 17 | DEP-014 | Manage OrderItem | Inventory Levels | +0.3154 | 0.8877 | 0.5722 | 2 |
| 18 | DEP-009 | Check Product Availability | Inventory Quantity Updated | +0.2150 | 0.6987 | 0.4836 | 4 |
| 19 | DEP-013 | Check Product Availability | Confirmation Message Shown | +0.2150 | 0.6987 | 0.4836 | 4 |
| 20 | DEP-008 | Order | Order Confirmation Email Sent | +0.1582 | 0.7934 | 0.6351 | 3 |

## 3. 三种排序下的前 5 / 前 10 名（RQ2 预算视角）

**ACE** 前 10：DEP-003(+0.529), DEP-011(+0.529), DEP-016(+0.529), DEP-018(+0.529), DEP-020(+0.529), DEP-019(+0.529), DEP-002(+0.508), DEP-004(+0.508), DEP-006(+0.508), DEP-007(+0.508)

**Reachability** 前 10：DEP-016(+0.529), DEP-018(+0.529), DEP-001(+0.406), DEP-009(+0.215), DEP-012(+0.315), DEP-013(+0.215), DEP-019(+0.529), DEP-020(+0.529), DEP-002(+0.508), DEP-004(+0.508)

**Random** 前 10：DEP-001(+0.406), DEP-018(+0.529), DEP-019(+0.529), DEP-004(+0.508), DEP-020(+0.529), DEP-010(+0.508), DEP-008(+0.158), DEP-016(+0.529), DEP-012(+0.315), DEP-006(+0.508)

## 4. RQ3 五变体结果

| 变体 | 提名数 | dependency | isolated | operation | 补充需求数 | 初步去向分布 |
|---|---:|---:|---:|---:|---:|---|
| Full | 215 | 20 | 77 | 118 | 11 | covered=111, unsupported=81, unresolved=11, retained=11, out_of_scope=1 |
| NoFullDocumentValidation | 214 | 20 | 79 | 115 | 214 | not_checked=214 |
| NoIsolatedReview | 196 | 20 | 0 | 176 | 10 | covered=135, unsupported=43, retained=10, unresolved=7, out_of_scope=1 |
| NoOperationReview | 191 | 20 | 171 | 0 | 7 | unsupported=113, covered=53, unresolved=12, retained=7, out_of_scope=6 |
| NoSignedPropagation | 219 | 20 | 84 | 115 | 13 | covered=108, unsupported=90, retained=13, unresolved=8 |

## 5. Full 变体中被初步保留的补充需求（11 条）

1. **[OPERATION] Customer Registration Function**
   - 审查问题：Does the registration workflow need a documented operation for handling duplicate email attempts, such as presenting a recovery or update path?
   - 初步理由：FRBLOCK-001 establishes in-scope duplicate-email checking during registration but does not define the next operation when a duplicate is found, and no other original FR states an equivalent obligation. The draft is a supported, scoped gap-filling requirement that does not assume full CRUD.
   - 补充需求：When a duplicate email is detected during customer registration, the system shall define and execute a documented next step, such as presenting a recovery or account-update path, without requiring full CRUD functionality.
   - 证据 FR：FRBLOCK-001

2. **[OPERATION] Validate Updated Information (CONSTRAINT)**
   - 审查问题：What validation rules apply to updated contact information fields, such as phone number format or address completeness, before the system stores the update?
   - 初步理由：FRBLOCK-005 establishes that the system validates updated contact information, so the validation topic is in scope. However, none of the checked original FRs specify the validation criteria for updated contact information fields before storage. The draft's obligation to specify/enforce such criteria is a supported, in-scope gap not already stated in the original FRs.
   - 补充需求：The system shall validate updated contact information fields according to specified criteria before storing the update.
   - 证据 FR：FRBLOCK-005

3. **[OPERATION] Active Order/Cart Check**
   - 审查问题：Does the Active Order/Cart Check operation define what happens when the check finds active orders or cart references, or does it only prevent proceeding?
   - 初步理由：FRBLOCK-008 establishes that the system checks for active orders or cart references before proceeding, but it does not define the outcome when such references are found. No other original FR covers the behavior during product removal. The nomination identifies an in-scope gap: the system behavior for a positive check must be specified.
   - 补充需求：The system shall, when active orders or cart references are found during product removal, prevent the product removal and notify the administrator that the product is still in use.
   - 证据 FR：FRBLOCK-008

4. **[OPERATION] Add to Cart**
   - 审查问题：Should the Add to Cart operation check product availability before adding the product to the cart?
   - 初步理由：FRBLOCK-012 covers the Add to Cart action and states that product availability is checked and inventory is updated, but it does not specify whether those actions occur before or after recording the product in the shopping cart. This in-scope sequencing obligation is not covered by FRBLOCK-012 or any other original FR.
   - 补充需求：The system shall check product availability before recording the product in the shopping cart when the customer invokes Add to Cart.
   - 证据 FR：FRBLOCK-012

5. **[OPERATION] Shopping Cart Creation Function**
   - 审查问题：Is the Shopping Cart Creation Function complete with respect to inventory update failure?
   - 初步理由：FR-12 describes the shopping cart creation flow including inventory update, but does not specify handling for inventory update failure after the product is added to the cart. No other original FR covers this error-handling obligation, and the topic is in-scope for the Shopping Cart Creation Function.
   - 补充需求：The system shall handle inventory update failures that occur after a product is added to the shopping cart, including ensuring cart/inventory consistency and notifying the customer.
   - 证据 FR：FRBLOCK-012

6. **[OPERATION] Compliance Check Initiation**
   - 审查问题：Should the Compliance Check Initiation event trigger a documented operation, and what operation should it invoke?
   - 初步理由：The original FR FRBLOCK-020 describes the compliance check initiation and its resulting actions, but does not explicitly define the operation triggered by the Compliance Check Initiation event. The draft obligation is therefore supported and in-scope, but not covered as a distinct operation definition.
   - 补充需求：The system shall invoke the Compliance Check operation when the Compliance Check Initiation event occurs. The operation shall generate a compliance report, highlight non-compliant elements, and record the compliance check event in Purchase History.
   - 证据 FR：FRBLOCK-020

7. **[OPERATION] Inventory Adjustment**
   - 审查问题：For a quantity change, should inventory be adjusted by the difference between the previous and new quantity?
   - 初步理由：FRBLOCK-021 establishes that inventory levels are adjusted when cart quantities change, but it does not specify the calculation method. The draft clarifies the business obligation to adjust by the quantity delta, which is an in-scope refinement not explicitly covered by the original FRs.
   - 补充需求：The system shall adjust inventory levels by the difference between the previous and new cart item quantities when a customer changes the quantity of an item in the cart.
   - 证据 FR：FRBLOCK-021

8. **[OPERATION] Payment Viewing Event**
   - 审查问题：What data must be captured for a Payment Viewing Event when payment details are viewed?
   - 初步理由：FRBLOCK-026 establishes that a viewing event is recorded in Purchase History, but it does not define the event attributes needed to identify the payment viewed, the actor, or the view time. No other original FR covers those specific attributes, and the nomination is an in-scope refinement for auditable payment-viewing records.
   - 补充需求：The system shall record, for each Payment Viewing Event, the viewed payment identifier, the viewing actor, and the view timestamp.
   - 证据 FR：FRBLOCK-026

9. **[OPERATION] Administrator**
   - 审查问题：Does the Manage Administrator Function need to treat 'update' and 'deactivate' as distinct operations for an administrator account?
   - 初步理由：FRBLOCK-027 lists updating or deactivating administrator accounts, but it only describes update behavior and does not define deactivation as a distinct status-changing operation or clarify that personal/contact information need not be overwritten. This is an in-scope gap for the Manage Administrator Function.
   - 补充需求：The system shall treat deactivation of an administrator account as a distinct operation from update, changing the account status without overwriting the account's personal or contact information.
   - 证据 FR：FRBLOCK-027

10. **[OPERATION] Personal Information Data Entity**
   - 审查问题：When an update is requested, should the system update only the changed attributes or replace the entire Personal Information record?
   - 初步理由：FRBLOCK-031 is the relevant in-scope FR for Personal Information updates, but it only states that the entity is updated if changes are made. It does not specify whether unchanged fields should be preserved or the entire record replaced. No other original FR states an equivalent partial-update obligation. Therefore, the draft introduces a supported in-scope business rule that is not already covered.
   - 补充需求：The system shall apply only validated, changed personal information fields to the Personal Information data entity when an update is requested.
   - 证据 FR：FRBLOCK-031

11. **[ISOLATED] Eligibility Constraint for Cancellation**
   - 审查问题：What documented rule set defines an order as being in an eligible status for cancellation, and how is that rule enforced when a customer or administrator triggers cancellation?
   - 初步理由：FRBLOCK-033 establishes that cancellation is allowed only when the order is in an eligible status, but it does not explicitly require the system to validate the selected order against the cancellation eligibility rule before executing cancellation. The draft is supported by this eligibility condition and is an in-scope enforcement obligation not already stated in the checked original FRs.
   - 补充需求：The system shall validate the selected order against the defined cancellation eligibility rule before executing the Order Cancellation function.
   - 证据 FR：FRBLOCK-033

## 6. Full 变体全部提名的初步去向明细

| 提名 | 来源 | 主题 | 去向 | 检查 FR 数 |
|---|---|---|---|---:|
| DEP-001 | dependency | Check Product Availability → Shopping Cart Creation Function | unsupported | 33 |
| DEP-002 | dependency | Customer Login Function → Personalized Dashboard | covered | 33 |
| DEP-003 | dependency | User Interface Specification Compliance Checking Function →  | covered | 33 |
| DEP-004 | dependency | Order Cancellation → Cancellation Event Recorded | covered | 33 |
| DEP-005 | dependency | Shopping Cart Creation Function → Product Added to Shopping  | unresolved | 33 |
| DEP-006 | dependency | Customer Registration Function → Customer Account Created | covered | 33 |
| DEP-007 | dependency | Order Confirmation Email Sending Function → Confirmation Eve | covered | 33 |
| DEP-008 | dependency | Order → Order Confirmation Email Sent | covered | 33 |
| DEP-009 | dependency | Check Product Availability → Inventory Quantity Updated | covered | 33 |
| DEP-010 | dependency | Product Addition Function → Product Data Entity | covered | 33 |
| DEP-011 | dependency | Order Cancellation → Cancelled Order Status | covered | 33 |
| DEP-012 | dependency | Payment Processing → Inventory Levels | covered | 33 |
| DEP-013 | dependency | Check Product Availability → Confirmation Message Shown | unsupported | 33 |
| DEP-014 | dependency | Manage OrderItem → Inventory Levels | covered | 33 |
| DEP-015 | dependency | Product Categorization Function → Product Assigned to Select | covered | 33 |
| DEP-016 | dependency | Checkout Function → Order Created | covered | 33 |
| DEP-017 | dependency | Management Event Recording → Purchase History Recorded | covered | 33 |
| DEP-018 | dependency | Checkout Function → Payment Processed | covered | 33 |
| DEP-019 | dependency | Inventory Management Function → Inventory Levels Stored | covered | 33 |
| DEP-020 | dependency | Payment Processing → Successful Payment | covered | 33 |
| OPERATION-8d85e564504b | operation | Customer Registration Function | retained | 33 |
| OPERATION-16474f53a790 | operation | Personal Information | covered | 33 |
| OPERATION-03711fe91783 | operation | Contact Information | covered | 33 |
| ISOLATED-4caaa0405613 | isolated | Personal Information View or Update Event | unsupported | 33 |
| ISOLATED-b557e934f48f | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-077d5abc8181 | isolated | System | covered | 33 |
| ISOLATED-5380395bca3b | isolated | System | covered | 33 |
| OPERATION-446932587fb7 | operation | Purchase History | covered | 33 |
| OPERATION-ed02427cec99 | operation | Login Event | covered | 33 |
| OPERATION-1d4c98d96e5d | operation | Authenticated | covered | 33 |
| OPERATION-4a45abd7f912 | operation | Personalized Dashboard | covered | 33 |
| ISOLATED-24d8707ccd22 | isolated | System | covered | 33 |
| ISOLATED-384e46ff76e0 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-fa20d5953a08 | operation | Purchase History | covered | 33 |
| OPERATION-081e0d0c48f0 | operation | Session Terminated | covered | 33 |
| ISOLATED-c70714fe010f | isolated | Personal Information View or Update Event | covered | 33 |
| OPERATION-dbf00bcf2a33 | operation | Personal Information | unsupported | 33 |
| OPERATION-960661ea1272 | operation | Purchase History | covered | 33 |
| OPERATION-d82810dc2dde | operation | Manage Contact Information | unresolved | 33 |
| OPERATION-9f2b1be930db | operation | Validate Updated Information (CONSTRAINT) | retained | 33 |
| OPERATION-ac2361b373ee | operation | Contact Information Update Event | unsupported | 33 |
| ISOLATED-1f64b8401451 | isolated | Validate Changes | covered | 33 |
| ISOLATED-6f874d259c39 | isolated | System | covered | 33 |
| ISOLATED-f14532a239c1 | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-a32f8a385172 | isolated | System | covered | 33 |
| OPERATION-0a9707a29159 | operation | Purchase History | covered | 33 |
| OPERATION-a1d6ff835018 | operation | Purchase History Viewing Function | covered | 33 |
| OPERATION-553e9ea9b3fc | operation | Modify Inventory Levels | covered | 33 |
| OPERATION-8ef0d91c87f8 | operation | Validate Changes | unsupported | 33 |
| OPERATION-c60e04f67c6d | operation | Addition Event | covered | 33 |
| ISOLATED-ed86eb2978ba | isolated | System | unsupported | 33 |
| OPERATION-b0ed70a62769 | operation | Active Order/Cart Check | retained | 33 |
| OPERATION-9409987c52ab | operation | Modify Inventory Levels | unsupported | 33 |
| OPERATION-526d3f1cb20b | operation | Validate Changes | covered | 33 |
| ISOLATED-b7f72d9c6562 | isolated | User Interface Specification Compliance | out_of_scope | 33 |
| ISOLATED-ba0bf790bfa9 | isolated | System | covered | 33 |
| ISOLATED-82912a0f5399 | isolated | Eligibility Constraint for Cancellation | unsupported | 33 |
| ISOLATED-54e4368bed94 | isolated | Modify Inventory Levels | covered | 33 |
| ISOLATED-64aadaf417cb | isolated | Validate Changes | unsupported | 33 |
| OPERATION-8803f0002f23 | operation | Update Product Information | covered | 33 |
| OPERATION-4e4f3150ac54 | operation | Update Event | covered | 33 |
| OPERATION-d1a9f5830695 | operation | Validate Changes | covered | 33 |
| ISOLATED-5263691677ac | isolated | System | covered | 33 |
| ISOLATED-39b76ffc44e9 | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-ecd2a44d808d | isolated | Modify Inventory Levels | covered | 33 |
| ISOLATED-0459b98094ab | isolated | View Inventory Levels | covered | 33 |
| ISOLATED-3bc6a765ecbf | isolated | System | covered | 33 |
| ISOLATED-7433f63a1c9a | isolated | Validate Changes | unsupported | 33 |
| OPERATION-a9520d81eb55 | operation | Modify Inventory Levels | covered | 33 |
| OPERATION-f265d9b3e153 | operation | Inventory Quantity Update | unsupported | 33 |
| OPERATION-35996338317d | operation | Management Event Recording | covered | 33 |
| OPERATION-4fcbe2f8b02f | operation | Add to Cart | retained | 33 |
| OPERATION-7f2a75b6d6bd | operation | Check Product Availability | unsupported | 33 |
| OPERATION-ebb278528096 | operation | Modify Inventory Levels | unsupported | 33 |
| OPERATION-11f4e1b69a3f | operation | View Inventory Levels | unresolved | 33 |
| OPERATION-9597f5538e1f | operation | Validate Changes | unsupported | 33 |
| ISOLATED-35331bd04470 | isolated | System | covered | 33 |
| ISOLATED-e690bc271511 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-aaa14549d825 | operation | Shopping Cart Creation Function | retained | 33 |
| ISOLATED-9bb2feed9366 | isolated | Modify Inventory Levels | covered | 33 |
| OPERATION-004daf596129 | operation | Remove action | covered | 33 |
| OPERATION-1877178cbacd | operation | quantity change | covered | 33 |
| OPERATION-f889f10d8565 | operation | Modification Event | unsupported | 33 |
| OPERATION-c85adf57b667 | operation | Customer | unresolved | 33 |
| OPERATION-b03f012b638b | operation | Shopping Cart | covered | 33 |
| OPERATION-45edffd8a4b4 | operation | Cart Items | covered | 33 |
| OPERATION-023f74f89f22 | operation | Cart Summary Displayed | covered | 33 |
| OPERATION-9e5af1a6bad4 | operation | Purchase History | covered | 33 |
| OPERATION-ad04480a3580 | operation | Viewing Event Recorded | covered | 33 |
| OPERATION-a6e0d8d9b8f4 | operation | Shopping Cart Viewing Function | covered | 33 |
| ISOLATED-fbcb67ed153b | isolated | System | covered | 33 |
| ISOLATED-43a541a03650 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-e9639f301f12 | operation | Modify Inventory Levels | covered | 33 |
| OPERATION-fc365b2cda3f | operation | Validate Changes | unsupported | 33 |
| OPERATION-2eede297e2fe | operation | View Inventory Levels | unsupported | 33 |
| ISOLATED-1580b7a90b4f | isolated | System | covered | 33 |
| ISOLATED-11ebd15df5d8 | isolated | Personal Information View or Update Event | unsupported | 33 |
| ISOLATED-5359761dbfb5 | isolated | Eligibility Constraint for Cancellation | unsupported | 33 |
| ISOLATED-7c4d8de57279 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-a0339d21be16 | operation | Order | covered | 33 |
| OPERATION-23592760472d | operation | EmailRecord | covered | 33 |
| OPERATION-2d2dc5d36afb | operation | Purchase History | unsupported | 33 |
| OPERATION-c8b02d6f4ede | operation | Order Confirmation Email Sending Function | unsupported | 33 |
| ISOLATED-cb72231d3ad8 | isolated | System | covered | 33 |
| OPERATION-ff9a50e838ca | operation | Payment Processing | covered | 33 |
| OPERATION-96a3f77e438a | operation | Payment Data Entity | covered | 33 |
| OPERATION-021cbb3a50be | operation | Order Data Entity | covered | 33 |
| OPERATION-b94a9159cdbc | operation | Inventory Updated | covered | 33 |
| OPERATION-3fd8cb956c00 | operation | Payment Event | covered | 33 |
| ISOLATED-be0094c67890 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-89bf156ad239 | isolated | Modify Inventory Levels | unsupported | 33 |
| ISOLATED-17a94d9ab9ac | isolated | View Inventory Levels | unsupported | 33 |
| OPERATION-e08534fbc252 | operation | Administrator | covered | 33 |
| OPERATION-7457a49b17a1 | operation | Plugin Development Function | unresolved | 33 |
| OPERATION-5dd481659a71 | operation | Plugin Validation Constraint | unsupported | 33 |
| ISOLATED-7032db173ea7 | isolated | System | unsupported | 33 |
| ISOLATED-92837d639609 | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-3fef0c9e682d | isolated | Validate Changes | covered | 33 |
| OPERATION-86d0953b3c7a | operation | Configure Plugin Settings | unsupported | 33 |
| OPERATION-1b3bfb3f17aa | operation | Plugin Data Entity | unsupported | 33 |
| OPERATION-37b68e1d5387 | operation | Configuration Event | unsupported | 33 |
| OPERATION-3246e03199f6 | operation | System Interface Reflects Updated Settings | unsupported | 33 |
| ISOLATED-44d96d1f07df | isolated | System | unsupported | 33 |
| OPERATION-510793654eca | operation | Administrator | covered | 33 |
| OPERATION-ed3c03254259 | operation | Compliance Check Initiation | retained | 33 |
| OPERATION-f79b958616ca | operation | User Interface Specification Compliance Checking Function | covered | 33 |
| OPERATION-2e6b71c0618e | operation | Compliance Report | covered | 33 |
| OPERATION-74ae7fb05c57 | operation | Non-compliant Element Highlight | covered | 33 |
| OPERATION-3dde4468c8b2 | operation | Purchase History | covered | 33 |
| ISOLATED-8b57de6bcdf1 | isolated | System | covered | 33 |
| ISOLATED-f3de809f8186 | isolated | User Interface Specification Compliance | covered | 33 |
| OPERATION-1fff7e14dd04 | operation | Manage CartItem Function | covered | 33 |
| OPERATION-621372d73bca | operation | Inventory Adjustment | retained | 33 |
| OPERATION-e1247f9f10ef | operation | CartItem Data Entity | covered | 33 |
| OPERATION-7753d27aebb3 | operation | Modification Event | unsupported | 33 |
| ISOLATED-d501037d9ab5 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-ea8ff157820b | isolated | Modify Inventory Levels | covered | 33 |
| OPERATION-455e9d9256b2 | operation | Validate Changes | unsupported | 33 |
| OPERATION-ed619e979b99 | operation | Modify Inventory Levels | covered | 33 |
| OPERATION-d768703b48aa | operation | Eligibility Constraint for Cancellation | unsupported | 33 |
| ISOLATED-9b582e062f47 | isolated | View Inventory Levels | covered | 33 |
| ISOLATED-abc5e84c6191 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-14cd699a8f75 | operation | Manage EmailRecord | covered | 33 |
| OPERATION-57ba231c91cd | operation | Manage EmailRecord | covered | 33 |
| OPERATION-ee1c99b17e50 | operation | EmailRecord | unresolved | 33 |
| ISOLATED-4df74bdc7fee | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-0f21836bc504 | isolated | Personal Information View or Update Event | unsupported | 33 |
| ISOLATED-874950bfbb7c | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-29319ceb76aa | isolated | System | covered | 33 |
| ISOLATED-5a0bdf4665dd | isolated | System | covered | 33 |
| ISOLATED-e1b8eb311070 | isolated | Personal Information View or Update Event | unsupported | 33 |
| ISOLATED-c927ae0d1828 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-f595515b8616 | operation | View EmailRecord Function | covered | 33 |
| OPERATION-f307568d90f3 | operation | Viewing Event | unsupported | 33 |
| ISOLATED-563cfbb1c4ab | isolated | System | covered | 33 |
| OPERATION-5e6b3de90d98 | operation | CartItem Data Entity | covered | 33 |
| OPERATION-c8c3105c6248 | operation | Purchase History data entity | covered | 33 |
| OPERATION-123f682b47f8 | operation | View CartItem Function | covered | 33 |
| OPERATION-87ef7d6f9e4b | operation | Viewing Event Recorded | covered | 33 |
| OPERATION-5ea8ac5f70c4 | operation | Customer | unsupported | 33 |
| OPERATION-5e6f44a938d6 | operation | Administrator | unsupported | 33 |
| OPERATION-d84565ab9777 | operation | Payment Data Entity | covered | 33 |
| OPERATION-cf9ef4f13201 | operation | Payment Viewing Event | retained | 33 |
| OPERATION-6feee3ba4d82 | operation | Purchase History data entity | covered | 33 |
| OPERATION-24437c892444 | operation | View Payment Function | unsupported | 33 |
| ISOLATED-24a838eb0929 | isolated | System | covered | 33 |
| OPERATION-87fa1dae7471 | operation | Administrator | retained | 33 |
| OPERATION-f3c3af799c05 | operation | Management Event | unsupported | 33 |
| OPERATION-1f53e2c4a0c3 | operation | Personal Information | unsupported | 33 |
| ISOLATED-1d2984a37dd5 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-d2dcd83d025d | isolated | Personal Information View or Update Event | unsupported | 33 |
| ISOLATED-9effd7bfa3d9 | isolated | Eligibility Constraint for Cancellation | unsupported | 33 |
| ISOLATED-599798f466ef | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-3b794647c0b0 | isolated | System | covered | 33 |
| OPERATION-21d2374ab698 | operation | Personal Information | covered | 33 |
| OPERATION-706ce6e156f5 | operation | Contact Information | covered | 33 |
| OPERATION-f524efafc3c7 | operation | Purchase History | covered | 33 |
| OPERATION-756799872933 | operation | Management Event | covered | 33 |
| OPERATION-1c04df487c3d | operation | Manage Customer Function | covered | 33 |
| ISOLATED-3370a6dda3fc | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-fbd8dbfef3ee | isolated | Personal Information View or Update Event | covered | 33 |
| ISOLATED-2659cdc76cfd | isolated | Eligibility Constraint for Cancellation | unsupported | 33 |
| ISOLATED-3d833e3d41a0 | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-3cb9c66859b1 | isolated | System | unsupported | 33 |
| OPERATION-a4a20d4238ef | operation | Validate Category | unsupported | 33 |
| OPERATION-87806f67a0cd | operation | Management Event | covered | 33 |
| OPERATION-a15d44bb910d | operation | Product Associations | unresolved | 33 |
| OPERATION-43be5c00eedd | operation | Category Data Entity | unresolved | 33 |
| ISOLATED-207b2c069cde | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-f739b3756862 | isolated | User Interface Specification Compliance | unsupported | 33 |
| ISOLATED-302534d142f4 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-8d1f0250a05c | isolated | System | covered | 33 |
| OPERATION-800dd8b4e771 | operation | Manage User Interface Specification Function | covered | 33 |
| OPERATION-37484ba33b1c | operation | Management Event Recorded | unsupported | 33 |
| OPERATION-8aee8e74127b | operation | Administrators | unsupported | 33 |
| OPERATION-b639e08250e8 | operation | User Interface Specification data entity | unsupported | 33 |
| OPERATION-44c71d193b0f | operation | Personal Information View or Update Event | unsupported | 33 |
| OPERATION-6cff1477f20b | operation | Personal Information Data Entity | retained | 33 |
| OPERATION-a44c17e0c62e | operation | Administrator | unsupported | 33 |
| ISOLATED-b1fdab7d1981 | isolated | Validate Changes | unsupported | 33 |
| OPERATION-1006feed7b33 | operation | Manage Personal Information | unresolved | 33 |
| ISOLATED-099787d282f9 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-d2a18fbd7319 | isolated | System | covered | 33 |
| OPERATION-5babe5ecb961 | operation | Contact Information | covered | 33 |
| OPERATION-59b48c3585bd | operation | Manage Contact Information | covered | 33 |
| OPERATION-65c6755d27b1 | operation | Viewing or Update Event | covered | 33 |
| ISOLATED-793c8d40ef6f | isolated | Eligibility Constraint for Cancellation | retained | 33 |
| ISOLATED-d2426ebd3a24 | isolated | Modify Inventory Levels | unsupported | 33 |
| ISOLATED-e2e63e5c7aa6 | isolated | Validate Changes | unsupported | 33 |
| ISOLATED-0aa010cd46c7 | isolated | System | unsupported | 33 |
| ISOLATED-43072cbd0f98 | isolated | User Interface Specification Compliance | unsupported | 33 |
| OPERATION-301dcdaba024 | operation | Order Cancellation | unsupported | 33 |
| OPERATION-c72a82a5b93d | operation | Cancelled Order Status | unresolved | 33 |
| OPERATION-fb933fbc07c5 | operation | Cancellation Event Recorded | unsupported | 33 |
| OPERATION-24c5945214da | operation | Inventory Updated | unresolved | 33 |
