from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from lib.tratar_txt import cadastrar

def validar_hora(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M").time()
        return True
    
    except ValueError:
        return False

# Criação da interface
def criar_interface():
    try:
        root = tk.Tk()
        root.title("Dados para cadastro")
        root.geometry("250x300")

        label_login = tk.Label(root, text="Usuário: ")
        label_login.grid(row=0, column=0, padx=10, pady=10)
        login = tk.Entry(root)
        login.grid(row=0, column=1, padx=10, pady=10)

        label_senha = tk.Label(root, text="Senha: ")
        label_senha.grid(row=1, column=0, padx=10, pady=10)
        senha = tk.Entry(root)
        senha.grid(row=1, column=1, padx=10, pady=10)

        label_hora1 = tk.Label(root, text="Hora 1: ")
        label_hora1.grid(row=2, column=0, padx=10, pady=10)
        hora1 = tk.Entry(root)
        hora1.grid(row=2, column=1, padx=10, pady=10)

        label_hora2 = tk.Label(root, text="Hora 2: ")
        label_hora2.grid(row=3, column=0, padx=10, pady=10)
        hora2 = tk.Entry(root)
        hora2.grid(row=3, column=1, padx=10, pady=10)

        label_hora3 = tk.Label(root, text="Hora 3: ")
        label_hora3.grid(row=4, column=0, padx=10, pady=10)
        hora3 = tk.Entry(root)
        hora3.grid(row=4, column=1, padx=10, pady=10)

        label_hora4 = tk.Label(root, text="hora 4: ")
        label_hora4.grid(row=5, column=0, padx=10, pady=10)
        hora4 = tk.Entry(root)
        hora4.grid(row=5, column=1, padx=10, pady=10)

        #Função que cadastra e encerra a interface
        def cadastrar_e_encerrar_interface():
            try:
                user = login.get()
                password = senha.get()
                horas = [hora1.get(), hora2.get(), hora3.get(), hora4.get()]

                if len(set(horas)) < len(horas):
                    messagebox.showerror("ERRO", "As horas não podem ser duplicadas")
                    return
                
                for hr in horas:
                    if hr and not validar_hora(hr):
                        messagebox.showerror("ERRO", "A hora não está no formato correto de HH:MM")
                        return

                if user and password:
                    cadastrar(user, password, *horas)
                    root.destroy()
                else:
                    messagebox.showerror("ERRO", "Os campos login e senha precisam ser preenchidos.")
            
            except Exception as e:
                messagebox.showerror("ERRO", f"erro: {e}")

        enviar_button = tk.Button(root, text="Enviar", command=cadastrar_e_encerrar_interface)
        enviar_button.grid(row=6, column=1, columnspan=2, pady=20)

        root.mainloop()

    except Exception as e:
        messagebox.showerror("ERRO", f"Erro ao criar interface: {e}")