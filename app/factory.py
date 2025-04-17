from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.middlewares.auth import AuthMiddleware
from app.api.routes import users, utils



def create_app():
    app = FastAPI()
    create_api(app)
    return app


def create_api(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost",
            "http://localhost:8000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(AuthMiddleware)

    app.include_router(users.router, prefix="/users")
    app.include_router(utils.router, prefix="/utils")



