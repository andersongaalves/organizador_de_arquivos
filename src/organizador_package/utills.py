import os

def exibir(template: str):
    print(template)
    print(f'{"=" * 60}' + '\n')

def pedir_diretorio() -> str:
    return input('Digite o caminho do diretório que deseja organizar: ')

def limpar_terminal(delay=1.5):
    animar_pontos(3, delay)
    os.system('cls' if os.name == 'nt' else 'clear')

def animar_pontos(pontos=3, tempo=1.5):
    import time

    for _ in range(pontos):
        print('.', end='', flush=True)
        time.sleep(tempo / pontos)