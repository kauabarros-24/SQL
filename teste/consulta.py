import sqlite3

#Conexao com o banco de dados
conexao = sqlite3.connect('banco.db')
marcador = conexao.cursor()

#Reazlizar consulta
try:
    marcador.execute('SELECT nome FROM usuario WHERE nome LIKE "%aua";')
    nome_usuario = marcador.fetchall()
    for nome in nome_usuario:
        print(nome)
except sqlite3.OperationalError:
    print("sqlite3 não encontrou a tabela")

marcador.close()
conexao.close()