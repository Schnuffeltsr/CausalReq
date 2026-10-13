# RQ3 审查材料：MDOT_MDOT_simple2 / NoFullDocumentValidation

**注意：下列去向只是模型初步筛查，不是人工有效性结论。**

## 运行设置

```json
{
  "signed_propagation": true,
  "isolated_review": true,
  "operation_review": true,
  "full_document_validation": false
}
```

## dependency：20 条提名

### DEP-001
- 主题：Use Oracle 10G for archiving → Allow users to query archived data via SQL-based tools
- 审查问题：Is there a requirement that the SQL-based query tools be compatible with the Oracle 10G archive to ensure users can query archived data?
- 场景：The system is required to use Oracle 10G for archiving and to allow users to query archived data via SQL-based tools. The current functional requirements state 'using Oracle 10G' and 'allow users to query archived data via SQL-based tools', but do not explicitly state whether the SQL-based query tools must be able to access the Oracle 10G archive directly.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall provide SQL-based query tools that can directly query data stored in the Oracle 10G archive.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-002
- 主题：Support batch ingestion of historical data → Support machine learning models
- 审查问题：Does the system specification clearly require that batch-ingested historical data is available to train the machine learning models used for predictive analysis of traffic trends and incident likelihood?
- 场景：A traffic management system supports predictive analysis using machine learning models for traffic trends and incident likelihood. The system must support batch ingestion of historical data for backfilling archives and training models. This dependency indicates that the batch ingestion capability should enable the machine learning models to access historical data for training.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall provide batch-ingested historical data to the machine learning models used for predictive analysis of traffic trends and incident likelihood, so that the models can be trained.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-003
- 主题：Accept real-time data inputs from external sources → Normalized data stored in central database
- 审查问题：Does FRBLOCK-001 require that every real-time data input accepted from external sources (probe vehicles, traffic sensors, weather stations, and traveler information systems) must result in normalized data stored in the central database, or are there conditions under which accepted data may not be stored?
- 场景：The system accepts a real-time data input from a traffic sensor. The functional requirement states: "The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems." Another requirement states: "Normalized data stored in a central database." A reviewer needs to determine whether the accepted input must always be normalized and stored.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall normalize and store in the central database all real-time data inputs it accepts from external sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-004
- 主题：Schedule Automatic Report Generation and Email Delivery → Generate Pre-defined Reports
- 审查问题：When a user schedules automatic report generation and email delivery, does the system generate the pre-defined reports on traffic volume, incident frequency, and road condition trends at the scheduled time?
- 场景：A user schedules automatic report generation and email delivery for a future time. The system is expected to trigger the generation of the pre-defined reports as part of the scheduled task.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：The system shall generate the pre-defined reports when automatic report generation is scheduled.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-005
- 主题：Automated data purging policies → Support automated data purging policies
- 审查问题：Does the system have a requirement to support automated data purging policies, given that these policies are defined to manage storage limits?
- 场景：The source is 'automated data purging policies', meaning automated data purging policies are defined and active to manage storage limits. The target is 'support automated data purging policies', meaning the system has active automated data purging policies to manage storage limits. The documented dependency is that supporting automated data purging policies depends on the existence of those policies.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall support the defined automated data purging policies for managing storage limits.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-006
- 主题：Use Oracle 10G for archiving → Publish processed data in standardized formats
- 审查问题：Does the dependency from 'using Oracle 10G' for archiving to 'publish processed data in standardized formats' require an additional business obligation to ensure the Oracle 10G archive can supply data for publishing?
- 场景：The system is required to 'maintain a long-term archive of all processed data' using Oracle 10G and to 'publish processed data in standardized formats'. A reviewer must determine whether the existing requirements fully cover the dependency, or whether a new obligation is needed to bridge the Oracle 10G archive and the publishing function.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall provide the capability to publish processed data from the Oracle 10G archive in the standardized formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-007
- 主题：Input data fields → Validate incoming data and reject invalid data
- 审查问题：Does the system requirement specify that validation against predefined quality rules and rejection of invalid or malformed data apply to each of the accepted input data fields—GPS data, speed, location, road condition reports, temperature, precipitation, and visibility?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The incoming data contains the listed input data fields. A requirements reviewer checks whether the validation requirement explicitly covers validation and rejection for each of these fields.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall validate GPS data, speed, location, road condition reports, temperature, precipitation, and visibility against predefined quality rules and reject invalid or malformed values for each field.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-008
- 主题：Support batch ingestion of historical data → Publish processed data in standardized formats
- 审查问题：Does the current set of requirements explicitly state that data ingested via batch historical ingestion must be published in standardized formats, or is this implied only through the long-term archive requirement, leaving a potential gap?
- 场景：The source requirement states: 'The system shall support batch ingestion of historical data for backfilling archives and training models.' The target requirement states: 'publish processed data in standardized formats.' The dependency between them is indirect: batch ingestion enables maintaining a long-term archive, and publishing processed data depends on that archive. The model-based priority score (ACE) is low (0.13), indicating that the current evidence does not strongly connect the source directly to the target, which may indicate a missing explicit obligation.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall ensure that historical data ingested via batch processing is processed and published in the standardized formats required by the target requirement.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-009
- 主题：Input data fields → Accept real-time data inputs from external sources
- 审查问题：Does the obligation to accept real-time data inputs from external sources adequately specify the handling of all listed input data fields, including GPS data, speed, location, road condition reports, temperature, precipitation, and visibility?
- 场景：A system is required to accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The input data fields include GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The current obligation states only that the system shall accept these inputs, but does not explicitly address how each field is processed or made available for downstream functions.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall ensure that all listed input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, and visibility) are accepted and made available for processing by the system.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-010
- 主题：Support batch ingestion of historical data → Maintain long-term archive of processed data
- 审查问题：Is there an explicit requirement that the system maintain a long-term archive of processed data, given that FRBLOCK-001 states the system shall support batch ingestion for 'backfilling archives'?
- 场景：The source requirement FRBLOCK-001 specifies batch ingestion for backfilling archives and training models. The phrase 'backfilling archives' implies that a long-term archive exists and needs to be populated, but the target obligation to maintain that archive may not be explicitly defined elsewhere. The positive dependency between batch ingestion and archive maintenance suggests that the archive maintenance requirement is critical and should be clearly specified.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall maintain a long-term archive of all processed data, including data ingested via batch processes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-011
- 主题：Use Oracle 10G for archiving → Maintain long-term archive of processed data
- 审查问题：Given that the system's ability to maintain a long-term archive of processed data depends on using Oracle 10G, is there an explicit obligation in the requirements that the archiving function shall be implemented using Oracle 10G, and is this obligation sufficiently clear to guide implementation and verification?
- 场景：A requirements reviewer examines the dependency between 'using Oracle 10G for archiving' and 'maintaining a long-term archive of all processed data' to confirm that the obligation connecting these two requirements is explicitly stated and not left implicit.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall use Oracle 10G for archiving processed data to maintain a long-term archive of all processed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-012
- 主题：Configure Data Sources, Algorithms, and Output Formats → Log Administrative Actions and Errors
- 审查问题：Is the obligation to log configuration actions performed by administrators (as enabled by 'The system shall allow administrators to configure data sources, algorithms, and output formats.') adequately covered by the requirement to 'log all administrative actions and errors'? Does the current specification make clear that every change to data sources, algorithms, or output formats by an administrator must be logged?
- 场景：A system administrator modifies the output format configuration. The source requirement 'The system shall allow administrators to configure data sources, algorithms, and output formats.' enables this action. The target requirement states the system must 'log all administrative actions and errors.' As a review question, assess whether the dependency from the configuration capability to the logging requirement is correctly and completely specified so that such a configuration change triggers a mandatory log entry.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall log every administrative action where an administrator configures data sources, algorithms, or output formats, in accordance with the requirement to log all administrative actions and errors.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-013
- 主题：Accept real-time data inputs from external sources → Validate incoming data and reject invalid data
- 审查问题：Does the validation requirement for incoming data extend to all real-time data inputs accepted from external sources, and is rejection the only required action for invalid data?
- 场景：A traffic management system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The system must validate each incoming data record against predefined quality rules and reject any invalid or malformed data.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall validate all real-time data inputs from external sources against predefined quality rules and reject invalid or malformed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-014
- 主题：Schedule Automatic Report Generation and Email Delivery → Email Delivery
- 审查问题：Given that the system allows users to schedule automatic report generation and email delivery, does it ensure that the scheduled report email is delivered to the designated recipients?
- 场景：A user schedules automatic report generation and email delivery. The system generates the report and triggers the email delivery process.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：When a user schedules automatic report generation and email delivery, the system shall deliver the scheduled report email to the designated recipients.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-015
- 主题：High-volume data display → De-cluttering features
- 审查问题：Does the system specification require that when the system is engaged in high-volume data display, it automatically activates de-cluttering features to reduce visual complexity?
- 场景：Consider a situation where the system is displaying a large amount of data, leading to visual complexity. The de-cluttering features are intended to reduce this complexity during high-volume data display.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：When high-volume data display occurs, the system shall activate de-cluttering features.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-016
- 主题：Maintain long-term archive of processed data → Publish processed data in standardized formats
- 审查问题：Does the system have an explicit obligation to use the maintained long-term archive of processed data as the source when publishing processed data in standardized formats?
- 场景：The system maintains a long-term archive of all processed data, but the publication process for standardized formats (SAE J2354, TMDD) could pull from a different data source, breaking the intended dependency between the archive and publication.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003, FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall publish processed data in standardized formats using data retrieved from the maintained long-term archive.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-017
- 主题：Support batch ingestion of historical data → Allow users to query archived data via SQL-based tools
- 审查问题：Does the batch ingestion of historical data, which backfills archives, ensure that the resulting archived data can be queried by users using SQL-based tools?
- 场景：The system supports batch ingestion of historical data for backfilling archives and training models. The system also maintains a long-term archive of all processed data. Users need to query archived data via SQL-based tools.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001, FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall ensure that historical data ingested in batch and stored in the long-term archive is accessible to users via SQL-based query tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-018
- 主题：Detect and classify incidents → Incident reports
- 审查问题：Does the system produce incident reports containing time, location, type, and severity for every incident it detects and classifies?
- 场景：An incident (e.g., crash, debris, stalled vehicle, work zone) is detected and classified. The system should generate an incident report with time, location, type, and severity.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall generate an incident report with time, location, type, and severity for each detected and classified incident.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-019
- 主题：Maintain long-term archive of processed data → Allow users to query archived data via SQL-based tools
- 审查问题：Is there an explicit functional requirement that the system maintain a long-term archive of all processed data to enable users to query archived data via SQL-based tools?
- 场景：A business user needs to retrieve historical processed data using SQL queries. The requirement source states: "maintain a long-term archive of all processed data" and "allow users to query archived data via SQL-based tools." The review checks whether the specification clearly links archive maintenance to query availability.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall maintain a long-term archive of processed data so that users can query archived data via SQL-based tools.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### DEP-020
- 主题：Input data fields → Normalized data stored in central database
- 审查问题：Does the specification require that the real-time data inputs identified as 'GPS data, speed, location, road condition reports, temperature, precipitation, visibility' be normalized and stored in the central database after acceptance?
- 场景：The system accepts real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems. The accepted data includes GPS data, speed, location, road condition reports, temperature, precipitation, and visibility. The system is expected to process these inputs and produce normalized data stored in a central database.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall normalize the accepted real-time data inputs and store the normalized data in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## isolated：16 条提名

