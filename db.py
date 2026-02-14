import sqlite3
import os
from tkinter import messagebox

class Database:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(os.path.join(BASE_DIR, "database.db"))
        self.c = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.c.execute('''
                       CREATE TABLE IF NOT EXISTS bancoPessoas (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome TEXT, 
                           sexo TEXT,
                           cpf VARCHAR(11),
                           data_nasc TEXT,
                           rg TEXT,
                           orgao_expedidor TEXT,
                           data_expedicao TEXT,
                           nome_do_pai TEXT,
                           nome_da_mae TEXT,
                           estado_civil TEXT, 
                           endereco TEXT,
                           cidade TEXT,
                           uf VARCHAR(2),
                           cep CLOB,
                           telefone CLOB,
                           telefone_sec CLOB,
                           nivel_escolaridade TEXT,
                           email TEXT,
                           img TEXT
                       )
                       ''')
        self.conn.commit()
        
    def cadastrar_pessoa(self, bancoPessoas):
        self.c.execute('''INSERT INTO bancoPessoas(nome, sexo, cpf, data_nasc, rg, orgao_expedidor,
                       data_expedicao, nome_do_pai, nome_da_mae, estado_civil,
                       endereco, cidade, uf, cep, telefone, telefone_sec, 
                       nivel_escolaridade, email, img
                       
                       ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (bancoPessoas))
        messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
        self.conn.commit()
    
    def atualizar_pessoa(self, novoValor):
        query = '''UPDATE bancoPessoas SET nome=?, sexo=?, cpf=?, data_nasc=?, rg=?, orgao_expedidor=?,
                       data_expedicao=?, nome_do_pai=?, nome_da_mae=?, estado_civil=?,
                       endereco=?, cidade=?, uf=?, cep=?, telefone=?, telefone_sec=?, 
                       nivel_escolaridade=?, email=?, img=? WHERE id=?'''
        self.c.execute(query, novoValor)
        self.conn.commit()
        
        messagebox.showinfo("Sucesso", f'Cadastro atualizado com sucesso para a pessoa com ID  {novoValor[19]}!')
    
    def deletar_pessoa(self, id):
        self.c.execute("DELETE FROM bancoPessoas WHERE id=?", (id,))
        self.conn.commit()
        
        messagebox.showinfo("Sucesso", f'Pessoa com o ID {id} deletada com sucesso!')
        
    def pesquisar_pessoas(self, id):
        self.c.execute("SELECT * FROM bancoPessoas WHERE id=?", (id,))
        dados = self.c.fetchone()
        if not dados:
            messagebox.showwarning("Erro", "ID não encontrado")
        return dados
        
    def verificar_id(self, id):
        self.c.execute("SELECT * FROM bancoPessoas WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados
    
    def mostrar_pessoa_nome(self, nome):
        self.c.execute("SELECT * FROM bancoPessoas WHERE nome LIKE ?", ('%' + nome + '%',))
        dados = self.c.fetchall()
        return dados
    
    def listar_todos_registros(self):
        self.c.execute("SELECT * FROM bancoPessoas")
        dados = self.c.fetchall()
        return dados

registro = Database()
registro.create_table()