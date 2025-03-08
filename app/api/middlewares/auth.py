import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)
print("Handlers en middleware:", logger.handlers)


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Put your logic here
        logger.info("Executing AuthMiddleware")
        response = await call_next(request)
        return response