### ISOLATED-08e7869ab193
- 主题：Compute traffic metrics
- 审查问题：Does FRBLOCK-001 need to specify that the accepted real-time data inputs (GPS data, speed, location) are used to compute traffic metrics, and if so, what are the expected outputs and storage locations?
- 场景：A traffic management operator needs to know current traffic conditions; the FR only specifies normalization and storage of raw inputs but does not mention computation of traffic metrics.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall compute traffic metrics (e.g., average speed, congestion level) from the accepted real-time data inputs and store them in the central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-cf62f7eafd00
- 主题：Configure new data source types without major software changes
- 审查问题：Does FRBLOCK-001 need to document how newly configured data source types are integrated into the existing validation and normalization pipeline?
- 场景：An administrator configures a new data source type; the FR states the system shall allow configuration without major software changes, but does not specify whether the new source's data will be validated and normalized automatically.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall automatically apply the existing validation rules and normalization processes to data from newly configured data source types.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-10080ec40edc
- 主题：Compute traffic metrics
- 审查问题：Is the Compute traffic metrics function explicitly linked to the raw sensor and probe data inputs in the system architecture? If not, should such a connection be specified?
- 场景：The FR block states that raw sensor and probe data are inputs, but the isolated elements list includes Compute traffic metrics, suggesting the graph lacks a connection between the data inputs and this function.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall document a data flow from raw sensor and probe data to the Compute traffic metrics function.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f6a0b89fce21
- 主题：Perform automated data quality checks
- 审查问题：Is the Perform automated data quality checks function connected to the data sources it is supposed to validate? If not, what connection is needed?
- 场景：The isolated elements list includes Perform automated data quality checks, but the FR block does not specify which data sources are checked or how this function is connected to them.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall document which data sources are checked and the connection between the data quality function and those sources.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-f836bf4bad01
- 主题：Implement dynamic caching for frequently accessed data
- 审查问题：The element 'Implement dynamic caching for frequently accessed data' is isolated in the system model. Is there a documented connection between dynamic caching and the long-term archive (for example, cache invalidation or data consistency when archived data changes)?
- 场景：The FR block specifies both long-term archiving and dynamic caching, but the caching element has no relationships in the graph. Understanding this linkage affects performance and data consistency.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall document the relationship between dynamic caching and archived data to ensure cache coherence with archival updates and purging.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-7dbcd685c067
- 主题：Compute traffic metrics
- 审查问题：Should the FR block include computation of traffic metrics as part of the processed data that is published in standardized formats?
- 场景：A reviewer sees that 'Compute traffic metrics' is an isolated element not connected to this FR. The FR mentions publishing processed data, which may rely on computed traffic metrics. The reviewer should confirm whether this computation is within scope.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall compute traffic metrics from raw traffic data before publishing processed data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4657b6b143e1
- 主题：Generate statistical summaries
- 审查问题：Should the FR block require generation of statistical summaries as part of the processed data provided to external applications?
- 场景：A reviewer notes that 'Generate statistical summaries' is isolated. The FR includes an API for external applications to consume traffic and weather data; statistical summaries might be required for those consumers. The reviewer should determine if this element belongs to the FR.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall generate statistical summaries of traffic and weather data for consumption via the API.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-751c7b7bc9cf
- 主题：Perform automated data quality checks
- 审查问题：Should the FR block specify automated data quality checks before publishing processed data?
- 场景：A reviewer sees that 'Perform automated data quality checks' is isolated. The FR requires publishing processed data in standardized formats; data quality checks may be necessary to ensure reliability. The reviewer should confirm if this element should be linked.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall perform automated data quality checks on all data before publication.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-16ff7a71c671
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Should the FR block include provision of ad-hoc reporting tools for users to create custom reports from available data?
- 场景：A reviewer notes that 'Provide Ad-hoc Reporting Tools' is isolated. The FR supports exporting data in multiple formats, which may be used for ad-hoc reporting, but the FR does not mention reporting tools. The reviewer should determine if reporting tools are in scope.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall provide ad-hoc reporting tools that allow users to create custom reports using exported data.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-ed55a19dbb49
- 主题：Compute traffic metrics
- 审查问题：Is 'Compute traffic metrics' intended to have a documented connection to the user interface requirements, given that the web-based interface is for viewing traffic data that may include computed metrics?
- 场景：A user viewing traffic data may need to see computed metrics such as average speed or congestion level, but the current FR block does not explicitly reference computation of these metrics.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：If business workflows require display of computed traffic metrics, the system shall connect the computation function to the UI viewing feature; otherwise, no connection is required.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-54d52a3f4eef
- 主题：Generate statistical summaries
- 审查问题：Does the FR block require the user interface to display statistical summaries generated by the system, or is 'Generate statistical summaries' intentionally isolated from the UI requirements?
- 场景：Users may benefit from viewing statistical summaries (e.g., incident frequency by region) through the web-based interface, but no explicit requirement connects the summary generation to UI display.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：If statistical summaries are to be presented to users, the system shall provide a documented connection between summary generation and the user interface.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-58ea01f90d0a
- 主题：Provide Ad-hoc Reporting Tools
- 审查问题：Is 'Provide Ad-hoc Reporting Tools' considered part of the user interface capabilities described in this FR block, or should it be connected to the custom dashboard and filtering features?
- 场景：Ad-hoc reporting tools may rely on the filtering/search and custom dashboard functionality, but the FR block does not mention ad-hoc reporting explicitly.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：If ad-hoc reporting is a business requirement, the system shall integrate or connect the ad-hoc reporting tools with the existing user interface features (filtering, dashboards).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-31a85cb7f56b
- 主题：Configure new data source types without major software changes
- 审查问题：Should the system's configuration capability for data sources include adding new data source types without requiring major software changes?
- 场景：The element 'Configure new data source types without major software changes' is currently isolated, but FR-SAC-001 implies data source configuration; if extensibility is required, it should be connected to this FR.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall allow administrators to configure new data source types without requiring major software changes.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-4aa6db0d1b97
- 主题：Compute traffic metrics
- 审查问题：Does the FR need to explicitly require the computation of traffic metrics (e.g., totals, averages) to support the pre-defined reports, or is this already implied by the requirement to generate pre-defined reports on traffic volume?
- 场景：A stakeholder expects traffic volume metrics such as average daily traffic and peak hour volume to be available in pre-defined reports, but the FR only mentions reports on traffic volume without specifying that metrics are computed.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：The system shall compute traffic metrics including total traffic volume, average daily traffic, and peak hour volume from collected traffic data to support pre-defined reports.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-d90489838037
- 主题：Perform automated data quality checks
- 审查问题：Should the FR specify automated data quality checks for the data underlying reports to ensure reliability of traffic volume, incident frequency, and road condition reports?
- 场景：Report consumers may act on inaccurate data if quality issues are not detected before report generation.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：The system shall perform automated data quality checks on traffic, incident, and road condition data prior to report generation, flagging missing, inconsistent, or outlier values.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### ISOLATED-10cccc3cb98a
- 主题：all users
- 审查问题：Is there a documented connection between 'all users' and the authentication mechanism that specifies user roles or attributes required for authorization?
- 场景：The system must distinguish between different user types for authorization; the definition of 'all users' may need clarity.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：0
- 草案：The system shall maintain a documented mapping of user roles and permissions for all users subject to authentication and authorization.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## operation：23 条提名

