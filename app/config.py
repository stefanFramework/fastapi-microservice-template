import os
import sys
import json
import logging

from typing import Literal

from datetime import timedelta, datetime

from logging.handlers import TimedRotatingFileHandler
from pythonjsonlogger.jsonlogger import JsonFormatter

from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    ENV: Literal['DEV', 'TEST', 'PROD'] = 'DEV'

    NAME: str = 'microservice-starter'

    # When set tu True, it ignores middleware authentication
    SKIP_AUTH: bool = False

    # Multiple language support
    LOCALE: str = 'en'

    # For CORS purposes
    FRONTEND_URL: str = ''

    # Track inserts, updates, and deletes for models. Signals before or during session.flush() and session.commit()
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Ex: postgresql://<user>:<pass>@<host>:<port>/<database>
    SQLALCHEMY_DATABASE_URI: str = ''

    # The number of connections to keep open inside the connection pool
    SQLALCHEMY_DATABASE_POOL_SIZE: int = 5

    JWT_SECRET_KEY: str = 'M1CR0S3RV1C3'
    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_LOCATION: list = ['headers']
    JWT_HEADER_NAME: str = "Authorization"
    JWT_HEADER_TYPE: str = "Bearer"
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(hours=6)  # Expires in 6 hours
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(days=3)  # Expires in 3 days

    GOOGLE_CLIENT_ID: str = ''
    GOOGLE_SECRET_KEY: str = ''

    DEFAULT_LOG_FILE_FORMAT: str = '%(asctime)s %(levelname)s %(name)s %(message)s %(pathname)s %(lineno)d %(module)s %(funcName)s'
    DEFAULT_LOG_CONSOLE_FORMAT: str = '[%(asctime)s] (%(name)s) %(levelname)s: %(message)s'

    LOG_LEVEL: str = 'INFO'

    LOG_FILENAME: str = 'storage/logs/mss.log'
    LOG_BACKUP_COUNT: int = 7
    LOG_ROTATION_INTERVAL: int = 1
    LOG_ROTATION_INTERVAL_UNIT: str = 'D'

    LOG_FILE_FORMAT: str = DEFAULT_LOG_FILE_FORMAT
    LOG_CONSOLE_FORMAT: str = DEFAULT_LOG_CONSOLE_FORMAT

    def get_file_handler(self):
        handler = TimedRotatingFileHandler(
            filename=self.LOG_FILENAME,
            when=self.LOG_ROTATION_INTERVAL_UNIT,
            backupCount=self.LOG_BACKUP_COUNT,
            interval=self.LOG_ROTATION_INTERVAL,
            encoding='utf-8'
        )
        formatter = JsonFormatter(fmt=self.LOG_FILE_FORMAT, json_encoder=CustomJsonEncoder)
        handler.setFormatter(formatter)
        return handler

    def get_console_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(fmt=self.LOG_CONSOLE_FORMAT)
        handler.setFormatter(formatter)
        return handler

    def get_current_log_level(self):
        return self.LOG_LEVEL


current_config = BaseConfig()
current_config = BaseConfig(_env_file=['.env', f'.env{current_config.ENV.lower()}'])
