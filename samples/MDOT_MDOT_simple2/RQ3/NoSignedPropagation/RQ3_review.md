# RQ3 审查材料：MDOT_MDOT_simple2 / NoSignedPropagation

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
- 主题：Use Oracle 10G for archiving → Allow users to query archived data via SQL-based tools
- 审查问题：Does the requirements specification explicitly state that the SQL-based query tools must be able to access the archive data stored in Oracle 10G, ensuring the dependency between 'Use Oracle 10G for archiving' and 'Allow users to query archived data via SQL-based tools' is fulfilled?
- 场景：FRBLOCK-003 contains the statements 'using Oracle 10G', 'maintain a long-term archive of all processed data', and 'allow users to query archived data via SQL-based tools'. The dependency analysis shows that the ability to query archived data depends on the archive maintained using Oracle 10G. The reviewer must verify whether an explicit requirement connects the Oracle 10G archive to the SQL query capability.
- 模型初步去向：covered
- 模型解释：FRBLOCK-003 explicitly requires the system to maintain a long-term archive of processed data using Oracle 10G (FR-DSA-001) and to allow users to query archived data via SQL-based tools (FR-DSA-003). Together these statements establish the obligation that SQL-based query tools can access the Oracle 10G archive.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall allow users to query the long-term archive of processed data, which is maintained using Oracle 10G, via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Support batch ingestion of historical data → Support machine learning models
- 审查问题：Is there an explicit requirement ensuring that the batch-ingested historical data is available and suitable for training the machine learning models that perform predictive analysis of traffic trends and incident likelihood?
- 场景：The system shall support batch ingestion of historical data for backfilling archives and training models, and shall support machine learning models for predictive analysis of traffic trends and incident likelihood. The documented dependency indicates that batch ingestion enables model training.
- 模型初步去向：retained
- 模型解释：The original FRs separately require batch ingestion of historical data for training models (FRBLOCK-001) and support for machine learning models for predictive analysis of traffic trends and incident likelihood (FRBLOCK-002), but none explicitly states that the batch-ingested historical data must be made available and suitable for training those ML models. The documented dependency between the two capabilities supports deriving this obligation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall ensure that historical data ingested in batch is made available and suitable for training the machine learning models used for predictive analysis of traffic trends and incident likelihood.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Accept real-time data inputs from external sources → Normalized data stored in central database
- 审查问题：Does the system requirement define an obligation to normalize and store all accepted real-time data inputs from external sources in the central database?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, and normalized data is stored in a central database.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already specifies that the system accepts real-time data inputs from external sources and that the outputs are normalized data stored in a central database, which directly covers the obligation to normalize and store all accepted real-time data inputs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall ensure that all accepted real-time data inputs from external sources are normalized and stored in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports
- 审查问题：Does the requirement 'schedule automatic report generation and email delivery' necessitate that the system generate the pre-defined reports on traffic volume, incident frequency, and road condition trends, given that the source quote only mentions scheduling and the target quote only specifies report types?
- 场景：A user schedules automatic report generation and email delivery, and the system is expected to generate pre-defined reports on traffic volume, incident frequency, and road condition trends.
- 模型初步去向：covered
- 模型解释：Original FR-REP-001 requires the system to generate pre-defined reports on traffic volume, incident frequency, and road condition trends, and FR-REP-002 allows users to schedule automatic report generation and email delivery. The draft obligation is already covered by these requirements.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall generate pre-defined reports on traffic volume, incident frequency, and road condition trends in accordance with the scheduled automatic report generation and email delivery.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Automated data purging policies → Support automated data purging policies
- 审查问题：Does the system's support for automated data purging policies correctly depend on the existence of automated data purging policies as described in FRBLOCK-003?
- 场景：A requirements reviewer examines the dependency between 'automated data purging policies' and 'support automated data purging policies' in FRBLOCK-003.
- 模型初步去向：unsupported
- 模型解释：The draft obligation adds a condition—that support applies only when automated data purging policies are defined and active—that is not stated in FRBLOCK-003 or any other checked original FR. FRBLOCK-003 requires support for automated data purging policies but does not make that support conditional on policy existence or active status.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall support automated data purging policies when automated data purging policies are defined and active.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Use Oracle 10G for archiving → Publish processed data in standardized formats
- 审查问题：Is the target requirement 'publish processed data in standardized formats' correctly conditioned on the source constraint 'using Oracle 10G'? Specifically, should the system be required to publish processed data only if the archive uses Oracle 10G, or are these requirements independent despite the modeled dependency?
- 场景：The system must maintain a long-term archive of all processed data using Oracle 10G (FR quote: 'using Oracle 10G'). The system must also publish processed data in standardized formats (FR quote: 'publish processed data in standardized formats'). The ACE priority score suggests a dependency chain: publishing processed data depends on the long-term archive, which depends on using Oracle 10G. A reviewer must decide whether the source constraint 'using Oracle 10G' is a necessary precondition for the target obligation.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-004 (FR-DPO-001) already states an unconditional obligation to publish processed data in standardized formats, with no condition relating to Oracle 10G. The source constraint 'using Oracle 10G' applies only to the long-term archive in FRBLOCK-003. No original FR conditions publication on the archive technology, so the draft's conditional clause is an unsupported policy.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats (SAE J2354, TMDD) when the long-term archive of processed data is maintained using Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Input data fields → Validate incoming data and reject invalid data
- 审查问题：Does the validation requirement 'The system shall validate incoming data against predefined quality rules and reject invalid or malformed data' explicitly ensure that each of the input data fields listed in the source ('GPS data, speed, location, road condition reports, temperature, precipitation, visibility') is subject to those quality rules and rejection criteria?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, including the fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The validation process is active, checking incoming data against predefined quality rules and rejecting invalid or malformed data.
- 模型初步去向：retained
- 模型解释：Original FR-DCI-002 states validation generally for incoming data but does not explicitly enumerate the input data fields; none of the other original FR blocks cover field-level validation. The dependency evidence identifies the listed fields as part of incoming data, so making the field-level scope explicit is supported.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall apply predefined quality rules to each of the following input data fields—GPS data, speed, location, road condition reports, temperature, precipitation, and visibility—and reject any incoming record where one or more of these fields is invalid or malformed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Support batch ingestion of historical data → Publish processed data in standardized formats
- 审查问题：Does the requirement to support batch ingestion of historical data for backfilling archives need to explicitly require that the ingested historical data be processed and published in standardized formats (SAE J2354, TMDD), or is the dependency between batch ingestion and publishing adequately covered by existing FRs?
- 场景：Historical data is ingested via batch to backfill archives. After processing, the data must be published in standardized formats for downstream consumers. The current FRs state that the system shall support batch ingestion for backfilling archives and training models, and that the system shall publish processed data in standardized formats. However, no FR explicitly links batch-ingested historical data to the publishing step, leaving uncertainty about whether backfilled data will be published.
- 模型初步去向：retained
- 模型解释：Existing FRs separately require batch ingestion of historical data for backfilling archives (FRBLOCK-001), maintaining a long-term archive of processed data (FRBLOCK-003), and publishing processed data in standardized formats (FRBLOCK-004), but no FR explicitly links batch-ingested historical data to the processing and publishing steps. This creates ambiguity about whether backfilled data will be published in standardized formats. The obligation clarifies this required dependency.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall ensure that historical data ingested via batch for archive backfill is processed and made available for publishing in standardized formats (SAE J2354, TMDD).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Input data fields → Accept real-time data inputs from external sources
- 审查问题：Does the functional requirement 'The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems' explicitly require the system to accept all listed input data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility?
- 场景：A requirements engineer is reviewing the dependency between the source data fields and the target acceptance function to determine if the obligation to process these specific fields is explicitly stated.
- 模型初步去向：covered
- 模型解释：The original FRBLOCK-001 already includes an Inputs list that enumerates GPS data, speed, location, road condition reports, temperature, precipitation, and visibility, and it explicitly requires accepting real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. Therefore the draft obligation is already stated in the original requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall accept real-time data inputs that include GPS data, speed, location, road condition reports, temperature, precipitation, and visibility from probe vehicles, traffic sensors, weather stations, and traveler information systems.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Support batch ingestion of historical data → Maintain long-term archive of processed data
- 审查问题：Does the source requirement 'The system shall support batch ingestion of historical data for backfilling archives and training models' adequately ensure the target obligation 'Maintain long-term archive of processed data' is met, considering that 'backfilling archives' may describe a one-time historical data load rather than the ongoing maintenance required by the target?
- 场景：The system has been implemented to support batch ingestion of historical data for backfilling archives and training models, as stated in FRBLOCK-001. After the initial backfill, no separate requirement explicitly mandates that the archive of processed data be actively maintained and updated with new processed data. Review whether the ENABLES relationship from batch ingestion to long-term archive maintenance is valid.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-003 already states an equivalent obligation: 'The system shall maintain a long-term archive of all processed data using Oracle 10G.' This directly requires ongoing archival of processed data, not just initial backfill.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall maintain the long-term archive of processed data by ensuring that all processed data, including newly ingested data, is archived and preserved over time, not only during initial backfill.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Use Oracle 10G for archiving → Maintain long-term archive of processed data
- 审查问题：Is the dependency between 'use Oracle 10G for archiving' and 'maintain a long-term archive of all processed data' adequately represented in the requirements, or does the archive requirement need to explicitly state that Oracle 10G is the storage technology?
- 场景：The system is required to maintain a long-term archive of all processed data, and the architecture specifies using Oracle 10G for archiving. The requirements may need to clarify that the archive obligation depends on the Oracle 10G technology.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-003 already states the equivalent obligation: 'The system shall maintain a long-term archive of all processed data using Oracle 10G.' Therefore the dependency is already represented in the requirements.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall maintain a long-term archive of all processed data using Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Configure Data Sources, Algorithms, and Output Formats → Log Administrative Actions and Errors
- 审查问题：Should each administrative configuration of data sources, algorithms, or output formats be logged as an administrative action under the requirement to log all administrative actions and errors?
- 场景：An administrator changes the output format setting using the system's configuration capability. The system currently may allow this configuration but the requirement to log all administrative actions and errors does not explicitly state that configuration changes must be logged.
- 模型初步去向：covered
- 模型解释：FR-SAC-002 in FRBLOCK-006 already requires logging all administrative actions; an administrator configuring data sources, algorithms, or output formats is an administrative action, so the draft obligation is an instance of that existing requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：When an administrator configures data sources, algorithms, or output formats, the system shall log that configuration action as an administrative action.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Accept real-time data inputs from external sources → Validate incoming data and reject invalid data
- 审查问题：Does the acceptance of real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems necessarily enable the validation of incoming data against predefined quality rules and the rejection of invalid or malformed data, and is this dependency accurately captured by an ENABLES relation?
- 场景：The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The system shall validate incoming data against predefined quality rules and reject invalid or malformed data. The documented dependency states that acceptance of these data inputs enables the validation process.
- 模型初步去向：covered
- 模型解释：The original FR block FRBLOCK-001 already contains the obligations to accept real-time data inputs from the specified sources (FR-DCI-001) and to validate incoming data against predefined quality rules and reject invalid or malformed data (FR-DCI-002). The draft obligation combines these existing requirements but adds no new business obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall, upon accepting real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, validate the incoming data against predefined quality rules and reject invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Schedule Automatic Report Generation and Email Delivery → Email Delivery
- 审查问题：Does the system explicitly require that when users schedule automatic report generation and email delivery, the email is delivered to the designated recipients?
- 场景：A user schedules a report for automatic generation and email delivery. The expectation is that the scheduled report email is delivered to the designated recipients.
- 模型初步去向：retained
- 模型解释：The original FR FRBLOCK-007 only requires that users can schedule automatic report generation and email delivery; it does not explicitly state that the email is delivered to the designated recipients. The dependency evidence indicates that scheduling triggers email delivery, making the delivery to designated recipients an implied business obligation that is not covered by the original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall deliver the scheduled report email to the designated recipients when automatic report generation and email delivery is scheduled.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：High-volume data display → De-cluttering features
- 审查问题：Does the system activate de-cluttering features when high-volume data display occurs, as required to reduce visual complexity?
- 场景：The system is currently displaying a high volume of data, causing visual complexity. In this situation, de-cluttering features should be triggered to reduce the visual load on the user.
- 模型初步去向：covered
- 模型解释：The original FR in FRBLOCK-005 already states an equivalent obligation: it requires the system to support de-cluttering features to reduce visual complexity during high-volume data display, which covers activation of de-cluttering when high-volume data display occurs.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall activate de-cluttering features whenever high-volume data display is detected, to reduce visual complexity as specified.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Maintain long-term archive of processed data → Publish processed data in standardized formats
- 审查问题：Given that the system maintains a long-term archive of all processed data, is there a missing obligation to publish processed data in standardized formats (SAE J2354, TMDD) from that archive?
- 场景：Review the dependency between 'maintain a long-term archive of all processed data' and 'publish processed data in standardized formats'. The model suggests publishing processed data depends on the archive as the data source, but no explicit requirement linking the two has been identified.
- 模型初步去向：unsupported
- 模型解释：The original FRs separately require maintaining a long-term archive of processed data (FRBLOCK-003) and publishing processed data in standardized formats (FRBLOCK-004), but neither requires that the publication use the archive as its data source. The draft adds a source constraint not present or supported by the original FRs.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats (SAE J2354, TMDD) using data from the long-term archive of all processed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the system's support for batch ingestion of historical data for backfilling archives ensure that users are able to query archived data via SQL-based tools, as documented in the requirement 'maintain a long-term archive of all processed data' and 'allow users to query archived data via SQL-based tools'?
- 场景：A data engineer triggers batch ingestion of historical data to backfill archives. After the ingestion completes, a data analyst attempts to query the archived data using a SQL-based tool. The review should assess whether the dependency from batch ingestion to SQL-based querying of archived data is valid based on the stated requirements.
- 模型初步去向：covered
- 模型解释：The original FRs already state equivalent obligations: FRBLOCK-001 requires supporting batch ingestion of historical data for backfilling archives, and FRBLOCK-003 requires allowing users to query archived data via SQL-based tools. Together these cover the draft's requirement that after backfilling, users can query archived data via SQL; the maintain-a-long-term-archive aspect is inherent in the query requirement for 'archived data'.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall maintain a long-term archive of all processed data such that after batch ingestion of historical data backfills the archive, users can query the archived data via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Detect and classify incidents → Incident reports
- 审查问题：What functional requirement or obligation ensures that the system's detection and classification of an incident leads to the generation of an incident report containing time, location, type, and severity?
- 场景：The system is monitoring a roadway and detects a stalled vehicle, classifying it as an incident. According to the FR, the system should output an incident report. The reviewer needs to identify the obligation that mandates this output.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 / FR-DPA-002 already requires the system to detect and classify incidents and explicitly lists outputs as incident reports with time, location, type, and severity, covering the nominated obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：Upon detection and classification of an incident, the system shall generate an incident report that includes the time, location, type, and severity of the incident.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Maintain long-term archive of processed data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the current specification sufficiently ensure that the long-term archive of processed data is accessible for querying via SQL-based tools, or is an explicit obligation needed to define the query interface?
- 场景：A system must maintain a long-term archive of all processed data and allow users to query that archive using SQL-based tools. The existing requirements include both capabilities but do not specify how the archive becomes queryable via SQL.
- 模型初步去向：covered
- 模型解释：Original FR FR-DSA-003 already requires the system to allow users to query archived data via SQL-based tools, which is equivalent to the draft obligation of providing a SQL-compatible query interface for the long-term archive.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide a SQL-compatible query interface that enables users to access and query the long-term archive of processed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Input data fields → Normalized data stored in central database
- 审查问题：Is the dependency between the input data fields and the normalized data stored in the central database adequately specified, such that the system shall produce normalized data containing the listed input data fields after accepting real-time data inputs?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. These inputs include the input data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility.
- 模型初步去向：retained
- 模型解释：The original FRBLOCK-001 lists the input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) and states that normalized data is stored in a central database, but it does not explicitly specify that the normalized data must incorporate those input data fields. The dependency between the input fields and the normalized stored data is not adequately specified, and no other original FR covers this obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall store normalized data in the central database that incorporates the accepted input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) derived from the real-time data inputs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：30 条提名