### OPERATION-b8927230c99b
- 主题：Perform automated data quality checks
- 审查问题：Does the FR's validation requirement (FR-DCI-002) imply automated data quality checks, and should it specify the frequency and scope of such checks?
- 场景：Data arrives in real time; the system validates against predefined quality rules, but the FR does not state whether these checks are automated or manual, leading to potential operational ambiguity.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall perform automated data quality checks on all incoming data in real time, using the predefined quality rules, and log all rejected records.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5d50ce8aef71
- 主题：Support batch ingestion of historical data
- 审查问题：Does FRBLOCK-001 need to clarify how batch ingestion of historical data coexists with real-time ingestion, specifically regarding validation and storage consistency?
- 场景：An operator loads historical data in batch; the FR requires the system to support batch ingestion but does not specify whether the same validation rules apply or whether historical data is stored in the same central database.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-001
- 全文已检查 FR 数：0
- 草案：The system shall apply the same data validation rules to batch-ingested historical data as to real-time data, and store the normalized results in the same central database.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-f1ab4f4db124
- 主题：Generate statistical summaries
- 审查问题：What specific operation allows users to retrieve or view the generated statistical summaries? Does the system provide a command or query interface for these summaries?
- 场景：The FR block states that the system shall generate statistical summaries of daily, weekly, and monthly traffic patterns, but does not specify how users access these summaries.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall provide an operation to retrieve the generated statistical summaries for a specified time period.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-14d1d5d79dac
- 主题：Detect and classify incidents
- 审查问题：What specific operation triggers the incident detection and classification process? Is it continuous, scheduled, or event-driven?
- 场景：The FR block requires incident detection and classification but does not define the operational trigger for this function.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-002
- 全文已检查 FR 数：0
- 草案：The system shall define a trigger for the incident detection and classification operation, such as real-time sensor streaming or periodic batch processing.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-6ea32fb03ed6
- 主题：Support automated data purging policies
- 审查问题：The FR specifies that the system shall support automated data purging policies, but does not mention an operation for administrators to define, modify, or review these policies. Should the system provide an operation to configure purging policies?
- 场景：In the data storage workflow, administrators likely need to adjust retention periods or purge schedules. The current FR only states support for automated policies, leaving configuration unspecified.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-003
- 全文已检查 FR 数：0
- 草案：The system shall allow authorized administrators to configure automated data purging policies, including defining retention periods and purge schedules.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-756d4068e4d4
- 主题：Generate alerts
- 审查问题：Should the system support updating the status of generated alerts (e.g., acknowledged, resolved)?
- 场景：The FR states that the system shall generate alerts. In typical operations, alerts need lifecycle management, including status updates. The reviewer should confirm if an update operation is required for alert handling.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall allow authorized users to update the status of generated alerts.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-1ae312a0ea92
- 主题：Support data export formats
- 审查问题：Should the system allow authorized users to update the configuration of data exports (e.g., selecting fields, schedule)?
- 场景：The FR requires exporting data in multiple formats, but does not specify if export configurations can be updated. A reviewer should verify whether an update operation is needed for export management.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-004
- 全文已检查 FR 数：0
- 草案：The system shall allow authorized users to update data export configurations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c3c92db3854a
- 主题：Web-based interface for viewing data
- 审查问题：Does the web-based interface support role-based access control, allowing different user types (e.g., public, operator, administrator) to view different subsets of traffic, incident, traveler, and weather data?
- 场景：An operator needs to view detailed incident data while a public user should only see high-level traffic information.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：The system shall enforce role-based access control for data visibility in the web-based interface.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-44b2daf510ec
- 主题：Map displays with icon layers
- 审查问题：Does the map display allow users to selectively show or hide individual icon layers (traffic, incidents, road closures) independently?
- 场景：A user wants to view only road closures on the map to assess impact on a route.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：The system shall provide controls to toggle visibility of each icon layer independently.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-d4fd447042c3
- 主题：De-cluttering features
- 审查问题：Does the de-cluttering operation automatically trigger based on data volume thresholds, or is it user-controlled?
- 场景：High-volume data display occurs and visual complexity needs reduction.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：Define the trigger mechanism for de-cluttering (automatic, user-controlled, or hybrid).
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-904a11a9521c
- 主题：Data filtering and search
- 审查问题：Can users combine multiple filter criteria (location, time, event type, and other relevant criteria) in a single search operation?
- 场景：A user wants to find all incidents of type 'accident' within a specific city and time window.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：The system shall support simultaneous application of multiple filter criteria in search and filter operations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-7b3ebbc2d440
- 主题：Multi-language UI support
- 审查问题：Does the multi-language UI support include dynamic language switching without requiring re-authentication or session restart?
- 场景：A user wants to switch the interface language mid-session to another supported language.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：The system shall allow users to change the UI language during an active session.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-661be28d3ef4
- 主题：Custom dashboards
- 审查问题：Can users persist, retrieve, and modify custom dashboards they have created for frequent data views?
- 场景：A user creates a custom dashboard, logs out, and expects to access it in a future session.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-005
- 全文已检查 FR 数：0
- 草案：The system shall provide persistence and retrieval capabilities for user-created custom dashboards.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-c8c070ad70d7
- 主题：Backup and Restore Capabilities
- 审查问题：Is there a documented operation for an administrator to initiate a backup or restore of the database or configuration settings?
- 场景：An administrator needs to restore the database after a failure, but the FR only states that backup and restore capabilities are provided; it does not specify how the operation is triggered or who can perform it.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall allow authorized administrators to initiate backup and restore operations for the database and configuration settings.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-afbc5bdda727
- 主题：Role-Based Access Control
- 审查问题：Is there a specific operation to manage user roles or permissions?
- 场景：The FR states support for role-based access control for different user types, but does not define how roles are assigned, modified, or revoked, which is necessary for administration.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall allow administrators to manage user roles and their associated permissions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9b55bad64875
- 主题：Configure Data Sources, Algorithms, and Output Formats
- 审查问题：Is there a documented workflow for an administrator to manage the configuration of data sources, algorithms, or output formats?
- 场景：The FR allows administrators to configure these items, but it does not specify the operations for managing configurations, which could lead to ambiguous implementation.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall provide administrative operations to manage configurations for data sources, algorithms, and output formats.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-dd8253608df5
- 主题：Log Administrative Actions and Errors
- 审查问题：Is there a specific operation for viewing or exporting the administrative action and error logs?
- 场景：Logs are generated, but the FR does not specify how authorized users can access or analyze these logs for audit and troubleshooting.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-006
- 全文已检查 FR 数：0
- 草案：The system shall provide authorized users with the ability to view, filter, and export administrative action and error logs.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-70f1cd2d84f4
- 主题：Schedule Automatic Report Generation and Email Delivery
- 审查问题：Should the system also allow users to cancel or modify a scheduled report generation and email delivery, given that users can schedule them?
- 场景：A user schedules a weekly report but later needs to change the schedule or stop it; the current FR only mentions scheduling, not modification or cancellation.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：The system shall allow users to cancel or modify a scheduled report generation and email delivery.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-474aea440227
- 主题：Generate Pre-defined Reports
- 审查问题：Should the system allow authorized users to manually trigger generation of a pre-defined report on demand, in addition to scheduled generation?
- 场景：A user needs an immediate traffic volume report outside the scheduled time, but the FR only specifies that the system shall generate pre-defined reports without specifying user-initiated generation.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-007
- 全文已检查 FR 数：0
- 草案：The system shall allow authorized users to manually run a pre-defined report on demand.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-23b92139c078
- 主题：Enforce secure authentication and authorization
- 审查问题：Does the system implement a specific operation to authenticate users (e.g., login) before granting access to protected resources?
- 场景：A user attempts to access a restricted feature; the system must verify identity and permissions.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：0
- 草案：The system shall include a user authentication operation that verifies credentials and an authorization operation that checks permissions before allowing access.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5dca9d7b8c55
- 主题：TLS 1.2+ encryption for data transmissions
- 审查问题：Are all data transmissions, including internal service-to-service communication, covered by the TLS 1.2+ encryption requirement?
- 场景：The system exchanges data between modules; all paths must be encrypted.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：0
- 草案：The system shall apply TLS 1.2 or higher to every data transmission channel without exceptions.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-9d9e04802881
- 主题：Compliance with MDIT and FIPS 140-2
- 审查问题：What specific operations or configurations are necessary to demonstrate compliance with FIPS 140-2 encryption requirements (e.g., algorithm selection, key management)?
- 场景：The system uses cryptographic modules; they must be FIPS 140-2 validated.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：0
- 草案：The system shall use FIPS 140-2 validated cryptographic modules for all encryption and key management operations.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

