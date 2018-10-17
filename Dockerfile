FROM python:3.7.0-alpine3.8
LABEL maintainer="luk.zim91@gmail.com"

COPY . /tmp/luigibio
WORKDIR /tmp/luigibio
RUN apk update --no-cache -U && \
    apk add --no-cache -U --virtual .builddeps \
        gcc \
        musl-dev && \
    python setup.py install && \
    apk del --purge .builddeps && \
    rm -rf /tmp/* /var/tmp/* && sync
WORKDIR /
 
