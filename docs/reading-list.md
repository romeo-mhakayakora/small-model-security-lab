# Reading List

Read each item **at the stage that needs it**, not before. For each paper, write 3-4 lines in [`notes/papers.md`](../notes/papers.md):

1. What problem does it say exists?
2. What did they build or measure?
3. What did they find, and what are the limits?
4. What does it change in my pipeline?

If a paper changes no decision, stop reading it.

> **Verify links.** Titles and arXiv IDs were written from memory. Search the title if a link is wrong. Blog and course names are search terms.

## Before you start
| Type | Item | Why |
|---|---|---|
| Paper | **PrimeVul**: *Vulnerability Detection with Code Language Models: How Far Are We?* (arXiv 2403.18624) | Why this task is hard, how splits are built, pair-wise metrics |
| Docs | Hugging Face: **Chat templating**, **Text generation** | Prevents most early garbage-output bugs |

## Stage 0: Setup
| Type | Item |
|---|---|
| Docs | Hugging Face Transformers quickstart |
| Docs | Hugging Face quantization docs (bitsandbytes, 4-bit) |
| Blog | Hugging Face: *Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA* |

## Stage 1: Data
| Type | Item | Why |
|---|---|---|
| Paper | **DiverseVul** (arXiv 2304.00409) | How datasets are built, where label noise comes from |
| Paper | Search: *Data Quality for Software Vulnerability Datasets* | Duplicates and label errors |
| Paper | Search: *Deep Learning based Vulnerability Detection: Are We There Yet?* | Why realistic-data results are much lower |
| Docs | Hugging Face `datasets` | Loading and processing |

## Stage 2: Evaluation harness
| Type | Item |
|---|---|
| Docs | **Inspect AI**: tutorial, tasks, solvers, scorers, log viewer, examples gallery |
| Docs | scikit-learn metrics |
| Docs | Pydantic validators |

## Stage 3: Baseline
| Type | Item |
|---|---|
| Paper | **PrimeVul** again: evaluation and pair-wise metric sections |
| Reading | Any short explainer on **bootstrap confidence intervals** |
| Docs | Semgrep and Cppcheck (non-LLM reference baseline) |

## Stage 4: First fine-tune
| Type | Item |
|---|---|
| Docs | Hugging Face **TRL** `SFTTrainer`; **PEFT** LoRA |
| Paper | **LoRA** (arXiv 2106.09685): intro and method only |
| Paper | **QLoRA** (arXiv 2305.14314): intro and method only |
| Blog | Sebastian Raschka, practical tips for fine-tuning with LoRA (search the title) |
| Course | Hugging Face **Smol Course** |
| Report | Qwen2.5-Coder technical report (skim data and evaluation) |

## Stage 5: Diagnose
| Type | Item |
|---|---|
| Blog | Search: *training loss vs validation loss overfitting LLM fine-tuning* |
| Reading | Your own experiment log |

## Stage 6: Evidence
| Type | Item |
|---|---|
| Paper | Hinton et al., *Distilling the Knowledge in a Neural Network* (concept only) |
| Docs | Terms of service of any stronger model whose outputs you train on |

## Stage 7: DPO (optional)
| Type | Item |
|---|---|
| Paper | **DPO** (arXiv 2305.18290) |
| Docs | TRL `DPOTrainer` |
| Blog | Hugging Face: *Illustrating RLHF* |

## Stage 8: Agent
| Type | Item |
|---|---|
| Blog | Anthropic: *Building effective agents* |
| Docs | Inspect AI agents and tools; Pydantic for tool arguments |
| Talk | The post-training-for-agents talk summarized in [reward hacking](reward-hacking-and-environment-fidelity.md) |
| Reading | Search: *CyberSecEval*; LLM cybersecurity and CTF-style benchmarks |

## Stage 9: Verification
| Type | Item |
|---|---|
| Docs | Semgrep rule writing; Docker network isolation and resource limits; pytest fixtures |
| Reading | OWASP Web Security Testing Guide (when you reach web targets) |

## Stage 10: Deployment
| Type | Item |
|---|---|
| Docs | llama.cpp GGUF conversion and quantization; vLLM |
| Reading | Search: *KV cache memory LLM inference* |

## Only if you reach reinforcement learning
| Type | Item |
|---|---|
| Paper | **DeepSeekMath** (arXiv 2402.03300): introduces GRPO |
| Docs | TRL `GRPOTrainer` |
| Blog | Lilian Weng: *Reward Hacking in Reinforcement Learning* |

## Optional background
Andrej Karpathy's *Neural Networks: Zero to Hero*; Hugging Face LLM Course; Lilian Weng's blog.
