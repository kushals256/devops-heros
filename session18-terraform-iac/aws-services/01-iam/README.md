# AWS IAM – Governance & Identity Security

**IAM (Identity and Access Management)** controls who can do what in AWS.

## Core Building Blocks

| Concept | Meaning |
|---|---|
| **User** | Long-lived identity for a person or service |
| **Group** | Collection of users that share policies |
| **Role** | Temporary credentials assumed by services or users (via STS) |
| **Policy** | JSON document describing Allow/Deny permissions |

## Policy Evaluation

```text
Explicit Deny  >  Explicit Allow  >  Default Deny
```

## Principle of Least Privilege

Grant only the minimum actions and resources required for a task.

## Best Practices

1. Enable MFA for interactive users.
2. Prefer roles over long-lived access keys.
3. Attach policies to groups/roles, not individual users when possible.
4. Protect the root account; do not use it for daily work.
5. Rotate access keys regularly.

## Useful CLI Commands

```bash
aws sts get-caller-identity
aws iam list-users
aws iam list-attached-user-policies --user-name <username>
```
