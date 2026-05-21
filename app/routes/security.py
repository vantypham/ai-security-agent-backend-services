#router
from fastapi import APIRouter
from app.models import (
    SecurityRequest
)
from app.services.security_service import (
    security_service
)

router = APIRouter()


@router.post("/analyze")
async def analyze(
    request: SecurityRequest
):

    result = await security_service.analyze(

        request.rule_id,
        request.code
    )

    return result


@router.post("/suggest-fix")
async def suggest_fix(
    request: SecurityRequest
):

    result = await security_service.suggest_fix(

        request.rule_id,
        request.code
    )

    return result


@router.get("/health")
async def health():

    return {
        "status":"UP"
    }