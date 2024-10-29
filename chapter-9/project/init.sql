create table link(
    id uuid primary key,

    short_link text unique not null,
    long_link text not null
);
