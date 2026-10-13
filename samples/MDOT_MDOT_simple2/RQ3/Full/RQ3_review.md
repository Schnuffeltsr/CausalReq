# RQ3 审查材料：MDOT_MDOT_simple2 / Full

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
- 主题：Use Oracle 10G for archiving → Allow users to query archived data via SQL-based tools
- 审查问题：Does the requirement block FRBLOCK-003 clearly obligate the system to allow users to query archived data via SQL-based tools given that the archive is maintained using Oracle 10G, or is an explicit obligation to provide SQL-based query access to the archived data missing?
- 场景：In FRBLOCK-003, the requirements include the statements: "using Oracle 10G" and "maintain a long-term archive of all processed data" and "allow users to query archived data via SQL-based tools". The dependency analysis shows that the ability to query archived data depends on the existence of the archive maintained using Oracle 10G. Review whether the obligation to provide SQL-based query access to the archived data is explicitly stated or only implicitly assumed.
- 模型初步去向：covered
- 模型解释：FRBLOCK-003 explicitly states: 'The system shall allow users to query archived data via SQL-based tools.' This is equivalent to the draft obligation. The additional context about Oracle 10G maintenance does not create a new unsupported obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall allow users to query archived data via SQL-based tools, where the archived data is the long-term archive of processed data maintained using Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Support batch ingestion of historical data → Support machine learning models
- 审查问题：Should the system include an explicit requirement to ensure that batch-ingested historical data is made available to the machine learning model training process, given the documented dependency?
- 场景：A traffic management system is required to support batch ingestion of historical data for backfilling archives and training models, and also to support machine learning models for predictive analysis of traffic trends and incident likelihood. If the batch ingestion process does not provide the historical data to the training pipeline, the machine learning models may not be trained on the required historical data.
- 模型初步去向：retained
- 模型解释：The original FRs require batch ingestion of historical data for training models and support machine learning models for predictive analysis, but they do not explicitly state that the batch-ingested historical data must be made available and accessible to the machine learning model training process. This is a necessary in-scope obligation derived from the documented dependency.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall ensure that the batch-ingested historical data is available and accessible to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Accept real-time data inputs from external sources → Normalized data stored in central database
- 审查问题：Is there a business obligation that the system shall normalize and store the accepted real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems into the central database?
- 场景：A requirements reviewer is validating the functional decomposition for the data input function. The source requirement states: "The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems." The target requirement states: "Normalized data stored in a central database." The reviewer needs to determine whether the dependency between these two statements is explicitly captured as a business obligation.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-001 already specifies 'Normalized data stored in a central database' as the output of the function that accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, which is equivalent to the nominated obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall normalize and store all accepted real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports
- 审查问题：Does the system need to generate the pre-defined reports on traffic volume, incident frequency, and road condition trends whenever a user schedules automatic report generation and email delivery?
- 场景：A user schedules automatic report generation and email delivery. As a result of that scheduled action, the system should generate the pre-defined reports on traffic volume, incident frequency, and road condition trends.
- 模型初步去向：retained
- 模型解释：The original FRs (FRBLOCK-007) specify generating pre-defined reports and scheduling automatic report generation and email delivery as separate capabilities, but no original FR states that scheduling the automatic report generation triggers generation of the predefined reports. The dependency evidence supports an inferred TRIGGERS relationship, making this a retained business obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：When a user schedules automatic report generation and email delivery, the system shall generate the pre-defined reports on traffic volume, incident frequency, and road condition trends.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Automated data purging policies → Support automated data purging policies
- 审查问题：Given the dependency from 'automated data purging policies' to 'support automated data purging policies', does the target requirement adequately specify the obligation to support the defined policies?
- 场景：A requirements reviewer checks whether the target requirement 'support automated data purging policies' is necessary and correctly derived from the source requirement 'automated data purging policies'.
- 模型初步去向：covered
- 模型解释：Original requirement FRBLOCK-003 already states 'The system shall support automated data purging policies to manage storage limits,' which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall support automated data purging policies when such policies are defined and active.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Use Oracle 10G for archiving → Publish processed data in standardized formats
- 审查问题：Does the documented dependency from 'Use Oracle 10G for archiving' to 'Publish processed data in standardized formats' warrant an explicit obligation that processed data to be published is sourced from the Oracle 10G long-term archive?
- 场景：The FR block states the system shall 'maintain a long-term archive of all processed data' using Oracle 10G (source) and shall 'publish processed data in standardized formats' (target). The dependency reasoning indicates that publishing requires processed data to be available, and the archive is the designated long-term store.
- 模型初步去向：unsupported
- 模型解释：The original FRs require archiving processed data using Oracle 10G and publishing processed data in standardized formats, but no original FR or dependency evidence establishes that published data must be sourced from the long-term archive. The dependency relation indicates availability, not a sourcing constraint; therefore the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats from the long-term archive maintained using Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Input data fields → Validate incoming data and reject invalid data
- 审查问题：Does the validation requirement (FR-DCI-002) specify predefined quality rules for each of the input data fields listed in FR-DCI-001, including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems (FR-DCI-001). The incoming data includes GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. FR-DCI-002 requires validation of incoming data against predefined quality rules and rejection of invalid or malformed data. The source active meaning is that these listed data fields are present and accepted; the target active meaning is that validation is active.
- 模型初步去向：covered
- 模型解释：The original FR-DCI-002 already requires validation of incoming data against predefined quality rules and rejection of invalid or malformed data, which applies to all accepted real-time data inputs including the fields listed in FR-DCI-001. The draft only makes the field enumeration explicit without adding a new obligation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall validate each accepted real-time data input field (GPS data, speed, location, road condition reports, temperature, precipitation, and visibility) against predefined quality rules and reject any record where a field is invalid or malformed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Support batch ingestion of historical data → Publish processed data in standardized formats
- 审查问题：Is there a requirement that explicitly connects the source FR 'The system shall support batch ingestion of historical data for backfilling archives and training models' to the target FR 'publish processed data in standardized formats', ensuring that historical data ingested in batch is both archived and subsequently published in those standardized formats?
- 场景：A requirements analyst is reviewing whether the dependency from 'Support batch ingestion of historical data' to 'Publish processed data in standardized formats' is adequately covered by an operational obligation. The evidence chain shows that batch ingestion enables 'Maintain long-term archive of processed data' (source quote: 'The system shall support batch ingestion of historical data for backfilling archives and training models'), and the publication function depends on that archive (target quote: 'publish processed data in standardized formats'). However, no direct requirement has been identified that guarantees the backfilled archive data is actually made available in the standardized output formats. The analyst needs to decide whether to add a new obligation.
- 模型初步去向：retained
- 模型解释：The original FRs separately require batch ingestion for backfilling archives, long-term archiving of processed data, and publication in standardized formats, but no FR explicitly connects batch-ingested historical data to subsequent publication. The dependency evidence from REL-06 and REL-08 supports this additional obligation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall ensure that processed data originating from batch ingestion of historical data is stored in the long-term archive and is then made available for publication in the standardized formats (e.g., SAE J2354, TMDD).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Input data fields → Accept real-time data inputs from external sources
- 审查问题：Is it required that the system accept the input data fields 'GPS data, speed, location, road condition reports, temperature, precipitation, visibility' as part of accepting real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems?
- 场景：A requirements reviewer is verifying whether the obligation to accept real-time data inputs from external sources includes the specific input data fields listed in the FR.
- 模型初步去向：covered
- 模型解释：FR-DCI-001 in the original FR explicitly requires accepting real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, and it lists the exact input data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The draft obligation is equivalent to the original FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, including the input data fields: GPS data, speed, location, road condition reports, temperature, precipitation, and visibility.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Support batch ingestion of historical data → Maintain long-term archive of processed data
- 审查问题：Does the support for batch ingestion of historical data, as specified in the functional requirement ('The system shall support batch ingestion of historical data for backfilling archives and training models'), sufficiently ensure that the long-term archive of processed data is actively maintained?
- 场景：An operator initiates a batch ingestion of historical data for the purpose of backfilling the archive. The system must process the batch and update the long-term archive with the ingested data, ensuring the archive remains current.
- 模型初步去向：covered
- 模型解释：Original FR-DSA-001 (FRBLOCK-003) states: 'The system shall maintain a long-term archive of all processed data using Oracle 10G.' This obligation already covers storing processed data from batch ingestion into the long-term archive and maintaining the archive's completeness. The draft obligation is a specific instance of this existing requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall, upon completing batch ingestion of historical data, store the processed data into the long-term archive, thereby maintaining the archive's completeness and continuity.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Use Oracle 10G for archiving → Maintain long-term archive of processed data
- 审查问题：Does the requirement that the system 'maintain a long-term archive of all processed data' adequately handle scenarios where 'using Oracle 10G' for archiving is no longer feasible (e.g., unsupported, unavailable), given that the target depends on this source?
- 场景：The requirement states the system shall maintain the archive 'using Oracle 10G'. If Oracle 10G becomes unavailable or cannot be used for archiving, the dependency implies the long-term archive maintenance could be compromised unless the requirement provides alternative measures.
- 模型初步去向：retained
- 模型解释：The original requirement FRBLOCK-003 states that the system shall maintain the long-term archive using Oracle 10G, but it does not specify that archival operations must continue if Oracle 10G becomes unavailable or unsupported. No other original FR covers this continuity obligation. The draft obligation is a necessary supplement to ensure the archive is not solely dependent on a specific technology.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall maintain the long-term archive of all processed data without being solely dependent on Oracle 10G, ensuring continuity of archival operations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Configure Data Sources, Algorithms, and Output Formats → Log Administrative Actions and Errors
- 审查问题：Does the requirement to allow administrators to configure data sources, algorithms, and output formats adequately trigger the logging of all administrative actions, including those configuration changes, as required by the logging of all administrative actions and errors?
- 场景：An administrator uses the system to configure a new data source, modify an algorithm, or change an output format, and the system must ensure this administrative action is logged.
- 模型初步去向：covered
- 模型解释：The original FRs already require logging of all administrative actions and errors (FRBLOCK-006) and audit logging of all user activities and system events (FRBLOCK-008). Therefore, logging configuration changes by administrators is an equivalent obligation already captured.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall log every administrative action involving the configuration of data sources, algorithms, and output formats as an administrative action, in accordance with the requirement to log all administrative actions and errors.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Accept real-time data inputs from external sources → Validate incoming data and reject invalid data
- 审查问题：Is the dependency between FR-DCI-001 (Accept real-time data inputs from external sources) and FR-DCI-002 (Validate incoming data and reject invalid data) adequately specified such that every accepted real-time data input is subject to validation and rejection if invalid or malformed?
- 场景：The system continuously receives real-time data from probe vehicles, traffic sensors, weather stations, and traveler information systems. FR-DCI-001 requires acceptance of these inputs. FR-DCI-002 requires validation against predefined quality rules and rejection of invalid or malformed data. The review must determine whether the validation obligation covers all accepted external input types and whether rejection is explicitly required without additional assumptions.
- 模型初步去向：covered
- 模型解释：FR-DCI-002 in FRBLOCK-001 already requires the system to validate incoming data against predefined quality rules and reject invalid or malformed data. Since FR-DCI-001 defines incoming data to include real-time inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, the obligation that every such input is validated and rejected if invalid is already covered by the original FR.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall validate every real-time data input accepted from probe vehicles, traffic sensors, weather stations, and traveler information systems against predefined quality rules, and shall reject any input that is invalid or malformed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Schedule Automatic Report Generation and Email Delivery → Email Delivery
- 审查问题：Does the system guarantee that when users schedule automatic report generation and email delivery (as stated in FRBLOCK-007), the scheduled report email is actually delivered to the designated recipients?
- 场景：A user schedules automatic report generation and email delivery according to FRBLOCK-007: 'The system shall allow users to schedule automatic report generation and email delivery.' The schedule triggers, and the system must deliver the email to recipients.
- 模型初步去向：retained
- 模型解释：FRBLOCK-007 only requires the system to allow users to schedule automatic report generation and email delivery; it does not state that the scheduled report email is actually delivered to designated recipients. The draft obligation adds an in-scope business requirement ensuring delivery upon schedule trigger, which is not covered by the original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：When automatic report generation and email delivery is scheduled, the system shall deliver the report email to the designated recipients.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：High-volume data display → De-cluttering features
- 审查问题：Is there an explicit requirement that high-volume data display triggers de-cluttering features?
- 场景：A requirements review is conducted to confirm that the system's behavior during 'high-volume data display' activates 'de-cluttering features' as referenced in FR-UIP-003.
- 模型初步去向：covered
- 模型解释：FRBLOCK-005 already states an equivalent obligation: 'The system shall support de-cluttering features to reduce visual complexity during high-volume data display.'
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall activate de-cluttering features when high-volume data display occurs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Maintain long-term archive of processed data → Publish processed data in standardized formats
- 审查问题：Given the requirement to "maintain a long-term archive of all processed data" and the requirement to "publish processed data in standardized formats", does the system need to ensure that the published data is obtained from the long-term archive, rather than from some other transient source?
- 场景：A stakeholder is reviewing the dependency between the obligations. The source requirement states the system must "maintain a long-term archive of all processed data", and the target requirement states the system must "publish processed data in standardized formats". The reviewer must confirm that the publication process relies on the long-term archive as the data source, ensuring that published data is retrieved from the archive.
- 模型初步去向：unsupported
- 模型解释：The original FRs include a requirement to maintain a long-term archive of processed data (FRBLOCK-003) and a separate requirement to publish processed data in standardized formats (FRBLOCK-004). None of the original FRs specifies that the published data must be retrieved from the long-term archive. The dependency relation only indicates that publication requires processed data to be available; it does not establish the archive as the mandatory source. Therefore the draft obligation adds an unsupported policy.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats by retrieving the relevant processed data from the long-term archive of all processed data that the system maintains.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the system's support for batch ingestion of historical data (FRBLOCK-001: 'The system shall support batch ingestion of historical data for backfilling archives and training models.') explicitly require that the resulting archived data be accessible for querying via SQL-based tools (FRBLOCK-003: 'allow users to query archived data via SQL-based tools')?
- 场景：The system must support batch ingestion of historical data for backfilling archives and training models. The requirements also state the need to maintain a long-term archive of processed data and to allow users to query archived data via SQL-based tools. The source capability (batch ingestion) is intended to populate the archive, which is then queried by users. The dependency between batch ingestion and SQL-based querying of archived data is under review to ensure the intended flow is explicitly captured.
- 模型初步去向：retained
- 模型解释：The original FRs separately require batch ingestion for backfilling archives and SQL-based querying of archived data, but none states the explicit linkage that data ingested via batch must be queryable through SQL. The dependency is directly supported: batch ingestion populates the long-term archive, and the archive is the data source for SQL queries. This obligation clarifies the intended end-to-end flow without introducing new policy.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall ensure that batch ingestion of historical data, performed for backfilling archives, results in archived data that is queryable by users via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Detect and classify incidents → Incident reports
- 审查问题：Does the system's obligation specify that when an incident is detected and classified, an incident report with time, location, type, and severity is generated?
- 场景：The system detects and classifies an incident such as a crash, debris, stalled vehicle, or work zone.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already states that the system shall detect and classify incidents and that the output includes incident reports with time, location, type, and severity, which is equivalent to the draft obligation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：When the system detects and classifies an incident, the system shall generate an incident report with time, location, type, and severity.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Maintain long-term archive of processed data → Allow users to query archived data via SQL-based tools
- 审查问题：If the system is maintaining a long-term archive of processed data, must users always be able to query that archived data via SQL-based tools, or are there additional prerequisites that could prevent querying even when the archive is maintained?
- 场景：A user attempts to query archived data using a SQL-based tool while the system is actively maintaining a long-term archive of processed data.
- 模型初步去向：covered
- 模型解释：FRBLOCK-003 (FR-DSA-003) already explicitly requires the system to allow users to query archived data via SQL-based tools, without prerequisites. The draft obligation re-states this capability conditioned on archive maintenance, which is already inherent in the existing archive and query functionality.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall allow users to query archived data via SQL-based tools whenever the long-term archive of processed data is maintained.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Input data fields → Normalized data stored in central database
- 审查问题：Does the system include an obligation to ensure that when the input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) are present in real-time data, the system accepts those inputs and produces normalized data stored in a central database?
- 场景：A real-time data stream arrives containing GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The system must accept these real-time data inputs and normalize them into the central database.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states the obligation: the system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, with inputs GPS data, speed, location, road condition reports, temperature, precipitation, visibility, and outputs normalized data stored in a central database.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：When the system receives real-time data inputs that include GPS data, speed, location, road condition reports, temperature, precipitation, and visibility, it shall accept those inputs and store normalized data in a central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：19 条提名

