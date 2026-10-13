# RQ1 人工审查材料：MDOT_MDOT_simple2

本文件只包含原始需求与 CausalReq 生成的新增需求；不包含任何基线输出，也没有自动质量评分。

## 原始需求

Functional Requirement
2. Functional Requirements
2.1 Data Collection and Ingestion
FR-DCI-001: The system shall accept real-time data inputs from probe vehicles, traffic sensors, weather stations, and traveler information systems.

Inputs: GPS data, speed, location, road condition reports, temperature, precipitation, visibility.
Outputs: Normalized data stored in a central database.
FR-DCI-002: The system shall validate incoming data against predefined quality rules and reject invalid or malformed data.

FR-DCI-003: The system shall allow for the configuration of new data source types without requiring major software changes.

FR-DCI-004: The system shall support batch ingestion of historical data for backfilling archives and training models.

2.2 Data Processing and Analysis
FR-DPA-001: The system shall compute traffic metrics including congestion levels, travel times, queue lengths, and traffic flow patterns.

FR-DPA-002: The system shall detect and classify incidents such as crashes, debris, stalled vehicles, and work zones.

Inputs: Raw sensor and probe data.
Outputs: Incident reports with time, location, type, and severity.
FR-DPA-003: The system shall calculate road surface conditions based on weather data and sensor inputs.

FR-DPA-004: The system shall perform automated data quality checks to flag anomalies and inconsistencies.

FR-DPA-005: The system shall support machine learning models for predictive analysis of traffic trends and incident likelihood.

FR-DPA-006: The system shall generate statistical summaries of daily, weekly, and monthly traffic patterns.

2.3 Data Storage and Archiving
FR-DSA-001: The system shall maintain a long-term archive of all processed data using Oracle 10G.

FR-DSA-002: The system shall implement dynamic caching for frequently accessed data to improve performance.

FR-DSA-003: The system shall allow users to query archived data via SQL-based tools.

FR-DSA-004: The system shall support automated data purging policies to manage storage limits.

2.4 Data Publication and Output
FR-DPO-001: The system shall publish processed data in standardized formats (SAE J2354, TMDD).

FR-DPO-002: The system shall provide real-time data feeds to MDOT’s MI Drive system.

FR-DPO-003: The system shall generate alerts for traffic incidents, severe weather events, and asset failures.

FR-DPO-004: The system shall support exporting data in CSV, JSON, XML, and KML formats for third-party use.

FR-DPO-005: The system shall provide an API for external applications to consume traffic and weather data in real time.

2.5 User Interface and Presentation
FR-UIP-001: The system shall provide a web-based interface for viewing traffic, incident, traveler, and weather data.

FR-UIP-002: The interface shall include map displays with icon layers representing traffic, incidents, and road closures.

FR-UIP-003: The system shall support de-cluttering features to reduce visual complexity during high-volume data display.

FR-UIP-004: Users shall be able to filter and search data by location, time, event type, and other relevant criteria.

FR-UIP-005: The system shall support multi-language UI options to accommodate diverse user groups.

FR-UIP-006: The system shall allow users to create custom dashboards for frequent data views.

2.6 System Administration and Configuration
FR-SAC-001: The system shall allow administrators to configure data sources, algorithms, and output formats.

FR-SAC-002: The system shall log all administrative actions and errors for audit and troubleshooting purposes.

FR-SAC-003: The system shall support role-based access control for different user types (e.g., field operator, analyst, admin).

FR-SAC-004: The system shall provide backup and restore capabilities for the database and configuration settings.

2.7 Reporting and Analytics
FR-REP-001: The system shall generate pre-defined reports on traffic volume, incident frequency, and road condition trends.

FR-REP-002: The system shall allow users to schedule automatic report generation and email delivery.

FR-REP-003: The system shall provide ad-hoc reporting tools for querying and visualizing data.

FR-REP-004: Reports must be exportable in PDF, Excel, and HTML formats.
2.8 Security and Compliance
FR-SEC-001: The system shall enforce secure authentication and authorization for all users.

FR-SEC-002: All data transmissions must be encrypted using TLS 1.2 or higher.

FR-SEC-003: The system shall comply with MDIT security standards and FIPS 140-2 encryption requirements.

FR-SEC-004: The system shall support audit logging of all user activities and system events.

---

## CausalReq：仅新增需求

1. The system shall ensure that batch-ingested historical data is available and accessible to the machine learning model training process to support predictive analysis of traffic trends and incident likelihood.

2. The system shall generate the pre-defined reports on traffic volume, incident frequency, and road condition trends whenever a user schedules automatic report generation and email delivery.

3. The system shall ensure that processed data originating from batch ingestion of historical data is stored in the long-term archive and is subsequently published in the standardized formats (e.g., SAE J2354, TMDD).

4. The system shall maintain the long-term archive of all processed data without being solely dependent on Oracle 10G, ensuring continuity of archival operations.

5. The system shall deliver the scheduled report email to the designated recipients when the scheduled automatic report generation and email delivery is triggered.

6. The system shall ensure that historical data ingested in batch for archive backfill is stored in the long-term archive and made available for user queries through SQL-based tools.

7. The system shall perform automated data quality checks on stored normalized data in addition to ingestion-time validation to detect anomalies or inconsistencies not identified during ingestion.

8. The system shall have access to historical traffic data sufficient to generate the required statistical summaries.

9. The system shall allow authorized users to update or reclassify a detected incident under defined conditions, including the roles and permissions required for such updates.

10. The system shall provide mechanisms to retrain and update machine learning models when performance degrades or new data becomes available.

11. The system shall execute automated data purging only after the applicable retention period has elapsed, according to configurable retention policies, and shall record audit logs identifying the data purged, the policy applied, and the timestamp of deletion.

12. The system shall invalidate cached data entries when corresponding archived data is purged.

13. The system shall compute traffic metrics to support the detection of traffic incidents and the generation of traffic incident alerts.

14. The system shall export generated statistical summaries in CSV, JSON, XML, and KML formats for third-party use.

15. The system shall perform automated data quality checks on processed data prior to publication in standardized formats.

16. The system shall provide ad-hoc reporting tools that allow third-party users to create custom reports using exported data.

17. The system shall define user roles and access permissions for data publication, real-time feeds, alerts, and export capabilities to ensure that authorized users, including third-party users and external applications, have appropriate access while preventing unauthorized access.

18. The system shall define and implement a delivery mechanism for real-time data feeds to MI Drive, specifying whether it is push-based or pull-based.

19. The system shall support role-based access control for all user categories, including a default 'all users' role if such a role is defined, ensuring that permissions for that role are specified and enforced.

20. The system shall allow administrators to view, filter, and export audit log entries (including administrative actions and errors) for audit and troubleshooting purposes.

21. The system shall provide administrative operations to create, modify, and assign user roles and permissions.

22. The system shall allow administrators to schedule automatic backups and perform partial restores of database and configuration settings (e.g., restore only configuration settings without affecting the database).

23. The system shall allow users to specify and update the email recipients for scheduled automatic report delivery.

24. The system shall provide an operation to revoke a user's authentication and authorization.

25. The system shall provide authorized users with the ability to view and search audit logs.

26. The system shall provide authorized users with the ability to generate compliance reports demonstrating adherence to MDIT security standards and FIPS 140-2 encryption requirements.

27. The system shall specify the user roles (e.g., field operator, analyst, administrator) that constitute 'all users' for security requirements to ensure consistent application.
