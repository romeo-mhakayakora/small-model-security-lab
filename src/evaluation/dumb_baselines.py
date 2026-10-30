"""Non-model baselines. If your model cannot beat these, that is the finding."""
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score


def prf(y_true, y_pred) -> dict:
    return {
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }


def run(y_true, seed: int = 42) -> dict:
    y_true = np.asarray(y_true).astype(int)
    rng = np.random.default_rng(seed)
    return {
        "always_vulnerable": prf(y_true, np.ones_like(y_true)),
        "always_safe": prf(y_true, np.zeros_like(y_true)),
        "random": prf(y_true, rng.integers(0, 2, size=len(y_true))),
    }
