# Kubernetes volumes

## emptyDir

An emptyDir volume is created when a Pod is scheduled and deleted when that Pod is deleted. Containers in the same Pod can share it. It is a scratch space, not a database.

Applied `session-13-storage-hpa-probes/01-volumes/emptydir-pod.yaml` (`emptydir-demo`). Writing `/data/note.txt` inside the container succeeded.

![emptyDir write](../screenshots/02-emptydir-exec.png)

## hostPath

A hostPath volume mounts a file or directory from the node into the Pod. `hostpath-demo` mounts `/tmp/hostpath-data`. The data survives a container restart on that same node and disappears if the Pod is scheduled onto another node. It is useful for node agents, not for portable app data.

## PersistentVolume

A PersistentVolume is cluster storage that exists outside the Pod lifecycle. The course manifest `student-pv` is a 1Gi hostPath volume with reclaim policy Retain. A PVC only binds to it when `storageClassName` is empty (or matches) and the size and access mode fit. Binding it explicitly:

```yaml
storageClassName: ""
volumeName: student-pv
```

That PVC is `student-static-pvc`. After apply, `student-pv` status is Bound.

![static PV](../screenshots/12-static-pv.png)

## PersistentVolumeClaim

A PVC is the Pod’s request for storage. The Pod references the claim, not the volume. `student-pvc` from the course (no `storageClassName`) was filled in with the default class `standard` and bound to a dynamically created PV.

## StorageClass

A StorageClass is a named provisioner. On Minikube the default class is `standard` (`k8s.io/minikube-hostpath`). A PVC that names that class, or omits the class when it is the default, does not need a pre-created PV.

## Dynamic provisioning

`dynamic-pvc` from `03-storageclass/pvc.yaml` went Bound to a PV named `pvc-<uid>` that the storage provisioner created. That is dynamic provisioning: the claim creates the volume.

![PV and PVC](../screenshots/03-pv-pvc.png)

![Pods](../screenshots/01-volumes.png)

![Static PVC bound to student-pv](../screenshots/13-static-pvc.png)

