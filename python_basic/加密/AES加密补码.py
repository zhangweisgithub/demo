# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 pkcs5补码方式
"""

import base64
from Crypto.Cipher import AES


# 补足字符串长度为16的倍数
def add_to_16(s):
    while len(s) % 16 != 0:
        s += (16 - len(s) % 16) * chr(16 - len(s) % 16)  # chr():返回值是当前整数对应的 ASCII 字符。
    return str.encode(s)  # 返回bytes


"""
通过秘钥的长度确定为哪一种加密方式,从而创建出一个加密器
"""
key = '1234567890123456'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
text = 'abcdefg'  # 待加密文本

aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
print(add_to_16(text))           # b'abcdefg\t\t\t\t\t\t\t\t\t'            \t 跳格       \r 回车       \n 换行
encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密

decrypted_text = aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).decode("utf8")  # 解密
print(decrypted_text)         # "abcdefg									"后面有很多空格
decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位  ord正好跟chr函数作用相反(数据转ascii, ascii转数值)

print('pkcs5加密值:', encrypted_text)
print('pkcs5解密值:', decrypted_text)
