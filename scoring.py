"""Score a run and price it."""

FIELDS = ("category", "sentiment", "refund_requested", "cafe")


def score(cases, outputs):
    """Step 2: the share of all cases right for each field in FIELDS, plus "no_answer".

    outputs[i] is the answer for cases[i] as a dictionary, or None if the call was refused or cut off.
    A None output is right on no field.
    """
    raise NotImplementedError("Step 2: write score")


def cost_per_1000(usages, price):
    """Step 2: the average cost of one call in dollars, times 1,000. `price` is dollars per million tokens."""
    raise NotImplementedError("Step 2: write cost_per_1000")
