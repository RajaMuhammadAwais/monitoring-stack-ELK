# 📊 Monitoring Stack with ELK (Elasticsearch, Logstash, Kibana)

This project demonstrates how to set up centralized logging and monitoring using the ELK stack with Docker. It’s designed as a portfolio-friendly, easy-to-run environment that collects Docker container logs with Filebeat, ships them to Logstash, indexes them in Elasticsearch, and visualizes them in Kibana.

---

## 🚀 Project Goals

- Centralized logging using ELK stack
- Monitor logs from multiple services (via Docker)
- Visualize logs and create dashboards in Kibana
- Easy-to-deploy setup using Docker Compose
- Ready for GitHub with a CI workflow that validates the Compose config

---

## 🧰 Tools & Technologies

- Elasticsearch — log indexing & search engine
- Logstash — log collection & transformation
- Kibana — visualization & dashboards
- Filebeat — ships Docker container logs to Logstash
- Docker Compose — service orchestration
- GitHub Actions — CI: validate docker-compose config

---

## 🗂️ Repository Structure

- docker-compose.yml — ELK + Filebeat stack
- logstash/pipeline/logstash.conf — Logstash pipeline (Beats input → Elasticsearch)
- filebeat/filebeat.yml — Filebeat config to read Docker container logs
- sample-app/app.py — Small Python app that emits JSON logs
- sample-app/docker-compose.override.yml — Optional overlay to run the sample app
- .github/workflows/ci.yml — CI to validate Compose

---

## 🔧 Prerequisites

- Docker Desktop or Docker Engine + Docker Compose Plugin
- 4 GB+ RAM available to Docker
- Linux only: set vm.max_map_count (see Troubleshooting)

---

## ⚙️ Quick Start

1) Start ELK stack
```bash
docker compose up -d
```

2) (Optional) Run the sample app that emits logs
```bash
docker compose -f docker-compose.yml -f sample-app/docker-compose.override.yml up -d
```

3) Open Kibana
- URL: http://localhost:5601

4) Create a data view
- In Kibana: Stack Management → Data Views → Create data view
- Name: logs-*
- Timestamp field: @timestamp

5) Explore logs
- Kibana → Discover → Select data view logs-*

---

## 🧪 What’s Included

- Log parsing: Logstash attempts to parse JSON from the message field
- Container metadata: Filebeat adds Docker container metadata to events
- Indexing: Elasticsearch indexes into logs-YYYY.MM.dd
- CI: GitHub Actions validates Compose files on push/PR

---

## 🖥️ Stopping & Cleanup

- Stop services (keep data):
```bash
docker compose down
```

- Stop and remove data volume:
```bash
docker compose down -v
```

---

## 🔐 Security

For local demos this stack disables security for simplicity. If you plan to deploy or expose it:
- Enable xpack.security in Elasticsearch and Kibana
- Use credentials/API keys for Logstash → Elasticsearch
- Restrict network access to ports 9200/5601/5044

---

## 🛠️ Troubleshooting

- Linux: increase vm.max_map_count for Elasticsearch
```bash
sudo sysctl -w vm.max_map_count=262144
# make it persistent:
echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-elasticsearch.conf
sudo sysctl --system
```

- Not enough memory
  - Increase Docker Desktop resources or reduce ES_JAVA_OPTS in docker-compose.yml

- Filebeat permissions on macOS/Windows
  - Docker Desktop manages logs for containers; the provided mounts generally work.
  - If you hit issues, consider shipping via sidecars per service or run Filebeat with elevated access.

---

## ⬆️ Publish to GitHub

Initialize the repository and push:

Using GitHub CLI (recommended):
```bash
git init
git add .
git commit -m "Initial commit: ELK monitoring stack"
gh repo create your-username/monitoring-stack-elk --public --source=. --remote=origin --push
```

Manual (without GitHub CLI):
```bash
git init
git add .
git commit -m "Initial commit: ELK monitoring stack"
git branch -M main
git remote add origin https://github.com/your-username/monitoring-stack-elk.git
git push -u origin main
```

This repo ships with a CI workflow (.github/workflows/ci.yml) that verifies docker-compose.yml and the sample app overlay parse correctly.

---

## 📷 Dashboards

After data starts flowing, create your own dashboards in Kibana (Visualize → Dashboard). Add screenshots to your README or a docs/ folder to showcase your results.