### OPERATION-5fcb1f0efed4
- 主题：Audit logging of user activities and system events
- 审查问题：Does the audit logging functionality capture both successful and failed authentication attempts as part of user activities?
- 场景：A user attempts to log in; the event should be recorded regardless of outcome.
- 模型初步去向：not_checked
- 模型解释：Full-document validation disabled in this ablation.
- 原文证据 FR：FRBLOCK-008
- 全文已检查 FR 数：0
- 草案：The system shall log all authentication attempts, including failures, with relevant metadata.
- 人工判定：＿＿＿＿＿＿
- 人工义务编号：＿＿＿＿＿＿
- 人工备注：＿＿＿＿＿＿

## 本次输出的补充需求

1. [unchecked_draft] The system shall provide SQL-based query tools that can directly query data stored in the Oracle 10G archive.

2. [unchecked_draft] The system shall provide batch-ingested historical data to the machine learning models used for predictive analysis of traffic trends and incident likelihood, so that the models can be trained.

3. [unchecked_draft] The system shall normalize and store in the central database all real-time data inputs it accepts from external sources.

4. [unchecked_draft] The system shall generate the pre-defined reports when automatic report generation is scheduled.

5. [unchecked_draft] The system shall support the defined automated data purging policies for managing storage limits.

6. [unchecked_draft] The system shall provide the capability to publish processed data from the Oracle 10G archive in the standardized formats.

