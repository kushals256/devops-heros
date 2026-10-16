# Observability — Metrics, Logs, Traces

**Author:** Kushal S · **Enrollment:** 24bcs10355 · **Session:** 20

## Why observability is required

Monitoring answers “is a known signal bad?”  
Observability answers “why is this new failure happening?” using the telemetry you already collect.

## Metrics

Time-series numbers: CPU, memory, request rate, error rate, latency percentiles.

- **Tools:** Prometheus, Grafana, Datadog, CloudWatch
- **Kubernetes:** metrics-server, kube-state-metrics, ServiceMonitor/PodMonitor

## Logs

Discrete events with timestamps and messages.

- **Tools:** Loki, Elasticsearch/OpenSearch, Fluent Bit, CloudWatch Logs
- **Kubernetes:** `kubectl logs`, node journal, sidecar agents

## Traces

A single request’s path across services as a tree of spans.

- **Tools:** OpenTelemetry, Jaeger, Tempo, Zipkin
- **Kubernetes:** OTel Collector DaemonSet / sidecars

## How the three work together

```text
Alert fires on high latency (metric)
        → find error lines for that window (logs)
        → open the slow trace and find the slow span (traces)
```

## This homework’s live demo

Prometheus + Grafana compose under `../monitoring/` scrapes metrics and loads alert rules.  
Traces are documented here; a full Jaeger stack is optional beyond the course Minikube lab.
