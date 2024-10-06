## Как скачать питон

В идеале использовать версию питона не ниже 3.10

### Инструкция для linux
Конкретно для debian-based. Остальные дестрибутивы имеют аналогичные репозитории.
- Запустите в терминале `sudo apt install -y python3 python3-pip python3-dev python3-setuptools python3-venv`
- Проверьте, что питон работает
```bash
❯ python3 --version
Python 3.10.13
```
Нам нужна версия питона не ниже `3.10`
- Установим Юпитер: `pip install jupyter`
- Запустим его: `jupyter notebook`

### Инстукция для MacOS
1. Устанавливаем [homebrew](https://brew.sh)
2. `brew install python`

### Инструкция для Windows
- Установить линукс или купить macbook
- Если этот вариант невозможен, то перепроверьте, можете ли вы купить Macbook Air.
- Если не возможно, то постарайтесь установить WSL с докером и подключить VSCode к нему.
    - WSL: https://winitpro.ru/index.php/2020/07/13/zapusk-linux-v-windows-wsl-2/
    - VSCode with WSL: https://code.visualstudio.com/docs/remote/wsl
    - Docker in WSL: https://docs.docker.com/desktop/wsl/

### Среды разработки
- [PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac), универсальная и самая простая среда
- [VSCode](https://code.visualstudio.com/) - минималистичная среда разработки, если у вас слабый ПК, то лучше использовать её, чем PyCharm, так как он кушает много RAM.
- [Jupyter](https://jupyter.org/) - ячеечная среда разработки, хорошо подходит для аналитики, МЛ, для бекенда не очень подойдет.
- [Google Colab](https://research.google.com/colaboratory/) - тоже самое, что jupyter, но онлайн без регистрации, СМС и скачиваний.
