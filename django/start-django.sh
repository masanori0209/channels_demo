#!/bin/bash
sleep 5
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --socket :8001 --module chat_demo.wsgi & daphne -b 0.0.0.0 -p 3001 --ping-interval 10 --ping-timeout 120 chat_demo.asgi:application
