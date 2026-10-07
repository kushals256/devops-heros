# CoreDNS

## What it is

CoreDNS is the DNS server shipped with Kubernetes. It runs as a Deployment in `kube-system` and is exposed as the Service `kube-dns`.

## Why Kubernetes uses it

Pods and Services get new IPs. Applications should call a name (`backend`) instead of a Pod IP. CoreDNS is that cluster DNS.

## Service discovery

1. A Service is created.
2. The API server stores it.
3. CoreDNS watches Services and EndpointSlices.
4. A query for `backend.default.svc.cluster.local` returns the ClusterIP.
5. kube-proxy load-balances that IP to ready Pods.

Headless Services (`clusterIP: None`) return the Pod IPs instead of a virtual IP.

## How a query is resolved

The Pod’s `/etc/resolv.conf` points at `kube-dns` and lists search domains. A short name is tried against each search domain until one answers. `ndots:5` means a name with fewer than 5 dots is tried against the search list first.

## Configuration

The Corefile lives in the ConfigMap `coredns` in `kube-system`. The default Corefile loads the `kubernetes` plugin for `cluster.local`, forwards other names upstream, and caches answers.

## Troubleshooting DNS

```bash
kubectl get deploy -n kube-system coredns
kubectl logs -n kube-system deploy/coredns --tail=50
kubectl exec dns-check -- nslookup kubernetes.default.svc.cluster.local
```

Typical failures:

| Symptom | Likely cause |
|---|---|
| `nslookup` times out | CoreDNS Pods not Ready, or NetworkPolicy blocks UDP 53 |
| Name not found | Wrong namespace, or the Service does not exist |
| Resolved but connection refused | Service has no ready Endpoints |
| External names are slow | `ndots:5` tries cluster search domains first |

![CoreDNS Deployment](../../../DevOpsHomework-3/session-11/screenshots/05-coredns.png)

A live lookup from a Pod is in `DevOpsHomework-3/session-14/screenshots/15-dns.png`.
