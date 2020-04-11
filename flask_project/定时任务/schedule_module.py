# !/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule


def foo():
    print(123)


# 每隔3秒钟运行foo，如果有参数，直接通过args= 或者kwargs=进行传参即可
schedule.every(3).seconds.do(foo)
# 每隔1秒钟运行foo
schedule.every().seconds.do(foo)
# 每隔1分钟运行foo
schedule.every().minutes.do(foo)
# 每隔一小时运行foo
schedule.every().hours.do(foo)
# 每隔一天运行foo
schedule.every().days.do(foo)
# 每隔一星期运行foo
schedule.every().weeks.do(foo)
# 每隔3到5秒钟运行foo
schedule.every(3).to(5).seconds.do(foo)
# 每隔3到5天运行foo
schedule.every(3).to(5).days.do(foo)

# 每天在10:30的时候运行foo
schedule.every().days.at("10:30").do(foo)
# 每周一的时候运行foo
schedule.every().monday.do(foo)
# 每周日晚上11点的时候运行foo
schedule.every().sunday.at("23:00").do(foo)
while True:
    # 保持schedule一直运行，然后去查询上面的任务
    schedule.run_pending()

