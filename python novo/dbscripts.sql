create database logbateria;

create table log(
    id int primary key auto_increment,
    data_hora datetime,
    alerta varchar(255),
    status_bateria decimal(5,2)
)character set='utf8mb4'; 