import logging
import os.path


def set_logger(name_logger: str) -> logging.Logger:
    """
    Создает и настраивает объект логгера с заданным именем.
    Пишет логи в папку /logg в файл log.log
    По умолчанию стоит уровень ERROR
    Пример формата:
        11.11.2023 18:47:50 example_logger       WARNING    This is a warning message.

    Arguments:
        name_logger (str): Имя логгера.

    Returns:
        logging.Logger: Объект логгера.

    Example:
        >>> logger = set_logger('example_logger')
        >>> logger.warning('This is a warning message.')
    """
    logger = logging.getLogger(name_logger)
    logger.setLevel(logging.ERROR)
    file_handler = logging.FileHandler('core/logg/log.log')
    file_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.info('===START LOGGING===')
    return logger

