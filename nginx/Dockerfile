FROM nginx:1.11.7

RUN apt-get update

# 設定ファイル nginx
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/default.conf /etc/nginx/sites-available/default
ADD nginx/default.conf /etc/nginx/sites-enabled/default
ADD nginx/start-nginx.sh /etc/nginx/start-nginx.sh
ADD nginx/uwsgi_params /etc/nginx/uwsgi_params
ADD nginx/robots.txt /usr/share/nginx/robots.txt

# Web Resource
RUN mkdir -p /var/www/static
ADD django/static /var/www/static/