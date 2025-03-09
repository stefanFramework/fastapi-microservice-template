import logging

from app.config import current_config, log_config
from app.factory import create_app

app = create_app()

logger = logging.getLogger()

logger.setLevel(log_config.get_current_log_level())

if not logger.handlers:
    logger.addHandler(log_config.create_file_handler())
    logger.addHandler(log_config.create_console_handler())


if __name__ == '__main__':
    logger.info(f"Launching app in {current_config.ENVIRONMENT} environment")