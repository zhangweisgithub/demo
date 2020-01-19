# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

"""
base64加密的是一个二进制字符串,所以要先对字符串进行encode,返回一个base64加密后的二进制对象
str(), 将二进制编码的数据转化为字符串,可以指定encoding="utf-8"
"""
base64_encode = str(base64.b64encode("88stIVA2017".encode("utf-8")), "utf-8")  # b'ODhzdElWQTIwMTc='
print(base64_encode)
base64_decode = str(base64.b64decode("ODhzdElWQTIwMTc="), "utf-8")
print(base64_decode)
MYSQL_USER = str(base64.b64decode("12cm9vdA===4"[2:-2]), "utf-8")  # cm9vdA==进行base64解码之后为:root
print(MYSQL_USER)


# 文本简单加密
bs64_my_time = base64.b64encode("真的羡慕你们这种18岁的,我还差15年呢!".encode("utf-8"))
print("bs64格式的文本(伪加密)", bs64_my_time)
my_time = base64.b64decode(bs64_my_time).decode("utf-8")
print("原文本:", my_time)

# a = "eyJ1aWROdW1iZXIiOiAiMTkyMTIiLCAiZGlzcGxheU5hbWUiOiAiemhhbmd3ZWlfdmVuZG9yIiwgInJvbGUiOiAwLCAidWlkIjogInpoYW5nd2VpX3ZlbmRvciIsICJwbGF0Zm9ybSI6IDEsICJyZW1vdGVfaXAiOiAiMTAuOS4xNzYuMiIsICJleHBpcmUiOiAiMjAxOS0wOS0yNCAxODowOTo0NiJ9"
a = "eyJ1aWROdW1iZXIiOiAiMTkyMTIiLCAiZGlzcGxheU5hbWUiOiAiemhhbmd3ZWlfdmVuZG9yIiwgInJvbGUiOiAwLCAidWlkIjogInpoYW5nd2VpX3ZlbmRvciIsICJwbGF0Zm9ybSI6IDEsICJyZW1vdGVfaXAiOiAiMTAuOS4xNzYuMiIsICJleHBpcmUiOiAiMjAxOS0wOS0yNSAxMToyOTo1MSJ9"
b = base64.b64decode(a).decode("utf-8")
# 同: b = str(base64.b64decode(a), "utf-8")
print("token:", b)

