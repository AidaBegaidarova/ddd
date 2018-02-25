#!/bin/bash

if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/default
fi
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo killall gunicorn
sudo gunicorn -c etc/gunicorn.conf.py hello:wsgi_app -D
#sudo /etc/init.d/gunicorn restart
