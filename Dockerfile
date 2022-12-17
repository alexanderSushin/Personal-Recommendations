FROM python:3.10-slim AS bot

RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

WORKDIR /api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x bot.py

CMD python3 bot.py
