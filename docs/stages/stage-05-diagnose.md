# Stage 5: Diagnose (1-2 weeks)

## Goal
Learn to investigate **why** results changed. This is where you start doing research.

## Read first
Search: training vs validation loss and overfitting in LLM fine-tuning. Re-read your experiment log.

## Experiments, one change at a time
| # | Question | Variable |
|---|---|---|
| 1 | Does data quantity matter? | More vs. less data |
| 2 | Is the learning rate right? | 5e-5, 1e-4, 2e-4 |
| 3 | Is it overfitting? | Epochs (train loss falls, test F1 stalls) |
| 4 | Does class balance matter? | Balanced vs. imbalanced |
| 5 | Does it generalize? | Juliet, DiverseVul, unseen projects |
| 6 | Do some CWEs regress? | Per-CWE breakdown |

## Record for each run
Model revision, dataset version, configuration, seed, metrics with intervals, resource usage in `experiments/log.csv`.

## Also do
Write your [research question](../research-question.md) before leaving this stage.

## Done when
You identified at least one meaningful failure, investigated its cause, and ran an experiment designed to address it.

**Next:** [Stage 6](stage-06-evidence.md)
