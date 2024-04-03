from pydantic import BaseModel


class Roles(BaseModel):
    user: "user"
    admin: "admin"
