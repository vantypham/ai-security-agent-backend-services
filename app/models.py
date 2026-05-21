from pydantic import BaseModel
from typing import Optional


class SecurityRequest(BaseModel):

    rule_id: str

    code: str

    file_path: Optional[str] = None

    language: Optional[str] = None


class AnalyzeResponse(BaseModel):

    severity: str

    owasp: str

    explanation: str


class SuggestFixResponse(BaseModel):

    explanation: str

    fixed_code: str