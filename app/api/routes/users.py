import logging

from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.models.requests import UserRequest
from app.database import get_session
from app.models.db import User

logger = logging.getLogger(__name__)

router = APIRouter()


class UserResource:
    @staticmethod
    @router.post("/", response_model=UserRequest)
    def create_user(user_request: UserRequest, session: Session = Depends(get_session)):
        logger.info(f"Creating user {user_request}")
        user = User(
            email=user_request.email,
            password=user_request.password,
            first_name=user_request.first_name,
            last_name=user_request.last_name,
        )
        session.add(user)
        session.commit()

        return user_request


    @staticmethod
    @router.get("/", response_model=List[UserRequest])
    def get_all_users(session: Session = Depends(get_session)):
        users = session.exec(select(User)).all()
        return [
            UserRequest(
                email=u.email,
                password="",
                first_name=u.first_name,
                last_name=u.last_name
            ) for u in users
        ]


UserResource()


