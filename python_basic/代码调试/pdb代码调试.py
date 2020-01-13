# coding=utf-8
import ipdb
def combine(s1, s2):
    # pdb.set_trace()
    s3 = s1 + s2 + s1
    s3 = '"' + s3 + '"'
    return s3


a = "aaa"
# ipdb.set_trace()
b = "bbb"
c = "ccc"
final = combine(a, b)
print(final)

# 可以直接python -m ipdb demo_4.py运行文件进行断点调试, b 10可以直接打断点
# 或者import pdb 然后再需要停止的地方pdb.set_trace()程序就会再对应的地方暂停，可以进行调试
