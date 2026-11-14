"""Brewly's feedback sorter: one customer comment in, one structured answer out."""

from typing import Literal

from pydantic import BaseModel

MODEL = "claude-opus-5-5"

# Step 3: say what each field means, with the edge cases from your test set.
INSTRUCTIONS = "Sort the customer comment."


class Feedback(BaseModel):
    category: Literal["drinks", "food", "service", "cleanliness", "price", "other"]
    sentiment: Literal["positive", "neutral", "negative"]
    refund_requested: bool
    cafe: str | None  # None when no café is named


def sort_comment(text, client, model=MODEL):
    """Return (Feedback, usage), or (None, usage) when the reply was refused or cut off.

    `client` is anthropic.Anthropic() in real runs; the checks pass a stand-in that replays saved replies.
    Step 3: call client.messages.parse with output_format=Feedback, and put the comment in the user message.
    """
    raise NotImplementedError("Step 3: write sort_comment")
