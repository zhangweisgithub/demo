#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Eddy'

import sys
import numpy
import threading
from time import sleep, time

sys.path.append("F:\\Eddy\\13、Python\\guopeng\\test")
from common_func import *


class SetRunClass:
    RunNumber = 0
    ErrNumber = 0
    SetRun = {'method': 'POST', 'uri': '/auto/set/run'}
    SetList = {'method': 'GET', 'uri': '/auto/set/list'}
    SetStop = {'method': 'POST', 'uri': '/auto/set/stop'}
    ComUserLog = {'method': 'POST', 'uri': '/common/user/login'}
    SetProgress = {'method': 'POST', 'uri': '/auto/set/progress'}  # 测试集状态
    SleepTime = 20
    Headers = {
        "platform": "sBTShiYxKsZVwu6pIG/5fg==",
        # "source":"ci",
        # "token": "JCXpduf05S2RP6N2ZHoaqQP6b9Eooo03BQrqCVEc739nS+qf03YPhL3kCdvMeYgQ9gJdX+8gb+zKIua1wY4x11C/RJ"
        #          "pkV364IbU7OzvHLx5TXMaDK6fb9ozqiMMKjlXyBxJ1tKoY1oLz2tzREFBF6SxBL41dDHAo/WSh+kGGmpI=",
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
        url = 'http://{0}{1}'.format(self.host, SetRunClass.ComUserLog['uri'])
        response = restful_api(
            req_url=url,
            req_method=SetRunClass.ComUserLog['method'],
            params=body,
            headers=SetRunClass.Headers,
            log=self.log)
        if response['status_code'] == 200:
            return True, response['data']  # 返回(True,{'token': 'JCXp'})
        else:
            return False, response['code']

    def set_list(self, set_nums, params=None):
        body = {
            "page_no": "1",
            "page_size": "1000",
            "project_id": "1"
            # ,
            # "title": "37"
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, SetRunClass.SetList["uri"])
        response = restful_api(
            req_url=url,
            req_method=SetRunClass.SetList['method'],
            params=body,
            headers=SetRunClass.Headers,
            log=self.log)
        __set_list_dict = {}
        for i in response["sets"]:
            __set_list_dict.update({i["id"]: i["run_status"]})  # 返回一个测试集ID和状态的字典
            # {1676: 1, 1762: 1, 2864: 1, 1657: 1, 1679: 1, 1646: 1, 1776: 1, 1795: 3, 1658: 1, 1659: 1}
        # 返回随机的set_nums个set ID的列表
        __set_chose_id_list = numpy.random.choice(list(__set_list_dict), size=set_nums, replace=False)
        # [1646 1676 1776]
        return __set_chose_id_list

    def set_run(self, set_id, params=None):
        body = {
            "set_id": [set_id],
            "choice": 2,
            # "cc": [],
            # "email": ["guopeng@sensetime.com"],
            # "user_config":user_config,
            # "loop_cnt": [],
            # "sleep_time": "",
            # "module": [],
            # "setup": {},
            # "teardown": {},
            "user_config": SetRunClass.UserConfig
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, SetRunClass.SetRun["uri"])
        response = restful_api(
            req_url=url,
            req_method=SetRunClass.SetRun['method'],
            params=body,
            headers=SetRunClass.Headers,
            log=self.log)
        return response

    def set_stop(self, set_id, params=None):
        body = {
            "set_id": [set_id],
            "choice": 2
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, SetRunClass.SetStop["uri"])
        response = restful_api(
            req_url=url,
            req_method=SetRunClass.SetStop['method'],
            params=body,
            headers=SetRunClass.Headers,
            log=self.log)
        return response

    def set_progress(self, set_id, params=None):
        body = {
            "set_id": [set_id]
        }
        if params and isinstance(params, dict):
            body.update(params)
        url = "http://{0}{1}".format(self.host, SetRunClass.SetProgress["uri"])
        response = restful_api(
            req_url=url,
            req_method=SetRunClass.SetProgress['method'],
            params=body,
            headers=SetRunClass.Headers,
            log=self.log)
        return response[str(set_id)]["status"]  # 返回查询的set_id的状态

    def sep_set_run(self, set_chose_id, set_chose_status):
        try:
            self.log.error('选择的测试集是{}，状态为{}'.format(
                set_chose_id, SetRunClass.set_status_dict.get(set_chose_status, "其他")))
            if set_chose_status not in (2, 5, 6):
                self.log.error("运行测试集{}".format(set_chose_id))
                run_response = SetRunClass.set_run(self, set_chose_id)
                if run_response.get("code") == 0:
                    self.log.error("测试集{}执行成功！\n等待{}秒钟".format(set_chose_id, SetRunClass.SleepTime))
                    sleep(10*60)
                    # 停止测试集
                    # stop_response = SetRunClass.set_stop(self, set_chose_id)
                    # if stop_response.get("code") == 0:
                    #     self.log.error("测试集{}停止成功！\n等待{}秒钟".format(set_chose_id, SetRunClass.SleepTime))
                    #     sleep(SetRunClass.SleepTime)
                    #     # 查看这个测试集的状态
                    #     progress_status = SetRunClass.set_progress(self, set_chose_id)
                    #     self.log.error("progress_status {0},{1}".format(progress_status, SetRunClass.set_status_dict.get(set_chose_status, "其他")))
                    #     if progress_status == 3:
                    #         self.log.error("执行正常")
                    #         SetRunClass.RunNumber += 1
                    #     else:
                    #         self.log.error("测试集{}状态为{},{},状态异常".format(
                    #             set_chose_id, progress_status, SetRunClass.set_status_dict.get(progress_status, "其他")))
                    #         SetRunClass.ErrNumber += 1
                    # else:
                    #     self.log.error("测试集{}停止失败".format(set_chose_id))
                    #     SetRunClass.ErrNumber += 1
                else:
                    self.log.error("测试集{}未执行成功".format(set_chose_id))
                    SetRunClass.ErrNumber += 1
            else:
                self.log.error("测试集在运行，停止它")
                stop_response = SetRunClass.set_stop(self, set_chose_id)
                if stop_response.get("code") == 0:
                    self.log.error("测试集{}停止成功！\n等待{}秒钟".format(set_chose_id, SetRunClass.SleepTime))
                    sleep(SetRunClass.SleepTime)
                    # 查看这个测试集的状态
                    progress_status = SetRunClass.set_progress(self, set_chose_id)
                    if progress_status == 3:
                        self.log.error("执行正常")
                        SetRunClass.RunNumber += 1
                    else:
                        self.log.error("测试集{}状态为{}，状态异常".format(
                            set_chose_id, SetRunClass.set_status_dict.get(progress_status, "其他")))
                        SetRunClass.ErrNumber += 1
                else:
                    self.log.error("测试集{}停止失败".format(set_chose_id))
                    SetRunClass.ErrNumber += 1
        finally:
            self.log.error("正常执行了{}次，出错{}次".format(SetRunClass.RunNumber, SetRunClass.ErrNumber))
            self.log.error("*" * 20)


def main():
    set_nums = 3  # 设定一次性获取的测试集数量，也是同时跑测试集的线程数
    host = "10.9.244.33:9000"
    user_log_info = {"username": "guopeng", "password": "Snc2SGFyZS0tLWluZzIwMjBkUE42"}
    log = log_config(out_path='../logs', filename='set_start_progress_stop', fix=True)[0]
    set_run_class = SetRunClass(host, log)
    user_log_response = set_run_class.user_log(params=user_log_info)
    if user_log_response:
        set_run_class.Headers.update(user_log_response[1])
    # import pdb;  pdb.set_trace()
    while set_run_class.RunNumber < 100000000:
        # try:
        set_chose_id_list = set_run_class.set_list(set_nums)
        thread_list = []
        for i in set_chose_id_list:
            i = str(i)
            set_chose_status = set_run_class.set_progress(i)
            t = threading.Thread(target=set_run_class.sep_set_run, args=(i, set_chose_status))
            thread_list.append(t)
            t.start()
        for i in thread_list:
            i.join()
        # except:
        #     print("执行错误,休眠30s")
        #     sleep(60)
        #     continue


if __name__ == '__main__':
    main()

