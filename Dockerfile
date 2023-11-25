FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config  \
    default-mysql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .