from fastapi import FastAPI
from src.infra.routers import router

app = FastAPI( title="Minha API de Exemplo",
    description="API para gerenciar TODOs",
    version="1.0.0")

app.include_router(router)