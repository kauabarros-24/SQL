import sqlite3

#Conexão com o banco
conectar = sqlite3.connect("tutorial.db")
#Para percorrermos as tabelas
marcador = conectar.cursor()

marcador.execute("""
CREATE TABLE tarefas_programacao (
    id INTEGER PRYMARY KEY.
    title TEXT NOT NULL, 
    description TEXT NULL,
    dificuldade INTEGER NOT NULL CHEACK(dificuldade BETWEEN 1 AND 5).
    resolvidos INTEGER NOT NULL DEFAULT 0,
    );
""")