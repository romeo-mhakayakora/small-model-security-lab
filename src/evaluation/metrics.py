"""Metrics with bootstrap confidence intervals, computed from results.jsonl."""
import argparse
import json

import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score

from .dumb_baselines import run as dumb_run


def load_results(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def to_arrays(rows):
    """Invalid outputs count as WRONG: prediction is set opposite to the truth."""
    y_true = np.array([int(r["exp_vuln"]) for r in rows])
    y_pred = np.array([
        int(r["pred_vuln"]) if r["valid"] else 1 - int(r["exp_vuln"]) for r in rows
    ])
    return y_true, y_pred


def _metric(fn):
    return lambda t, p: fn(t, p, zero_division=0)


METRICS = {
    "precision": _metric(precision_score),
    "recall": _metric(recall_score),
    "f1": _metric(f1_score),
}


def bootstrap_ci(y_true, y_pred, metric, n=1000, seed=42):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    rng = np.random.default_rng(seed)
    idx = np.arange(len(y_true))
    vals = []
    for _ in range(n):
        s = rng.choice(idx, size=len(idx), replace=True)
        vals.append(metric(y_true[s], y_pred[s]))
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return float(metric(y_true, y_pred)), float(lo), float(hi)


def paired_bootstrap_diff(y_true, pred_a, pred_b, metric, n=1000, seed=42):
    """Difference (b - a) on the SAME resampled examples. CI excluding 0 suggests a real change."""
    y_true, pred_a, pred_b = map(np.asarray, (y_true, pred_a, pred_b))
    rng = np.random.default_rng(seed)
    idx = np.arange(len(y_true))
    diffs = []
    for _ in range(n):
        s = rng.choice(idx, size=len(idx), replace=True)
        diffs.append(metric(y_true[s], pred_b[s]) - metric(y_true[s], pred_a[s]))
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    point = metric(y_true, pred_b) - metric(y_true, pred_a)
    return float(point), float(lo), float(hi)


def summarize(rows) -> dict:
    y_true, y_pred = to_arrays(rows)
    out = {"n": len(rows)}
    for name, fn in METRICS.items():
        p, lo, hi = bootstrap_ci(y_true, y_pred, fn)
        out[name] = {"value": p, "ci95": [lo, hi]}
    out["invalid_rate"] = float(np.mean([not r["valid"] for r in rows]))
    out["fence_rate"] = float(np.mean([r.get("had_fence", False) for r in rows]))
    vuln = [r for r in rows if r["exp_vuln"]]
    out["cwe_accuracy_on_vulnerable"] = (
        float(np.mean([r["cwe_ok"] for r in vuln])) if vuln else None
    )
    lat = [r["latency_s"] for r in rows if "latency_s" in r]
    out["mean_latency_s"] = float(np.mean(lat)) if lat else None
    out["dumb_baselines"] = dumb_run(y_true)
    return out


def format_report(s: dict) -> str:
    lines = [f"n = {s['n']}"]
    for name in METRICS:
        m = s[name]
        lines.append(f"{name:10s} {m['value']:.2f} [{m['ci95'][0]:.2f}-{m['ci95'][1]:.2f}]")
    lines.append(f"invalid output rate: {s['invalid_rate']:.2%}")
    lines.append(f"markdown fence rate: {s['fence_rate']:.2%}")
    if s["cwe_accuracy_on_vulnerable"] is not None:
        lines.append(f"CWE accuracy (vulnerable only): {s['cwe_accuracy_on_vulnerable']:.2%}")
    if s["mean_latency_s"] is not None:
        lines.append(f"mean latency: {s['mean_latency_s']:.2f}s")
    lines.append("dumb baselines (F1): " + ", ".join(
        f"{k}={v['f1']:.2f}" for k, v in s["dumb_baselines"].items()))
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", default=None, help="optional path to save summary JSON")
    a = ap.parse_args()
    summary = summarize(load_results(a.results))
    print(format_report(summary))
    if a.out:
        with open(a.out, "w") as f:
            json.dump(summary, f, indent=2)
