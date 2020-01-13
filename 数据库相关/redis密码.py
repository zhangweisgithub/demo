# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
#
# a = str(base64.b64encode("88stIVA2017"))
# print(a)
#
# """
# ODhzdElWQTIwMTc=
# """


b = "12YmFja2Rvb3I==4"

c = str(base64.b64decode(b[2:-2]), "utf-8")

print(c)      # backdoor

a = str(base64.b64encode("root".encode("utf-8")),'utf-8')

print(a)    # cm9vdA==


m = "12cm9vdA===4"

n = str(base64.b64decode(m[2:-2]), "utf-8")
print(n)    # root

#
mima = str(base64.b64encode("88stIVA#2017".encode("utf-8")), "utf-8")
print(mima)   # ODhzdElWQSMyMDE3



