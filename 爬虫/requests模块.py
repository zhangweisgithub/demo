# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

# ret = requests.get(url="http://10.9.242.41:9000/common/project/list?page_no=1&page_size=10",
#                    headers={
#                        "token": "eyJ1aWROdW1iZXIiOiAiMTkyMTIiLCAiZGlzcGxheU5hbWUiOiAiemhhbmd3ZWlfdmVuZG9yIiwgInJvbGUiOiAwLCAidWlkIjogInpoYW5nd2VpX3ZlbmRvciIsICJwbGF0Zm9ybSI6IDEsICJyZW1vdGVfaXAiOiAiMTAuOS4xNzYuMiIsICJleHBpcmUiOiAiMjAxOS0xMC0xOCAxODo1Nzo1NyJ9",
#                        "platform": "19212"}, timeout=2)

ret = requests.get(url="http://127.0.0.1:5000/hello")

data = ret.json()
print(data)