7. [unchecked_draft] The system shall validate GPS data, speed, location, road condition reports, temperature, precipitation, and visibility against predefined quality rules and reject invalid or malformed values for each field.

8. [unchecked_draft] The system shall ensure that historical data ingested via batch processing is processed and published in the standardized formats required by the target requirement.

9. [unchecked_draft] The system shall ensure that all listed input data fields (GPS data, speed, location, road condition reports, temperature, precipitation, and visibility) are accepted and made available for processing by the system.

10. [unchecked_draft] The system shall maintain a long-term archive of all processed data, including data ingested via batch processes.

11. [unchecked_draft] The system shall use Oracle 10G for archiving processed data to maintain a long-term archive of all processed data.

12. [unchecked_draft] The system shall log every administrative action where an administrator configures data sources, algorithms, or output formats, in accordance with the requirement to log all administrative actions and errors.

13. [unchecked_draft] The system shall validate all real-time data inputs from external sources against predefined quality rules and reject invalid or malformed data.

14. [unchecked_draft] When a user schedules automatic report generation and email delivery, the system shall deliver the scheduled report email to the designated recipients.

15. [unchecked_draft] When high-volume data display occurs, the system shall activate de-cluttering features.

16. [unchecked_draft] The system shall publish processed data in standardized formats using data retrieved from the maintained long-term archive.

