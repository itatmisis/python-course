## Урок 3 - WEB 1 — HTTP, JSON и REST
HTTP, JSON и REST

## Домашка
Написать декодер HTTP запросов 

Создать класс `Request` вида:
```python
@dataclass
class Request:
    method: str
    path: str
    proto: str
    headers: dict[str, str]
    bode: str 

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
>>> Request(method='POST', path='/users', proto="HTTP/1.1", headers={'Host': 'example.com', ...}, ...)
```
Функция `to_str` возвращает HTTP запрос в виде строки