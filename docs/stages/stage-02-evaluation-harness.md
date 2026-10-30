# Stage 2: Evaluation Harness (4-6 days)

## Goal
One command that scores any model on your test set and prints a report. **Build this before training.**

## Read first
- Inspect AI tutorial, tasks, scorers, log viewer
- scikit-learn metrics docs; Pydantic validators

## What is already in this repo
| File | Purpose |
|---|---|
| `src/evaluation/schema.py` | Pydantic output schema |
| `src/evaluation/parse.py` | Tolerant JSON parser that logs markdown fences |
| `src/evaluation/scoring.py` | `score_example`, shared by every runner |
| `src/evaluation/run_local.py` | Local 4-bit runner (works on a 4 GB GPU), writes `results.jsonl` |
| `src/evaluation/metrics.py` | Precision/recall/F1 with bootstrap intervals from `results.jsonl` |
| `src/evaluation/dumb_baselines.py` | Always-vulnerable, always-safe, random |
| `src/evaluation/task.py` | Inspect AI task using the same scorer |
| `tests/` | pytest tests for parser, scoring, metrics |

## Two runners, one scorer
- **Local runner** loads the model with 4-bit quantization directly, so it fits on a 4 GB GPU.
- **Inspect AI** gives logs, a viewer and agent support later. Check the Inspect Hugging Face provider docs for how it passes quantization arguments before relying on it locally. On Kaggle/Colab, full precision may be fine.

Both call `score_example`, so numbers agree.

## Steps
1. Run `pytest` and read the tests. Add a case for every parsing surprise you meet.
2. Freeze the prompt in `configs/evaluation/prompt_v1.txt`.
3. Run on 20 examples:

```bash
python -m src.evaluation.run_local --data data/processed/primevul_v1_test.jsonl \
  --model Qwen/Qwen2.5-Coder-1.5B-Instruct --limit 20 --out reports/dev/results.jsonl
python -m src.evaluation.metrics --results reports/dev/results.jsonl
```
4. Every run writes a record: model and revision, adapter path, dataset hash, prompt version, decoding settings, seed, date, GPU, metrics.
5. Optionally wire the same task into Inspect AI (`inspect eval src/evaluation/task.py`).

## Metrics reported
Precision, recall, F1, invalid-output rate, CWE accuracy, latency, peak GPU memory, each with a 95% bootstrap interval where meaningful.

## Done when
- One command prints a report table.
- Parser and scorer tests pass.
- Every run is saved with its metadata.

## Pitfalls
- Scoring accuracy alone. A model that always says "vulnerable" looks good on imbalanced data.
- Using a different prompt or chat template for training than for evaluation.
- Using `eval()` on dataset fields. Use `json.loads`.

**Next:** [Stage 3](stage-03-baseline.md)
