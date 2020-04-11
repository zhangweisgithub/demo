# !/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/traditional/p/10991231.html
from datetime import date, datetime
from apscheduler.schedulers.blocking import BlockingScheduler


# 选择了阻塞式调度器，创建一个调度器的实例
scheduler = BlockingScheduler()


# 创建一个任务
def my_task(name, age, gender):
    print(f"name is {name}, age is {age}, gender is {gender}")


# 通过调用调度实例下的add_job方法，将任务添加进去
"""
常用参数：
func：任务(执行函数)
trigger：触发器，一共三种方式。
         date 日期：触发任务运行的具体日期
         interval 间隔：触发任务运行的时间间隔
         cron 周期：触发任务运行的周期
run_date：运行日期，当我们指定trigger为'date'时，可以添加这么一个参数。类型可以是date、datetime、以及文本类型
args：任务的位置参数
kwargs：任务的关键字参数
"""
# scheduler.add_job(my_task, trigger="date",
#                   run_date=date(2020, 6, 10),
#                   args=("mashiro", 17),
#                   kwargs={"gender": "女"})

# date指定日期进行执行
scheduler.add_job(my_task,
                  trigger="date",
                  run_date=datetime(2020, 4, 14, 16, 40, 4),   # 或者  run_date="2019-6-9 17:14:05"
                  args=("mashiro", 17),
                  kwargs={"gender": "女"})


# 其他参数没什么变化，当我们把trigger指定成interval的时候，表示每隔xx时间执行一次。可以额外指定如下参数
"""
weeks：每隔多少周后执行一次
days：每隔多少天后执行一次
hours：每隔多少小时后执行一次
minutes：每隔多少分钟后执行一次
seconds：每隔多少秒后执行一次
此外还可以指定start_date，和end_date。表示任务触发的起始时间和结束时间。
比如某个任务每隔一天执行一次，但是这个任务有截止日期，当超过了截止日期的时候，就不需要再执行它了。于是就可以将该"截止日期"设置为end_date，如果超过了，那么任务会被取消掉
"""
scheduler.add_job(my_task,
                  trigger="interval",
                  minutes=1,
                  args=("mashiro", 17),
                  kwargs={"gender": "女"})

# cron  周期执行
"""
class CronTrigger:
    def __init__(self, year=None, month=None, day=None, week=None, day_of_week=None, hour=None,
                 minute=None, second=None, start_date=None, end_date=None, timezone=None,
                 jitter=None):
year：四位数的年份
month：1-12之间的数字或字符串，如果不指定，则为*，表示每个月
day：1-31，如果不指定，则为*，表示每一天
week：1-53，如果不指定，则为*，表示每一星期
day_of_week：一周有7天，用0-6表示，比如指定0-3，则表示周一到周四。不指定则为7天，也可以用			mon,tue,wed,thu,fri,sat,sun表示
hour：0-23
minute：0-59
second：0-59
start_date：起始时间
end_date：结束时间
timezone：时区
jitter：随机的浮动秒数
当省略时间参数时，在显式指定参数之前的参数会被设定为*，表示每(月、天)xxx。之后的参数会被设定为最小值，week 和day_of_week的最小值为*。
比如，设定day=10等同于设定year='*', month='*', day=1, week='*', day_of_week='*', hour=0, minute=0, second=0，
即每个月的第10天触发。为什么是每个月而不是每个星期，注意参数位置，week被放在了后面。day后面的参数hour、minute、second则被设置为0。因此不仅是每个月的第10天触发，还是每个月的第10天的00:00:00的时候触发
"""
scheduler.add_job(my_task,
                  trigger="cron",
                  second=10,          # 这个地方表示的是每分钟的第10s开始执行
                  args=("cron", 17),
                  kwargs={"gender": "男"})

# 未指定日期，则会立即执行
# scheduler.add_job(my_task,
#                   args=("mashiro", 17),
#                   kwargs={"gender": "女"})

# 启动调度器
scheduler.start()