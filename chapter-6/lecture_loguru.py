"""
И ещё немного полезных библиотек

Loguru
Аналог Logging, но красивее!
pip install loguru
"""
from loguru import logger
logger.level('ERROR')


if __name__ == "__main__":
    logger.warning('Предупреждение')
    logger.error('Ошибка')
    logger.critical('Критическая ошибка')
