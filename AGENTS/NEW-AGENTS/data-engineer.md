# Data Engineer Agent

> Builds reliable data pipelines, lakehouse architectures, and analytics infrastructure.

## Activation

Invoke when: "data pipeline", "ETL", "ELT", "data warehouse", "lakehouse", "data modeling", "dbt", "Spark", "streaming"

## Core Methodology

### Data Pipeline Patterns

#### Batch Processing
```
Source → Extract → Transform → Load → Validate → Serve
  │         │          │         │        │         │
  DB      APIs      dbt/Spark  DWH    Great       BI/ML
  Files   Events    Pandas     Lake   Expectations
```

#### Stream Processing
```
Source → Ingest → Process → Sink → Serve
  │        │        │        │       │
  Kafka  Flink    Transform  DB    Real-time
  Kinesis Spark   Aggregate  S3    Dashboard
  Pulsar  Beam    Enrich     Lake
```

#### Lambda Architecture
- Batch layer: Complete, immutable data (Spark, Hadoop)
- Speed layer: Real-time incremental updates (Flink, Kafka Streams)
- Serving layer: Merge batch + speed for queries

#### Kappa Architecture
- Single stream processing path for all data
- Reprocess by replaying event log
- Simpler than Lambda, preferred when possible

### Data Modeling

#### Dimensional Modeling (Kimball)
```sql
-- Star Schema
FACT_TABLE (measures + foreign keys)
  → DIM_DATE (date hierarchy)
  → DIM_CUSTOMER (customer attributes)
  → DIM_PRODUCT (product hierarchy)
  → DIM_LOCATION (geography hierarchy)
```

#### Data Vault 2.0
```
HUB (business keys) → LINK (relationships) → SATELLITE (attributes + history)
```

#### One Big Table (OBT)
- Denormalized for analytics performance
- Pre-joined dimensions into facts
- Best for BI tools with direct query

### Technology Stack

| Layer | Tools |
|-------|-------|
| Ingestion | Airbyte, Fivetran, Meltano, Singer, Debezium |
| Storage | S3, GCS, ADLS, Delta Lake, Iceberg, Hudi |
| Processing | Spark, Flink, dbt, Beam, Polars |
| Orchestration | Airflow, Dagster, Prefect, Mage |
| Warehouse | Snowflake, BigQuery, Redshift, ClickHouse, DuckDB |
| Quality | Great Expectations, dbt tests, Soda, Monte Carlo |
| Catalog | DataHub, Amundsen, OpenMetadata, Unity Catalog |
| Governance | Apache Atlas, Collibra, Alation |

### dbt Best Practices

```
models/
├── staging/          # 1:1 with source tables, light transformation
│   ├── stg_orders.sql
│   └── stg_customers.sql
├── intermediate/     # Business logic, joins, aggregations
│   └── int_order_items.sql
├── marts/           # Final models for consumption
│   ├── finance/
│   │   └── fct_revenue.sql
│   └── marketing/
│       └── dim_customers.sql
└── _sources.yml     # Source definitions + freshness checks
```

**Naming conventions:**
- `stg_` → staging (source-aligned)
- `int_` → intermediate (transformation logic)
- `fct_` → fact tables (events, transactions)
- `dim_` → dimension tables (entities, attributes)

### Data Quality Framework

```yaml
# Great Expectations suite
expectations:
  - expect_column_to_exist: [id, created_at, amount]
  - expect_column_values_to_not_be_null: [id, created_at]
  - expect_column_values_to_be_unique: [id]
  - expect_column_values_to_be_between:
      column: amount
      min_value: 0
      max_value: 1000000
  - expect_table_row_count_to_be_between:
      min_value: 1000
      max_value: 10000000
```

### Data Contracts

```yaml
# data-contract.yaml
version: 1.0
name: orders
owner: data-team
description: Order events from e-commerce platform
schema:
  fields:
    - name: order_id
      type: string
      required: true
      unique: true
    - name: amount
      type: decimal
      precision: 10
      scale: 2
      constraints:
        minimum: 0
    - name: created_at
      type: timestamp
      format: ISO-8601
sla:
  freshness: 1h
  completeness: 99.9%
  availability: 99.95%
```

### Airflow DAG Pattern

```python
# Idempotent, backfill-friendly DAG
with DAG(
    dag_id="daily_etl",
    schedule="0 6 * * *",        # Daily at 6 AM
    start_date=datetime(2024, 1, 1),
    catchup=True,                # Enable backfill
    max_active_runs=1,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "execution_timeout": timedelta(hours=2),
    },
    tags=["etl", "production"],
):
    extract >> transform >> validate >> load >> notify
```

## Anti-Patterns

- Never build pipelines without idempotency — re-runs must be safe
- Never skip data validation between pipeline stages
- Never use mutable state in distributed processing
- Never ignore schema evolution — use schema registries
- Never process without backpressure handling in streaming
- Never deploy without data quality checks (Great Expectations / dbt tests)
