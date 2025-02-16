import tkinter as tk
from tkinter import messagebox

# Função para verificar as credenciais
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Simulação de credenciais
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo ao sistema!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

# Criando a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Tamanho da janela
root.geometry("300x200")

# Rótulos (Labels)
label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack(pady=5)

# Entrada de texto para o usuário
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

# Rótulo (Label) para senha
label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)

# Entrada de texto para a senha
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

# Botão de login
botao_login = tk.Button(root, text="Entrar", command=verificar_login)
botao_login.pack(pady=10)

# Iniciar a interface
root.mainloop()