### ISOLATED-a64e96c907e8
- 主题：Compute traffic metrics
- 审查问题：Does FRBLOCK-001 require a documented connection between the normalized data stored in the central database and the computation of traffic metrics, or is traffic metric computation out of scope for this FR block?
- 场景：The FR block specifies data collection and ingestion, producing normalized data, but does not mention computing traffic metrics. An isolated element 'Compute traffic metrics' may rely on this data.
- 模型初步去向：unsupported
- 模型解释：The draft obligation introduces a requirement to document the data flow from normalized data to traffic metric computation (or explicitly exclude it) that is not present in any original FR. FRBLOCK-001 does not mention traffic metrics, and FRBLOCK-002 includes traffic metric computation but does not require such documentation. This is a new policy not supported by the source.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：If traffic metrics are within the system scope, the system shall document the data flow from normalized data to traffic metric computation; otherwise, the FR block shall explicitly exclude it.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-aa322bcb7fa9
- 主题：Generate statistical summaries
- 审查问题：Does FRBLOCK-001 imply that the system should generate statistical summaries from the collected and normalized data, or is that a separate downstream function?
- 场景：The FR block addresses data collection and storage but does not include generation of statistical summaries; the isolated element may be a consumer of the stored data.
- 模型初步去向：unsupported
- 模型解释：The original FRs already require statistical summaries/reports (FR-DPA-006, FR-REP-001) but do not require specifying how summaries are derived from normalized data, nor do they require stating that summarization is out of scope. The draft introduces a new documentation/derivation-specification policy unsupported by the checked FRs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：If statistical summaries are required, the system shall specify how they are derived from the normalized data; if not, the FR block should state that summarization is out of scope.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-aca033bbe5bb
- 主题：Perform automated data quality checks
- 审查问题：Does the validation requirement in FR-DCI-002 encompass automated data quality checks as an isolated function, or are automated data quality checks a separate requirement that should be connected to the validation process?
- 场景：The FR block already requires validation against predefined quality rules, but 'Perform automated data quality checks' appears as an isolated element, possibly overlapping or extending that requirement.
- 模型初步去向：retained
- 模型解释：The original FRs include validation against predefined quality rules (FR-DCI-002) and automated data quality checks (FR-DPA-004) as separate requirements, but do not define their scope or relationship. The draft obligation to clarify this relationship is in-scope and not covered by any checked FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：If automated data quality checks extend beyond the predefined validation rules, the system shall define their scope and relationship to FR-DCI-002.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f12d49b4de50
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Does FRBLOCK-001 require that ad-hoc reporting tools have access to the normalized data stored in the central database, or are such tools outside the scope of data collection and ingestion?
- 场景：The FR block focuses on data collection and storage, but the isolated element 'Provide Ad-hoc Reporting Tools' might depend on the stored data.
- 模型初步去向：retained
- 模型解释：The original FRs do not specify a requirement for ad-hoc reporting tools to access the normalized data stored in the central database. FRBLOCK-001 defines the storage of normalized data in a central database, and FRBLOCK-007 requires ad-hoc reporting tools for querying and visualizing data, but no original FR defines the interface or data access method that connects ad-hoc reporting tools to the normalized data. This integration requirement is in-scope and needs to be added.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：If ad-hoc reporting is expected to use the normalized data, the system shall define the interface or data access method; otherwise, the FR block should clarify that reporting is not addressed here.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6a13da768f75
- 主题：Configure new data source types without major software changes
- 审查问题：Although FR-DCI-003 explicitly requires configuration of new data source types, this capability appears isolated. Does FRBLOCK-001 require that this configuration capability be integrated with the data validation and storage processes?
- 场景：The element is supported by the FR text but is isolated in the graph, suggesting potential missing connections to validation and storage workflows.
- 模型初步去向：retained
- 模型解释：The original requirements specify configuration of new data source types, data validation, and normalized storage, but none state that newly configured types must be incorporated into those existing validation and storage processes. This integration is an in-scope business obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall document how newly configured data source types are incorporated into the existing validation and storage pipelines.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2c8d1e438169
- 主题：Compute traffic metrics
- 审查问题：Does the system documentation specify how computed traffic metrics are delivered to downstream consumers or stored?
- 场景：The FR block states that the system computes traffic metrics but does not define any output data flow or consumer, leaving this element isolated.
- 模型初步去向：retained
- 模型解释：No original FR specifies the output data flow or consumer for computed traffic metrics; FRBLOCK-002 only requires computation, and FRBLOCK-004 addresses general data publication but does not require documentation of how computed traffic metrics are delivered or stored. This gap is in scope because computed metrics must be consumed or stored to be useful.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system documentation shall specify the data flow and consumer for computed traffic metrics.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-1f828497c34d
- 主题：Perform automated data quality checks
- 审查问题：Does the system documentation specify how flagged anomalies and inconsistencies are reported or handled?
- 场景：The FR block requires automated data quality checks to flag issues, but no subsequent action or notification is defined, isolating this function.
- 模型初步去向：retained
- 模型解释：The original FRs require automated data quality checks to flag anomalies and inconsistencies, but none specify how flagged issues are handled, reported, or notified. A documentation requirement addressing the handling and notification process is a necessary in-scope supplement.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system documentation shall specify the handling and notification process for flagged data quality issues.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-2c34e50b08b4
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Although FR-DSA-002 specifies dynamic caching for frequently accessed data, this element is reported as isolated in the architecture model. Is there a documented connection between dynamic caching and the archived data or automated purging policies that should be captured to ensure consistency?
- 场景：FRBLOCK-003 contains the dynamic caching requirement, but the current graph model does not show it connected to other elements such as the long-term archive or purging policies.
- 模型初步去向：retained
- 模型解释：The original FRBLOCK-003 contains separate requirements for dynamic caching, archived data, and automated purging, but does not require documenting or coordinating their relationship. The nominated obligation adds an in-scope, business-level requirement to capture that relationship, ensuring performance and storage management are aligned. It is not covered by any original FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall document the relationship between dynamic caching and the archive/purging functions to ensure performance and storage management are coordinated.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-684d54da7081
- 主题：Compute traffic metrics
- 审查问题：Does the system need to compute traffic metrics to support alert generation and API data consumption?
- 场景：FR-DPO-003 requires generating alerts for traffic incidents, which may rely on computed metrics such as speed or flow; FR-DPO-005 provides an API for external applications to consume traffic data in real time, which may require derived metrics.
- 模型初步去向：retained
- 模型解释：The original FRs collectively require computation of traffic metrics (FRBLOCK-002), generation of alerts (FRBLOCK-004), and API data consumption (FRBLOCK-005). However, no single original FR explicitly states that the system shall compute key traffic metrics to enable alert generation and data consumption. The draft obligation is a supported, in-scope business requirement derived from the combination of these original requirements.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should compute key traffic metrics (e.g., average speed, volume, occupancy) to enable meaningful alerts and data consumption.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-68d7b391d6b4
- 主题：Configure new data source types without major software changes
- 审查问题：Is the ability to configure new data source types required to support the export and publication of diverse data?
- 场景：FR-DPO-004 requires exporting data in multiple formats for third-party use, which may necessitate adding new data sources without significant software modifications.
- 模型初步去向：unresolved
- 模型解释：The original FR FRBLOCK-001 already requires configuration of new data source types without major software changes; FRBLOCK-004 requires exporting data in standardized formats. The draft obligation adds only a purpose clause linking these existing requirements, so no new obligation is introduced.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should allow configuration of new data source types without major software changes to support exporting data in standardized formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-89c9910771ae
- 主题：Generate statistical summaries
- 审查问题：Should the system generate statistical summaries as part of the processed data published in standardized formats?
- 场景：FR-DPO-001 states that processed data is published in standardized formats; statistical summaries could be a component of that processed data.
- 模型初步去向：unsupported
- 模型解释：The draft expands beyond the original FRs: FRBLOCK-004 requires publishing processed data but does not specify statistical summaries, and FRBLOCK-002 already requires statistical summaries for traffic patterns only. No original FR requires weather-data summaries or mandates that statistical summaries be included in published outputs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should generate statistical summaries of traffic and weather data for inclusion in published outputs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9c8708bfe5ce
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Does the system need to implement dynamic caching for frequently accessed data to meet real-time feed and API performance requirements?
- 场景：FR-DPO-002 and FR-DPO-005 require real-time data feeds and an API; dynamic caching may be necessary to ensure timely delivery.
- 模型初步去向：covered
- 模型解释：FRBLOCK-003 already states: 'The system shall implement dynamic caching for frequently accessed data to improve performance.' This covers the obligation to implement dynamic caching for frequently accessed data to ensure timely delivery of real-time feeds and API responses.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should implement dynamic caching for frequently accessed data to ensure timely delivery of real-time feeds and API responses.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b62cc7c2f226
- 主题：Perform automated data quality checks
- 审查问题：Should automated data quality checks be performed before publishing processed data in standardized formats?
- 场景：FR-DPO-001 requires publishing processed data; quality checks may be needed to ensure the accuracy and reliability of that data.
- 模型初步去向：retained
- 模型解释：Original FRs include automated data quality checks (FR-DPA-004) and publication in standardized formats (FR-DPO-001), but none specifies that quality checks must be performed before publication. The draft adds this required timing, which is a reasonable in-scope obligation to ensure accuracy of published data and is not covered by existing FRs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should perform automated data quality checks on processed data before publication to ensure accuracy and compliance with standards.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-293ab7d60063
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Is providing ad-hoc reporting tools required to support third-party use of exported data?
- 场景：FR-DPO-004 supports exporting data for third-party use; ad-hoc reporting tools could enhance that use by allowing custom report generation.
- 模型初步去向：unsupported
- 模型解释：The draft obligation introduces a new requirement for the system to provide ad-hoc reporting tools specifically to enable third parties to generate custom reports from exported data. The cited evidence (FRBLOCK-004) only requires exporting data in CSV, JSON, XML, and KML formats for third-party use and does not mention providing reporting tools. Although FRBLOCK-007 includes a generic ad-hoc reporting tools requirement, it is not specific to third-party use or exported data, so it does not cover this obligation. Therefore, the draft is not supported by the original FRs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should provide ad-hoc reporting tools to enable third parties to generate custom reports from exported data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6fb7f6f99cac
- 主题：all users
- 审查问题：Does the FR block need to specify access controls or user roles for data publication and API consumption?
- 场景：FR-DPO-005 provides an API for external applications; without defined user roles, access may be unrestricted, which could be a security or data governance concern.
- 模型初步去向：covered
- 模型解释：FR-SEC-001 already requires secure authentication and authorization for all users, which encompasses access controls and user roles for data publication and API consumption.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should define user roles and access controls for all users accessing published data and APIs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-15cc4318b445
- 主题：Compute traffic metrics
- 审查问题：Should the web-based interface for viewing traffic data also display computed traffic metrics (e.g., congestion levels, average speeds) even though 'Compute traffic metrics' is currently isolated in the system graph?
- 场景：A user viewing traffic data on the web interface may need derived metrics to interpret conditions. The FR block mentions viewing traffic data but does not explicitly state whether computed metrics are included.
- 模型初步去向：retained
- 模型解释：The original FRs require computation of traffic metrics and a web-based interface for viewing traffic data, but no FR explicitly states that computed metrics must be accessible through that interface. This is an in-scope integration gap.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall ensure computed traffic metrics are accessible through the web-based interface for viewing traffic data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-652707b10793
- 主题：Generate statistical summaries
- 审查问题：Should custom dashboards support displaying statistical summaries (e.g., incident counts by time period) given that 'Generate statistical summaries' is isolated?
- 场景：A user creating a custom dashboard for frequent data views may require statistical summaries of traffic or incident data. The FR block allows custom dashboards but does not mention statistical summaries.
- 模型初步去向：retained
- 模型解释：The draft obligation extends the existing custom dashboard capability (FRBLOCK-005) to include generated statistical summaries, which is not covered by any original FR. It is in scope for dashboard functionality and supported by the user scenario.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall allow users to add generated statistical summaries to custom dashboards.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-e0857b0c8d8a
- 主题：Compute traffic metrics
- 审查问题：Is the element 'Compute traffic metrics' intended to be covered by this FR block (e.g., as part of output formats or data processing), or is it handled by another requirement outside FRBLOCK-006?
- 场景：During review, this element was found to be isolated from the FR block, meaning no existing requirement in FRBLOCK-006 references it. The reviewer must determine if this is a gap.
- 模型初步去向：covered
- 模型解释：The element 'Compute traffic metrics' is already stated as an obligation in original FRBLOCK-002 (FR-DPA-001): 'The system shall compute traffic metrics including congestion levels, travel times, queue lengths, and traffic flow patterns.' Therefore it is covered and not a gap.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If confirmed in scope, the system shall compute traffic metrics as part of its data processing capabilities.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9b947e6a5c20
- 主题：Configure new data source types without major software changes
- 审查问题：Should the FR block include a requirement that the system can configure new data source types without major software changes, or is that covered by the existing configure data sources requirement?
- 场景：The element is isolated; the existing FR-SAC-001 only mentions configuring data sources, not the extensibility aspect.
- 模型初步去向：covered
- 模型解释：An original FR already states an equivalent obligation: FRBLOCK-001 includes the requirement 'The system shall allow for the configuration of new data source types without requiring major software changes' (FR-DCI-003), which directly covers the nominated requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If confirmed in scope, the system shall support adding new data source types through configuration without major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-cbad83f27a15
- 主题：Generate statistical summaries
- 审查问题：Does the FR block need to address generation of statistical summaries (e.g., as an output format or algorithm), or is this functionality outside the scope of system administration and configuration?
- 场景：This element is isolated; it may relate to output formats configured by administrators but is not explicitly mentioned.
- 模型初步去向：covered
- 模型解释：An original FR already states an equivalent obligation: FRBLOCK-002 includes the requirement 'The system shall generate statistical summaries of daily, weekly, and monthly traffic patterns.' This covers generation of statistical summaries; the draft obligation does not add a new obligation beyond what is already present.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If in scope, the system shall generate statistical summaries as part of its configurable output formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8646d08e9682
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：Is dynamic caching for frequently accessed data a configuration requirement that should be included in this FR block, or is it a non-functional requirement handled elsewhere?
- 场景：The element is isolated; FRBLOCK-006 focuses on administration, not performance, but caching may need admin configuration.
- 模型初步去向：unsupported
- 模型解释：The draft obligation requires administrators to configure dynamic caching, but no original FR specifies administrative configuration of caching. FRBLOCK-003 requires dynamic caching implementation, not admin configuration, and FRBLOCK-006 lists administration items without caching.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If in scope, the system shall allow administrators to configure dynamic caching for frequently accessed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-cd3fa01b0729
- 主题：Perform automated data quality checks
- 审查问题：Should automated data quality checks be part of the administrative functions described in this FR block, or are they addressed by separate requirements?
- 场景：This element is isolated; data quality checks are not mentioned in FRBLOCK-006.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-001 already requires the system to validate incoming data against predefined quality rules and reject invalid or malformed data, and FRBLOCK-002 requires automated data quality checks to flag anomalies and inconsistencies. These cover the nominated obligation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If in scope, the system shall perform automated data quality checks on configured data sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-319ad96264cf
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Should the FR block include a requirement for providing ad-hoc reporting tools, or is that beyond the scope of system administration and configuration?
- 场景：Ad-hoc reporting tools are not mentioned in FRBLOCK-006; this element is isolated.
- 模型初步去向：covered
- 模型解释：The obligation is already covered by original FRBLOCK-007, which states: 'The system shall provide ad-hoc reporting tools for querying and visualizing data.'
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If in scope, the system shall provide ad-hoc reporting tools as part of its configurable output options.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b531e3a0c975
- 主题：all users
- 审查问题：The element 'all users' is isolated. Should the role-based access control requirement explicitly include 'all users' as a role, or is it covered by the example roles field operator, analyst, admin?
- 场景：FR-SAC-003 lists specific roles but not 'all users'; this isolation may indicate a missing role definition.
- 模型初步去向：unsupported
- 模型解释：The original FR requires role-based access control for different user types, citing examples (field operator, analyst, admin), but it does not define 'all users' as a role. No original FR supports adding 'all users' as a defined role in the RBAC configuration; the phrase 'all users' appears only in the context of authentication and authorization scope, not as a role. Therefore the draft obligation is an unsupported policy.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall include 'all users' as a defined role in the role-based access control configuration.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ee3611451f72
- 主题：Compute traffic metrics
- 审查问题：Does FR-REP-001 require a documented connection to 'Compute traffic metrics' to clarify how traffic volume values are derived for pre-defined reports?
- 场景：A reviewer needs to verify whether the reporting function depends on a separate traffic metrics computation component, which is currently graph-isolated and not referenced by FRBLOCK-007.
- 模型初步去向：unsupported
- 模型解释：The draft obligation is not supported by the original FRs. FR-REP-001 only requires generating pre-defined reports and does not specify how traffic volume values are derived or require a documented connection to a 'Compute traffic metrics' component. FR-DPA-001 may compute traffic metrics, but there is no original requirement linking it to FR-REP-001 or requiring FR-REP-001 to reference the component.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic metrics needed for traffic volume reports, or FR-REP-001 shall explicitly reference the component that performs this computation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9a4e8857357a
- 主题：Generate statistical summaries
- 审查问题：Does FR-REP-003 require a documented connection to 'Generate statistical summaries' to clarify whether ad-hoc reporting includes statistical aggregation beyond basic querying and visualization?
- 场景：Ad-hoc reporting tools are specified for querying and visualizing data, but statistical summaries are a separate isolated element that may be expected by users.
- 模型初步去向：unsupported
- 模型解释：The checked original FRs contain FR-REP-003, which specifies ad-hoc reporting tools for querying and visualizing data only. No original FR requires statistical summary generation within ad-hoc reporting or an explicit exclusion of statistical summarization. The draft introduces an unsupported either-or policy not grounded in the supplied requirements.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall provide statistical summary generation within ad-hoc reporting tools, or explicitly exclude statistical summarization from FR-REP-003.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-6905a39f98e2
- 主题：Configure new data source types without major software changes
- 审查问题：Does FR-REP-003 require a documented connection to 'Configure new data source types without major software changes' to enable ad-hoc reporting on new data sources?
- 场景：Ad-hoc reporting tools may need to access various data sources; the isolated configurability element could be necessary to avoid major software changes when adding sources.
- 模型初步去向：unsupported
- 模型解释：The original FR-REP-003 only requires providing ad-hoc reporting tools for querying and visualizing data; it does not mention configuration of new data source types, major software changes, or limitations to predefined data sources. The draft therefore introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow configuration of new data source types for ad-hoc reporting without major software changes, or explicitly state that ad-hoc reporting is limited to predefined data sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0e9bc1e8495e
- 主题：Perform automated data quality checks
- 审查问题：Does FR-REP-001 or FR-REP-003 require a documented connection to 'Perform automated data quality checks' to ensure report accuracy?
- 场景：Reports on traffic volume and incident frequency rely on underlying data quality; the isolated data quality check element may be relevant to prevent inaccurate reports.
- 模型初步去向：retained
- 模型解释：The original FRs do not require a documented connection between report generation and automated data quality checks. FRBLOCK-007 specifies pre-defined and ad-hoc reporting but does not mention data quality, while FRBLOCK-002 includes automated data quality checks but does not link them to report data. This is an in-scope reporting accuracy obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks on data used for pre-defined and ad-hoc reports, or reference an existing data quality component.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-098f391f7eb5
- 主题：Compute traffic metrics
- 审查问题：Should 'Compute traffic metrics' have a documented connection to the TLS 1.2+ encryption constraint in FR-SEC-002, or is its isolation acceptable?
- 场景：The element 'Compute traffic metrics' is currently graph-isolated. It may involve processing or transmitting network data, but the FR block does not explicitly link it to encryption requirements.
- 模型初步去向：covered
- 模型解释：FR-SEC-002 already requires all data transmissions to be encrypted using TLS 1.2 or higher, which includes any transmissions related to computing traffic metrics. The draft obligation is a subset of the existing requirement.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall encrypt all data transmissions related to computing traffic metrics using TLS 1.2 or higher.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-9f59340cfd2a
- 主题：Perform automated data quality checks
- 审查问题：Should 'Perform automated data quality checks' be connected to the audit logging requirement in FR-SEC-004, or is its isolation acceptable?
- 场景：The element 'Perform automated data quality checks' is graph-isolated. Data quality check executions are system events that may need to be captured for compliance.
- 模型初步去向：covered
- 模型解释：FR-SEC-004 in FRBLOCK-008 already requires audit logging of all system events. Automated data quality check activities are system events, so the draft obligation is already covered by the original requirement.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall log automated data quality check activities as system events.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：15 条提名

