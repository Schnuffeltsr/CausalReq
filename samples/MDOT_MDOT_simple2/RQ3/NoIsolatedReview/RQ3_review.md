# RQ3 审查材料：MDOT_MDOT_simple2 / NoIsolatedReview

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
- 主题：Use Oracle 10G for archiving → Allow users to query archived data via SQL-based tools
- 审查问题：Is there an explicit requirement that ensures users can query archived data via SQL-based tools when the archive is stored using Oracle 10G?
- 场景：The source requirement states the system shall maintain a long-term archive of all processed data using Oracle 10G, and the target requirement states the system shall allow users to query archived data via SQL-based tools. Propagation is enabled, and the dependency between the archive technology and the query capability is documented. Review whether the current obligations adequately cover this dependency.
- 模型初步去向：covered
- 模型解释：The original functional requirement FRBLOCK-003 contains both FR-DSA-001, which specifies maintaining a long-term archive using Oracle 10G, and FR-DSA-003, which explicitly allows users to query archived data via SQL-based tools. Together these obligations cover the draft requirement.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide SQL-based query access to archived data stored in Oracle 10G.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Support batch ingestion of historical data → Support machine learning models
- 审查问题：Given that FRBLOCK-001 states the system shall support batch ingestion of historical data for backfilling archives and training models, and FRBLOCK-002 states the system shall support machine learning models for predictive analysis of traffic trends and incident likelihood, is there an explicit requirement ensuring that the batch-ingested historical data is actually used to train the machine learning models referenced in FRBLOCK-002?
- 场景：The source requirement (FRBLOCK-001) enables the target requirement (FRBLOCK-002) by providing historical data for training models. However, no direct requirement currently mandates that the batch ingestion process feeds the machine learning model training for predictive analysis of traffic trends and incident likelihood.
- 模型初步去向：retained
- 模型解释：No original FR explicitly requires that batch-ingested historical data be provided to the machine learning model training process. FRBLOCK-001 states batch ingestion is for training models, and FRBLOCK-002 requires machine learning models for predictive analysis, but the linkage is not explicitly stated.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall provide batch-ingested historical data to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Accept real-time data inputs from external sources → Normalized data stored in central database
- 审查问题：Does the system ensure that normalized data from accepted real-time data inputs (probe vehicles, traffic sensors, weather stations, traveler information systems) is stored in the central database?
- 场景：Real-time data is accepted from external sources such as probe vehicles, traffic sensors, weather stations, and traveler information systems, and the system is expected to produce normalized data stored in the central database.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already specifies that the system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, and lists 'Outputs: Normalized data stored in a central database' as an output of that function. This is an equivalent obligation to the draft.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall store normalized data resulting from accepted real-time data inputs in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports
- 审查问题：For the scheduled automatic report generation and email delivery feature, is it required that the system generates the pre-defined reports (traffic volume, incident frequency, and road condition trends) whenever a schedule triggers?
- 场景：A user has configured a schedule for automatic report generation and email delivery. At the scheduled time, the system is expected to produce the pre-defined reports.
- 模型初步去向：retained
- 模型解释：The original FRs separately require generating pre-defined reports and scheduling automatic report generation with email delivery, but no original FR explicitly states that a schedule trigger must cause generation of those specific pre-defined reports. The dependency relation TRIGGERS from FRBLOCK-007 supports this obligation, and it is within scope.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall generate the pre-defined reports when the scheduled automatic report generation and email delivery is triggered.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Automated data purging policies → Support automated data purging policies
- 审查问题：Does the dependency between the definition of automated data purging policies and the system's ability to support those policies correctly ensure that support functionality is only enabled after the policies are defined and active, without assuming implementation details not present in the requirements?
- 场景：A system is being specified to manage storage limits through automated data purging. The requirements include both 'automated data purging policies' and 'support automated data purging policies', with a dependency indicating that the former depends on the latter.
- 模型初步去向：unsupported
- 模型解释：The original requirements only state that the system shall support automated data purging policies. They do not specify a dependency between policy definition/activation and the enabling of support functionality. The draft obligation introduces a new conditional activation requirement not present in any original FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall not activate support for automated data purging policies until those policies are defined and active, ensuring that support functions are not operational in the absence of underlying policy definitions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Use Oracle 10G for archiving → Publish processed data in standardized formats
- 审查问题：Does the requirement to use Oracle 10G for archiving need to be reviewed to ensure it does not prevent the system from publishing processed data in standardized formats, given that the archive is the source for published data?
- 场景：The system is required to maintain a long-term archive of all processed data using Oracle 10G (FRBLOCK-003: 'using Oracle 10G', 'maintain a long-term archive of all processed data'), and to publish processed data in standardized formats (FRBLOCK-004: 'publish processed data in standardized formats'). The dependency shows publishing relies on the archive.
- 模型初步去向：retained
- 模型解释：The original FRs require archiving processed data using Oracle 10G (FRBLOCK-003) and publishing processed data in standardized formats (FRBLOCK-004), but no original FR explicitly requires the archive to support retrieval and publication. The draft obligation derives from the dependency between these requirements and is necessary to ensure both can be satisfied.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：Ensure that the Oracle 10G archive supports retrieval and publication of processed data in the required standardized formats (SAE J2354, TMDD).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Input data fields → Validate incoming data and reject invalid data
- 审查问题：Should the system be required to validate incoming real-time data inputs (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) against predefined quality rules and reject invalid or malformed data?
- 场景：A real-time data stream includes fields for GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. Some records contain malformed or invalid values according to predefined quality rules.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-001 (FR-DCI-002) already states: 'The system shall validate incoming data against predefined quality rules and reject invalid or malformed data.' This covers the nominated obligation for real-time data inputs, including the listed fields, because the FR applies to incoming data generally and the evidence links those fields to the accepted real-time data inputs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall validate incoming real-time data inputs including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility against predefined quality rules and reject invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Support batch ingestion of historical data → Publish processed data in standardized formats
- 审查问题：Does the system's support for batch ingestion of historical data obligate it to publish the processed data in standardized formats, given that batch ingestion enables the long-term archive and the archive depends on publication?
- 场景：A user initiates batch ingestion of historical data for backfilling archives and training models. The system processes the data but does not automatically publish it in standardized formats. The long-term archive maintenance depends on publication of processed data, so the archive could become incomplete if publication is not performed.
- 模型初步去向：covered
- 模型解释：Original FR-DPO-001 (FRBLOCK-004) already requires the system to publish processed data in standardized formats (SAE J2354, TMDD). This general obligation covers all processed data, including historical data ingested via batch for backfilling archives, so the nominated draft obligation is already stated.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall publish processed data in standardized formats (SAE J2354, TMDD) for all historical data ingested via batch, when that data is intended for backfilling archives.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Input data fields → Accept real-time data inputs from external sources
- 审查问题：Does the FR clearly specify which of the listed input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) are mandatory for each real-time data input from the specified sources, and which are optional?
- 场景：The system is required to accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The FR lists specific data fields that these sources may provide. The dependency indicates that the accept function depends on these fields being present. However, it is not explicitly stated whether all fields are required for every input or if some are conditional on the source type.
- 模型初步去向：retained
- 模型解释：The original FRs list input data fields and the accept real-time data function but do not specify which fields are mandatory or optional per source. The draft obligation addresses a legitimate business gap by requiring the system to define this distinction to support reliable input processing.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall define the mandatory and optional data fields for each type of real-time data input source.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Support batch ingestion of historical data → Maintain long-term archive of processed data
- 审查问题：Does the required support for batch ingestion of historical data for backfilling archives create an obligation for the system to maintain a long-term archive of all processed data?
- 场景：The system is required to support batch ingestion of historical data for backfilling archives (FRBLOCK-001: "The system shall support batch ingestion of historical data for backfilling archives and training models."). This capability is intended to backfill archives, which implies a long-term archive exists and must be maintained.
- 模型初步去向：covered
- 模型解释：The obligation to maintain a long-term archive of all processed data is already stated in original FR FRBLOCK-003: 'The system shall maintain a long-term archive of all processed data using Oracle 10G.' This includes historical data ingested via batch backfill, so the draft obligation is covered.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall maintain a long-term archive of all processed data, including historical data ingested via batch backfill, to ensure the archive remains complete and accurate.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Use Oracle 10G for archiving → Maintain long-term archive of processed data
- 审查问题：Does the system maintain a long-term archive of all processed data using Oracle 10G technology?
- 场景：The requirement states that the system shall use Oracle 10G for archiving, and separately, that it shall maintain a long-term archive of all processed data. The dependency indicates that the maintenance of the archive relies on the use of Oracle 10G. We need to verify that when the source obligation (using Oracle 10G) is satisfied, the target obligation (maintaining the archive) is also satisfied.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-003 already explicitly states the obligation: 'The system shall maintain a long-term archive of all processed data using Oracle 10G' (FR-DSA-001). Therefore the draft obligation is equivalent to an existing original FR.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall maintain a long-term archive of all processed data using Oracle 10G technology.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Configure Data Sources, Algorithms, and Output Formats → Log Administrative Actions and Errors
- 审查问题：Given that the system shall allow administrators to configure data sources, algorithms, and output formats, and that FR-SAC-002 requires logging all administrative actions and errors, does the current requirements specification adequately ensure that configuration changes performed by administrators are logged?
- 场景：An administrator uses the system to modify data source configurations, algorithm parameters, or output format settings. The system's functional requirement FR-SAC-002 mandates that all administrative actions and errors be logged. However, the current specification states only that the system shall allow administrators to configure these items, without explicitly tying this configuration activity to the logging requirement. This raises a potential gap where configuration actions may occur without being recorded.
- 模型初步去向：covered
- 模型解释：FR-SAC-002 already requires logging all administrative actions, which includes configuration changes to data sources, algorithms, or output formats. The draft obligation is a specific restatement of this existing requirement.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system shall log an administrative action whenever an administrator configures data sources, algorithms, or output formats, in accordance with FR-SAC-002.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Accept real-time data inputs from external sources → Validate incoming data and reject invalid data
- 审查问题：Does the requirement set clearly obligate the system to validate every real-time data input it accepts from probe vehicles, traffic sensors, weather stations, and traveler information systems against predefined quality rules, and to reject invalid or malformed data?
- 场景：The system is specified to accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. It is also specified to validate incoming data against predefined quality rules and reject invalid or malformed data. The dependency between acceptance and validation may be implicit, leaving unclear whether validation must cover all accepted real-time inputs.
- 模型初步去向：covered
- 模型解释：Original FRBLOCK-001 already contains FR-DCI-001, which requires accepting real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems, and FR-DCI-002, which requires validating incoming data against predefined quality rules and rejecting invalid or malformed data. Read together, FR-DCI-002 applies to the real-time inputs accepted under FR-DCI-001, stating the same obligation as the draft.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall validate all real-time data inputs accepted from external sources (probe vehicles, traffic sensors, weather stations, traveler information systems) against predefined quality rules and reject any invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Schedule Automatic Report Generation and Email Delivery → Email Delivery
- 审查问题：Does the requirements set explicitly state that scheduling automatic report generation and email delivery (FRBLOCK-007: 'The system shall allow users to schedule automatic report generation and email delivery.') must trigger the corresponding email delivery event, ensuring scheduled reports are delivered?
- 场景：A user schedules automatic report generation and email delivery. When the scheduled time arrives, the system generates the report and should perform email delivery to the intended recipients.
- 模型初步去向：covered
- 模型解释：Original FR FRBLOCK-007 already states 'The system shall allow users to schedule automatic report generation and email delivery', which implies that email delivery will be executed when the scheduled report generation occurs. The draft obligation does not add a new requirement beyond this existing specification.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall perform email delivery of the generated report when the scheduled automatic report generation and email delivery is executed.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：High-volume data display → De-cluttering features
- 审查问题：Is there a requirement that high-volume data display triggers de-cluttering features?
- 场景：The system is displaying a high volume of data, causing visual complexity.
- 模型初步去向：unsupported
- 模型解释：The source FR only requires the system to support de-cluttering features during high-volume data display; it does not require that high-volume data display automatically triggers or activates those features. The draft obligation's automatic activation is an unsupported extension.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：When high-volume data display occurs, de-cluttering features shall be activated to reduce visual complexity.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Maintain long-term archive of processed data → Publish processed data in standardized formats
- 审查问题：Does the obligation to 'maintain a long-term archive of all processed data' inherently guarantee that the archived data is available in a form that can be 'publish[ed] ... in standardized formats (SAE J2354, TMDD)', or could the archive store data in a representation that requires additional transformation before publishing?
- 场景：The system successfully maintains an archive of all processed data but stores the data in an internal proprietary format that is not directly publishable as SAE J2354 or TMDD. Without a separate mechanism to export or convert the archived data into the required standardized formats, the publishing requirement cannot be met even though the archive exists.
- 模型初步去向：retained
- 模型解释：The original FRs require maintaining a long-term archive of processed data (FRBLOCK-003) and publishing processed data in standardized formats (FRBLOCK-004), but neither explicitly requires the ability to export archived data into those formats. This is an in-scope, supported dependency gap.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide a capability to export archived processed data into SAE J2354 and TMDD standardized formats for publication.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the system ensure that historical data ingested through batch processing, as described in 'The system shall support batch ingestion of historical data for backfilling archives and training models,' is subsequently maintained in the long-term archive and made available when users 'query archived data via SQL-based tools'?
- 场景：A user needs to query historical data that was loaded via batch ingestion specifically to backfill the archive. The system supports batch ingestion for backfilling archives, and the archive is supposed to 'maintain a long-term archive of all processed data,' but it is not clear from the requirements whether backfilled data is automatically included in the archive and exposed to SQL-based query tools.
- 模型初步去向：covered
- 模型解释：The original FRs already state equivalent obligations: FRBLOCK-001 requires support for batch ingestion of historical data for backfilling archives, and FRBLOCK-003 (FR-DSA-001, FR-DSA-003) requires maintaining a long-term archive of all processed data and allowing users to query archived data via SQL-based tools. Together they ensure that historical data ingested via batch for archive backfill is stored in the archive and accessible through SQL, so the draft obligation is already covered.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：When batch ingestion is used for backfilling archives, all ingested historical data shall be stored in the long-term archive of processed data and shall be accessible to users through SQL-based query tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Detect and classify incidents → Incident reports
- 审查问题：Does the system generate an incident report with time, location, type, and severity for each incident it detects and classifies?
- 场景：The system has detected and classified at least one incident as a crash, debris, stalled vehicle, or work zone.
- 模型初步去向：covered
- 模型解释：FRBLOCK-002 already states that the system outputs incident reports with time, location, type, and severity for detected and classified incidents.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall generate an incident report containing time, location, type, and severity for each incident detected and classified.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Maintain long-term archive of processed data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the requirement to 'maintain a long-term archive of all processed data' (FRBLOCK-003) alone guarantee that users can query archived data via SQL-based tools, or is an explicit requirement needed to provide SQL-based query capabilities on the archive?
- 场景：The system is required to maintain a long-term archive of all processed data (FRBLOCK-003). The target capability is to allow users to query archived data via SQL-based tools (FRBLOCK-003). The dependency model indicates that querying depends on the archive, but it is unclear if the source obligation alone ensures the target.
- 模型初步去向：covered
- 模型解释：The original FR FRBLOCK-003 explicitly includes the requirement that the system shall allow users to query archived data via SQL-based tools (FR-DSA-003), matching the draft obligation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall allow users to query archived data via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Input data fields → Normalized data stored in central database
- 审查问题：Is there an existing requirement that the system normalize and store the listed input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) in the central database after they are accepted?
- 场景：The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The accepted input data fields include GPS data, speed, location, road condition reports, temperature, precipitation, visibility. The target FR states 'Normalized data stored in a central database.' Review whether an obligation exists that guarantees these specific input data fields are normalized and stored.
- 模型初步去向：covered
- 模型解释：FRBLOCK-001 already states that the system shall accept the listed real-time input data fields and that the output is normalized data stored in a central database, which covers normalizing and storing accepted inputs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall normalize each accepted input data field (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) and store the normalized data in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：0 条提名

