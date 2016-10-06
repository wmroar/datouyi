create table product(
id int auto_increment primary key,
title varchar(256),
name varchar(128),
content varchar(1024),
user_id int,
prioriry int,
read_num int,
price float,
source varchar(128)
)


create table section(
id int auto_increment primary key,
name varchar(128),
content title varchar(256)
)


create table user(
username varchar(64) primary key,
password varchar(64),
addr   varchar(64),
phone  varchar(64),
mail varchar(64),
role int default 0,
level int default 0,
)