# Session 18 — Terraform & Infrastructure as Code

**Repository path:** `session18-terraform-iac/`

This session covers two things:
1. Running the full Terraform workflow to create and destroy an AWS S3 bucket
2. Understanding the core AWS services that show up in real cloud / DevOps work

---

## What You Will Learn

| Topic | Outcome |
|---|---|
| Infrastructure as Code | Define cloud resources in files instead of clicking in a console |
| Terraform workflow | `init` → `fmt` → `validate` → `plan` → `apply` → `output` → `destroy` |
| State | How Terraform remembers what it created |
| AWS foundations | IAM, EC2, S3, VPC, DynamoDB, RDS |

---

## Project Layout

```text
session18-terraform-iac/
├── Assignment_Readme.md          ← this file
├── Readme.md                     ← install links
├── 01-iac-basics/ … 09-state/    ← concept labs from course
├── terraform-s3-demo/            ← hands-on S3 project
│   ├── terraform.tf
│   ├── providers.tf
│   ├── variables.tf
│   ├── terraform.tfvars          ← local values (gitignored)
│   ├── main.tf
│   ├── outputs.tf
│   └── README.md
└── aws-services/
    ├── 01-iam/
    ├── 02-ec2/
    ├── 03-s3/
    ├── 04-vpc/
    └── 05-dynamodb-rds/
```

---

## Task 1 — Terraform S3 Demo

### Goal

Use Terraform to create an S3 bucket in `ap-northeast-2` (Seoul), inspect state/outputs, verify it in AWS, then destroy it cleanly.

### Code Overview

**`terraform.tf`** — version + provider constraints

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}
```

**`providers.tf`** — AWS region from a variable

```hcl
provider "aws" {
  region = var.aws_region
}
```

**`variables.tf`** — inputs

```hcl
variable "aws_region" {
  type        = string
  description = "AWS region where the S3 bucket will be created."
  default     = "ap-northeast-2"
}

variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket."
  default     = "yatri1107"
}
```

**`main.tf`** — the bucket resource

```hcl
resource "aws_s3_bucket" "yatri1107" {
  bucket        = var.bucket_name
  force_destroy = true

  tags = {
    Name        = var.bucket_name
    Environment = "dev"
    ManagedBy   = "Terraform"
    Project     = "Session18"
  }
}
```

**`outputs.tf`** — values Terraform prints after apply

```hcl
output "bucket_name" {
  value = aws_s3_bucket.yatri1107.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.yatri1107.arn
}

output "bucket_region" {
  value = aws_s3_bucket.yatri1107.region
}
```

### Prerequisites

```bash
# Install (once)
# Terraform: https://developer.hashicorp.com/terraform/install
# AWS CLI:   https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

terraform -version
aws --version
aws configure
aws sts get-caller-identity
```

`aws sts get-caller-identity` should succeed before you run any Terraform commands.

### Hands-on Workflow

```bash
cd session18-terraform-iac/terraform-s3-demo
```

| Step | Command | What it does |
|---|---|---|
| 1 | `terraform init` | Downloads AWS provider, creates lock file |
| 2 | `terraform fmt` | Formats `.tf` files |
| 3 | `terraform validate` | Checks syntax (no cloud API calls) |
| 4 | `terraform plan` | Shows what will be created/changed/destroyed |
| 5 | `terraform apply` | Creates the bucket (type `yes`) |
| 6 | `terraform state list` | Lists resources in state |
| 7 | `terraform state show aws_s3_bucket.yatri1107` | Shows full resource details |
| 8 | `terraform output` | Prints bucket name / ARN / region |
| 9 | `aws s3 ls` | Confirms the bucket exists in AWS |
| 10 | `terraform plan -destroy` | Preview teardown |
| 11 | `terraform destroy` | Deletes the bucket (type `yes`) |

Expected plan before create:

```text
Plan: 1 to add, 0 to change, 0 to destroy.
```

Expected destroy plan:

```text
Plan: 0 to add, 0 to change, 1 to destroy.
```

### Lifecycle (mental model)

```text
*.tf / *.tfvars
      │
      ▼
  terraform init
      │
      ▼
  fmt + validate
      │
      ▼
  plan  ──► review deltas
      │
      ▼
  apply ──► AWS resources + terraform.tfstate
      │
      ├── state list / show / output
      │
      ▼
  destroy ──► resources removed, state updated
```

### About `terraform.tfstate`

- JSON file mapping config → real cloud objects
- Local state is fine for class demos
- Production: store state in a remote backend (S3) with locking (DynamoDB)
- Never edit the state file by hand

---

## Task 2 — AWS Core Services (Research Notes)

Full write-ups live under [`aws-services/`](./aws-services/). Short summary below.

### IAM — Who is allowed to do what

- **Users / Groups / Roles / Policies**
- Roles give temporary credentials (preferred over long-lived keys)
- Evaluation order: explicit deny → allow → default deny
- Best practice: least privilege + MFA + protect root

### EC2 — Virtual machines

- Launch from an **AMI**
- Choose an **instance type** (CPU/RAM size)
- **Security Groups** control inbound/outbound traffic
- **EBS** = persistent disk
- Lifecycle: Pending → Running → Stopped → Terminated

### S3 — Object storage

- Buckets hold objects (files)
- Bucket names are globally unique
- Storage classes trade cost vs access speed
- Versioning + lifecycle rules protect and age data
- Common DevOps uses: artifacts, logs, Terraform remote state

### VPC — Your private network

```text
VPC (10.0.0.0/16)
 ├── Public subnet  → Internet Gateway
 └── Private subnet → NAT Gateway (outbound only)
```

- Security Groups = stateful, instance-level
- NACLs = stateless, subnet-level

### DynamoDB & RDS — Databases

| | DynamoDB | RDS |
|---|---|---|
| Type | NoSQL | Relational SQL |
| Scale | Horizontal partitions | Vertical + read replicas |
| Best for | High-throughput key lookups, locks | Apps needing JOINs / ACID |
| DevOps note | Often used for Terraform state locking | Common app primary DB |

---

## Quick Reference — Terraform Commands

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform state list
terraform state show <resource>
terraform output
terraform plan -destroy
terraform destroy
```

## Quick Reference — AWS Checks

```bash
aws sts get-caller-identity
aws s3 ls
aws s3 ls s3://yatri1107
```

---

## Checklist

| Item | Location |
|---|---|
| S3 Terraform project | `terraform-s3-demo/` |
| Manifests (`main`, `variables`, `outputs`, `providers`, `terraform`) | `terraform-s3-demo/*.tf` |
| Project README | `terraform-s3-demo/README.md` |
| IAM notes | `aws-services/01-iam/README.md` |
| EC2 notes | `aws-services/02-ec2/README.md` |
| S3 notes | `aws-services/03-s3/README.md` |
| VPC notes | `aws-services/04-vpc/README.md` |
| DynamoDB & RDS notes | `aws-services/05-dynamodb-rds/README.md` |

---

## Notes

- S3 bucket names must be globally unique. If `yatri1107` is taken, change `bucket_name` in `variables.tf` / `terraform.tfvars`.
- Always run `terraform destroy` after the lab so you do not leave unused (billable) resources.
- Keep AWS access keys out of git. `*.tfvars` is gitignored in this project for that reason.
