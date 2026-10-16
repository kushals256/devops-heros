# AWS IAM — Governance

**Author notes (Session 18 homework):** Kushal S · 24bcs10355

## What is IAM?

**Identity and Access Management** controls authentication (who you are) and authorization (what you can do) across AWS.

## Users

- Long-lived identity for a person or automation account
- Can have console password and/or access keys
- Prefer **not** attaching policies directly to users — use groups/roles

## Groups

- Collection of users that share the same policies
- Example: `Developers`, `Ops`, `ReadOnly`

## Roles

- Temporary credentials assumed via STS (`AssumeRole`)
- Used by EC2, Lambda, EKS pods, cross-account access, federated users
- Preferred over long-lived access keys for services

## Policies

- JSON documents of `Effect` / `Action` / `Resource` / optional `Condition`
- Types: managed (AWS), customer managed, inline

## Permissions

```text
Explicit Deny  >  Explicit Allow  >  Default Deny
```

## Least privilege

Grant only the minimum actions and resources required for a task. Start deny-all, add what is needed, review regularly.

## IAM best practices

1. Enable MFA for interactive users
2. Prefer roles over long-lived access keys
3. Attach policies to groups/roles, not individual users when possible
4. Protect the root account; do not use it for daily work
5. Rotate access keys; prefer short-lived credentials
6. Use CloudTrail to audit API calls
7. Use permission boundaries / SCPs in multi-account setups

## Common use cases

- Human login to AWS Console
- CI/CD role assumed by GitHub Actions (OIDC)
- EC2 instance profile reading from S3
- Cross-account admin role for platform team

## Useful CLI

```bash
aws sts get-caller-identity
aws iam list-users
aws iam list-attached-user-policies --user-name <username>
aws iam list-roles
```
