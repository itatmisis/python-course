"""
И ещё немного полезных библиотек

Logging
Встроенная библиотека, позволяющая производить логирование данных
"""
import logging

logger = logging.getLogger()
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", datefmt="%y-%m-%d %H:%M:%S"
)


if __name__ == "__main__":
    logger.info("Инфо")
    logger.warning("Предупреждение")
    logger.error("Ошибка")
    logger.critical("Критическая ошибка")
