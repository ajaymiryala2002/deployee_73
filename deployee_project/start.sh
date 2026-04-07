#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn deployee_project.wsgi:application