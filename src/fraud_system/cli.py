from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console

from fraud_system.data import generate_transactions
from fraud_system.model import FraudModel
from fraud_system.rules import evaluate_rules

app = typer.Typer(help="Financial fraud detection command line tools")
console = Console()


@app.command()
def generate(output: Path = Path("transactions.json"), rows: int = 1000) -> None:
    """Generate synthetic financial transactions."""
    data = generate_transactions(rows)
    output.write_text(json.dumps(data, indent=2), encoding="utf-8")
    console.print(f"Generated {rows} transactions -> {output}")


@app.command()
def score(amount: float, merchant_category: str, country: str, hour: int, customer_age_days: int) -> None:
    """Score one transaction from CLI arguments."""
    model = FraudModel()
    model.fit(generate_transactions(500))
    row = {
        "amount": amount,
        "merchant_category": merchant_category,
        "country": country,
        "hour": hour,
        "customer_age_days": customer_age_days,
    }
    reasons = evaluate_rules(row)
    risk = model.score(row)
    if reasons:
        risk = min(1.0, risk + 0.15 * len(reasons))
    console.print_json(data={"risk_score": round(risk, 4), "is_suspicious": risk >= 0.5, "reasons": reasons})


@app.command()
def demo(rows: int = 1000) -> None:
    """Run a simple end-to-end demo."""
    data = generate_transactions(rows)
    model = FraudModel()
    model.fit(data)
    suspicious = 0
    for row in data[:100]:
        risk = model.score(row) + 0.15 * len(evaluate_rules(row))
        suspicious += risk >= 0.5
    console.print({"rows": rows, "sampled": 100, "suspicious_in_sample": suspicious})
