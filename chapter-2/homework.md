# Домашнее задание для главы 2

# Глава 1

## Предисловие
Петр получил предложение на работу в новой компании по разработке роботов Wahoo. В качестве вступительного испытания ему необходимо написать интерфейс для общения робота с пользователем. Помогите Петру выполнить его вступительное задание!

## Задание 2.1.1

### Условие
На вход подаётся строка, содержащая фамилию и имя через пробел. Необходимо написать функцию `greetings()`, которая принимает на вход строчку из ввода, и возвращает приветствие в формате строки и вывести эту строку:
```bash
in: Гендо Геннадий
out: Доброго времени суток, Гендо "Человек" Геннадий!
```

> Пояснение к примеру: необходимо вернуть из функции строку формата `Доброго времени суток, ИМЯ "Человек" ФАМИЛИЯ!`

### Пример
```bash
in: Гендо Геннадий
out: Доброго времени суток, Гендо "Человек" Геннадий!
```

## Задание 2.1.2

### Условие
На вход подаётся целое число `N`, после которого на следующей строке вводится `N` целых чисел. Необходимо написать функцию `summation()`, которая будет считать сумму всех введёных `N` чисел с условием, что:

1. Если число отрицательное, то надо сделать его положительным и умножить на два;
2. Каждое число нужно нормализовать (поделить каждое число на самое большое число)

### Пример
```bash
in_1: 5
in_2: -10 2 3 15 -4
out: 2.4
```

## Задание 2.1.3

### Условие
Необходимо написать функцию `debug_control()`, которая будет считать и возвращать количество подаваемых на ввод аргументов.

### Пример
```python
debug_control("Hello!", 1000, 7)
>> 3
```

## Задание 2.1.4

### Условие
Необходимо доработать решение из задачи [2.1.3](#задание-213) и дополнительно считать различные типы аргументов (а именно `str`, `int`, `float`) и ключевых аргументов.

### Пример
```python
debug_control("Hello!", 1000, 7, 993.0, name="Petr", task="Eliminate")
>> str: 3, int: 2, float: 1
```