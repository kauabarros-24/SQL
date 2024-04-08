import sqlite3

#Conexão + marcador
conexao = sqlite3.connect('banco.db')
marcador = conexao.cursor()

#Consulta
marcador.execute("SELECT data_nascimento FROM perfil_usuario WHERE data_nascimento BETWEEN '1955-01-01' AND '2002-01-01';")

idade_usuarios = marcador.fetchall()

for idade in idade_usuarios:
    print(idade)

marcador.close()
conexao.close()
