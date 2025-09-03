#!/bin/sh

# Ждём пока Postgres будет доступен
until nc -z -v -w30 db 5432
do
  echo "Waiting for postgres..."
  sleep 1
done

# Миграции и сборка статики
python manage.py migrate
python manage.py collectstatic --noinput

# Запуск Gunicorn
gunicorn server.wsgi:application --bind 0.0.0.0:8000
