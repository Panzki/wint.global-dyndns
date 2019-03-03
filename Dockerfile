FROM python:3.6-alpine

COPY ./docker-entry.sh /app/
COPY ./cron-refresh.sh /app/
COPY ./refresh_dyndns.py /app/
COPY ./crontab /etc/cron/crontab

RUN ["chmod", "+x", "/app/docker-entry.sh"]
RUN ["chmod", "+x", "/app/cron-refresh.sh"]
RUN crontab /etc/cron/crontab

CMD /app/docker-entry.sh