# CausalReq 单文档运行结果 — MDOT_MDOT_simple2

## 1. 抽取与图结构

| 项 | 值 |
|---|---:|
| 源 FR 块数 | 8 |
| 抽取元素数 | 50 |
| 有 active_meaning 的元素 | 45 |
| 抽出关系数 | 56 |
| 证据图节点 | 50 |
| 证据图边 | 56 |
| 模拟图节点 | 45 |
| 模拟图边 | 14 |
| 被排除关系 | 30 |
| RQ2 固定候选池 | 20 |
| LLM 调用次数 | 23 |
| 阶段耗时(分钟) | 33.7 |
| 模型版本号 | MODEL-a988258ceab9 |

## 2. RQ2 固定候选池与 ACE 排序（20 条）

| 排名 | 候选 | 源元素 | 目标元素 | ACE | p(do=1) | p(do=0) | 可达性 |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | DEP-018 | Detect and classify incidents | Incident reports | +0.5292 | 0.7982 | 0.2689 | 1 |
| 2 | DEP-003 | Accept real-time data inputs from external sources | Normalized data stored in central database | +0.5084 | 0.7773 | 0.2689 | 2 |
| 3 | DEP-005 | Automated data purging policies | Support automated data purging policies | +0.5084 | 0.7773 | 0.2689 | 1 |
| 4 | DEP-014 | Schedule Automatic Report Generation and Email Delivery | Email Delivery | +0.5084 | 0.7773 | 0.2689 | 2 |
| 5 | DEP-015 | High-volume data display | De-cluttering features | +0.5084 | 0.7773 | 0.2689 | 1 |
| 6 | DEP-019 | Maintain long-term archive of processed data | Allow users to query archived data via SQL-based tools | +0.5084 | 0.7773 | 0.2689 | 2 |
| 7 | DEP-004 | Schedule Automatic Report Generation and Email Delivery | Generate Pre-defined Reports | +0.4860 | 0.7549 | 0.2689 | 2 |
| 8 | DEP-009 | Input data fields | Accept real-time data inputs from external sources | +0.4621 | 0.7311 | 0.2689 | 3 |
| 9 | DEP-012 | Configure Data Sources, Algorithms, and Output Formats | Log Administrative Actions and Errors | +0.4621 | 0.7311 | 0.2689 | 1 |
| 10 | DEP-011 | Use Oracle 10G for archiving | Maintain long-term archive of processed data | +0.4394 | 0.8259 | 0.3864 | 3 |
| 11 | DEP-002 | Support batch ingestion of historical data | Support machine learning models | +0.4368 | 0.7058 | 0.2689 | 4 |
| 12 | DEP-013 | Accept real-time data inputs from external sources | Validate incoming data and reject invalid data | +0.4102 | 0.6792 | 0.2689 | 2 |
| 13 | DEP-010 | Support batch ingestion of historical data | Maintain long-term archive of processed data | +0.3679 | 0.7736 | 0.4057 | 4 |
| 14 | DEP-016 | Maintain long-term archive of processed data | Publish processed data in standardized formats | +0.3535 | 0.6225 | 0.2689 | 2 |
| 15 | DEP-020 | Input data fields | Normalized data stored in central database | +0.2349 | 0.6406 | 0.4057 | 3 |
| 16 | DEP-001 | Use Oracle 10G for archiving | Allow users to query archived data via SQL-based tools | +0.2234 | 0.6888 | 0.4654 | 3 |
| 17 | DEP-007 | Input data fields | Validate incoming data and reject invalid data | +0.1896 | 0.5688 | 0.3793 | 3 |
| 18 | DEP-017 | Support batch ingestion of historical data | Allow users to query archived data via SQL-based tools | +0.1870 | 0.6622 | 0.4752 | 4 |
| 19 | DEP-006 | Use Oracle 10G for archiving | Publish processed data in standardized formats | +0.1554 | 0.5609 | 0.4056 | 3 |
| 20 | DEP-008 | Support batch ingestion of historical data | Publish processed data in standardized formats | +0.1301 | 0.5424 | 0.4123 | 4 |

## 3. 三种排序下的前 5 / 前 10 名（RQ2 预算视角）

**ACE** 前 10：DEP-018(+0.529), DEP-003(+0.508), DEP-005(+0.508), DEP-014(+0.508), DEP-015(+0.508), DEP-019(+0.508), DEP-004(+0.486), DEP-009(+0.462), DEP-012(+0.462), DEP-011(+0.439)

**Reachability** 前 10：DEP-002(+0.437), DEP-008(+0.130), DEP-010(+0.368), DEP-017(+0.187), DEP-001(+0.223), DEP-006(+0.155), DEP-007(+0.190), DEP-009(+0.462), DEP-011(+0.439), DEP-020(+0.235)

**Random** 前 10：DEP-012(+0.462), DEP-014(+0.508), DEP-006(+0.155), DEP-005(+0.508), DEP-016(+0.354), DEP-007(+0.190), DEP-001(+0.223), DEP-019(+0.508), DEP-009(+0.462), DEP-015(+0.508)

