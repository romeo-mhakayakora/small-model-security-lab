import numpy as np
from sklearn.metrics import f1_score

from src.evaluation.dumb_baselines import run as dumb_run
from src.evaluation.metrics import (METRICS, bootstrap_ci, paired_bootstrap_diff,
                                    summarize, to_arrays)


def _row(exp, pred, valid=True):
    return {"exp_vuln": exp, "pred_vuln": pred, "valid": valid, "cwe_ok": True, "had_fence": False}


def test_invalid_counts_as_wrong():
    y_true, y_pred = to_arrays([_row(True, None, valid=False)])
    assert y_true[0] == 1 and y_pred[0] == 0


def test_dumb_always_vulnerable_on_balanced():
    res = dumb_run([1, 0] * 50)
    assert res["always_vulnerable"]["recall"] == 1.0
    assert abs(res["always_vulnerable"]["precision"] - 0.5) < 1e-9


def test_bootstrap_interval_contains_point_and_is_ordered():
    rng = np.random.default_rng(0)
    y = rng.integers(0, 2, 100)
    p = np.where(rng.random(100) < 0.7, y, 1 - y)
    point, lo, hi = bootstrap_ci(y, p, METRICS["f1"])
    assert lo <= point <= hi


def test_paired_diff_zero_for_same_predictions():
    y = np.array([1, 0] * 20)
    p = np.array([1, 1, 0, 0] * 10)
    d, lo, hi = paired_bootstrap_diff(y, p, p, METRICS["f1"])
    assert d == 0 and lo == 0 and hi == 0


def test_summarize_runs():
    rows = [_row(True, True), _row(False, False), _row(True, False), _row(False, True)]
    s = summarize(rows)
    assert s["n"] == 4 and 0 <= s["f1"]["value"] <= 1
    assert s["f1"]["value"] == f1_score([1, 0, 1, 0], [1, 0, 0, 1])
