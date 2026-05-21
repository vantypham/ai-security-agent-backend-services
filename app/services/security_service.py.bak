from app.services.llm_service import (
    llm_service
)
import json

class SecurityService:

    async def analyze(
        self,
        rule_id:str,
        code:str
    ):

        prompt = f"""
Security finding:

Rule:
{rule_id}

Code:
{code}

Return:

1. Severity
2. OWASP category
3. Explanation
"""

        result = await llm_service.ask(
            prompt
        )

        return result


    async def suggest_fix(
        self,
        rule_id:str,
        code:str
    ):

        prompt=f"""
Analyze security issue.

Rule:
{rule_id}

Code:
{code}

Return ONLY JSON:

{{
    "severity":"HIGH",
    "owasp":"A03 Injection",
    "explanation":"",
    "fixed_code":""
}}
"""

        result=await llm_service.ask(
            prompt
        )

        return json.loads(result)


security_service = SecurityService()