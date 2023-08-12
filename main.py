from fastapi import FastAPI

from core.routes import router as core_router

app = FastAPI(title="Titanic Survival")

app.include_router(core_router)