### OPERATION-75492aa33387
- 主题：Normalized data stored in central database
- 审查问题：Should FRBLOCK-001 include a specific operation to retrieve or query the normalized data stored in the central database, given that the output is stored but no read operation is specified?
- 场景：Downstream consumers or other system components may need to access the normalized data, but the FR block only describes storage, not retrieval.
- 模型初步去向：unsupported
- 模型解释：The draft obligation introduces a retrieval mechanism for normalized data from the central database for downstream processing. The only supporting source, FRBLOCK-001, states that normalized data is stored in a central database but does not mention retrieval, querying, or downstream processing. No original FR provides an equivalent or broader requirement. Therefore the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall provide a mechanism to retrieve normalized data from the central database for downstream processing.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b56de95a86b8
- 主题：Incident reports
- 审查问题：Should the system provide an operation for authorized users to retrieve incident reports?
- 场景：The FR block specifies that incident reports are produced with time, location, type, and severity, but does not mention any operation to access them.
- 模型初步去向：retained
- 模型解释：The original FRs specify that incident reports are produced as outputs but do not define any operation for authorized users to retrieve them. This is a necessary in-scope capability to make the produced reports accessible.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation for authorized users to retrieve incident reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-132dfb9a7aa5
- 主题：Allow users to query archived data via SQL-based tools
- 审查问题：FR-DSA-003 specifies that users can query archived data via SQL-based tools, which implies a read operation. Is there any additional operation on archived data (e.g., update, delete) that the business workflow requires, or is query-only sufficient?
- 场景：The documented workflow in FRBLOCK-003 provides read access to archived data. Reviewing whether other operations are needed ensures the requirement is not under-specified.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-003 already states that users can query archived data via SQL-based tools, which is read-only access. No additional operations are specified, so the draft obligation is equivalent.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide read-only access to archived data via SQL-based tools, unless additional operations are explicitly required by business rules.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d358a34c43d7
- 主题：Publish processed data in standardized formats
- 审查问题：Should the system support scheduled publication of processed data in addition to on-demand publication?
- 场景：FR-DPO-001 requires publishing processed data in standardized formats, but does not specify whether publication can be scheduled (e.g., periodic reports).
- 模型初步去向：covered
- 模型解释：An original FR already states an equivalent obligation: FRBLOCK-007 requires scheduled automatic report generation and email delivery (FR-REP-002) and on-demand reporting (FR-REP-003), which together with FRBLOCK-004's standardized publication covers scheduled publication of processed data in standardized formats.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should allow scheduled publication of processed data in standardized formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2eb987670a70
- 主题：Generate alerts
- 审查问题：Should users be able to subscribe to specific alert types (traffic incidents, severe weather, asset failures)?
- 场景：FR-DPO-003 generates alerts for multiple categories; subscription management would allow users to receive only relevant alerts.
- 模型初步去向：unsupported
- 模型解释：The checked original FRs only require generating alerts for traffic incidents, severe weather events, and asset failures (FRBLOCK-004). None of the original FRs mention subscription management or user-selectable alert types. The draft obligation introduces a new requirement without source support.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should support subscription management for alert types.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-10dce4e98af3
- 主题：Support data export formats
- 审查问题：Should the system allow users to select which data fields to include when exporting?
- 场景：FR-DPO-004 supports exporting data in multiple formats, but field selection would enable users to customize exports for their needs.
- 模型初步去向：retained
- 模型解释：The original FRs specify export formats (CSV, JSON, XML, KML) but do not include a requirement for users to select which data fields to include. Field selection is an in-scope enhancement to the data export functionality and is not covered by any original FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system should enable field selection for data exports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fbce9be4ba4f
- 主题：Data filtering and search
- 审查问题：When users apply filters or search criteria, should the map displays automatically update to show only matching traffic, incident, and road closure icons?
- 场景：A user filters data by location and expects the map to immediately reflect the filtered icons without manually refreshing or re-plotting.
- 模型初步去向：retained
- 模型解释：The original FR BLOCK-005 provides filter and search functionality, but it does not explicitly require the map display to automatically update to show only matching traffic, incident, and road closure icons. This obligation is a specific presentation behavior within scope and not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall update map displays in response to applied filter and search criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2b628bcf017a
- 主题：Custom dashboards
- 审查问题：Does the operation to create a custom dashboard include persisting the dashboard configuration and retrieving it in later sessions?
- 场景：A user creates a custom dashboard for frequent data views and expects it to be available the next time they log in. If persistence is not provided, users would need to recreate dashboards each session.
- 模型初步去向：retained
- 模型解释：The original FR (FRBLOCK-005) only states that users can create custom dashboards for frequent data views; it does not explicitly require persisting the dashboard configuration or retrieving it in later sessions. No other original FR covers this obligation. The expectation that a user-created dashboard remains available across sessions is a natural business requirement implied by the phrase 'for frequent data views' and is supported by the nomination scenario.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall persist user-created custom dashboards and allow retrieval for subsequent sessions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-39fd617ec54f
- 主题：Configure Data Sources, Algorithms, and Output Formats
- 审查问题：Does the configuration operation need to specify whether changes require validation, approval, or are applied immediately?
- 场景：The FR states administrators can configure, but does not detail the workflow of the configuration operation.
- 模型初步去向：unsupported
- 模型解释：The draft adds a validation-and-approval workflow for configuration changes, but the cited FR only states that administrators can configure data sources, algorithms, and output formats. No original FR specifies that changes must be validated or approved before being applied.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall apply configuration changes only after validation and approval by an authorized administrator.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-08edb476b138
- 主题：Log Administrative Actions and Errors
- 审查问题：Should the logging operation capture specific attributes such as actor identity, timestamp, action type, and error details?
- 场景：The FR requires logging but does not specify the content of the log entries.
- 模型初步去向：retained
- 模型解释：The original FR (FRBLOCK-006) requires logging all administrative actions and errors for audit and troubleshooting but does not specify the content of log entries. The draft obligation adds necessary audit log attributes (actor identity, timestamp, action/error details), which is a supported, in-scope elaboration not covered by the checked original FRs.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall log each administrative action and error with at least actor identity, timestamp, and action/error details.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6dd09caf4b86
- 主题：Role-Based Access Control
- 审查问题：Is the enforcement of role-based access control required to be performed at every access attempt, including read and write operations?
- 场景：The FR mentions RBAC but does not specify the granularity of enforcement.
- 模型初步去向：retained
- 模型解释：FRBLOCK-006 requires the system to support role-based access control for different user types but does not specify enforcement granularity. The draft obligation clarifies that RBAC must be applied consistently to all access attempts, which is an in-scope elaboration of the existing RBAC support requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall enforce role-based access control on every data access and administrative operation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a7cc2d67a656
- 主题：Backup and Restore Capabilities
- 审查问题：Do the backup and restore operations need to support scheduled backups, manual triggers, and point-in-time recovery?
- 场景：The FR provides backup and restore capabilities but does not define operational parameters.
- 模型初步去向：unsupported
- 模型解释：The draft introduces specific requirements for scheduled backups, manual triggers, and point-in-time recovery that are not supported by the cited FR, which only requires generic backup and restore capabilities for the database and configuration settings. No source in the checked original FRs specifies these operational parameters.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall support scheduled and manual backup operations with restore to any point within the retention period.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-143bf1ad8ab7
- 主题：Schedule Automatic Report Generation and Email Delivery
- 审查问题：Does FR-REP-002 require an operation to modify or cancel a scheduled automatic report?
- 场景：The requirement allows scheduling and email delivery, but does not mention whether users can manage existing schedules (e.g., edit frequency, recipients, or cancel).
- 模型初步去向：unsupported
- 模型解释：FR-REP-002 only states that users can schedule automatic report generation and email delivery. It does not mention modifying or canceling existing scheduled reports. The draft adds new management operations that are not supported by the original requirement.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow users to modify and cancel scheduled automatic report generation jobs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3d53f6da17fe
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Does FR-REP-003 require an operation to save ad-hoc report definitions for reuse?
- 场景：Ad-hoc reporting tools are provided, but it is unclear whether users can persist queries or visualizations beyond a single session.
- 模型初步去向：unsupported
- 模型解释：The original FR (FRBLOCK-007) only requires providing ad-hoc reporting tools for querying and visualizing data. It does not mention saving report definitions, queries, or visualizations for later reuse, and no other original FR covers this obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow users to save ad-hoc report queries and visualizations for later reuse.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-27233d2f8d29
- 主题：Audit logging of user activities and system events
- 审查问题：Should the system provide a specific operation to retrieve (read) audit log entries for review?
- 场景：The FR mandates audit logging but does not specify how logs are accessed. Review whether a read operation on audit logs is required for compliance and operational use.
- 模型初步去向：retained
- 模型解释：The original FR FRBLOCK-008 requires audit logging of user activities and system events, but no checked original FR specifies how logs are accessed. Providing a retrieval/view operation is a necessary in-scope capability to support audit review and compliance.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation to retrieve and view audit log entries.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall ensure that historical data ingested in batch is made available and suitable for training the machine learning models used for predictive analysis of traffic trends and incident likelihood.

