#!/bin/bash

echo "Creating migrations..."
python app/manage.py makemigrations

echo "Migrating..."
python app/manage.py migrate
