# FQDN

## What is an FQDN?

A fully qualified domain name is a complete name that does not depend on a search suffix. `kubernetes.default.svc.cluster.local` is an FQDN. `kubernetes` is a short name.

## Kubernetes Service DNS

CoreDNS gives every Service a name in the cluster. Pods use the nameserver in `/etc/resolv.conf` (the `kube-dns` Service, usually `10.96.0.10`).

## Naming convention

```text
<service>.<namespace>.svc.<cluster-domain>
```

The cluster domain is `cluster.local` unless the cluster was installed with another one.

## Namespace-based DNS

| From a Pod in `default` | Resolves |
|---|---|
| `kubernetes` | `kubernetes.default.svc.cluster.local` via the search list |
| `kubernetes.default` | same Service |
| `kubernetes.kube-system` | the Service in another namespace |
| `kube-dns.kube-system.svc.cluster.local` | CoreDNS itself |

The search list is typically:

```text
default.svc.cluster.local
svc.cluster.local
cluster.local
```

## Pod-to-Service communication

A Pod calls `http://web-service.production-webapp.svc.cluster.local`. CoreDNS returns the Service ClusterIP. kube-proxy sends the packet to a ready Pod selected by the Service.

## Examples

```text
kubernetes.default.svc.cluster.local
web-service.production-webapp.svc.cluster.local
notes-notes.default.svc.cluster.local
web-stateful-0.web-headless.default.svc.cluster.local
```

The last form is a StatefulSet Pod behind a headless Service: the FQDN returns that Pod’s IP, not a virtual IP.

![CoreDNS Service](../../../DevOpsHomework-3/session-11/screenshots/04-dns.png)
