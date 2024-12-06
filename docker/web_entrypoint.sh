#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations 
python manage.py migrate

# Start server
echo "--> Starting web process"
gunicorn blog.wsgi:application -b 0.0.0.0:8030
