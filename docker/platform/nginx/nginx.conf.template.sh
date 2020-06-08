user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;

    upstream backend_api {
        # server 10.9.242.42:5240 weight=10;
        server ${api_ip}:${api_port} weight=10;
    }
    upstream backend_common {
        # server 10.9.242.42:5140 weight=10;
        server ${common_ip}:${common_port} weight=10;
    }

    upstream backend_precision {
        # server 10.9.242.42:5200 weight=10;
        server ${precision_ip}:${precision_port} weight=10;
    }
    upstream backend_perf {
        # server 10.9.242.42:5340;
        server ${perf_ip}:${perf_port} weight=10;
    }

    upstream backend_data {
        server ${statis_ip}:${statis_port} weight=10;
    }


    server {
        # listen       9000 default_server;
        # listen       [::]:9000 default_server;
        listen       ${nginx_port} default_server;
        listen       [::]:${nginx_port} default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location /precision/socket.io/ {
            proxy_pass http://backend_precision/precision/socket.io/;
