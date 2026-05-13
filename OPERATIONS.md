# Operations Runbook

## Runtime Configuration

The service is controlled through environment variables in `.env.example`.

Important values:

- `FRAUD_SUSPICIOUS_THRESHOLD`: minimum score that marks a transaction suspicious.
- `FRAUD_RULE_WEIGHT`: contribution added per deterministic fraud rule.
- `FRAUD_MODEL_VERSION`: model identifier returned in every decision.
- `FRAUD_ALERT_STORE_PATH`: JSONL file where suspicious decisions are written.

## Alert Lifecycle

1. Transaction is scored through `/score`.
2. Model and rule signals are combined.
3. A risk tier is assigned.
4. Suspicious decisions are written as JSONL audit events.
5. Downstream teams can ingest this stream into SIEM, dashboards, or case-management systems.

## Risk Tiers

- `low`: routine transaction
- `medium`: monitor or sample-review
- `high`: suspicious transaction requiring review
- `critical`: immediate fraud operations escalation

## Production Hardening Roadmap

- Replace JSONL alert storage with PostgreSQL or Kafka.
- Add Prometheus metrics and Grafana dashboards.
- Add model registry integration.
- Add feature store integration.
- Add batch retraining and drift monitoring.
- Add RBAC, audit retention, and case review workflow.
