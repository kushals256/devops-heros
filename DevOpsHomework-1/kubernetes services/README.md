# Kubernetes Services — ClusterIP Homework

**Name:** Kushal S  
**Enrollment number:** 24bcs10355

**Manifests:** `session-11-kubernetes-services/01-clusterip/`

---

## Prerequisites

```bash
colima start
minikube start --driver=docker
kubectl cluster-info
```

---

## Task: Deploy ClusterIP Service and test internal access

### Step 1 — Deploy nginx backend (3 replicas)

```bash
cd session-11-kubernetes-services/01-clusterip
kubectl apply -f app-deployment.yaml
kubectl get pods -l app=web-clusterip -o wide
```

Output:

```text
NAME                                 READY   STATUS    RESTARTS   AGE   IP           NODE
web-app-clusterip-66865d4855-2wg5c   1/1     Running   0          19s   10.244.0.4   minikube
web-app-clusterip-66865d4855-5mzhm   1/1     Running   0          19s   10.244.0.3   minikube
web-app-clusterip-66865d4855-h89jk   1/1     Running   0          19s   10.244.0.5   minikube
```

### Step 2 — Create ClusterIP service

```bash
kubectl apply -f service.yaml
kubectl get svc web-service-clusterip
kubectl get endpoints web-service-clusterip
```

Output:

```text
NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
web-service-clusterip   ClusterIP   10.105.180.204   <none>        8080/TCP   0s

NAME                    ENDPOINTS
web-service-clusterip   10.244.0.3:80,10.244.0.4:80,10.244.0.5:80
```

### Step 3 — Deploy curl client pod and test

```bash
kubectl apply -f client-pod.yaml
kubectl exec curl-client -- curl -s http://web-service-clusterip:8080 | head -5
kubectl exec curl-client -- curl -s http://web-service-clusterip.default.svc.cluster.local:8080 | head -5
```

Output (nginx welcome page):

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
```

### Step 4 — Verify all resources

```bash
kubectl get all
```

Output:

```text
NAME                                     READY   STATUS    RESTARTS   AGE
pod/curl-client                          1/1     Running   0          22s
pod/web-app-clusterip-66865d4855-2wg5c   1/1     Running   0          41s
pod/web-app-clusterip-66865d4855-5mzhm   1/1     Running   0          41s
pod/web-app-clusterip-66865d4855-h89jk   1/1     Running   0          41s

NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes              ClusterIP   10.96.0.1        <none>        443/TCP    6d23h
service/web-service-clusterip   ClusterIP   10.105.180.204   <none>        8080/TCP   22s

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/web-app-clusterip   3/3     3            3           41s
```

### Cleanup

```bash
kubectl delete all --all
```

---

## What we learned

- **ClusterIP** is the default service type — internal-only, not reachable from outside the cluster.
- The service gets a stable virtual IP and DNS name (`web-service-clusterip`).
- `port: 8080` is the service port; `targetPort: 80` is the container port.
- A client pod inside the cluster can reach the service by name, FQDN, or ClusterIP.
- Endpoints list all pod IPs behind the service (load balancing via kube-proxy).
