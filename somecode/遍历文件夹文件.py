# -*- coding: utf-8 -*-
# @Time    : 2018-05-15 17:59
# @Email   : Yzh_smlie@163.com
# @File    : 遍历文件夹文件.py

# coding:utf-8
import os
from collections import deque


class GuangDu:
    def __init__(self, path):
        "初始换函数，读取的根目录"
        self.path = path
        self.MyList = deque([])  # 实例化一个队列
        self.MyList.append(self.path)  # 把根目录路径放入队列中

    def BianLi(self):
        "广度遍历的方法实现"
        while len(self.MyList) != 0:  # 当队列中为空的时候跳出循环
            path = self.MyList.popleft()  # 从队列中弹出一个路径
            if os.path.isdir(path):  # 对弹出的path路径判断是否是一个文件夹
                print("文件夹", path)  # 打印文件夹的路径
                myFilePath = os.listdir(path)  # 如果是一个文件夹，就把文件夹里面的所有东西添加进列表中，
                for line in myFilePath:  # 对添加到列表中的东西进行遍历
                    myPath = path + "\\" + line  # 形成绝对路径，
                    self.MyList.append(myPath)  # 把遍历的东西都加入到队列中
            else:  # 如果不是一个文件夹，就直接把路径打印出来，不用对其进行遍历了
                print("文件", path)


path = r"F:\MyCode"  # 初始的文件目录
file = GuangDu(path)  # 实例化一个对象
file.BianLi()  # 对象调用方法
