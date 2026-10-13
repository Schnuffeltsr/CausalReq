# RQ3 审查材料：MDOT_MDOT_simple2 / NoOperationReview

**注意：下列去向只是模型初步筛查，不是人工有效性结论。**

## 运行设置

```json
{
  "signed_propagation": true,
  "isolated_review": true,
  "operation_review": false,
  "full_document_validation": true
}
```

## dependency：20 条提名

### DEP-001
- 主题：Use Oracle 10G for archiving → Allow users to query archived data via SQL-based tools
- 审查问题：Given that the system uses Oracle 10G for archiving (FRBLOCK-003: 'using Oracle 10G'), is it required that users be able to query archived data via SQL-based tools (FRBLOCK-003: 'allow users to query archived data via SQL-based tools')?
- 场景：The system is required to maintain a long-term archive of all processed data using Oracle 10G. During requirements review, stakeholders must decide whether the ability to query archived data via SQL-based tools is a necessary capability when the archive is stored in Oracle 10G.
- 模型初步去向：covered
- 模型解释：The original functional requirement FRBLOCK-003 already explicitly states the obligation: 'The system shall allow users to query archived data via SQL-based tools.' The nomination's draft obligation adds a condition about Oracle 10G archiving, but the core query capability is already covered by the original FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall allow users to query archived data via SQL-based tools when archiving is performed using Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Support batch ingestion of historical data → Support machine learning models
- 审查问题：Is there a requirement that ensures batch-ingested historical data is made available in a suitable form for training the machine learning models used for predictive analysis?
- 场景：The system shall support batch ingestion of historical data for backfilling archives and training models, and it shall support machine learning models for predictive analysis of traffic trends and incident likelihood. The batch ingestion capability directly enables the training of these models, creating a positive dependency. We are reviewing whether an explicit obligation exists to connect the batch-ingested historical data to the ML training process.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already requires batch ingestion of historical data for training models, which encompasses making historical data available for model training; the draft adds formatting/accessibility detail but does not establish a new business obligation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall ensure that historical data ingested via batch processing is accessible and formatted appropriately for training the machine learning models that perform predictive analysis of traffic trends and incident likelihood.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Accept real-time data inputs from external sources → Normalized data stored in central database
- 审查问题：Does the system specification explicitly require that real-time data inputs accepted from probe vehicles, traffic sensors, weather stations, and traveler information systems are normalized and stored in the central database, or is this PRODUCES relationship only implied by the documented dependency?
- 场景：The system is specified to accept real-time data from multiple external sources, and the target functional requirement indicates that normalized data is stored in a central database. However, there is no clear statement that the accepted data must undergo normalization and subsequent storage, potentially leading to accepted data being discarded or not persisted as required.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 (FR-DCI-001) already specifies that the accepted real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems produce normalized data stored in a central database, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall normalize all real-time data inputs accepted from probe vehicles, traffic sensors, weather stations, and traveler information systems and store the resulting normalized data in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports
- 审查问题：Does the system ensure that when automatic report generation is scheduled, the pre-defined reports (traffic volume, incident frequency, and road condition trends) are generated automatically at the scheduled time without manual intervention?
- 场景：A user schedules automatic report generation and email delivery. At the scheduled time, the system should automatically generate the pre-defined reports and then email them to the designated recipients.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already states that users can schedule automatic report generation and email delivery, which implies that pre-defined reports are generated automatically at the scheduled time without manual intervention.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall generate the pre-defined reports automatically when the scheduled time for report generation is reached.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Automated data purging policies → Support automated data purging policies
- 审查问题：Does the system provide the capability to support automated data purging policies?
- 场景：Automated data purging policies are defined and active to manage storage limits. The system should enable execution and management of these policies.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-003 already explicitly states: 'The system shall support automated data purging policies to manage storage limits.' This is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall support automated data purging policies.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Use Oracle 10G for archiving → Publish processed data in standardized formats
- 审查问题：Does the requirement to 'publish processed data in standardized formats' require that the long-term archive maintained 'using Oracle 10G' be able to provide processed data in those standardized formats?
- 场景：The system must 'maintain a long-term archive of all processed data' using Oracle 10G, and separately must 'publish processed data in standardized formats'. The dependency indicates that publishing processed data depends on the archive as the source of processed data.
- 模型初步去向：unsupported
- 模型解释：The draft obligation requires the long-term archive itself to provide processed data in standardized publication formats. Original FRs only require maintaining an archive (FRBLOCK-003) and separately publishing processed data in standardized formats (FRBLOCK-004); they do not require the archive to output data in those formats. The dependency only supports that the archive is the source of processed data, not that the archive must provide it in standardized formats.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall ensure that the long-term archive maintained using Oracle 10G provides processed data in the standardized formats required for publication.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Input data fields → Validate incoming data and reject invalid data
- 审查问题：Does the system validate every listed input data field (GPS data, speed, location, road condition reports, temperature, precipitation, and visibility) against predefined quality rules and reject invalid or malformed data?
- 场景：A real-time data stream from probe vehicles, traffic sensors, weather stations, and traveler information systems delivers GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. Some records contain invalid or malformed values for these fields.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-001 already states: 'The system shall validate incoming data against predefined quality rules and reject invalid or malformed data.' This covers validation of all incoming data fields, including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility, because those fields are specified as incoming data inputs in the same FR block (FR-DCI-001). Thus the draft obligation is equivalent to an existing original requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall validate all input data fields listed in the data input requirements (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) against predefined quality rules and reject any record containing invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Support batch ingestion of historical data → Publish processed data in standardized formats
- 审查问题：Does the system include a requirement that when historical data is batch ingested (per FRBLOCK-001: 'The system shall support batch ingestion of historical data for backfilling archives and training models'), the resulting processed data is published in standardized formats (per FRBLOCK-004: 'publish processed data in standardized formats')?
- 场景：The system performs batch ingestion of historical data to backfill archives and train models (FRBLOCK-001). Separately, the system is required to publish processed data in standardized formats (FRBLOCK-004). However, there is no explicit requirement ensuring that data ingested via batch is subsequently processed and published in those standardized formats. Without such a linkage, historical data may remain archived but never be published.
- 模型初步去向：retained
- 模型解释：The draft links FRBLOCK-001 (batch ingestion for backfilling archives) and FRBLOCK-003 (archive of processed data) to FRBLOCK-004 (publish processed data in standardized formats). No original FR explicitly requires that processed data from batch ingestion be published, but the trace evidence supports this as a necessary closure of the data flow within scope.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data resulting from batch ingestion of historical data in standardized formats (SAE J2354, TMDD).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Input data fields → Accept real-time data inputs from external sources
- 审查问题：Is there a documented requirement that the system shall accept real-time data inputs including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility from probe vehicles, traffic sensors, weather stations, and traveler information systems?
- 场景：The system is operational and connected to external data sources: probe vehicles, traffic sensors, weather stations, and traveler information systems. Real-time data streams are available, containing fields such as GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The system must determine whether it has a mandatory obligation to accept and process these inputs.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 (FR-DCI-001) explicitly requires the system to accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, and lists the exact data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, including the following data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Support batch ingestion of historical data → Maintain long-term archive of processed data
- 审查问题：Does the system's support for batch ingestion of historical data for backfilling archives and training models ensure that the long-term archive of processed data is maintained?
- 场景：The system shall support batch ingestion of historical data for backfilling archives and training models, which is intended to enable the maintenance of a long-term archive of processed data.
- 模型初步去向：unresolved
- 模型解释：An existing original FR already requires maintaining a long-term archive of processed data. The batch ingestion context does not add a new obligation beyond what is already stated.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall maintain a long-term archive of processed data, supported by batch ingestion of historical data for backfilling archives and training models.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Use Oracle 10G for archiving → Maintain long-term archive of processed data
- 审查问题：Given the positive dependency between 'using Oracle 10G' for archiving and 'maintain a long-term archive of all processed data', should there be an explicit obligation to ensure the long-term archive remains maintained even if Oracle 10G is no longer used?
- 场景：The requirement states that the system shall maintain a long-term archive of all processed data using Oracle 10G. The model shows that the archive maintenance function depends on Oracle 10G. Reviewers are assessing whether any obligation is missing to address archive continuity if the Oracle 10G dependency is not satisfied.
- 模型初步去向：retained
- 模型解释：The original requirement specifies maintaining a long-term archive using Oracle 10G, but does not address continuity if that technology is replaced or unavailable. The draft adds a technology-independent obligation to maintain the archive, which is an in-scope business obligation not explicitly stated in the checked original FRs.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The organization shall maintain a long-term archive of all processed data, ensuring that this obligation remains in effect regardless of the specific archiving technology used, including Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Configure Data Sources, Algorithms, and Output Formats → Log Administrative Actions and Errors
- 审查问题：Given the requirement that 'The system shall allow administrators to configure data sources, algorithms, and output formats' and the requirement to 'log all administrative actions and errors', does the system currently log an administrator's configuration of data sources, algorithms, or output formats as an administrative action?
- 场景：An administrator uses the system to configure data sources, algorithms, and output formats.
- 模型初步去向：covered
- 模型解释：Original FR-SAC-002 (FRBLOCK-006) already requires logging all administrative actions and errors, which covers logging administrator configuration of data sources, algorithms, and output formats. FR-SEC-004 (FRBLOCK-008) also provides equivalent coverage through audit logging of all user activities and system events.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：When administrators configure data sources, algorithms, or output formats, the system shall log that administrative action and any errors, in accordance with the requirement to log all administrative actions and errors.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Accept real-time data inputs from external sources → Validate incoming data and reject invalid data
- 审查问题：Does the acceptance of real-time data inputs from external sources obligate the system to validate each input against predefined quality rules and reject invalid or malformed data?
- 场景：A traffic sensor sends a real-time data message containing a temperature reading that is outside the expected range. The system receives this message through its real-time data input interface.
- 模型初步去向：covered
- 模型解释：The original FR already contains FR-DCI-002, which explicitly states that the system shall validate incoming data against predefined quality rules and reject invalid or malformed data. This establishes the validation and rejection obligation for incoming data, including the real-time data inputs accepted under FR-DCI-001. The draft obligation does not add a new requirement beyond what is already stated.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：When the system accepts real-time data inputs from external sources, it shall validate each input against predefined quality rules and reject any invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Schedule Automatic Report Generation and Email Delivery → Email Delivery
- 审查问题：Does the documented dependency between 'Schedule Automatic Report Generation and Email Delivery' and 'Email Delivery' require an explicit business obligation to ensure that scheduled report emails are actually delivered to the intended recipients?
- 场景：A user schedules automatic report generation and email delivery using the system. The system must ensure that the email delivery event occurs as scheduled.
- 模型初步去向：retained
- 模型解释：The original FR only states that users can schedule automatic report generation and email delivery; it does not explicitly require the system to perform the delivery when scheduled. The documented TRIGGERS dependency indicates that the scheduled function should trigger email delivery, making this a necessary operational obligation that is in scope but missing from the original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall deliver the generated report via email to the designated recipients when the scheduled time occurs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：High-volume data display → De-cluttering features
- 审查问题：Does the system have an explicit obligation to activate de-cluttering features when high-volume data display occurs, as implied by FR-UIP-003?
- 场景：The system is displaying a high volume of data, leading to visual complexity.
- 模型初步去向：unsupported
- 模型解释：The original FR requires the system to 'support de-cluttering features to reduce visual complexity during high-volume data display,' which implies providing the capability but does not mandate automatic activation when high-volume data is displayed. The draft obligation introduces an unsupported policy of automatic activation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：When the system is displaying a high volume of data, it shall activate de-cluttering features to reduce visual complexity.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Maintain long-term archive of processed data → Publish processed data in standardized formats
- 审查问题：When reviewing the target functional requirement 'publish processed data in standardized formats', does it explicitly specify that the data to be published is sourced from the long-term archive required by 'maintain a long-term archive of all processed data'?
- 场景：A requirements reviewer is checking whether the dependency between archiving processed data and publishing standardized data is sufficiently explicit, so that publication can rely on the archive as the authoritative source.
- 模型初步去向：retained
- 模型解释：The original FRs separately require (1) maintaining a long-term archive of all processed data and (2) publishing processed data in standardized formats, but neither explicitly states that the published data must be sourced from the long-term archive. The dependency evidence and relation support making this source explicit as an in-scope business obligation not covered by the checked original FRs.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats using the processed data maintained in the long-term archive.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools
- 审查问题：What obligation ensures that historical data ingested via batch is available for SQL-based querying after being archived?
- 场景：A user needs to query archived historical data that was backfilled via batch ingestion using SQL-based tools.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-003 already requires that users can query archived data via SQL-based tools. Historical data ingested via batch for backfilling archives becomes part of the archived data, so the draft obligation is already covered by that existing requirement.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall ensure that historical data ingested via batch for backfilling archives is queryable by users via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Detect and classify incidents → Incident reports
- 审查问题：Does the current set of functional requirements clearly and completely specify that the system must produce an incident report containing time, location, type, and severity whenever it detects and classifies an incident (e.g., crash, debris, stalled vehicle, work zone)?
- 场景：A stakeholder is reviewing the dependency between 'Detect and classify incidents' and 'Incident reports'. The quoted functional requirements state: 'The system shall detect and classify incidents such as crashes, debris, stalled vehicles, and work zones.' and 'Outputs: Incident reports with time, location, type, and severity.' The reviewer needs to determine whether the obligation to generate the report is adequately specified for every detected incident, or whether any conditions or exceptions are missing.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already specifies that the system outputs incident reports with time, location, type, and severity as part of incident detection and classification, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall generate an incident report with time, location, type, and severity for each incident that is detected and classified as a crash, debris, stalled vehicle, or work zone.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Maintain long-term archive of processed data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the requirement to 'maintain a long-term archive of all processed data' (FRBLOCK-003) sufficiently guarantee that users will be able to query archived data via SQL-based tools, or should the system explicitly require that the archive be made queryable through SQL-based interfaces?
- 场景：A requirements reviewer is evaluating the dependency between maintaining a long-term archive and allowing SQL-based queries. They must decide whether the archive maintenance obligation alone is enough to ensure queryability, without adding an additional obligation to expose the archive through SQL tools.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-003 already states the equivalent obligation: 'The system shall allow users to query archived data via SQL-based tools.' Therefore, the draft is already covered.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide SQL-based query access to the long-term archive of processed data that it maintains.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Input data fields → Normalized data stored in central database
- 审查问题：Does the specification include a requirement that, when the system accepts real-time data inputs containing the listed fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility), the system must produce normalized data stored in a central database?
- 场景：The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The accepted data fields include GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The expected output is normalized data stored in a central database.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already specifies that the system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, with input data fields including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility, and that the outputs are normalized data stored in a central database. This covers the obligation to normalize and store all accepted real-time input data fields in the central database.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall normalize and store all accepted real-time input data fields in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：47 条提名

