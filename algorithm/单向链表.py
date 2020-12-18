# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 单向链表  https://www.cnblogs.com/kumata/p/9147077.html
# class Node:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next
#
#
# class LianBiao:
#     def __init__(self):
#         self.root = None
#
#     # 给单向链表添加元素
#     def addNode(self, data):
#         newNode = Node(data=data, next=None)
#         if self.root == None:
#             self.root = newNode
#         else:
#             # 有头结点,则需要遍历到尾部节点, 进行链表的增加操作
#             cursor = self.root
#             while cursor.next != None:
#                 cursor = cursor.next
#             cursor.next = newNode

"""
约瑟夫问题：n个人围成一个圈，每个人分别标注为1、2、…、n，要求从1号从1开始报数，报到k的人出圈，接着下一个人又从1开始报数，
如此循环，直到只剩最后一个人时，该人即为胜利者。

解约瑟夫问题的一种方法是模拟这个过程，模拟的载体可以是队列，也可以是链表
如果需要用链表解决该问题，则需要循环链表，即最后一个节点接头结点。相对于队列，循环链表的差异在于不需要频繁的入队出队，
只需要一直循环遍历链表，把第k个节点删除直至留下最后一个节点。在单链表的基础上，只要将最后一个节点链接上头结点即实现循环链表
"""


# 循环链表解决约瑟夫问题
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LoopLinkedList:
    def __init__(self):
        self.root = None

    # 在循环链表尾部添加节点，尾部即头结点上一个
    def addNode(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            cursor = self.root
            while cursor.next != self.root:
                cursor = cursor.next
            cursor.next = newNode
        newNode.next = self.root  # 链接成环

    # 链表长度
    def size(self):
        if self.root == None:
            return 0
        cursor = self.root
        i = 1
        while cursor.next != self.root:
            i += 1
            cursor = cursor.next
        return i


# 约瑟夫问题仿真函数
def circle(num, nameList):
    linkedList = LoopLinkedList()
    for i in range(len(nameList)):
        linkedList.addNode(nameList[i])
    i = 1
    pre = linkedList.root
    cursor = linkedList.root
    while linkedList.size() != 1:
        if i != num:
            pre = cursor
            cursor = cursor.next
            i += 1
        else:
            pre.next = cursor.next  # 删除当前节点需要用上一个节点连接下一个节点
            cursor = pre.next
            linkedList.root = cursor  # 重新选择头结点是为了计算链表长度
            i = 1
    return cursor.data


# 主函数
if __name__ == '__main__':
    nameList = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(circle(7, nameList))
# 输出结果      Kent
