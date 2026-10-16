# GitOps demo — Session 20

**Author:** Kushal S · **Enrollment:** 24bcs10355

## What is GitOps?

Git is the source of truth. Desired cluster state lives in Git as declarative YAML. A controller continuously reconciles the live cluster to match Git.

## Layout

```text
gitops/
├── README.md
├── deployment.yaml          # simple manual-apply demo (Task 3 baseline)
└── app/
    ├── deployment.yaml      # desired app state
    ├── service.yaml
    └── argocd-application.yaml   # Argo CD Application CR
```

## Workflow

```text
edit gitops/app/*.yaml
        |
        v
   git commit + push
        |
        v
Argo CD detects drift / change
        |
        v
 cluster matches Git (self-heal)
```

## Manual reconciliation (no Argo required)

```bash
kubectl apply -f app/deployment.yaml -f app/service.yaml
kubectl get deploy,svc,pods -l app=gitops-demo
```

## Argo CD path (controller-based)

Follow course lab `session20-monitoring-observability-gitops/07-argocd/README.md`:

1. Install Argo CD into a local cluster (kind / Minikube)
2. Update `repoURL` in `app/argocd-application.yaml`
3. `kubectl apply -f app/argocd-application.yaml -n argocd`
4. Change `replicas` in Git → Argo syncs automatically

## Ideas demonstrated

| Idea | Evidence |
|---|---|
| Git as source of truth | Manifests under `gitops/app/` |
| Declarative config | `replicas: 2` in Deployment |
| Continuous reconciliation | Argo `selfHeal: true` + automated sync |
| Kubernetes + GitOps | Application CR targets this path |
