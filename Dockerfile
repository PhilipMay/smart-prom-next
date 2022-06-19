# https://hub.docker.com/_/python
FROM python:3.10.5-slim-bullseye

RUN apt-get update && \
    apt-get -y install smartmontools && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir prometheus_client

ADD smart_prom_next /smart_prom_next

WORKDIR /smart_prom_next

EXPOSE 9902

CMD ["python","-u","/smart_prom_next/main.py"]
