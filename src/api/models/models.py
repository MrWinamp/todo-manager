from typing import Literal, Union, Optional

from pydantic import BaseModel

class NewTask(BaseModel):
    name: str
    description: Optional[str] = ""

class Task(NewTask):
    id: int
    status: Union[
            Literal["process"],
            Literal["done"]
        ]