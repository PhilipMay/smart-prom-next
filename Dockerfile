# https://hub.docker.com/_/python
FROM python:3.10.5-slim-bullseye

ADD . /smart_prom_next

# TODO: change to pypi smart_prom_next install

RUN apt-get update && \
    apt-get -y install smartmontools && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir /smart_prom_next

EXPOSE 9902

CMD ["smart-prom-next"]
