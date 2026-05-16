# Financial Anomaly Detection & Fraud System

Enterprise fraud risk platform for near real-time transaction scoring, anomaly detection, rule-based fraud explainability, audit logging, and operational risk review.

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
- React/Vite fraud analyst command center frontend

## Quickstart

```bash
pip install .[dev]
uvicorn fraud_system.api:app --reload
```

## Frontend Dashboard

The `frontend/` app is a premium React/Vite command center for fraud analysts and risk leaders.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

The dashboard includes:

- executive KPI cards
- interactive transaction scoring simulator
- fallback scoring mode when the API is offline
- model decision explainability panel
- analyst review queue
- enterprise command-center styling

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
