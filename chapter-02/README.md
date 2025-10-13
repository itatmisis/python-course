## Урок 2 - Python 2 — ООП и ООП
Классы и ООП, датаклассы и чуть-чуть декораторов

## Домашка 1
Начиная с этой домашки и далее есть требования к дз:
1. Указывать типы - обязательно
2. Используем питон версии не менее 3.11
3. `import *` делать нельзя

Написать программу, которая тестирует перформанс следующий операций

Проверка на вхождения в коллекцию. Есть лист `["A", "B", "C", "D", ...]` и словарь `{"A", "B", "C", "D", ...}`, необходимо написать программу, которая тестирует время выполения операции `"A" in list_` и `"A" in dict_`. Провести не менее 100 итерации и выдать среднее и медианное значения. Важно протестировать на разных условиях: 
- Размеры коллекции: от 0 до 10_000 с шагом 10. (Если будет слишком долго - шаг можно увеличить)
- Местонахождения искомого элемента: положить элемент в конец, в начало, в случайное место

Пример выполнения программы:
```shell
python3 main.py

dict 10 first: 0.001 ns # 10 элементов, первый элемент - искомый
list 10 first: 0.001 ns

dict 100 first: 0.002 ns
list 100 first: 0.002 ns
...
dict 10 random: 0.002 ns
list 10 random: 0.01 ns
...
dict 10 last: 0.002 ns
list 10 last: 0.05 ns
```

## Домашка 2
Написать декодер HTTP запросов 

Создать класс `Request` вида:
```python
@dataclass
class Request:
    method: str
    path: str
    proto: str
    headers: dict[str, str]
    body: str 

    def from_str(cls, v: str) -> "Request":
        ...

    def to_str(self) -> str:
        ...
```
Функция `from_str` принимает на вход сам HTTP запрос в виде строки и должна создавать объект класса `Request`. Например: 

```python
>>> v = """POST /users HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 49

name=FirstName+LastName&email=bsmth%40example.com"""
>>> Request.from_str(v) 
Request(method='POST', path='/users', proto="HTTP/1.1", headers={'Host': 'example.com', ...}, ...)
```
Функция `to_str` возвращает HTTP запрос в виде строки