# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 打开文件
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)

line = fo.readline()
print("读取的数据为: %s" % (line))

# 重新设置文件读取指针到开头
"""
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
"""
fo.seek(0, 1)
line = fo.readline()
print("读取的数据为: %s" % (line))

# 关闭文件
fo.close()