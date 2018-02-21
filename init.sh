#!/bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo gunicorn -c etc/hello.py hello:wsgi_app -D
#sudo /etc/init.d/gunicorn restart
