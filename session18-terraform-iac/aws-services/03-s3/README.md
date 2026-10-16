# AWS S3 — Storage

**Author notes (Session 18 homework):** Kushal S · 24bcs10355

## What is S3?

**Simple Storage Service** — object storage. Files are objects (key + data + metadata) inside buckets.

## Buckets

- Globally unique name
- Belong to one region
- Container for objects and policies

## Objects

- Addressable by key (path-like string)
- Optional version IDs when versioning is on
- Metadata and tags for lifecycle/search

## Storage classes

| Class | Typical use |
|---|---|
| Standard | Hot / frequent access |
| Standard-IA / One Zone-IA | Infrequent access |
| Glacier Instant / Flexible / Deep Archive | Archive / backup |
| Intelligent-Tiering | Unknown or changing access patterns |

## Versioning

Keeps previous versions of an object so deletes/overwrites are recoverable.

## Lifecycle policies

Rules that transition objects to colder classes or expire them after N days.

## Encryption

- **SSE-S3** — AWS-managed keys
- **SSE-KMS** — customer-controlled via KMS
- **SSE-C** — customer-provided keys
- Bucket default encryption recommended

## Bucket policies

JSON resource policies on the bucket (who can `s3:GetObject`, public access blocks, enforce HTTPS, etc.). Combine with IAM identity policies.

## Common use cases

- Static websites / assets
- Terraform remote state
- CI artifacts and logs
- Backups and data lakes
- Session 18 `terraform-s3-demo` homework bucket

## Useful CLI

```bash
aws s3 ls
aws s3 mb s3://my-unique-bucket-name
aws s3 cp ./file.txt s3://my-unique-bucket-name/
aws s3 rb s3://my-unique-bucket-name --force
```
