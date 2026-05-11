# Financial Anomaly Detection & Fraud System

Production-ready ML platform for detecting suspicious financial transactions in near real time. It combines synthetic transaction generation, feature engineering, deterministic fraud rules, Isolation Forest anomaly detection, risk scoring, SQLite alert persistence, FastAPI APIs, CLI workflows, Docker, CI, and tests.

## Features

- Synthetic transaction generator with realistic fraud patterns
- Explainable fraud rules for amount, country, merchant, odd-hour, and new-customer risk
- Isolation Forest anomaly model
- Hybrid risk score combining model and rules
- FastAPI service for scoring and alert review
- CLI for generate/train/evaluate/score/demo
- SQLite persistence
- Docker and docker-compose
- GitHub Actions CI
- Pytest coverage

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
fraudctl demo --rows 1000
pytest -q
uvicorn fraud_system.api.main:app --reload
```

## API

```bash
curl -X POST http://localhost:8000/score \
  -H "Content-Type: application/json" \
  -d '{"amount":9500,"merchant_category":"crypto","country":"NG","hour":2,"customer_age_days":3}'
```

## Architecture

```text
Synthetic Data -> Feature Builder -> Rules Engine
                         |              |
                         v              v
                  Isolation Forest -> Risk Scorer -> SQLite Alerts
                                                   |
                                                   v
                                             FastAPI / CLI
```

## Portfolio talking points

- Built an end-to-end fraud detection platform with real-time scoring interfaces.
- Combined unsupervised ML with deterministic rules for explainability.
- Implemented data generation, model training, evaluation, API serving, CLI, Docker, CI, and tests.