## operation：32 条提名

### OPERATION-3a6a65f761ec
- 主题：Normalized data stored in central database
- 审查问题：Should the system provide a query or retrieval operation for authorized consumers to access normalized data from the central database?
- 场景：A downstream analytics service needs to read normalized data for real-time traffic metrics.
- 模型初步去向：retained
- 模型解释：The original FRs specify that normalized data is stored in a central database and include access control mechanisms for authorized users, but none specify a read, query, or retrieval operation for authorized consumers to access that normalized data from the central database. The obligation is therefore a supported, in-scope addition not covered by existing FRs.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall provide a read operation to retrieve normalized data from the central database for authorized consumers.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c92c66dc0c44
- 主题：Accept real-time data inputs from external sources
- 审查问题：Should the system send an acknowledgment to the source system after successfully accepting and processing a real-time data input?
- 场景：A probe vehicle sends a GPS data packet and needs confirmation that it was received and accepted.
- 模型初步去向：unsupported
- 模型解释：The draft obligation to return an acknowledgment to the data source is not stated in any original FR. FRBLOCK-001 only requires accepting real-time data inputs, not acknowledging the source after successful ingestion. No evidence supports this additional requirement.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall return an acknowledgment to the data source upon successful ingestion of each real-time data input.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f191aa09fba3
- 主题：Validate incoming data and reject invalid data
- 审查问题：Should the system log or alert operators when incoming data is rejected due to quality rule violations?
- 场景：A weather station sends malformed temperature readings; operators need visibility into rejected records to diagnose sensor issues.
- 模型初步去向：retained
- 模型解释：The original FRs require validation and rejection of invalid data but do not specify logging or alerting operators when data is rejected due to quality rule violations. The screening notes confirm no original FR covers this obligation, and the need for operator visibility into rejected records is within the system's data quality scope.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall log all rejected data records and provide an alerting mechanism for quality rule violations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-eecf0fc2c63b
- 主题：Configure new data source types without major software changes
- 审查问题：Should the system restrict the configuration operation to authorized administrators and provide an audit trail of configuration changes?
- 场景：Only designated administrators should be able to add or modify data source type definitions to prevent unauthorized changes.
- 模型初步去向：covered
- 模型解释：Original FR-SAC-001 allows administrators to configure data sources, FR-SAC-003 supports role-based access control for different user types, and FR-SAC-002 requires logging of all administrative actions. Together, these cover the obligation to restrict configuration of data source types to authorized administrators and maintain an audit trail.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall enforce role-based access control for configuration of data source types and maintain an audit log of configuration changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e9693c61143c
- 主题：Support batch ingestion of historical data
- 审查问题：Should the batch ingestion operation support idempotent processing to prevent duplicate records when the same historical data file is ingested more than once?
- 场景：A data engineer re-ingests a historical weather data file after a partial failure; duplicate records would skew model training.
- 模型初步去向：retained
- 模型解释：FRBLOCK-001 requires batch ingestion of historical data but does not specify idempotent processing or duplicate prevention. The operational scenario identifies a legitimate business need to avoid duplicate records when the same file is re-ingested after a partial failure. None of the reviewed original FRs state an equivalent obligation, and the requirement remains within the scope of the batch ingestion operation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：8
- 草案：The system shall ensure batch ingestion is idempotent, detecting and preventing duplicate historical data records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f07db0a5ce46
- 主题：Incident reports
- 审查问题：Should the system provide an operation to retrieve incident reports for authorized users?
- 场景：A traffic management operator needs to access incident reports generated by the system to review and act on detected incidents.
- 模型初步去向：retained
- 模型解释：The original FRs mention incident reports as outputs and provide generic data access/viewing but do not specify an operation for authorized users to retrieve incident reports. The nominated obligation is in-scope and supported by the presence of incident reports.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall allow authorized users to retrieve incident reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7a345b34a79e
- 主题：Incident reports
- 审查问题：Should the system provide an operation to update incident report information after initial automatic generation?
- 场景：An operator may need to correct or update the severity or type of an incident after manual verification or further investigation.
- 模型初步去向：retained
- 模型解释：The original FRs specify that incident reports are generated with fields such as time, location, type, and severity, but none of the checked FRs include an operation to update incident report information after initial automatic generation. The operational need to correct or update incident details after manual verification is a supported, in-scope business obligation not found in the original FRs.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：8
- 草案：The system shall allow authorized users to update incident report fields.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5e05cd5acf5a
- 主题：Automated data purging policies
- 审查问题：What operation allows authorized administrators to configure the automated data purging policies that manage storage limits?
- 场景：The FR requires supporting automated data purging policies, but does not specify how these policies are defined or adjusted, leaving a gap in storage management.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 requires automated data purging policies but does not specify how they are configured or who may configure them. The draft adds an administrative configuration operation, which is a necessary in-scope capability to meet the storage limit requirement and is not stated in the original FRs.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation for authorized administrators to configure automated data purging policies to meet storage limit requirements.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-bfbbd7881f7c
- 主题：Allow users to query archived data via SQL-based tools
- 审查问题：What operation controls which users are authorized to query archived data via SQL-based tools?
- 场景：The FR permits users to query archived data, but does not define how access permissions are granted, modified, or revoked, potentially leading to unauthorized access.
- 模型初步去向：retained
- 模型解释：The original FR FRBLOCK-003 only states that users are allowed to query archived data via SQL-based tools, but it does not define any operation for managing user permissions. Screening notes across all original FRs confirm no existing requirement covers an administrator operation to grant, modify, or revoke permissions for this access. The draft obligation is supported by the scenario and fills a necessary gap in access control for the archived data query feature.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation for administrators to manage user permissions for querying archived data via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-79872daa2888
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：What operation allows administrators to manually invalidate or refresh the dynamic cache when underlying data changes?
- 场景：Dynamic caching is implemented, but no operation is specified for cache invalidation or refresh, risking stale data being served to users.
- 模型初步去向：retained
- 模型解释：FRBLOCK-003 requires dynamic caching for frequently accessed data, but none of the original FRs specify a manual invalidation or refresh operation. The draft identifies a necessary cache consistency operation to prevent stale data, which is an in-scope business obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation to invalidate or refresh cached data to ensure consistency with the underlying data source.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-fbf116a306df
- 主题：Maintain long-term archive of processed data
- 审查问题：What operation allows authorized users to restore archived data back into the operational environment when needed?
- 场景：The FR mandates maintaining a long-term archive, but does not specify an operation to restore archived data, which is essential for recovery or reprocessing.
- 模型初步去向：covered
- 模型解释：An original FR already requires backup and restore capabilities for the database (screening FRBLOCK-006: 'The system shall provide backup and restore capabilities for the database and configuration settings'), which encompasses restoring archived data into the operational environment upon authorized request. The authorization aspect is supported by the RBAC requirement.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：8
- 草案：The system shall provide an operation to restore archived data into the operational environment upon authorized request.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-65af4a21ad85
- 主题：Publish processed data in standardized formats
- 审查问题：Does the system need to support updating or retracting previously published standardized data?
- 场景：After initial publication, data corrections or updates are required due to revised source data or errors.
- 模型初步去向：retained
- 模型解释：The original FR requires publishing processed data in standardized formats but does not address updates or retractions. The obligation is an in-scope extension needed to handle data corrections or revised source data after initial publication.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide a mechanism to update or retract previously published standardized data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-675d025083e3
- 主题：Provide real-time data feeds to MI Drive
- 审查问题：Should the system support an operation to restart or reconfigure the MI Drive data feed without system downtime?
- 场景：MDOT changes the MI Drive endpoint or authentication credentials, requiring a feed reconfiguration.
- 模型初步去向：retained
- 模型解释：The original FRs require providing real-time data feeds to MI Drive but do not state an administrative operation to reconfigure the feed connection when endpoint or credentials change. Such reconfiguration is a necessary operational capability to maintain the required feed and is not excluded by any original FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide an administrative operation to reconfigure the MI Drive data feed connection.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-33e18cbfdd8e
- 主题：Generate alerts
- 审查问题：Should the system allow operators to acknowledge or suppress generated alerts?
- 场景：Duplicate or false alerts are generated, requiring operator intervention to manage alert lifecycle.
- 模型初步去向：retained
- 模型解释：The original FRs specify that the system shall generate alerts (FRBLOCK-004) but do not include operator acknowledgment or suppression of those alerts. The proposed obligation is an in-scope extension of the alert functionality, addressing operator intervention for duplicate or false alerts.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall support operator acknowledgment and suppression of generated alerts.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-77bd5217633e
- 主题：Support data export formats
- 审查问题：Is there a need for an operation to schedule automated exports or are exports only on-demand?
- 场景：Third parties require periodic data extracts (e.g., daily CSV) without manual intervention.
- 模型初步去向：unsupported
- 模型解释：The draft obligation requires scheduled automated exports, but the only cited original FR (FRBLOCK-004) supports exporting data in CSV, JSON, XML, and KML formats without specifying any scheduling or automation. No original FR states a scheduled export operation, so the scheduling requirement is introduced without support.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The system shall provide scheduled automated exports in supported formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d6c698611e89
- 主题：Provide API for real-time consumption
- 审查问题：Should the API support data query parameters to filter the returned traffic and weather data?
- 场景：External applications need to request specific subsets (e.g., by geographic area or time range).
- 模型初步去向：retained
- 模型解释：FRBLOCK-004 requires an API for external applications to consume real-time traffic and weather data, but does not specify filtering capabilities. The scenario establishes that external applications need specific subsets, making query parameter support an in-scope extension not covered by any original FR.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：8
- 草案：The API shall support query parameters for filtering traffic and weather data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5d7631505bcb
- 主题：Data filtering and search
- 审查问题：Is the filtering and search operation sufficiently specified to support combined filtering across multiple data types and criteria?
- 场景：A traffic operator needs to filter incidents by location and time simultaneously, then further narrow by event type to identify patterns.
- 模型初步去向：retained
- 模型解释：The original FR (FRBLOCK-005) specifies filtering and search by location, time, event type, and other relevant criteria, but it does not explicitly require concurrent multi-criteria filtering across all specified data types (traffic, incident, traveler, and weather). The obligation is supported and in scope, and a supplement is needed to clarify cross-data-type combined filtering.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall provide filtering and search functionality that allows users to specify multiple criteria concurrently across traffic, incident, traveler, and weather data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d9f8bece409d
- 主题：Custom dashboards
- 审查问题：Does the custom dashboard creation operation include the ability to save, edit, and share dashboards with other users?
- 场景：A user wants to create a dashboard containing frequently used traffic and weather data views and share it with colleagues for collaborative monitoring.
- 模型初步去向：retained
- 模型解释：The original FR only specifies creation of custom dashboards for frequent data views; saving, editing, and sharing are additional in-scope dashboard management capabilities not found in the checked FRs.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall allow users to create, save, edit, and share custom dashboards consisting of user-selected data views.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5ae87a65a40e
- 主题：Web-based interface for viewing data
- 审查问题：Is the data viewing operation specified with respect to data refresh frequency and user access control?
- 场景：A user opens the web-based interface to view real-time traffic and incident data, but it is unclear whether data updates automatically or requires manual refresh.
- 模型初步去向：unsupported
- 模型解释：The draft extends the web-based viewing requirement with defined refresh intervals and user access controls, but the cited original FR only states providing a web-based interface for viewing traffic, incident, traveler, and weather data. No original FR specifies data refresh frequency or user access controls for this viewing operation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：8
- 草案：The system shall provide a web-based interface for viewing traffic, incident, traveler, and weather data with defined refresh intervals and appropriate user access controls.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f275b745a9c7
- 主题：Configure Data Sources, Algorithms, and Output Formats
- 审查问题：Should the system provide an operation to test or validate a data source configuration before it is saved or activated?
- 场景：An administrator configures a new data source and wants to ensure the connection parameters are correct before the configuration goes live.
- 模型初步去向：retained
- 模型解释：The original FRs state that administrators can configure data sources but do not specify an operation to validate a data source configuration before saving or activation. This is an in-scope business obligation that supports safe configuration management and is not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system must allow administrators to validate data source configurations before applying them.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-83238edebfe6
- 主题：Log Administrative Actions and Errors
- 审查问题：Should the system provide an operation to search, filter, and export administrative action and error logs?
- 场景：An auditor needs to review all administrative actions performed during a specific time period to investigate a security incident.
- 模型初步去向：retained
- 模型解释：The original FRs require logging administrative actions and errors for audit and troubleshooting purposes, but none of the checked original FRs specify the ability to search, filter, or export those logs. The proposed capability is a necessary in-scope extension to make the audit log usable for its stated purpose.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system must allow administrators to search, filter, and export administrative action and error logs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1f39dc181680
- 主题：Role-Based Access Control
- 审查问题：Should the system provide an operation to assign and modify user roles?
- 场景：A field operator is promoted to analyst, and the administrator needs to update the user's access rights accordingly.
- 模型初步去向：retained
- 模型解释：The original FRs include role-based access control (FRBLOCK-006) but do not explicitly require an operation for administrators to assign or modify user roles. This is an in-scope operational requirement needed to support the stated RBAC capability.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system must allow administrators to assign and modify roles for user accounts.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-2c434449735e
- 主题：Backup and Restore Capabilities
- 审查问题：Should the system provide an operation to schedule automatic backups of the database and configuration settings?
- 场景：The operations team wants to ensure that backups are taken regularly without manual intervention to minimize data loss risk.
- 模型初步去向：retained
- 模型解释：The original FR requires backup and restore capabilities for the database and configuration settings, but does not explicitly require the ability to schedule automatic backups. This is a related, in-scope business obligation not found in the checked original FRs.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：8
- 草案：The system must allow administrators to schedule automatic backups of the database and configuration settings.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c3937d33a986
- 主题：Generate Pre-defined Reports
- 审查问题：Is the operation 'Generate Pre-defined Reports' required to be available to users, and should it support both on-demand execution and predefined scheduling?
- 场景：A traffic operations analyst needs to retrieve a standard report on traffic volume trends for a weekly meeting.
- 模型初步去向：retained
- 模型解释：Original FRs (FR-REP-001, FR-REP-002) already require generating pre-defined reports and scheduled automatic generation, but do not explicitly require on-demand execution by users. The operational scenario of an analyst retrieving a standard report supports on-demand execution as an in-scope business obligation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall generate pre-defined reports on traffic volume, incident frequency, and road condition trends upon user request or according to a defined schedule.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f0d1798b7b36
- 主题：Schedule Automatic Report Generation and Email Delivery
- 审查问题：Is the operation 'Schedule Automatic Report Generation and Email Delivery' expected to allow users to define recurrence, recipients, and report parameters for automated delivery?
- 场景：A system administrator configures a daily 6 AM report on road condition trends to be emailed to the maintenance team.
- 模型初步去向：retained
- 模型解释：Original FRBLOCK-007 states the system shall allow users to schedule automatic report generation and email delivery, but does not specify that users can define recurrence, recipients, and report parameters. These details are necessary to operationalize the scheduling feature and are supported by the nomination scenario.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow users to schedule automatic report generation and email delivery, including specification of recurrence, recipients, and report parameters.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d470fe6a4e8d
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Is the operation 'Provide Ad-hoc Reporting Tools' required to support user-defined queries, data filtering, and visualization without predefined report templates?
- 场景：A manager wants to explore incident frequency by corridor and time of day beyond the pre-defined reports.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 already states: 'The system shall provide ad-hoc reporting tools for querying and visualizing data.' This covers user-defined queries (ad-hoc) and visualization without predefined templates; data filtering is inherent to querying.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall provide ad-hoc reporting tools that enable users to query and visualize data according to their own criteria.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-b5c6162af7a8
- 主题：Report Export Formats
- 审查问题：Is the operation of exporting reports in PDF, Excel, and HTML formats required for all generated reports, including ad-hoc and scheduled reports?
- 场景：After generating an ad-hoc report, a user needs to export it to Excel for further analysis and to PDF for distribution.
- 模型初步去向：covered
- 模型解释：FRBLOCK-007 (FR-REP-004) already states 'Reports must be exportable in PDF, Excel, and HTML formats.' The screening confirms this applies to all report types generated by the system, including pre-defined, scheduled, and ad-hoc reports.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall allow users to export any generated report in PDF, Excel, and HTML formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-3a0f0db65dda
- 主题：Email Delivery
- 审查问题：Is the operation 'Email Delivery' required to ensure that scheduled reports are sent to designated recipients with the report attached or embedded, and should delivery be confirmed?
- 场景：A scheduled report email is sent to traffic supervisors; they must receive the report in the expected format without manual intervention.
- 模型初步去向：unsupported
- 模型解释：The original FR block FRBLOCK-007 only mentions 'email delivery' and scheduling automatic report generation; it does not specify designated recipients, that the report must be attached or embedded, or that delivery confirmation is required. The draft obligation introduces these additional requirements without source support.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：8
- 草案：The system shall deliver scheduled report emails to designated recipients with the report included, and provide delivery confirmation.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-81b67364a515
- 主题：Enforce secure authentication and authorization
- 审查问题：Should the system require step-up authentication for high-risk operations?
- 场景：A user logged in as admin attempts to export audit logs; the system currently only authenticates at login, not per operation.
- 模型初步去向：unsupported
- 模型解释：The cited evidence requires only general secure authentication and authorization; it does not state or imply step-up/re-authentication for sensitive or administrative operations. The draft therefore introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall require re-authentication for operations involving sensitive data or administrative functions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-e485c9b3ad31
- 主题：Audit logging of user activities and system events
- 审查问题：Should authorized users be able to view and export audit logs?
- 场景：An auditor needs to review user activity logs; currently the system records logs but provides no interface to access them.
- 模型初步去向：retained
- 模型解释：The original FR requires audit logging of user activities and system events, but does not specify that authorized users can access these logs. Providing viewing, filtering, and exporting functionality is a necessary elaboration to make the audit logs usable for auditors.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall provide authorized users with the ability to view, filter, and export audit logs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-99d49c1fc965
- 主题：TLS 1.2+ encryption for data transmissions
- 审查问题：Should the system provide an operation to manage TLS certificates (upload, renew, revoke)?
- 场景：An administrator needs to renew an expiring TLS certificate; currently there is no interface to update certificates without downtime.
- 模型初步去向：retained
- 模型解释：The original FRs require TLS 1.2+ encryption for data transmissions but do not specify operations for managing the certificates needed to maintain that encryption. Certificate management is an in-scope operational obligation necessary to fulfill the encryption requirement, and no checked original FR covers it.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall allow authorized administrators to upload and manage TLS certificates used for data transmission encryption.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-857089bfdef6
- 主题：Compliance with MDIT and FIPS 140-2
- 审查问题：Should the system provide an operation to generate compliance reports for MDIT and FIPS 140-2?
- 场景：An auditor requests evidence of FIPS compliance; currently the system has no way to produce a compliance report.
- 模型初步去向：unsupported
- 模型解释：The draft obligation to generate compliance reports is not stated in any original FR. The referenced FR BLOCK-008 only requires compliance with MDIT and FIPS 140-2 standards, not generation of compliance reports. Therefore, the draft introduces an unsupported policy.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：8
- 草案：The system shall generate compliance reports demonstrating adherence to MDIT and FIPS 140-2 standards.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [model_preliminarily_retained] The system shall provide batch-ingested historical data to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.

