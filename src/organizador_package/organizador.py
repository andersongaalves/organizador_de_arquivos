import shutil
import os

from .validar import validar_str, validar_diretorio, verificar_grupo, verificar_projeto, verificar_stems, verificar_track
from .config import GRUPOS, SUBPASTAS

def ler_arquivos_do_diretorio(diretorio: str) -> list[str]:
    """
    Lê os arquivos do diretório e retorna uma lista com os endereços completos dos arquivos.

    Args:
        diretorio (str): Caminho do diretório a ser lido.
    
    Returns:
        list[str]: Lista com os endereços completos dos arquivos.
    
    Raises:
        TypeError: Se 'diretorio' não for str.
    
    Examples:
        >>> ler_arquivos_do_diretorio('C:/MeusArquivos')
        ['C:/MeusArquivos/arquivo1.txt', 'C:/MeusArquivos/arquivo2.mp3', ...]
    """
    #Type check
    diretorio = validar_str(diretorio)

    #FileExist check
    diretorio = validar_diretorio(diretorio)

    #Lendo os arquivos do diretório
    arquivos_diretorio = os.listdir(diretorio)

    #Retornando a lista com os endereços completos dos arquivos
    return [os.path.join(diretorio, arquivo) for arquivo in arquivos_diretorio]

def separar_enderecos_por_grupo(arquivos: list[str]) -> dict[str, list[str]]:

    enderecos_por_grupo = {}

    for endereco_arquivo in arquivos:
        if os.path.isfile(endereco_arquivo):
            adicionado = False
            for grupo in GRUPOS:
                if verificar_grupo(os.path.basename(endereco_arquivo), grupo):
                    enderecos_por_grupo.setdefault(grupo, []).append(endereco_arquivo)
                    adicionado = True
                    break

            if not adicionado:
                enderecos_por_grupo.setdefault('OUTROS', []).append(endereco_arquivo)

    return enderecos_por_grupo

def criar_sub_pastas_n1(caminho: str) -> None:
    """
    Cria pastas com os nomes das strings armazenadas na chave 'n1' do dict SUBPASTAS.

    Args:
        caminho (str): Caminho onde a pasta será criada.
    
    Returns:
        None
    
    Raises:
        TypeError: Se 'caminho' não for str.
    """

    for sub_pasta_n1 in SUBPASTAS['n1']:
        caminho_n1 = os.path.join(caminho, sub_pasta_n1)
        os.makedirs(caminho_n1)

def criar_sub_pastas_n2(caminho: str) -> None:

    if not 'EXPORTAÇÕES' in caminho:
        caminho = os.path.join(caminho, 'EXPORTAÇÕES')

    for sub_pasta_n2 in SUBPASTAS['n2']:
        caminho_n2 = os.path.join(caminho, sub_pasta_n2)
        os.makedirs(caminho_n2)
        criar_sub_pastas_n3(caminho_n2)

def criar_sub_pastas_n3(caminho: str) -> None:

    if not 'EXPORTAÇÕES' in caminho:
        caminho = os.path.join(caminho, 'EXPORTAÇÕES')

    for sub_pasta_n3 in SUBPASTAS['n3']:
        caminho_n3 = os.path.join(caminho, sub_pasta_n3)
        os.makedirs(caminho_n3)

def criar_pastas(grupos, diretorio: str) -> None:
    """
    Cria pastas e subpastas para cada grupo da constante GRUPOS.

    Args:
        diretorio (str): onde as pastas serão criadas.

    Raises:
        TypeError: Se 'diretorio' não for str.

    """

    diretorio = validar_str(diretorio)

    for grupo in grupos.keys():
        caminho = os.path.join(diretorio, grupo)

        if os.path.exists(caminho):
            continue

        os.makedirs(caminho)

        match grupo:
            case 'BEAT':

                criar_sub_pastas_n1(caminho)
                criar_sub_pastas_n3(caminho)

            case 'GRAVAÇÃO':

                criar_sub_pastas_n1(caminho)
                criar_sub_pastas_n3(caminho)

            case 'ROUGH MIX':
                criar_sub_pastas_n1(caminho)
                criar_sub_pastas_n2(caminho)

            case 'OUTROS':
                pass

            case _:
                criar_sub_pastas_n1(caminho)        

def separar_por_tipo(diretorio, grupo_enderecos: dict[str, list[str]]) -> dict[str, dict[str, list[str]]]:
    separados_por_grupos_e_tipo = {}

    for grupo, enderecos in grupo_enderecos.items():

        for endereco in enderecos:
            nome_arquivo = os.path.basename(endereco)
            
            if verificar_stems(nome_arquivo):
                separados_por_grupos_e_tipo.setdefault(grupo, {}).setdefault('STEMS', []).append(endereco)
            elif verificar_projeto(nome_arquivo):
                separados_por_grupos_e_tipo.setdefault(grupo, {}).setdefault('PROJETOS', []).append(endereco)
            elif verificar_track(diretorio, grupo, nome_arquivo):
                separados_por_grupos_e_tipo.setdefault(grupo, {}).setdefault('TRACKS', []).append(endereco)
            else:
                separados_por_grupos_e_tipo.setdefault(grupo, {}).setdefault('MULTITRACK', []).append(endereco)

    return separados_por_grupos_e_tipo

def mover_arquivos(diretorio, grupo_enderecos):
    
    for grupo, tipos in grupo_enderecos.items():
        for tipo, enderecos in tipos.items():
            for endereco in enderecos:
                match tipo:

                    case 'STEMS':
                        shutil.move(
                            endereco,
                            os.path.join(diretorio, grupo, 'EXPORTAÇÕES', tipo, os.path.basename(endereco))
                            )

                    case 'MULTITRACK':
                        caminho = os.path.join(diretorio, grupo, 'EXPORTAÇÕES', tipo)

                        if grupo == 'OUTROS':
                            shutil.move(
                                endereco,
                                os.path.join(diretorio, grupo, os.path.basename(endereco))
                                )
                        elif os.path.exists(caminho):
                            shutil.move(
                                endereco,
                                os.path.join(caminho, os.path.basename(endereco))
                                )
                        else:
                            shutil.move(
                                endereco,
                                os.path.join(diretorio, grupo, 'EXPORTAÇÕES', os.path.basename(endereco))
                                )

                    case 'PROJETOS':
                        shutil.move(
                            endereco,
                            os.path.join(diretorio, grupo, 'PROJETOS', os.path.basename(endereco))
                        )

                    case _:
                        shutil.move(
                            endereco,
                            os.path.join(diretorio, grupo, 'EXPORTAÇÕES', 'TRACKS', os.path.basename(endereco))
                            )