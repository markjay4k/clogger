#!/usr/bin/env python3

from logging.handlers import RotatingFileHandler
import logging
import sys
import os


class ColorFormatter(logging.Formatter):
    def __init__(self, *args: str, **kwargs: str:)
        super().__init__(*args, **kwargs)
        
        GREY = "\x1b[31;20m"
        YELLOW = "\x1b[33;20m"
        RED = "\x1b[36;20m"
        BOLD_RED = "\x1b[36;1m"
        
        self.colors = {
            logging.DEBUG: GREY,
            logging.INFO: GREY,
            logging.WARNING: YELLOW,
            logging.ERROR: BOLD_RED,
            logging.CRITICAL: BOLD_RED,
        }

        self._fmts = {
            level: self.add_colors(level) for level in self.colors
        }

    def add_colors(self, level: int) -> str:
        _color = self.colors.get(level)
        RESET = "\x1b[0m"
        return self._style._fmt.replace('#c', _color).replace('#r', RESET)

    def format(self, record: int) -> str:
        self._style._fmt = self._fmts[record.levelno] 
        return super().format(record)


def log(
        level: str = 'INFO',
        logdir: str = '.logs',
        max_bytes: int = 524288,
        backup_count: int = 2,
        logger_name: str = __name__,
    ) -> logging.Logger:
    
    loglevel = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITITCAL': logging.CRITICAL
    }

    try:
        level = loglevel[level.upper()]
    except (KeyError, AttributeError) as e:
        _err = f'invalid level {e}: using default value "INFO" instead'
        level = logging.INFO
    else:
        _err = None

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    ftime = '{asctime:15s}'
    module = '{module:7s}'
    clevel = '#c{levelname:8s}#r'
    message = '{message}'
    formatter = ColorFormatter(
        fmt=f'{ftime}| {module} {clevel} | {message}',
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

