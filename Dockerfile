# https://hub.docker.com/_/python
FROM python:3.10.5-slim-bullseye

# fix for "[BUG] no output in docker logs #13"
# see https://github.com/PhilipMay/smart-prom-next/issues/13
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

RUN apt-get update && \
    apt-get -y install smartmontools && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

EXPOSE 9902

CMD ["smart-prom-next"]
