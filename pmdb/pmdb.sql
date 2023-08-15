sqlite3 pmdb.sqlite3

create table tbl1(one text, two int);
insert into tbl1 values('hello!',10);
insert into tbl1 values('goodbye', 20);
select * from tbl1;