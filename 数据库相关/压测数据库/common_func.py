# -*- coding: utf-8 -*-

from io import TextIOWrapper

import requests
import json
from requests.exceptions import ConnectionError
import uuid
import traceback
import inspect
import functools
import logging
import os
import time
from logging.handlers import RotatingFileHandler as LogHandler


def log_config(f_level=logging.INFO, c_level=logging.ERROR, out_path='', filename='info', fix=False):
    logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.log' \
        if not fix else os.path.join(out_path, filename) + '.log'
    logger = logging.getLogger(logfile)

    if f_level is None:
        if c_level is None:
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(c_level)
    else:
        logger.setLevel(f_level)

    formatter = logging.Formatter(
        '[%(levelname)s][%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')

    if c_level is not None:
        ch = logging.StreamHandler()
        ch.setLevel(c_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if f_level is not None:
        fh = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=100)
        fh.setLevel(f_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger, logfile


def get_item_by_key(obj, key, result=None):
    if isinstance(obj, dict):
        for k in obj:
            if key == k:
                if isinstance(result, list):
                    if isinstance(obj[k], list):
                        result.extend(obj[k])
                    else:
                        result.append(obj[k])
                elif result is None:
                    result = obj[k]
                else:
                    result = [result, obj[k]]
            else:
                if isinstance(obj[k], dict) or isinstance(obj[k], list):
                    result = get_item_by_key(obj[k], key, result)
    elif isinstance(obj, list):
        for i in obj:
            if isinstance(i, dict) or isinstance(i, list):
                result = get_item_by_key(i, key, result)
    return result[0] if isinstance(result, list) and len(result) == 1 else result


def flow(func):
    @functools.wraps(func)
    def wrap(config, log):
        config['log'] = log
        params = {}
        for key in inspect.getfullargspec(func).args:
            if key in config:
                params[key] = config[key]
        try:
            r = func(**params)
            if isinstance(r, list):
                response = []
                for elem in r:
                    if elem[1]:
                        response.append({"title": func.__doc__ + elem[0],
                                         "result": "Pass",
                                         "detail": '\n'.join(elem[2:])})
                    else:
                        response.append({"title": func.__doc__ + elem[0],
                                         "result": "Fail",
                                         "detail": '\n'.join(elem[2:])})
                return response
            else:
                result_dict = {"name": func.__name__, "title": func.__doc__, "result": "Fail"}

                if r is True:
                    result_dict["result"] = "Pass"
                elif not type(r) is bool:
                    result_dict["reason"] = str(r)

                return [result_dict]
        except:
            e = str(traceback.format_exc())
            log.error(e)
            return [{"title": func.__doc__, "result": "Fail", "reason": e}]
    return wrap



def sort_data(di):
    """
    :param di: 输入参数的params
    :return:
    """
    for k in di.keys():
        if di[k] is None:
            di.pop(k)
    return "".join(["{0}={1}&".format(k, di[k]) for k in sorted(di.keys())])[:-1]


def decode_str(content, encoding='utf-8'):
    # 只支持json格式
    # indent 表示缩进空格数
    import json
    return json.dumps(content,ensure_ascii=False, indent=4)


def retry(times):
    global count
    count = 0

    def decorated(func):
        def wrapper(*args, **kwargs):
            global result
            try:
                result = func(*args, **kwargs)
            except ConnectionError as e:
                global count
                count += 1
                # print("This is count %s" % count)
                if count < times:
                    wrapper(*args, **kwargs)
                result = {"ret": str(e)}
            return result

        return wrapper

    return decorated


@retry(5)
def request_data(url, method, param=None, **kwargs):
    """
    :param url: 接口请求地址url
    :param method: 请求的方法（DEBUG或者MOCK，其中MOCK为自己构造的返回）
    :param param: 请求参数
    :param kwargs: 其他需要的kwargs
    :return: 请求返回数据
    """
    ret = None
    # import pdb
    # pdb.set_trace()
    if method.upper() == "POST":
        # print(param, kwargs)
        ret = requests.post(url, param, **kwargs)
    elif method.upper() == "GET":
        ret = requests.get(url, params=param, **kwargs)
    elif method.upper() == "DELETE":
        ret = requests.delete(url, **kwargs)
    elif method.upper() == "PUT":
        ret = requests.put(url, json=param, **kwargs)
    elif method.upper() == "PATCH":
        ret = requests.patch(url, json=param, **kwargs)
    # log(param)
    # log(ret.text)
    try:
        ret_new = ret.json()
        if isinstance(ret_new, list) or isinstance(ret_new, int):
            ret_new = {"status_code": ret.status_code, "elapsed": ret.elapsed.microseconds / 1000, "ret": ret_new}
        elif isinstance(ret_new, str):
            ret_new = get_ret(ret)
            ret_new.update({"status_code": ret.status_code, "elapsed": ret.elapsed.microseconds / 1000})
        else:
            ret_new.update({"status_code": ret.status_code, "elapsed": ret.elapsed.microseconds / 1000})
        return ret_new
    except Exception as e:
        return {"status_code": ret.status_code, "ret": ret.text, "elapsed": ret.elapsed.microseconds / 1000}


def get_ret(ret):
    try:
        ret_new = json.loads(str(ret.json()).encode('raw_unicode_escape').decode())
        return ret_new
    except Exception as e:
        return ret.text


def restful_api(req_url, req_method, params=None, files=None, headers=None, cookies=None, cert=None, timeout=30,
                log=None):
    post_query_param = None
    if isinstance(params, dict):
        if params and "post_query_param" in params.keys():
            post_query_param = params["post_query_param"]
            params.pop("post_query_param")
    if post_query_param:
        if req_method.upper() == "POST" or req_method.upper() == "PUT" or req_method.upper() == "DELETE":
            suffix = sort_data(post_query_param)
            req_url = req_url + "?" + suffix
    if req_method.upper() == "POST":
        if headers and "Content-Type" in headers.keys() and "x-www-form-urlencoded" in headers["Content-Type"]:
            ret = request_data(req_url, req_method, params, files=files, headers=headers, cookies=cookies,
                               cert=cert, allow_redirects=False, timeout=timeout)
        elif headers and "Content-Type" in headers.keys() and "form-data" in headers["Content-Type"]:
            boundary_str = '-------' + str(uuid.uuid4()).replace('-', '')
            from requests_toolbelt.multipart.encoder import MultipartEncoder
            form_data_params = params.copy()
            if files and isinstance(files, dict):
                form_data_params.update(files)
            ms = MultipartEncoder(
                fields=form_data_params,
                boundary=boundary_str
            )
            headers.update({"Content-Type": ms.content_type})
            ret = request_data(req_url, req_method, param=ms.to_string(), headers=headers, cookies=cookies,
                               cert=cert, allow_redirects=False, timeout=timeout)
        else:
            ret = request_data(req_url, req_method, json=params, files=files, headers=headers, cookies=cookies,
                               cert=cert, allow_redirects=False, timeout=timeout)
    elif req_method.upper() == "DELETE":
        ret = request_data(req_url, req_method, json=params, headers=headers, cookies=cookies, cert=cert,
                           allow_redirects=False, timeout=timeout)
    else:
        ret = request_data(req_url, req_method, params, headers=headers, cookies=cookies, cert=cert,
                           allow_redirects=False, timeout=timeout)
    if log:
        try:
            log.info(req_method + ": " + req_url)
            log.info(decode_str(headers))
            log.info(decode_str(params))
            log.info(str(files))
            log.info(decode_str(ret))
        except:
            log.error(req_method + ": " + req_url)
            log.error(decode_str(headers))
            log.error(decode_str(params))
            log.error(str(files))
            log.error(decode_str(ret))
    if files:
        if hasattr(files, "close") and isinstance(files, TextIOWrapper):
            files.close()
    return ret


if __name__ == "__main__":
    req_url = "http://172.20.25.142:10219/senseface/portraits/batch/upload"
    req_method = "POST"
    headers = {"accessToken": "325efc9bc6de458e9a96e8cc5c9d26e6"}
    params = {"images": open("C:\\pic.zip", "rb"), "tarLibSerial": (None, "c4c7e856-1831-41e4-8295-367916ff6000")}
    result = restful_api(req_url, req_method, files=params, headers=headers)
    print(result)
