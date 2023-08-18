create table generations(generationid int);
create table pmdex(pmid int primary key, pmname text unique, hp int, atk int, def int, spc int, spa int, spd int, spe int);

insert into generations values(1);

insert into pmdex values(1 ,'Bulbasaur', 45, 49, 49, 65, 65, 65, 45);

select * from pmdex;
select * from generations;