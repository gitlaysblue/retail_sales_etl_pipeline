# Local Retail Sales ETL Pipeline & Analytics Warehouse

## 📌 Project Overview
An end-to-end data engineering pipeline designed to simulate a modern cloud data platform architecture running entirely on a local machine.
This project extracts raw transactional retail logs, applies rigorous cleaning transformations using Python,
structures and warehouses the data inside PostgreSQL, and delivers an executive business intelligence dashboard via Power BI.

### 🛠️ Architecture Flow
```text
[Raw CSV Landing] ──> (Python ETL Engine) ──> [PostgreSQL Warehouse] ──> [Power BI Interactive Dashboard]
   (Data Lake)            (Pandas/SQLAlchemy)           (Data Store)                  (BI Analytics Layer)
