create table battle_starts (
s varchar (32),
mydate varchar(256),
n varchar(32)
);

drop table if exists subs;
create table subs as
	select date '2014-01-01' + (i/30)::int as created_at,
		'foobar@foo.com' || (i % 7)::text as email
	from generate_series(1, 100) i;
create index on subs (email, created_at);