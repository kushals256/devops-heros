# AWS EC2 — Compute

**Author notes (Session 18 homework):** Kushal S · 24bcs10355

## What is EC2?

**Elastic Compute Cloud** provides virtual servers (instances) you control — OS, packages, networking, and storage attachments.

## AMI

**Amazon Machine Image** — template (OS + baked software) used to launch instances. Examples: Amazon Linux 2023, Ubuntu.

## Instance types

CPU / memory / network / GPU size classes (`t4g.micro`, `t3.micro`, `m6i.large`, …). Family letter + generation + size.

## Key pairs

SSH public/private key material for Linux login. AWS stores the public key; you keep the private `.pem`.

## Security Groups

Stateful virtual firewall attached to ENIs/instances. Allow rules for inbound/outbound; return traffic is tracked automatically.

## EBS

**Elastic Block Store** — persistent block volumes attached to instances (gp3, io2, …). Survive stop/start; deleted with instance only if `DeleteOnTermination` is true.

## Public vs private IP

| | Public IP | Private IP |
|---|---|---|
| Scope | Internet-routable | VPC-internal |
| Stop/start | Often changes (unless Elastic IP) | Stays with the ENI |
| Use | Bastion, public web | App tiers, databases |

## Instance lifecycle

```text
Pending → Running → Stopping → Stopped → (start again) → Terminated
```

- **Stop**: EBS-backed; billing for storage continues, not for instance hours
- **Terminate**: instance gone; EBS may be deleted per flag

## Common use cases

- Web servers / app servers
- Bastion hosts
- Build agents / runners
- Session 19 Terraform lab (`t4g.micro` + nginx user-data)

## Useful CLI

```bash
aws ec2 describe-instances
aws ec2 describe-security-groups
aws ec2 describe-images --owners amazon --filters "Name=name,Values=al2023-ami-*"
```
