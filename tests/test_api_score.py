from fraud_system.rules import evaluate_rules


def test_high_risk_score_reasons():
    transaction = {
        'amount': 9500,
        'merchant_category': 'crypto',
        'country': 'NG',
        'hour': 2,
        'customer_age_days': 3,
    }
    reasons = evaluate_rules(transaction)
    assert len(reasons) >= 3
    assert 'high_amount' in reasons
    assert 'high_risk_category' in reasons