## 4. RQ3 五变体结果

| 变体 | 提名数 | dependency | isolated | operation | 补充需求数 | 初步去向分布 |
|---|---:|---:|---:|---:|---:|---|
| Full | 54 | 20 | 19 | 15 | 27 | retained=27, covered=17, unsupported=9, out_of_scope=1 |
| NoFullDocumentValidation | 59 | 20 | 16 | 23 | 59 | not_checked=59 |
| NoIsolatedReview | 52 | 20 | 0 | 32 | 27 | retained=27, covered=17, unsupported=8 |
| NoOperationReview | 67 | 20 | 47 | 0 | 14 | covered=33, unsupported=15, retained=14, unresolved=5 |
| NoSignedPropagation | 65 | 20 | 30 | 15 | 23 | covered=23, retained=23, unsupported=18, unresolved=1 |

## 5. Full 变体中被初步保留的补充需求（27 条）

1. **[DEPENDENCY] Support batch ingestion of historical data → Support machine learning models**
   - 审查问题：Should the system include an explicit requirement to ensure that batch-ingested historical data is made available to the machine learning model training process, given the documented dependency?
   - 初步理由：The original FRs require batch ingestion of historical data for training models and support machine learning models for predictive analysis, but they do not explicitly state that the batch-ingested historical data must be made available and accessible to the machine learning model training process. This is a necessary in-scope obligation derived from the documented dependency.
   - 补充需求：The system shall ensure that batch-ingested historical data is available and accessible to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.
   - 证据 FR：FRBLOCK-001, FRBLOCK-002

2. **[DEPENDENCY] Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports**
   - 审查问题：Does the system need to generate the pre-defined reports on traffic volume, incident frequency, and road condition trends whenever a user schedules automatic report generation and email delivery?
   - 初步理由：The original FRs (FRBLOCK-007) specify generating pre-defined reports and scheduling automatic report generation and email delivery as separate capabilities, but no original FR states that scheduling the automatic report generation triggers generation of the predefined reports. The dependency evidence supports an inferred TRIGGERS relationship, making this a retained business obligation.
   - 补充需求：The system shall generate the pre-defined reports on traffic volume, incident frequency, and road condition trends whenever a user schedules automatic report generation and email delivery.
   - 证据 FR：FRBLOCK-007

3. **[DEPENDENCY] Support batch ingestion of historical data → Publish processed data in standardized formats**
   - 审查问题：Is there a requirement that explicitly connects the source FR 'The system shall support batch ingestion of historical data for backfilling archives and training models' to the target FR 'publish processed data in standardized formats', ensuring that historical data ingested in batch is both archived and subsequently published in those standardized formats?
   - 初步理由：The original FRs separately require batch ingestion for backfilling archives, long-term archiving of processed data, and publication in standardized formats, but no FR explicitly connects batch-ingested historical data to subsequent publication. The dependency evidence from REL-06 and REL-08 supports this additional obligation.
   - 补充需求：The system shall ensure that processed data originating from batch ingestion of historical data is stored in the long-term archive and is subsequently published in the standardized formats (e.g., SAE J2354, TMDD).
   - 证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004

4. **[DEPENDENCY] Use Oracle 10G for archiving → Maintain long-term archive of processed data**
   - 审查问题：Does the requirement that the system 'maintain a long-term archive of all processed data' adequately handle scenarios where 'using Oracle 10G' for archiving is no longer feasible (e.g., unsupported, unavailable), given that the target depends on this source?
   - 初步理由：The original requirement FRBLOCK-003 states that the system shall maintain the long-term archive using Oracle 10G, but it does not specify that archival operations must continue if Oracle 10G becomes unavailable or unsupported. No other original FR covers this continuity obligation. The draft obligation is a necessary supplement to ensure the archive is not solely dependent on a specific technology.
   - 补充需求：The system shall maintain the long-term archive of all processed data without being solely dependent on Oracle 10G, ensuring continuity of archival operations.
   - 证据 FR：FRBLOCK-003

5. **[DEPENDENCY] Schedule Automatic Report Generation and Email Delivery → Email Delivery**
   - 审查问题：Does the system guarantee that when users schedule automatic report generation and email delivery (as stated in FRBLOCK-007), the scheduled report email is actually delivered to the designated recipients?
   - 初步理由：FRBLOCK-007 only requires the system to allow users to schedule automatic report generation and email delivery; it does not state that the scheduled report email is actually delivered to designated recipients. The draft obligation adds an in-scope business requirement ensuring delivery upon schedule trigger, which is not covered by the original FRs.
   - 补充需求：The system shall deliver the scheduled report email to the designated recipients when the scheduled automatic report generation and email delivery is triggered.
   - 证据 FR：FRBLOCK-007

