FROM python:3.6-alpine

RUN adduser -D appuser
WORKDIR /home/appuser

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY webapp.py config.py entrypoint-webapp.sh entrypoint-dev.sh ./
RUN chmod +x entrypoint-webapp.sh entrypoint-dev.sh

# Mounting a volume has caused issues when hosting on a server because the files
# from the volume don't get the proper owner set after the image is created
COPY app/ ./app

ENV FLASK_APP webapp.py

RUN chown -R appuser:appuser ./
USER appuser

CMD ["./entrypoint-webapp.sh"]
