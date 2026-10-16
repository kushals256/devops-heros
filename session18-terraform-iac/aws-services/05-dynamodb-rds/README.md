# AWS DynamoDB & RDS — Database Services

**Author notes (Session 18 homework):** Kushal S · 24bcs10355

## DynamoDB

### What it is

Fully managed **NoSQL** key-value / document database.

### Core concepts

| Concept | Meaning |
|---|---|
| Table | Collection of items |
| Item | A single record (JSON-like attribute map) |
| Attributes | Fields on an item |
| Partition key | Required; hashes to a storage partition |
| Sort key | Optional; orders items under the same partition key |

### Use cases

- Session stores, feature flags
- High-throughput lookups
- Terraform state locking (`dynamodb` lock table with S3 backend)
- IoT / gaming leaderboards

## RDS

### What it is

Managed **relational** database service (SQL engines).

### Supported engines

PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Amazon Aurora (MySQL/PostgreSQL compatible).

### DB instances

Sized compute + storage (instance class, allocated storage, Multi-AZ option).

### Security

- Deploy in private subnets
- Security groups limiting app-tier access
- Encryption at rest (KMS) and in transit (TLS)
- IAM auth optional for some engines

### Backups

Automated backups + manual snapshots; Point-In-Time Recovery (PITR) within retention window.

### Multi-AZ

Synchronous standby in another AZ for automatic failover (HA, not read scaling).

### Read replicas

Async copies for read scaling (and cross-region DR patterns).

### Use cases

- Transactional application databases
- Analytics replicas
- Course apps that need SQL (e.g. Postgres for a web API)

## Quick comparison

| | DynamoDB | RDS |
|---|---|---|
| Model | NoSQL | Relational SQL |
| Schema | Flexible items | Fixed tables / relations |
| Scaling | Horizontal partitions | Vertical + read replicas |
| Strength | Low latency at huge scale | JOINs, ACID, complex queries |

## Useful CLI

```bash
aws dynamodb list-tables
aws rds describe-db-instances
```
