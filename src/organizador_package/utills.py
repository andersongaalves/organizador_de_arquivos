import os

from .validar import pertence_ao_grupo, validar_diretorio

def tratar_input_texto(entrada: str) -> str:
    return entrada.strip()

def pedir_diretorio():
    return validar_diretorio(tratar_input_texto(input('Digite o endereço do diretorio: ')))

def pegar_extensao(endereco: str) -> str:
    return os.path.splitext(endereco)[1].lower()

def adicionar_a(colecao: dict, grupo_base: str, subgrupo: str, enderecos: list, condicoes: list):
    colecao[subgrupo] = [
            endereco for endereco in enderecos
            if pertence_ao_grupo(endereco, grupo_base, subgrupo, condicoes)
            ]