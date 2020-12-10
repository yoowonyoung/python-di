import logging
import os

from testfixtures import log_capture

from di.utils.config.settings import config
from di.utils.logger import get_logger


@log_capture()
def test_logger_level_debug(capture):
    logger = get_logger(__name__, logger_level=logging.DEBUG)
    assert logger.level == logging.DEBUG

    logger.debug('a debug')
    logger.info('a message')
    logger.error('an error')
    capture.check(
        (__name__, 'DEBUG', 'a debug'),
        (__name__, 'INFO', 'a message'),
        (__name__, 'ERROR', 'an error')
    )


@log_capture()
def test_logger_level_info(capture):
    config['DEBUG'] = False
    logger = get_logger(__name__)
    assert logger.getEffectiveLevel() == logging.INFO

    logger.debug('a debug')
    logger.info('a message')
    logger.error('an error')
    capture.check(
        (__name__, 'INFO', 'a message'),
        (__name__, 'ERROR', 'an error')
    )


@log_capture()
def test_config_set_debug(capture):
    config['DEBUG'] = True
    logger = get_logger(__name__)
    assert logger.getEffectiveLevel() == logging.DEBUG
    logger.debug('a debug')
    logger.info('a message')
    logger.error('an error')
    capture.check(
        (__name__, 'DEBUG', 'a debug'),
        (__name__, 'INFO', 'a message'),
        (__name__, 'ERROR', 'an error')
    )
    config['DEBUG'] = False


def test_logger_no_handlers():
    expected = 0
    if config['CONSOLE_LOG']:
        expected += 1
    logger = get_logger(__name__, file=False, logger_level=logging.INFO)
    assert len(logger.handlers) == expected


def test_logger_with_file_handler():
    expected = 1
    if config['CONSOLE_LOG']:
        expected += 1

    logger = get_logger(__name__, file=True, logger_level=logging.INFO)
    assert len(logger.handlers) == expected


def test_logger_with_config_console_log():
    config['CONSOLE_LOG'] = True
    logger = get_logger(__name__, file=False, logger_level=logging.INFO)
    assert len(logger.handlers) == 1
    config['CONSOLE_LOG'] = False


def test_logger_with_config_log_path():
    config['LOG_PATH'] = '/tmp/test/logs'
    logger = get_logger(__name__, file=False, logger_level=logging.INFO)
    assert os.path.exists(config['LOG_PATH'])
    os.rmdir(config['LOG_PATH'])
    config['LOG_PATH'] = ''


def test_logger_with__empty_logger_name():
    config['LOG_PATH'] = '/tmp/test/logs'
    logger = get_logger('', file=False, logger_level=logging.INFO)
    assert os.path.exists(config['LOG_PATH'])
    os.rmdir(config['LOG_PATH'])
    config['LOG_PATH'] = ''
