# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取词性：每个词都有其词性，比如名词、动词、代词等，结巴分词的结果也可以带上每个词的词性，要用到jieba.posseg
"""

import jieba.posseg as psg

s = '我想大口吃肉大碗喝酒！！！'
print('分词及词性：')
result = psg.cut(s)
print(result)
print([(x.word, x.flag) for x in result])

# 获取名词

import jieba.posseg as psg

s = '我想大口吃肉大碗喝酒！！！'
print('分词及词性：')
result = psg.cut(s)
print(result)
# 筛选为名词的
print([(x.word, x.flag) for x in result if x.flag == 'n'])
