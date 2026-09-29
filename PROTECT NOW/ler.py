import tkinter as tk
import json
from arvore_crypto import descriptografar_texto

janela = tk.Tk()
janela.title("Protect Now - Ler e Descriptografar")
janela.geometry("900x600")

area = tk.Text(janela, font=("Arial", 12))
area.pack(fill="both", expand=True, padx=10, pady=10)

try:
    # 1. Lê os dados do arquivo
    with open("mensagem.dat", "r", encoding="utf-8") as arquivo:
        lista_cripto = json.load(arquivo)

    # 2. Descriptografa o texto de cada nó mantendo a posição
    nos_descriptografados = []
    for no in lista_cripto:
        texto_limpo = descriptografar_texto(no["txt"])
        nos_descriptografados.append((no["pos"], texto_limpo))

    # 3. Reorganiza na ordem sequencial original da frase
    nos_descriptografados.sort(key=lambda x: x[0])
    mensagem_final = " ".join([item[1] for item in nos_descriptografados])

    area.insert(tk.END, "--- DADOS DA MENSAGEM RECEBIDA ---\n\n")
    area.insert(tk.END, f"Texto Criptografado Lido (Pré-Ordem): {lista_cripto}\n\n")
    area.insert(tk.END, f"--------------------------------------------------\n")
    area.insert(tk.END, f"MENSAGEM DESCRIPTOGRAFADA CORRETA:\n")
    area.insert(tk.END, f"\"{mensagem_final}\"")

except Exception as e:
    area.insert(tk.END, f"Erro ao ler mensagem: {e}")

janela.mainloop()