# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


def get_ret(ret):
    try:
        ret_new = json.loads(str(ret.json()).encode('raw_unicode_escape').decode())
        return ret_new
    except Exception as e:
        return ret.text


if __name__ == '__main__':
    resp = requests.get("http://www.baidu.com")
    print(resp)  # <Response [200]>
    ret = get_ret(resp)
    print(ret)  # 获取到的网页内容
