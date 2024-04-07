import sqlite3

conexao = sqlite3.connect('banco.db')
marcador = conexao.cursor()

marcador.execute("SELECT nome FROM usuario")

nome_usuarios = marcador.fetchall()

for nome in nome_usuarios:
    print(nome)


marcador.close()
conexao.close()