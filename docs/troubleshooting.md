# Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Model returns prose, not JSON | Loose prompt or wrong chat template | Tighten prompt; same `apply_chat_template` in training and inference |
| Everything parses invalid | Markdown fences or extra text | Tolerant parser; log fence frequency |
| Scores identical across runs | Greedy decoding | Good |
| Scores differ across runs | Sampling on, or data order changed | Greedy, fixed seed, fixed order |
| Near 50% on PrimeVul | Task is hard | Expected; report honestly |
| Out-of-memory | Sequence too long, batch too big | Lower `max_length`, batch 1, more accumulation |
| Great train loss, bad test F1 | Overfitting or leakage | Check splits and duplicates, fewer epochs |
| F1 suspiciously high | Imbalance or contamination | Check balance; compare with always-vulnerable |
| Fine-tuned worse than baseline | Noisy labels, template mismatch, high LR | Inspect labels, check template, lower LR |
| API or argument errors | Library version drift | Use `requirements.lock`; check current docs |
| Session dies mid-training | Cloud limits | Save checkpoints and adapters often |
| Outputs get shorter or odd during RL | Environment quirk exploited | See [reward hacking](reward-hacking-and-environment-fidelity.md) |
