from typing import List
from pydantic import BaseModel


class student_model(BaseModel):
    name: str
    id: str
    age: int
    classes: List[str]