### ISOLATED-6a9ad138716f
- 主题：Compute traffic metrics
- 审查问题：Is there a documented connection between computing traffic metrics and the data collection and ingestion requirements in FRBLOCK-001?
- 场景：The element 'Compute traffic metrics' is isolated in the graph, but computing metrics may be a downstream use of the normalized data stored by the ingestion process. The FR block only covers data ingestion, validation, configuration, and batch ingestion; it does not mention computing metrics. This review question seeks to confirm whether such a connection should be documented.
- 模型初步去向：unsupported
- 模型解释：FR-DPA-001 in FRBLOCK-002 already requires computing traffic metrics, but the draft adds an unsupported source qualifier 'from the normalized data ingested from external sources'; no original FR specifies that traffic metrics must be computed from normalized ingested data, so the added policy is not supported.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic metrics from the normalized data ingested from external sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e4e5cef90e12
- 主题：Configure new data source types without major software changes
- 审查问题：Is there a documented connection between the configuration of new data source types and the data ingestion and validation workflows in FRBLOCK-001?
- 场景：The element is isolated but has a direct FR requirement (FR-DCI-003). The review should confirm whether the configuration capability is integrated with the real-time ingestion and validation processes, or if it is standalone.
- 模型初步去向：unsupported
- 模型解释：The original FR only states that new data source types can be configured without major software changes (FR-DCI-003). It does not document integration of newly configured source types into the real-time ingestion and validation pipeline. FR-DCI-001 and FR-DCI-002 address ingestion and validation but do not link them to configured source types; therefore the draft introduces an unsupported connection.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall integrate newly configured data source types into the real-time ingestion and validation pipeline without major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9b45c5726850
- 主题：Generate statistical summaries
- 审查问题：Is there a documented connection between generating statistical summaries and the data collection and ingestion requirements in FRBLOCK-001?
- 场景：Element is isolated; generating statistical summaries may rely on the normalized data stored in the central database, but the FR block does not mention any summarization or analytics. This question asks whether such a connection should be added.
- 模型初步去向：retained
- 模型解释：No original FR states an equivalent obligation. FRBLOCK-001 only specifies that normalized data is stored in a central database, and FRBLOCK-002's statistical summary requirement does not reference the normalized data or data ingestion. The draft adds a specific in-scope connection that is not covered by the checked original FRs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall generate statistical summaries from the normalized data stored in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d3803c5f2b08
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Is there a documented connection between dynamic caching and the central database/storage requirement in FRBLOCK-001?
- 场景：Element is isolated; dynamic caching could improve access to frequently queried normalized data, but the FR block does not address caching. The review should determine if caching is implied by the storage requirement.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-003 includes FR-DSA-002: 'The system shall implement dynamic caching for frequently accessed data to improve performance,' which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall implement dynamic caching for frequently accessed normalized data to improve retrieval performance.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d5a4ce73cbfc
- 主题：Perform automated data quality checks
- 审查问题：Is there a documented connection between automated data quality checks and the validation requirement (FR-DCI-002) in FRBLOCK-001?
- 场景：Element is isolated; data quality checks may be part of the validation process, but the FR block only mentions validation against predefined quality rules without specifying automation. This question seeks to clarify whether automated checks are included.
- 模型初步去向：unsupported
- 模型解释：The draft obligation introduces a connection between automated data quality checks and validation that is not documented in the source. FR-DCI-002 requires validation against predefined quality rules but does not mention automation, and screening notes confirm FR-DPA-004 covers automated data quality checks without linking them to FR-DCI-002.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks as part of the incoming data validation process.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4f70a023572c
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Is there a documented connection between ad-hoc reporting tools and the stored normalized data in FRBLOCK-001?
- 场景：Element is isolated; ad-hoc reporting may be a user-facing feature that consumes normalized data, but the FR block only covers ingestion and storage, not reporting. This question asks whether reporting tools should be connected to the central database.
- 模型初步去向：retained
- 模型解释：No original FR states that ad-hoc reporting tools query the normalized data stored in the central database. FRBLOCK-001 only specifies that normalized data is stored in a central database, and while FR-REP-003 mentions ad-hoc reporting tools, it does not connect them to the normalized data. Therefore, this obligation is a missing in-scope requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools that query the normalized data stored in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-145532500ef6
- 主题：all users
- 审查问题：Is there a documented connection between all users and the data collection/ingestion or reporting functions in FRBLOCK-001?
- 场景：The element 'all users' is isolated; the FR block mentions external data sources (probe vehicles, sensors, etc.) but not end users who might access or consume the data. This question seeks to determine whether all users should be connected to any FR capability.
- 模型初步去向：retained
- 模型解释：No single original FR states this obligation, but FRBLOCK-005 (web-based interface for viewing data), FRBLOCK-006 (role-based access control for different user types), and FRBLOCK-008 (authentication and authorization for all users) collectively support a general user access requirement. The draft is a reasonable synthesis of these in-scope user-facing capabilities.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall provide access to relevant data and functions for all users as appropriate.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-528dc0f35b45
- 主题：Compute traffic metrics
- 审查问题：What business processes or user roles require computed traffic metrics, and what documented connections to data inputs and outputs are necessary to ensure the metric results are actionable?
- 场景：The element 'Compute traffic metrics' appears isolated in the graph; review whether its isolation is intentional or if there is a missing documented connection to data sources or downstream consumers within the FR block.
- 模型初步去向：covered
- 模型解释：The obligation is already covered by FRBLOCK-007, which requires the system to generate pre-defined reports on traffic volume, incident frequency, and road condition trends. Traffic volume is a computed traffic metric, and the reports serve as specified consumers, satisfying the draft obligation to provide computed traffic metrics to at least one specified consumer.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：If the review confirms a business need, the system shall provide computed traffic metrics to at least one specified consumer (e.g., dashboard, report, or downstream process).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c6bea276c753
- 主题：Generate statistical summaries
- 审查问题：Who are the intended users of the statistical summaries, and what business decisions or reporting requirements depend on these daily, weekly, and monthly traffic patterns?
- 场景：The element 'Generate statistical summaries' appears isolated; determine whether the isolation is acceptable or if there is a need to connect the summaries to specific reporting or decision-making processes.
- 模型初步去向：unsupported
- 模型解释：The original FR FRBLOCK-002 only requires generation of statistical summaries. It does not specify availability to authorized users or purposes such as operational reporting and trend analysis. No checked original FR supports these added policy elements, so the draft obligation introduces unsupported policy.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall make statistical summaries available to authorized users for operational reporting and trend analysis.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-13a3c520fecd
- 主题：Perform automated data quality checks
- 审查问题：What downstream processes or stakeholders rely on the results of automated data quality checks, and what should happen when anomalies or inconsistencies are flagged?
- 场景：The element 'Perform automated data quality checks' is isolated; assess whether its isolation is intentional or if there is a missing connection to alerting, data correction, or reporting workflows.
- 模型初步去向：unsupported
- 模型解释：The draft obligation adds a requirement to communicate flagged data quality issues to data stewards or log them for corrective action. The cited original FR (FRBLOCK-002) only requires automated data quality checks to flag anomalies and inconsistencies; it does not specify what happens after flagging, who receives notifications, or that issues must be logged. No other original FR covers this obligation. Therefore, the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：Flagged data quality issues shall be communicated to data stewards or logged for corrective action.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3c72313ad041
- 主题：Configure new data source types without major software changes
- 审查问题：Is the capability to configure new data source types without major software changes within the scope of the data processing and analysis FR block, and if so, what business need drives this configurability?
- 场景：The element 'Configure new data source types without major software changes' appears isolated; review whether this capability is required by the FR block's inputs (raw sensor and probe data) or if it is out of scope.
- 模型初步去向：covered
- 模型解释：An original FR already states an equivalent obligation: FRBLOCK-001 (FR-DCI-003) requires 'The system shall allow for the configuration of new data source types without requiring major software changes,' which matches the draft obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：If required, the system shall allow authorized administrators to add new data source types through configuration rather than code changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5e1c88cfabfb
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Do the data processing and analysis functions require dynamic caching for performance, and which frequently accessed data sets would benefit from such caching?
- 场景：The element 'Implement dynamic caching for frequently accessed data' is isolated; determine if performance requirements for the FR block's traffic metrics, incident reports, or summaries warrant caching.
- 模型初步去向：unresolved
- 模型解释：The original FR FR-DSA-002 (in FRBLOCK-003) already states: 'The system shall implement dynamic caching for frequently accessed data to improve performance.' The draft's caching of frequently accessed traffic metrics and incident reports, conditioned on performance requirements, falls within this general obligation and does not introduce a new unsupported policy.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：If performance requirements are confirmed, the system shall implement caching for frequently accessed traffic metrics and incident reports to meet response time targets.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6d3c31b4fc90
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Which user roles require ad-hoc reporting capabilities over the data produced by the FR block, and what data domains should be accessible for ad-hoc querying?
- 场景：The element 'Provide Ad-hoc Reporting Tools' appears isolated; assess whether the statistical summaries or incident reports require user-driven ad-hoc reporting tools, or if predefined reports suffice.
- 模型初步去向：retained
- 模型解释：The original FRs include a general ad-hoc reporting tools requirement (FR-REP-003) but do not specify the data domains or user roles for ad-hoc querying. The draft obligation is supported by FRBLOCK-002 outputs (traffic metrics, incident data) and FRBLOCK-006 role-based access control, but the original FRs lack the specific scoping to traffic metrics and incident data.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：If ad-hoc reporting is needed, the system shall provide a reporting tool that allows authorized users to query and visualize traffic metrics and incident data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-423784cd3d3d
- 主题：all users
- 审查问题：Who are the 'all users' referenced in the context of the FR block, and what access or interaction do they need with the data processing and analysis functions?
- 场景：The element 'all users' is isolated; clarify the user roles and their permissions or interactions with the system functions described in FRBLOCK-002.
- 模型初步去向：unsupported
- 模型解释：The draft introduces an obligation to define user roles and access levels for data processing and analysis outputs, but none of the original FRs specify user roles, access levels, or interactions with these outputs. Existing role-based access control and authentication requirements are general and do not cover this specific context.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall define user roles and access levels for interacting with the data processing and analysis outputs, such as incident reports and traffic metrics.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-552841eb97af
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Does the FR block document a connection between the dynamic caching function and the long-term archive or data purging functions, or is it isolated as a standalone requirement?
- 场景：A reviewer is checking whether FR-DSA-002's caching requirement has any documented dependencies or interactions with the archival (FR-DSA-001) and purging (FR-DSA-004) requirements.
- 模型初步去向：unsupported
- 模型解释：The original FRs treat dynamic caching, long-term archive, and data purging as separate requirements with no documented connection or integration. The draft introduces a new obligation to document integration, which is not stated or supported by any original FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall document how dynamic caching integrates with archived data storage and automated purging policies to ensure consistent data management.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a6213748a89d
- 主题：all users
- 审查问题：Does the FR block document that 'all users' (as opposed to a limited subset) are intended to have query access to archived data, and how that access is governed?
- 场景：A reviewer is checking whether the FR block clarifies the scope of users who can query archived data, given that the isolated element 'all users' may imply a broader audience than the generic term 'users'.
- 模型初步去向：retained
- 模型解释：The original FR block states that users can query archived data via SQL-based tools, but it does not define which user roles are included in 'all users' or document the authorization model for querying archived data. This is an in-scope governance obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall define the user roles included in 'all users' and document the authorization model for querying archived data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a3b21d3568fe
- 主题：Compute traffic metrics
- 审查问题：Does FR-DPO-001 (publish processed data) imply that the system must compute traffic metrics as part of generating processed data, and should this isolated element be explicitly connected to the FR block?
- 场景：A reviewer notices that the FR block requires publishing processed data but does not explicitly state how traffic metrics are computed; the isolated element 'Compute traffic metrics' may need a documented connection to the publication requirement.
- 模型初步去向：covered
- 模型解释：The original FR block FRBLOCK-002 includes FR-DPA-001, which already explicitly requires the system to compute traffic metrics including congestion levels, travel times, queue lengths, and traffic flow patterns. Therefore the draft obligation to compute traffic metrics is already covered by an original FR, even though the specific linkage to FR-DPO-001 is not explicitly stated.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic metrics necessary for the processed data published per FR-DPO-001.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e706bcc1f073
- 主题：Configure new data source types without major software changes
- 审查问题：Should the system's ability to configure new data source types without major software changes be explicitly linked to the real-time data feed requirement, given that new data sources may affect feed content?
- 场景：The FR block requires providing real-time data feeds to MI Drive; the isolated element about configuring new data source types could be relevant to maintaining those feeds when data sources change.
- 模型初步去向：retained
- 模型解释：The draft obligation combines the existing ability to configure new data source types without major software changes (FR-DCI-003) with the real-time data feed requirement (FRBLOCK-004). No single original FR explicitly links the configurability to supporting real-time feed operations, so the linkage is a new business obligation not covered by the checked FRs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall allow configuration of new data source types without major software changes to support ongoing real-time data feed operations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f862d2ee57a6
- 主题：Generate statistical summaries
- 审查问题：Does the publication of processed data require generating statistical summaries, and should this isolated element be connected to FR-DPO-001?
- 场景：The FR block specifies publishing processed data in standardized formats; statistical summaries could be a form of processed data that requires explicit coverage.
- 模型初步去向：covered
- 模型解释：An original FR already states the core obligation: FRBLOCK-002 (FR-DPA-006) requires generating statistical summaries of traffic patterns. The draft's added publication context is already addressed by FRBLOCK-004, which requires publishing processed data in standardized formats.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall generate statistical summaries as part of processed data publication.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-70ec85628d1c
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Should the requirement for real-time data feeds include dynamic caching to ensure performance, and does the isolated element need a documented connection to FR-DPO-002?
- 场景：The FR block mandates real-time data feeds to MI Drive; dynamic caching could be necessary to meet real-time performance expectations.
- 模型初步去向：unresolved
- 模型解释：The original FR-DSA-002 (within FRBLOCK-003) already states: 'The system shall implement dynamic caching for frequently accessed data to improve performance.' The draft obligation adds a specific rationale ('to support real-time data feed performance') but does not introduce a new functional requirement; the core caching requirement is equivalent and already covered.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall implement dynamic caching for frequently accessed data to support real-time data feed performance.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d6d425e041af
- 主题：Perform automated data quality checks
- 审查问题：Should automated data quality checks be explicitly required before publishing processed data, and does this isolated element need to be linked to FR-DPO-001?
- 场景：The FR block requires publishing processed data but does not mention quality checks; quality checks may be essential to ensure data integrity.
- 模型初步去向：retained
- 模型解释：No original FR explicitly requires automated data quality checks immediately prior to publication in standardized formats. FRBLOCK-002 already requires automated quality checks generally, and FRBLOCK-004 requires publication in standardized formats, but the specific sequencing is not stated. The combined obligation is a supported, in-scope business rule.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks on data prior to publication in standardized formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d35160fe9658
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Should the system provide ad-hoc reporting tools to support the data export formats required by FR-DPO-004, and does this isolated element need a connection?
- 场景：The FR block requires exporting data in CSV, JSON, XML, and KML; ad-hoc reporting tools could utilize these export capabilities for user-generated reports.
- 模型初步去向：retained
- 模型解释：The original FRs require data export in CSV, JSON, XML, and KML (FRBLOCK-004) and include ad-hoc reporting tools (FR-REP-003 within FRBLOCK-007) as separate capabilities, but no original FR explicitly requires that ad-hoc reporting tools leverage these export formats for user-defined reports. The draft adds a reasonable in-scope integration of these existing capabilities.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools that leverage the supported export formats for user-defined reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-92597f20b89b
- 主题：all users
- 审查问题：Should the FR block clarify whether the API provided for external applications is accessible to all users, and does the isolated element 'all users' need to be connected to FR-DPO-005?
- 场景：The FR block states an API for external applications but does not specify user scope; the isolated element 'all users' could indicate a requirement for unrestricted access.
- 模型初步去向：unsupported
- 模型解释：The original FR-DPO-005 only requires an API for external applications to consume data in real time. It does not specify accessibility to all users or authorized users. The isolated phrase 'all users' appears in a different context (secure authentication and authorization) and is not equivalent to API accessibility. The draft obligation introduces an access-control requirement not present in the source.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall ensure the real-time data API is accessible to all authorized users.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1aeec962678a
- 主题：Compute traffic metrics
- 审查问题：Does the UI FR block require a documented connection to the isolated element 'Compute traffic metrics'? The FR references traffic data but does not specify computation of metrics for map display.
- 场景：A reviewer notes that 'Compute traffic metrics' is graph-isolated and might be needed to support traffic icon layers in the map, but isolation alone does not establish a gap.
- 模型初步去向：unresolved
- 模型解释：The draft obligation is conditional on stakeholder confirmation, and none of the checked original FRs explicitly state a requirement to compute traffic metrics specifically to support UI traffic icon layers. While FRBLOCK-002 mentions computation of traffic metrics and FRBLOCK-005 mentions UI traffic icon layers, no original FR links the two, and the nomination itself notes that isolation alone does not establish a gap. Therefore, evidence is insufficient to determine whether this should be retained as a new in-scope obligation or treated as unsupported.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If stakeholders confirm the need, the system shall compute traffic metrics sufficient to support the traffic icon layers specified in FR-UIP-002.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3dbe5b081f31
- 主题：Configure new data source types without major software changes
- 审查问题：Should the UI FR block require that the system can configure new data source types without major software changes, given that FR-UIP-001 lists specific data types but does not address extensibility?
- 场景：The isolated element suggests a possible need for the UI to display data from sources beyond traffic, incident, traveler, and weather, but no explicit requirement exists.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already contains FR-DCI-003, which states: 'The system shall allow for the configuration of new data source types without requiring major software changes.' This is equivalent to the proposed obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall allow configuration of new data source types for display in the web interface without major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5fcdc00840d6
- 主题：Generate statistical summaries
- 审查问题：Does the UI FR block need to include a requirement to generate statistical summaries of the displayed data, or is raw data viewing sufficient?
- 场景：The FR defines viewing and filtering of data but does not mention generation of summaries, leaving ambiguity about whether statistical summarization is in scope.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-007 already requires generation of pre-defined reports on traffic volume, incident frequency, and road condition trends, which are statistical summaries. Therefore the UI FR block does not need a separate requirement to generate statistical summaries; the obligation is already covered.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If required, the system shall generate statistical summaries of traffic, incident, traveler, and weather data for presentation in the web interface.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-815639d82b2b
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Is dynamic caching for frequently accessed data required to meet the UI's performance expectations during high-volume data display, as referenced in FR-UIP-003?
- 场景：FR-UIP-003 addresses visual complexity but not performance optimization; the isolated element hints at a possible performance requirement.
- 模型初步去向：covered
- 模型解释：An original FR already states an equivalent obligation. FRBLOCK-003 includes FR-DSA-002: 'The system shall implement dynamic caching for frequently accessed data to improve performance.' This directly specifies dynamic caching for frequently accessed data to support performance, which covers the draft obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If performance requirements dictate, the system shall implement dynamic caching for frequently accessed data to support high-volume data display.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1579422d4802
- 主题：Perform automated data quality checks
- 审查问题：Should the UI FR block require automated data quality checks on the data sources it displays, to ensure that filtering and map layers present valid information?
- 场景：FR-UIP-004 provides filtering but does not address data quality assurance before display, leaving a potential gap that stakeholders may need to close.
- 模型初步去向：covered
- 模型解释：Original functional requirements already impose automated data quality checks on incoming data sources. FR-DCI-002 (via FRBLOCK-001) requires validation against predefined quality rules and rejection of invalid data, and FR-DPA-004 (via FRBLOCK-002) requires automated data quality checks to flag anomalies and inconsistencies. These obligations ensure that only valid data is available for display through filtering and map layers.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If data quality is a concern, the system shall perform automated data quality checks on incoming traffic, incident, traveler, and weather data before display.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ebe26af2b768
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Does the FR block's support for custom dashboards imply a need for ad-hoc reporting tools, or are custom dashboards the intended limit of user-driven data views?
- 场景：FR-UIP-006 enables custom dashboards; 'Provide Ad-hoc Reporting Tools' is isolated, and stakeholders should clarify whether reporting is a separate requirement.
- 模型初步去向：covered
- 模型解释：An original FR already requires ad-hoc reporting tools for querying and visualizing data (FRBLOCK-007 / FR-REP-003), which covers the nominated obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If reporting is required, the system shall provide ad-hoc reporting tools that can access the same data as custom dashboards.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b409cef95a59
- 主题：all users
- 审查问题：Should the FR block explicitly state that the web-based interface and UI features are available to all users, or are there role-based restrictions to define?
- 场景：'all users' is isolated; FR-UIP-005 mentions diverse user groups, but the scope of 'all users' and any access controls are not specified.
- 模型初步去向：retained
- 模型解释：The original FRs specify the web-based interface and UI features (FRBLOCK-005) and secure authentication and authorization for all users (FRBLOCK-006, FRBLOCK-008), but no original FR explicitly states that the web-based interface and its features are available to all users with those controls. This is an in-scope business obligation that fills the identified gap without introducing unsupported policy.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall provide access to the web-based interface and its features to all users, with appropriate authentication and authorization controls.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-36d9a384cced
- 主题：Compute traffic metrics
- 审查问题：Does FR-SAC-001's allowance to configure algorithms include the ability to compute traffic metrics, or is traffic metrics computation a separate requirement?
- 场景：An administrator wants to configure an algorithm to compute traffic metrics using the system's configuration capabilities.
- 模型初步去向：unsupported
- 模型解释：The draft combines two separate original obligations: FRBLOCK-006 allows administrators to configure algorithms, and FRBLOCK-002 requires the system to compute traffic metrics. No original FR requires that traffic metrics computation be provided as part of configurable algorithms. The draft therefore introduces an unsupported linkage.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall provide the capability to compute traffic metrics as part of configurable algorithms.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-cd50d96f97f8
- 主题：Configure new data source types without major software changes
- 审查问题：Does the requirement to configure data sources include adding new data source types without major software changes, or is this covered elsewhere?
- 场景：An administrator needs to add a new type of data source to the system without requiring a major software update.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states an equivalent obligation: 'The system shall allow for the configuration of new data source types without requiring major software changes.'
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall allow administrators to configure new data source types without requiring major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9e3131c6d8e5
- 主题：Generate statistical summaries
- 审查问题：Does the configurability of output formats include generating statistical summaries, or is that a separate analytics capability?
- 场景：An analyst wants to generate statistical summaries as part of the system's output configuration.
- 模型初步去向：unsupported
- 模型解释：The evidence shows that configurability of output formats (FRBLOCK-006) and generation of statistical summaries (FRBLOCK-002) are separate original requirements; no source text links statistical summaries to configurable output formats. The draft's assertion that statistical summaries are generated as part of configurable output formats introduces an unsupported integration.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall generate statistical summaries as part of configurable output formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-392a7ee52668
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Does the configuration of data sources include dynamic caching options for frequently accessed data?
- 场景：An administrator wants to enable dynamic caching for data sources that are accessed frequently to improve performance.
- 模型初步去向：retained
- 模型解释：The draft combines an existing dynamic caching obligation (identified in FRBLOCK-003) with the data source configuration capability (FRBLOCK-006). While no single original FR explicitly states that dynamic caching is configurable as part of data source settings, both components are supported by the checked original FRs, and the combined obligation is in scope.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall implement dynamic caching for frequently accessed data as part of data source configuration.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-434ca1eb9c89
- 主题：Perform automated data quality checks
- 审查问题：Does data source configuration include automated data quality checks, or is that a separate requirement?
- 场景：An administrator configures a data source and expects the system to automatically verify data quality before use.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-002 already states an equivalent obligation: 'The system shall perform automated data quality checks to flag anomalies and inconsistencies.' This covers the draft requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks on configured data sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1d8301ce8c66
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Does the requirement to configure output formats include providing ad-hoc reporting tools, or is that a separate user-facing capability?
- 场景：An analyst wants to create ad-hoc reports using the system's output configuration features.
- 模型初步去向：unsupported
- 模型解释：The original FRs require ad-hoc reporting tools (FR-REP-003) and configurable/exportable output formats separately, but none states that ad-hoc reporting tools are part of configurable output formats. The draft introduces an unsupported conflation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools as part of configurable output formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f4f4ee6557c3
- 主题：all users
- 审查问题：Is 'all users' intended to be a separate role in the role-based access control model, or does it refer to the set of all user types collectively?
- 场景：The requirement mentions user types like field operator, analyst, and admin, but 'all users' appears as a distinct concept that may need clarification.
- 模型初步去向：unresolved
- 模型解释：The draft obligation requires the system to clarify the meaning of 'all users', but the source text does not assign such a clarification function to the system; clarifying terminology is a specification issue, not a system behavior.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall clarify the scope of 'all users' in the context of role-based access control.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-34294aa28f36
- 主题：Compute traffic metrics
- 审查问题：Does FRBLOCK-007 need to explicitly document a connection to computing traffic metrics, or is this computation assumed to be part of the pre-defined report generation?
- 场景：The isolated element 'Compute traffic metrics' may be a prerequisite for generating the traffic volume reports specified in FR-REP-001.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-007 already states generating pre-defined reports on traffic volume, incident frequency, and road condition trends, which inherently requires computing those metrics. The draft obligation does not introduce a new unsupported requirement; it makes explicit what is implied by the existing FR.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic volume, incident frequency, and road condition trend metrics as required by the pre-defined reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-a9aa65bd95b9
- 主题：Configure new data source types without major software changes
- 审查问题：Should FRBLOCK-007 specify that new data source types can be configured without major software changes, given the ad-hoc reporting tools?
- 场景：The ad-hoc reporting tools in FR-REP-003 may require data from new sources; this isolated element could be a scalability requirement.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-001 already states an equivalent obligation: 'The system shall allow for the configuration of new data source types without requiring major software changes.' This broadly covers the proposed obligation, including for ad-hoc reporting.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow configuration of new data source types for ad-hoc reporting without major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-3e877819037b
- 主题：Generate statistical summaries
- 审查问题：Does FRBLOCK-007 require the generation of statistical summaries beyond the listed pre-defined reports?
- 场景：The pre-defined reports include trends, but statistical summaries may be an additional analysis capability.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-007 requires only pre-defined reports on traffic volume, incident frequency, and road condition trends, plus user-driven ad-hoc querying/visualization. It does not mandate system-generated statistical summaries beyond those pre-defined reports, so the draft introduces an unsupported general obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall generate statistical summaries as part of the reporting and analytics functionality.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d6410fda79c5
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Should FRBLOCK-007 address dynamic caching to support performance of reporting and analytics?
- 场景：Reporting and analytics may require frequent data access; dynamic caching could be a non-functional requirement.
- 模型初步去向：covered
- 模型解释：FRBLOCK-003 already states 'The system shall implement dynamic caching for frequently accessed data to improve performance.' This general requirement encompasses reporting and analytics data as frequently accessed data, so the proposed obligation is already covered.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall implement dynamic caching for frequently accessed reporting and analytics data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-03d13ef9b6b1
- 主题：Perform automated data quality checks
- 审查问题：Is automated data quality checking within the scope of FRBLOCK-007, given its focus on reporting and analytics?
- 场景：The accuracy of reports depends on data quality; this isolated element may need to be connected.
- 模型初步去向：covered
- 模型解释：Original FRs FRBLOCK-001 and FRBLOCK-002 already state equivalent obligations for automated data quality checks: FRBLOCK-001 requires validation of incoming data against predefined quality rules and rejection of invalid data; FRBLOCK-002 requires automated data quality checks to flag anomalies and inconsistencies. The draft obligation does not add a new requirement.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks to ensure the integrity of data used in reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-893aa04d89fe
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Although FR-REP-003 requires ad-hoc reporting tools, should FRBLOCK-007 explicitly connect this element to the data query and visualization capabilities?
- 场景：The element is already mentioned but may be isolated in the architecture; the FR block may need to clarify its integration.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 (FR-REP-003) already states the obligation to provide ad-hoc reporting tools for querying and visualizing data. The draft obligation's reference to integration with reporting and analytics data sources is inherently covered by the existing query and visualization capability; no new distinct requirement is introduced.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools that are integrated with the overall reporting and analytics data sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7eac1a48ea6a
- 主题：all users
- 审查问题：Should FRBLOCK-007 clarify which user roles are included in 'all users' for scheduling and report delivery?
- 场景：FR-REP-002 refers to 'users', but the isolated element 'all users' may need explicit role-based access definition.
- 模型初步去向：unsupported
- 模型解释：The original FRBLOCK-007 only permits users to schedule automatic report generation and email delivery; it does not define user roles, mention 'all users', or require access control for scheduling/report delivery. The draft introduces a new role-based access policy not supported by the source.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall define and enforce user roles for scheduling and receiving reports, ensuring 'all users' have appropriate access.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ef3dd992ef67
- 主题：Compute traffic metrics
- 审查问题：Should the computation of traffic metrics be considered a system event that must be included in audit logging?
- 场景：An administrator generates traffic metrics; this action may need to be recorded for security auditing.
- 模型初步去向：covered
- 模型解释：FRBLOCK-008 (FR-SEC-004) already requires audit logging of all system events. The computation and access of traffic metrics qualify as system events under that broad requirement, so the draft obligation does not add a new requirement.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall include the generation and access of computed traffic metrics in the audit log of system events.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e5bae3bfcaa2
- 主题：Configure new data source types without major software changes
- 审查问题：Must data transmissions from newly configured data source types comply with TLS 1.2 or higher encryption?
- 场景：A user configures a new external data source type; the system must ensure that all data transmissions from that source are encrypted accordingly.
- 模型初步去向：covered
- 模型解释：The original FR already states that all data transmissions must be encrypted using TLS 1.2 or higher, which encompasses transmissions from newly configured data source types.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall enforce TLS 1.2 or higher encryption for all data transmissions, including those from newly configured data source types.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-bd4bdfaff7d5
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Should Ad-hoc Reporting Tools enforce secure authentication and authorization for all users accessing them?
- 场景：A user uses the ad-hoc reporting tool to generate a report; the system must ensure only authorized users can access the tool.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-008 already requires secure authentication and authorization for all users, which includes users accessing Ad-hoc Reporting Tools.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall require secure authentication and authorization for any user accessing Ad-hoc Reporting Tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：0 条提名

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall publish processed data resulting from batch ingestion of historical data in standardized formats (SAE J2354, TMDD).

