# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Linux如何自己封装命令

1.打开需编辑的文件

vim ~/.bashrc

2.文件中如下写（举个栗子）

alias gitll=’git pull’
alias gitsh=’git push’
alias jumps = "cd /jumpserver && ./login"        # 输入jumps的时候进入到对应的文件中执行对应的命令

3.最后执行文件使其及时生效

source ~/.bashrc

这样以后pull代码或者push代码只需要输入gitll或者gitsh，当然这只是一个简单的栗子，其他复杂的自己去diy吧~~~~
输入jumps就可以执行对应的login文件,然后直接进行跳板机的登陆了
"""
