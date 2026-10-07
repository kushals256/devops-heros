# Session 21 — TaskBoard capstone

**Author:** Kushal S  
**Enrollment:** 24bcs10355  
**App:** `session21-python/`

The board is the course TaskBoard stack (React, FastAPI, PostgreSQL), with the dashboard signed in as Kushal S. This write-up is the evidence from the machine that actually ran the labs.

## What ran

| Check | Result |
|---|---|
| Pytest | 6 passed (`health`, `ready`, root, create/list/stats, get/update/delete, validation 422) |
| Docker Compose | postgres, backend, frontend all up. UI on http://localhost:3000, API on :8000 |
| Images | Non-root. Frontend is a multi-stage Node build served by nginx on 8080 |
| Helm on Minikube | Release `taskboard` deployed. 2 frontend replicas, 2 backend replicas, Postgres Running |
| Ingress | `taskboard.local`: `/` → frontend, `/api` → backend. Reached with `kubectl port-forward` because the Docker-driver node IP is not reachable from the Mac |
| HPA | `taskboard-backend` min 2 / max 4, target 60% CPU. Live reading was 12%/60% |
| `/metrics` | Prometheus instrumentator on the FastAPI process |
| Terraform | `terraform init` and `terraform validate` succeeded for the VPC + EKS modules in `ap-south-1` |
| Troubleshooting | A missing image ends in `ErrImagePull` / `ImagePullBackOff`. A Service whose selector matches nothing has empty endpoints |

![pytest](screenshots/01-pytest.png)

![compose](screenshots/02-compose.png)

![dashboard](screenshots/03-app.png)

![swagger](screenshots/04-docs.png)

![metrics](screenshots/05-metrics.png)

![helm](screenshots/06-helm.png)

![ingress](screenshots/07-ingress.png)

![broken image](screenshots/08-broken-image.png)

![broken service](screenshots/09-broken-service.png)

![terraform validate](screenshots/11-terraform-validate.png)

![trivy](screenshots/10-trivy.png)

## How it was run

```bash
cd session21-python/backend && .venv/bin/pytest -v
cd session21-python && docker-compose up --build -d
kubectl apply -f session21-python/k8s/namespace.yaml
# images loaded into Minikube as taskboard-frontend:local and taskboard-backend:local
helm upgrade --install taskboard ./helm/taskboard -n taskboard -f ./helm/taskboard/values-minikube.yaml
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 18081:80
curl -H 'Host: taskboard.local' http://127.0.0.1:18081/api/tasks
```

Compose waits until Postgres is healthy, then the backend retries `alembic upgrade head` before uvicorn. Nginx resolves the `backend` hostname at request time and listens on 8080 as user `nginx`, with the pid file in `/tmp`.

The broken manifests are `session21-python/troubleshooting/broken-image.yaml` and `broken-service.yaml`. They were applied, captured, and deleted so they are not left in the namespace.

## What did not run

These items are in `GRADING.md` and were not faked.

- **GitHub Actions and GHCR.** The workflow in `session21-python/.github/workflows/ci-cd.yml` runs pytest, builds both images tagged with the commit SHA, runs Trivy at HIGH and CRITICAL (`exit-code: 1`, `ignore-unfixed: true`), then pushes to GHCR. That only happens after a push to GitHub. Nothing was pushed in this pass.
- **Trivy on this Mac.** Trivy 0.58.1 scanned both local images with `--severity HIGH,CRITICAL --ignore-unfixed`, the same flags as the workflow. The backend OS layer is clean. Python still has 3 HIGH findings in `starlette` 0.41.3. The frontend Alpine image has 42 HIGH and 2 CRITICAL, including `libcrypto3`. Those have fixes, so `ignore-unfixed` does not hide them, and the workflow’s `exit-code: 1` would fail the job until the base image and Starlette are upgraded.
- **`terraform plan`, apply, AWS console, destroy.** `terraform validate` is clean. A plan needs a working AWS principal. The class key returns `InvalidClientTokenId`, and an EKS apply would also create a NAT gateway and two `t3.medium` nodes. No stack was created, so there is nothing to destroy and no console screenshot.
- **Prometheus and Grafana.** `/metrics` is live on the backend. The ServiceMonitor stays off in `values-minikube.yaml` because the Minikube cluster does not have the Prometheus Operator CRDs, and the kube-prometheus-stack was not installed on this node.

## Fixes made so the labs match the checklist

- Pytest uses a `TestClient` lifespan so SQLite creates the `tasks` table, and `psycopg` is `3.2.10` so the local Python 3.14 venv can install it. The container still runs Python 3.12.
- Frontend image runs as `nginx` on port 8080. Compose maps `3000:8080`.
- Terraform files are normal HCL. The previous one-line blocks failed `terraform validate`.
- `terraform/terraform.tfvars.example` has region and cluster name only. No credentials.
