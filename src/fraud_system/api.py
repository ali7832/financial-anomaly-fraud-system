from fastapi import FastAPI

from fraud_system.config import settings
from fraud_system.schemas import HealthResponse, ScoreResponse, Transaction
from fraud_system.service import FraudScoringService

app = FastAPI(
    title='Financial Fraud Detection API',
    description='Enterprise-grade fraud scoring API with configurable thresholds, risk tiers, and audit alerts.',
    version='0.2.0',
)

_service = FraudScoringService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status='ok',
        model_version=settings.model_version,
        environment=settings.environment,
    )


@app.post('/score', response_model=ScoreResponse)
def score(transaction: Transaction) -> ScoreResponse:
    return _service.score(transaction)
