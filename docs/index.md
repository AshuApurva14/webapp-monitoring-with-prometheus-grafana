---
icon: lucide/rocket
---

# Webapp Monitoring with Prometheus & Grafana

This repository demonstrates how to monitor a web application using Prometheus (metrics collection) and Grafana (visualization). It includes example scrape configurations, a sample dashboard, and instructions to run locally.

## Overview

- Instrument a webapp to expose Prometheus metrics at /metrics.
- Use Prometheus to scrape metrics from the webapp and other exporters.
- Visualize metrics and create alerts in Grafana.

## Prerequisites

- Docker & docker-compose (or Kubernetes)
- git
- A browser to view Grafana dashboards

## Quickstart (Docker)

1. Clone the repo
   - git clone <repo-url>

2. Start services
   - docker-compose up -d

3. Application & services
   - Webapp: http://localhost:8080 (example)
   - Metrics endpoint: http://localhost:8080/metrics
   - Prometheus UI: http://localhost:9090
   - Grafana: http://localhost:3000 (default admin/admin)

4. Import dashboards
   - Open Grafana → Dashboards → Import → upload JSON or paste dashboard ID from /dashboards/

## Prometheus basics

- Edit prometheus.yml to configure scrape targets and job labels.
- Common scrape config example:
  - job_name: 'webapp'
  - static_configs: targets: ['webapp:8080']

- Reload Prometheus after changing config: POST to /-/reload or restart container.

## Grafana tips

- Add Prometheus as a data source (URL: http://prometheus:9090 in compose).
- Import provided dashboards or create panels with PromQL queries.
- Example PromQL:
  - rate(http_requests_total[5m])
  - node_cpu_seconds_total (for node exporter)

## Alerts

- Define alerting rules in Prometheus (rules files) and configure Alertmanager.
- Route alerts to email, Slack, or other integrations via Alertmanager.

## Files of interest

- docker-compose.yml — quick local environment
- prometheus/prometheus.yml — scrape config & rule files
- grafana/dashboards/ — exported dashboard JSON
- webapp/ — example instrumented application
- README.md — repo-level details

## Development & Testing

- Run the webapp locally and curl /metrics to confirm metrics output.
- Use Prometheus expression browser to validate metrics and queries.
- Use Grafana to create, save, and share dashboards.

## Resources

- Prometheus docs: https://prometheus.io/docs/
- Grafana docs: https://grafana.com/docs/
- Prometheus metrics best practices: https://prometheus.io/docs/practices/naming/

## Contributing

Contributions are welcome: open issues or submit PRs for missing dashboards, improved examples, or bug fixes.

```// filepath: /workspaces/webapp-monitoring-with-prometheus-grafana/docs/index.md
---
icon: lucide/rocket
---

# Webapp Monitoring with Prometheus & Grafana

This repository demonstrates how to monitor a web application using Prometheus (metrics collection) and Grafana (visualization). It includes example scrape configurations, a sample dashboard, and instructions to run locally.

## Overview

- Instrument a webapp to expose Prometheus metrics at /metrics.
- Use Prometheus to scrape metrics from the webapp and other exporters.
- Visualize metrics and create alerts in Grafana.

## Prerequisites

- Docker & docker-compose (or Kubernetes)
- git
- A browser to view Grafana dashboards

## Quickstart (Docker)

1. Clone the repo
   - git clone <repo-url>

2. Start services
   - docker-compose up -d

3. Application & services
   - Webapp: http://localhost:8080 (example)
   - Metrics endpoint: http://localhost:8080/metrics
   - Prometheus UI: http://localhost:9090
   - Grafana: http://localhost:3000 (default admin/admin)

4. Import dashboards
   - Open Grafana → Dashboards → Import → upload JSON or paste dashboard ID from /dashboards/

## Prometheus basics

- Edit prometheus.yml to configure scrape targets and job labels.
- Common scrape config example:
  - job_name: 'webapp'
  - static_configs: targets: ['webapp:8080']

- Reload Prometheus after changing config: POST to /-/reload or restart container.

## Grafana tips

- Add Prometheus as a data source (URL: http://prometheus:9090 in compose).
- Import provided dashboards or create panels with PromQL queries.
- Example PromQL:
  - rate(http_requests_total[5m])
  - node_cpu_seconds_total (for node exporter)

## Alerts

- Define alerting rules in Prometheus (rules files) and configure Alertmanager.
- Route alerts to email, Slack, or other integrations via Alertmanager.

## Files of interest

- docker-compose.yml — quick local environment
- prometheus/prometheus.yml — scrape config & rule files
- grafana/dashboards/ — exported dashboard JSON
- webapp/ — example instrumented application
- README.md — repo-level details

## Development & Testing

- Run the webapp locally and curl /metrics to confirm metrics output.
- Use Prometheus expression browser to validate metrics and queries.
- Use Grafana to create, save, and share dashboards.

## Resources

- Prometheus docs: https://prometheus.io/docs/
- Grafana docs: https://grafana.com/docs/
- Prometheus metrics best practices: https://prometheus.io/docs/practices/naming/

## Contributing

Contributions are welcome: open issues or submit PRs for missing dashboards, improved examples, or bug fixes.
