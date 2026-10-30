# Stage 9: Verification (2-4 weeks)

## Goal
Independently check the model's findings.

## Read first
Semgrep rule writing; Docker network isolation and limits; pytest fixtures; OWASP WSTG when you reach web targets.

## Steps
1. Build or use a **deliberately vulnerable** local app in Docker with **no external network**. Fixed image, fixed seed data, reset per run.
2. For each finding, generate a pytest that tries to demonstrate it.
3. Label every finding:

| Status | Meaning |
|---|---|
| Model-suspected | The model claims it |
| Scanner-confirmed | A static tool also flags it |
| Reproduced | A test demonstrates it |

## Principles
- A scanner alert is not proof.
- A failed reproduction does **not** prove the code is safe; the environment may be broken.
- Reports state what was verified and what remains uncertain.
- The grader is independent of the model.

## Done when
The system distinguishes model prediction, scanner alert and reproducible evidence, and reports sandbox failure rates.

**Next:** [Stage 10](stage-10-deployment.md)
