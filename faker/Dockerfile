FROM python:3.8-alpine

MAINTAINER Le Grand Poxa

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV WAIT_VERSION 2.7.2

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app /app

Expose 5555

CMD python generate_Fake_Data.py
CMD python generate_fake_Notes.py

