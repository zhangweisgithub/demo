# !/usr/bin/env python
# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet

# 秘钥#随机生成秘钥(这里可以生成一个二进制的随机秘钥)
# cipher_key = Fernet.generate_key()      # b'nt-bzPPWtUJl8tdhjGbOVfMc9v-VrebwxL3oroIs1cg='
cipher_key = 'pXVAHabI4HADuM-fyVogxwV5rHRN1pZe-QQ3yM9ZvPg='

# 123为要加密的对象
a = Fernet(cipher_key).encrypt("123".encode()).decode()
print(a)  # gAAAAABdySgQcFjf6kveYVUOWpWGdwKgD1A9qujjR_-Z-EHT0h5WXxLEjAWRq5g58vo8k7IwFChEBI5CmhNzL6jk7zURZlCE9Q==

#  解密：

b = Fernet(cipher_key).decrypt(a.encode()).decode()
print(b)  # 123


"""
1.生成秘钥
2.加密(带着秘钥)
3.解密(带着秘钥)
"""