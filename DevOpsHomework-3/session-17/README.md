# Session 17 — CI/CD and DevSecOps

**Author:** Kushal S  
**Enrollment:** 24bcs10355

## Flow

```text
Code → unit test → secret scan → Docker build → image scan → deploy
```

| Stage | Implementation |
|---|---|
| Application | `app.py` (`greet`) |
| Unit test | `tests/test_app.py` — 1 passed |
| Secret scan | Workflow step fails if it finds an `AKIA…` key. Local scan passed |
| Docker build | `Dockerfile`, image `session17-devsecops:local`, container printed `Hello Docker` |
| Image scan | Workflow runs `aquasec/trivy` on `HIGH,CRITICAL` |
| Kubernetes | `k8s/deployment.yaml`, `k8s/service.yaml` |
| Security gate | `build` and deploy are not separate jobs that skip a failed test. The workflow is one ordered job: a failed test or secret scan stops the rest |

The unit test covers `greet`. The secret scan searches the tree for an access-key pattern and passed on this app. The image build produced `session17-devsecops:local`, and the container printed `Hello Docker`. Trivy in the workflow scans that image at HIGH and CRITICAL before the Kubernetes manifests are applied.

![pytest](screenshots/02-pytest.png)

![pipeline](screenshots/01-pipeline.png)

The secret scan is the gate that stops the job when an access key is committed.