2. [model_preliminarily_retained] The system shall validate each of the listed input data fields—GPS data, speed, location, road condition reports, temperature, precipitation, and visibility—against applicable predefined quality rules and reject any incoming record where one or more of these fields is invalid or malformed.

3. [model_preliminarily_retained] The system shall process historical data ingested via batch for archive backfill and make it available for publishing in standardized formats (SAE J2354, TMDD).

4. [model_preliminarily_retained] The system shall deliver the scheduled report email to the designated recipients when automatic report generation and email delivery is scheduled.

5. [model_preliminarily_retained] The system shall store normalized data in the central database that contains the accepted real-time input data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility.

6. [model_preliminarily_retained] The system shall define the scope and relationship between automated data quality checks and the validation process specified in FR-DCI-002, including any checks that extend beyond predefined validation rules.

7. [model_preliminarily_retained] The system shall provide ad-hoc reporting tools with access to the normalized data stored in the central database through a defined data access method or interface.

8. [model_preliminarily_retained] The system shall ensure that newly configured data source types are processed by the existing data validation and storage pipelines.

9. [model_preliminarily_retained] The system documentation shall specify the data flow and consumer(s) for computed traffic metrics, including whether they are delivered to downstream consumers or stored, and the delivery mechanism or storage location.

10. [model_preliminarily_retained] The system documentation shall specify the handling and notification process for flagged data quality issues.

