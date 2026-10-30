"""Tolerant parser: accepts markdown fences and surrounding text, but reports it."""
import json
import re

from .schema import Finding

FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.S)


def parse_output(text: str):
    """Return (Finding | None, flags). Never raises."""
    flags = {"had_fence": False, "valid_json": False, "valid_schema": False}
    try:
        m = FENCE.search(text)
        if m:
            flags["had_fence"] = True
            text = m.group(1)
        start, end = text.index("{"), text.rindex("}") + 1
        obj = json.loads(text[start:end])
        flags["valid_json"] = True
        finding = Finding(**obj)
        flags["valid_schema"] = True
        return finding, flags
    except Exception:
        return None, flags