### ISOLATED-0e1b0192d0c8
- 主题：Compute traffic metrics
- 审查问题：Does the data collection and ingestion block require computing traffic metrics from the normalized data stored in the central database?
- 场景：Traffic operations need real-time metrics such as average speed and congestion levels derived from ingested probe vehicle and sensor data to support downstream traffic management decisions.
- 模型初步去向：out_of_scope
- 模型解释：The source text assigns computing traffic metrics to the Data Processing and Analysis block (FR-DPA-001), not to Data Collection and Ingestion. The nominated draft obligation places this computation in the data collection and ingestion block, which is outside the scope of that block.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic metrics from normalized data as part of data collection and ingestion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-48cf41c3f600
- 主题：Generate statistical summaries
- 审查问题：Is there a requirement to generate statistical summaries from the collected data within this FR block?
- 场景：Analysts require daily and weekly statistical summaries of traffic and weather data for reporting and model training.
- 模型初步去向：covered
- 模型解释：The obligation to generate statistical summaries from collected data is already stated in original FR blocks: FRBLOCK-002 requires generating statistical summaries of daily, weekly, and monthly traffic patterns, and FRBLOCK-007 requires pre-defined reports on traffic volume, incident frequency, and road condition trends.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall generate statistical summaries from normalized data as part of data collection and ingestion.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b4880b6a372e
- 主题：Perform automated data quality checks
- 审查问题：Does the FR block require automated data quality checks beyond the predefined quality rules validation specified in FR-DCI-002?
- 场景：Data quality team needs automated periodic checks on stored normalized data to detect anomalies not caught at ingestion time.
- 模型初步去向：retained
- 模型解释：The original FRs only require validation against predefined quality rules at ingestion and rejection of invalid data. They do not specify automated data quality checks on stored normalized data beyond ingestion-time validation. The draft introduces an in-scope business obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks on stored normalized data in addition to ingestion-time validation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-5b5c3831d697
- 主题：Perform automated data quality checks
- 审查问题：Does the system need to define an action for the anomalies and inconsistencies flagged by the automated data quality checks, such as generating alerts or logs, and if so, what are the target recipients or destinations?
- 场景：The FR block states that the system will flag anomalies but does not specify what happens after flagging. Without a defined outcome, the quality check function may be incomplete.
- 模型初步去向：unsupported
- 模型解释：The original FR only requires the system to flag anomalies and inconsistencies; it does not specify generating quality alerts or log entries or directing them to recipients. The draft introduces an additional alerting/logging obligation not supported by the source FRs.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall generate quality alerts or log entries for flagged anomalies, directing them to appropriate monitoring interfaces or personnel.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-bf0abba87494
- 主题：Generate statistical summaries
- 审查问题：Does the 'Generate statistical summaries' function require access to historical traffic data, and if so, is that data source documented?
- 场景：Statistical summaries of daily, weekly, and monthly patterns require historical data aggregation. The FR block does not explicitly mention storage or retrieval of historical data.
- 模型初步去向：retained
- 模型解释：The original FR requires generating statistical summaries of daily, weekly, and monthly traffic patterns, which logically requires access to historical traffic data. No checked original FR explicitly provides for such access or documents the data source, so the obligation is a necessary addition.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall have access to a persistent data store containing historical traffic data for the purpose of generating statistical summaries.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0cb7c283f9de
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：The dynamic caching function appears isolated in the graph; does the FR block require a documented connection between dynamic caching and automated data purging to ensure cached data is invalidated when purged?
- 场景：Data is purged from the archive; cached copies of that data may remain, causing stale reads. A documented connection would define cache invalidation behavior.
- 模型初步去向：retained
- 模型解释：The original FRs specify dynamic caching and automated data purging as separate requirements but do not define any connection or invalidation behavior. The draft obligation addresses a necessary consistency requirement between these two in-scope functions.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall invalidate cached data entries when corresponding archived data is purged.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-b552a384e9e8
- 主题：Compute traffic metrics
- 审查问题：Should the system compute traffic metrics as an input to generating traffic incident alerts as required by FR-DPO-003?
- 场景：FR-DPO-003 requires generating alerts for traffic incidents, but does not specify whether traffic metrics (e.g., speed, volume) are computed to detect incidents. Without such metrics, alert generation may not be possible.
- 模型初步去向：retained
- 模型解释：The original FRs include computing traffic metrics (FR-DPA-001), detecting traffic incidents (FR-DPA-002), and generating traffic incident alerts (FR-DPO-003), but no original FR explicitly requires computing traffic metrics as an input to detection and alert generation. The draft obligation is a necessary elaboration to ensure alert generation is supported.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall compute traffic metrics to support the detection and generation of traffic incident alerts.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-da5bb9debf38
- 主题：Generate statistical summaries
- 审查问题：Should the statistical summaries generated by the system be included in the data export formats specified in FR-DPO-004?
- 场景：FR-DPO-004 requires support for exporting data in CSV, JSON, XML, and KML formats, but it does not mention whether statistical summaries are part of the exported data. Third-party users may need statistical summaries.
- 模型初步去向：retained
- 模型解释：The original FRs require generating statistical summaries (FRBLOCK-002) and exporting data in CSV, JSON, XML, and KML formats (FRBLOCK-004), but do not explicitly require exporting the generated statistical summaries in those formats. This obligation fills that gap and is in scope.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall export generated statistical summaries in CSV, JSON, XML, and KML formats for third-party use.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-56687cada6f5
- 主题：Perform automated data quality checks
- 审查问题：Should the system perform automated data quality checks before publishing processed data as specified in FR-DPO-001?
- 场景：FR-DPO-001 requires publishing processed data in standardized formats, but does not address data quality. Publishing data without quality checks could propagate errors to consumers.
- 模型初步去向：retained
- 模型解释：The original FRs include automated data quality checks (FR-DPA-004 in FRBLOCK-002) and publishing processed data in standardized formats (FR-DPO-001/FRBLOCK-004), but none specifies performing the checks prior to publication. Adding this timing constraint is a supported in-scope business obligation to prevent propagating data errors, and it is not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall perform automated data quality checks on processed data prior to publication in standardized formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7b8c6e9fdf70
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Should the system provide ad-hoc reporting tools to enable third-party users to generate custom reports using the data exported according to FR-DPO-004?
- 场景：FR-DPO-004 supports data export in multiple formats, but does not specify any user-facing reporting tools. Third-party users may require ad-hoc reporting capabilities beyond raw data export.
- 模型初步去向：retained
- 模型解释：The original FRs do not include an obligation for third-party users to generate custom reports using exported data. FRBLOCK-004 only specifies exporting data in CSV, JSON, XML, and KML formats for third-party use, and FRBLOCK-007 mentions ad-hoc reporting tools but not for third-party users or using exported data. The draft fills a gap by specifying reporting capabilities for third-party users based on the exported data.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools that allow third-party users to create custom reports using exported data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-17a876312556
- 主题：all users
- 审查问题：Should the data publication, real-time feeds, alerts, and export capabilities be accessible to all users, or only to specific user groups identified in the FR block (e.g., third-party, external applications)?
- 场景：The FR block references 'third-party use' (FR-DPO-004) and 'external applications' (FR-DPO-005), but does not define the scope of 'all users'. This could lead to ambiguity about who can access these capabilities.
- 模型初步去向：retained
- 模型解释：The original FRs reference third-party use and external applications but do not define user roles or access permissions for data publication, real-time feeds, alerts, or export capabilities. The draft obligation clarifies the need to ensure appropriate access for intended users, which is a supported in-scope business obligation not explicitly stated in the checked original FRs.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall define user roles and access permissions for data publication, feeds, alerts, and export capabilities to ensure all intended users have appropriate access.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8c80b876730d
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：The element 'Provide Ad-hoc Reporting Tools' appears isolated in the graph. FR-UIP-004 requires filtering and searching data by location, time, event type, and other relevant criteria. Does that capability imply the need for ad-hoc reporting tools, or are reporting tools out of scope for this block? Please document any explicit or implicit connection, or confirm that the isolation is intentional and no gap exists.
- 场景：A reviewer sees that FR-UIP-004 provides data filtering and search, which often precedes report generation, but no connection to 'Provide Ad-hoc Reporting Tools' is documented. The question seeks to determine whether a link should be created or whether the isolated element remains out of scope.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 explicitly requires ad-hoc reporting tools for querying and visualizing data, which is equivalent to the isolated element 'Provide Ad-hoc Reporting Tools'. The filtering and search capability in FR-UIP-004 does not independently imply ad-hoc reporting, but the original FR set already contains the obligation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system should provide ad-hoc reporting tools only if the filtering and search capability is intended to support user-defined report generation; otherwise, ad-hoc reporting is out of scope.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-66e6676c4a7a
- 主题：all users
- 审查问题：The element 'all users' is isolated in the graph. FR-UIP-005 requires multi-language UI options to accommodate diverse user groups. Does this FR imply support for all users, or is 'all users' a broader concept that should be linked to this requirement? Please document the intended relationship or confirm that isolation is acceptable.
- 场景：The graph shows 'all users' as isolated, while FR-UIP-005 mentions diverse user groups. The reviewer wants to clarify whether the multi-language option is meant for all users or only specific groups, and whether a documented relationship is needed to avoid ambiguity.
- 模型初步去向：unsupported
- 模型解释：The draft obligation asserts that multi-language UI support must apply to all user groups and that the system must not inadvertently exclude any user group. The original FR (FRBLOCK-005) only requires support to accommodate diverse user groups; it does not state universal applicability or a non-exclusion guarantee. This introduces an unsupported policy beyond the original requirement.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The multi-language UI support should apply to all user groups unless a specific subset is defined; the system should not inadvertently exclude any user group.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4ae8b88ad69f
- 主题：Configure new data source types without major software changes
- 审查问题：Does FR-SAC-001 imply that administrators can add entirely new data source types (e.g., new protocols or file formats) without requiring major software changes, or is configuration limited to selecting among existing data source types?
- 场景：A new data source type is introduced after deployment; the administrator needs to integrate it without a software release.
- 模型初步去向：covered
- 模型解释：The original FR block FRBLOCK-001 contains FR-DCI-003, which states: 'The system shall allow for the configuration of new data source types without requiring major software changes.' This is equivalent to the draft obligation, so the obligation is already covered.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall allow administrators to add and configure new data source types without requiring major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-c951653cb78a
- 主题：all users
- 审查问题：Does the role-based access control requirement in FR-SAC-003 need to cover an 'all users' category (e.g., a default role or public access), or are the listed user types (field operator, analyst, admin) exhaustive?
- 场景：A stakeholder asks whether all authenticated users, regardless of specific role, should have a baseline set of permissions.
- 模型初步去向：retained
- 模型解释：The original FR requires role-based access control for different user types, using 'e.g.' to indicate a non-exhaustive list. It does not explicitly state whether an 'all users' default role or baseline permissions must be covered. The draft clarifies that the system should define permissions for all applicable user categories, including any default 'all users' role if present. This is an in-scope elaboration supported by the source's non-exhaustive examples.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall define access permissions for all user categories, including any default 'all users' role if applicable.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-8afc448c15a1
- 主题：Compute traffic metrics
- 审查问题：FR-REP-001 requires pre-defined reports on traffic volume, incident frequency, and road condition trends, but the FR does not specify how these metrics are computed. Does the element 'Compute traffic metrics' require a documented connection to the reporting functionality, or is metric computation assumed to be external/upstream?
- 场景：A user requests a traffic volume report; the system may either rely on pre-computed metrics or compute them at report generation time.
- 模型初步去向：unsupported
- 模型解释：FRBLOCK-007 only requires generating pre-defined reports on traffic volume, incident frequency, and road condition trends; it does not require the system to compute these metrics. The computation may be external or upstream, so the draft obligation introduces an unsupported computation requirement.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall compute traffic volume, incident frequency, and road condition trend metrics as needed to generate the pre-defined reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-0b742696e428
- 主题：Configure new data source types without major software changes
- 审查问题：FR-REP-003 provides ad-hoc reporting tools for querying and visualizing data. Does the isolated element 'Configure new data source types without major software changes' need a documented connection to ad-hoc reporting, or is this capability out of scope?
- 场景：An analyst wants to add a new database as a data source for ad-hoc reports without requiring code changes.
- 模型初步去向：covered
- 模型解释：The original FR FR-DCI-003 (in FRBLOCK-001) already states: 'The system shall allow for the configuration of new data source types without requiring major software changes.' This general capability applies to ad-hoc reporting as a subset, so the nominated obligation is covered.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall allow configuration of new data source types for ad-hoc reporting without major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-dc05a306f651
- 主题：all users
- 审查问题：The actor 'all users' is graph-isolated; should this FR block explicitly specify which user roles are included in 'all users' to avoid ambiguity?
- 场景：Without role definition, the security requirements may be applied inconsistently; clarification is needed.
- 模型初步去向：retained
- 模型解释：The checked original FRs use the actor 'all users' in security requirements but do not define which user roles are included, so a clarification obligation is missing and is in scope.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall define the scope of 'all users' for security requirements.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-65f26d013389
- 主题：Compute traffic metrics
- 审查问题：Could the isolated element 'Compute traffic metrics' need a documented connection to security monitoring or audit logging in this FR block?
- 场景：Traffic metrics might be relevant for detecting security anomalies, but no connection is documented.
- 模型初步去向：unsupported
- 模型解释：The draft introduces a conditional requirement to document a connection between traffic metrics and audit logging that is not supported by any original FR. FRBLOCK-008 requires audit logging of user activities and system events but does not state that traffic metrics are used for security monitoring or that such a connection must be documented.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：If traffic metrics are used for security monitoring, the system shall document the connection to audit logging.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：15 条提名

