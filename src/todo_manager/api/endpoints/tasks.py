from todo_manager.services.tasks_service import TasksService
from todo_manager.api.dependends import get_tasks_service
from todo_manager.core.logger import logger

from fastapi import APIRouter, Response, status, Depends
from todo_manager.api.models.models import Task, NewTask

router = APIRouter()

@router.get("")
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}

@router.post("/tasks", response_model=int)
async def create_task(
                        new_task: NewTask,
                        service: TasksService = Depends(get_tasks_service)
                    ) -> int:
    result: int = await service.create_task(new_task)
    return result

@router.delete("/tasks")
async def delete_task(
                        id: int,
                        service: TasksService = Depends(get_tasks_service)
                    ) -> Response:
    ok = await service.delete_task(id)
    if not ok:
        logger.warning(f"Failed delete operation for task whith {id=}. Missing task.")
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=status.HTTP_200_OK)

@router.patch("/tasks")
async def update_task(
                        task: Task,
                        service: TasksService = Depends(get_tasks_service)
                    ) -> Response:
    ok: bool = await service.update_task(task)
    if not ok:
        logger.warning(f"Failed delete operation for task whith {task.id=}. Missing task.")
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=status.HTTP_200_OK)

@router.get("/tasks", response_model=list[Task])
async def get_tasks(service: TasksService = Depends(get_tasks_service)) -> list[Task]:
    result: list[Task] = await service.get_tasks()
    return result