# AWS VPC – Virtual Private Cloud Networking

**VPC** is your private network inside AWS.

## Key Concepts

| Concept | Meaning |
|---|---|
| **CIDR** | IP range for the VPC (e.g. `10.0.0.0/16`) |
| **Subnet** | Slice of the VPC in one Availability Zone |
| **Route table** | Rules for where traffic goes |
| **Internet Gateway** | Path from public subnets to the internet |
| **NAT Gateway** | Outbound internet for private subnets |
| **Security Group** | Stateful, instance-level firewall |
| **NACL** | Stateless, subnet-level firewall |

## Public vs Private Subnet

```text
Public subnet  → route 0.0.0.0/0 to Internet Gateway
Private subnet → route 0.0.0.0/0 to NAT Gateway (no direct IGW)
```

## Useful CLI Commands

```bash
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
```
