"""One scoring function shared by the local runner and Inspect AI."""
import json

from .parse import parse_output


def load_target(target) -> dict:
    """Targets are stored as JSON strings. Never use eval()."""
    return json.loads(target) if isinstance(target, str) else dict(target)


def score_example(output_text: str, target) -> dict:
    exp = load_target(target)
    exp_vuln = bool(exp["vulnerable"])
    exp_cwe = exp.get("cwe")
    finding, flags = parse_output(output_text)
    valid = finding is not None
    pred_vuln = finding.vulnerable if valid else None
    pred_cwe = finding.cwe if valid else None
    label_ok = valid and pred_vuln == exp_vuln
    cwe_ok = (not exp_vuln) or (valid and pred_cwe == exp_cwe)
    return {
        "valid": valid,
        "pred_vuln": pred_vuln,
        "pred_cwe": pred_cwe,
        "exp_vuln": exp_vuln,
        "exp_cwe": exp_cwe,
        "label_ok": bool(label_ok),
        "cwe_ok": bool(cwe_ok),
        "correct": bool(label_ok and cwe_ok),
        "had_fence": flags["had_fence"],
    }