2. [model_preliminarily_retained] The system shall generate the pre-defined reports (traffic volume, incident frequency, and road condition trends) when a scheduled automatic report generation and email delivery is triggered.

3. [model_preliminarily_retained] The system shall ensure that the Oracle 10G archive supports retrieval of processed data for publication in SAE J2354 and TMDD standardized formats.

4. [model_preliminarily_retained] The system shall specify for each real-time data input source (probe vehicles, traffic sensors, weather stations, traveler information systems) which of the listed data fields (GPS data, speed, location, road condition reports, temperature, precipitation, visibility) are mandatory and which are optional.

5. [model_preliminarily_retained] The system shall make archived processed data available in SAE J2354 and TMDD standardized formats to support publication.

6. [model_preliminarily_retained] The system shall provide a read operation to retrieve normalized data from the central database for authorized consumers.

7. [model_preliminarily_retained] The system shall log all rejected data records and alert operators when incoming data fails quality validation rules.

8. [model_preliminarily_retained] The system shall ensure batch ingestion is idempotent by detecting and preventing duplicate historical data records when the same data file is ingested more than once.

9. [model_preliminarily_retained] The system shall allow authorized users to retrieve incident reports including time, location, type, and severity.

10. [model_preliminarily_retained] The system shall allow authorized users to update incident report fields (e.g., type, severity) after initial automatic generation.

