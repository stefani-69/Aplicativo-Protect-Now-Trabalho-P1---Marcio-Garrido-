import tkinter as tk
from tkinter import messagebox
import shutil

def salvar_backup():

    try:

        shutil.copy(
            "mensagem.txt",
            "backup_mensagem.txt"
        )

        messagebox.showinfo(
            "Backup",
            "Backup realizado."
        )

    except:

        messagebox.showerror(
            "Erro",
            "Arquivo não encontrado."
        )

def enviar():

    messagebox.showinfo(
        "Enviar",
        "Arquivo preparado para envio."
    )

janela = tk.Tk()
janela.title("Salvar e Enviar")
janela.geometry("400x250")

tk.Label(
    janela,
    text="Central de Backup",
    font=("Arial",16,"bold")
).pack(pady=20)