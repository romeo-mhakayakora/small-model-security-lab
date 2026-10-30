# Smoke Test and Scale Ladder

Prove your pipeline works end to end on a tiny problem. The goal is **working plumbing**, not a good score.

## Setup

| Setting | Value |
|---|---|
| Model | `Qwen/Qwen2.5-Coder-0.5B-Instruct` |
| Data | Juliet, **one CWE only** (see [Juliet extraction](juliet-extraction.md)) |
| Size | 100 train, 40 test, balanced |
| Training | 1 epoch on Colab/Kaggle (0.5B may fit locally with QLoRA; test first) |
| Scoring | `vulnerable` true/false only, no CWE yet |

## Steps

1. Run the untouched model on 20 test examples. Fix parsing problems.
2. Run the always-vulnerable baseline on the same 20 examples.
3. Train 1 epoch on 100 examples.
4. Run the same 40 test examples on the fine-tuned model.
5. Compare.

## Pass criteria (about the pipeline, not the score)

- [ ] Valid-JSON rate above 90% after fine-tuning
- [ ] Re-running evaluation gives identical numbers
- [ ] Training loss decreases
- [ ] The saved adapter reloads and generates
- [ ] Results file records model, dataset hash, prompt version, seed

Juliet is easy and may be memorized. A good smoke-test score proves nothing about security skill.

## Scale ladder

Move up one rung only when the rung below works **and you can explain the result**.

| Rung | Size | Goal |
|---|---|---|
| 1 | 20 examples | Code runs, parser works |
| 2 | 100 train, 40 test | Pipeline works end to end |
| 3 | 500 | Training behaves sensibly |
| 4 | A few thousand, PrimeVul, 3-5 CWEs | Real experiments with confidence intervals |
| 5 | Larger model or more data | Only if rung 4 shows a signal |

If a rung fails, shrink the problem again instead of adding data.
