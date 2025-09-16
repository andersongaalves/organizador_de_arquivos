import os
import shutil
import json

from collections.abc import Iterable
from typing import Any

from .utills import pedir_diretorio, adicionar_a

from .validar import validar_tipo

with open("src\\organizador_package\\config.json", "r", encoding="utf-8") as config:
    config = json.load(config)

def ler_arquivos(diretorio: str) -> tuple[str]:
    """
    Lê os arquivos de um diretorio e retorna seus endereços numa tupla.

    Args:
        diretorio (str): Diretorio com os arquivos.

    Returns:
        tuple: endereços dos arquivos.
    
    Raises:
        TypeError: Se 'diretorio' não for str.
        ValueError: Se 'diretorio' estiver vazio.
    """

    #Type check
    validar_tipo('diretorio', diretorio, str)
    #Value check
    if not diretorio:
        raise ValueError(f"o diretorio não pode estar vazio")
    #File check
    if not os.path.exists(diretorio):
        raise FileExistsError(f"O diretorio {diretorio} não existe")

    enderecos = tuple(
        os.path.join(diretorio, item) #Cria um endereço seguro do arquivo
        for item in os.listdir(diretorio) #Lê os arquivos do diretorio
        if os.path.isfile(os.path.join(diretorio, item)) #Verifica se o item é um arquivo
    )

    return enderecos

def separar_por_template(
    enderecos: Iterable[str], 
    template: str = 'TEMPLATE_PADRÃO'
    ) -> dict[str, Any]:

    """
    Separa os endereços baseado no template.

    Args:
        enderecos (Iterable[str]): Coleção com os endereços dos arquivos.
        template (str): Template de separação.

    Returns:
        dict ([str, any]): Arquivos separados.
    
    Raises:
        TypeError: Se 'enderecos' não for iterável ou 'template' não for dict.
        ValueError: Se 'enderecos' ou 'template' estiver vazio.

    Examples:
        >>> separar_por_grupo(("Download\\Audio.mp3", "Download\\Imagem.jpg", "Download\\documento.txt"))
        {
        'Áudios': ['Download\\Audio.mp3'],
        'Imagens': ['Download\\Imagem.jpg'],
        'Documentos': ['Download\\documento.txt']
        }
    """
    
    #Type check
    validar_tipo('enderecos', enderecos, Iterable)
    validar_tipo('template', template, str)
    #Value check
    if not enderecos:
        raise ValueError("enderecos não pode estar vazio")
    if not template:
        raise ValueError("template não pode estar vazio")


    arqs_separados = {}

    for grupo, valor in config[f'{template}'].items():

        if isinstance(valor, dict):
            sub1_chave = arqs_separados.setdefault(grupo, {})

            for sub1_nome, sub1_conteudo in valor.items():

                if isinstance(sub1_conteudo, dict):
                    sub2_chave = sub1_chave.setdefault(sub1_nome, {})

                    for sub2_nome, sub2_conteudo in sub1_conteudo.items():

                        if isinstance(sub2_conteudo, dict):
                            sub3_chave = sub2_chave.setdefault(sub2_nome, {})

                            for sub3_nome, sub3_conteudo in sub2_conteudo.items():

                                if isinstance(sub3_conteudo, dict):
                                    raise ValueError("Muitas pastas aninhadas")

                                adicionar_a(sub3_chave, grupo, sub3_nome, enderecos, sub3_conteudo)

                        else:
                            adicionar_a(sub2_chave, grupo, sub2_nome, enderecos, sub2_conteudo)

                else:
                    adicionar_a(sub1_chave, grupo, sub1_nome, enderecos, sub1_conteudo)
        else:
            adicionar_a(arqs_separados, grupo, grupo, enderecos, valor)

    return arqs_separados

def gerar_enderecos(
    arqs_por_template: dict[str, Any], 
    base: str = ""
) -> tuple[str]:
    """
    Gera todos os endereços finais (incluindo os arquivos)
    a partir da estrutura aninhada de dicionários do separador.

    Args:
        arqs_por_template (dict): Estrutura de arquivos agrupados.
        base (str): Caminho base acumulado.

    Returns:
        tuple[str]: Coleção com os caminhos completos até os arquivos.
    
    Raises:
        TypeError: Se 'arqs_por_template' não for dict.
        ValueError: Se 'arqs_por_template' estiver vazio.
    """

    #Type check
    validar_tipo('arqs_por_template', arqs_por_template, dict)
    #Value check
    if not arqs_por_template:
        raise ValueError(f"arqs_por_template não pode estar vazio")

    enderecos = []

    for grupo, valor in arqs_por_template.items():
        novo_base = os.path.join(base, grupo)

        if isinstance(valor, dict):
            enderecos.extend(gerar_enderecos(valor, novo_base))
        elif isinstance(valor, list):
            for arquivo in valor:
                enderecos.append(os.path.join(novo_base, os.path.basename(arquivo)))

    return tuple(enderecos)

def criar_pastas(diretorio: str, enderecos: Iterable[str]) -> None:
    """
    Cria pastas com base nos endereços.
    
    Args:
        diretorio (str): Diretorio onde as pastas vão ser criadas.
        enderecos (Iterable[str]): Endereços dos arquivos.
        
    Raises:
        TypeError: Se 'diretorio' não for str ou 'enderecos' não for Iterable.
        ValueError: Se 'enderecos' estiver vazio.
    """

    #Type check
    validar_tipo('diretorio', diretorio, str)
    validar_tipo('enderecos', enderecos, Iterable)
    #Value check
    if not enderecos:
        raise ValueError(f"enderecos não pode estar vazio")

    for endereco in enderecos:
        caminho = os.path.dirname(os.path.join(diretorio, endereco))
        if not os.path.exists(caminho):
            os.makedirs(caminho)

def mover_arquivos(diretorio: str, enderecos: Iterable[str]) -> None:
    """
    Move os arquivos para as pasta do seu grupo respectivo.

    Args:
        diretorio (str): diretorio onde os arquivos se encontram.
        enderecos (Iterable[str]): Endereços do arquivos.
    
    Raises:
        TypeError: Se 'diretorio' não for str ou 'enderecos' não for Iterable.
        ValueError: Se 'enderecos' estiver vazio.
    """

    #Type check
    validar_tipo('diretorio', diretorio, str)
    validar_tipo('enderecos', enderecos, Iterable)
    #Value check
    if not enderecos:
        raise ValueError(f"enderecos não pode estar vazio")

    for endereco in enderecos:
        origem = os.path.join(diretorio, os.path.basename(endereco))
        destino = os.path.join(diretorio, endereco)
        shutil.move(origem, destino)

def executar_pipe_organizador():
    """Executa a lógica do organizador."""

    try:
        diretorio = pedir_diretorio()
        enderecos = ler_arquivos(diretorio)
        enderecos_separados = separar_por_template(enderecos)
        lista_de_enderecos = gerar_enderecos(enderecos_separados)
        criar_pastas(diretorio, lista_de_enderecos)
        mover_arquivos(diretorio, lista_de_enderecos)
    except Exception as e:
        print(e)