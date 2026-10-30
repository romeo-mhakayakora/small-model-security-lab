# Stage 4: First Fine-Tune (1 week)

## Goal
A saved adapter and a harness report for the fine-tuned model, side by side with the baseline.

## Read first
- TRL `SFTTrainer` docs; PEFT LoRA docs
- LoRA and QLoRA papers (intro and method only)
- Hugging Face Smol Course; Raschka's LoRA tips

## Method
SFT with QLoRA on Kaggle or Colab (see [cloud workflow](../cloud-workflow.md)).

## Steps
1. Build the **training split** in chat format using **exactly the same prompt template** as evaluation.
2. Train on 200 examples first: confirm it runs and loss falls.
3. Scale to the full filtered training set.
4. Save the adapter and the exact config in `configs/training/`.
5. Run the **same harness, same test set, same settings** on the adapter model.
6. Compare with baseline, with intervals.

## Skeleton
Argument names change between TRL versions. Check current docs.

```python
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig

peft_cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
                      target_modules="all-linear", task_type="CAUSAL_LM")
cfg = SFTConfig(output_dir="out", num_train_epochs=2,
                per_device_train_batch_size=2, gradient_accumulation_steps=8,
                learning_rate=2e-4, max_length=1024, logging_steps=10, seed=42)
trainer = SFTTrainer(model=model, args=cfg, train_dataset=train_ds, peft_config=peft_cfg)
trainer.train()
trainer.save_model("models/adapters/run_001")
```

## Learn only this
What LoRA does, what QLoRA adds, batch size vs gradient accumulation, reading a loss curve.

## Done when
- A saved adapter and a report next to the baseline exist.
- You can reproduce the run from its config.

## Pitfalls
- Prompt or chat-template mismatch between training and inference.
- Judging by training loss instead of held-out metrics.
- Forgetting to save the adapter before the session dies.

**Next:** [Stage 5](stage-05-diagnose.md)
