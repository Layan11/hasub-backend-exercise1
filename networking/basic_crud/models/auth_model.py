from pydantic import BaseModel
from roles import Roles


class auth_model(BaseModel):
    username: str
    password: str
    role: Roles
