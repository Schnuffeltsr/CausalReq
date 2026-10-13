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
