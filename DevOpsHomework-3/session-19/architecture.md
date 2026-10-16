# Session 19 — Architecture diagram

**Author:** Kushal S · **Enrollment:** 24bcs10355

```mermaid
flowchart TB
  TF[Terraform apply]
  TF --> VPC[aws_vpc.main<br/>10.20.0.0/16]
  VPC --> SUB[aws_subnet.public<br/>10.20.1.0/24]
  VPC --> IGW[aws_internet_gateway.main]
  VPC --> RT[aws_route_table.public<br/>0.0.0.0/0 → IGW]
  RT --> RTA[aws_route_table_association.public]
  RTA --> SUB
  VPC --> SG[aws_security_group.web<br/>ingress TCP 80]
  SUB --> EC2[aws_instance.web<br/>t4g.micro + nginx]
  SG --> EC2
  IGW -.->|depends_on| EC2
  TF --> S3[aws_s3_bucket.lab]
  Internet((Internet)) --> IGW
  IGW --> SUB
```

## Resource map

| Layer | Resource | Purpose |
|---|---|---|
| Network | VPC + public subnet + IGW + route | Reachable public network |
| Security | Security group | Allow HTTP 80 |
| Compute | EC2 `t4g.micro` | nginx Hello World via user-data |
| Storage | S3 bucket | Lab object storage |

This matches the course suggested architecture: **VPC → Subnet → Security Group → EC2 → S3**.
