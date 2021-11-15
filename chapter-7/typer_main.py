#!/usr/bin/env python3

# sys и os библиотеки для работы с ОС
import sys
# pathlib - работа с путями
from pathlib import Path
import os

import typer

SCRIPT = Path(os.path.realpath(__file__))
PARENT = SCRIPT.parent
app = typer.Typer()


@app.command()
def ls(directory: str):
    """
    Документация!!!
    """
    folder = PARENT / directory
    for file in folder.iterdir():
        print('file' if file.is_file() else 'directory',  file.name, sep=': ')


@app.command()
def ping(host: str):
    result = os.system(f'ping {host} -c 4')
    print(result)


if __name__ == "__main__":
    app()