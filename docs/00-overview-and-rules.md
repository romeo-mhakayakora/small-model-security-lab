# Overview and Rules

## The goal

Build a small, specialized model that analyzes code for security problems, produces structured findings, uses security tools, and has its findings checked independently. It should be efficient enough for resource-constrained settings.

## What you are becoming

A research engineer who can: take an existing model, identify a security capability it lacks, design a training experiment to improve it, verify the improvement independently, and deploy the result efficiently.

## Three core skills

| # | Skill | Meaning |
|---|---|---|
| 1 | Post-training research | Change model behavior and measure whether the change helps |
| 2 | Evaluation harness engineering | Establish whether the model performs the task correctly |
| 3 | Systems engineering | Turn the model and tools into a reliable pipeline |

## Learning by doing

> Build a tiny working version, find what you do not understand, learn exactly that, improve the version.

## The rules

1. Never start a stage until the previous stage's **Done when** check passes.
2. Never train before a baseline exists.
3. Change one thing per experiment.
4. Log everything: model revision, dataset version, config, seed, metrics.
5. When stuck for more than a day, shrink the problem.
6. Skip anything not in the current stage.
7. Loss going down is not improvement. Only held-out evaluation counts.
8. Never silently drop failed or timed-out runs. Count them.
9. Only test systems you own or are explicitly authorized to test.

## The task

```json
{"vulnerable": true, "cwe": "CWE-787", "evidence": "line or expression that causes it"}
```

Stages 1-5 score `vulnerable` and `cwe`. Stage 6 adds `evidence`.

## Definitions

| Term | Definition |
|---|---|
| True positive | Model says vulnerable, label is vulnerable |
| False positive | Model says vulnerable, label is safe |
| False negative | Model says safe, label is vulnerable |
| True negative | Model says safe, label is safe |
| Correct CWE | Exact CWE ID match (track "same family" separately) |
| Invalid output | Not parseable JSON matching the schema |

## Postpone until Stage 5 is done

Axolotl, LLaMA-Factory, multi-agent systems, LangGraph, distributed training, Kubernetes, Go services, GRPO, reward modeling, model routing.

## A note on C/C++

Most public datasets are C/C++. This phase teaches the pipeline. It does **not** show the model works on web apps, APIs or Android. Plan a later experiment on Python, JavaScript or Java data.
