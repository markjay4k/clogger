#!/usr/bin/env python3

from logging.handlers import RotatingFileHandler
import logging
import sys
import os


def log(
        level: str = 'INFO',
        logdir: str = '.',
        max_bytes: int = 524288,
        backup_count: int = 2,
    ) -> logging.Logger:
    """
    simple logger using python's logging module and RotatingFileHandler
    """
    
    loglevel = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITITCAL': logging.CRITICAL
    }

    try:
        level = loglevel[level.upper()]
    except KeyError as e:
        _err = f'invalid loglevel {e}: using "INFO"'
        level = logging.INFO
    else:
        _err = None

    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    formatter = logging.Formatter(
        fmt='{asctime}.{msecs:03.0f}| ({module}) {levelname}: {message}',
        datefmt='%Y-%m-%d %H:%M:%S',
        style='{'
   )
    if not os.path.isdir(logdir): 
        os.mkdir(logdir)

    file_handler = RotatingFileHandler(
        f'{logdir}/{os.path.split(os.path.abspath("."))[-1]}.log',
        mode='a', maxBytes=max_bytes,
        backupCount=backup_count, encoding=None, 
        delay=0
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if _err is not None:
        logger.warning(f'{_err}. level options: {list(loglevel.keys())}')

    return logger

