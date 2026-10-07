# Session 19 — Cloud infrastructure with Terraform

**Author:** Kushal S  
**Enrollment:** 24bcs10355  
**Region:** `ap-northeast-2` (Seoul)

## Architecture

```text
Terraform
    |
    ├── VPC 10.20.0.0/16          aws_vpc.main
    |
    ├── Public subnet 10.20.1.0/24  aws_subnet.public
    |
    ├── Internet gateway          aws_internet_gateway.main
    |     └── public route 0.0.0.0/0
    |
    ├── Security group            aws_security_group.web  (TCP 80)
    |
    ├── EC2 t4g.micro             aws_instance.web
    |     └── depends_on the internet gateway
    |
    └── S3                        aws_s3_bucket.lab
```

Files: `versions.tf`, `variables.tf`, `main.tf`, `outputs.tf`.

What the project demonstrates:

| Terraform idea | Where |
|---|---|
| Provider | `provider "aws"` in `versions.tf` |
| Variables | `aws_region`, `project` |
| Resources | VPC, subnet, IGW, route table, association, security group, instance, bucket |
| Outputs | vpc id, subnet id, security group id, instance id, bucket name |
| Dependencies | Subnet and IGW use the VPC id. The instance `depends_on` the IGW. The route uses the gateway id |
| State | Local `terraform.tfstate`, gitignored |

## Workflow

`terraform init`, `terraform fmt`, and `terraform validate` succeeded. The graph is one VPC, one public subnet, an internet gateway, a public route, a security group on TCP 80, one `t4g.micro` Amazon Linux 2023 instance, and one S3 bucket `session19-kushal-304166770455`.

On 3 Oct 2026 the Seoul VPC lab destroyed two `session19-vpc` stacks: `vpc-08a326bb68c82cc0b` and `vpc-06dd90e20035e1c53`, with their subnets, internet gateways, route tables, and security groups.
