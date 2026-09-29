import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import hashlib
import base64

# ==========================================================
# 1. CRIPTOGRAFIA AVANÇADA (SHA-256 + XOR DINÂMICO COM IV)
# ==========================================================
CHAVE_MESTRA = "ProtectNow_Marica_Niterói_2026_SecretKey_Complex!"

def gerar_chave_derivada(sal: bytes) -> bytes:
    return hashlib.sha256(CHAVE_MESTRA.encode('utf-8') + sal).digest()

def criptografar_texto_forte(texto: str) -> str:
    if not texto:
        return ""
    
    sal = os.urandom(16)
    chave = gerar_chave_derivada(sal)
    
    texto_bytes = texto.encode('utf-8')
    cifrado_bytes = bytearray()
    
    for i, b in enumerate(texto_bytes):
        cifrado_bytes.append(b ^ chave[i % len(chave)])
    
    resultado_final = sal + bytes(cifrado_bytes)
    return base64.b64encode(resultado_final).decode('utf-8')

def descriptografar_texto_forte(texto_cifrado_b64: str) -> str:
    if not texto_cifrado_b64:
        return ""
    
    try:
        dados = base64.b64decode(texto_cifrado_b64.encode('utf-8'))
        sal = dados[:16]
        conteudo_cifrado = dados[16:]
        
        chave = gerar_chave_derivada(sal)
        
        decifrado_bytes = bytearray()
        for i, b in enumerate(conteudo_cifrado):
            decifrado_bytes.append(b ^ chave[i % len(chave)])
            
        return decifrado_bytes.decode('utf-8')
    except Exception:
        return "[Erro de Descriptografia]"

# ==========================================================
# 2. LÓGICA DA ÁRVORE BINÁRIA DE BUSCA (BST)
# ==========================================================

class No:
    def __init__(self, palavra, pos_original):
        self.palavra = palavra
        self.pos_original = pos_original
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, palavra, pos_original):
        if not self.raiz:
            self.raiz = No(palavra, pos_original)
        else:
            self._inserir_recursivo(self.raiz, palavra, pos_original)

    def _inserir_recursivo(self, no, palavra, pos_original):
        if palavra.lower() < no.palavra.lower():
            if no.esquerda is None:
                no.esquerda = No(palavra, pos_original)
            else:
                self._inserir_recursivo(no.esquerda, palavra, pos_original)
        else:
            if no.direita is None:
                no.direita = No(palavra, pos_original)
            else:
                self._inserir_recursivo(no.direita, palavra, pos_original)

    def pre_ordem(self, no, lista):
        if no:
            lista.append({"pos": no.pos_original, "txt": no.palavra})
            self.pre_ordem(no.esquerda, lista)
            self.pre_ordem(no.direita, lista)

# ==========================================================
# 3. INTERFACE GRÁFICA MULTI-TELA (TKINTER)
# ==========================================================

