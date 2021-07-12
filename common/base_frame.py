#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 上午12:27
# @File    : base_frame.py
from utils.LogUtil import Logger


class BaseFrame:

    def setup_class(self):
        Logger.info("--- setup class ---")

    def setup(self):
        Logger.info("--- setup ---")

    def teardown(self):
        Logger.info("--- teardown ---")

    def teardown_class(self):
        Logger.info("--- teardown_class ---")