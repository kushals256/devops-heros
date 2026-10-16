# AWS VPC — Networking

**Author notes (Session 18 homework):** Kushal S · 24bcs10355

## What is VPC?

A **Virtual Private Cloud** is your isolated private network in an AWS Region.

## CIDR

IP range for the VPC, e.g. `10.20.0.0/16`. Subnets carve smaller ranges from it.

## Subnets

- Slice of the VPC in **one Availability Zone**
- Public or private depending on routing (not a magic flag alone)

## Route tables

Rules that decide where packets go (local VPC, IGW, NAT, peering, TGW).

## Internet Gateway (IGW)

Attached to the VPC; enables traffic between public subnets and the internet when routes point `0.0.0.0/0` to the IGW and instances have public IPs.

## NAT Gateway

Outbound internet for **private** subnets (updates, package installs) without allowing inbound from the internet.

## Security Groups

Stateful, instance/ENI-level allow lists.

## Network ACLs

Stateless, subnet-level allow/deny. Less common for day-to-day app rules than security groups; used for coarse subnet controls.

## Public vs private subnet

```text
Public subnet  → route 0.0.0.0/0 to Internet Gateway (+ public IP / EIP)
Private subnet → route 0.0.0.0/0 to NAT Gateway (no direct IGW)
```

## Common pattern (Session 19 lab)

```text
VPC → public subnet → IGW → security group → EC2
```

## Useful CLI

```bash
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-internet-gateways
```
