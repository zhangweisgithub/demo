FROM centos:v7
RUN mkdir /frontend
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
ADD /ssh /root/.ssh
WORKDIR /frontend
ADD /frontend /frontend
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
RUN yum install -y nodejs && yum install -y git && npm install -g n
RUN n v8.11.3
RUN npm install -y
RUN npm install -y vue-cli && npm install --save v-charts && npm install --save crypto-js -y && npm install stylus && npm install stylus-loader
RUN npm rebuild node-sass
EXPOSE 9000 9001
CMD ["npm", "run", "dev"]
