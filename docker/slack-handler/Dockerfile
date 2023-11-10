FROM docker.io/library/python:3.11-alpine
WORKDIR /
COPY requirements.txt /
COPY send_message.py /
RUN apk add --no-cache jq \
    && pip install --no-cache-dir -r requirements.txt