6. **[DEPENDENCY] Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools**
   - 审查问题：Does the system's support for batch ingestion of historical data (FRBLOCK-001: 'The system shall support batch ingestion of historical data for backfilling archives and training models.') explicitly require that the resulting archived data be accessible for querying via SQL-based tools (FRBLOCK-003: 'allow users to query archived data via SQL-based tools')?
   - 初步理由：The original FRs separately require batch ingestion for backfilling archives and SQL-based querying of archived data, but none states the explicit linkage that data ingested via batch must be queryable through SQL. The dependency is directly supported: batch ingestion populates the long-term archive, and the archive is the data source for SQL queries. This obligation clarifies the intended end-to-end flow without introducing new policy.
   - 补充需求：The system shall ensure that historical data ingested in batch for archive backfill is stored in the long-term archive and made available for user queries through SQL-based tools.
   - 证据 FR：FRBLOCK-001, FRBLOCK-003

7. **[ISOLATED] Perform automated data quality checks**
   - 审查问题：Does the FR block require automated data quality checks beyond the predefined quality rules validation specified in FR-DCI-002?
   - 初步理由：The original FRs only require validation against predefined quality rules at ingestion and rejection of invalid data. They do not specify automated data quality checks on stored normalized data beyond ingestion-time validation. The draft introduces an in-scope business obligation not found in the checked original FRs.
   - 补充需求：The system shall perform automated data quality checks on stored normalized data in addition to ingestion-time validation to detect anomalies or inconsistencies not identified during ingestion.
   - 证据 FR：FRBLOCK-001

8. **[ISOLATED] Generate statistical summaries**
   - 审查问题：Does the 'Generate statistical summaries' function require access to historical traffic data, and if so, is that data source documented?
   - 初步理由：The original FR requires generating statistical summaries of daily, weekly, and monthly traffic patterns, which logically requires access to historical traffic data. No checked original FR explicitly provides for such access or documents the data source, so the obligation is a necessary addition.
   - 补充需求：The system shall have access to historical traffic data sufficient to generate the required statistical summaries.
   - 证据 FR：FRBLOCK-002

9. **[OPERATION] Detect and classify incidents**
   - 审查问题：Should the system support updating or reclassifying an incident after initial detection, and what user roles or conditions permit such updates?
   - 初步理由：The original FRs only require detection and initial classification of incidents; none specify the ability to update or reclassify an incident after detection, and no FR assigns this outside the system. The obligation is in-scope for incident management and supported by the operational need to refine classification as more information becomes available.
   - 补充需求：The system shall allow authorized users to update or reclassify a detected incident under defined conditions, including the roles and permissions required for such updates.
   - 证据 FR：FRBLOCK-002

10. **[OPERATION] Support machine learning models**
   - 审查问题：Is there a need for the system to support retraining or updating machine learning models, and what triggers such updates?
   - 初步理由：The original FRs only require support for machine learning models and predictive analysis, and possibly batch ingestion for training, but do not address retraining/updating models or triggers. Maintaining model accuracy is an in-scope business need.
   - 补充需求：The system shall provide mechanisms to retrain and update machine learning models when performance degrades or new data becomes available.
   - 证据 FR：FRBLOCK-002

11. **[OPERATION] Support automated data purging policies**
   - 审查问题：How are automated data purging policies configured, scheduled, and verified to ensure they manage storage limits without deleting data prematurely?
   - 初步理由：FRBLOCK-003 requires support for automated data purging policies but does not specify configurable retention parameters, prevention of premature deletion, or audit logging of purged data. The draft adds these operational details, which are necessary to ensure retention periods are preserved and purges are auditable.
   - 补充需求：The system shall execute automated data purging only after the applicable retention period has elapsed, according to configurable retention policies, and shall record audit logs identifying the data purged, the policy applied, and the timestamp of deletion.
   - 证据 FR：FRBLOCK-003

12. **[ISOLATED] Implement dynamic caching for frequently accessed data**
   - 审查问题：The dynamic caching function appears isolated in the graph; does the FR block require a documented connection between dynamic caching and automated data purging to ensure cached data is invalidated when purged?
   - 初步理由：The original FRs specify dynamic caching and automated data purging as separate requirements but do not define any connection or invalidation behavior. The draft obligation addresses a necessary consistency requirement between these two in-scope functions.
   - 补充需求：The system shall invalidate cached data entries when corresponding archived data is purged.
   - 证据 FR：FRBLOCK-003

13. **[ISOLATED] Compute traffic metrics**
   - 审查问题：Should the system compute traffic metrics as an input to generating traffic incident alerts as required by FR-DPO-003?
   - 初步理由：The original FRs include computing traffic metrics (FR-DPA-001), detecting traffic incidents (FR-DPA-002), and generating traffic incident alerts (FR-DPO-003), but no original FR explicitly requires computing traffic metrics as an input to detection and alert generation. The draft obligation is a necessary elaboration to ensure alert generation is supported.
   - 补充需求：The system shall compute traffic metrics to support the detection of traffic incidents and the generation of traffic incident alerts.
   - 证据 FR：FRBLOCK-004

