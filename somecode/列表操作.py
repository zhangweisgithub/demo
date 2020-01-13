# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 21:07
# @Email   : Yzh_smlie@163.com
# @File    : 列表操作.py

list1 = [1, 5, 7, 9]
list2 = [2, 2, 6, 8]
# 合并列表
list1.extend(list2)
print(list1)
# 排序
list1.sort(reverse=False)
print(list1)

# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1, 2], [3, 4], [5, 6]]
x = [j for i in a for j in i]
print(x)

# 两个列表 +  等同于 extend（）  合并
a = [1, 2, 3]

b = [4, 5, 6]

res = a + b
print(res)

# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，
# 输出[2,3,4,5,6,9]

list = [2, 3, 5, 4, 9, 6]
new_list = []


def get_min(list):
    # 获取列表最小值
    a = min(list)
    # 删除最小值
    list.remove(a)
    # 将最小值加入新列表
    new_list.append(a)
    if len(list) > 0:
        get_min(list)
    return new_list


new_list = get_min(list)
print(new_list)

# sort和sorted
# sort是在list的基础上修改 无返回值
# sorted有返回值是新的list

# 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使
# 用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
ww = sorted(foo,key=lambda x:x)
print(ww)