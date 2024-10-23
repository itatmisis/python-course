## Глава 6 - БД: Что такое БД, какие бывают, когда какие нужны

Запись лекции от 22 октября, 2024 года: https://t.me/itam_python_course/200

### Домашняя работа
- Спроектировать СУБД для нашего сервиса коротких ссылок, в нем должны быть таблицы:
    - link. В данной таблице будет хранится связка short-link -> long link
    - link_usage. При переходе по ссылке будет сохраняться информация о том, на какую ссылку перешел кто. Сохранять можно айпи адрес и user-agent клиента, что переходят
- Почитать про то, что такое [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) и зачем он нужен