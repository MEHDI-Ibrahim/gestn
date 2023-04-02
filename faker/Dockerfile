FROM python:3.8-alpine


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV WAIT_VERSION 2.7.2

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app /app

RUN python generate_Fake_Data.py
RUN python generate_fake_Notes.py

EXPOSE 5555