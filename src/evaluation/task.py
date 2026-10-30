"""Inspect AI task using the same scorer as the local runner.

Inspect's API evolves. Treat this as a structure to adapt and check the current docs
(inspect.aisi.org.uk), especially how the Hugging Face provider passes quantization args.

Run: inspect eval src/evaluation/task.py --model <provider/model>
"""
from inspect_ai import Task, task
from inspect_ai.dataset import Sample, json_dataset
from inspect_ai.scorer import Score, Target, accuracy, scorer
from inspect_ai.solver import TaskState, generate

from .run_local import build_prompt
from .scoring import score_example

TEMPLATE = open("configs/evaluation/prompt_v1.txt").read()


def record_to_sample(rec: dict) -> Sample:
    return Sample(
        id=rec["id"],
        input=build_prompt(TEMPLATE, rec["code"]),
        target=rec["target"],  # JSON string
        metadata=rec.get("meta", {}),
    )


@scorer(metrics=[accuracy()])
def security_scorer():
    async def score(state: TaskState, target: Target):
        res = score_example(state.output.completion, target.text)
        return Score(value=1 if res["correct"] else 0,
                     answer=state.output.completion, metadata=res)
    return score


@task
def vuln_detect(dataset_path: str = "data/processed/primevul_v1_test.jsonl"):
    return Task(dataset=json_dataset(dataset_path, record_to_sample),
                solver=[generate()], scorer=security_scorer())