11. [model_preliminarily_retained] The system shall provide an operation for authorized administrators to configure automated data purging policies to meet storage limit requirements.

12. [model_preliminarily_retained] The system shall provide administrators with the ability to grant, modify, and revoke user permissions for querying archived data via SQL-based tools.

13. [model_preliminarily_retained] The system shall provide an operation to invalidate or refresh cached data to ensure consistency with the underlying data source.

14. [model_preliminarily_retained] The system shall provide a mechanism to update or retract previously published standardized data.

15. [model_preliminarily_retained] The system shall allow administrators to reconfigure the MI Drive data feed connection (including endpoint and authentication credentials) without requiring system downtime.

16. [model_preliminarily_retained] The system shall allow authorized operators to acknowledge and suppress generated alerts to manage duplicate or false alerts.

17. [model_preliminarily_retained] The system shall support query parameters on the real-time traffic and weather API to filter data by geographic area, time range, and other relevant criteria.

18. [model_preliminarily_retained] The system shall allow users to apply multiple filtering criteria concurrently across traffic, incident, traveler, and weather data.

19. [model_preliminarily_retained] The system shall allow users to save, edit, and share custom dashboards they have created, consisting of user-selected data views.

20. [model_preliminarily_retained] The system shall allow administrators to validate data source configurations before applying them.

21. [model_preliminarily_retained] The system shall provide administrators with the capability to search, filter, and export administrative action and error logs to support audit and troubleshooting activities.

22. [model_preliminarily_retained] The system shall allow administrators to assign and modify roles for user accounts.

23. [model_preliminarily_retained] The system shall allow administrators to schedule automatic backups of the database and configuration settings.

24. [model_preliminarily_retained] The system shall allow users to execute pre-defined reports on demand.

25. [model_preliminarily_retained] The system shall allow users to specify recurrence, recipients, and report parameters when scheduling automatic report generation and email delivery.

26. [model_preliminarily_retained] The system shall provide authorized users with the ability to view, filter, and export audit logs.

27. [model_preliminarily_retained] The system shall allow authorized administrators to upload, renew, and revoke TLS certificates used for data transmission encryption.
