CREATE TABLE book_v2(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title	VARCHAR(50),
    author_id INTEGER NOT NULL,
    price	DECIMAL(8, 2),
    amount	INTEGER,
    FOREIGN KEY (author_id)  REFERENCES author (id)
);

CREATE TABLE author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name	VARCHAR
)