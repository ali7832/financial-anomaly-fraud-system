# Financial Anomaly Detection & Fraud System

Production-ready ML platform for detecting suspicious financial transactions in near real time.

## Features

- FastAPI scoring API
- Isolation Forest anomaly detection
- Hybrid fraud rules engine
- Synthetic transaction generation
- CLI workflows
- Docker + Docker Compose
- GitHub Actions CI
- Pytest coverage
- Deployment documentation
- Model persistence utilities

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

## Architecture

See: `docs/architecture.md`

## Deployment

See: `docs/deployment.md`

## Portfolio Highlights

- End-to-end ML fraud detection platform
- Real-time scoring architecture
- Production-ready deployment stack
- CI/CD enabled
- Recruiter/interview friendly structure
