from os.path import basename, exists

from collections.abc import Iterable

def validar_str(string) -> str:
    """
    Verifica se o argumento passado é uma string.
    Retorna o texto da string se for, caso contrário, lança TypeError.

    Args:
        string: O argumento a ser verificado.

    Returns:
        str: O texto da string verificada.
    
    Raises:
        TypeError: Se 'string' não for str.

    Examples:
        >>> verificar_str('Olá, mundo!')
        'Olá, mundo!'

        >>> verificar_str(123)
        Traceback (most recent call last):
            ...
        TypeError: 123 deve ser str. Você passou int
     """

    if not isinstance(string, str):
        raise TypeError(f'"{string}" deve ser str. Você passou {type(string).__name__}')

    return string

def validar_diretorio(diretorio: str) -> bool | str:
    """
    Verifica se o diretório existe. Retorna True se existir caso contrário, lança FileNotFoundError.

    Args:
        diretorio (str): O diretório a ser verificado.
    
    Returns:
        bool: True se existir, False caso contrário.

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
    diretorio = validar_str(diretorio)

    #Verificando se o diretório existe
    if not exists(diretorio):
        raise FileNotFoundError(f'O diretório {diretorio} não existe.')

    return diretorio

def verificar_condicao(endereco: str, subgrupo: str, condicoes: Iterable) -> bool:
    if isinstance(condicoes, (tuple, list)):
        for condicao in condicoes:
            return verificar_condicao(endereco, subgrupo, condicao)

    elif isinstance(condicoes, str):  
        return any((
            endereco.endswith(condicoes), 
            condicoes in basename(endereco),
            subgrupo in basename(endereco)
            ))

def pertence_ao_grupo(endereco, grupo_base, subgrupo, condicoes) -> bool:
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