from fastapi import FastAPI
from app.api.middlewares.auth import AuthMiddleware
from app.api.routes.users import router as users_router


def create_app():
    app = FastAPI()
    create_api(app)
    return app


def create_api(app):
    app.add_middleware(AuthMiddleware)

    app.include_router(users_router)



