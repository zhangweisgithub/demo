# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
结巴”中文分词：做最好的 Python 中文分词组件
支持三种分词模式：
精确模式，试图将句子最精确地切开，适合文本分析；
全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
支持繁体分词
支持自定义词典
MIT 授权协议
https://www.cnblogs.com/lyq-biu/p/9641677.html
"""
import jieba

# 2.1.精确模式（返回结果是一个生成器，对大量数据分词很重要，占内存小）：
s = '我想大口吃肉大碗喝酒！！！'
cut = jieba.cut(s)
print(cut)
# 精确模式
print('精确模式输出：')
print('，'.join(cut))

# 　2.2.全模式（返回结果也是生成器，特点是把文本分成尽可能多的词）：
import jieba

s = '我想大口吃肉大碗喝酒！！！'
print('全模式：')
result = jieba.cut(s, cut_all=True)
print(result)
print(' '.join(result))


# 2.3.搜索引擎模式：
import jieba

s = '我想大口吃肉大碗喝酒！！！'
print("搜索引擎模式")
result = jieba.cut_for_search(s)
print(result)
print(",".join(result))


