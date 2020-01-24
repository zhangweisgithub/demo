# -*- coding: utf-8 -*-
# @Time    : 2018-04-28 21:31
# @Email   : Yzh_smlie@163.com
# @File    : Q进程间通信.py
# coding=utf-8

"""
初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；
Queue.qsize()：返回当前队列包含的消息数量；
Queue.empty()：如果队列为空，返回True，反之False ；
Queue.full()：如果队列满了，返回True,反之False；
Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
"""
from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

# 因为消息列队已满下面的try都会抛出异常，第一个Try会立刻抛出异常，第二个try会等待2秒后再抛出异常，
try:
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize())

try:
    q.put("消息4", True, 2)
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize())

# 推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

# 读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
