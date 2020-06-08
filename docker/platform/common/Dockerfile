FROM registry.sensetime.com/sensetest/centos_python3.7:v2
ADD /ssh /root/.ssh
RUN mkdir -p /platform/backend-common
WORKDIR /platform/backend-common
ADD backend-common /platform/backend-common
RUN pip3 install -r /platform/backend-common/requirements.txt
RUN yum -y install tzdata \
    && yum install ntpdate -y \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' >/etc/timezone \
    && yum erase httpd.x86_64 -y \
    && rm -rf /platform/backend-common/* \
    && rm -f /home/*  \
    && yum clean all
RUN ntpdate asia.pool.ntp.org

EXPOSE 5100 9000 9001
ENTRYPOINT ["/bin/bash", "-c", "./start_server.sh"]