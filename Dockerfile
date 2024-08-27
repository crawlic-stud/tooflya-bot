FROM python:3.11-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY src/app .

RUN python manage.py collectstatic --noinput

CMD gunicorn app.wsgi:application -b 0.0.0.0:8000