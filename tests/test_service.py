from fraud_system.schemas import Transaction
from fraud_system.service import FraudScoringService


def test_service_returns_enterprise_decision_metadata():
    transaction = Transaction(
        transaction_id='txn_001',
        customer_id='cust_001',
        amount=9500,
        merchant_category='crypto',
        country='NG',
        hour=2,
        customer_age_days=3,
    )

    response = FraudScoringService().score(transaction)

    assert response.decision_id
    assert response.model_version
    assert response.risk_tier in {'low', 'medium', 'high', 'critical'}
    assert response.is_suspicious is True
    assert 'high_amount' in response.reasons
