import sqlite3

conexao = sqlite3.connect("banco.db")
marcador = conexao.cursor()



marcador.close()
conexao.close()