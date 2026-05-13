from __future__ import annotations

from uuid import uuid4

from fraud_system.audit import write_audit_event
from fraud_system.config import settings
from fraud_system.data import generate_transactions
from fraud_system.model import FraudModel
from fraud_system.rules import evaluate_rules
from fraud_system.schemas import ScoreResponse, Transaction


class FraudScoringService:
    def __init__(self) -> None:
        self.model = FraudModel()
        self.model.fit(generate_transactions(settings.model_training_rows))

    def score(self, transaction: Transaction) -> ScoreResponse:
        payload = transaction.model_dump()
        reasons = evaluate_rules(payload)
        model_score = self.model.score(payload)
        risk_score = min(1.0, model_score + settings.rule_weight * len(reasons))
        risk_score = round(risk_score, 4)
        risk_tier = self._tier(risk_score)
        decision_id = str(uuid4())

        response = ScoreResponse(
            risk_score=risk_score,
            risk_tier=risk_tier,
            is_suspicious=risk_score >= settings.suspicious_threshold,
            reasons=reasons,
            model_version=settings.model_version,
            decision_id=decision_id,
        )

        if response.is_suspicious:
            write_audit_event(
                {
                    'event_type': 'fraud_alert_created',
                    'decision_id': decision_id,
                    'transaction': payload,
                    'response': response.model_dump(),
                },
                settings.alert_store_path,
            )

        return response

    @staticmethod
    def _tier(score: float) -> str:
        if score >= 0.75:
            return 'critical'
        if score >= 0.50:
            return 'high'
        if score >= 0.25:
            return 'medium'
        return 'low'
