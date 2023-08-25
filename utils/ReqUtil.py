#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 下午9:58
# @File    : ReqUtil.py

import json
import requests
from .ParsUtil import read_config_yaml, read_extract_yaml


class RequestUtil:

    def __init__(self, logger):
        # 获得日志对象
        self.logger = logger
        # 初始化基本路径
        self.base_url = read_config_yaml('url', 'base_url')
        self.base_url = read_config_yaml('url', 'base_url')
        # 初始化请求头
        self.last_headers = {}
        # 初始化请求数据
        self.last_data = {}

    def _get(self, url, headers, data):
        return requests.get(url=url, headers=headers, params=data)

    def _post(self, url, headers, data):
        return requests.post(url=url, headers=headers, data=data)

    def _delete(self, url, headers, data):
        return requests.delete(url=url, headers=headers, data=data)

    def _put(self, url, headers, data):
        return requests.delete(url=url, headers=headers, data=data)

    # 请求封装
    def send_request(self, method, url, port, headers=None, data=None):
        # method参数转换成小写
        self.last_method = str(method).lower()
        # 处理请求路径
        # 请求路径等于基本路径加接口路径
        self.last_url = self.base_url + port + url
        # 如果headers不为None并且为字典类型，则在self.headers中增加请求头
        if headers and isinstance(headers, dict):
            for key, value in headers.items():
                if str(value).startswith("${") and str(value).endswith("}"):  # 参数提取
                    self.last_headers[str(key)] = read_extract_yaml(str(value)[2:-1], 'api_token')
                else:
                    self.last_headers[str(key)] = str(value)
        # 如果data不为None并且为字典类型，则转换成json字符串
        if data and isinstance(data, dict):
            for key, value in data.items():
                if str(value).startswith("${") and str(value).endswith("}"):  # 参数提取
                    data[str(key)] = read_extract_yaml(str(value)[2:-1], 'api_token')
                else:
                    # data[str(key)] = str(value)
                    data[str(key)] = value
            self.last_data = json.dumps(data)
        # 打印最终的数据
        res = ''
        if self.last_method == 'get':
            res = self._get(self.last_url, self.last_headers, self.last_data)
        elif self.last_method == 'post':
            res = self._post(self.last_url, self.last_headers, self.last_data)
        elif self.last_method == 'delete':
            res = self._delete(self.last_url, self.last_headers, self.last_data)
        elif self.last_method == 'put':
            res = self._put(self.last_url, self.last_headers, self.last_data)
        return res