11. [model_preliminarily_retained] The system shall provide an operation for authorized users to retrieve incident reports.

12. [model_preliminarily_retained] The system shall document the relationship between dynamic caching for frequently accessed data and the archive/purging functions to ensure coordinated performance and storage management.

13. [model_preliminarily_retained] The system shall compute traffic metrics (e.g., average speed, volume, occupancy) to support alert generation and API data consumption.

14. [model_preliminarily_retained] The system shall perform automated data quality checks on processed data before publishing it in standardized formats.

15. [model_preliminarily_retained] The system shall enable users to select which data fields to include when exporting data in the supported formats.

16. [model_preliminarily_retained] The system shall ensure computed traffic metrics are accessible through the web-based interface for viewing traffic data.

17. [model_preliminarily_retained] The system shall allow users to add generated statistical summaries to custom dashboards.

18. [model_preliminarily_retained] The system shall automatically update map displays to show only traffic, incident, and road closure icons that match user-applied filters or search criteria.

19. [model_preliminarily_retained] The system shall persist user-created custom dashboards and allow retrieval for subsequent sessions.

20. [model_preliminarily_retained] The system shall ensure that logs of administrative actions and errors include at least actor identity, timestamp, and action/error details.

21. [model_preliminarily_retained] The system shall enforce role-based access control for every data access attempt (including read and write operations) and for all administrative operations, ensuring users can perform only actions permitted by their assigned role.

22. [model_preliminarily_retained] The system shall perform automated data quality checks on data used for pre-defined and ad-hoc reports, or reference an existing data quality component, to ensure report accuracy.

23. [model_preliminarily_retained] The system shall allow authorized users to retrieve and view audit log entries.
