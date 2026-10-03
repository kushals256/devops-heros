# AWS S3 – Simple Storage Service

**S3** is object storage for files (objects) inside buckets.

## Key Concepts

| Concept | Meaning |
|---|---|
| **Bucket** | Globally unique container in a region |
| **Object** | File stored as key + data (+ metadata) |
| **Storage class** | Cost/performance tier (Standard, IA, Glacier, …) |
| **Versioning** | Keeps previous object versions |
| **Lifecycle** | Auto-transition / expire objects |
| **Encryption** | SSE-S3, SSE-KMS, SSE-C |

## Why S3 Matters for DevOps

- Store artifacts, backups, static websites, logs.
- Common remote backend for Terraform state.

## Useful CLI Commands

```bash
aws s3 ls
aws s3 mb s3://my-unique-bucket-name
aws s3 cp ./file.txt s3://my-unique-bucket-name/
aws s3 rb s3://my-unique-bucket-name --force
```
