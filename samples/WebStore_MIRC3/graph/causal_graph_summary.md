# Causal graph export — WebStore_MIRC3

- model version: `MODEL-ed936aeafef8`
- elements: 140 | extracted relations: 387
- evidence graph: 140 nodes, 387 edges (multi-edge, keeps every quotations)
- signed simulation graph: 118 nodes, 92 edges
- excluded from simulation: 109
- parameters: background log-odds -1.0, propagation strength 2.5, max parents 8

## Simulation edges

| source | → | target | sign | weight |
|---|---|---|---:|---:|
| Checkout Function | → | Checkout Event Recorded | positive | 0.95 |
| Checkout Function | → | Order Confirmation Email Sent | positive | 0.95 |
| Checkout Function | → | Order Created | positive | 0.95 |
| Checkout Function | → | Payment Processed | positive | 0.95 |
| Compliance Check Initiation | → | User Interface Specification Compliance Checking Function | positive | 0.95 |
| Customer Logout Function | → | Logout Event | positive | 0.95 |
| Customer Logout Function | → | Session Terminated | positive | 0.95 |
| Inventory Management Function | → | Inventory Quantity Update | positive | 0.95 |
| Manage Personal Information | → | Personal Information Data Entity | positive | 0.95 |
| Manage Personal Information | → | Viewing or Update Event | positive | 0.95 |
| Manage User Interface Specification Function | → | Management Event Recorded | positive | 0.95 |
| Manage User Interface Specification Function | → | System Interface Modified | positive | 0.95 |
| Manage User Interface Specification Function | → | User Interface Specification data entity | positive | 0.95 |
| Order Cancellation | → | Cancelled Order Status | positive | 0.95 |
| Payment Processing | → | Order Data Entity | positive | 0.95 |
| Payment Processing | → | Successful Payment | positive | 0.95 |
| Personal Information Update | → | Personal Information Updated | positive | 0.95 |
| Personal Information Update | → | Update Event Recorded | positive | 0.95 |
| Plugin Development Function | → | Plugin Data | positive | 0.95 |
| Product Categorization Function | → | Category Update Logged | positive | 0.95 |
| Product Categorization Function | → | Product Assigned to Selected Category | positive | 0.95 |
| Product Removal Function | → | Product Removal Recorded | positive | 0.95 |
| Purchase History Viewing Function | → | Purchase History Displayed | positive | 0.95 |
| Shopping Cart Creation Function | → | Confirmation Message Shown | positive | 0.95 |
| Shopping Cart Creation Function | → | Inventory Quantity Updated | positive | 0.95 |
| Shopping Cart Creation Function | → | Product Added to Shopping Cart | positive | 0.95 |
| Shopping Cart Modification Function | → | Inventory Adjustment | positive | 0.95 |
| Update Product Information | → | Update Event | positive | 0.95 |
| User Interface Specification Compliance Checking Function | → | Compliance Report | positive | 0.95 |
| Add to Cart | → | Shopping Cart Creation Function | positive | 0.90 |
| Cart Items | → | Checkout Function | positive | 0.90 |
| Configure Plugin Settings | → | Configuration Event | positive | 0.90 |
| Configure Plugin Settings | → | Plugin Data Entity | positive | 0.90 |
| Configure Plugin Settings | → | System Interface Reflects Updated Settings | positive | 0.90 |
| Customer Login Function | → | Authenticated | positive | 0.90 |
| Customer Login Function | → | Login Event | positive | 0.90 |
| Customer Login Function | → | Personalized Dashboard | positive | 0.90 |
| Customer Registration Function | → | Customer Account Created | positive | 0.90 |
| Inventory Management Function | → | Inventory Levels Stored | positive | 0.90 |
| Inventory Management Function | → | Management Event Recording | positive | 0.90 |
| Inventory Management Function | → | Purchase History Recorded | positive | 0.90 |
| Manage Category Function | → | Management Event Recorded | positive | 0.90 |
| Manage Category Function | → | Product Associations | positive | 0.90 |
| Manage Category Function | → | Validate Category | positive | 0.90 |
| Manage EmailRecord | → | Confirmation Message Displayed | positive | 0.90 |
| Manage EmailRecord | → | EmailRecord Data Entity | positive | 0.90 |
| Manage OrderItem | → | Inventory Levels | positive | 0.90 |
| Manage OrderItem | → | Order Item Status Update | positive | 0.90 |
| Manage Personal Information | → | Validate Personal Information Changes | positive | 0.90 |
| Order | → | Order Confirmation Email Sending Function | positive | 0.90 |
| Order Cancellation | → | Cancellation Event Recorded | positive | 0.90 |
| Order Cancellation | → | Inventory Levels | positive | 0.90 |
| Order Confirmation Email Sending Function | → | Confirmation Event | positive | 0.90 |
| Order Confirmation Email Sending Function | → | Order Confirmation Email Sent | positive | 0.90 |
| Order Created | → | Order Data Entity | positive | 0.90 |
| Payment Processing | → | Inventory Levels | positive | 0.90 |
| Payment Processing | → | Payment Event | positive | 0.90 |
| Personal Information Update | → | Personal Information Data Entity | positive | 0.90 |
| Personal Information Update | → | Validate Updated Information (FUNCTION) | positive | 0.90 |
| Plugin Development Event | → | Purchase History Data | positive | 0.90 |
| Plugin Development Function | → | Plugin Activated State | positive | 0.90 |
| Plugin Development Function | → | Plugin Development Event | positive | 0.90 |
| Plugin Development Function | → | System Interface Updated | positive | 0.90 |
| Product Addition Function | → | Addition Event | positive | 0.90 |
| Product Addition Function | → | Product Data Entity | positive | 0.90 |
| Product Categorization Function | → | Category Validation | positive | 0.90 |
| Shopping Cart Viewing Function | → | Cart Summary Displayed | positive | 0.90 |
| Successful Checkout | → | Order Confirmation Email Sending Function | positive | 0.90 |
| Update Product Information | → | Inventory and Category Updated | positive | 0.90 |
| Updated Product Information Fields | → | Update Product Information | positive | 0.90 |
| User Interface Specification Compliance Checking Function | → | Non-compliant Element Highlight | positive | 0.90 |
| Valid Registration Information | → | Customer Registration Function | positive | 0.90 |
| View CartItem Function | → | Cart Item Details Displayed | positive | 0.90 |
| View CartItem Function | → | Viewing Event | positive | 0.90 |
| View EmailRecord Function | → | Viewing Event | positive | 0.90 |
| View Payment Function | → | Payment Viewing Event | positive | 0.90 |
| Cart Items | → | Shopping Cart Viewing Function | positive | 0.85 |
| Category Validation | → | Product Assigned to Selected Category | positive | 0.85 |
| Check Product Availability | → | Product Added to Shopping Cart | positive | 0.85 |
| Check Product Availability | → | Shopping Cart Creation Function | positive | 0.85 |
| Inventory Quantity Update | → | Inventory Levels Stored | positive | 0.85 |
| Manage EmailRecord | → | Email Record Management Event | positive | 0.85 |
| Management Event Recording | → | Purchase History Recorded | positive | 0.85 |
| Plugin Development Function | → | Purchase History Data | positive | 0.85 |
| Plugin Validation Constraint | → | Plugin Activated State | positive | 0.85 |
| Product Addition Function | → | Product Assigned to Selected Category | positive | 0.85 |
| Validate Personal Information Changes | → | Personal Information Data Entity | positive | 0.85 |
| Validate Updated Information (CONSTRAINT) | → | Contact Information data entity | positive | 0.85 |
| Validate Updated Information (FUNCTION) | → | Personal Information Data Entity | positive | 0.85 |
| Validate Updated Information (FUNCTION) | → | Personal Information Updated | positive | 0.85 |
| Eligible Order Status | → | Order Cancellation | positive | 0.80 |
| Validate Updated Information (CONSTRAINT) | → | Contact Information Stored | positive | 0.80 |

