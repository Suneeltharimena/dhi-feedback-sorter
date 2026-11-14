"""Run the whole test set and report score and cost"""

import importlib
import json


def test_scores_and_costs_a_run(replay, fixtures):
    """evaluate() gives the right scores and cost per 1,000 on the saved replies"""
    evaluate = importlib.import_module("evaluate")
    cases = [json.loads(line) for line in (fixtures / "comments.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    result = evaluate.evaluate(cases, replay, model="claude-opus-5-5")
    scores = result["scores"]
    assert scores["no_answer"] == 0.25, "2 of the 8 saved replies are a refusal and a cut-off: no_answer is 0.25."
    assert (scores["category"], scores["sentiment"]) == (0.5, 0.5), "On the saved replies category and sentiment are each 4 of 8 right."
    assert (scores["refund_requested"], scores["cafe"]) == (0.75, 0.75), "Refund and café are each 6 of 8 right."
    assert abs(result["cost_per_1000"] - 3.2115) < 1e-6, (
        f"Cost per 1,000 should be $3.2115 from the usage of all 8 calls, including the two with no answer; got {result['cost_per_1000']}."
    )
