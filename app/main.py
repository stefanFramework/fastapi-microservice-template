import logging

from app.config import current_config
from app.factory import create_app

app = create_app()

logger = logging.getLogger(__name__)

logger.setLevel(current_config.get_current_log_level())

if not logger.handlers:
    logger.addHandler(current_config.get_file_handler())
    logger.addHandler(current_config.get_console_handler())


if __name__ == '__main__':
    logger.info(f"Launching app in {current_config.ENV} environment")
