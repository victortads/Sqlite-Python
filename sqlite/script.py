import sqlite3 as db

import pandas as pd

con = db.connect("my_database.db")

cursor = con.cursor()

cursor.execute("create table administrador ("
"ID_Diretor int NOT NULL,"
"Nome_Diretor varchar(10) NOT NULL,"
"Sobrenome_Diretor varchar(30) NOT NULL,"
"CPF_Diretor char(11) NOT NULL,"
"Nascimento_Diretor date,"
"primary key (ID_Diretor)"
")")

cursor.execute("create table estudante ("
"ID_Aluno int NOT NULL,"
"Nome_Aluno varchar(10) NOT NULL,"
"Sobrenome_Aluno varchar(30) NOT NULL,"
"CPF_Aluno char(11) NOT NULL,"
"Nascimento_Aluno date,"
"primary key (ID_Aluno)"
")")

cursor.execute("create table turma ("
"ID_Turma int NOT NULL,"
"Nome_Turma varchar(10) NOT NULL,"
"Aluno int NOT NULL,"
"primary key (ID_Turma)"
")")



con.commit()

cursor.close()
con.close()