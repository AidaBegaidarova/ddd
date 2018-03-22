#!/bin/bash

default_nginx=/etc/nginx/sites-enabled/default

if [ -f $default_nginx ]; then
  sudo rm $default_nginx
fi
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo killall gunicorn
sudo gunicorn -c etc/gunicorn.conf.py hello:wsgi_app -D
cd ask
sudo gunicorn ask.wsgi -D
#sudo /etc/init.d/gunicorn restart
