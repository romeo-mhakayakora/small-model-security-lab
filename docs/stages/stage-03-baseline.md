# Stage 3: Baseline (1-2 weeks)

## Goal
Establish what the **untouched** model can do. This is the number every later experiment must beat. **Do not change model weights in this stage.**

## Read first
- PrimeVul again: evaluation and pair-wise metric sections
- Any explainer on bootstrap confidence intervals
- Semgrep and Cppcheck docs

## Datasets
| Dataset | Role | Notes |
|---|---|---|
| PrimeVul (test split only) | Main baseline | Expect near-random results; that is a real finding |
| Juliet sample | Sanity check | Should score better than PrimeVul; if not, check prompt and parser |
| DiverseVul | Optional | Useful later for generalization |
| Devign / Big-Vul | Skip | Known label-noise problems |

Use balanced sets of 100-200 examples. Check licenses before any commercial use.

## Fixed settings (record all)
| Setting | Value |
|---|---|
| Decoding | Greedy (`do_sample=False`) |
| `max_new_tokens` | Fixed (for example 256) |
| Prompt | `configs/evaluation/prompt_v1.txt` |
| Seed | Fixed (for example 42) |
| Model revision | Exact Hugging Face commit hash |

Changing any of these changes your baseline.

## Part A: Dumb baselines (first)
Run always-vulnerable, always-safe and seeded random on the same set, plus Semgrep or Cppcheck as a non-LLM reference. If the model cannot beat always-vulnerable on F1, that is your finding. See `src/evaluation/dumb_baselines.py`.

## Part B: Prompt variants
Run each separately: zero-shot, few-shot (2-3 examples from **outside** the test set), zero-shot with stricter JSON instruction. Pick the best, freeze it, use it for every later comparison. Do not tune endlessly.

## Part C: PrimeVul paired evaluation
PrimeVul pairs each vulnerable function with its patch. The paper defines pair-wise metrics that check whether the model handles **both halves**. Implement them from the paper's exact definitions and report them next to F1.

## Part D: Confidence intervals
Report every metric as `0.57 [0.49-0.65]`. A fine-tuned model counts as better only if intervals clearly separate. For two models on the same examples, use a paired bootstrap (`paired_bootstrap_diff` in `metrics.py`).

## Part E: Contamination
Qwen was probably trained on public GitHub code and possibly these datasets. Note this in the report. Later, build a small private test set (code written after the model's cutoff, or code you write and label yourself).

## Procedure
1. Freeze the prompt.
2. Run 20 examples; fix parsing.
3. Run dumb baselines on the same 20.
4. Run the full 100-200 per dataset.
5. Run prompt variants; freeze the best.
6. Run Semgrep/Cppcheck on the same functions.
7. Compute metrics with intervals and the pair-wise score.
8. Save to `reports/baseline_v1/`: model and revision, dataset hash, prompt version, decoding settings, metrics, latency, peak memory, dumb-baseline scores.
9. Export wrong answers to CSV and **read 20 by hand**. Tag each:

| Tag | Meaning |
|---|---|
| ALWAYS_VULN / ALWAYS_SAFE | Predicts one class almost always |
| BROKEN_JSON | Not parseable |
| INVENTED_CWE | CWE does not exist or is unrelated |
| WRONG_FAMILY | Wrong category entirely |
| RIGHT_FAMILY_WRONG_ID | Close but not exact |
| RIGHT_LABEL_BAD_REASON | Correct verdict, unsupported explanation |
| LABEL_SUSPECT | The dataset label looks wrong |

## Done when
- [ ] Dumb baselines and Semgrep/Cppcheck scored
- [ ] Pair-wise metric computed
- [ ] Confidence intervals on every metric
- [ ] Three prompt variants compared, one frozen
- [ ] 20 wrong answers hand-tagged
- [ ] Contamination caveat in the report
- [ ] Everything reproducible with `run_baseline.sh`
- [ ] You can say in two sentences what the base model does badly

## Pitfalls
See [troubleshooting](../troubleshooting.md). Near 50% on PrimeVul is expected.

**Next:** [Stage 4](stage-04-first-finetune.md)
