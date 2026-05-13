# ADR-001: Hybrid Fraud Scoring Architecture

## Status

Accepted

## Context

Financial fraud detection needs both adaptive anomaly detection and explainable business rules. Pure ML models can detect unusual behavior but are difficult for fraud analysts to audit. Pure rules are explainable but brittle and easy to bypass.

## Decision

Use a hybrid scoring system:

- Isolation Forest provides anomaly scoring.
- Deterministic rules capture known fraud patterns.
- Configurable rule weights adjust operational sensitivity.
- Every suspicious decision includes reasons, risk tier, model version, and decision ID.
- Suspicious events are written to an audit stream.

## Consequences

Benefits:

- More explainable fraud decisions.
- Easier analyst review.
- Simple production rollout path.
- Configurable risk thresholding.

Tradeoffs:

- Rule tuning requires operational feedback.
- JSONL audit storage is suitable for local/demo deployment but should be replaced by Kafka or a database in production.