## Exclusions

| source | target | reason |
|---|---|---|
| Checkout Function | Inventory Updated | undefined_activation_state |
| Login Event | Purchase History data entity | undefined_activation_state |
| Manage Contact Information | Contact Information data entity | undefined_activation_state |
| Order Confirmation Email Sending Function | EmailRecord | undefined_activation_state |
| Payment Processing | Payment Data Entity | undefined_activation_state |
| Product Addition Function | Inventory Updated | undefined_activation_state |
| Product Addition Function | Product | undefined_activation_state |
| Product Removal Function | Product | undefined_activation_state |
| Shopping Cart Modification Function | CartItem | unspecified_sign |
| Shopping Cart Modification Function | Shopping Cart | undefined_activation_state |
| Update Product Information | Product Data Entity | unspecified_sign |
| Viewing or Update Event | Purchase History data entity | undefined_activation_state |
| Addition Event | Purchase History data entity | undefined_activation_state |
| Administrator | Compliance Check Initiation | undefined_activation_state |
| Administrator | Plugin Development Function | undefined_activation_state |
| Administrator | Product Addition Function | undefined_activation_state |
| Administrator | Product Categorization Function | undefined_activation_state |
| Administrators | Manage Customer Function | undefined_activation_state |
| Administrators | Manage User Interface Specification Function | undefined_activation_state |
| Administrators | Product Removal Function | undefined_activation_state |
| Administrators | Update Product Information | undefined_activation_state |
| CartItem Data Entity | Cart Item Details Displayed | undefined_activation_state |
| CartItem Data Entity | View CartItem Function | undefined_activation_state |
| Configuration Event | Purchase History data entity | undefined_activation_state |
| Confirmation Event | Purchase History data entity | undefined_activation_state |
| Contact Information Update Event | Purchase History data entity | undefined_activation_state |
| Customer | Customer Logout Function | undefined_activation_state |
| Customer | Personal Information Update | undefined_activation_state |
| Customer Logout Function | Purchase History data entity | undefined_activation_state |
| Customer Registration Function | Confirmation Email Sent | undefined_activation_state |
| Customers | Customer Logout Function | undefined_activation_state |
| Customers | Manage Contact Information | undefined_activation_state |
| Customers | Personal Information Update | undefined_activation_state |
| Customers | Shopping Cart Modification Function | undefined_activation_state |
| Customers | Shopping Cart Viewing Function | undefined_activation_state |
| Email Record Management Event | Purchase History data entity | undefined_activation_state |
| EmailRecord Data Entity | View EmailRecord Function | unspecified_sign |
| Manage Administrator Function | Contact Information | undefined_activation_state |
| Manage Administrator Function | Personal Information | undefined_activation_state |
| Manage Administrator Function | Purchase History data entity | undefined_activation_state |
| Manage CartItem Function | CartItem Data Entity | undefined_activation_state |
| Manage CartItem Function | Inventory Adjustment | unspecified_sign |
| Manage Category Function | Category Data Entity | undefined_activation_state |
| Manage Category Function | Management Event | undefined_activation_state |
| Manage Category Function | Purchase History data entity | undefined_activation_state |
| Manage Contact Information | Contact Information Stored | undefined_activation_state |
| Manage Contact Information | Contact Information Update Event | undefined_activation_state |
| Manage Contact Information | Validate Updated Information (CONSTRAINT) | undefined_activation_state |
| Manage Contact Information | Viewing or Update Event | undefined_activation_state |
| Manage Customer Function | Contact Information | undefined_activation_state |
| Manage Customer Function | Personal Information | undefined_activation_state |
| Manage Customer Function | Purchase History data entity | undefined_activation_state |
| Manage OrderItem | OrderItem | unspecified_sign |
| Manage OrderItem | Purchase History data entity | undefined_activation_state |
| Manage Personal Information | Purchase History data entity | undefined_activation_state |
| Manage User Interface Specification Function | Purchase History data entity | undefined_activation_state |
| Management Event Recorded | Purchase History data entity | undefined_activation_state |
| Order Data Entity | Order Confirmation Email Sending Function | unspecified_sign |
| Payment Data Entity | View Payment Function | undefined_activation_state |
| Payment Processed | Payment Data Entity | undefined_activation_state |
| Payment Processing | Inventory Updated | undefined_activation_state |
| Payment Processing | Purchase History data entity | undefined_activation_state |
| Personal Information Update | Confirmation Email Sent | undefined_activation_state |
| Product Addition Function | Inventory | undefined_activation_state |
| Product Removal Function | Inventory | undefined_activation_state |
| Product Removal Function | Inventory Updated | undefined_activation_state |
| Product Removal Function | Product Data Entity | unspecified_sign |
| Product Removal Recorded | Purchase History data entity | undefined_activation_state |
| Purchase History Viewing Function | Viewing Event Recorded | undefined_activation_state |
| Shopping Cart Modification Function | Inventory Levels | unspecified_sign |
| Shopping Cart Modification Function | Modification Event | undefined_activation_state |
| Shopping Cart Viewing Function | Viewing Event Recorded | undefined_activation_state |
| Update Event Recorded | Purchase History data entity | undefined_activation_state |
| Viewing Event | Purchase History data entity | undefined_activation_state |
| Active Order/Cart Check | Product Removal Function | unspecified_sign |
| Administrators | Manage Administrator Function | undefined_activation_state |
| Administrators | Manage Contact Information | undefined_activation_state |
| Administrators | Order Cancellation | undefined_activation_state |
| Checkout Event Recorded | Purchase History data entity | undefined_activation_state |
| Customer Registration Function | Contact Information | undefined_activation_state |
| Customer Registration Function | Personal Information | undefined_activation_state |
| Customers | Customer Login Function | undefined_activation_state |
| Customers | Order Cancellation | undefined_activation_state |
| Customers | Purchase History Viewing Function | undefined_activation_state |
| Manage Administrator Function | Management Event | undefined_activation_state |
| Manage CartItem Function | Modification Event | undefined_activation_state |
| Manage CartItem Function | Purchase History data entity | undefined_activation_state |
| Manage Customer Function | Management Event | undefined_activation_state |
| Manage EmailRecord | Purchase History data entity | undefined_activation_state |
| Manage OrderItem | Modification Event | undefined_activation_state |
| Modification Event | Purchase History data entity | undefined_activation_state |
| Payment Event | Purchase History data entity | undefined_activation_state |
| Payment Viewing Event | Purchase History data entity | undefined_activation_state |
| Product | Product Categorization Function | undefined_activation_state |
| Product Removal Function | Purchase History data entity | undefined_activation_state |
| Purchase History Viewing Function | Purchase History data entity | undefined_activation_state |
| Shopping Cart Creation Function | Check Product Availability | cycle_requires_review |
| Update Event | Purchase History data entity | undefined_activation_state |
| User Interface Specification Compliance Checking Function | Purchase History data entity | undefined_activation_state |
| View EmailRecord Function | Purchase History data entity | undefined_activation_state |
| Viewing Event Recorded | Purchase History data entity | undefined_activation_state |
| Administrators | Inventory Management Function | undefined_activation_state |
| Administrators | Manage Category Function | undefined_activation_state |
| Management Event | Purchase History data entity | undefined_activation_state |
| Purchase History | Purchase History Viewing Function | undefined_activation_state |
| Updated contact information fields | Manage Contact Information | undefined_activation_state |
| View CartItem Function | Purchase History data entity | undefined_activation_state |
| Category Validation | Product Categorization Function | cycle_requires_review |
| Logout Event | Purchase History data entity | undefined_activation_state |

