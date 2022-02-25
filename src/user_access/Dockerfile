FROM python:3.7
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY /scripts/start.sh /app/scripts/
RUN chmod +x ./scripts/start.sh