import os

from .config import STEMS, PROJETOS

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
        raise TypeError(f'{string} deve ser str. Você passou {type(string).__name__}')

    return string

def validar_diretorio(diretorio: str) -> str:
    """
    Verifica se o diretório existe.
    Retorna o diretório se existir, caso contrário, lança FileNotFoundError.

    Args:
        diretorio (str): O diretório a ser verificado.
    
    Returns:
        str: O diretório verificado.

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
    if not os.path.exists(diretorio):
        raise FileNotFoundError(f'O diretório {diretorio} não existe.')

    return diretorio

def verificar_grupo(arquivo: str, grupo: str) -> bool:
    """
    Verifica se o nome do grupo está contido no nome do arquivo.
    Retorna True se estiver contido, caso contrário, retorna False.

    Args:
        arquivo (str): Nome do arquivo a ser verificado.
        grupo (str): Nome do grupo a ser verificado.
    
    Returns:
        bool: True se o nome do grupo estiver contido, False caso contrário.

    Raises:
        TypeError: Se 'arquivo' ou 'grupo' não forem str.

    Examples:
        >>> verificar_grupo('minha_musica_BEAT.wav', 'BEAT')
        True
        >>> verificar_grupo('minha_musica_GRAVAÇÃO.mp3', 'BEAT')
        False
    """

    #Type check
    arquivo = validar_str(arquivo)
    grupo = validar_str(grupo)

    #Verificando se o nome do grupo está contido no nome do arquivo
    if grupo in arquivo:
        return True

    return False

def verificar_projeto(arquivo: str) -> bool:
    """
    Verifica se a extensão do arquivo está na lista de extensões de projetos.
    Retorna True se estiver, caso contrário, retorna False.

    Args:
        arquivo (str): Nome do arquivo a ser verificado.

    Raises:
        TypeError: Se 'arquivo' não for str.

    Examples:
        >>> verificar_projeto('meu_projeto.flp')
        True
        >>> verificar_projeto('minha_musica.mp3')
        False
    """
    _, extensao_arq = os.path.splitext(arquivo)

    if extensao_arq in PROJETOS:
        return True

    return False

def verificar_stems(endereco_arquivo: str) -> bool:
    """
    Verifica se o nome do arquivo contém algum dos nomes de stems definidos.
    Retorna True se contiver, caso contrário, retorna False.

    Args:
        endereco_arquivo (str): Endereço completo do arquivo a ser verificado.
    
    Raises:
        TypeError: Se 'endereco_arquivo' não for str.
    
    Examples:
        >>> verificar_stems('C:/Musicas/track1_Vocals.wav')
        True
        >>> verificar_stems('C:/Musicas/track1_Voz_Principal.mp3')
        False
    """

    endereco_arquivo = validar_str(endereco_arquivo)

    for mix_bus in STEMS:
        nome_arquivo = os.path.basename(endereco_arquivo)
        
        if mix_bus in nome_arquivo:
            return True

    return False

def verificar_track(diretorio: str, grupo: str, nome_arquivo: str) -> bool:
    """
    Verifica se o nome do arquivo é igual ao do diretorio ou diretorio + grupo.
    Retorna True se for, False caso contrário.

    Args:
        diretorio (str): Endereço do diretorio.
        grupo (str): Nome do grupo
        nome_arquivo (str): Nome do arquivo a ser verificado.

    Returns:
        bool: True se for igual, False caso contrário.
    
    Raises:
        TypeError: Se 'diretorio', 'grupo' ou 'nome_arquivo' não forem str.
    
    Examples:
        >>> verificar_track()
    """
    nome_arquivo, _ = os.path.splitext(nome_arquivo)

    return nome_arquivo in (diretorio, f'{diretorio} [{grupo}]')