# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""正则匹配163邮箱"""
import re
email_list = ["xiaowang@163.com", "xiaoming@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)


"""findall结果无需加group(),search需要加group()提取"""

