FROM registry.sensetime.com/sensetest/centos_python3.7:v2
ADD /ssh /root/.ssh
RUN mkdir -p /platform/backend-api
WORKDIR /platform/backend-api
ADD /backend-api /platform/backend-api
RUN yum -y update \
    && yum -y install epel-release \
    && yum -y install redis \
    && yum -y install net-tools \
    && sed -i -e 's@protected-mode yes@protected-mode no@g' /etc/redis.conf \
    && sed -i -e 's@port 6379@port 6378@g' /etc/redis.conf \
    && sed -i -e 's@daemonize no@daemonize yes@g' /etc/redis.conf \
    && sed -i -e 's@bind 127.0.0.1@bind 0.0.0.0@g' /etc/redis.conf \
    && echo "requirepass ODhzdElWQTIwMTc=" >> /etc/redis.conf 
RUN pip3 install -r /platform/backend-api/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \
    && pip3 install -r /platform/backend-api/scripts/sats/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \
    && pip3 install -r /platform/backend-api/scripts/vats/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \
    && pip3 install -r /platform/backend-api/scripts/biats/requirement.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \    
    && pip3 uninstall kafka -y \
    && pip3 uninstall kafka-python -y \
    && pip3 install kafka-python \
    && pip3 install redis --upgrade \
    && pip3 install xeger --upgrade \
    && pip3 install spark-python 
RUN yum install -y libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false \
    && yum install -y git \
    && curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \
    && yum -y install nodejs \
    && chmod +x /platform/backend-api/restart.sh  \
    && yum -y install tzdata \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' >/etc/timezone \
    && mv /usr/bin/python /usr/bin/python_2.7 \ 
    && ln -s /usr/local/bin/python3/bin/python3 /usr/bin/python \
    && cd /etc/yum.repos.d && wget https://repo.codeit.guru/codeit.el`rpm -q --qf "%{VERSION}" $(rpm -q --whatprovides redhat-release)`.repo \
    && yum install httpd -y

EXPOSE 5400 5555 6378 9000
ENTRYPOINT ["/bin/bash", "-c", "./restart.sh"]

