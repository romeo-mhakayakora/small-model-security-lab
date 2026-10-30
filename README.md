# Small-Model Security Lab

A hands-on, stage-by-stage learning project: **post-training small language models for security engineering**, built to run on limited hardware.

You go from one working prompt to a fine-tuned model, an evaluation harness, a tool-using agent, an independent verification pipeline, and an efficient deployment. Every stage ends with a working artifact and a **Done when** check. Do not start the next stage until the check passes.

> **Goal:** become a research engineer who can take an existing model, find a security capability it lacks, design a training experiment to improve it, verify the improvement independently, and deploy it efficiently.

## How to use this repo

1. Read [`docs/00-overview-and-rules.md`](docs/00-overview-and-rules.md) once.
2. Do the [smoke test](docs/smoke-test.md) to prove your plumbing works on a tiny problem.
3. Work through the stages in order. Each page says what to read, what to build, and how to know you are done.
4. Log every run in [`experiments/log.csv`](experiments/log.csv).
5. Keep paper notes in [`notes/papers.md`](notes/papers.md).
6. When stuck for more than a day, **shrink the problem**.

## Stage map

| Stage | Page | What you produce | Rough time |
|---|---|---|---|
| 0 | [Setup](docs/stages/stage-00-setup.md) | A model answers a prompt on your machine | 1-2 days |
| 1 | [Data](docs/stages/stage-01-data.md) | Clean, versioned, reproducible dataset | 3-5 days |
| 2 | [Evaluation harness](docs/stages/stage-02-evaluation-harness.md) | One command that scores any model | 4-6 days |
| 3 | [Baseline](docs/stages/stage-03-baseline.md) | A reproducible baseline report | 1-2 weeks |
| 4 | [First fine-tune](docs/stages/stage-04-first-finetune.md) | Saved adapter plus report vs. baseline | 1 week |
| 5 | [Diagnose](docs/stages/stage-05-diagnose.md) | Experiment log with explained failures | 1-2 weeks |
| 6 | [Add evidence](docs/stages/stage-06-evidence.md) | Model cites where and why | 1-2 weeks |
| 7 | [DPO (optional)](docs/stages/stage-07-dpo.md) | Evidence on whether preference training helps | 1-2 weeks |
| 8 | [Tools and agent](docs/stages/stage-08-agent.md) | A sandboxed tool-using agent | 2-4 weeks |
| 9 | [Verification](docs/stages/stage-09-verification.md) | Findings checked by independent tests | 2-4 weeks |
| 10 | [Deployment](docs/stages/stage-10-deployment.md) | Quantized, measured, usable prototype | 2+ weeks |

**Stages 0-5 alone make a solid portfolio project.**

## Supporting docs

| Doc | Purpose |
|---|---|
| [Reading list](docs/reading-list.md) | Papers, docs and blogs, placed at the stage that needs them |
| [Smoke test and scale ladder](docs/smoke-test.md) | Start small, grow only when the rung below works |
| [Cloud workflow](docs/cloud-workflow.md) | Develop locally, train on Kaggle/Colab |
| [Juliet extraction](docs/juliet-extraction.md) | Turning Juliet into usable examples |
| [Reward hacking](docs/reward-hacking-and-environment-fidelity.md) | Lessons for the agent and RL stages |
| [Safety and authorization](docs/safety-and-authorization.md) | Rules for responsible security work |
| [Research question](docs/research-question.md) | Turning a pipeline into a contribution |
| [Troubleshooting](docs/troubleshooting.md) | Symptom, cause, fix |
| [Glossary](docs/glossary.md) | Terms used throughout |

## Chosen defaults (do not revisit until Stage 5)

| Decision | Choice |
|---|---|
| Task | Given a C/C++ function, output JSON: `vulnerable`, `cwe`, later `evidence` |
| Main dataset | PrimeVul (test split for evaluation) |
| Sanity-check dataset | Juliet (C/C++) |
| Model | `Qwen/Qwen2.5-Coder-1.5B-Instruct` (0.5B for the smoke test) |
| Training | SFT with QLoRA via TRL + PEFT |
| Evaluation | Local 4-bit runner (or Inspect AI), scikit-learn, bootstrap intervals |
| Hardware | Develop on a 4 GB GPU laptop, train on Kaggle/Colab |

Newer small coder models may exist. Check Hugging Face once, **pick one, and do not switch mid-project.**

## Layout

```text
small-model-security-lab/
├── configs/{training,evaluation}/
├── data/{raw,processed,manifests}/     # raw and processed are not in Git
├── docs/                               # stage pages and supporting docs
├── experiments/log.csv
├── notes/papers.md
├── reports/
├── src/{data_pipeline,evaluation,training,agent,verification}/
├── tests/
├── run_baseline.sh
└── requirements.txt
```

Commit code, configs, manifests and reports. **Never commit datasets or model weights.**

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest                      # parser, scoring and metric tests
pip freeze > requirements.lock
```

Then follow [Stage 0](docs/stages/stage-00-setup.md).

## Status

- [ ] Stage 0  - [ ] Smoke test  - [ ] Stage 1  - [ ] Stage 2  - [ ] Stage 3  - [ ] Stage 4
- [ ] Stage 5  - [ ] Stage 6  - [ ] Stage 7 (optional)  - [ ] Stage 8  - [ ] Stage 9  - [ ] Stage 10