### OPERATION-9c33eb1c3f74
- 主题：Normalized data stored in central database
- 审查问题：Does the data collection and ingestion block require an operation to retrieve normalized data from the central database for downstream consumers?
- 场景：Downstream modules such as traffic prediction and alerting need to access normalized data, but no read operation is specified in this block.
- 模型初步去向：unsupported
- 模型解释：The draft introduces an obligation to provide a read operation for downstream consumers, but the only evidence cited is that normalized data is stored in a central database. No original FR specifies such a read operation or identifies downstream consumers requiring access.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall provide a read operation to retrieve normalized data from the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-ff3e64c096de
- 主题：Detect and classify incidents
- 审查问题：Should the system support updating or reclassifying an incident after initial detection, and what user roles or conditions permit such updates?
- 场景：Incident classification may need refinement as more information becomes available; the FR block does not specify whether classification can be changed after initial detection.
- 模型初步去向：retained
- 模型解释：The original FRs only require detection and initial classification of incidents; none specify the ability to update or reclassify an incident after detection, and no FR assigns this outside the system. The obligation is in-scope for incident management and supported by the operational need to refine classification as more information becomes available.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall allow authorized users to update the classification of a detected incident under defined conditions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f939eb67b240
- 主题：Support machine learning models
- 审查问题：Is there a need for the system to support retraining or updating machine learning models, and what triggers such updates?
- 场景：Predictive analysis based on machine learning models may require periodic retraining to maintain accuracy; the FR block only mentions support for models, not their lifecycle.
- 模型初步去向：retained
- 模型解释：The original FRs only require support for machine learning models and predictive analysis, and possibly batch ingestion for training, but do not address retraining/updating models or triggers. Maintaining model accuracy is an in-scope business need.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall provide mechanisms to retrain and update machine learning models when performance degrades or new data becomes available.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-0a251e0a66f5
- 主题：Allow users to query archived data via SQL-based tools
- 审查问题：What specific SQL-based tools are supported for querying archived data, and what access controls apply to this query operation?
- 场景：A user needs to retrieve archived data for analysis; the system must provide a defined set of SQL-based tools and enforce appropriate permissions to protect archived data.
- 模型初步去向：unsupported
- 模型解释：The draft obligation adds read-only access, approved tools, and role-based access control, none of which are stated in FRBLOCK-003 or any original FR. FRBLOCK-003 only allows querying archived data via SQL-based tools; role-based access control is mentioned generally in FRBLOCK-006 but not applied to archived data querying.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide read-only SQL-based query access to archived data using approved tools, with role-based access control.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6971fcf37cfd
- 主题：Support automated data purging policies
- 审查问题：How are automated data purging policies configured, scheduled, and verified to ensure they manage storage limits without deleting data prematurely?
- 场景：Storage limits are reached; the system must automatically purge data according to defined policies while preserving required retention periods and providing auditability.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 requires support for automated data purging policies but does not specify configurable retention parameters, prevention of premature deletion, or audit logging of purged data. The draft adds these operational details, which are necessary to ensure retention periods are preserved and purges are auditable.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall execute automated data purging according to configurable retention policies and provide audit logs of purged data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-635a8c4ea312
- 主题：Provide API for real-time consumption
- 审查问题：Should the API provided for external applications support a read operation to retrieve real-time traffic and weather data?
- 场景：FR-DPO-005 requires providing an API for external applications to consume data, but does not specify the operations (e.g., read, subscribe) that the API must support. External applications need a defined operation to retrieve data.
- 模型初步去向：covered
- 模型解释：FRBLOCK-004 already requires the system to provide an API for external applications to consume traffic and weather data in real time, which is equivalent to supporting a read operation for retrieving that real-time data.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The API shall support a read operation that allows external applications to retrieve real-time traffic and weather data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-535534b72c5c
- 主题：Provide real-time data feeds to MI Drive
- 审查问题：Should the system support a push-based operation to deliver real-time data feeds to MI Drive, or is a pull-based mechanism sufficient?
- 场景：FR-DPO-002 requires real-time data feeds to MDOT’s MI Drive system, but does not specify whether the system should actively push data or allow MI Drive to pull data via API. The delivery mechanism affects real-time performance and system design.
- 模型初步去向：retained
- 模型解释：The original FR (FRBLOCK-004) requires providing real-time data feeds to MDOT’s MI Drive system, but it does not specify whether the delivery mechanism should be push-based or pull-based. Defining and implementing a delivery mechanism is a necessary clarification to fulfill the existing requirement and is not covered by any original FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall define and implement a delivery mechanism for real-time data feeds to MI Drive, specifying whether it is push-based or pull-based.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-53a2c099bc55
- 主题：Custom dashboards
- 审查问题：FR-UIP-006 states that users can create custom dashboards. Does the documented workflow require users to also modify or delete existing custom dashboards? If so, document the obligation for update and delete operations; if not, confirm that creation alone is sufficient.
- 场景：A reviewer observes that only creation of custom dashboards is specified. In practice, users may need to manage dashboards over time, but the FR does not mention update or delete. This question clarifies whether those operations are in scope for this block.
- 模型初步去向：unsupported
- 模型解释：The original FRs (specifically FRBLOCK-005) only state that users can create custom dashboards; none of the checked FRs mention update or delete operations or a dashboard lifecycle requirement. The draft obligation introduces a conditional update/delete requirement without evidence, making it unsupported.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system should allow users to update and delete their custom dashboards if management of dashboard lifecycle is required; otherwise, only creation is required.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-a3455eb84139
- 主题：Log Administrative Actions and Errors
- 审查问题：Should the system provide an operation for administrators to view, filter, and export the logged administrative actions and errors for audit and troubleshooting?
- 场景：An auditor needs to review logs for a specific time period and export them for external analysis.
- 模型初步去向：retained
- 模型解释：The original FRs require logging administrative actions and errors for audit and troubleshooting, but none specifies that administrators can view, filter, or export those logs. The nominated draft extends the logging obligation to include an operational interface for accessing the logs, which is a necessary in-scope business obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall allow administrators to view, filter, and export the audit log.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-047c524af82b
- 主题：Role-Based Access Control
- 审查问题：Should the system include administrative operations to create, modify, and assign roles and permissions to users, or is role assignment assumed to be preconfigured?
- 场景：An administrator needs to add a new user and assign them to an existing role.
- 模型初步去向：retained
- 模型解释：The original FRs state that the system supports role-based access control but do not specify how roles and permissions are managed. Administrative operations are necessary to operationalize RBAC and are not covered by the checked FRs.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall provide administrative operations for managing user roles and permissions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-66497b27ce21
- 主题：Backup and Restore Capabilities
- 审查问题：Should administrators be able to schedule automatic backups and perform partial restores (e.g., only configuration settings) as part of backup and restore capabilities?
- 场景：A configuration change causes a failure; the administrator wants to restore only the previous configuration settings without affecting the database.
- 模型初步去向：retained
- 模型解释：The original FRBLOCK-006 requires backup and restore capabilities for the database and configuration settings, but it does not specify scheduled backups or partial restores. The nomination refines this in-scope obligation by adding administrative control over scheduling and selective restoration.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall support scheduled and partial backup/restore operations for database and configuration settings.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bfe2c70a5486
- 主题：Schedule Automatic Report Generation and Email Delivery
- 审查问题：FR-REP-002 allows users to schedule automatic report generation and email delivery. Does the operation to specify or update the email recipients for a scheduled report need to be explicitly required, or is it implicitly covered by the scheduling function?
- 场景：A user schedules a monthly incident report and needs to change the distribution list after team changes.
- 模型初步去向：retained
- 模型解释：The original FR (FRBLOCK-007) allows scheduling automatic report generation and email delivery, but does not explicitly require the ability to specify or update the email recipients for those scheduled deliveries. This is a necessary operational detail to make scheduled email delivery functional, and it is not covered by the checked original FRs.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：If confirmed, the system shall allow users to specify and update the email recipients for scheduled automatic report delivery.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e2933756876e
- 主题：Enforce secure authentication and authorization
- 审查问题：Does the system include an operation to revoke a user's authentication and authorization, or only to enforce at login?
- 场景：When a user leaves the organization, access must be removed immediately; the FR only describes enforcement, not revocation.
- 模型初步去向：retained
- 模型解释：The original FRBLOCK-008 only requires enforcing secure authentication and authorization, not providing an operation to revoke them. None of the original FRs cover revocation of user authentication/authorization. Revocation is a necessary in-scope business obligation for managing user access.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation to revoke user authentication and authorization.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5d69238cf751
- 主题：Audit logging of user activities and system events
- 审查问题：Does the audit logging function include an operation for authorized users to view and search audit logs?
- 场景：Compliance officers need to review audit trails; if logs are only written but not readable, they cannot be used for oversight.
- 模型初步去向：retained
- 模型解释：The original FRs require audit logging (e.g., FRBLOCK-008) but do not state that authorized users can view or search audit logs. The nominated obligation addresses a valid in-scope business need for compliance oversight and is not covered by the checked original FRs.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall provide authorized users with the ability to view and search audit logs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-4362eb6f486f
- 主题：Compliance with MDIT and FIPS 140-2
- 审查问题：Does the system need an operation to generate compliance reports demonstrating adherence to MDIT and FIPS 140-2?
- 场景：Auditors require documented evidence of compliance; a reporting operation may be necessary.
- 模型初步去向：retained
- 模型解释：FRBLOCK-008 requires compliance with MDIT security standards and FIPS 140-2, but no original FR specifies an operation to generate compliance reports demonstrating adherence. This is a supported in-scope business obligation not found in the original FRs.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall provide authorized users with the ability to generate compliance reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall ensure that batch-ingested historical data is available and accessible to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.

