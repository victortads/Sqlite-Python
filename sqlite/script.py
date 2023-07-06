import sqlite3 as db
import pandas as pd

conn = db.connect("meu_banco.db")
cursor = conn.cursor()

#Comandos para criar as tabelas
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
"Diretor int not null, foreign key (Diretor) references administrador(ID_Diretor)"
"primary key (ID_Aluno)"
")")

cursor.execute("""
INSERT INTO administrador (ID_Diretor, Nome_Diretor, Sobrenome_Diretor, CPF_Diretor, Nascimento_Diretor) VALUES 
               (1, 'Renata', 'Silva', '13424234542', '1978-12-15'),
               (2, 'Fernando', 'Oliveira', '05987541201', '1990-06-25'),
               (3, 'Amanda', 'Pereira', '08456874563', '1982-09-03'),
                (4, 'Ricardo', 'Santos', '19785678901', '1987-04-18'),
               (5, 'Patrícia', 'Rodrigues', '12345098765', '1989-07-12'),
               (6, 'Diego', 'Ferreira', '03214568902', '1984-03-27'),
               (7, 'Cristina', 'Costa', '25413654877', '1975-10-30'),
               (8, 'Alexandre', 'Almeida', '09876123456', '1988-02-05'),
               (9, 'Isabella', 'Ribeiro', '04215786543', '1992-11-08'),
               (10, 'Leandro', 'Martins', '15789456789', '1981-08-22')
               """)

cursor.execute("insert into estudante"
"(ID_Aluno, Nome_Aluno, Sobrenome_Aluno, CPF_Aluno, Nascimento_Aluno, Diretor)"
"values"
"(1, 'Laura', 'Fernandes', '9876543210', '2005-09-15', 2),"
"(2, 'Pedro', 'Silva', '1234567890', '2006-06-02', 2),"
"(3, 'Isabela', 'Pereira', '4567890123', '2009-11-20', 1),"
"(4, 'Lucas', 'Rodrigues', '5678901234', '2003-04-10', 3),"
"(5, 'Gabriela', 'Santos', '2345678901', '2007-07-30', 1),"
"(6, 'Rafael', 'Costa', '8901234567', '2004-02-14', 5),"
"(7, 'Lara', 'Martins', '3456789012', '2010-03-25', 4),"
"(8, 'Gustavo', 'Oliveira', '6789012345', '2008-08-18', 6),"
"(9, 'Sophia', 'Almeida', '9012345678', '2002-12-05',6),"
"(10, 'Enzo', 'Ribeiro', '5678901234', '2006-10-12',7)")

#Comandos especiais
# estudante = pd.read_sql_query("Select * from estudante", conn)
# estudante

# query = """
#     SELECT estudante.Nome_Aluno, administrador.Nome_Diretor
#     FROM estudante
#     INNER JOIN administrador ON estudante.Diretor = administrador.ID_Diretor
#     """
# cursor.execute(query)

# result = cursor.fetchall()
# result

# pd.read_sql_query("""
#      SELECT estudante.Nome_Aluno, administrador.Nome_Diretor
#     FROM estudante
#     INNER JOIN administrador ON estudante.Diretor = administrador.ID_Diretor
#     """, conn)

# pd.read_sql_query("""
#      SELECT estudante.Nome_Aluno, administrador.Nome_Diretor
#     FROM estudante
#     LEFT JOIN administrador ON estudante.Diretor = administrador.ID_Diretor
#     """, conn) 


conn.commit()

cursor.close()
conn.close()