## Fixed RQ2 pool (top 10 by |ACE|)

| candidate | source | target | ACE | p(do=1) | p(do=0) | reachability |
|---|---|---|---:|---:|---:|---:|
| DEP-003 | User Interface Specification Compliance Checking Function | Compliance Report | 0.529 | 0.798 | 0.269 | 2 |
| DEP-011 | Order Cancellation | Cancelled Order Status | 0.529 | 0.798 | 0.269 | 3 |
| DEP-016 | Checkout Function | Order Created | 0.529 | 0.798 | 0.269 | 5 |
| DEP-018 | Checkout Function | Payment Processed | 0.529 | 0.798 | 0.269 | 5 |
| DEP-020 | Payment Processing | Successful Payment | 0.529 | 0.798 | 0.269 | 4 |
| DEP-019 | Inventory Management Function | Inventory Levels Stored | 0.529 | 0.929 | 0.400 | 4 |
| DEP-002 | Customer Login Function | Personalized Dashboard | 0.508 | 0.777 | 0.269 | 3 |
| DEP-004 | Order Cancellation | Cancellation Event Recorded | 0.508 | 0.777 | 0.269 | 3 |
| DEP-006 | Customer Registration Function | Customer Account Created | 0.508 | 0.777 | 0.269 | 1 |
| DEP-007 | Order Confirmation Email Sending Function | Confirmation Event | 0.508 | 0.777 | 0.269 | 2 |