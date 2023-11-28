FROM --platform=linux/amd64 python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gcc 

RUN pip install --no-cache-dir git+https://github.com/jayvynl/django-clickhouse-backend

WORKDIR /app
COPY ./app /app

EXPOSE 8000