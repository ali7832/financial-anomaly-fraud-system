from __future__ import annotations

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    amount: float = Field(..., ge=0)
    merchant_category: str
    country: str
    hour: int = Field(..., ge=0, le=23)
    customer_age_days: int = Field(..., ge=0)
    transaction_id: str | None = None
    customer_id: str | None = None


class ScoreResponse(BaseModel):
    risk_score: float
    risk_tier: str
    is_suspicious: bool
    reasons: list[str]
    model_version: str
    decision_id: str


class HealthResponse(BaseModel):
    status: str
    model_version: str
    environment: str
