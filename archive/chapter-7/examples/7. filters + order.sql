/*
 SELECT col1, col2, ...colN
FROM tableName
WHERE condition
ORDER BY colName [ASC|DESC];
 */
-- примеры для вставки
/*
INSERT INTO book(title, author, price, amount)
VALUES ('Герой нашего времени', 'Лермонтов М.Ю.', 999, 5);

INSERT INTO book(title, author, price, amount)
VALUES ('Тысячеликий герой', 'Кэмпбелл Дж.', 1703, 1);

INSERT INTO book(title, author, price, amount)
VALUES ('Паттерны разработки на Python', 'Персиваль Г.', 8000, 2);
*/

SELECT title, author, price
FROM book
WHERE amount >= 2
ORDER BY price
