# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
并行分词：在文本数据量非常大的时候，为了提高分词效率，开启并行分词就很有必要了。
jieba支持并行分词，基于python自带的multiprocessing模块，但要注意的是在Windows环境下不支持。
"""
import jieba
# 开启并行分词模式，参数为并发执行的进程数
# jieba.enable_parallel(5)

# 关闭并行分词模式
# jieba.disable_parallel()


# 5.获取出现频率Top n的词（有些词无实际意义，可筛选）：

from collections import Counter

words_total = open('./1.txt', encoding='utf-8').read()
c = Counter(words_total).most_common(20)
print(len(words_total))
print(c)
