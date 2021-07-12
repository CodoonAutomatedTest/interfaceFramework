#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 下午11:18
# @File    : BaseFrame.py
import pytest
import os, time


if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system('allure generate ./temp -o ./reports --clean')