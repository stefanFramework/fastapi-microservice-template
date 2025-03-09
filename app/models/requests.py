from pydantic import BaseModel


class UserRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