14. **[ISOLATED] Generate statistical summaries**
   - 审查问题：Should the statistical summaries generated by the system be included in the data export formats specified in FR-DPO-004?
   - 初步理由：The original FRs require generating statistical summaries (FRBLOCK-002) and exporting data in CSV, JSON, XML, and KML formats (FRBLOCK-004), but do not explicitly require exporting the generated statistical summaries in those formats. This obligation fills that gap and is in scope.
   - 补充需求：The system shall export generated statistical summaries in CSV, JSON, XML, and KML formats for third-party use.
   - 证据 FR：FRBLOCK-004

15. **[ISOLATED] Perform automated data quality checks**
   - 审查问题：Should the system perform automated data quality checks before publishing processed data as specified in FR-DPO-001?
   - 初步理由：The original FRs include automated data quality checks (FR-DPA-004 in FRBLOCK-002) and publishing processed data in standardized formats (FR-DPO-001/FRBLOCK-004), but none specifies performing the checks prior to publication. Adding this timing constraint is a supported in-scope business obligation to prevent propagating data errors, and it is not found in the checked original FRs.
   - 补充需求：The system shall perform automated data quality checks on processed data prior to publication in standardized formats.
   - 证据 FR：FRBLOCK-004

16. **[ISOLATED] Provide Ad-hoc Reporting Tools**
   - 审查问题：Should the system provide ad-hoc reporting tools to enable third-party users to generate custom reports using the data exported according to FR-DPO-004?
   - 初步理由：The original FRs do not include an obligation for third-party users to generate custom reports using exported data. FRBLOCK-004 only specifies exporting data in CSV, JSON, XML, and KML formats for third-party use, and FRBLOCK-007 mentions ad-hoc reporting tools but not for third-party users or using exported data. The draft fills a gap by specifying reporting capabilities for third-party users based on the exported data.
   - 补充需求：The system shall provide ad-hoc reporting tools that allow third-party users to create custom reports using exported data.
   - 证据 FR：FRBLOCK-004

17. **[ISOLATED] all users**
   - 审查问题：Should the data publication, real-time feeds, alerts, and export capabilities be accessible to all users, or only to specific user groups identified in the FR block (e.g., third-party, external applications)?
   - 初步理由：The original FRs reference third-party use and external applications but do not define user roles or access permissions for data publication, real-time feeds, alerts, or export capabilities. The draft obligation clarifies the need to ensure appropriate access for intended users, which is a supported in-scope business obligation not explicitly stated in the checked original FRs.
   - 补充需求：The system shall define user roles and access permissions for data publication, real-time feeds, alerts, and export capabilities to ensure that authorized users, including third-party users and external applications, have appropriate access while preventing unauthorized access.
   - 证据 FR：FRBLOCK-004

18. **[OPERATION] Provide real-time data feeds to MI Drive**
   - 审查问题：Should the system support a push-based operation to deliver real-time data feeds to MI Drive, or is a pull-based mechanism sufficient?
   - 初步理由：The original FR (FRBLOCK-004) requires providing real-time data feeds to MDOT’s MI Drive system, but it does not specify whether the delivery mechanism should be push-based or pull-based. Defining and implementing a delivery mechanism is a necessary clarification to fulfill the existing requirement and is not covered by any original FR.
   - 补充需求：The system shall define and implement a delivery mechanism for real-time data feeds to MI Drive, specifying whether it is push-based or pull-based.
   - 证据 FR：FRBLOCK-004

19. **[ISOLATED] all users**
   - 审查问题：Does the role-based access control requirement in FR-SAC-003 need to cover an 'all users' category (e.g., a default role or public access), or are the listed user types (field operator, analyst, admin) exhaustive?
   - 初步理由：The original FR requires role-based access control for different user types, using 'e.g.' to indicate a non-exhaustive list. It does not explicitly state whether an 'all users' default role or baseline permissions must be covered. The draft clarifies that the system should define permissions for all applicable user categories, including any default 'all users' role if present. This is an in-scope elaboration supported by the source's non-exhaustive examples.
   - 补充需求：The system shall support role-based access control for all user categories, including a default 'all users' role if such a role is defined, ensuring that permissions for that role are specified and enforced.
   - 证据 FR：FRBLOCK-006

20. **[OPERATION] Log Administrative Actions and Errors**
   - 审查问题：Should the system provide an operation for administrators to view, filter, and export the logged administrative actions and errors for audit and troubleshooting?
   - 初步理由：The original FRs require logging administrative actions and errors for audit and troubleshooting, but none specifies that administrators can view, filter, or export those logs. The nominated draft extends the logging obligation to include an operational interface for accessing the logs, which is a necessary in-scope business obligation not found in the checked original FRs.
   - 补充需求：The system shall allow administrators to view, filter, and export audit log entries (including administrative actions and errors) for audit and troubleshooting purposes.
   - 证据 FR：FRBLOCK-006

21. **[OPERATION] Role-Based Access Control**
   - 审查问题：Should the system include administrative operations to create, modify, and assign roles and permissions to users, or is role assignment assumed to be preconfigured?
   - 初步理由：The original FRs state that the system supports role-based access control but do not specify how roles and permissions are managed. Administrative operations are necessary to operationalize RBAC and are not covered by the checked FRs.
   - 补充需求：The system shall provide administrative operations to create, modify, and assign user roles and permissions.
   - 证据 FR：FRBLOCK-006

