import os
from tkinter import messagebox

# Verifica se existe um caminho especificado
def arquivo_existe(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open(arq, 'wt+')
        arquivo.close()

# Verifica se o txt tem alguma informação lá dentro
def arquivo_vazio(arquivo):
    try:
        return os.stat(arquivo).st_size == 0
    except FileNotFoundError:
        messagebox.showerror("ERRO", "O arquivo não existe ou não foi encontrado")

# Função que abre e cadastra dados em um txt
def cadastrar(user, password, hr1=None, hr2=None, hr3=None, hr4=None):
    arq = buscar_file_path()
    try:
        with open(arq, 'at') as arquivo:
            arquivo.write(f"{user};{password}\n")
            arquivo.write(f"{hr1};{hr2};{hr3};{hr4}")
    
    except FileNotFoundError:
        messagebox.showerror("ERRO", "O arquivo não existe ou não foi encontrado")
    except:
        messagebox.showerror("ERRO", "Erro ao inserir as informações")

# Função que lê um arquivo txt
def ler_arquivo(arq):
    try:
        dados = []
        with open(arq, 'rt') as arquivo:
            for linha in arquivo:
                dados += linha.split(";")
        login = dados[0:2]
        lista_horas = dados[2:]
        return login, lista_horas
    
    except FileNotFoundError:
        messagebox.showerror("ERRO", "O arquivo não existe ou não foi encontrado")
    except:
        messagebox.showerror("ERRO", "Erro na leitura do arquivo.")

# Busca o caminho do arquivo e retorna o path completo  
def buscar_file_path():
    try:
        users = os.path.expanduser("~")
        name = "Dados.txt"
        file_path = os.path.normpath(os.path.join(users, "Documents", "Automação Ponto", name))
        return file_path
    except Exception as e:
        messagebox.showerror("ERRO", "Não foi possível adquirir o caminho para o arquivo")
        return