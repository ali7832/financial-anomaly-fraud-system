from __future__ import annotations

from pathlib import Path

import joblib

from fraud_system.model import FraudModel


def save_model(model: FraudModel, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, target)


def load_model(path: str | Path) -> FraudModel:
    return joblib.load(Path(path))
