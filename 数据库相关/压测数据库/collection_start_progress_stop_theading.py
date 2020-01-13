#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Eddy'

import sys
import numpy
import threading
from time import sleep
sys.path.append("F:\\Eddy\\13、Python\\guopeng\\test")
from common_func import *


class CollectionRunClass:
    RunNumber = 0
    ErrNumber = 0
    StopError = 0
    ComUserLog = {'method': 'POST', 'uri': '/common/user/login'}
    CollectionList = {'method': 'GET', 'uri': '/auto/collection/list'}
    CollectionRun = {'method': 'POST', 'uri': '/auto/collection/run'}
    CollectionProgress = {'method': 'POST', 'uri': '/auto/collection/progress'}
    CollectionStop = {'method': 'POST', 'uri': '/auto/set/stop'}  # 测试任务测试任务停止是同一个接口，参数不一样
    SleepTime = 20
    Headers = {
        "platform": "sBTShiYxKsZVwu6pIG/5fg==",
        # "source":"ci",
        "Content-Type": "application/json;charset=UTF-8"
    }
    UserConfig = {"host": "10.9.244.37:30080", "feature_version": "24602", "protocol": "HTTP"}
    set_status_dict = {
        0: "待执行",
        1: "已完成",
        2: "执行中",
        3: "已停止",
        4: "执行异常",
        5: "setup",
        6: "teardown",
    }

    def __init__(self, host, log):
        self.host = host
        self.log = log

    def user_log(self, params=None):
        body = {}
        if params and isinstance(params, dict):
            body.update(params)
        url = 'http://{0}{1}'.format(self.host, CollectionRunClass.ComUserLog['uri'])
        response = restful_api(
            req_url=url,
            req_method=CollectionRunClass.ComUserLog['method'],
            params=body,
            headers=CollectionRunClass.Headers,
            log=self.log)
        if response['status_code'] == 200:
            return True, response['data']  # 返回(True,{'token': 'JCXp'})
        else:
            return False, response['code']

    def collection_list(self, collection_nums, params=None):
        body = {
            "page_no": "1",
            "page_size": "200",
            "project_id": "1"
            # ,
            # "title": "37"
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, CollectionRunClass.CollectionList["uri"])
        response = restful_api(
            req_url=url,
            req_method=CollectionRunClass.CollectionList['method'],
            params=body,
            headers=CollectionRunClass.Headers,
            log=self.log)
        __collection_list_dict_all = {}
        __collection_list_dict = {}
        # print(response)
        for i in response["collections"]:
            __collection_list_dict_all.update({i["id"]: i["set_ids"]})  # 返回一个测试任务ID和其包含的测试集id的字典
            # {161: [2738, 2777, 2782, 2779, 2778, 2784], 155: [2738, 2777, 2782, 2779, 2778, 2784]}
        # 返回随机的collection_nums个col ID的列表
        __collection_chose_id_list = numpy.random.choice(list(__collection_list_dict_all),
                                                         size=collection_nums if collection_nums < len(
                                                             __collection_list_dict_all) else len(
                                                             __collection_list_dict_all), replace=False)
        for col_id in __collection_chose_id_list:
            __collection_list_dict.update({col_id: __collection_list_dict_all[col_id]})

        # return response, __collection_list_dict
        return __collection_list_dict

    def collection_run(self, collection_id, params=None):
        body = {
            "collection_id": collection_id,
            # "concurrent": 1,
            # "cc": [],
            # "module": [],
            "setup": {},
            # "rerun": False,
            "teardown": {},
            "user_config": CollectionRunClass.UserConfig
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, CollectionRunClass.CollectionRun["uri"])
        response = restful_api(
            req_url=url,
            req_method=CollectionRunClass.CollectionRun['method'],
            params=body,
            headers=CollectionRunClass.Headers,
            log=self.log)
        return response

    def collection_stop(self, collection_id, set_id, params=None):
        body = {
            "collection_id": collection_id,
            "choice": 2,
            "set_id": set_id
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, CollectionRunClass.CollectionStop["uri"])
        response = restful_api(
            req_url=url,
            req_method=CollectionRunClass.CollectionStop['method'],
            params=body,
            headers=CollectionRunClass.Headers,
            log=self.log)
        return response

    def collection_progress(self, collection_id, params=None):
        body = {
            "collection_ids": [collection_id]
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, CollectionRunClass.CollectionProgress["uri"])
        response = restful_api(
            req_url=url,
            req_method=CollectionRunClass.CollectionProgress['method'],
            params=body,
            headers=CollectionRunClass.Headers,
            log=self.log)
        return response[str(collection_id)]["status"]  # 返回查询的collection_id的状态

    def sep_col_run(self, collection_chose_id, col_set_ids, col_chose_status):
        try:
            self.log.error('选择的测试任务是{}，状态为{}'.format(
                collection_chose_id, CollectionRunClass.set_status_dict.get(col_chose_status, "其他")))
            if col_chose_status not in (2, 5, 6):
                self.log.error("运行测试任务{}".format(collection_chose_id))
                run_response = CollectionRunClass.collection_run(self, collection_chose_id)
                if run_response.get("code") == 0:
                    self.log.error("测试任务{}执行成功！\n等待2分钟后停止".format(collection_chose_id))
                    sleep(120)
                    # 停止测试任务
                    stop_response = CollectionRunClass.collection_stop(self, collection_chose_id, col_set_ids)
                    if stop_response.get("code") == 0:
                        self.log.error("测试任务{}停止成功！\n等待{}秒钟".format(collection_chose_id, CollectionRunClass.SleepTime))
                        sleep(CollectionRunClass.SleepTime)
                        # 查看这个测试任务的状态
                        progress_status = CollectionRunClass.collection_progress(self, collection_chose_id)
                        self.log.error("progress_status {} {}".format(
                            progress_status, CollectionRunClass.set_status_dict.get(progress_status, "其他")))
                        if progress_status == 3:
                            self.log.error("执行正常")
                            CollectionRunClass.RunNumber += 1
                        else:
                            self.log.error("测试任务{}状态为{},{},状态异常".format(
                                collection_chose_id, progress_status,
                                CollectionRunClass.set_status_dict.get(progress_status, "其他")))
                            CollectionRunClass.ErrNumber += 1
                    else:
                        self.log.error("测试任务{}停止失败".format(collection_chose_id))
                        CollectionRunClass.StopError += 1
                else:
                    self.log.error("测试任务{}未执行成功".format(collection_chose_id))
                    CollectionRunClass.ErrNumber += 1
            else:
                self.log.error("执行失败,因为测试任务在运行，停止它")
                stop_response = CollectionRunClass.collection_stop(self, collection_chose_id, col_set_ids)
                if stop_response.get("code") == 0:
                    self.log.error("测试任务{}停止成功！\n等待{}秒钟".format(collection_chose_id, CollectionRunClass.SleepTime))
                    sleep(CollectionRunClass.SleepTime)
                    # 查看这个测试任务的状态
                    progress_status = CollectionRunClass.collection_progress(self, collection_chose_id)
                    if progress_status == 3:
                        self.log.error("执行正常")
                        CollectionRunClass.RunNumber += 1
                    else:
                        self.log.error("测试任务{}状态为{}，状态异常".format(
                            collection_chose_id, CollectionRunClass.set_status_dict.get(progress_status, "其他")))
                        CollectionRunClass.ErrNumber += 1
                else:
                    self.log.error("测试任务{}停止失败".format(collection_chose_id))
                    CollectionRunClass.StopError += 1
        finally:
            self.log.error("正常执行了{}次, 停止失败:{} 出错{}次".format(CollectionRunClass.RunNumber, CollectionRunClass.ErrNumber, CollectionRunClass.ErrNumber))
            self.log.error("*" * 20)


