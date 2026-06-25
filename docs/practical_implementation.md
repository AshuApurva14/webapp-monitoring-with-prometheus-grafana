ure, let’s walk through how you would add the observability stack to a concrete application running in your Kubernetes cluster.

1. Instrument the application

Add the OpenTelemetry SDK for your language (for example, opentelemetry‑java‑instrumentation or opentelemetry‑python) and wrap the HTTP handlers, database calls, and any external APIs.
Export spans and metrics to the OpenTelemetry Collector endpoint (http://otel-collector.monitoring.svc:4317).
2. Deploy the collector

bash


helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install otel-collector grafana/otel-collector \
 --set mode=daemonset \
 --namespace monitoring \
 --create-namespace \
 -f values.yaml # configure receivers, processors, and exporters
In values.yaml enable the Prometheus receiver, the Jaeger exporter (or Tempo), and the Loki exporter for logs.

3. Add Prometheus scrape config Create a ServiceMonitor for your app:

yaml


apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
 name: myapp-monitor
 labels:
 release: prometheus
spec:
 selector:
 matchLabels:
 app: myapp
 endpoints:
 - port: metrics
 path: /metrics
 interval: 30s
Make sure your pod exposes a /metrics endpoint (Prometheus client library).

4. Deploy Loki for log aggregation

bash


helm install loki grafana/loki-stack \
 --namespace monitoring \
 --set fluent-bit.enabled=true \
 --set fluent-bit.backend.type=loki
Configure Fluent Bit to add Kubernetes metadata (kubernetes.namespace_name, kubernetes.pod_name) so you can correlate logs with traces.

5. Deploy Grafana dashboards

bash


helm install grafana grafana/grafana \
 --namespace monitoring \
 --set datasources.datasource.yaml.apiVersion=1 \
 --set datasources.datasource.yaml.datasources.type=prometheus \
 --set datasources.datasource.yaml.datasources.url=http://prometheus-server.monitoring.svc:9090 \
 --set datasources.datasource.yaml.datasources.type=loki \
 --set datasources.datasource.yaml.datasources.url=http://loki.monitoring.svc:3100
Import a dashboard that shows request rate, latency percentiles, CPU/memory per pod, and a panel that links to Tempo traces.

6. Configure alerts In alertmanager.yaml add rules such as:

yaml


groups:
- name: myapp-alerts
 rules:
 - alert: HighLatency
 expr: histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{job="myapp"})) by (le)) > 0.3
 for: 2m
 labels:
 severity: critical
 annotations:
 summary: "99th‑percentile latency > 300 ms"
 runbook: "https://runbooks.example.com/myapp-latency"
Route alerts to Slack or PagerDuty.

7. Autoscaling Create an HPA that scales on custom metrics:

yaml


apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
 name: myapp-hpa
spec:
 scaleTargetRef:
 apiVersion: apps/v1
 kind: Deployment
 name: myapp
 minReplicas: 3
 maxReplicas: 30
 metrics:
 - type: Pods
 pods:
 metric:
 name: http_requests_per_second
 target:
 type: AverageValue
 averageValue: "100"
Enable the Cluster Autoscaler on your node pool so new nodes are provisioned when needed.

8. Security and RBAC Give the collector a dedicated ServiceAccount with only the metrics.k8s.io and pods read permissions it needs. Use NetworkPolicies to limit inbound traffic to the collector.

9. CI/CD integration Add a step in your pipeline that validates the OpenTelemetry config (otelcol --dry-run) and runs unit tests for the instrumentation code before merging.

That gives you a production‑ready observability pipeline for a specific app.

Now to keep the conversation moving: which part of this setup do you feel most comfortable tackling first—instrumenting the code, deploying the collector, or configuring alerts?
