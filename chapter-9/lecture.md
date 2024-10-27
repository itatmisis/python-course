### Requirements
`requirementx.txt` - это файл, для управления зависимостями.
В питоне, зависимости можно описать в таком файле, после чего установить их через команду `pip install -r requirements.txt`


```python
fastapi==0.104.1 # точная версия
uvicorn>=0.24,<1 # любая версия больше или равная 0.24.0, но строго меньше 1.0.0
pydantic-settings>0.2 # любая версия выше 0.2.0
```

### Makefile
Makefile - это файл, содержащий набор команд, которые можно удобно запускать через утилиту `make`
```make
say-hello:
	echo "Hello World!"

install:
	pip install -r requirements.txt

run:
	cd app && python entrypoint.py
```


### Докер
![image](https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg?uselang=ru)
Система для автоматизации развёртывания и управления контейнерами.
Позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер.
### Прелести докера
#### Декларативность описания
Используя Dockerfile и docker-compose можно однозначно описать как запускать проект

#### Универсальность
Если у вас установлен докер, вы можете запустить хоть что на хоть чем.

#### Изолированность
Контейнеры по умолчанию не могут влиять на вашу "материнскую" систему и взаимодействовать с друг-дружкой.

### Ссылки
- [Инструкция работы с докер от создателя Fastapi](https://fastapi.tiangolo.com/ru/deployment/docker/)
- [Установка докер](https://docs.docker.com/engine/install/)
- [Пример проекта с докером](https://github.com/TeaDove/evraz-hack-misis-anime/tree/master/backend)
