from __future__ import annotations

import numpy as np
from sklearn.ensemble import IsolationForest


FEATURES = [
    "amount",
    "hour",
    "customer_age_days",
]


class FraudModel:
    def __init__(self) -> None:
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.05,
            random_state=42,
        )

    def fit(self, rows: list[dict]) -> None:
        matrix = np.array([[r[f] for f in FEATURES] for r in rows])
        self.model.fit(matrix)

    def score(self, row: dict) -> float:
        matrix = np.array([[row[f] for f in FEATURES]])
        raw = self.model.decision_function(matrix)[0]
        risk = float(max(0.0, min(1.0, (0.5 - raw))))
        return round(risk, 4)
