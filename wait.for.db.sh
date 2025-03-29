#!/bin/sh
until python manage.py check --database default; do
  echo "Waiting for database..."
  sleep 2
done