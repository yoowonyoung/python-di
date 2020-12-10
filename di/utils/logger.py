import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from di.utils.config.settings import config

# log ex : [yyyy-MM-dd HH:mm:ss,SSS][INFO][function:lineno][Messages]
FORMATTER = logging.Formatter("[%(asctime)s][%(levelname)s][%(funcName)s:%(lineno)d][%(message)s]")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(log_path, logger_name):
    file_handler = RotatingFileHandler(f'{log_path}/{logger_name}.log',
                                       maxBytes=(1024 * 1024 * 5) if config['LOG_LIMIT'] else 0,
                                       backupCount=3)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name, logger_level=logging.INFO, file=True):
    if config['LOG_PATH'] is None or config['LOG_PATH'] == "":
        worker_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(worker_dir, '../logs')
    else:
        log_dir = config['LOG_PATH']

    Path(log_dir).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.handlers.clear()
    if config['DEBUG']:
        logger_level = logging.DEBUG
    logger.setLevel(logger_level)
    if config['CONSOLE_LOG']:
        logger.addHandler(get_console_handler())
    if file:
        logger.addHandler(get_file_handler(log_path=log_dir, logger_name=logger_name))

    return logger
