# Kubernetes object comparison

## Deployment vs ReplicaSet

| | ReplicaSet | Deployment |
|---|---|---|
| Purpose | Keep N Pods running that match a label selector | Declare a desired app version and manage ReplicaSets for you |
| Pod management | Creates or deletes Pods until the count matches | Creates a new ReplicaSet for each change of the Pod template |
| Scaling | `spec.replicas` | `spec.replicas`, which it copies onto the current ReplicaSet |
| Rolling updates | No built-in strategy | `RollingUpdate` or `Recreate` |
| Relationship | Lower-level controller | Owns one or more ReplicaSets. You edit the Deployment. You do not edit the ReplicaSet by hand |

A Deployment named `web` with 3 replicas creates a ReplicaSet like `web-7d8f9c`. That ReplicaSet owns the Pods. A new image creates a second ReplicaSet and scales the old one down.

## Deployment vs DaemonSet vs StatefulSet

| | Deployment | DaemonSet | StatefulSet |
|---|---|---|---|
| Use case | Stateless APIs, web frontends | One agent per node (logs, CNI, monitoring) | Databases, queues, anything that needs a stable name |
| Pod creation | Parallel, random suffix | One Pod per matching node | Ordered: `app-0`, then `app-1` |
| Scaling | Any replica count | Scales when nodes join or leave | Scale by ordinal |
| Networking | Usually behind a ClusterIP Service | Often no Service, or a normal Service | Headless Service so each Pod has a DNS name |
| Storage | Shared or emptyDir | hostPath is common | One PVC per ordinal |
| Example | nginx frontend | node exporter | Postgres, Kafka |

## ReplicaSet vs Service

| | ReplicaSet | Service |
|---|---|---|
| Responsibility | How many Pods exist and that they stay up | A stable virtual IP and DNS name in front of those Pods |
| What it selects | Pods to create from a template | Existing Pods by label |
| Why both | Pods die and get new IPs. A ReplicaSet replaces them. A Service finds the current ones through Endpoints / EndpointSlices |
| Traffic path | Client → Service ClusterIP → kube-proxy rules → Pod IP:port |

A ReplicaSet does not route traffic. A Service does not restart crashed Pods. An app needs both when callers must survive Pod replacement.

`kubectl explain` output from this cluster is in `DevOpsHomework-3/session-11/`.
