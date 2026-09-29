import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

print("Arquivo iniciou")

def fazer_login():
    email = campo_email.get()
    senha = campo_senha.get()

    if email == "" or senha == "":
        messagebox.showerror(
            "Erro",
            "Preencha e-mail e senha."
        )
        return

    messagebox.showinfo(
        "Login",
        f"Bem-vindo {email}"
    )

def abrir_cadastro():
    subprocess.Popen([sys.executable, "cadastro.py"])

def esqueci_senha():
    subprocess.Popen([sys.executable, "esqueci_senha.py"])

janela = tk.Tk()

janela.title("Protect Now")
janela.geometry("1600x1600")
janela.resizable(False, False)

fundo = tk.PhotoImage(file="FUNDO FULL.png")

label_fundo = tk.Label(
    janela,
    image=fundo
)

label_fundo.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

logo = tk.PhotoImage(file="LOGO ESTILIZADO3.png")

logo = logo.subsample(3, 3)

titulo = tk.Label(
    janela,
    image=logo
)
titulo.pack(pady=10)

# Painel dos campos e botões
painel = tk.Frame(
    janela,
    bg="#071A3D"
)

painel.pack(
    pady=10,
    padx=20
)

label_email = tk.Label(
    painel,
    text="E-mail",
    font=("Arial", 11, "bold"),
    bg="#071A3D",
    fg="white"
)

label_email.pack(pady=(10, 3))

campo_email = tk.Entry(
    painel,
    width=32,
    font=("Arial", 11),
    bg="white",
    fg="#071A3D",
    relief="flat"
)

campo_email.pack(pady=(0, 10), ipady=5)

label_senha = tk.Label(
    painel,
    text="Senha",
    font=("Arial", 11, "bold"),
    bg="#071A3D",
    fg="white"
)

label_senha.pack(pady=(5, 3))

campo_senha = tk.Entry(
    painel,
    width=32,
    font=("Arial", 11),
    bg="white",
    fg="#071A3D",
    show="*",
    relief="flat"
)

campo_senha.pack(pady=(0, 15), ipady=5)

botao_login = tk.Button(
    painel,
    text="Entrar",
    width=25,
    font=("Arial", 10, "bold"),
    bg="#1677FF",
    fg="white",
    activebackground="#0D5FCC",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=fazer_login
)

botao_login.pack(pady=5, ipady=3)

botao_cadastro = tk.Button(
    painel,
    text="Criar Conta",
    width=25,
    font=("Arial", 10, "bold"),
    bg="#1677FF",
    fg="white",
    activebackground="#0D5FCC",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_cadastro
)

botao_cadastro.pack(
    pady=5,
    ipady=3
)

botao_esqueci = tk.Button(
    painel,
    text="Esqueci Minha Senha",
    width=25,
    font=("Arial", 10, "bold"),
    bg="#1677FF",
    fg="white",
    activebackground="#0D5FCC",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=esqueci_senha
)

botao_esqueci.pack(
    pady=(5, 15),
    ipady=3
)


print("Tela criada")

janela.mainloop()

print("Arquivo terminou")