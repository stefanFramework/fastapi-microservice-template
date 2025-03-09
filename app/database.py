from sqlmodel import create_engine, Session, SQLModel
from app.config import current_config


engine = create_engine(current_config.SQLALCHEMY_DATABASE_URI)


def get_session():
    with Session(engine) as session:
        yield session
