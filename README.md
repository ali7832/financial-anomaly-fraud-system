# Financial Anomaly Detection & Fraud System

Enterprise-style fraud risk platform for near real-time transaction scoring, anomaly detection, rule-based fraud explainability, audit logging, and operational risk review.

## What This System Demonstrates

This repository is structured as a stakeholder-facing fraud platform rather than a single notebook or script. It separates runtime configuration, scoring services, deterministic rules, anomaly models, API routes, audit events, tests, Docker deployment, and operational runbooks.

## Core Capabilities

- FastAPI transaction scoring API
- Isolation Forest anomaly detection baseline
- Hybrid fraud rules engine for explainable decisions
- Configurable scoring thresholds and rule weights
- Enterprise response metadata: decision ID, model version, risk tier, and reasons
- JSONL suspicious-decision audit stream
- Model persistence utilities
- Synthetic transaction generation for repeatable local testing
- CLI workflows for demo and scoring
- Docker + Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
uvicorn fraud_system.api:app --reload
```

## Docker

```bash
docker-compose up --build
```

## CLI

```bash
fraudctl demo --rows 1000
fraudctl score --amount 9500 --merchant-category crypto --country NG --hour 2 --customer-age-days 3
```

## Example API Request

```bash
curl -X POST http://localhost:8000/score \
  -H 'Content-Type: application/json' \
  -d @examples/sample_transaction.json
```

## Runtime Configuration

See `.env.example` for configurable thresholds, model version, training rows, and audit stream path.

## Documentation

- `docs/architecture.md`
- `docs/deployment.md`
- `docs/adr-001-hybrid-fraud-scoring.md`
- `OPERATIONS.md`

## Production Extension Roadmap

- PostgreSQL or Kafka-backed alert storage
- Fraud analyst case-review workflow
- Feature store integration
- Model registry and drift monitoring
- Prometheus/Grafana operational dashboards
- RBAC and audit retention controls

## Portfolio Highlights

- Demonstrates ML system design beyond model training
- Shows API, service-layer, configuration, audit, and operations patterns
- Strong fit for fintech, risk, fraud, MLOps, and backend ML platform roles
