import os

from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from db import *
from verificar_login import *

#Definindo cores
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#e5e5e5"
co3 = "#403d3d"
co4 = "#0f0147"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_IMAGEM_PADRAO = os.path.join(BASE_DIR, "assets", "pessoa.png")
    
def telaLogin():
    tela_login = Toplevel(root)
    tela_login.title("cad.me - Login")
    tela_login.geometry("800x600")
    tela_login.configure(background=co1)
    tela_login.resizable(width=FALSE, height=FALSE)
    
    style = Style(tela_login)
    style.theme_use("clam")
    
    frame_login = Frame(tela_login, width=400, height=200, bg=co1)
    frame_login.place(x=200, y=200)

    l_usuario = Label(frame_login, text="Usuário *", anchor=NW, font="Ivy 10", bg=co1, fg=co3)
    l_usuario.place(x=100, y=20)
    e_usuario = Entry(frame_login, width=25, justify='left', relief='solid')
    e_usuario.place(x=100, y=50)
    
    l_senha = Label(frame_login, text="Senha *", anchor=NW, font="Ivy 10", bg=co1, fg=co3)
    l_senha.place(x=100, y=80)
    e_senha = Entry(frame_login, width=25, justify='left', relief='solid', show='*')
    e_senha.place(x=100, y=110)

    def realizarLogin():
        usuario = e_usuario.get()
        senha = e_senha.get()
        
        if sistema.verificarLogin(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!", parent=tela_login)
            tela_login.destroy()
            abrirSistema()
        else:
            messagebox.showwarning("Erro", "Usuário ou senha incorretos.", parent=tela_login)
    
    botao_login = Button(frame_login, command=realizarLogin, text="Entrar", width=9, anchor=CENTER, overrelief=RIDGE, font="Ivy 10 bold", bg=co2, fg=co0)
    botao_login.place(x=150, y=150)
 

def listar_todos():
    tela_pesquisa = Toplevel(root)
    tela_pesquisa.title("cad.me - Lista Completa de Registros")
    tela_pesquisa.geometry("1366x768")
    tela_pesquisa.configure(background=co2)
    tela_pesquisa.resizable(height=FALSE, width=FALSE)

    frame_pessoa = Frame(tela_pesquisa, background=co4)
    frame_pessoa.place(x=0, y=200, width=1366, height=500)

    # Cabeçalho
    cabecalho_lista = ['id', 'nome', 'sexo', 'cpf', 'data_nasc', 'rg', 'orgao_expedidor',
                       'data_expedicao', 'nome_do_pai', 'nome_da_mae', 'estado_civil',
                       'endereco', 'cidade', 'uf', 'cep', 'telefone', 'telefone_sec',
                       'nivel_escolaridade', 'email']

    df_list = registro.listar_todos_registros()
    
    tree_pessoa = ttk.Treeview(frame_pessoa, selectmode="extended", columns=cabecalho_lista, show="headings")
    
    vsb = ttk.Scrollbar(frame_pessoa, orient="vertical", command=tree_pessoa.yview)
    hsb = ttk.Scrollbar(frame_pessoa, orient="horizontal", command=tree_pessoa.xview)

    tree_pessoa.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posição correta
    tree_pessoa.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    # Expansibilidade
    frame_pessoa.grid_rowconfigure(0, weight=1)
    frame_pessoa.grid_columnconfigure(0, weight=1)

    # Ajuste de largura
    hd = ["nw", "nw", "center","center","center","center","center","center","center","center","center","center","center","center","center", "center", "center", "center", "center", "nw"]
    h=[40,250,80,100,100,100,80,100,250,250,100,130,160,40,250,250,250,250,250,250]

    for i, col in enumerate(cabecalho_lista):
        tree_pessoa.heading(col, text=col.title(), anchor=NW)
        tree_pessoa.column(col, width=h[i], anchor=hd[i])
        
    for item in df_list:
        tree_pessoa.insert('', 'end', values=item)
    
    
def pesquisar_pessoas():
    tela_pesquisa = Toplevel(root)
    tela_pesquisa.title("cad.me - Pesquisar")
    tela_pesquisa.geometry("1366x768")
    tela_pesquisa.configure(background=co2)
    tela_pesquisa.resizable(height=FALSE, width=FALSE)

    frame_tabela = Frame(tela_pesquisa, background=co4)
    frame_tabela.place(x=0, y=200, width=1366, height=500)

    # Cabeçalhos
    cabecalho_lista = ['id', 'nome', 'sexo', 'cpf', 'data_nasc', 'rg', 'orgao_expedidor',
                       'data_expedicao', 'nome_do_pai', 'nome_da_mae', 'estado_civil',
                       'endereco', 'cidade', 'uf', 'cep', 'telefone', 'telefone_sec',
                       'nivel_escolaridade', 'email']

    tree_pessoa = ttk.Treeview(frame_tabela, selectmode="extended", columns=cabecalho_lista, show="headings")
    
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_pessoa.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_pessoa.xview)

    tree_pessoa.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posição correta
    tree_pessoa.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    # Expansibilidade
    frame_tabela.grid_rowconfigure(0, weight=1)
    frame_tabela.grid_columnconfigure(0, weight=1)

    # Ajuste de largura
    hd = ["nw", "nw", "center","center","center","center","center","center","center","center","center","center","center","center","center", "center", "center", "center", "center", "nw"]
    h=[40,250,80,100,100,100,80,100,250,250,100,130,160,40,250,250,250,250,250,250]

    for i, col in enumerate(cabecalho_lista):
        tree_pessoa.heading(col, text=col.title(), anchor=NW)
        tree_pessoa.column(col, width=h[i], anchor=hd[i])

    #Entrada e botão de pesquisa    
    frame_pesquisa = Frame(tela_pesquisa, width=550, height=130, background=co2)
    frame_pesquisa.place(x=10, y=30)
    
    l_pesquisa = Label(frame_pesquisa, text="Digite o nome *", anchor=NW, font="Arial 11", background=co2)
    l_pesquisa.place(x=0, y=0)
    
    e_pesquisa = Entry(frame_pesquisa, width=25)
    e_pesquisa.place(x=0, y=30)

    def tabela():
        for item in tree_pessoa.get_children():
            tree_pessoa.delete(item)
            
        nome_pessoa = e_pesquisa.get().strip()
        
        if nome_pessoa == "":
            messagebox.showwarning("Erro", "Digite um nome antes de pesquisar", parent=tela_pesquisa)
            return
        df_list = registro.mostrar_pessoa_nome(nome_pessoa)
        
        for item in df_list:
            tree_pessoa.insert('', 'end', values=item)
            
        if not registro.mostrar_pessoa_nome(nome_pessoa):
            messagebox.showwarning("Erro", "Nenhum registro encontrado", parent=tela_pesquisa)
            return

    botao_pesquisar = Button(frame_pesquisa, command=tabela, width=10, text="Pesquisar", font="Arial 8 bold")
    botao_pesquisar.place(x=210, y=28)

    botao_listar_todos = Button(frame_pesquisa, command=listar_todos, width=15, text="Listar Todos", font="Arial 10 bold")
    botao_listar_todos.place(x=310, y=26)

