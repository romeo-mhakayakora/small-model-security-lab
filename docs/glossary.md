# Glossary

| Term | Meaning |
|---|---|
| SFT | Supervised fine-tuning on input-output examples |
| LoRA | Training small added matrices instead of all weights |
| QLoRA | LoRA on a 4-bit quantized base model |
| DPO | Direct Preference Optimization: learning from chosen/rejected pairs |
| GRPO | Group Relative Policy Optimization: RL comparing many rollouts per prompt |
| Rollout | One full attempt by the model at a task |
| Reward hacking | Exploiting quirks of the environment or grader instead of doing the task |
| Quantization | Lower numeric precision to save memory |
| Baseline | Untouched model's performance, the bar to beat |
| Harness | System that runs tasks, scores outputs and records results |
| CWE | Common Weakness Enumeration |
| Data leakage | Test data or near-copies present in training |
| Contamination | Test data present in the pretrained model's own training data |
| Bootstrap CI | Confidence interval from repeated resampling |
| Greedy decoding | Always pick the most likely next token |
| GGUF | File format used by llama.cpp |
| Adapter | Small trained LoRA weights saved separately from the base model |
| Trace | Full record of an agent run: prompts, tool calls, results, grade |
