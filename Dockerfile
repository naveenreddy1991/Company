FROM python:3.7.2

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt app/requirements.txt

run pip install -r requirements.txt

COPY . /app