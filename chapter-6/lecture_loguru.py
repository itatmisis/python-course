"""
И ещё немного полезных библиотек

Loguru
Аналог Logging, но красивее!
pip install loguru
"""
import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="WARNING")


if __name__ == "__main__":
    logger.info("Инфо")
    logger.warning("Предупреждение")
    logger.error("Ошибка")
    logger.critical("Критическая ошибка")
