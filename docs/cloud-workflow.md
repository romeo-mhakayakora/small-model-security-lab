# Cloud Workflow

A 4 GB laptop GPU is enough for writing code and small inference runs. Real training happens on free cloud GPUs.

> **Develop locally, train in the cloud.**

| Task | Laptop | Kaggle / Colab |
|---|---|---|
| Write and debug code, tests | Yes | |
| Inference on 0.5B-1.5B in 4-bit | Yes, with length cap | Faster |
| Full baseline runs | Slow | Preferred |
| QLoRA training | Not comfortable | **Yes** |

## Moving things between machines

| Item | How |
|---|---|
| Code and configs | Git: clone the repo inside the notebook |
| Datasets | Kaggle Dataset or Google Drive. Verify SHA-256 against `data/manifests/` |
| Adapters | Hugging Face Hub (private repo) or Drive, **at the end of every run** |
| Results | Download `results.jsonl`, commit summaries to `reports/` |

## Rules

1. Sessions die. Save checkpoints and adapters often.
2. Never put tokens in shared notebooks. Use Kaggle/Colab secrets.
3. Check dataset hashes after download.
4. Record GPU type and library versions in every run record.
5. Pin `requirements.lock` so cloud and local behave the same.

## Typical flow

```text
1. git clone <repo>; pip install -r requirements.lock
2. Download dataset; verify hash
3. Run training with a config from configs/training/
4. Save adapter to Hub/Drive
5. Run evaluation with the same harness as local
6. Download results; commit report
```

Out-of-memory: lower `max_length`, batch size 1, raise gradient accumulation, use a smaller model.
