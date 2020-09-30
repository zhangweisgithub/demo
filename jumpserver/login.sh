#!/usr/bin/expect
exec ntpdate -u ntp.api.bz
set timeout 3

spawn ssh xxx@jump01.sz.sensetime.com       # xxx替换成LDAP用户名
expect "*Verification*"
send_user  [exec python3 get_token.py]
send [exec python3 get_token.py]
send "\r"
expect "*Password*"
send "xxx\r"                                # xxx替换成LDAP密码(实际使用时这一行的注释需要去掉)
sleep 1
expect "*Please enter your Login Ip*"
send "172.20.26.40\r"
interact

