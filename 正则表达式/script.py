# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re

str = "def delete_db(log, host, db_type, feature_version, object_type='face', images=('material/Viper/Business/1.jpeg', 'material/Viper/Business/2.jpeg', 'material/Viper/Business/50k.jpg')):"
# m2 = re.match(u'.*def (?P<func_name>.+)\(.*', str)
m2 = re.match(u'.*def (?P<func_name>\w+[^(]?)', str)
print(m2)
if m2:
    func_name = m2.group("func_name")
    print(func_name)



# 方法二
test = re.findall(r"def (.*?)\(", str)
print (test[0])






