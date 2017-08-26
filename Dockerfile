FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_DIR=/srv/website

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY website/requirements.txt $APP_DIR

RUN pip install -r requirements.txt

COPY website $APP_DIR
