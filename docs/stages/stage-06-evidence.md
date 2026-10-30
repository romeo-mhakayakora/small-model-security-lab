# Stage 6: Add Evidence (1-2 weeks)

## Goal
Make the model say **where** and **why**, not only a label.

## Read first
Hinton et al. on distillation (concept only). Terms of service of any stronger model you use to draft evidence.

## Steps
1. Use a stronger model to draft `evidence` for training examples.
2. **Verify automatically:** discard any whose quoted evidence does not appear in the code (normalize whitespace and compare).
3. Spot-check 30 manually.
4. Retrain with the evidence field.
5. Score with new metrics:
   - Does the cited line exist in the code?
   - Is it the real problem (compare with the patch diff where PrimeVul provides one)?

This is lightweight distillation and your first real security-reasoning step.

## Done when
Evidence quality is scored automatically and reported next to label accuracy.

## Pitfalls
Rewarding convincing explanations instead of correct ones. Tie checks to verifiable facts.

**Next:** [Stage 7](stage-07-dpo.md)
