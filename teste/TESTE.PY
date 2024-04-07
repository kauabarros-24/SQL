import sqlite3

conexao = sqlite3.connect("banco.db")
marcador = conexao.cursor()

#marcador.execute("""
#CREATE TABLE usuario(
#    id INTEGER PRIMARY KEY,
#    nome TEXT NOT NULL,
#    email TEXT NOT NULL UNIQUE,
#    senha TEXT NOT NULL UNIQUE
#);
#""")
#d
#marcador.execute("""
#CREATE TABLE perfil_usuario(
#   localizacao INTEGER NOT NULL,
#    data_nascimento DATE,
#    sexo TEXT NOT NULL
#);
#""")

perfis = [
    (124141, "2000-01-01", 'M'),
    (11314526, "2002-01-01", "M"),
    (123141, "1955-24-02", "M")
]

marcador.executemany("INSERT INTO perfil_usuario (localizacao, data_nascimento, sexo) VALUES (?, ?, ?)", perfis)

conexao.commit()
marcador.close()
conexao.close()