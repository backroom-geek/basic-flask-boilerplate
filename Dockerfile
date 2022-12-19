FROM python:3.8.3

ARG APP_PORT

LABEL maintainer="Backroom Geek <adom2989@backroomgeek.dev>"

WORKDIR /my-boilerplate-app

COPY requirements.txt .

RUN pip install --no-cache-dir --trusted-host pypi.python.org  -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:${APP_PORT} 'server:create_app()' -w 3 --threads 3 --reload
