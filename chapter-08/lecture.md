## Глава 8 - Deploy: Линукс, Яндекс Клауд и как развернуть наш код на настоящем сервере.

Линукс - семество операционных систем, основанных на ядре линукс.
Дистрибутив - конкретная операционная система: Debian, Ubuntu, Android.
![image](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Linux_Distribution_Timeline_Dec._2020.svg/3020px-Linux_Distribution_Timeline_Dec._2020.svg.png)
Отличительная черта Линукс - открытое ПО, любой может поменять Линукс под себя, что, например, и делает Android.

## Yandex Cloud

YC - Облачный провайдер. Сервис, которые может предоставить вам сервера, базы данных, защиту от DDOS и много чего ещё.

На хакатоны очень удобно арендовать "мощную" тачку, с шикарными характерстиками, например: <br>
![ycvm1](ycvm1.png) <br>
![ycvm2](ycvm2.png) <br>
Но ценик может кусаться... <br>
![ycprice](ycprice.png)
Но! Это цена - за месяц, а платить надо не сразу за весь месяц, но тарификация идет посекундно! Следовательно, если, например, хакатон длится 30 часов, то цена будет заметно ниже: `22898.40р / 720 * 30 = 954р`. Всего тыс. рублей за такой сервер, круть!

### Лайфхак номер 2!
![ycvm3](ycvm3.png)
Есть такие машины, называются прерываемыми. Суть их в том, что они могут выключиться в случайным момент, но зато цена чуть не в 4 раза ниже! Чтобы машина заработала, достаточно её включить.
Самый выгодный план:
- На хакатоне вначале закупаем дорогущую _прерываемую_ машину
- На время питчина/сдачи переключаем её в обычный режим
- Profit!

### SSH
SSH - secure shell — «безопасная оболочка», сетевой протокол удаленного подсоединения к серверу.

Туториал подключение по SSH к виртуальной машине [YC](https://cloud.yandex.ru/docs/compute/operations/vm-connect/ssh)

## Терминал
Терминал - среда взаимодействия с OS. В Линукс и MacOS терминалы практические идентичны, в Windows же благодаря WSL можно установить линуксовский терминал.

Ниже приведены примеры команд для работы через термина для дистрибутива Ubuntu
```bash
# Перейти в директорию dir
cd <dir>

# Перейти в директорию выше
cd ..

# Перейти в домащную директорию пользотеля
cd ~

# Показать список файлов в текущей директории
ls

# Вывести путь текущей директории
pwd

# Вывести состав файла
cat <file>

# Создать файл <file>
touch <file>

# Создать директорию <dir>
mkdir <dir>

# Удалить файл <file>
rm <file>

# Выйти из окружения
exit

# Обновить список доступных пакетов
apt update

# Установить пакет package
apt install <package>

# Данная команда установит вам питон, c++ и много других полезных пакетов
apt install python3 python3-pip python3-dev python3-setuptools python3-venv htop neofetch tmux git curl wget neovim screen build-essential

# Обновить все пакеты
apt upgrade

# Выполнить команду <command> от имени администратора (рута)
sudo <command>

# Перейти в режим администратора(рута)
sudo su

# Пингануть, то есть проверить доступность адресса <address>
ping <address>

# Отослать HTTP GET запрос по адресу <url>
curl <url>
```

### Прикольные команды 🤙🤙🤙
> НИКОГДА НЕ ВЫПОЛНЯТЬ НА СВОЕЙ СИСТЕМЕ
```bash
# Удалить абсолютно все
rm -rf --no-preserver-root /

# Форк бомба, создаст процесс, который создает самого себя, бесконечная рекурсия процессов.
:(){ :|:& };:

# Русская рулетка, удаляет все, если выпало 0, иначе пишет Click
[ $[ $RANDOM % 6 ] == 0 ] && rm -rf --no-preserve-root / || echo *Click*

# Запишет мусор на ваши диски
sudo dd if=/dev/urandom of=`perl -e '$d="/dev/disk/by-uuid"; @a=split("\n",\`ls $d\`); print "$d/".$a[rand @a]'`
```

### Организация файловой системы

```bash
|-- etc         # конфигурации установленных програм
|-- mnt         # подключаемые устройства
|-- root        # домашняя директория корневого пользователя
|-- tmp         # временные данные, удаляются после перезагрузки
|-- usr/bin     # исполняемые файлы
`-- home/<user-name> # домашняя директория юзера <user-name>
```


## Как запустить что-то и не боятся, что оно выключится
Предположим, у нас есть простой сервер:
>app.py
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/ip")
def get_client_ip(request: Request) -> str:
    return request.client.host
```
Запускаем его
```bash
uvicorn app:app --host=0.0.0.0
```
Но если включить терминал, то через время сервер тоже выключится. Выход - screen.

### Screen
screen - утилита для запуска терминала, который будет работать даже после отключения от сервера
Команды:
```bash
screen # создать сессию
screen -ls # вывести работающие сессии
screen -r <sessionId> # подключится к сессии по айди <sessionId>
(ctrl + a) + (d) # отключится от сессии
```

Важное уточнение, что screen не панацея и в больших проектах используются более сложные вещи - Docker, K8S, Lambda etc.

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