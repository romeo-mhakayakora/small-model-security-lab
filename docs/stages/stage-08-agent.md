# Stage 8: Tools and Agent (2-4 weeks)

## Goal
A model that investigates with tools instead of only describing what it would do.

## Read first
Anthropic *Building effective agents*; Inspect AI agents and tools; Pydantic; the [reward hacking notes](../reward-hacking-and-environment-fidelity.md); search CyberSecEval and CTF-style benchmarks.

## Steps
1. Write a **plain Python loop** first, no framework: model chooses a tool from a whitelist, you run it, result returns, repeat.
2. Tools: `run_semgrep(file)` and `read_file(path)` restricted to the project folder.
3. Validate every tool call with Pydantic.
4. Enforce a step limit, a per-call timeout and a total budget.
5. **Log full traces:** prompt, tool calls, results, timeouts, grade.
6. Track tool failure and timeout rates as metrics. Never silently drop timed-out runs.
7. Score the agent in Inspect AI.

## Safety
The model never runs arbitrary commands. Software decides which tools and arguments are allowed. Only authorized targets. See [safety](../safety-and-authorization.md).

## Done when
The agent completes a small repeatable task and your harness measures its success, including failure and timeout rates.

**Next:** [Stage 9](stage-09-verification.md)
