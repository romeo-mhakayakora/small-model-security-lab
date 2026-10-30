from src.evaluation.parse import parse_output


def test_valid():
    f, flags = parse_output('{"vulnerable": true, "cwe": "CWE-787", "evidence": null}')
    assert f.vulnerable is True and f.cwe == "CWE-787" and not flags["had_fence"]


def test_fenced():
    f, flags = parse_output('```json\n{"vulnerable": false, "cwe": null}\n```')
    assert f is not None and flags["had_fence"]


def test_text_around_json():
    f, _ = parse_output('Sure! {"vulnerable": false, "cwe": null} Hope that helps.')
    assert f is not None and f.vulnerable is False


def test_prose_is_invalid():
    f, _ = parse_output("This function looks vulnerable.")
    assert f is None


def test_bad_cwe_format():
    f, flags = parse_output('{"vulnerable": true, "cwe": "787"}')
    assert f is None and flags["valid_json"] and not flags["valid_schema"]
