CREATE DATABASE ApeOpsArcade;

USE ApeOpsArcade;

CREATE TABLE IF NOT EXISTS utente(
	Nickname varchar(25) NOT NULL,
	Password varchar(32) NOT NULL,
	Email varchar(32) NOT NULL,
	Nazione CHAR(3),
	DataNascita DATE,
	PRIMARY KEY (Nickname)
	);

CREATE TABLE IF NOT EXISTS tasto(
	CodiceTasto CHAR(4) NOT NULL,
	Descrizione varchar(15),
	PRIMARY KEY (CodiceTasto)
	);

CREATE TABLE IF NOT EXISTS configura(
	CodTasto CHAR(4) NOT NULL,
	NickUser varchar(25) NOT NULL,
	Azione varchar(15) NOT NULL,
	PRIMARY KEY (CodTasto, NickUser),
	FOREIGN KEY (CodTasto) REFERENCES tasto(CodiceTasto),
	FOREIGN KEY (NickUser) REFERENCES utente(Nickname)
	);

CREATE TABLE IF NOT EXISTS salvataggio(
	CodiceS CHAR(16) NOT NULL,
	Data DATETIME,
	Tempo TIME NOT NULL,
	Punteggio INT NOT NULL,
	UserNick varchar(25),
	PRIMARY KEY (CodiceS),
	FOREIGN KEY (UserNick) REFERENCES utente(Nickname)
	);

SHOW TABLES;

CREATE INDEX nazione_ind ON utente(Nazione);
CREATE INDEX punteggio_ind ON salvataggio(Punteggio);