class AppProtectNow:
    def __init__(self, root):
        self.root = root
        self.root.title("Protect Now - Sistema de Mensageria Inquebrável")
        self.root.geometry("950x680")
        self.root.resizable(False, False)

        self.historico = []
        self.nos_criptografados_atuais = None

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.telas = {}

        try:
            self.fundo_img = tk.PhotoImage(file="FUNDO FULL.png")
        except:
            self.fundo_img = None

        for TelaClass in (TelaLogin, TelaEscrever, TelaLer, TelaCadastro):
            nome_tela = TelaClass.__name__
            frame = TelaClass(parent=self.container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("TelaLogin")

    def mostrar_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        if nome_tela == "TelaLer":
            frame.atualizar_historico_ui()
        frame.tkraise()


# ------------------------------------------
# TELA 1: LOGIN (AJUSTADA)
# ------------------------------------------
class TelaLogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#071A3D")
        self.controller = controller

        if controller.fundo_img:
            lbl_fundo = tk.Label(self, image=controller.fundo_img)
            lbl_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        painel = tk.Frame(self, bg="#071A3D", bd=2, relief="groove")
        painel.place(relx=0.5, rely=0.5, anchor="center", width=380, height=420)

        tk.Label(painel, text="PROTECT NOW", font=("Arial", 18, "bold"), bg="#071A3D", fg="white").pack(pady=(20, 15))

        tk.Label(painel, text="E-mail", font=("Arial", 11, "bold"), bg="#071A3D", fg="white").pack(anchor="w", padx=30)
        self.email_entry = tk.Entry(painel, font=("Arial", 11), width=28)
        self.email_entry.pack(pady=(2, 12), ipady=3)

        tk.Label(painel, text="Senha", font=("Arial", 11, "bold"), bg="#071A3D", fg="white").pack(anchor="w", padx=30)
        self.senha_entry = tk.Entry(painel, font=("Arial", 11), width=28, show="*")
        self.senha_entry.pack(pady=(2, 20), ipady=3)

        tk.Button(painel, text="Entrar", bg="#1677FF", fg="white", font=("Arial", 11, "bold"), width=20,
                  cursor="hand2", command=lambda: controller.mostrar_tela("TelaEscrever")).pack(pady=6, ipady=3)

        tk.Button(painel, text="Criar Conta", bg="#003A8C", fg="white", font=("Arial", 11, "bold"), width=20,
                  cursor="hand2", command=lambda: controller.mostrar_tela("TelaCadastro")).pack(pady=6, ipady=3)


# ------------------------------------------
# TELA 2: ESCREVER & EXPORTAR ARQUIVO JSON
# ------------------------------------------
class TelaEscrever(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F0F2F5")
        self.controller = controller

        bar = tk.Frame(self, bg="#071A3D", height=45)
        bar.pack(fill="x")
        
        tk.Button(bar, text="Escrever/Enviar", bg="#1677FF", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10, pady=6)
        tk.Button(bar, text="Ler/Receber", bg="#003A8C", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.mostrar_tela("TelaLer")).pack(side="left", padx=5, pady=6)
        
        tk.Button(bar, text="🔑 Voltar ao Login", bg="#FF4D4F", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.mostrar_tela("TelaLogin")).pack(side="right", padx=10, pady=6)

        tk.Label(self, text="Painel de Envio (Maricá -> Niterói)", font=("Arial", 16, "bold"), bg="#F0F2F5", fg="#071A3D").pack(pady=10)

        tk.Label(self, text="Digite a mensagem curta:", font=("Arial", 11, "bold"), bg="#F0F2F5").pack(anchor="w", padx=25)
        self.txt_mensagem = tk.Text(self, font=("Arial", 11), height=4)
        self.txt_mensagem.pack(fill="x", padx=25, pady=5)

        btn_frame = tk.Frame(self, bg="#F0F2F5")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="1. Gerar Árvore e Criptografar", bg="#1677FF", fg="white", font=("Arial", 11, "bold"),
                  command=self.processar_e_criptografar).pack(side="left", padx=8)

        tk.Button(btn_frame, text="2. Exportar / Baixar Arquivo (.json)", bg="#FA8C16", fg="white", font=("Arial", 11, "bold"),
                  command=self.exportar_json).pack(side="left", padx=8)

        tk.Label(self, text="Visualização dos Nós Criptografados (Pré-Ordem Base64):", font=("Arial", 11, "bold"), bg="#F0F2F5").pack(anchor="w", padx=25)
        self.txt_resultado = tk.Text(self, font=("Arial", 10), height=5, bg="#E6F7FF")
        self.txt_resultado.pack(fill="x", padx=25, pady=5)

    def processar_e_criptografar(self):
        msg = self.txt_mensagem.get("1.0", tk.END).strip()
        if not msg:
            messagebox.showerror("Erro", "Digite uma mensagem primeiro.")
            return

        palavras = msg.split()
        arvore = ArvoreBinaria()
        for idx, palavra in enumerate(palavras):
            arvore.inserir(palavra, idx)

        lista_nos = []
        arvore.pre_ordem(arvore.raiz, lista_nos)

        for no in lista_nos:
            no["txt"] = criptografar_texto_forte(no["txt"])

        self.controller.nos_criptografados_atuais = lista_nos

        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(tk.END, f"{lista_nos}")

        messagebox.showinfo("Sucesso", "Árvore gerada e criptografada com sucesso!")

    def exportar_json(self):
        if not self.controller.nos_criptografados_atuais:
            messagebox.showerror("Erro", "Gere e criptografe uma mensagem antes de exportar.")
            return

        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivos JSON", "*.json"), ("Todos os Arquivos", "*.*")],
            title="Salvar Mensagem Criptografada"
        )

        if caminho_arquivo:
            with open(caminho_arquivo, "w", encoding="utf-8") as file:
                json.dump(self.controller.nos_criptografados_atuais, file, ensure_ascii=False, indent=4)

            messagebox.showinfo("Download Concluído", f"Arquivo exportado com sucesso em:\n{caminho_arquivo}")
            self.txt_mensagem.delete("1.0", tk.END)


