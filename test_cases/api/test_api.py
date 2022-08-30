"""
test_api.py -

Author: Jeff Bian
Date:2022-08-28
"""
import time
import pytest

import allure
from support.api.request_util import RequestUtil
from support.api.response_util import response_write_to_xlsx, merge_xlsx, attach_log_file
from support.api.yaml_util import read_testcase_yaml


@allure.feature('Test input/product api to get logs (API)')
class TestApi:

    @allure.title('Testing get_catlog api with invalid method')
    @pytest.mark.parametrize('get_catlog_fail', read_testcase_yaml('get_catlog_fail.yaml'))
    def test_get_catlog_fail(self, get_catlog_fail):
        url = get_catlog_fail['request']['url']
        res = RequestUtil().send_request(method=get_catlog_fail['request']['method'], url=url)
        if res is not None:
            assert get_catlog_fail['validate'][0]['eq']['err_code'] == res.status_code
        else:
            assert get_catlog_fail['validate'][0]['eq']['err'] == res

    @allure.title('Monitor the progress of the system generating a catalog output')
    def test_get_catlog(self):
        url = 'https://6306707cdde73c0f845aa718.mockapi.io/input'
        counter = 0
        index = 0
        while counter < 60:
            res = RequestUtil().send_request(method='get', url=url)
            res_lists = res.json()
            response_write_to_xlsx(res_lists, f'catlog-{index}')
            time.sleep(5)
            counter += 5
            index += 1
        with allure.step('catlog is stored in ./output/api/final-catlog.xlsx'):
            merge_xlsx('catlog')

        attach_log_file('final-catlog.xlsx')

    @allure.title('Monitor the progress of the system generating a product output')
    def test_get_productlog(self):
        url = 'https://6306707cdde73c0f845aa718.mockapi.io/product'
        counter = 0
        index = 0
        while counter < 60:
            res = RequestUtil().send_request(method='get', url=url)
            res_lists = res.json()
            response_write_to_xlsx(res_lists, f'productlog-{index}')
            time.sleep(5)
            counter += 5
            index += 1
        with allure.step('prodcut log is stored in ./output/api/final-prodcutlog.xlsx'):
            merge_xlsx('productlog')

        attach_log_file('final-productlog.xlsx')
