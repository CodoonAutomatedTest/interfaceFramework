# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 上午12:31
# @File    : test_api.py
import pytest

from common.base_frame import BaseFrame
from utils.ParsUtil import read_yaml_data


class TestApi(BaseFrame):

    @pytest.mark.parametrize('args', read_yaml_data("traning.yaml"))
    def test_traning_modules(self, args):
        url = args['api_request']['url']
        port = args['api_request']['port']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        parmas = args['api_request']['parmas']
        validate = args['api_validate']

        res = self.httpRequest.send_request(method=method, url=url, port=port, headers=headers, data=parmas)
        for val in validate:
            assert res.status_code == val['eq']['code']

    @pytest.mark.parametrize('args', read_yaml_data("advertisement.yaml"))
    def test_advert_modules(self, args):
        url = args['api_request']['url']
        port = args['api_request']['port']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        parmas = args['api_request']['parmas']
        validate = args['api_validate']

        res = self.httpRequest.send_request(method=method, url=url, port=port, headers=headers, data=parmas)
        self.logger.debug(res.text)
        for val in validate:
            assert res.status_code == val['eq']['code']
    # def test_02(self):
    #     Logger.info("test_04")
    #     print('测试用例4')
