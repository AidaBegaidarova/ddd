#!/bin/bash

default_nginx=/etc/nginx/sites-enabled/default

if [ -f $default_nginx ]; then
  sudo rm $default_nginx
fi
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo killall gunicorn
sudo gunicorn -c /home/box/web/etc/gunicorn.conf.py hello:wsgi_app -D
cd /home/box/web/ask
sudo gunicorn -c /home/box/web/etc/gunicorn.django.conf.py ask.wsgi -D
#sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database if not exists stepic_db"
mysql -uroot -e "grant all on stepic_db.* to 'box'@'localhost' identified by 'box'"
