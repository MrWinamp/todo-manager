from src.services.tasks_service import TasksService
from src.repositories.tasks_repository import TasksRepository

_tasks_service = TasksService(TasksRepository())

def get_tasks_service() -> TasksService:
    return _tasks_service