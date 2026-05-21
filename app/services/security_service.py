from app.services.llm_service import (
    llm_service
)
import json
import re

class SecurityService:
##############################################
# analyze
##############################################
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

##############################################
# suggest-fix
##############################################
    async def suggest_fix(
        self,
        rule_id: str,
        code: str
    ):

        prompt = f"""
Analyze this security issue.

Rule:
{rule_id}

Code:
{code}

Return ONLY valid JSON.
Do not include explanations outside JSON.

Format:

{{
    "severity":"HIGH",
    "owasp":"A03 Injection",
    "explanation":"",
    "fixed_code":""
}}
"""

        result = await llm_service.ask(
            prompt
        )

        print("RAW LLM RESPONSE:")
        print(result)

        try:
            return json.loads(result)

        except json.JSONDecodeError:

            # Extract JSON block if model wrapped it
            match = re.search(
                r'\{.*\}',
                result,
                re.DOTALL
            )

            if match:

                try:
                    return json.loads(
                        match.group()
                    )

                except Exception:
                    pass

            return {
                "severity":"UNKNOWN",
                "owasp":"UNKNOWN",
                "explanation":
                    "Unable to parse AI response",

                "fixed_code":""
            }
#####################################################

security_service = SecurityService()