import sqlite3
import os

class SistemaLogin:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(os.path.join(BASE_DIR, "usuarios.db"))
        self.c = self.conn.cursor()
        self.criarTabela()

    def criarTabela(self):
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()
        
    def verificarLogin(self, usuario, senha):
        self.c.execute("SELECT * FROM login WHERE usuario = ? AND senha = ?", (usuario, senha))
        resultado = self.c.fetchone()
        return bool(resultado)
    
sistema = SistemaLogin()
