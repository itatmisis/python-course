# Базовый образ. По умолчанию берется из https://hub.docker.com/
FROM python:3.13-trixie

# Выполнить команду в контейрене.
RUN apt-get update && apt-get install -y gcc python3-dev

# Поменять рабочую директорию. Если ее нет, создать ее.
WORKDIR /app

# Скопировать из материнской машины в контейнер
COPY ./requirements.txt /app/requirements.txt

# Установить зависимости
RUN pip install -r /app/requirements.txt

# Скопировать остальной исходный код
COPY . /app

# Запустить команду
CMD ["python", "web_app.py"]
