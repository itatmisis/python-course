## Как скачать питон
### Инструкция для linux
Конкретно для debian-based. Остальные дестрибутивы имеют аналогичные репозитории.
- Запустите в терминале `sudo apt install -y python3 python3-pip python3-dev python3-setuptools python3-venv`
- Проверьте, что питон работает
```bash
❯ python3 --version
Python 3.8.10
```
Нам нужна версия питона не ниже `3.10`
- Установим Юпитер: `pip install jupyter`
- Запустим его: `jupyter notebook`

### Инстукция для MacOS
1. Устанавливаем [homebrew](https://brew.sh)
2. `brew install python`

### Инструкция для Windows
- Установить линукс или купить macbook
- Если этот вариант невозможен, то
    - Рекомендуем использовать [Google Colab](https://research.google.com/colaboratory/) для Юпитера.
    - Установить [PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac)
