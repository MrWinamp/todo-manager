from todo_manager.services.tasks_service import TasksService
from todo_manager.repositories.tasks_repository import TasksRepository

_tasks_service = TasksService(TasksRepository())

def get_tasks_service() -> TasksService:
    return _tasks_service