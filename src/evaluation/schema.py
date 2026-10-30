"""Output schema the model must produce."""
import re
from typing import Optional

from pydantic import BaseModel, field_validator


class Finding(BaseModel):
    vulnerable: bool
    cwe: Optional[str] = None
    evidence: Optional[str] = None

    @field_validator("cwe")
    @classmethod
    def cwe_format(cls, v):
        if v is None:
            return v
        if not re.fullmatch(r"CWE-\d+", v):
            raise ValueError("cwe must look like CWE-123")
        return v
