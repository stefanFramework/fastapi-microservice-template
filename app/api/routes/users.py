import logging

from typing import List
from fastapi import APIRouter, HTTPException, Depends

from app.models.requests import User

logger = logging.getLogger(__name__)
router = APIRouter()


class UserResource:
    @staticmethod
    @router.post("/users", response_model=User)
    def create_user(user: User):
        # Add new user on DB
        logger.info(f"Creating user {user}")
        return user

    @staticmethod
    @router.get("/users", response_model=List[User])
    def get_all_users():
        return [
            User(
                email="example@example.com",
                password="",
                first_name="John",
                last_name="Doe"
            ),
        ]


UserResource()


