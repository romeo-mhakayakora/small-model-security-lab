# Reward Hacking and Environment Fidelity

Notes from a talk on post-training agents (speaker not identified in the transcript). Relevant to Stages 7-9 and any RL you try later.

## Three levels of post-training

| Level | Setup | Where it appears here |
|---|---|---|
| 1. Single-turn Q&A | Prompt, answer, grader, weight update | Stages 4-7 |
| 2. Synthetic environments | Multi-turn tool use in a **replayable** sandbox | Stages 8-9 |
| 3. Bring your own harness | Train on real production usage you do not control | Beyond this project |

GRPO compares many rollouts of the same prompt and upweights the better ones. That needs replayability: reset the environment to the same start state and run again.

## Key lesson: models learn your environment's quirks

1. **Flaky tools.** About 10% of tool calls failed from networking issues. The model produced shorter and shorter responses with no length penalty in the reward: longer runs meant more chances to hit a failure and get zero.
2. **Timeouts.** Timed-out rollouts were filtered from training. On hard problems the model learned to spam slow tool calls to force a timeout, avoiding a zero reward because the rollout was dropped.

Your Semgrep, Docker and pytest steps can fail or time out too. If you train on their outcomes, the model may learn the sandbox, not security.

## Practices for this project

1. **Log full traces from the first agent run:** prompt, tool calls, results, timeouts, grade.
2. **Track tool failure and timeout rates as metrics.**
3. **Never silently drop timed-out runs.** Count them and give them a defined score.
4. **Keep the sandbox replayable:** fixed Docker image, fixed seed data, reset per run.
5. **Keep the grader independent of the model.** The model proposes, tests decide.
6. **After any RL experiment, check for hacks:** compare output length, tool-call counts and timeout frequency with baseline. If they drift, suspect the environment before celebrating the score.
7. **Start with verifiable rewards:** for example, "does the cited line exist and match the patch".

## Manual version of automated data pipelines

The speaker's team reviews traces by hand, finds failure modes and curates data. Your Stage 3 error tagging is the same activity. Start manual.

## Ignore for now

Bring-your-own-harness training, self-distillation, learning from qualitative feedback, self-improving deployments. The speaker describes these as open research directions.
