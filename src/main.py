from src.api.endpoints.tasks import router
from src.core.logger import logger

from contextlib import asynccontextmanager

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application...")

    yield

    logger.info("Shutting down application...")

app = FastAPI(
    title="TODO Manager Test Server",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router=router, prefix="/api/v1")