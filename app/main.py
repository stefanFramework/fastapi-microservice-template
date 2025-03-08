import logging
import uvicorn

from app.config import current_config, log_config
from app.factory import create_app

app = create_app()

logger = logging.getLogger()

logger.setLevel(log_config.get_current_log_level())

if not logger.handlers:
    logger.addHandler(log_config.create_file_handler())
    logger.addHandler(log_config.create_console_handler())


if __name__ == '__main__':
    logger.info(f"Launching app with debug {current_config.DEBUG}")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=current_config.DEBUG,
        reload_excludes=["logs"]
    )