2. [model_preliminarily_retained] The system shall generate the pre-defined reports on traffic volume, incident frequency, and road condition trends whenever a user schedules automatic report generation and email delivery.

3. [model_preliminarily_retained] The system shall ensure that processed data originating from batch ingestion of historical data is stored in the long-term archive and is subsequently published in the standardized formats (e.g., SAE J2354, TMDD).

4. [model_preliminarily_retained] The system shall maintain the long-term archive of all processed data without being solely dependent on Oracle 10G, ensuring continuity of archival operations.

5. [model_preliminarily_retained] The system shall deliver the scheduled report email to the designated recipients when the scheduled automatic report generation and email delivery is triggered.

6. [model_preliminarily_retained] The system shall ensure that historical data ingested in batch for archive backfill is stored in the long-term archive and made available for user queries through SQL-based tools.

7. [model_preliminarily_retained] The system shall perform automated data quality checks on stored normalized data in addition to ingestion-time validation to detect anomalies or inconsistencies not identified during ingestion.

8. [model_preliminarily_retained] The system shall have access to historical traffic data sufficient to generate the required statistical summaries.

9. [model_preliminarily_retained] The system shall allow authorized users to update or reclassify a detected incident under defined conditions, including the roles and permissions required for such updates.

10. [model_preliminarily_retained] The system shall provide mechanisms to retrain and update machine learning models when performance degrades or new data becomes available.

