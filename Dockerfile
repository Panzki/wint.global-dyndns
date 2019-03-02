FROM python:3.6-alpine

COPY ./refresh_dyndns.py /app/refresh_dyndns.py
COPY ./crontab /etc/cron/crontab
RUN crontab /etc/cron/crontab

CMD ["crond", "-f"]