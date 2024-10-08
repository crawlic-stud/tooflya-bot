FROM python:3.11-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY src/app .
COPY .env .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

CMD gunicorn app.wsgi:application -b 0.0.0.0:8000 --access-logfile -