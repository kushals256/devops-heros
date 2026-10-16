# Session 17 — Complete CI/CD + DevSecOps

**Author:** Kushal S  
**Enrollment:** 24bcs10355

## Expected flow

```text
Code → Unit Test → SAST (Bandit) → SCA (pip-audit) → Secret Scan
  → Docker Build → Trivy (HIGH/CRITICAL exit 1) → Push GHCR → Deploy (kind)
```

## Deliverables

| Item | Path |
|---|---|
| Application | `app/app.py` |
| Dockerfile | `Dockerfile` |
| Tests | `tests/test_app.py` |
| Workflow | `.github/workflows/devsecops.yml` |
| Security notes | `SECURITY.md` |
| Kubernetes | `k8s/deployment.yaml`, `k8s/service.yaml` |

## Screenshots / proof

### Unit tests (3 passed)

![pytest](screenshots/03-pytest.png)

### SAST — Bandit (no issues)

![bandit](screenshots/04-bandit.png)

### SCA — pip-audit (no known vulns in requirements.txt)

![pip-audit](screenshots/05-pip-audit.png)

### Secret scan passed

![secret scan](screenshots/06-secret-scan.png)

### App running in Docker

![app running](screenshots/08-app-running.png)

![app ui](screenshots/09-app-ui.png)

### Trivy image scan — Total HIGH/CRITICAL: 0

![trivy](screenshots/10-trivy.png)

### GitHub Actions — green run (root workflow)

![actions runs](screenshots/11-actions-runs.png)

![actions green UI](screenshots/08-actions-green-ui.png)

### Earlier captures

![pipeline](screenshots/01-pipeline.png)

![pytest old](screenshots/02-pytest.png)

## Evidence table

| Stage | Result | Log |
|---|---|---|
| Unit test | **3 passed** | `logs/03-pytest.txt` |
| SAST (Bandit) | No issues | `logs/04-bandit.txt` |
| SCA (pip-audit) | No known vulnerabilities | `logs/05-pip-audit.txt` |
| Secret scan | passed | `logs/06-secret-scan.txt` |
| Docker / HTTP | healthy + Hello HTML | `logs/08-health.txt`, `logs/09-home.txt` |
| Trivy | **Total: 0** | `logs/10-trivy.txt` |

GitHub Actions workflow runs the same stages end-to-end including GHCR push and kind deploy.
