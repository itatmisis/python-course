GRANT ALL PRIVILEGES ON DATABASE db_main TO db_main;

\c db_main;

CREATE TABLE public.user (
        id BIGSERIAL NOT NULL,
        name TEXT
);

INSERT INTO public.user(name) values ('Peter'), ('Amelia'), ('Artem'), ('Ilia'), ('Ivan'), ('Ksenia'), ('Maria');
