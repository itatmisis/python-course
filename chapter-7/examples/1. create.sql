/*
CREATE TABLE tableName (
  col1 datatype,
  col2 datatype,
  ...
  colN datatype,
  PRIMARY KEY (одна или более колонка)
);
*/

CREATE TABLE book(
    book_id INTEGER,  --PRIMARY KEY AUTOINCREMENT
    title	VARCHAR(50),
    author	VARCHAR(30),
    price	DECIMAL(8, 2),
    amount	INT
)