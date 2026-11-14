# Brewly's feedback sorter

A Dhi graded project (AI engineering, Building with models). Brewly is a practice company: every comment here is invented.

Build an AI feature that sorts customer comments into a category, a sentiment, a refund flag and the café named, then prove how well it works with a test set, graders, a score and a cost.

## Start

1. Click **Use this template** on GitHub to make your own public repository, then open it in a codespace.
2. `pip install -r requirements.txt`
3. `python grade.py --all`. Every step says NOT YET until you build it.

Python 3.12 or later. `grade.py --all` takes under 10 seconds on a laptop.

## The steps

| Step | You build | Check it |
|---|---|---|
| 1 | `cases.jsonl` (30 or more labelled comments) and `holdout.jsonl` (10 kept apart) | `python grade.py --step 1` |
| 2 | `score()` and `cost_per_1000()` in `scoring.py` | `python grade.py --step 2` |
| 3 | `sort_comment()` and `INSTRUCTIONS` in `sorter.py` | `python grade.py --step 3` |
| 4 | `evaluate()` in `evaluate.py` | `python grade.py --step 4` |
| 5 | Nothing new: no key or secret anywhere in the repository | `python grade.py --step 5` |

Push to GitHub and the **Actions** tab runs `python grade.py --all`. A green tick means every step passes.

## How the checks work

The checks never call a model. Steps 3 and 4 replay saved replies from `fixtures/replies.json`, so every run is free and gives the same result. Each saved reply shows the model and date it stands for.

For your own results table, `python grade.py --live` runs your sorter once on the saved comments with your own key (`ANTHROPIC_API_KEY`) and prints the score and cost. A live run never passes or fails. Your real scores come from `python evaluate.py cases.jsonl`.

## What the checks do not prove

They prove your scoring, your sorter and your safety on saved replies. They do not prove the quality of your own hand labels, your prompt changes or your README. Mark those yourself with the marking guide in the Dhi lesson.

## Licence

MIT (see `LICENSE`). The code you add is yours.
