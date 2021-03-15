// Creation de la database

drop database if exists comptes_linux;
create database comptes_linux;

use comptes_linux;
create table users (
    username varchar(20),
    x varchar(5),
    uid int,
    gid int,
    gecos varchar(100),
    homedir varchar(50),
    prog varchar(50)
);
    
desc users;
select * from users;