22. **[OPERATION] Backup and Restore Capabilities**
   - 审查问题：Should administrators be able to schedule automatic backups and perform partial restores (e.g., only configuration settings) as part of backup and restore capabilities?
   - 初步理由：The original FRBLOCK-006 requires backup and restore capabilities for the database and configuration settings, but it does not specify scheduled backups or partial restores. The nomination refines this in-scope obligation by adding administrative control over scheduling and selective restoration.
   - 补充需求：The system shall allow administrators to schedule automatic backups and perform partial restores of database and configuration settings (e.g., restore only configuration settings without affecting the database).
   - 证据 FR：FRBLOCK-006

23. **[OPERATION] Schedule Automatic Report Generation and Email Delivery**
   - 审查问题：FR-REP-002 allows users to schedule automatic report generation and email delivery. Does the operation to specify or update the email recipients for a scheduled report need to be explicitly required, or is it implicitly covered by the scheduling function?
   - 初步理由：The original FR (FRBLOCK-007) allows scheduling automatic report generation and email delivery, but does not explicitly require the ability to specify or update the email recipients for those scheduled deliveries. This is a necessary operational detail to make scheduled email delivery functional, and it is not covered by the checked original FRs.
   - 补充需求：The system shall allow users to specify and update the email recipients for scheduled automatic report delivery.
   - 证据 FR：FRBLOCK-007

24. **[OPERATION] Enforce secure authentication and authorization**
   - 审查问题：Does the system include an operation to revoke a user's authentication and authorization, or only to enforce at login?
   - 初步理由：The original FRBLOCK-008 only requires enforcing secure authentication and authorization, not providing an operation to revoke them. None of the original FRs cover revocation of user authentication/authorization. Revocation is a necessary in-scope business obligation for managing user access.
   - 补充需求：The system shall provide an operation to revoke a user's authentication and authorization.
   - 证据 FR：FRBLOCK-008

25. **[OPERATION] Audit logging of user activities and system events**
   - 审查问题：Does the audit logging function include an operation for authorized users to view and search audit logs?
   - 初步理由：The original FRs require audit logging (e.g., FRBLOCK-008) but do not state that authorized users can view or search audit logs. The nominated obligation addresses a valid in-scope business need for compliance oversight and is not covered by the checked original FRs.
   - 补充需求：The system shall provide authorized users with the ability to view and search audit logs.
   - 证据 FR：FRBLOCK-008

26. **[OPERATION] Compliance with MDIT and FIPS 140-2**
   - 审查问题：Does the system need an operation to generate compliance reports demonstrating adherence to MDIT and FIPS 140-2?
   - 初步理由：FRBLOCK-008 requires compliance with MDIT security standards and FIPS 140-2, but no original FR specifies an operation to generate compliance reports demonstrating adherence. This is a supported in-scope business obligation not found in the original FRs.
   - 补充需求：The system shall provide authorized users with the ability to generate compliance reports demonstrating adherence to MDIT security standards and FIPS 140-2 encryption requirements.
   - 证据 FR：FRBLOCK-008

27. **[ISOLATED] all users**
   - 审查问题：The actor 'all users' is graph-isolated; should this FR block explicitly specify which user roles are included in 'all users' to avoid ambiguity?
   - 初步理由：The checked original FRs use the actor 'all users' in security requirements but do not define which user roles are included, so a clarification obligation is missing and is in scope.
   - 补充需求：The system shall specify the user roles (e.g., field operator, analyst, administrator) that constitute 'all users' for security requirements to ensure consistent application.
   - 证据 FR：FRBLOCK-008

## 6. Full 变体全部提名的初步去向明细