11. [model_preliminarily_retained] The system shall execute automated data purging only after the applicable retention period has elapsed, according to configurable retention policies, and shall record audit logs identifying the data purged, the policy applied, and the timestamp of deletion.

12. [model_preliminarily_retained] The system shall invalidate cached data entries when corresponding archived data is purged.

13. [model_preliminarily_retained] The system shall compute traffic metrics to support the detection of traffic incidents and the generation of traffic incident alerts.

14. [model_preliminarily_retained] The system shall export generated statistical summaries in CSV, JSON, XML, and KML formats for third-party use.

15. [model_preliminarily_retained] The system shall perform automated data quality checks on processed data prior to publication in standardized formats.

16. [model_preliminarily_retained] The system shall provide ad-hoc reporting tools that allow third-party users to create custom reports using exported data.

17. [model_preliminarily_retained] The system shall define user roles and access permissions for data publication, real-time feeds, alerts, and export capabilities to ensure that authorized users, including third-party users and external applications, have appropriate access while preventing unauthorized access.

18. [model_preliminarily_retained] The system shall define and implement a delivery mechanism for real-time data feeds to MI Drive, specifying whether it is push-based or pull-based.

19. [model_preliminarily_retained] The system shall support role-based access control for all user categories, including a default 'all users' role if such a role is defined, ensuring that permissions for that role are specified and enforced.

20. [model_preliminarily_retained] The system shall allow administrators to view, filter, and export audit log entries (including administrative actions and errors) for audit and troubleshooting purposes.

21. [model_preliminarily_retained] The system shall provide administrative operations to create, modify, and assign user roles and permissions.

22. [model_preliminarily_retained] The system shall allow administrators to schedule automatic backups and perform partial restores of database and configuration settings (e.g., restore only configuration settings without affecting the database).

23. [model_preliminarily_retained] The system shall allow users to specify and update the email recipients for scheduled automatic report delivery.

24. [model_preliminarily_retained] The system shall provide an operation to revoke a user's authentication and authorization.

25. [model_preliminarily_retained] The system shall provide authorized users with the ability to view and search audit logs.

26. [model_preliminarily_retained] The system shall provide authorized users with the ability to generate compliance reports demonstrating adherence to MDIT security standards and FIPS 140-2 encryption requirements.

27. [model_preliminarily_retained] The system shall specify the user roles (e.g., field operator, analyst, administrator) that constitute 'all users' for security requirements to ensure consistent application.
