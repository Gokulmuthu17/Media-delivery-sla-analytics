# 📦 Media Delivery SLA & Operations Analytics Platform

An end-to-end analytics case study that simulates large-scale media delivery operations and analyzes SLA breaches, partner performance, artwork/content quality risks, and operational delay drivers using Python, MySQL, and Looker Studio.
This project mirrors real-world OTT / broadcast supply-chain analytics used by streaming platforms and media distributors.
________________________________________
 Project Objective
To build a realistic analytics platform that:
•	Tracks delivery volumes & success rates
•	Identifies SLA breach drivers
•	Ranks risky partners, formats, and genres
•	Flags high-risk content titles
•	Enables operational teams to take corrective actions
________________________________________
Business Problems Solved
•	Which partners contribute most to SLA breaches?
•	Does approval status impact delivery time?
•	Which formats (TIFF, PNG, JPEG) fail more?
•	Are certain genres operationally risky?
•	Where should operations teams focus first?
________________________________________
 Architecture Overview
Python → CSV Data Generator  
        ↓
MySQL Data Warehouse  
        ↓
SQL Views & Metrics Layer  
        ↓
Looker Studio Dashboards
________________________________________
Tech Stack
•	Python – Synthetic data generation
•	MySQL – Data warehouse & transformations
•	SQL – KPI logic & aggregations
•	Looker Studio – Dashboarding
•	GitHub – Version control & portfolio hosting
________________________________________
Dashboards Included
1) Executive Overview
High-level health of delivery operations.
KPIs:
•	Total Deliveries
•	SLA Breach %
•	Success Rate %
•	Avg Delivery Hours
Charts:
•	SLA Breach Trend Over Time
•	Key Insight Summary
________________________________________
2) Partner Performance Analysis
Evaluates which partners cause most operational risk.
KPIs:
•	Partner Deliveries
•	Partner SLA Breach %
•	Partner Success Rate %
Charts:
•	Top Partners by SLA Breach Rate
•	Delivery Volume by Partner
•	Partner Performance Table
________________________________________
3) Content & Artwork Quality Risk
Identifies risky titles, formats, and genres.
KPIs:
•	Total Failures
•	Failure Rate %
•	Avg Delivery Hours
•	SLA Breach %
Charts:
•	High-Risk Content Titles
•	Failures by Asset Format
•	Failures by Genre
•	Failure Trend Over Time
________________________________________
4) Operational Drilldowns – Risk & Delay Drivers
Deep dive into root causes.
KPIs:
•	Total Deliveries
•	SLA Breach %
•	Success Rate %
•	Avg Delivery Hours
Charts:
•	Impact of Approval on Delivery Time
•	SLA Breach by Format
•	High-Risk Operational Segments
•	Avg Delivery Time by Partner
________________________________________
KPI & Metric Definitions
Total Deliveries
COUNT(delivery_id)
Total Failures
COUNT(CASE WHEN status = 'FAILED' THEN delivery_id END)
Success Rate %
SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END) / COUNT(*) * 100
SLA Breach %
SUM(CASE WHEN actual_hours > sla_hours THEN 1 ELSE 0 END) / COUNT(*) * 100
Avg Delivery Hours
AVG(actual_hours)
________________________________________
Repository Structure
media-delivery-sla-analytics/
│
├── python/              # Data generator scripts
├── sql/                 # Warehouse schema & KPI queries
├── dashboards/          # Looker screenshots
├── case-study/          # PDF documentation
├── data_model/          # ER diagrams
└── README.md
________________________________________
 Key Insights Discovered
•	SLA breaches remain high even with strong success rates → hidden inefficiencies exist.
•	LATAM partners show higher SLA risk despite moderate volumes.
•	TIFF assets have higher breach rates than PNG/JPEG.
•	Approval delays significantly increase delivery time.
•	Certain genres (Sports, Action) experience more failures.
________________________________________
Why This Project Matters
This case study demonstrates:
✔ End-to-end analytics engineering
✔ KPI design for executives
✔ Operational root cause analysis
✔ Dashboard storytelling
✔ Real-world media domain understanding
Perfect for Data Analyst / BI / Analytics Engineer portfolios.
________________________________________
 How to Run Locally
1.	Run Python generator:
python generate_media_data.py
2.	Load CSVs into MySQL.
3.	Create SQL views.
4.	Connect Looker Studio to exported views.
________________________________________
Author
Gokul Muthu
Data Analytics | BI Engineering | SQL | Python

