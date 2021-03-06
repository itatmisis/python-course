### План части лекции по обучению созданию своих модулей
1. Создать простой `main.py`
2. Создать другой файл в той же директории
    - `power`
    - `dir`
    - `__doc__`
3. Создать `utils`, `core`
4. Рассказать про `if __name__ == "__main__":`
5. Relative / absolute
6. `__main__`

### План практики
1. Создание проекта с подключаемыми модулями (внешними и внутренними)
2. Создание папки `work_practice`
3. В папке создать `main.py`, который будет вызываться пользователем
4. Создать новую папку `methods` в которую добавить следующие файлы:
    - `datetime_method.py`
    - `math_method.py`
    - `str_method.py`
    - `random_method.py`
    - `re_method.py`
    - `__init__.py`
5. В каждом из файлов описать функцию `method_n(inp)`, которая принимает на вход один аргумент (n это номер человека)
6. В `main.py` написать интерфейс взаимодействия пользователя с методами посредством `input()`
   1. К примеру, принимать на вход число, на каждый метод, после вводить сам аргумент к методу
7. Всё это на компьютерах, в аудитории.

### План домашки
1. Реализовать модуль `study` который будет реализовывать:
   1. Классы `School`, `Humanoid`, `Student`, `Teacher`
   2. Класс `Humanoid` определяет семейство гуманоидных существ с аттрибутом `species`, которая является перечислением `Species`
   3. Классы `Student` и `Teacher` наследуются от `Humanoid`
   4. Класс `School` имеет аттрибуты `students` и `teachers`, которые являются списком всех студентов и учителей
   5. Каждый `Humanoid` имеет аттрибуты `first_name`, `middle_name`, `last_name` (Имя Отчество Фамилия соответственно)
2. Реализовать поиск с фильтром по школе (метод класса `School`):
   1. Поиск по роду деятельности (Студент/Учитель/Без разницы)
   2. Поиск по виду (Один вид/Несколько видов/Без разницы)
   3. Поиск по ФИО (Полное совпадение/Только фамилия или имя или отчество/Любая комбинация ФИО)