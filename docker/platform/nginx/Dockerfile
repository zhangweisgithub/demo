FROM docker.io/nginx:latest
RUN rm -rf /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/nginx.conf
ENV api_ip 10.9.242.41
ENV api_port 5200
ENV common_ip 10.9.242.41
ENV common_port 5100
ENV precision_ip 10.9.242.51
ENV precision_port 5200
ENV perf_ip 10.9.242.41
ENV perf_port 5600
ENV ci_ip 10.9.242.41
ENV ci_port 5050
ENV statis_ip 10.9.242.41
ENV statis_port 5880
ENV manual_ip 10.9.242.41
ENV manual_port 5800
ENV sdk_ip 10.9.242.35
ENV sdk_port 6001
ENV security_ip 10.9.242.41
ENV security_port 5900
ENV front_ip 10.9.242.41
ENV front_port 9001
ENV nginx_port 80
COPY nginx.conf.template /etc/nginx
RUN apt-get update && apt-get install net-tools
RUN apt-get install vim -y
CMD envsubst '$api_ip $api_port $common_ip $common_port $precision_ip $precision_port $ci_ip $ci_port $perf_ip $perf_port $statis_ip $statis_port $manual_ip $manual_port $sdk_ip $sdk_port $security_ip $security_port $nginx_port $front_ip  $front_port' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
