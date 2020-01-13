# -*- coding: utf-8 -*-
# @Time    : 2018-05-09 17:10
# @Email   : Yzh_smlie@163.com
# @File    : 发邮件.py
# 功能: 发送简单的文本邮件
# 注意： 确保该代码可用请先到发送者邮箱后台开启 SMTP 登录功能，并获得第3方登录密码
# 注意： 使用163邮件服务器时，可用 SMTP()方法,25端口进行登录
# 注意： 使用腾讯邮件服务器时，必须使用 SMTP_SSL()方法,465端口进行登录

import smtplib  # 导入 smtplib 邮件处理库
from email.mime.text import MIMEText
from email.utils import formataddr

mail_server = "smtp.163.com"  # 发件人的 SMTP 服务器
port = "25"  # 服务端口

sender = "21@163.com"  # 发件人邮箱帐号
sender_passw = "py"  # 发件人邮箱密码(第3方登录授权密码)
receiver = "135m"  # 收件人邮箱帐号

mail_msg = '你好，'
msg = MIMEText(mail_msg, "plain", "utf-8")  # 邮件内容（正文）  需要发送HTML文件时，plain 改为 html 即可!
msg['From'] = formataddr(["阿里巴巴中国", sender])  # 发件人信息
msg['To'] = formataddr(["面试邀请", receiver])  # 收件人信息
msg['Subject'] = "面试邀请"  # 邮件的主题


def sendMail(mail_server, port, sender, sender_passw, receiver):
    try:
        mail = smtplib.SMTP(mail_server, port)  # 使用SMTP()方法指向服务器（使用QQ邮箱服务器时，需改用 SMTP_SSL()方法）
        mail.login(sender, sender_passw)  # 请求服务器，登录帐号
        mail.sendmail(sender, [receiver], msg.as_string())  # 发送邮件(给receiver传入列表时，表示群发)
        mail.quit()  # 断开连接
        print("邮件发送成功！")
    except:
        mail.quit()
        print("邮件发送失败！")


sendMail(mail_server, port, sender, sender_passw, receiver)
