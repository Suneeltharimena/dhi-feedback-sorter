"""Label your test set before you write a prompt"""

import json

FIELDS = {
    "category": {"drinks", "food", "service", "cleanliness", "price", "other"},
    "sentiment": {"positive", "neutral", "negative"},
}


def _load(path):
    assert path.exists(), f"{path.name} is missing. Create it next to grade.py."
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                raise AssertionError(f"{path.name} line {number} is not valid JSON. Each line is one labelled comment.") from None
    return rows


def _check_rows(name, rows):
    for number, row in enumerate(rows, 1):
        assert isinstance(row.get("text"), str) and row["text"].strip(), f"{name} line {number} needs a \"text\"."
        for field, allowed in FIELDS.items():
            assert row.get(field) in allowed, f"{name} line {number}: {field} must be one of {sorted(allowed)}."
        assert isinstance(row.get("refund_requested"), bool), f"{name} line {number}: refund_requested must be true or false."
        assert row.get("cafe") is None or isinstance(row["cafe"], str), f"{name} line {number}: cafe is a name or null."


def test_at_least_30_labelled_cases(src):
    """cases.jsonl holds at least 30 labelled comments"""
    rows = _load(src / "cases.jsonl")
    _check_rows("cases.jsonl", rows)
    assert len(rows) >= 30, f"cases.jsonl has {len(rows)} labelled comments. Label at least 30 by hand."


def test_awkward_cases_included(src):
    """The test set includes awkward cases: every category, no café named, and a refund"""
    rows = _load(src / "cases.jsonl")
    missing = FIELDS["category"] - {row.get("category") for row in rows}
    assert not missing, f"No case has the category {', '.join(sorted(missing))}. Add at least one of each."
    assert any(row.get("cafe") is None for row in rows), "Add cases that name no café (cafe: null)."
    assert any(row.get("refund_requested") is True for row in rows), "Add at least one case that asks for a refund."


def test_holdout_kept_apart(src):
    """holdout.jsonl holds 10 comments that are not in cases.jsonl"""
    rows = _load(src / "holdout.jsonl")
    _check_rows("holdout.jsonl", rows)
    assert len(rows) == 10, f"holdout.jsonl has {len(rows)} comments. Move exactly 10 there, chosen at random."
    shared = {row["text"] for row in rows} & {row.get("text") for row in _load(src / "cases.jsonl")}
    assert not shared, "A held-out comment is also in cases.jsonl. Keep the two sets apart."
