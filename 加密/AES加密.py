# !/usr/bin/env python
# -*- coding: utf-8 -*-
# AES-demo
"""
    @author: sy

    @file: python_AES.py

    @time: 2017/12/12 09:10

    @desc: AES加密
"""

from Crypto.Cipher import AES

# 秘钥,此处需要将字符串转为字节
key = b'abcdefgh'


# 加密内容需要长达16位字符，所以进行空格拼接(将text的后面加上空格，时期能被16整除)
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


# 加密秘钥需要长达16位字符，所以进行空格拼接(%：返回除法的余数,这里的意思是能被16整除)
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


# 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
aes = AES.new(pad_key(key), AES.MODE_ECB)          # 这里生成了一个加密对象(参数为一个bytes类型)
# 加密内容,此处需要将字符串转为字节
text = b'woshijiamineirong'
# 进行内容拼接16位字符后传入加密类中，结果为字节类型
encrypted_text = aes.encrypt(pad(text))
print(encrypted_text)            # b'\x8f\xea\x87\xa5\n\xa6 <\xfc\xfdP\x8f\xa3\x0f\x8f\xa0\xd8\xcd\x10>:7\xef\x05\x7fwc\xef\xf7t+Q'

# 此处是为了验证是否能将字节转为字符串后，进行解密成功
# 实际上a 就是 encrypted_text ，也就是加密后的内容

"""
注意这里,构造一个aes对象后,我可以使用这个构造的对象对其他已经加密的编码进行解密
"""
a = b'\xb9K\xe8_.q\x1c!\x9f\xa2\xc8\x06\xf5\xc1\xd07'
# 用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
de = str(aes.decrypt(a), encoding='utf-8', errors="ignore")
# 获取str从0开始到文本内容的字符串长度。
print(de[:len(text)])

"""对上面加密后的数据进行解密"""
dec = str(aes.decrypt(encrypted_text), encoding="utf-8", errors="ignore")        # 对上面加密的内容进行解密
print("2:", dec)       # 2: woshijiamineirong


"""
之前的加密方法是直接通过base64进行加密的
{"uidNumber": "19212", "displayName": "zhangwei_vendor", "role": 2, "uid": "zhangwei_vendor", "platform": 1, "remote_ip": "127.0.0.1", "expire": "2019-10-10 11:23:03"}
"""
import base64
t = "eyJ1aWROdW1iZXIiOiAiMTkyMTIiLCAiZGlzcGxheU5hbWUiOiAiemhhbmd3ZWlfdmVuZG9yIiwgInJvbGUiOiAyLCAidWlkIjogInpoYW5nd2VpX3ZlbmRvciIsICJwbGF0Zm9ybSI6IDEsICJyZW1vdGVfaXAiOiAiMTI3LjAuMC4xIiwgImV4cGlyZSI6ICIyMDE5LTEwLTEwIDExOjIzOjAzIn0="
p = str(base64.b64decode(t), "utf-8")
print(p)
