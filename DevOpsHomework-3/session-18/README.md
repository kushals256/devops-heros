# Session 18 — Terraform S3 and AWS services

**Author:** Kushal S  
**Enrollment:** 24bcs10355

## Task 1 — S3 project

Project: `session18-terraform-iac/terraform-s3-demo/`

```text
main.tf
variables.tf
outputs.tf
providers.tf
terraform.tfvars   (gitignored)
README.md
```

### Workflow

| Command | Result |
|---|---|
| `terraform init` | AWS provider v6.66.0 installed |
| `terraform fmt` | Files already formatted |
| `terraform validate` | Configuration is valid |

The bucket is `aws_s3_bucket.devops553` in `ap-northeast-2`, with `force_destroy = true`, so destroy removes the bucket even when it still has objects. State stays in the local `terraform.tfstate`, which is gitignored.

## Task 2 — AWS service notes

| Service | README |
|---|---|
| IAM | `session18-terraform-iac/aws-services/01-iam/README.md` |
| EC2 | `session18-terraform-iac/aws-services/02-ec2/README.md` |
| S3 | `session18-terraform-iac/aws-services/03-s3/README.md` |
| VPC | `session18-terraform-iac/aws-services/04-vpc/README.md` |
| DynamoDB and RDS | `session18-terraform-iac/aws-services/05-dynamodb-rds/README.md` |

Longer walkthrough: `session18-terraform-iac/Assignment_Readme.md`.
