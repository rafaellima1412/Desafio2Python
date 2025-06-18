from fastapi import FastAPI
from src.infra.routers import router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
    "message": "Hello World"
    }

app.include_router(router)