| 提名 | 来源 | 主题 | 去向 | 检查 FR 数 |
|---|---|---|---|---:|
| DEP-001 | dependency | Use Oracle 10G for archiving → Allow users to query archived | covered | 8 |
| DEP-002 | dependency | Support batch ingestion of historical data → Support machine | retained | 8 |
| DEP-003 | dependency | Accept real-time data inputs from external sources → Normali | covered | 8 |
| DEP-004 | dependency | Schedule Automatic Report Generation and Email Delivery → Ge | retained | 8 |
| DEP-005 | dependency | Automated data purging policies → Support automated data pur | covered | 8 |
| DEP-006 | dependency | Use Oracle 10G for archiving → Publish processed data in sta | unsupported | 8 |
| DEP-007 | dependency | Input data fields → Validate incoming data and reject invali | covered | 8 |
| DEP-008 | dependency | Support batch ingestion of historical data → Publish process | retained | 8 |
| DEP-009 | dependency | Input data fields → Accept real-time data inputs from extern | covered | 8 |
| DEP-010 | dependency | Support batch ingestion of historical data → Maintain long-t | covered | 8 |
| DEP-011 | dependency | Use Oracle 10G for archiving → Maintain long-term archive of | retained | 8 |
| DEP-012 | dependency | Configure Data Sources, Algorithms, and Output Formats → Log | covered | 8 |
| DEP-013 | dependency | Accept real-time data inputs from external sources → Validat | covered | 8 |
| DEP-014 | dependency | Schedule Automatic Report Generation and Email Delivery → Em | retained | 8 |
| DEP-015 | dependency | High-volume data display → De-cluttering features | covered | 8 |
| DEP-016 | dependency | Maintain long-term archive of processed data → Publish proce | unsupported | 8 |
| DEP-017 | dependency | Support batch ingestion of historical data → Allow users to  | retained | 8 |
| DEP-018 | dependency | Detect and classify incidents → Incident reports | covered | 8 |
| DEP-019 | dependency | Maintain long-term archive of processed data → Allow users t | covered | 8 |
| DEP-020 | dependency | Input data fields → Normalized data stored in central databa | covered | 8 |
| ISOLATED-0e1b0192d0c8 | isolated | Compute traffic metrics | out_of_scope | 8 |
| ISOLATED-48cf41c3f600 | isolated | Generate statistical summaries | covered | 8 |
| ISOLATED-b4880b6a372e | isolated | Perform automated data quality checks | retained | 8 |
| OPERATION-9c33eb1c3f74 | operation | Normalized data stored in central database | unsupported | 8 |
| ISOLATED-5b5c3831d697 | isolated | Perform automated data quality checks | unsupported | 8 |
| ISOLATED-bf0abba87494 | isolated | Generate statistical summaries | retained | 8 |
| OPERATION-ff3e64c096de | operation | Detect and classify incidents | retained | 8 |
| OPERATION-f939eb67b240 | operation | Support machine learning models | retained | 8 |
| OPERATION-0a251e0a66f5 | operation | Allow users to query archived data via SQL-based tools | unsupported | 8 |
| OPERATION-6971fcf37cfd | operation | Support automated data purging policies | retained | 8 |
| ISOLATED-0cb7c283f9de | isolated | Implement dynamic caching for frequently accessed data | retained | 8 |
| ISOLATED-b552a384e9e8 | isolated | Compute traffic metrics | retained | 8 |
| ISOLATED-da5bb9debf38 | isolated | Generate statistical summaries | retained | 8 |
| ISOLATED-56687cada6f5 | isolated | Perform automated data quality checks | retained | 8 |
| ISOLATED-7b8c6e9fdf70 | isolated | Provide Ad-hoc Reporting Tools | retained | 8 |
| ISOLATED-17a876312556 | isolated | all users | retained | 8 |
| OPERATION-635a8c4ea312 | operation | Provide API for real-time consumption | covered | 8 |
| OPERATION-535534b72c5c | operation | Provide real-time data feeds to MI Drive | retained | 8 |
| ISOLATED-8c80b876730d | isolated | Provide Ad-hoc Reporting Tools | covered | 8 |
| ISOLATED-66e6676c4a7a | isolated | all users | unsupported | 8 |
| OPERATION-53a2c099bc55 | operation | Custom dashboards | unsupported | 8 |
| ISOLATED-4ae8b88ad69f | isolated | Configure new data source types without major software chang | covered | 8 |
| ISOLATED-c951653cb78a | isolated | all users | retained | 8 |
| OPERATION-a3455eb84139 | operation | Log Administrative Actions and Errors | retained | 8 |
| OPERATION-047c524af82b | operation | Role-Based Access Control | retained | 8 |
| OPERATION-66497b27ce21 | operation | Backup and Restore Capabilities | retained | 8 |
| ISOLATED-8afc448c15a1 | isolated | Compute traffic metrics | unsupported | 8 |
| ISOLATED-0b742696e428 | isolated | Configure new data source types without major software chang | covered | 8 |
| OPERATION-bfe2c70a5486 | operation | Schedule Automatic Report Generation and Email Delivery | retained | 8 |
| OPERATION-e2933756876e | operation | Enforce secure authentication and authorization | retained | 8 |
| OPERATION-5d69238cf751 | operation | Audit logging of user activities and system events | retained | 8 |
| OPERATION-4362eb6f486f | operation | Compliance with MDIT and FIPS 140-2 | retained | 8 |
| ISOLATED-dc05a306f651 | isolated | all users | retained | 8 |
| ISOLATED-65f26d013389 | isolated | Compute traffic metrics | unsupported | 8 |

## 7. 人工判定：RQ2 固定候选池

- 候选数 **20**；依赖有原文依据 **15/20**；缺失义务成立 **1/20**
- 人工义务 ID：**O-01**

