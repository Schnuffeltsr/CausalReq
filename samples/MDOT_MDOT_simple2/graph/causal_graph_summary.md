# Causal graph export — MDOT_MDOT_simple2

- model version: `MODEL-a988258ceab9`
- elements: 50 | extracted relations: 56
- evidence graph: 50 nodes, 56 edges (multi-edge, keeps every quotations)
- signed simulation graph: 45 nodes, 14 edges
- excluded from simulation: 30
- parameters: background log-odds -1.0, propagation strength 2.5, max parents 8

## Simulation edges

| source | → | target | sign | weight |
|---|---|---|---:|---:|
| Detect and classify incidents | → | Incident reports | positive | 0.95 |
| Accept real-time data inputs from external sources | → | Normalized data stored in central database | positive | 0.90 |
| Automated data purging policies | → | Support automated data purging policies | positive | 0.90 |
| High-volume data display | → | De-cluttering features | positive | 0.90 |
| Maintain long-term archive of processed data | → | Allow users to query archived data via SQL-based tools | positive | 0.90 |
| Schedule Automatic Report Generation and Email Delivery | → | Email Delivery | positive | 0.90 |
| Use Oracle 10G for archiving | → | Maintain long-term archive of processed data | positive | 0.90 |
| Schedule Automatic Report Generation and Email Delivery | → | Generate Pre-defined Reports | positive | 0.85 |
| Configure Data Sources, Algorithms, and Output Formats | → | Log Administrative Actions and Errors | positive | 0.80 |
| Input data fields | → | Accept real-time data inputs from external sources | positive | 0.80 |
| Support batch ingestion of historical data | → | Maintain long-term archive of processed data | positive | 0.75 |
| Support batch ingestion of historical data | → | Support machine learning models | positive | 0.75 |
| Accept real-time data inputs from external sources | → | Validate incoming data and reject invalid data | positive | 0.70 |
| Maintain long-term archive of processed data | → | Publish processed data in standardized formats | positive | 0.60 |

## Exclusions

| source | target | reason |
|---|---|---|
| System | De-cluttering features | undefined_activation_state |
| System | Web-based interface for viewing data | undefined_activation_state |
| System | Audit logging of user activities and system events | undefined_activation_state |
| System | Backup and Restore Capabilities | undefined_activation_state |
| System | Compliance with MDIT and FIPS 140-2 | undefined_activation_state |
| System | Configure Data Sources, Algorithms, and Output Formats | undefined_activation_state |
| System | Custom dashboards | undefined_activation_state |
| System | Enforce secure authentication and authorization | undefined_activation_state |
| System | Generate alerts | undefined_activation_state |
| System | Log Administrative Actions and Errors | undefined_activation_state |
| System | Multi-language UI support | undefined_activation_state |
| System | Provide API for real-time consumption | undefined_activation_state |
| System | Provide real-time data feeds to MI Drive | undefined_activation_state |
| System | Publish processed data in standardized formats | undefined_activation_state |
| System | Role-Based Access Control | undefined_activation_state |
| System | Support data export formats | undefined_activation_state |
| System | TLS 1.2+ encryption for data transmissions | undefined_activation_state |
| User | Schedule Automatic Report Generation and Email Delivery | undefined_activation_state |
| Users | Schedule Automatic Report Generation and Email Delivery | undefined_activation_state |
| Web-based interface for viewing data | Map displays with icon layers | unspecified_sign |
| Predefined quality rules | Validate incoming data and reject invalid data | unspecified_sign |
| Probe vehicles, traffic sensors, weather stations, and traveler information systems | Accept real-time data inputs from external sources | undefined_activation_state |
| Probe vehicles, traffic sensors, weather stations, and traveler information systems | Input data fields | undefined_activation_state |
| Report Export Formats | Generate Pre-defined Reports | unspecified_sign |
| Role-Based Access Control | Configure Data Sources, Algorithms, and Output Formats | unspecified_sign |
| Web-based interface for viewing data | Custom dashboards | unspecified_sign |
| Web-based interface for viewing data | Data filtering and search | unspecified_sign |
| Web-based interface for viewing data | Multi-language UI support | unspecified_sign |
| Accept real-time data inputs from external sources | Detect and classify incidents | unspecified_sign |
| Accept real-time data inputs from external sources | Calculate road surface conditions | unspecified_sign |

## Fixed RQ2 pool (top 10 by |ACE|)

| candidate | source | target | ACE | p(do=1) | p(do=0) | reachability |
|---|---|---|---:|---:|---:|---:|
| DEP-018 | Detect and classify incidents | Incident reports | 0.529 | 0.798 | 0.269 | 1 |
| DEP-003 | Accept real-time data inputs from external sources | Normalized data stored in central database | 0.508 | 0.777 | 0.269 | 2 |
| DEP-005 | Automated data purging policies | Support automated data purging policies | 0.508 | 0.777 | 0.269 | 1 |
| DEP-014 | Schedule Automatic Report Generation and Email Delivery | Email Delivery | 0.508 | 0.777 | 0.269 | 2 |
| DEP-015 | High-volume data display | De-cluttering features | 0.508 | 0.777 | 0.269 | 1 |
| DEP-019 | Maintain long-term archive of processed data | Allow users to query archived data via SQL-based tools | 0.508 | 0.777 | 0.269 | 2 |
| DEP-004 | Schedule Automatic Report Generation and Email Delivery | Generate Pre-defined Reports | 0.486 | 0.755 | 0.269 | 2 |
| DEP-009 | Input data fields | Accept real-time data inputs from external sources | 0.462 | 0.731 | 0.269 | 3 |
| DEP-012 | Configure Data Sources, Algorithms, and Output Formats | Log Administrative Actions and Errors | 0.462 | 0.731 | 0.269 | 1 |
| DEP-011 | Use Oracle 10G for archiving | Maintain long-term archive of processed data | 0.439 | 0.826 | 0.386 | 3 |