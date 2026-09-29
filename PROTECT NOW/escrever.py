import tkinter as tk
from tkinter import messagebox
import json
from arvore_crypto import ArvoreBinaria, criptografar_texto

def salvar_criptografado():
    texto = area.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showerror("Erro", "Digite uma mensagem.")
        return

    palavras = texto.split()
    arvore = ArvoreBinaria()
    
    # Insere as palavras na árvore com seus índices
    for idx, p in enumerate(palavras):
        arvore.inserir(idx, p)

    # Coleta os nós em Pré-Ordem
    lista_nos = []
    arvore.pre_ordem(arvore.raiz, lista_nos)

    # Criptografa o texto de cada nó
    for no in lista_nos:
        no["txt"] = criptografar_texto(no["txt"])

    # Salva no arquivo de pendrive (.dat)
    with open("mensagem.dat", "w", encoding="utf-8") as arquivo:
        json.dump(lista_nos, arquivo)

    messagebox.showinfo("Sucesso", "Mensagem gravada com sucesso em Árvore Binária!")

janela = tk.Tk()
janela.title("Protect Now - Escrever e Criptografar")
janela.geometry("900x600")

area = tk.Text(janela, font=("Arial", 12))
area.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(janela, text="Gerar Árvore e Criptografar", bg="#1677FF", fg="white", font=("Arial", 11, "bold"), command=salvar_criptografado).pack(pady=10)

janela.mainloop()