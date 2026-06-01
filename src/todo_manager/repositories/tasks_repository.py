from todo_manager.api.models.models import Task, NewTask
import copy

class TasksRepository():
    def __init__(self):
        self.__tasks: list[Task] = list()
        self.__id: int = 0
    
    async def create_task(self, new_task: NewTask) -> int:
        self.__id = self.__id + 1
        task = Task(**new_task.model_dump(), id=self.__id, status="process")
        self.__tasks.append(task)
        return self.__id
    
    async def delete_task(self, id: int) -> bool:
        task = None
        for iter_task in self.__tasks:
            if iter_task.id == id:
                task: Task = iter_task
        if task is not None:
            self.__tasks.remove(task)
            return True
        return False

    async def get_tasks(self) -> list[Task]:
        tasks: list[Task] = copy.deepcopy(self.__tasks)
        return tasks
    
    async def update_task(self, task: Task) -> bool:
        old_task = None
        for iter_task in self.__tasks:
            if iter_task.id == task.id:
                old_task: Task = iter_task
        if old_task is not None:
            index: int = self.__tasks.index(old_task)
            self.__tasks.pop(index)
            self.__tasks.insert(index, task)
            return True
        return False
