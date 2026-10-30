# Stage 7: DPO (optional, 1-2 weeks)

## Goal
Test whether preference training beats SFT alone.

## Read first
DPO paper; TRL `DPOTrainer`; Hugging Face *Illustrating RLHF*.

## Steps
1. Build preference pairs: a **verified-correct** answer as `chosen`, a wrong or unsupported one as `rejected`.
2. Train with `DPOTrainer`.
3. Compare against SFT only, with intervals.

## Warning
If preferences reward convincing explanations over correct findings, the model learns to sound right, not be right. Tie them to verifiable outcomes.

## Done when
You can explain with evidence whether DPO helped. "It did not beat SFT" is a valid result.

**Next:** [Stage 8](stage-08-agent.md)
