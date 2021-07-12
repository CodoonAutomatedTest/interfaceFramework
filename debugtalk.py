#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 上午11:22
# @File    : debugtalk.py
import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
