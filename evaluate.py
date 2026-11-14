"""Run the sorter over a set of labelled comments and report score and cost.

    python evaluate.py cases.jsonl      a real run: needs ANTHROPIC_API_KEY and costs money
"""

import json
import sys

from scoring import cost_per_1000, score
from sorter import MODEL, sort_comment

# Dollars per million tokens, read from platform.claude.com/docs/en/about-claude/pricing in October 2026.
PRICES = {
    "claude-opus-5-5": {"input": 4.00, "output": 20.00},
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
}


def load(path):
    with open(path, encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def evaluate(cases, client, model=MODEL):
    """Step 4: sort every case's "text", then return {"scores": ..., "cost_per_1000": ...}.

    Use score() on the outputs (each a dictionary, or None) and cost_per_1000() on the usages
    (each {"input_tokens": ..., "output_tokens": ...}) at PRICES[model].
    """
    raise NotImplementedError("Step 4: write evaluate")


if __name__ == "__main__":
    import anthropic

    result = evaluate(load(sys.argv[1]), anthropic.Anthropic())
    print(json.dumps(result, indent=2))
