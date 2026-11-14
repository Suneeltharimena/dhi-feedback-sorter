"""Score a run and price it"""

import importlib

CASES = [
    {"category": "drinks", "sentiment": "negative", "refund_requested": True, "cafe": "York"},
    {"category": "service", "sentiment": "positive", "refund_requested": False, "cafe": None},
    {"category": "price", "sentiment": "negative", "refund_requested": False, "cafe": "Leeds"},
    {"category": "food", "sentiment": "neutral", "refund_requested": False, "cafe": None},
]
OUTPUTS = [
    {"category": "drinks", "sentiment": "negative", "refund_requested": False, "cafe": "York"},
    {"category": "service", "sentiment": "neutral", "refund_requested": False, "cafe": None},
    None,
    {"category": "other", "sentiment": "neutral", "refund_requested": False, "cafe": None},
]


def _scoring():
    return importlib.import_module("scoring")


def test_scores_each_field():
    """score() gives the share right for each field"""
    result = _scoring().score(CASES, OUTPUTS)
    assert set(result) == {"category", "sentiment", "refund_requested", "cafe", "no_answer"}, "Return one share per field, plus no_answer."
    assert result["category"] == 0.5, f"Category is right for cases 1 and 2: 2 of 4 is 0.5, not {result['category']}."
    assert result["sentiment"] == 0.5, "Sentiment is right for cases 1 and 4: 0.5."
    assert result["cafe"] == 0.75, "Café is right for cases 1, 2 and 4: 0.75."


def test_no_answer_counted_apart():
    """A refused or cut-off call is right on no field and counted in no_answer"""
    result = _scoring().score(CASES, OUTPUTS)
    assert result["refund_requested"] == 0.5, "Case 3 gave no answer, so it is wrong on every field: refund is 2 of 4."
    assert result["no_answer"] == 0.25, "One of four calls gave no answer: no_answer is 0.25."


def test_cost_per_1000():
    """cost_per_1000() prices input and output tokens apart"""
    usages = [{"input_tokens": 600, "output_tokens": 300}, {"input_tokens": 640, "output_tokens": 260}]
    got = _scoring().cost_per_1000(usages, {"input": 4.00, "output": 20.00})
    assert abs(got - 8.08) < 1e-9, f"Average call: (620 × $4 + 280 × $20) / 1,000,000 = $0.00808; times 1,000 is $8.08, not {got}."
