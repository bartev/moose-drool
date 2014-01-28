drop table if exists weather;
drop table if exists cities;
create table weather (
	city 	varchar(80),
	temp_lo	int, 			-- temperature
	temp_hi	int,
	prcp	real,			-- precipitation
	date 	date
);
create table cities (
	name		varchar(80),
	location	point
);

-- drop table weather;

INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');
INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
    VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');
INSERT INTO weather (date, city, temp_hi, temp_lo)
    VALUES ('1994-11-29', 'Hayward', 54, 37);

INSERT INTO weather (date, city, temp_hi, temp_lo)
    VALUES ('1994-11-29', 'Hayward', 54, 37),
    		('1994-11-30', 'Hayward', 56, 41),
    		('1994-12-01', 'Hayward', 53, 39);

INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');
INSERT INTO cities VALUES ('San Jose', '(-190.0, 51.0)');

INSERT INTO cities (name, location) VALUES ('San Jose', DEFAULT);
COPY weather FROM '/home/user/weather.txt';


SELECT *
    FROM weather LEFT OUTER JOIN cities ON (weather.city = cities.name);

create table a (a int);
create table b (b int);
insert into a values (1), (2), (3), (4);
insert into b values (3), (4), (5), (6);
