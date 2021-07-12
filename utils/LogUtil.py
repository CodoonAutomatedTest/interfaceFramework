#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 上午10:55
# @File    : LogUtil.py

import logging, os, time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
format = logging.Formatter(
            '[%(asctime)s][%(filename)s->%(funcName)s (line:%(lineno)d)]: %(message)s')
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Logger.err_handler)
    logger.addHandler(Logger.handler)
    logger.addHandler(Logger.console)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Logger.err_handler)
    logger.removeHandler(Logger.handler)
    logger.removeHandler(Logger.console)


def get_current_time():
    return time.strftime(Logger.date, time.localtime(time.time()))


class Logger:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path+'/Log/log.log'
    err_file = path+'/Log/err.log'
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    # 将日志输出到屏幕
    console = logging.StreamHandler()
    console.setLevel(LEVELS.get(level, logging.NOTSET))
    console.setFormatter(format)
    # 将日志输出到文件
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')
    handler.setFormatter(format)
    err_handler.setFormatter(format)

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL]" + log_meg)
        remove_handler('critical')
