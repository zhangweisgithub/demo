# -*- coding: utf-8 -*-
import logging
import os
import platform
import time
from cloghandler import ConcurrentRotatingFileHandler as LogHandler

if platform.system() == "Windows":
    from logging.handlers import RotatingFileHandler as LogHandler

ROOT_PATH = os.path.join(os.path.dirname(__file__))


def log_config(f_level=logging.INFO, c_level=logging.CRITICAL, out_path='', filename='info', fix=False):
    logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.log' \
        if not fix else os.path.join(out_path, filename) + '.log'
    print("2:", logfile)
    logger = logging.getLogger(logfile)
    if logger.handlers:
        logger.removeHandler(logger.handlers)
    logger.setLevel(f_level)

    fh = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=50)
    fh.setLevel(f_level)

    ch = logging.StreamHandler()
    ch.setLevel(c_level)

    formatter = logging.Formatter('[%(levelname)s]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger, logfile


def get_app_logger(logfile, path=None):
    out_path = os.path.join(ROOT_PATH, path) if path else ROOT_PATH
    log, filename = log_config(out_path=out_path, filename=logfile, fix=True, c_level=logging.INFO)
    return log


def log(message, log_name="app", level="INFO"):
    logfile = os.path.join(ROOT_PATH, "%s.log" % log_name)
    logger = logging.getLogger(logfile)
    filehandler = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=50)
    streamhandler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')
    streamhandler.setFormatter(formatter)
    filehandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)
    if level.lower() == "info":
        streamhandler.setLevel(logging.INFO)
        filehandler.setLevel(logging.INFO)
        logger.info(message)
    elif level.lower() == "error":
        streamhandler.setLevel(logging.ERROR)
        filehandler.setLevel(logging.ERROR)
        logger.error(message, exc_info=True)
    elif level.lower() == "critical":
        streamhandler.setLevel(logging.CRITICAL)
        filehandler.setLevel(logging.CRITICAL)
        logger.critical(message, exc_info=True)
    elif level.lower() == "warning":
        streamhandler.setLevel(logging.WARNING)
        filehandler.setLevel(logging.WARNING)
        logger.warning(message)
    logger.removeHandler(streamhandler)
    logger.removeHandler(filehandler)


def test(log):
    log.info("start run......")
    try:
        print(1 / 0)
    except Exception as e:
        log.error(f"error:{e}")


if __name__ == '__main__':
    # logger = log_config(c_level=logging.INFO)[0]   # 这种每次会每次会生成多个log文件
    log = get_app_logger("app")  # 这种就是在app.log中添加对应的错误信息
    test(log)