def abrirSistema():
    global imagem, imagem_string, l_imagem

    root.deiconify()
    root.title("cad.me - Sistema de Cadastro de Pessoas")
    root.geometry("1366x760")
    root.configure(background=co2)
    root.resizable(width=FALSE, height=FALSE)
    
    style = Style(root)
    style.theme_use("clam")
    
    def pesquisar():
        global imagem, imagem_string, l_imagem
        
        imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)
            
        l_imagem = Label(framePessoa, image=imagem, bg=co1)
        l_imagem.image = imagem
        l_imagem.place(x=0, y=0)
        
        id_pessoa = e_pesquisar.get()
        
        if(id_pessoa == ""):
            e_nome.delete(0, END)
            e_sexo.delete(0, END)
            e_cpf.delete(0, END)
            e_datanasc.delete(0, END)
            e_rg.delete(0, END)
            e_orgao.delete(0, END)
            e_dataexp.delete(0, END)
            e_nomePai.delete(0, END)
            e_nomeMae.delete(0, END)
            e_estadoCivil.delete(0, END)
            e_endereco.delete(0, END)
            e_cidade.delete(0, END)
            e_uf.delete(0, END)
            e_cep.delete(0, END)
            e_telefone.delete(0, END)
            e_telsec.delete(0, END)
            e_escolaridade.delete(0, END)
            e_email.delete(0, END)
            messagebox.showwarning("Erro", "ID não pode estar vazio")
            return
        
        e_nome.delete(0, END)
        e_sexo.delete(0, END)
        e_cpf.delete(0, END)
        e_datanasc.delete(0, END)
        e_rg.delete(0, END)
        e_orgao.delete(0, END)
        e_dataexp.delete(0, END)
        e_nomePai.delete(0, END)
        e_nomeMae.delete(0, END)
        e_estadoCivil.delete(0, END)
        e_endereco.delete(0, END)
        e_cidade.delete(0, END)
        e_uf.delete(0, END)
        e_cep.delete(0, END)
        e_telefone.delete(0, END)
        e_telsec.delete(0, END)
        e_escolaridade.delete(0, END)
        e_email.delete(0, END)  

        dados = registro.pesquisar_pessoas(id_pessoa)

        e_nome.insert(END, dados[1])
        e_sexo.insert(END, dados[2])
        e_cpf.insert(END, dados[3])
        e_datanasc.insert(END, dados[4])
        e_rg.insert(END, dados[5])
        e_orgao.insert(END, dados[6])
        e_dataexp.insert(END, dados[7])
        e_nomePai.insert(END, dados[8])
        e_nomeMae.insert(END, dados[9])
        e_estadoCivil.insert(END, dados[10])
        e_endereco.insert(END, dados[11])
        e_cidade.insert(END, dados[12])
        e_uf.insert(END, dados[13])
        e_cep.insert(END, dados[14])
        e_telefone.insert(END, dados[15])
        e_telsec.insert(END, dados[16])
        e_escolaridade.insert(END, dados[17])
        e_email.insert(END, dados[18])
        
        imagem_string = dados[19] if dados[19] else CAMINHO_IMAGEM_PADRAO
        
        imagem = Image.open(imagem_string)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem.configure(image=imagem)
        l_imagem.image = imagem 
    
    def atualizar():
        global imagem, imagem_string, l_imagem

        id_pessoa = e_pesquisar.get()
        
        if id_pessoa == "":
            e_nome.delete(0, END)
            e_sexo.delete(0, END)
            e_cpf.delete(0, END)
            e_datanasc.delete(0, END)
            e_rg.delete(0, END)
            e_orgao.delete(0, END)
            e_dataexp.delete(0, END)
            e_nomePai.delete(0, END)
            e_nomeMae.delete(0, END)
            e_estadoCivil.delete(0, END)
            e_endereco.delete(0, END)
            e_cidade.delete(0, END)
            e_uf.delete(0, END)
            e_cep.delete(0, END)
            e_telefone.delete(0, END)
            e_telsec.delete(0, END)
            e_escolaridade.delete(0, END)
            e_email.delete(0, END)
            e_pesquisar.delete(0, END)
        
            imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
            imagem = imagem.resize((140,140))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem.configure(image=imagem)
            l_imagem.image = imagem 
            
            messagebox.showwarning("Erro", "Digite um ID para atualizar")
            return

        registro.pesquisar_pessoas(id_pessoa)

        #Lendo valores
        nome = e_nome.get()
        sexo = e_sexo.get()
        cpf = e_cpf.get()
        data_nasc = e_datanasc.get()
        rg = e_rg.get()
        orgao_expedidor = e_orgao.get()
        data_exp = e_dataexp.get()
        nome_do_pai = e_nomePai.get()
        nome_da_mae = e_nomeMae.get()
        estadoCivil = e_estadoCivil.get()
        endereco = e_endereco.get()
        cidade = e_cidade.get()
        uf = e_uf.get()
        cep = e_cep.get()
        telefone = e_telefone.get()
        telefonesec = e_telsec.get()
        nivel_escolaridade = e_escolaridade.get()
        email = e_email.get() 
        img = imagem_string

        lista = [nome, sexo, cpf, data_nasc, rg, orgao_expedidor, data_exp, nome_do_pai,
                 nome_da_mae, estadoCivil, endereco, cidade, uf, cep, telefone, telefonesec,
                 nivel_escolaridade, email, img, id_pessoa]

        #Verifica se há valores escritos
        for i in lista:
            if i=="":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
        
        #Insere valores
        registro.atualizar_pessoa(lista)

        #Limpando campos após entrada
        e_nome.delete(0, END)
        e_sexo.delete(0, END)
        e_cpf.delete(0, END)
        e_datanasc.delete(0, END)
        e_rg.delete(0, END)
        e_orgao.delete(0, END)
        e_dataexp.delete(0, END)
        e_nomePai.delete(0, END)
        e_nomeMae.delete(0, END)
        e_estadoCivil.delete(0, END)
        e_endereco.delete(0, END)
        e_cidade.delete(0, END)
        e_uf.delete(0, END)
        e_cep.delete(0, END)
        e_telefone.delete(0, END)
        e_telsec.delete(0, END)
        e_escolaridade.delete(0, END)
        e_email.delete(0, END)
        e_pesquisar.delete(0, END)
        
        imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)

        l_imagem = Label(framePessoa, image=imagem, bg=co1, fg=co3)
        l_imagem.place(x=0, y=0)
        
    def deletar():
        global imagem, imagem_string, l_imagem

        id_pessoa = e_pesquisar.get()
                
        if id_pessoa == "":
            e_nome.delete(0, END)
            e_sexo.delete(0, END)
            e_cpf.delete(0, END)
            e_datanasc.delete(0, END)
            e_rg.delete(0, END)
            e_orgao.delete(0, END)
            e_dataexp.delete(0, END)
            e_nomePai.delete(0, END)
            e_nomeMae.delete(0, END)
            e_estadoCivil.delete(0, END)
            e_endereco.delete(0, END)
            e_cidade.delete(0, END)
            e_uf.delete(0, END)
            e_cep.delete(0, END)
            e_telefone.delete(0, END)
            e_telsec.delete(0, END)
            e_escolaridade.delete(0, END)
            e_email.delete(0, END)
            e_pesquisar.delete(0, END)
            
            imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
            imagem = imagem.resize((140,140))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem.configure(image=imagem)
            l_imagem.image = imagem 
            
            messagebox.showerror("Erro", "Digite um ID para deletar")
            return
                
        if not registro.verificar_id(id_pessoa):
            e_nome.delete(0, END)
            e_sexo.delete(0, END)
            e_cpf.delete(0, END)
            e_datanasc.delete(0, END)
            e_rg.delete(0, END)
            e_orgao.delete(0, END)
            e_dataexp.delete(0, END)
            e_nomePai.delete(0, END)
            e_nomeMae.delete(0, END)
            e_estadoCivil.delete(0, END)
            e_endereco.delete(0, END)
            e_cidade.delete(0, END)
            e_uf.delete(0, END)
            e_cep.delete(0, END)
            e_telefone.delete(0, END)
            e_telsec.delete(0, END)
            e_escolaridade.delete(0, END)
            e_email.delete(0, END)
            e_pesquisar.delete(0, END)
            
            messagebox.showwarning("Erro", "O ID não existe")
            e_pesquisar.delete(0, END)
            return
        
        imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)
            
        l_imagem = Label(framePessoa, image=imagem, bg=co1)
        l_imagem.image = imagem
        l_imagem.place(x=0, y=0)
        
        e_nome.delete(0, END)
        e_sexo.delete(0, END)
        e_cpf.delete(0, END)
        e_datanasc.delete(0, END)
        e_rg.delete(0, END)
        e_orgao.delete(0, END)
        e_dataexp.delete(0, END)
        e_nomePai.delete(0, END)
        e_nomeMae.delete(0, END)
        e_estadoCivil.delete(0, END)
        e_endereco.delete(0, END)
        e_cidade.delete(0, END)
        e_uf.delete(0, END)
        e_cep.delete(0, END)
        e_telefone.delete(0, END)
        e_telsec.delete(0, END)
        e_escolaridade.delete(0, END)
        e_email.delete(0, END)
        
        e_pesquisar.delete(0, END)
        
        registro.deletar_pessoa(id_pessoa)
        
        imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
        imagem = imagem.resize((130,130))

        imagem = ImageTk.PhotoImage(imagem)

        l_imagem = Label(framePessoa, image=imagem, bg=co1, fg=co3)
        l_imagem.image = imagem
        l_imagem.place(x=450, y=10)  
    
    framePessoa = Frame(root, width=140, height=180, bg=co2)
    framePessoa.place(x=200, y=130)
    
    imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
    imagem = imagem.resize((140,140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(framePessoa, image=imagem, bg=co1)
    l_imagem.place(x=0, y=0)
    
    frameBotoes = Frame(root, width=140, height=220, bg=co2)
    frameBotoes.place(x=200, y=400)
    
    frameDados = Frame(root, width=800, height=600, bg=co2)
    frameDados.place(x=600, y=90)
    
    l_nome = Label(frameDados, text="Nome", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frameDados, width=37, justify='left', relief='solid')
    e_nome.place(x=4, y=40)
    
    l_sexo = Label(frameDados, text="Sexo", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_sexo.place(x=4, y=70)
    e_sexo = Entry(frameDados, width=15, justify='left', relief='solid')
    e_sexo.place(x=4, y=100)
    
    l_cpf = Label(frameDados, text="CPF", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_cpf.place(x=4, y=130)
    e_cpf = Entry(frameDados, width=15, justify='left', relief='solid')
    e_cpf.place(x=4, y=160)
    
    l_datanasc = Label(frameDados, text="Data de Nascimento", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_datanasc.place(x=4, y=190)
    e_datanasc = Entry(frameDados, width=15, justify='left', relief='solid')
    e_datanasc.place(x=4, y=220)
    
    l_rg = Label(frameDados, text="Registro Geral", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_rg.place(x=4, y=250)
    e_rg = Entry(frameDados, width=15, justify='left', relief='solid')
    e_rg.place(x=4, y=280)
    
    l_orgao = Label(frameDados, text="Órgão Expedidor", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_orgao.place(x=4, y=310)
    e_orgao = Entry(frameDados, width=10, justify='left', relief='solid')
    e_orgao.place(x=4, y=340)
    
    l_dataexp = Label(frameDados, text="Data de Expedição", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_dataexp.place(x=4, y=370)
    e_dataexp = Entry(frameDados, width=15, justify='left', relief='solid')
    e_dataexp.place(x=4, y=400)
    
    l_nomePai = Label(frameDados, text="Nome do Pai", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_nomePai.place(x=4, y=430)
    e_nomePai = Entry(frameDados, width=37, justify='left', relief='solid')
    e_nomePai.place(x=4, y=460)
    
    l_nomeMae = Label(frameDados, text="Nome da Mãe", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_nomeMae.place(x=4, y=490)
    e_nomeMae = Entry(frameDados, width=37, justify='left', relief='solid')
    e_nomeMae.place(x=4, y=520)
    
    l_estadoCivil = Label(frameDados, text="Estado Civil", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_estadoCivil.place(x=400, y=10)
    e_estadoCivil = Entry(frameDados, width=15, justify='left', relief='solid')
    e_estadoCivil.place(x=400, y=40)
    
    l_endereco = Label(frameDados, text="Endereço", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_endereco.place(x=400, y=70)
    e_endereco = Entry(frameDados, width=37, justify='left', relief='solid')
    e_endereco.place(x=400, y=100)
    
    l_cidade = Label(frameDados, text="Cidade", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_cidade.place(x=400, y=130)
    e_cidade = Entry(frameDados, width=25, justify='left', relief='solid')
    e_cidade.place(x=400, y=160)
    
    l_uf = Label(frameDados, text="UF", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_uf.place(x=400, y=190)
    e_uf = Entry(frameDados, width=5, justify='left', relief='solid')
    e_uf.place(x=400, y=220)
    
    l_cep = Label(frameDados, text="CEP", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_cep.place(x=400, y=250)
    e_cep = Entry(frameDados, width=15, justify='left', relief='solid')
    e_cep.place(x=400, y=280)
    
    l_telefone = Label(frameDados, text="Telefone", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_telefone.place(x=400, y=310)
    e_telefone = Entry(frameDados, width=10, justify='left', relief='solid')
    e_telefone.place(x=400, y=340)
    
    l_telsec = Label(frameDados, text="Telefone secundário", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_telsec.place(x=400, y=370)
    e_telsec = Entry(frameDados, width=10, justify='left', relief='solid')
    e_telsec.place(x=400, y=400)
    
    l_escolaridade = Label(frameDados, text="Nível de Escolaridade", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_escolaridade.place(x=400, y=430)
    e_escolaridade = Entry(frameDados, width=30, justify='left', relief='solid')
    e_escolaridade.place(x=400, y=460)
    
    l_email = Label(frameDados, text="E-mail", anchor=NW, font="Ivy 10", bg=co2, fg=co3)
    l_email.place(x=400, y=490)
    e_email = Entry(frameDados, width=37, justify='left', relief='solid')
    e_email.place(x=400, y=520)

    frame_logo = Frame(root, width=1366, height=80, bg=co4)
    frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

    app_lg = Image.open(os.path.join(BASE_DIR, "assets", "logo.png"))
    app_lg = app_lg.resize((100,100))
    app_lg = ImageTk.PhotoImage(app_lg)
    app_logo = Label(frame_logo, image=app_lg, text="CAD.ME - Sistema de Cadastro de Pessoas", width=850, compound=LEFT, font=("Verdana 15"), bg=co4, fg=co2)
    app_logo.image = app_lg
    app_logo.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    imagem = Image.open(CAMINHO_IMAGEM_PADRAO)
    imagem = imagem.resize((140,140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(framePessoa, image=imagem, borderwidth=0, highlightthickness=0, relief='flat',bg=co1, fg=co3)
    l_imagem.image = imagem
    l_imagem.place(x=0, y=0)
    
    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = fd.askopenfilename()
        imagem_string = imagem

        imagem = Image.open(imagem)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(framePessoa, image=imagem, bg=co1, fg=co3)
        l_imagem.place(x=0, y=0)
    
    botao_carregarImagem = Button(framePessoa, command=escolher_imagem, text="Carregar foto".upper(), width=20, compound=CENTER, borderwidth=0, highlightthickness=0, relief='flat', anchor=CENTER, font="Ivy 7", bg=co1)
    botao_carregarImagem.place(x=0, y=142)
    
    app_img_deletar = Image.open(os.path.join(BASE_DIR, "assets", "delete.png"))
    app_img_deletar = app_img_deletar.resize((25,25))
    app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
    app_deletar = Button(frameBotoes, image=app_img_deletar, command=deletar, text="Deletar", width=140, compound=LEFT, anchor='w', padx=8, relief=GROOVE, overrelief=RIDGE, font="Ivy 11", bg=co2, fg=co0)
    app_deletar.image = app_img_deletar
    app_deletar.place(x=0, y=40)
    
    app_img_atualizar = Image.open(os.path.join(BASE_DIR, "assets", "update.png"))
    app_img_atualizar = app_img_atualizar.resize((25,25))
    app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
    app_atualizar = Button(frameBotoes, image=app_img_atualizar, command=atualizar, text="Atualizar", width=140, compound=LEFT, anchor='w', padx=8, relief=GROOVE, overrelief=RIDGE, font="Ivy 11", bg=co2, fg=co0)
    app_atualizar.image = app_img_atualizar
    app_atualizar.place(x=0, y=80)
    
    app_img_listar = Image.open(os.path.join(BASE_DIR, "assets", "search.webp"))
    app_img_listar = app_img_listar.resize((25,25))
    app_img_listar = ImageTk.PhotoImage(app_img_listar)
    app_listar = Button(frameBotoes, image=app_img_listar, command=pesquisar_pessoas, text="Pesquisar", width=140, compound=LEFT, anchor='w', padx=8, relief=GROOVE, overrelief=RIDGE, font="Ivy 11", bg=co2, fg=co0)
    app_listar.image = app_img_listar
    app_listar.place(x=0, y=120)
    
    frame_pesquisar = Frame(root, width=270, height=20, bg=co2, relief=RAISED)
    frame_pesquisar.place(x=200, y=340)
    
    botao_pesquisar_id = Button(frame_pesquisar, command=pesquisar, relief='flat', text="Pesquisar", width=12, anchor=CENTER, overrelief=RIDGE, font="Ivy 7 bold", bg=co1)
    botao_pesquisar_id.place(x=150, y=0)
    e_pesquisar = Entry(frame_pesquisar, width=17, highlightthickness=0, borderwidth=0, justify='center', relief='flat', font='Ivy 10')
    e_pesquisar.place(x=0, y=0)
            
    def adicionar():
        global imagem, imagem_string, l_imagem
        
        nome = e_nome.get()
        sexo = e_sexo.get()
        cpf = e_cpf.get()
        data_nasc = e_datanasc.get()
        rg = e_rg.get()
        orgao_expedidor = e_orgao.get()
        data_exp = e_dataexp.get()
        nome_do_pai = e_nomePai.get()
        nome_da_mae = e_nomeMae.get()
        estadoCivil = e_estadoCivil.get()
        endereco = e_endereco.get()
        cidade = e_cidade.get()
        uf = e_uf.get()
        cep = e_cep.get()
        telefone = e_telefone.get()
        telefonesec = e_telsec.get()
        nivel_escolaridade = e_escolaridade.get()
        email = e_email.get()
        img = imagem_string
        
        lista = [nome, sexo, cpf, data_nasc, rg, orgao_expedidor, data_exp, nome_do_pai,
                 nome_da_mae, estadoCivil, endereco, cidade, uf, cep, telefone, telefonesec,
                 nivel_escolaridade, email, img]
        
        for i in lista:
            if i=="":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
        #Inserindo valores
        registro.cadastrar_pessoa(lista)
        
        #Limpando campos após inserção
        e_nome.delete(0,END)
        e_sexo.delete(0,END)
        e_cpf.delete(0,END)
        e_datanasc.delete(0,END)
        e_rg.delete(0,END)
        e_orgao.delete(0,END)
        e_dataexp.delete(0,END)
        e_nomePai.delete(0,END)
        e_nomeMae.delete(0,END)
        e_estadoCivil.delete(0,END)
        e_endereco.delete(0,END)
        e_cidade.delete(0,END)
        e_uf.delete(0,END)
        e_cep.delete(0,END)
        e_telefone.delete(0,END)
        e_telsec.delete(0,END)
        e_escolaridade.delete(0,END)
        e_email.delete(0,END)
        
        imagem_string = CAMINHO_IMAGEM_PADRAO
        imagem = Image.open(imagem_string)
        imagem = imagem.resize((140,140))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem.configure(image=imagem)
        l_imagem.image = imagem
    
    botao_cadastrar = Button(frameDados, text="Cadastrar", command=adicionar, font="Ivy 10 bold", width=10, bg=co1)
    botao_cadastrar.place(x=250, y=570)

    def on_close(): 
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)

root = Tk()
root.withdraw()  
root.after(0, telaLogin)

root.mainloop()