FROM python:3.10

COPY ./requirements.txt /root/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /root/requirements.txt

WORKDIR /data