-- schema.sql
SHOW DATABASES;

DROP DATABASE IF EXISTS desafio;

CREATE DATABASE IF NOT EXISTS desafio;

USE desafio;

CREATE TABLE associado(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50),
sobrenome VARCHAR(100),
idade int,
email VARCHAR(200)
);

CREATE TABLE conta(
id INT AUTO_INCREMENT PRIMARY KEY,
tipo_conta VARCHAR(10),
data_criacao TIMESTAMP,
id_associado INT,
FOREIGN KEY (id_associado) REFERENCES associado(id)
);

CREATE TABLE cartao (
id INT AUTO_INCREMENT PRIMARY KEY,
num_cartao INT,
nom_impresso VARCHAR(100),
id_conta INT,
id_associado INT,
FOREIGN KEY (id_conta) REFERENCES conta(id),
FOREIGN KEY (id_associado) REFERENCES associado(id)
);

CREATE TABLE movimento (
id INT AUTO_INCREMENT PRIMARY KEY,
vlr_transacao DECIMAL(10,2),
des_transacao VARCHAR(50),
data_movimento TIMESTAMP,
id_cartao INT,
FOREIGN KEY (id_cartao) REFERENCES cartao(id)
);

SHOW TABLES;

GRANT ALL PRIVILEGES ON desafio.* TO 'sparkuser'@'%';

FLUSH PRIVILEGES;