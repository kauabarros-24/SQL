import sqlite3 

conexao = sqlite3.connect("teste.db")
marcador = conexao.cursor()

num_tuplas = int(input("Digite quantas usuários deseja inserir: "))

tuplas = []
for i in range(num_tuplas):
    valores = input(f"Insira os valores da tupla {i + 1} separados por vírgula: ")
    tupla = tuple(valores.split(','))
    tuplas.append(tupla)

usuarios = [item for tupla in tuplas for item in tupla]


marcador.executemany("INSERT INTO usuario (nome, EMAIL, SENHA) VALUES(?, ?, ?)", usuarios)

conexao.commit()
marcador.close()
conexao.close()
