from todo_manager.api.endpoints.tasks import router
from todo_manager.core.logger import logger

from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

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

def main() -> None:
    uvicorn.run(
        "todo_manager.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug",
    )

if __name__ == "__main__":
    main()