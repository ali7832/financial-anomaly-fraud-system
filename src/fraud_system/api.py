from fastapi import FastAPI

from fraud_system.model import FraudModel
from fraud_system.rules import evaluate_rules
from fraud_system.schemas import ScoreResponse, Transaction
from fraud_system.data import generate_transactions

app = FastAPI(title="Financial Fraud Detection API")

model = FraudModel()
model.fit(generate_transactions(500))


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/score", response_model=ScoreResponse)
def score(transaction: Transaction) -> ScoreResponse:
    payload = transaction.model_dump()

    risk_score = model.score(payload)
    reasons = evaluate_rules(payload)

    if reasons:
        risk_score = min(1.0, risk_score + 0.15 * len(reasons))

    return ScoreResponse(
        risk_score=round(risk_score, 4),
        is_suspicious=risk_score >= 0.5,
        reasons=reasons,
    )
