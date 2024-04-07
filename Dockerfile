FROM python:3.11.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt --default-timeout=10000

COPY ./docker_data /app/app

WORKDIR /app/app