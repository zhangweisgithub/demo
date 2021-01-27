# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二多线程测试
"""
import datetime
import json
import requests
import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

reponse_time = []
OK = []


class runScript():
    def API(self, url, params):
        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        except requests.RequestException as e:
            print(e)
        else:
            js = json.dumps(r.json())
            # print(r.json()) #json格式的响应数据
            # print(r.elapsed.total_seconds())　响应时间
            # print(js)　没有解码的响应数据
            return [r.json(), r.elapsed.total_seconds(), js]

    def circulation(self, url, params):
        # print(Restime.API(url, params)[0]['message'])
        reponse_time.append(self.API(url, params)[1])
        datas = json.loads(self.API(url, params)[2])["message"]
        status = json.loads(self.API(url, params)[2])["status"]
        if datas == 'ok':
            OK.append(datas)
            logger.info('请求状态为：' + datas + ',状态码为：' + status)
        else:
            logger.info('请求状态为：' + datas + ',状态码为：' + status)


def test(url, params):
    Restime = runScript()
    Restime.circulation(url, params)


def main(num, url, params):
    # print("Starting at:",ctime())
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    threads = []
    for i in range(num):
        t = threading.Thread(target=test, args=(url, params))
        threads.append(t)
    for t in range(num):
        threads[t].start()
    for j in range(num):
        threads[j].join()
    # print("All done at:",ctime())
    print("Starting at:", start_time)
    print("All done at:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # print(OK)
    print('响应次数：', len(reponse_time))
    print('正常响应次数：', len(OK))
    print('总响应最大时长：', max(reponse_time))
    print('总响应最小时长：', min(reponse_time))
    print('总响应时长：', sum(reponse_time))
    print('平均响应时长：', sum(reponse_time) / len(reponse_time))
    print('QPS（TPS）= 并发数/平均响应时间:', num / (sum(reponse_time) / len(reponse_time)))


if __name__ == '__main__':
    num = input('输入需要开启的线程数量:')
    url = 'http://www.kuaidi100.com/query'  # 地址
    params = {'type': 'zhongtong', 'postid': '73116039505988'}  # 参数
    main(int(num), url, params)
