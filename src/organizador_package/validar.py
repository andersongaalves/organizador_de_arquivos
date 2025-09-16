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
    diretorio = validar_str(diretorio)

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
    if not isinstance(endereco, str):
        raise TypeError(f"endereco deve ser str. Você passou {type(endereco).__name__}")
    if not isinstance(subgrupo, str):
        raise TypeError(f"subgrupo deve ser str. Você passou {type(subgrupo).__name__}")
    if not isinstance(condicoes, Iterable):
        raise TypeError(f"condicoes deve ser Iterable. Você passou {type(condicoes).__name__}")
    
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
    if not isinstance(endereco, str):
        raise TypeError(f"endereco deve ser str. Você passou {type(endereco).__name__}")
    if not isinstance(grupo_base, str):
        raise TypeError(f"grupo_base deve ser str. Você passou {type(grupo_base).__name__}")
    if not isinstance(subgrupo, str):
        raise TypeError(f"subgrupo deve ser str. Você passou {type(subgrupo).__name__}")
    if not isinstance(condicoes, Iterable):
        raise TypeError(f"condicoes deve ser Iterable. Você passou {type(condicoes).__name__}")


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