| 候选ID | 依赖有据 | 缺失义务成立 | 人工义务ID | 依据／否决原因 |
|---|---|---|---|---|
| DEP-018 | 是 | 否 |  | FR-DPA-002 的 Outputs 行已写明“Incident reports with time, location, type, and severity”，草稿与之等价；参考基准 FR-013 也未新增该义务。 |
| DEP-003 | 是 | 是 | O-01 | 原文 FR-DCI-001 的义务句只要求“accept real-time data inputs”，规范化仅出现在 Outputs 描述中；参考基准 FR-001 明确补上“shall normalize accepted inputs”义务，故属真缺失。 |
| DEP-005 | 否 | 否 |  | 源与目标是同一义务（自动清理策略），不是依赖；FR-DSA-004 已要求支持自动清理策略。 |
| DEP-014 | 是 | 否 |  | FR-REP-002 已含“email delivery”；参考基准 FR-066 新增的是“投递状态”，本候选未涉及。 |
| DEP-015 | 是 | 否 |  | FR-UIP-003 已规定在高数据量显示时降噪（de-cluttering），草稿只是同义复述。 |
| DEP-019 | 是 | 否 |  | FR-DSA-003 已直接要求允许用户通过 SQL 工具查询归档数据。 |
| DEP-004 | 是 | 否 |  | FR-REP-001（预定义报表）与 FR-REP-002（定时生成与投递）均已规定；“定时即生成报表”只是把两条义务连成一句。 |
| DEP-009 | 是 | 否 |  | FR-DCI-001 的 Inputs 行已列明 GPS/速度/位置/路况/温度/降水/能见度。 |
| DEP-012 | 是 | 否 |  | FR-SAC-002 已要求记录全部管理操作与错误，配置变更自然包含在内。 |
| DEP-011 | 是 | 否 |  | 草稿要求“不依赖 Oracle 10G”，与 FR-DSA-001 明确指定的技术冲突；参考基准 FR-026 仍保留 Oracle 10G，属改变既定技术约束的过度推断。 |
| DEP-002 | 是 | 否 |  | FR-DCI-004 已写明批式历史数据“用于回填归档与训练模型”，FR-DPA-005 已要求支持 ML 模型；参考基准 FR-008 新增的是“完成状态与失败源”，本候选未涉及。 |
| DEP-013 | 是 | 否 |  | FR-DCI-002 已要求按预定义质量规则校验并拒绝无效/畸形数据；参考基准 FR-002/FR-003 新增的是隔离与原因留痕，本候选未涉及。 |
| DEP-010 | 是 | 否 |  | FR-DCI-004（批式摄取用于回填归档）与 FR-DSA-001（长期归档全部处理后数据）已共同覆盖。 |
| DEP-016 | 否 | 否 |  | 原文未规定“发布须取自长期归档”，参考基准 FR-038 亦无此约束；该关系只是图上可达，属实现耦合。 |
| DEP-020 | 是 | 否 |  | FR-DCI-001 的 Inputs/Outputs 已覆盖“接受这些输入并输出规范化数据入库”。 |
| DEP-001 | 是 | 否 |  | FR-DSA-003 已要求允许用户用 SQL 工具查询归档数据；Oracle 10G 只是归档技术（FR-DSA-001）。 |
| DEP-007 | 是 | 否 |  | FR-DCI-002 已按数据（而非逐字段）要求质量规则校验与拒绝；逐字段枚举不构成新义务。 |
| DEP-017 | 否 | 否 |  | FR-DSA-003 已规定归档数据可 SQL 查询；“批式回填的数据也应可查”是同一义务的推论，原文未把它单列为依赖。 |
| DEP-006 | 否 | 否 |  | 与 DEP-016 同源，原文与参考基准均不支持“发布取自 Oracle 10G 归档”。 |
| DEP-008 | 否 | 否 |  | FR-DCI-004 + FR-DSA-001 + FR-DPO-001 三条既有义务的组合，原文未规定批式数据须进入发布链路。 |

## 8. 人工判定：RQ3 提名去向

- 审阅行数 **82**（Full 54，NoFullDocumentValidation 10，NoIsolatedReview 12，NoSignedPropagation 6）

| 人工去向 | 行数 |
|---|---:|
| 已覆盖·语义重复 | 36 |
| 缺乏依据·过度推断 | 21 |
| 待澄清 | 13 |
| 有效且缺失 | 12 |

- 有效且缺失 **12** 行，对应 **11** 个义务 ID：O-01, O-02, O-03, O-04, O-05, O-06, O-07, O-08, O-09, O-10, O-11

