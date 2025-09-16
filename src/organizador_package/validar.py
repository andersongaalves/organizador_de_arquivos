from os.path import basename, exists

from collections.abc import Iterable
from typing import Any

def validar_tipo(
    nome_var: str, 
    valor_var: Any, 
    tipo_esperado: type | tuple[type,...]
    ) -> None:

    """
    Verifica se uma variável é do tipo esperado. 
    Se não for, lança TypeError.

    Args:
        nome_var (str): Nome da variável verificada.
        valor_var (Any): Valor da variável.
        tipo_esperado (type | tuple[type, ...]): Tipo ou tupla de tipos esperados.

    Raises:
        TypeError: Se 'nome_var' não for str.
        TypeError: Se 'valor_var' não for do(s) tipo(s) esperado(s).
    """

    if not isinstance(nome_var, str):
        raise TypeError(f"nome_var deve ser str. Você passou {type(nome_var).__name__}")


    if not isinstance(valor_var, tipo_esperado):
        esperado = (
            tipo_esperado.__name__
            if isinstance(tipo_esperado, type)
            else ', '.join(t.__name__ for t in tipo_esperado)
        )
        raise TypeError(
            f"{nome_var} deve receber {esperado}. "
            f"Você passou {type(valor_var).__name__}"
        )
    
def validar_diretorio(diretorio: str) -> bool | str:
    """
    Verifica se o diretório existe. Retorna True se existir caso contrário, lança FileNotFoundError.

    Args:
        diretorio (str): O diretório a ser verificado.
    
    Returns:
        bool: Retorna o valor de diretorio se existir, False caso contrário.

    Raises:
        TypeError: Se 'diretorio' não for str.
        FileNotFoundError: Se o diretório não existir.
    
    Examples:  
        >>> validar_diretorio('C:/Users/Usuario/Documents')
        'C:/Users/Usuario/Documents'

        >>> validar_diretorio('C:/Caminho/Inexistente')
        Traceback (most recent call last):
            ...
        FileNotFoundError: O diretório C:/Caminho/Inexistente não existe.
    """

    #Type check
    validar_tipo('diretorio', diretorio, str)

    #Verificando se o diretório existe
    if not exists(diretorio):
        raise FileNotFoundError(f'O diretório {diretorio} não existe.')

    return diretorio

def verificar_condicao(endereco: str, subgrupo: str, condicoes: Iterable) -> bool:
    """
    Verifica se o arquivo preenche as condições.

    Args:
        endereco (str): Endereço do arquivo.
        subgrupo (str): Nome da pasta a qual o pertencimento será verificado.
        condicoes (Iterable): Condições de pertencimento.

    Raises:
        TypeError: Se 'enderecos' e 'subgrupo' não forem str ou se 'condicoes' não for Iterable.
        ValueError: Se algum argumento estiver vazio.
    """

    #Type check
    validar_tipo('endereco', endereco, str)
    validar_tipo('subgrupo', subgrupo, str)
    validar_tipo('condicoes', condicoes, Iterable)
    
    #Value check
    if not endereco:
        raise ValueError(f"endereco não pode estar vazio")
    if not subgrupo:
        raise ValueError(f"subgrupo não pode estar vazio")
    if not condicoes:
        raise ValueError(f"condicoes não pode estar vazio")

    if isinstance(condicoes, (tuple, list)):
        for condicao in condicoes:
            return verificar_condicao(endereco, subgrupo, condicao)

    elif isinstance(condicoes, str):  
        return any((
            endereco.endswith(condicoes), 
            condicoes in basename(endereco),
            subgrupo in basename(endereco)
            ))

def atende_as_condicoes(endereco: str, grupo_base: str, subgrupo: str, condicoes: Iterable) -> bool:
    """
    Verifica se o arquivo atende as condições necessárias de pertencimento.

    Args:
        endereco (str): Endereço completo do arquivo.
        grupo_base (str): Primeira pasta em relação ao diretorio principal.
        subgrupo (str): Nome da subpasta.
        condicoes (Iterable): Condições de pertencimento.

    Returns:
        bool: True se as condições forem atendidas, False caso contrário.

    Raises:
        TypeError: Se 'endereco,' 'grupo_base' ou 'subgrupo' não forem str. Se 'condicoes' não for Iterable.
    """

    #Type check
    validar_tipo('endereco', endereco, str)
    validar_tipo('subgrupo', subgrupo, str)
    validar_tipo('grupo_base', grupo_base, str)
    validar_tipo('condicoes', condicoes, Iterable)


    endereco = endereco.lower()
    grupo_base = grupo_base.lower()

    for condicao in condicoes:

        resultado = all((
            grupo_base in basename(endereco), 
            verificar_condicao(endereco, subgrupo, condicao)
        ))
        if resultado:
            break

    return resultado