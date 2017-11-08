    drop table if exists books;
    create table books (
        author_name text not null,
        ISBN text primary key not null,
        thumbnail text not null,
	times_scanned integer not null
    );

