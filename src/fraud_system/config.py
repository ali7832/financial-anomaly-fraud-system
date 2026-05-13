from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class FraudSettings:
    environment: str = os.getenv('FRAUD_ENV', 'local')
    suspicious_threshold: float = float(os.getenv('FRAUD_SUSPICIOUS_THRESHOLD', '0.50'))
    rule_weight: float = float(os.getenv('FRAUD_RULE_WEIGHT', '0.15'))
    model_training_rows: int = int(os.getenv('FRAUD_MODEL_TRAINING_ROWS', '800'))
    alert_store_path: str = os.getenv('FRAUD_ALERT_STORE_PATH', 'fraud_alerts.jsonl')
    model_version: str = os.getenv('FRAUD_MODEL_VERSION', 'iforest-baseline-v1')


settings = FraudSettings()
