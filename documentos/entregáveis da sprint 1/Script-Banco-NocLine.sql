create database nocLine;
use nocLine;


create table empresa (
idEmpresa int primary key auto_increment,
razaoSocial varchar (50),
CNPJ char (14),
telCel char (11),
telFixo char (10),
cep char (9)
);

create table endereco (
idEndereco int  auto_increment,
num int ,
bairro varchar (45), 
cidade varchar (45) ,
estado char (2),
pais varchar (45),
complemento varchar  (45),
fkEmpresaEndereco int,
constraint fkEmpresaEndereco foreign key (fkEmpresaEndereco ) references  empresa (idEmpresa),
constraint pkCompostaEndereco primary key (idEndereco, fkEmpresaEndereco)
) auto_increment = 50;

create table nivelAcesso (
idNivelAcesso int primary key auto_increment,
tipoPermicao char (3),
constraint ckPermicao check (tipoPermicao in("CCO", "SSO" , "RL"))
) ;

insert into nivelAcesso values 
(null, 'CCO'),
(null, 'SSO'),
(null, 'RL');

create table usuario (
idUsuario int  auto_increment,
nome varchar (45),
email varchar(50),
senha varchar (45),
fkNivelAcesso int,
constraint fkNivelAcesso foreign key (fkNivelAcesso) references nivelAcesso (idNivelAcesso),
fkEmpresaUsuario int, 
constraint fkEmpresaUsuario foreign key (fkEmpresaUsuario) references empresa (idEmpresa),
constraint pkCompostaEndereco primary key (idUsuario,fkNivelAcesso, fkEmpresaUsuario)
);

create table maquina (
idMaquina int auto_increment,
IP char (14),
SO varchar (20),
modelo varchar (45),
fkEmpresaMaquina int,
constraint fkEmpresaMaquina foreign key (fkEmpresaMaquina) references empresa (idEmpresa),
fkUsuarioMaquina int, 
constraint fkUsuarioMaquina foreign key (fkUsuarioMaquina) references usuario (idUsuario),
fkNivelAcesso int,
constraint fkNivelAcessoMaquina foreign key (fkNivelAcesso) references nivelAcesso (idNivelAcesso),
constraint pkCompostaMaquina primary key (idMaquina, fkEmpresaMaquina));

create table componentes (
idComponente int primary key auto_increment,
nomeComponente CHAR (5),
constraint ckComponente check ( nomeComponente in("RAM", "CPU" , "JA", "DISK","REDES"))
);

insert into componentes values
(null, 'CPU'),
(null, 'RAM'),
(null, 'DISK'),
(null, 'REDES'),
(null, 'JA');

create table monitoramento(
idMonitoramento int auto_increment,
uso double, 
dtHora datetime default current_timestamp,
fkMaquinaMonitoramento int,
fkEmpresaMonitoramento int,
fkComponentes int ,
constraint fkMaquinaMonitoramento foreign key (fkMaquinaMonitoramento) references maquina (idMaquina),
constraint fkEmpresaMonitoramento foreign key (fkEmpresaMonitoramento) references empresa(idEmpresa),
constraint fkComponentes foreign key (fkComponentes) references componentes(idComponente),
constraint pkCompostaMonitoramento primary key(idMonitoramento, fkMaquinaMonitoramento, fkEmpresaMonitoramento, fkComponentes)
) auto_increment = 100;

create table nivelAviso (
idNivelAviso int primary key auto_increment,
escalonamento varchar (45),
constraint ckNivelAcesso  check ( escalonamento in("Urgente", "Importante" , "Atenção"))
);
insert into nivelAviso values
(null, 'Urgente'),
(null, 'Importante'),
(null, 'Atenção');

CREATE TABLE aviso (
	idAviso INT AUTO_INCREMENT,
	titulo VARCHAR(100),
	descricao VARCHAR(150),
	fkUsuario INT,
    fkMonitoramento int,
    fkMaquina int,
    fkEmpresaAviso int,
    fkNivelAviso int , 
	constraint fkUsuarioAviso foreign key  (fkUsuario) references  usuario(idUsuario),
   constraint fkMonitoramentoAviso foreign key  (fkMonitoramento) references  monitoramento(idMonitoramento),
  constraint fkMaquinaAviso  foreign key  (fkMaquina) references  maquina (idMaquina),
  constraint fkEmpresaAviso  foreign key  (fkEmpresaAviso) references  empresa(idEmpresa),
    constraint fkNivelAviso foreign key (fkNivelAviso) references nivelAviso (idNivelAviso),
    constraint pkComposta primary key (idAviso,fkUsuario, fkMonitoramento, fkMaquina, fkEmpresaAviso, fkNivelAviso)
);

