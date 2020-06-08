FROM registry.sensetime.com/sensetest/centos_python3.7:v2.1
ADD /ssh /root/.ssh
RUN mkdir /platform/backend-api
COPY /platform/backend-api-only/requirements.txt /platform/backend-api
COPY /platform/backend-api-only/restart.sh /platform/backend-api
ADD /platform/backend-api-only/scripts /platform/backend-api/scripts
WORKDIR /platform/backend-api
RUN yum -y update \
    && yum -y install epel-release \
    && yum -y install net-tools \
    && yum install golang -y \
    && yum install ntpdate -y \
    && yum install java -y \
    && yum erase httpd.x86_64 -y \
    && yum clean all \
    && rm -rf /var/lib/yum/yumdb


RUN pip3 install --no-cache-dir -r /platform/backend-api/requirements.txt \
    && pip3 install --no-cache-dir -r scipts/requirements_adv.txt    /
    && pip3 install --no-cache-dir -r  scipts/requirements_cvats.txt  /
    && pip3 install --no-cache-dir -r  scipts/requirements_g10.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_iot.txt    /
    && pip3 install --no-cache-dir -r  scipts/requirements_sats.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_sg.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_solution.txt /
    && pip3 install --no-cache-dir -r  scipts/requirements_ss.txt     /
    && pip3 install --no-cache-dir -r  scipts/requirements_vats.txt  /
    && pip3 install --no-cache-dir -r  scipts/requirements_biats.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_eig_bd.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_gwt.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_rd_sym.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_senseid.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_soc.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_sp.txt    /
    && pip3 install --no-cache-dir -r  scipts/requirements_tp_ats.txt   /
    && pip3 install --no-cache-dir -r  scipts/requirements_vl.txt
    && pip3 uninstall kafka -y \
    && pip3 uninstall kafka-python -y \
    && pip3 install --no-cache-dir kafka-python \
    && pip3 install --no-cache-dir redis --upgrade \
    && pip3 install --no-cache-dir xeger --upgrade \
    && pip3 install --no-cache-dir spark-python


RUN yum install -y libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false \
    && yum install -y git \
    && chmod +x /platform/backend-api/restart.sh  \
    && yum -y install tzdata \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' >/etc/timezone \
    && ntpdate -u cn.pool.ntp.org \
    && rm -rf /platform/backend-api/* \
    && rm -f /home/* \
    && mv /usr/bin/python /usr/bin/python_2.7 \
    && ln -s /usr/local/bin/python3/bin/python3 /usr/bin/python \
    && yum clean all \
    && rm -rf /var/lib/yum/yumdb

EXPOSE 5400 5555
ENTRYPOINT ["/bin/bash", "-c", "./restart.sh"]

