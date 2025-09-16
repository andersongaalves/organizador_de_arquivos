import os

from collections.abc import Iterable

from .validar import atende_as_condicoes, validar_diretorio

def tratar_texto(entrada: str) -> str:
    """
    Formata um texto removendo os espaços desnecessários.
    
    Returns:
        str: Texto formatado.
    
    Raises:
        TypeError: Se 'entrada' não for str.
        ValueError: Se 'entrada' estiver vazia.
    """

    #Type check
    if not isinstance(entrada, str):
        raise TypeError(f"entrada deve ser str. Você passou {type(entrada).__name__}")
    #Value check
    if not entrada:
        raise ValueError(f"entrada não pode estar vazia")

    return entrada.strip()

def pedir_diretorio():
    """
    Pede o endereço do diretorio e imprime um input.
    
    Returns:
        str: Texto com endereço do diretorio.
    """
    return validar_diretorio(tratar_texto(input('Digite o endereço do diretorio: ')))

def pegar_extensao(endereco: str) -> str:
    """
    Separa a extensão do arquivo do restante do endereço.

    Args:
        endereco: Endereço do arquivo.

    Returns:
        str: Extensão do arquivo separada.

    Raises:
        TypeError: Se 'endereco' não for str.
        ValueError: Se 'endereco' estiver vazio.
        FileNotFoundError: Se o endereço passado não apontar pra um arquivo.
        
    """

    #Type check
    if not isinstance(endereco, str):
        raise TypeError(f"endereco deve ser str. Você passou {type(endereco).__name__}")
    #Value check
    if not endereco:
        raise ValueError(f"endereco não pode estar vazio")
    #File check
    if not os.path.isfile(endereco):
        raise FileNotFoundError(f"endereco deve apontar para um arquivo.")

    return os.path.splitext(endereco)[1].lower()

def adicionar_a(colecao: dict, grupo_base: str, subgrupo: str, enderecos: Iterable, condicoes: Iterable):
    """
    Adiciona o arquivo a um dicionario caso ele atenda as condições estabelecidas.

    Args:
        colecao (dict): Coleção onde o item será adicionado.
        grupo_base (str): Primeira pasta em relação ao diretorio principal.
        subgrupo (str): Nome da subpasta.
        condicoes (Iterable): Condições de pertencimento.
    
    Raises:
        TypeError: Se 'endereco,' 'grupo_base' ou 'subgrupo' não forem str. Se 'condicoes' não for Iterable.
    """

    #Type check
    if not isinstance(enderecos, Iterable):
        raise TypeError(f"enderecos deve ser Iterable. Você passou {type(enderecos).__name__}")
    if not isinstance(grupo_base, str):
        raise TypeError(f"grupo_base deve ser str. Você passou {type(grupo_base).__name__}")
    if not isinstance(subgrupo, str):
        raise TypeError(f"subgrupo deve ser str. Você passou {type(subgrupo).__name__}")
    if not isinstance(condicoes, Iterable):
        raise TypeError(f"condicoes deve ser Iterable. Você passou {type(condicoes).__name__}")
    
    colecao[subgrupo] = [
            endereco for endereco in enderecos
            if atende_as_condicoes(endereco, grupo_base, subgrupo, condicoes)
            ]