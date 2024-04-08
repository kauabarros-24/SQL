import sqlite3

#Conexao com o banco de dados
conexao = sqlite3.connect('banco.db')
marcador = conexao.cursor()

#Reazlizar consulta
try:
    marcador.execute('SELECT email FROM usuario WHERE email LIKE "%.com";')
    email_usuario = marcador.fetchall()
    for email in email_usuario:
        print(email)
except sqlite3.OperationalError:
    print("sqlite3 não encontrou a tabela")

marcador.close()
conexao.close()