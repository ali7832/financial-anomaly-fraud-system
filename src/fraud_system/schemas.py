from pydantic import BaseModel


class Transaction(BaseModel):
    amount: float
    merchant_category: str
    country: str
    hour: int
    customer_age_days: int


class ScoreResponse(BaseModel):
    risk_score: float
    is_suspicious: bool
    reasons: list[str]