| 义务ID | 版本 | 提名ID | 路线 | 原文依据 | 理由 |
|---|---|---|---|---|---|
| O-01 | Full | DEP-003 | dependency | FR-DCI-001（Outputs）；参考基准 FR-001 | 原文只声明“规范化的数据存入中央数据库”，未以义务句要求规范化；模型判 covered 属错杀。 |
| O-02 | Full | ISOLATED-5b5c3831d697 | isolated | FR-DPA-004；参考基准 FR-018 | 原文只要求“标记异常”，未要求把质量异常通知到相关方；参考基准 FR-018 正是该义务。模型判 unsupported 属错杀。 |
| O-03 | Full | OPERATION-0a251e0a66f5 | operation | FR-DSA-003；参考基准 FR-029 | 原文允许 SQL 查询但未规定检索授权；参考基准 FR-029 明确要求按授权范围返回（部分授权时只返回允许部分）。模型判 unsupported 属错杀。 |
| O-04 | Full | OPERATION-53a2c099bc55 | operation | FR-UIP-006；参考基准 FR-056 | 原文只要求“创建”自定义看板；参考基准 FR-056 明确补充“更新/删除、版本化、归属范围”。模型判 unsupported 属错杀。 |
| O-05 | Full | OPERATION-047c524af82b | operation | FR-SAC-003；参考基准 FR-073 | 原文要求 RBAC 但未规定角色与权限的创建/变更/分配；参考基准 FR-073 正是该义务（且要求版本化、可审计、原子应用）。 |
| O-06 | Full | OPERATION-bfe2c70a5486 | operation | FR-REP-002；参考基准 FR-066 | 原文允许定时生成与投递，但未规定收件人如何指定/更新；参考基准 FR-066 把 recipient list 列为输入/输出。 |
| O-08 | NoSignedPropagation | OPERATION-39fd617ec54f | operation | FR-SAC-001；参考基准 FR-058 | 原文允许管理员配置，但未规定配置变更的授权与生效控制；参考基准 FR-058 明确要求按角色授权、并在提交时与所有入口强制校验。 |
| O-07 | NoIsolatedReview | OPERATION-e9693c61143c | operation | FR-DCI-004；参考基准 FR-010 | 原文未规定批式回填的重复规避；参考基准 FR-010 要求按已处理区间台账跳过/拒绝重叠区间。 |
| O-08 | NoIsolatedReview | OPERATION-f275b745a9c7 | operation | FR-SAC-001；参考基准 FR-058 | 与 OPERATION-39fd617ec54f 同一义务：配置须经校验/授权后再生效。 |
| O-09 | NoIsolatedReview | OPERATION-3a0f0db65dda | operation | FR-REP-002；参考基准 FR-066 | 原文未规定投递确认/投递状态；参考基准 FR-066 的输出含“delivery status”。 |
| O-10 | NoFullDocumentValidation | OPERATION-c3c92db3854a | operation | FR-UIP-001; FR-SAC-003；参考基准 FR-054 | 参考基准 FR-054 明确要求搜索结果按授权在服务端过滤，使不同角色只看到被允许的数据；原文与参考基准均未在界面层规定这一点（原文只在 FR-SAC-003 泛泛要求 RBAC）。 |
| O-11 | NoFullDocumentValidation | OPERATION-44b2daf510ec | operation | FR-UIP-002；参考基准 FR-052 | 原文只说“地图包含图层”，参考基准 FR-052 补充为“configurable icon layers”，本条目正对应图层可独立开关。 |

---

## 9. RQ2 预算对比（人工判定）

只把人工确认为“缺失义务成立”的候选计入；同一义务 ID 只计一次。

- 20 条候选中人工确认有效：1 条 （DEP-003→O-01）
- 依赖有原文依据：15/20
- 已覆盖：19/20；待澄清：0/20

| 预算 | ACE 排序 | 可达性排序 | 随机排序 |
|---:|---:|---:|---:|
| 5 | 1 | 0 | 0 |
| 10 | 1 | 0 | 0 |
| 20 | 1 | 1 | 1 |

---

## 10. RQ3 组件贡献（人工判定）

Full 的 54 条逐条人工审阅；四个消融版只新增/消失条目单独审阅，其余条目继承其对 Full 匹配项的判定。

| 版本 | 提名总数 | 人工新增行 | 有效且缺失（继承+新增） | 有效义务 ID | 相对 Full 失去 | 相对 Full 新增 |
|---|---:|---:|---:|---|---|---|
| NoSignedPropagation | - | 6 | 6 | O-01, O-03, O-04, O-05, O-06, O-08 | O-02 | O-08 |
| NoIsolatedReview | - | 12 | 8 | O-01, O-03, O-04, O-05, O-06, O-07, O-08, O-09 | O-02 | O-07, O-08, O-09 |
| NoOperationReview | - | 0 | 1 | O-01 | O-02, O-03, O-04, O-05, O-06 | — |
| NoFullDocumentValidation | - | 10 | 6 | O-01, O-04, O-05, O-06, O-10, O-11 | O-02, O-03 | O-10, O-11 |

### 消融时的“补位”检查

- **NoOperationReview**（operation 路线关闭，isolated 由 19 增至 47）：这 47 条 isolated 提名中，0 条与 Full 的 operation 提名语义对齐、47 条与其 isolated 提名对齐、0 条与依赖提名对齐、0 条为真正新条目。人工判定下该版本没有新增有效义务，即 isolated 路线**未能补齐**失去的 operation 覆盖。

- **NoIsolatedReview**（isolated 关闭，operation 由 15 增至 32）：新增的 operation 提名确实带来 3 条新的有效义务（O-07 批式回填去重、O-08 配置变更审批、O-09 报表投递状态），即 operation 路线**部分补齐**了失去的 isolated 覆盖，但 Full 中由 isolated 发现的 O-02（质量异常通知）没有被补回。
