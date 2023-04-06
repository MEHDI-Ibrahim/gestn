FROM python:alpine

COPY ./login .


RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r app/requirements.txt \
  && rm -rf /var/cache/apk/*


EXPOSE 5050

CMD python app/login.py
