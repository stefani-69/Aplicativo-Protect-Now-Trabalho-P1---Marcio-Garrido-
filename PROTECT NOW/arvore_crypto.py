import json

class No:
    def __init__(self, posicao, palavra):
        self.posicao = posicao
        self.palavra = palavra
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, posicao, palavra):
        if not self.raiz:
            self.raiz = No(posicao, palavra)
        else:
            self._inserir_recursivo(self.raiz, posicao, palavra)

    def _inserir_recursivo(self, no, posicao, palavra):
        # Insere baseado no índice da posição original
        if posicao < no.posicao:
            if no.esquerda is None:
                no.esquerda = No(posicao, palavra)
            else:
                self._inserir_recursivo(no.esquerda, posicao, palavra)
        else:
            if no.direita is None:
                no.direita = No(posicao, palavra)
            else:
                self._inserir_recursivo(no.direita, posicao, palavra)

    def pre_ordem(self, no, lista):
        if no:
            lista.append({"pos": no.posicao, "txt": no.palavra})
            self.pre_ordem(no.esquerda, lista)
            self.pre_ordem(no.direita, lista)

# Cifra de César com suporte universal
def criptografar_texto(texto, chave=3):
    resultado = ""
    for char in texto:
        resultado += chr(ord(char) + chave)
    return resultado

def descriptografar_texto(texto, chave=3):
    resultado = ""
    for char in texto:
        resultado += chr(ord(char) - chave)
    return resultado