create database if not exists tp1;

use tp1;

create table if not exists citation(
    id int auto_increment primary key,
    text text(500),
    author varchar(255)
);

