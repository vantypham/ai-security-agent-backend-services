from fastapi import FastAPI
from app.routes.security import router

app = FastAPI(
    title="AI Security Agent"
)

app.include_router(
    router
)