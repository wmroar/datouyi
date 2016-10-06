create table product(
id int auto_increment primary key,
section_id int,
title varchar(256),
name varchar(128),
content varchar(1024),
major_pic varchar(128),
user_id int,
prioriry int,
read_num int,
price float,
source varchar(128)
)


create table section(
id int auto_increment primary key,
pid int,
name varchar(128),
content varchar(256)
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

insert into section(name,content) value ('product','product')
insert into section(name,content,pid) value ('公司新闻','公司新闻')
insert into section(name,content,pid) value ('最新活动','最新活动')
insert into section(name,content,pid) value ('成功案例','product')
insert into section(name,content,pid) value ('product','product')
insert into section(name,content,pid) value ('product','product')