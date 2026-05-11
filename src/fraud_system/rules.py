HIGH_RISK_COUNTRIES = {"NG", "RU", "KP"}
HIGH_RISK_CATEGORIES = {"crypto", "gift_cards"}


def evaluate_rules(transaction: dict) -> list[str]:
    reasons = []

    if transaction["amount"] > 5000:
        reasons.append("high_amount")

    if transaction["country"] in HIGH_RISK_COUNTRIES:
        reasons.append("high_risk_country")

    if transaction["merchant_category"] in HIGH_RISK_CATEGORIES:
        reasons.append("high_risk_category")

    if transaction["hour"] < 5:
        reasons.append("odd_hour_activity")

    if transaction["customer_age_days"] < 7:
        reasons.append("new_customer")

    return reasons
