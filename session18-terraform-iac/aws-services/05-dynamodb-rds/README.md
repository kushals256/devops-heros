# AWS DynamoDB & RDS – Cloud Databases

## Quick Comparison

| | **DynamoDB** | **RDS** |
|---|---|---|
| Model | NoSQL (key-value / document) | Relational SQL |
| Schema | Flexible items | Fixed tables / relations |
| Scaling | Horizontal partitions | Vertical + Read Replicas |
| Strength | Low latency at huge scale | JOINs, ACID, complex queries |
| Common DevOps use | Terraform state locking | App transactional databases |

## DynamoDB Basics

- **Partition key** (and optional **sort key**) uniquely identify items.
- Fully managed / serverless style scaling.
- Used often for sessions, locks, high-throughput lookups.

## RDS Basics

- Managed engines: PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora.
- **Multi-AZ** for high availability (failover).
- **Read Replicas** for read scaling.
- Automated backups and Point-In-Time Recovery (PITR).

## Useful CLI Commands

```bash
aws dynamodb list-tables
aws rds describe-db-instances
```
