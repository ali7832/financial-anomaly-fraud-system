# System Architecture

## Components

- FastAPI scoring service
- Isolation Forest anomaly engine
- Rule-based fraud detection
- Synthetic transaction generator
- CLI tooling
- Docker deployment stack
- CI pipeline

## Request Flow

1. Transaction received
2. Rules engine evaluates deterministic risks
3. Isolation Forest computes anomaly score
4. Hybrid risk score generated
5. API returns fraud assessment

## Production Extensions

- PostgreSQL alert persistence
- Kafka event ingestion
- Redis caching
- Prometheus/Grafana monitoring
- Kubernetes deployment
