import os
from tkinter import messagebox
from dotenv import load_dotenv

# Verifica se existe um caminho especificado
def criar_arquivo(arq):
    if not os.path.exists(arq):
        try:
            file = open(arq, 'w')
            file.close()
        except Exception as e:
            messagebox.showerror("ERRO", f"Não foi possível criar o arquivo .env: {e}")

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
            arquivo.write(f"login='{user}'\n")
            arquivo.write(f"senha='{password}'\n")
            arquivo.write(f"hora1='{hr1}'\n")
            arquivo.write(f"hora2='{hr2}'\n")
            arquivo.write(f"hora3='{hr3}'\n")
            arquivo.write(f"hora4='{hr4}'\n")
    
    except FileNotFoundError:
        messagebox.showerror("ERRO", "O arquivo não existe ou não foi encontrado")
    except:
        messagebox.showerror("ERRO", "Erro ao inserir as informações")

# Função que lê um arquivo txt
def retorna_env():
    load_dotenv()
    try:
        login = [os.environ['login'], os.environ['senha']]
        lista_horas = [os.environ['hora1'], os.environ['hora2'], os.environ['hora3'], os.environ['hora4']]
        return login, lista_horas
    except:
        messagebox.showerror("ERRO", "Erro na leitura do arquivo.")

# Busca o caminho do arquivo e retorna o path completo  
def buscar_file_path():
    try:
        users = os.path.expanduser("~")
        name = ".env"
        file_path = os.path.normpath(os.path.join(users, "Documents", "Automação Ponto", name))
        return file_path
    except Exception as e:
        messagebox.showerror("ERRO", "Não foi possível adquirir o caminho para o arquivo")
        return