17. [unchecked_draft] The system shall ensure that historical data ingested in batch and stored in the long-term archive is accessible to users via SQL-based query tools.

18. [unchecked_draft] The system shall generate an incident report with time, location, type, and severity for each detected and classified incident.

19. [unchecked_draft] The system shall maintain a long-term archive of processed data so that users can query archived data via SQL-based tools.

20. [unchecked_draft] The system shall normalize the accepted real-time data inputs and store the normalized data in the central database.

21. [unchecked_draft] The system shall compute traffic metrics (e.g., average speed, congestion level) from the accepted real-time data inputs and store them in the central database.

22. [unchecked_draft] The system shall automatically apply the existing validation rules and normalization processes to data from newly configured data source types.

23. [unchecked_draft] The system shall perform automated data quality checks on all incoming data in real time, using the predefined quality rules, and log all rejected records.

24. [unchecked_draft] The system shall apply the same data validation rules to batch-ingested historical data as to real-time data, and store the normalized results in the same central database.

25. [unchecked_draft] The system shall document a data flow from raw sensor and probe data to the Compute traffic metrics function.

26. [unchecked_draft] The system shall provide an operation to retrieve the generated statistical summaries for a specified time period.

27. [unchecked_draft] The system shall define a trigger for the incident detection and classification operation, such as real-time sensor streaming or periodic batch processing.

