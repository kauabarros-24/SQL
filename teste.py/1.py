import sqlite3 

conexao = sqlite3.connect("teste.db")
marcador = conexao.cursor()

kauas = [
    ('Kaua', 'k@k.com'),
    ('Bill Gates', 'g@g.com'),
    ('Jobs', 'j@j.com'),
    ('Mark Zuckerberg', 'm@m.com'),
    ('Page', 'p@p.com'),
]
marcador.executemany("INSERT INTO kaua (nome, email) VALUES(?, ?)", kauas)

conexao.commit()
marcador.close()
conexao.close()
