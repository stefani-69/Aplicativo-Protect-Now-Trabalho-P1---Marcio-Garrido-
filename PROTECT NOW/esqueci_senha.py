import tkinter as tk
from tkinter import messagebox

def enviar_codigo():
    messagebox.showinfo(
        "Código",
        "Código enviado para o e-mail."
    )

def salvar():

    nova = nova_senha.get()
    confirma = confirmar_senha.get()
    codigo = campo_codigo.get()

    if not nova or not confirma or not codigo:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos."
        )
        return

    if nova != confirma:
        messagebox.showerror(
            "Erro",
            "As senhas não coincidem."
        )
        return

    messagebox.showinfo(
        "Senha",
        "Senha alterada com sucesso."
    )

janela = tk.Tk()
janela.title("Esqueci Senha")
janela.geometry("500x500")

tk.Label(
    janela,
    text="E-mail"
).pack()

campo_email = tk.Entry(
    janela,
    width=40
)
campo_email.pack()

tk.Button(
    janela,
    text="Enviar Código",
    command=enviar_codigo
).pack(pady=10)

tk.Label(
    janela,
    text="Código de 6 Dígitos"
).pack()

campo_codigo = tk.Entry(
    janela,
    width=20
)
campo_codigo.pack()

tk.Label(
    janela,
    text="Nova Senha"
).pack()

nova_senha = tk.Entry(
    janela,
    width=40,
    show="*"
)
nova_senha.pack()

tk.Label(
    janela,
    text="Confirmar Senha"
).pack()

confirmar_senha = tk.Entry(
    janela,
    width=40,
    show="*"
)
confirmar_senha.pack()

tk.Button(
    janela,
    text="Salvar",
    command=salvar
).pack(pady=20)

janela.mainloop()