28. [unchecked_draft] The system shall document which data sources are checked and the connection between the data quality function and those sources.

29. [unchecked_draft] The system shall document the relationship between dynamic caching and archived data to ensure cache coherence with archival updates and purging.

30. [unchecked_draft] The system shall allow authorized administrators to configure automated data purging policies, including defining retention periods and purge schedules.

31. [unchecked_draft] The system shall compute traffic metrics from raw traffic data before publishing processed data.

32. [unchecked_draft] The system shall generate statistical summaries of traffic and weather data for consumption via the API.

33. [unchecked_draft] The system shall perform automated data quality checks on all data before publication.

34. [unchecked_draft] The system shall provide ad-hoc reporting tools that allow users to create custom reports using exported data.

35. [unchecked_draft] The system shall allow authorized users to update the status of generated alerts.

36. [unchecked_draft] The system shall allow authorized users to update data export configurations.

37. [unchecked_draft] If business workflows require display of computed traffic metrics, the system shall connect the computation function to the UI viewing feature; otherwise, no connection is required.

38. [unchecked_draft] If statistical summaries are to be presented to users, the system shall provide a documented connection between summary generation and the user interface.

39. [unchecked_draft] If ad-hoc reporting is a business requirement, the system shall integrate or connect the ad-hoc reporting tools with the existing user interface features (filtering, dashboards).