2. [model_preliminarily_retained] The system shall maintain a long-term archive of all processed data, ensuring that this obligation remains in effect regardless of the specific archiving technology used, including Oracle 10G.

3. [model_preliminarily_retained] The system shall deliver the generated report via email to the designated recipients when the scheduled time occurs.

4. [model_preliminarily_retained] The system shall publish processed data in standardized formats using the processed data maintained in the long-term archive as the authoritative source.

5. [model_preliminarily_retained] The system shall generate statistical summaries from the normalized data stored in the central database.

6. [model_preliminarily_retained] The system shall provide ad-hoc reporting tools that allow users to query the normalized data stored in the central database.

7. [model_preliminarily_retained] The system shall provide access to relevant data and functions for all users as appropriate.

8. [model_preliminarily_retained] The system shall provide ad-hoc reporting tools for authorized users to query and visualize traffic metrics and incident data, with user access controlled by the existing role-based access control policy.

9. [model_preliminarily_retained] The system shall define the user roles included in 'all users' and document the authorization model for querying archived data.

10. [model_preliminarily_retained] The system shall allow configuration of new data source types without major software changes to support ongoing real-time data feed operations.

11. [model_preliminarily_retained] The system shall perform automated data quality checks on data prior to publication in standardized formats.

12. [model_preliminarily_retained] The system shall provide ad-hoc reporting tools that allow users to define and generate reports using the supported data export formats (CSV, JSON, XML, KML).

13. [model_preliminarily_retained] The system shall provide all users with access to the web-based interface and its features, subject to authentication and authorization controls as specified in the security requirements.

14. [model_preliminarily_retained] The system shall allow administrators to configure dynamic caching options for frequently accessed data as part of data source configuration.
