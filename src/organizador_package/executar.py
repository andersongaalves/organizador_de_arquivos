from .utills import pedir_diretorio, limpar_terminal
from .organizador import ler_arquivos_do_diretorio, separar_enderecos_por_grupo, criar_pastas, separar_por_tipo, mover_arquivos

def executar_organizador_projetos():
    """Pipe de execução do organizador de projetos."""
    
    try:
        diretorio = pedir_diretorio() #Pedir o diretório ao usuário
        arquivos = ler_arquivos_do_diretorio(diretorio) #Ler os arquivos do diretório
        arquivos_separados_por_grupos = separar_enderecos_por_grupo(arquivos) #Separar os arquivos por grupo
        criar_pastas(arquivos_separados_por_grupos, diretorio) #Criar as pastas e subpastas
        arquivos_separados_por_tipo = separar_por_tipo(diretorio, arquivos_separados_por_grupos) #Separar os arquivos por tipo
        mover_arquivos(diretorio, arquivos_separados_por_tipo) #Mover os arquivos para as pastas e subpastas
        print('Organização concluída!')
        return True

    except Exception as e:
        print(f'Erro: {e}')
        return False

    finally:
        limpar_terminal()