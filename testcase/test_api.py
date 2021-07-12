#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 上午12:31
# @File    : test_api.py
from common.base_frame import BaseFrame
from utils.LogUtil import Logger


class TestApi(BaseFrame):

    def test_03(self):
        Logger.info("test_03")
        print('测试用例三')

    def test_04(self):
        Logger.info("test_04")
        print('测试用例4')
