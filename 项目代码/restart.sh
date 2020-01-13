#!/bin/bash

echo "started $0"
echo "$server_type, $api_ip, $api_cf, $api_port, $api_flower_port $line"

level=info
if [ $api_cf == product ]
then
  level=info
else
  level=debug
fi

if [ $server_type == 1 ]
then
  echo "启动API服务"
  echo "gunicorn -c gun.py api:app --log-file=app.log --log-level=${level} >> app.log 2>&1 &"
  nohup gunicorn -c gun.py api:app --log-file=app.log --log-level=${level} >> app.log 2>&1 &
elif [ $server_type == 2 ]
then
  echo "启动Celery任务调度服务"
  echo "nohup celery worker -A api.celery -l ${level} -n ${api_ip} --logfile=app.log --without-mingle  -O fair --autoscale=80,40 -Q query_platform_${line}_api >> app.log 2>&1 &"
  nohup celery worker -A api.celery -n ${api_ip} --logfile=app.log  --without-mingle  -O fair --autoscale=5,3 -Q query_platform_${line}_api >> app.log 2>&1 &
  sleep 10
  echo "开始启动监控服务"
  echo "nohup celery -A api:celery flower --port=$api_flower_port >> app.log 2>&1 &"
  nohup celery -A api:celery flower --port=$api_flower_port >> app.log 2>&1 &
  echo "服务启动完成"
else
  echo "张威启动API服务"
  echo "gunicorn -c gun.py api:app --log-file=app.log --log-level=${level} >> app.log 2>&1 &"
  nohup gunicorn -c gun.py api:app --log-file=app.log --log-level=${level} >> app.log 2>&1 &
  sleep 2
  echo "张威启动Celery任务调度服务"
  echo "nohup celery worker -A api.celery -l ${level} -n ${api_ip} --logfile=app.log --without-mingle -O fair --autoscale=80,40 -Q query_platform_${line}_api >> app.log 2>&1 &"
#  nohup celery worker -A api.celery -l ${level} -n ${api_ip} --logfile=app.log  --without-mingle -O fair --autoscale=80,40 -Q query_platform_${line}_api >> app.log 2>&1 &
  nohup celery worker -A api.celery -l info -n ${api_ip} --logfile=app.log  --without-mingle -O fair --autoscale=20,10 -Q query_platform_1_api >> app.log 2>&1 &
  nohup celery worker -A api.celery -l info -n ${api_ip} --logfile=app.log  --without-mingle -O fair --autoscale=20,10 -Q query_platform_2_api >> app.log 2>&1 &
  nohup celery worker -A api.celery -l info -n ${api_ip} --logfile=app.log  --without-mingle -O fair --autoscale=20,10 -Q query_platform_other_api >> app.log 2>&1 &
  celery worker -A api.celery -l info -n ${api_ip}_line_${line}_2 --autoscale=80,40 -Q query_platform_other_api
  sleep 3
  echo "张威开始启动监控服务"
  echo "nohup celery -A api:celery flower --port=${api_flower_port} >> app.log 2>&1 &"
  nohup celery -A api:celery flower --port=${api_flower_port} >> app.log 2>&1 &
  echo "张威服务启动完成"
fi
while true
do
        tail -f app.log
done
