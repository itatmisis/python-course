# Базовый образ. По умолчанию берется из https://hub.docker.com/_/python
FROM python:3.10-slim

# Выполнить команду в контейрене.
RUN apt-get update && apt-get install -y gcc python3-dev

# Поменять рабочую директорию. Если ее нет, создать ее.
WORKDIR /code

# Скопировать из материнской машины в контейнер
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./app /code/app

WORKDIR /code/app

# Запустить команду
CMD ["python", "entrypoint.py"]
