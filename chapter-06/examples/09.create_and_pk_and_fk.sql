CREATE TABLE book_v2(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title	TEXT,
    author_id INTEGER NOT NULL,
    price	INTEGER,
    amount	INTEGER
);

CREATE TABLE author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name	TEXT
)
