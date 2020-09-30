# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Google Authenticator是谷歌推出的一款动态口令工具，解决大家的google账户遭到恶意攻击的问题，
在手机端生成动态口令后，在google相关的服务登陆中除了用正常用户名和密码外，
需要输入一次动态口令才能验证成功。会首先使用在公司的OPEN VPN上。

Secret is:6JI6EIB3XDTDWUOE
"""

import pyotp

totp = pyotp.TOTP("6JI6EIB3XDTDWUOE")
totp.now()
print(totp.now())
