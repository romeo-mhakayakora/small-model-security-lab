"""Local runner: loads a model (optionally 4-bit, optionally with a LoRA adapter),
runs greedy generation over a JSONL dataset, scores each example, writes results.jsonl.

Dataset record: {"id", "code", "target" (JSON string), "meta"}.
Works on a 4 GB GPU with --load-4bit and a 0.5B-1.5B model.
"""
import argparse
import hashlib
import json
import os
import platform
import time
from datetime import datetime, timezone

from .scoring import score_example

PROMPT_PATH = "configs/evaluation/prompt_v1.txt"


def build_prompt(template: str, code: str) -> str:
    # str.replace, not str.format: the template contains literal JSON braces
    return template.replace("{code}", code)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--adapter", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--prompt", default=PROMPT_PATH)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--max-new-tokens", type=int, default=256)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--load-4bit", action="store_true")
    a = ap.parse_args()

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed

    set_seed(a.seed)
    template = open(a.prompt).read()
    rows = [json.loads(l) for l in open(a.data) if l.strip()]
    if a.limit:
        rows = rows[: a.limit]

    kwargs = {"device_map": "auto"}
    if a.load_4bit:
        kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16, bnb_4bit_quant_type="nf4")
    tok = AutoTokenizer.from_pretrained(a.model)
    model = AutoModelForCausalLM.from_pretrained(a.model, **kwargs)
    if a.adapter:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, a.adapter)
    model.eval()
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w") as fout:
        for r in rows:
            msgs = [{"role": "user", "content": build_prompt(template, r["code"])}]
            ids = tok.apply_chat_template(
                msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
            t0 = time.time()
            with torch.no_grad():
                out = model.generate(ids, max_new_tokens=a.max_new_tokens, do_sample=False)
            latency = time.time() - t0
            text = tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True)
            rec = {"id": r["id"], "output": text, "latency_s": latency,
                   **score_example(text, r["target"])}
            fout.write(json.dumps(rec) + "\n")

    meta = {
        "model": a.model,
        "model_revision": getattr(model.config, "_commit_hash", None),
        "adapter": a.adapter,
        "dataset": a.data,
        "dataset_sha256": sha256_file(a.data),
        "prompt": a.prompt,
        "prompt_sha256": sha256_file(a.prompt),
        "max_new_tokens": a.max_new_tokens,
        "decoding": "greedy",
        "seed": a.seed,
        "load_4bit": a.load_4bit,
        "n": len(rows),
        "peak_gpu_gb": (torch.cuda.max_memory_allocated() / 1e9) if torch.cuda.is_available() else None,
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        "python": platform.python_version(),
        "date": datetime.now(timezone.utc).isoformat(),
    }
    with open(a.out + ".meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"wrote {a.out} and {a.out}.meta.json")


if __name__ == "__main__":
    main()