40. [unchecked_draft] The system shall enforce role-based access control for data visibility in the web-based interface.

41. [unchecked_draft] The system shall provide controls to toggle visibility of each icon layer independently.

42. [unchecked_draft] Define the trigger mechanism for de-cluttering (automatic, user-controlled, or hybrid).

43. [unchecked_draft] The system shall support simultaneous application of multiple filter criteria in search and filter operations.

44. [unchecked_draft] The system shall allow users to change the UI language during an active session.

45. [unchecked_draft] The system shall provide persistence and retrieval capabilities for user-created custom dashboards.

46. [unchecked_draft] The system shall allow authorized administrators to initiate backup and restore operations for the database and configuration settings.

47. [unchecked_draft] The system shall allow administrators to manage user roles and their associated permissions.

48. [unchecked_draft] The system shall provide administrative operations to manage configurations for data sources, algorithms, and output formats.

49. [unchecked_draft] The system shall provide authorized users with the ability to view, filter, and export administrative action and error logs.

50. [unchecked_draft] The system shall allow administrators to configure new data source types without requiring major software changes.

51. [unchecked_draft] The system shall compute traffic metrics including total traffic volume, average daily traffic, and peak hour volume from collected traffic data to support pre-defined reports.

52. [unchecked_draft] The system shall perform automated data quality checks on traffic, incident, and road condition data prior to report generation, flagging missing, inconsistent, or outlier values.

53. [unchecked_draft] The system shall allow users to cancel or modify a scheduled report generation and email delivery.

54. [unchecked_draft] The system shall allow authorized users to manually run a pre-defined report on demand.

55. [unchecked_draft] The system shall include a user authentication operation that verifies credentials and an authorization operation that checks permissions before allowing access.

56. [unchecked_draft] The system shall apply TLS 1.2 or higher to every data transmission channel without exceptions.

57. [unchecked_draft] The system shall use FIPS 140-2 validated cryptographic modules for all encryption and key management operations.

58. [unchecked_draft] The system shall log all authentication attempts, including failures, with relevant metadata.

59. [unchecked_draft] The system shall maintain a documented mapping of user roles and permissions for all users subject to authentication and authorization.
