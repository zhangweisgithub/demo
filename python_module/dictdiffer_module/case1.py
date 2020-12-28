# !/usr/bin/env python
# -*- coding: utf-8 -*-
from dictdiffer import diff, patch, swap, revert
import json

first = {
    "title": "hello",
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30"],
    "settings": {
        "assignees": [100, 101, 201],
    },
    "test": 1234
}

second = {
    "title": "hellooo",
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30", "/users/40"],
    "settings": {
        "assignees": [100, 101, 202],
    }
}

result = diff(first, second)  # 获取的是相对于第一个,第二个更改了什么
print(list(result))

"""
[('change', 'title', ('hello', 'hellooo')),
 ('add', 'stargazers', [(2, '/users/40')]), 
 ('change', ['settings', 'assignees', 2],
 (201, 202)), ('remove', '', [('test', 1234)])]
"""

result = diff(first, second)
patched = patch(result, first)

assert patched == second

diff = diff(first, second)
diff = list(diff)
print("diff:", diff)

swapped = swap(result)
print("swapped:", list(swapped))

mark = json.dumps(diff, indent=2, ensure_ascii=False)
print("更改:", mark)