def main():
    collection_nums = 2  # 设定一次性获取的测试任务数量，也是同时跑测试任务的线程数
    host = "10.9.244.33:9000"
    # user_log_info = {"username": "guopeng", "password": "Snc2SGFyZS0tLWluZzIwMjBkUE42"}
    user_log_info = {"username":"zhangwei_vendor","password":"TnRvWncxMjM0NTY3ODlIUXFS"}
    log = log_config(out_path='../logs', filename='collection_start_progress_stop', fix=True)[0]
    collection_run_class = CollectionRunClass(host, log)
    user_log_response = collection_run_class.user_log(params=user_log_info)
    print("登录成功:", user_log_response)
    if user_log_response:
        collection_run_class.Headers.update(user_log_response[1])
    while collection_run_class.RunNumber < 100000000:
        try:
            sleep(120)
            list_response = collection_run_class.collection_list(collection_nums)
            thread_list = []
            # list_response = {204:[2759,2763,2765,2769]}
            for i in list(list_response):
                col_set_ids = list_response[i]
                i = str(i)
                col_chose_status = collection_run_class.collection_progress(i)
                t = threading.Thread(target=collection_run_class.sep_col_run, args=(i, col_set_ids, col_chose_status))
                thread_list.append(t)
                t.start()
            for i in thread_list:
                i.join()
        except Exception as e:
            print("错误,休眠30s:", e)
            sleep(60)
            continue


if __name__ == '__main__':
    main()
