import tkinter as tk
from tkinter import messagebox

def enviar_codigo():
    messagebox.showinfo(
        "Código",
        "Código de 6 dígitos enviado para o e-mail."
    )

def criar_conta():

    email = campo_email.get()
    senha = campo_senha.get()
    repetir = campo_repetir.get()
    codigo = campo_codigo.get()

    if not email or not senha or not repetir or not codigo:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos."
        )
        return

    if senha != repetir:
        messagebox.showerror(
            "Erro",
            "As senhas não coincidem."
        )
        return

    messagebox.showinfo(
        "Sucesso",
        "Conta criada com sucesso."
    )

janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("500x500")

tk.Label(janela,text="E-mail").pack()
campo_email = tk.Entry(janela,width=40)
campo_email.pack()

tk.Label(janela,text="Senha").pack()
campo_senha = tk.Entry(janela,width=40,show="*")
campo_senha.pack()

tk.Label(janela,text="Repetir Senha").pack()
campo_repetir = tk.Entry(janela,width=40,show="*")
campo_repetir.pack()

tk.Button(
    janela,
    text="Enviar Código",
    command=enviar_codigo
).pack(pady=10)

tk.Label(janela,text="Código de 6 Dígitos").pack()
campo_codigo = tk.Entry(janela,width=20)
campo_codigo.pack()

tk.Button(
    janela,
    text="Criar Conta",
    command=criar_conta
).pack(pady=20)

janela.mainloop()