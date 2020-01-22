# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import platform
from python_basic.time与datetime import time
from cloghandler import ConcurrentRotatingFileHandler as LogHandler
if platform.system() == "Windows":
    from logging.handlers import RotatingFileHandler as LogHandler

ROOT_PATH = os.environ.get("HOME_PATH")


def log_config(f_level=logging.INFO, c_level=logging.CRITICAL, out_path='', filename='info', fix=False):
    logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.log' \
        if not fix else os.path.join(out_path, filename) + '.log'
    logger = logging.getLogger(logfile)
    if logger.handlers:
        logger.removeHandler(logger.handlers)
    logger.setLevel(f_level)

    fh = LogHandler(logfile, maxBytes=100*1024*1024, backupCount=50)
    fh.setLevel(f_level)

    ch = logging.StreamHandler()
    ch.setLevel(c_level)

    formatter = logging.Formatter('[%(levelname)s]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger, logfile


# class Log(object):
#
#     def __init__(self, f_level=logging.INFO, c_level=logging.CRITICAL, out_path='', filename="info", fix=False):
#         logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.log' \
#             if not fix else os.path.join(out_path, filename) + '.log'
#         self.logger = logging.getLogger(logfile)
#         if not self.logger.handlers:
#             # loggger 文件配置路径
#             self.handler = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=50)
#             self.handler.setLevel(f_level)
#
#             self.stream = logging.StreamHandler()
#             self.stream.setLevel(c_level)
#
#             formatter = logging.Formatter(
#                 '[%(levelname)s]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')
#             self.handler.setFormatter(formatter)
#             self.stream.setFormatter(formatter)
#
#             self.logger.addHandler(self.handler)
#             self.logger.addHandler(self.stream)
#
#     def info(self, message=None):
#         self.__init__()
#         self.logger.info(message)
#         self.logger.removeHandler(self.logger.handlers)
#
#     def debug(self,message=None):
#         self.__init__()
#         self.logger.debug(message)
#         self.logger.removeHandler(self.logger.handlers)
#
#     def warning(self,message=None):
#         self.__init__()
#         self.logger.warning(message)
#         self.logger.removeHandler(self.logger.handlers)
#
#     def error(self,message=None):
#         self.__init__()
#         self.logger.error(message)
#         self.logger.removeHandler(self.logger.handlers)
#
#     def critical(self, message=None):
#         self.__init__()
#         self.logger.critical(message)
#         self.logger.removeHandler(self.logger.handlers)


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
    try:
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
    finally:
        logger.removeHandler(streamhandler)
        logger.removeHandler(filehandler)


if __name__ == '__main__':
    import traceback
    try:
        1/0
    except Exception as e:
        # traceback.print_exc()          # 这个数据会直接打印在哪一行出现了什么类型的错误
        # print(traceback.format_exc())   # traceback.format_exc():这个不会打印在控制台中,但是会返回一个字符串,除了不直接打印出来,效果跟traceback.print_exc()是一样的
        traceback.format_exc()
        log(e)
