from contextlib import asynccontextmanager
from fastapi import FastAPI
import router
from database import init_db, close_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(title="Employee Management API",lifespan=lifespan)

app.include_router(router)

@app.get("/health")
async def health_endpoint():
    return {"status":"Healthy"}