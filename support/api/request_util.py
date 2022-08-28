"""
all_request - all requests common function

Author: Jeff Bian
Date:2022-08-28
"""
import json
import requests


class RequestUtil:
    session = requests.session()

    def send_request(self, method, url, datas=None, header_type=None, **kwargs):
        method = str(method).lower()
        res = None

        if method == 'get':
            res = RequestUtil.session.request(method=method, url=url, params=datas, **kwargs)
        elif method == 'post':
            if datas and header_type == 'application/json':
                datas = datas
            elif datas:
                datas = json.dumps(datas)
            res = RequestUtil.session.request(method=method, url=url, data=datas, **kwargs)
        else:
            print('Invalid request method')
        return res
