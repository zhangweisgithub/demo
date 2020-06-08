FROM registry.sensetime.com/sensetest/centos_python3.7:v2
LABEL maintainer="zhangwei"
ADD /ssh /root/.ssh
ADD /backend_manual  /platform/backend-manual
WORKDIR /platform/backend-manual
RUN pip3 install --upgrade pip && pip3 install -r /platform/backend-manual/requirements.txt
RUN yum -y update \
    && yum -y install epel-release \
    && yum install ntpdate -y \
    && yum erase httpd.x86_64 -y
RUN ntpdate -u cn.pool.ntp.org && yum clean all
EXPOSE 5800
ENTRYPOINT ["/bin/bash", "-c", "./start_server.sh"]
