import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


class UtilsResource:
    @staticmethod
    @router.get("/health")
    def health():
        return {"status": "ok"}


UtilsResource()


