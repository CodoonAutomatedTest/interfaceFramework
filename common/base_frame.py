#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 上午12:27
# @File    : base_frame.py
from utils.LogUtil import Logger
from utils.ReqUtil import RequestUtil

class BaseFrame:

    def setup_class(self):
        Logger.info("--- setup class ---")
        # 创建日志类对象
        self.logger = Logger()
        # 获得接口请求对象
        self.httpRequest = RequestUtil(self.logger)

    def setup(self):
        Logger.info("--- setup ---")

    def teardown(self):
        Logger.info("--- teardown ---")

    def teardown_class(self):
        Logger.info("--- teardown_class ---")