from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    first_name: str
    last_name: str
