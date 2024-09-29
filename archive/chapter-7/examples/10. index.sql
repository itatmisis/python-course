/*
CREATE INDEX indexName
ON tableName (colName);
*/

CREATE INDEX author_id_index
on book_v2(author_id);

DROP INDEX author_id_index;

drop database
