drop table if exists books;
create table books (
    title text not null,
    author_name text not null,
    ISBN text primary key not null,
    thumbnail text not null,
    times_scanned integer not null
);