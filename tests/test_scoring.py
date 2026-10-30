import json

from src.evaluation.scoring import score_example

T_VULN = json.dumps({"vulnerable": True, "cwe": "CWE-787"})
T_SAFE = json.dumps({"vulnerable": False, "cwe": None})


def test_correct_vulnerable():
    r = score_example('{"vulnerable": true, "cwe": "CWE-787"}', T_VULN)
    assert r["correct"] and r["label_ok"] and r["cwe_ok"]


def test_wrong_cwe():
    r = score_example('{"vulnerable": true, "cwe": "CWE-416"}', T_VULN)
    assert r["label_ok"] and not r["cwe_ok"] and not r["correct"]


def test_false_positive():
    r = score_example('{"vulnerable": true, "cwe": "CWE-787"}', T_SAFE)
    assert not r["correct"]


def test_safe_correct_ignores_cwe():
    r = score_example('{"vulnerable": false, "cwe": null}', T_SAFE)
    assert r["correct"]


def test_invalid_is_wrong():
    r = score_example("not json", T_VULN)
    assert not r["valid"] and not r["correct"]


def test_dict_target_also_works():
    r = score_example('{"vulnerable": false}', {"vulnerable": False, "cwe": None})
    assert r["correct"]
