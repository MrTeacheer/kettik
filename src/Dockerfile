FROM python:3.10-slim

WORKDIR /kettik

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./startup.sh