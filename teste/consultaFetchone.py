import sqlite3

conexao = sqlite3.connect('banco.db')
marcador = conexao.cursor()

marcador.execute('SELECT nome FROM usuario WHERE id = 1;')

nome_usuario = marcador.fetchone()

try:
    for nome in nome_usuario: print(nome)
   #for nome in nome_usuario: print(nome[0]) -> Acesso a primeira letra do nome;
except sqlite3.OperationalError:
    print("Há um erro de conexão")

marcador.close()
conexao.close()