# ------------------------------------------
# TELA 3: UPAR E DESCRIPTOGRAFAR ARQUIVO JSON
# ------------------------------------------
class TelaLer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F0F2F5")
        self.controller = controller

        bar = tk.Frame(self, bg="#071A3D", height=45)
        bar.pack(fill="x")
        
        tk.Button(bar, text="Escrever/Enviar", bg="#003A8C", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.mostrar_tela("TelaEscrever")).pack(side="left", padx=10, pady=6)
        tk.Button(bar, text="Ler/Receber", bg="#1677FF", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5, pady=6)
        
        tk.Button(bar, text="🔑 Voltar ao Login", bg="#FF4D4F", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.mostrar_tela("TelaLogin")).pack(side="right", padx=10, pady=6)

        tk.Label(self, text="Painel de Recebimento / Leitura", font=("Arial", 16, "bold"), bg="#F0F2F5", fg="#071A3D").pack(pady=10)

        tk.Button(self, text="📁 Upar/Carregar Arquivo (.json)", bg="#52C41A", fg="white", font=("Arial", 11, "bold"),
                  command=self.upar_e_descriptografar).pack(pady=5)

        painel_duplo = tk.Frame(self, bg="#F0F2F5")
        painel_duplo.pack(fill="both", padx=20, pady=5, expand=True)

        f_esquerda = tk.Frame(painel_duplo, bg="#F0F2F5")
        f_esquerda.pack(side="left", fill="both", expand=True, padx=5)
        tk.Label(f_esquerda, text="Última Mensagem Carregada:", font=("Arial", 11, "bold"), bg="#F0F2F5").pack(anchor="w")
        self.txt_leitura = tk.Text(f_esquerda, font=("Arial", 10), height=10)
        self.txt_leitura.pack(fill="both", expand=True, pady=5)

        f_direita = tk.Frame(painel_duplo, bg="#F0F2F5")
        f_direita.pack(side="right", fill="both", expand=True, padx=5)
        tk.Label(f_direita, text="📜 Histórico de Mensagens:", font=("Arial", 11, "bold"), bg="#F0F2F5").pack(anchor="w")
        self.txt_historico = tk.Text(f_direita, font=("Arial", 10), height=10, bg="#FAFAFA")
        self.txt_historico.pack(fill="both", expand=True, pady=5)

    def upar_e_descriptografar(self):
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos JSON", "*.json"), ("Todos os Arquivos", "*.*")],
            title="Selecionar Arquivo JSON de Mensagem"
        )

        if not caminho_arquivo:
            return

        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as file:
                lista_cripto = json.load(file)

            nos_descriptografados = []
            for item in lista_cripto:
                texto_limpo = descriptografar_texto_forte(item["txt"])
                nos_descriptografados.append((item["pos"], texto_limpo))

            nos_descriptografados.sort(key=lambda x: x[0])
            mensagem_final = " ".join([no[1] for no in nos_descriptografados])

            nome_arquivo = os.path.basename(caminho_arquivo)

            self.txt_leitura.delete("1.0", tk.END)
            self.txt_leitura.insert(tk.END, f"=== ARQUIVO LIDO ({nome_arquivo}) ===\n\n")
            self.txt_leitura.insert(tk.END, f"Estrutura Criptografada Avançada (Pré-Ordem Base64):\n{lista_cripto}\n\n")
            self.txt_leitura.insert(tk.END, "--------------------------------------------------\n")
            self.txt_leitura.insert(tk.END, f"MENSAGEM FINAL DESCRIPTOGRAFADA:\n\"{mensagem_final}\"\n")

            if mensagem_final:
                if not self.controller.historico or self.controller.historico[-1] != mensagem_final:
                    self.controller.historico.append(mensagem_final)
                    self.atualizar_historico_ui()

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível descriptografar o arquivo:\n{e}")

    def atualizar_historico_ui(self):
        self.txt_historico.delete("1.0", tk.END)
        if not self.controller.historico:
            self.txt_historico.insert(tk.END, "Nenhuma mensagem gravada no histórico.")
        else:
            for idx, msg in enumerate(self.controller.historico, 1):
                self.txt_historico.insert(tk.END, f"[{idx}] {msg}\n---\n")


# ------------------------------------------
# TELA 4: CADASTRO DE USUÁRIO
# ------------------------------------------
class TelaCadastro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#071A3D")
        self.controller = controller

        painel = tk.Frame(self, bg="#071A3D")
        painel.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(painel, text="CRIAR CONTA", font=("Arial", 18, "bold"), bg="#071A3D", fg="white").pack(pady=10)

        tk.Label(painel, text="E-mail", font=("Arial", 11, "bold"), bg="#071A3D", fg="white").pack()
        tk.Entry(painel, font=("Arial", 11), width=28).pack(pady=5, ipady=3)

        tk.Label(painel, text="Senha", font=("Arial", 11, "bold"), bg="#071A3D", fg="white").pack()
        tk.Entry(painel, font=("Arial", 11), width=28, show="*").pack(pady=5, ipady=3)

        tk.Button(painel, text="Cadastrar", bg="#1677FF", fg="white", font=("Arial", 11, "bold"),
                  command=lambda: [messagebox.showinfo("Sucesso", "Conta criada!"), controller.mostrar_tela("TelaLogin")]).pack(pady=10, ipady=2)
        tk.Button(painel, text="Voltar ao Login", bg="#FF4D4F", fg="white", font=("Arial", 11, "bold"),
                  command=lambda: controller.mostrar_tela("TelaLogin")).pack(ipady=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = AppProtectNow(root)
    root.mainloop()