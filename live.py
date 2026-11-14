"""python grade.py --live: one real run of your sorter on the saved comments, with your own key."""

import json
from pathlib import Path


def main():
    import anthropic

    from evaluate import PRICES, evaluate
    from sorter import MODEL

    cases = [json.loads(line) for line in (Path(__file__).parent / "fixtures" / "comments.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    result = evaluate(cases, anthropic.Anthropic(), model=MODEL)
    fields = [value for key, value in result["scores"].items() if key != "no_answer"]
    return {
        "cases": len(cases),
        "model": MODEL,
        "score": sum(fields) / len(fields),
        "cost_usd": result["cost_per_1000"] * len(cases) / 1000,
        "prices_as_of": "October 2026",
    }
