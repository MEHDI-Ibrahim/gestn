FROM python:3.8-alpine


COPY ./notes .

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r app/requirements.txt \
  && rm -rf /var/cache/apk/*

EXPOSE 5051

CMD python app/notes.py
