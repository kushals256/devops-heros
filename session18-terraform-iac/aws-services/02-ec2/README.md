# AWS EC2 – Elastic Compute Cloud

**EC2** provides virtual servers (instances) in the cloud.

## Key Concepts

| Concept | Meaning |
|---|---|
| **AMI** | Image template (OS + software) used to launch instances |
| **Instance type** | CPU / memory / network size (`t3.micro`, `m6i.large`, …) |
| **Key pair** | SSH public/private key for login |
| **Security Group** | Stateful firewall for instance traffic |
| **EBS** | Persistent block disk attached to the instance |
| **Elastic IP** | Static public IPv4 address |

## Public vs Private IP

- **Private IP** — stays with the network interface across stop/start.
- **Public IP** — may change on stop/start unless you use an Elastic IP.

## Lifecycle

```text
Pending → Running → Stopping → Stopped → Terminated
```

## Useful CLI Commands

```bash
aws ec2 describe-instances
aws ec2 describe-security-groups
aws ec2 describe-images --owners amazon --filters "Name=name,Values=ubuntu/*"
```
