import os

from collections.abc import Iterable

from .validar import atende_as_condicoes, validar_diretorio, validar_tipo

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
    validar_tipo('entrada', entrada, str)

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
    validar_tipo('endereco', endereco, str)

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
    validar_tipo('colecao', colecao, dict)
    validar_tipo('enderecos', enderecos, Iterable)
    validar_tipo('grupo_base', grupo_base, str)
    validar_tipo('subgrupo', subgrupo, str)
    validar_tipo('condicoes', condicoes, Iterable)
    
    colecao[subgrupo] = [
            endereco for endereco in enderecos
            if atende_as_condicoes(endereco, grupo_base, subgrupo, condicoes)
            ]