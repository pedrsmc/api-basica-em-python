import sqlite3

DB = "database/database.db"

def conectar():
    try:
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    except sqlite3.Error as erro:
        return print("Erro ao tentar se conectar ao banco: ", erro)
