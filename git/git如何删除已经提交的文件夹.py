# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
在上传项目到github时,忘记忽略了某个文件夹.idea,就直接push上去了, 最后意识到了此问题,决定删除掉远程仓库中的.idea文件夹
在github上只能删除仓库,却无法删除文件夹或文件, 所以只能通过命令来解决
首先进入你的master文件夹下, Git Bash Here ,打开命令窗口

$ git --help                                      # 帮助命令
$ git pull origin master                    # 将远程仓库里面的项目拉下来
$ git rm -r --cached .idea              # 删除.idea文件夹
$ git commit -m '删除.idea'        # 提交,添加操作说明
$ git push -u origin master               # 将本次更改更新到github项目上去

"""


"""
git rm -r --cached *__pycache__* 
"""