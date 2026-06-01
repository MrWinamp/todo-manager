from todo_manager.api.models.models import NewTask, Task
from todo_manager.repositories.tasks_repository import TasksRepository

class TasksService():
    def __init__(self, repository: TasksRepository):
        self.__repository = repository

    async def create_task(self, new_task: NewTask) -> int:
        return await self.__repository.create_task(new_task)
    
    async def delete_task(self, id: int):
        return await self.__repository.delete_task(id)
    
    async def get_tasks(self) -> list[Task]:
        return await self.__repository.get_tasks()
    
    async def update_task(self, task: Task) -> bool:
        return await self.__repository.update_task(task)