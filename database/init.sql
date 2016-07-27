create table datouyi.kind(
id SERIAL4 PRIMARY KEY,
pid INT4 REFERENCES kind(id),
name VARCHAR(128),
des VARCHAR(512)
)

