from __future__ import annotations

import random

COUNTRIES = ["US", "UK", "DE", "PK", "NG"]
CATEGORIES = ["retail", "travel", "crypto", "food", "gift_cards"]


def generate_transactions(rows: int = 1000) -> list[dict]:
    data = []

    for _ in range(rows):
        amount = round(random.uniform(10, 12000), 2)
        category = random.choice(CATEGORIES)
        country = random.choice(COUNTRIES)
        hour = random.randint(0, 23)
        customer_age_days = random.randint(1, 1000)

        data.append(
            {
                "amount": amount,
                "merchant_category": category,
                "country": country,
                "hour": hour,
                "customer_age_days": customer_age_days,
            }
        )

    return data
