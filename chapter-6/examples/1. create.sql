/*
CREATE OR REPLACE TABLE tableName (
  col1 datatype,
  col2 datatype,
  ...
  colN datatype,
  PRIMARY KEY (одна или более колонка)
);
*/

CREATE OR REPLACE TABLE book(
    book_id INTEGER,  --PRIMARY KEY AUTOINCREMENT
    title	TEXT,
    author	TEXT,
    price	INT,
    amount	INT
)
