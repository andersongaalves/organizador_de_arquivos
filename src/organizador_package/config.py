GRUPOS = ('BEAT', 'GRAVAÇÃO', 'ROUGH MIX', 'MIXAGEM', 'MASTERIZAÇÃO')
STEMS = ('KEYBOARDS', 'DRUMS', 'DRUM AND BASS', 'VOCALS', 'BUS')
PROJETOS = ('.zip', '.flp')
SUBPASTAS = {
    'n1': ('EXPORTAÇÕES', 'PROJETOS'),
    'n2': ('INSTRUMENTAL', 'VOCALS'),
    'n3': ('STEMS', 'MULTITRACK', 'TRACKS'),
    }
INSTRUCOES = {
    'NOMEAR_ARQUIVOS': """
==================COMO NOMEAR OS ARQUIVOS==================

STEM:
Padrão: (Nome_do_projeto)_(Tipo)_([Grupo]).extensão
Ex:     Projeto_BUS_VOCALS_[GRAVAÇÃO].wav

MULTITRACK:
Padrão: (Nome_do_projeto)_(Elemento)_([Grupo]).extensão
Ex:     Projeto_GUITARRA_[BEAT].wav

PROJETO:
Padrão: (Nome_do_projeto)_([Grupo]).extensão
Ex:     Projeto_[MIXAGEM].flp

TRACK:
Padrão: (Nome_do_projeto)_([Grupo]).extensão
Ex:     Projeto_[MASTERIZAÇÃO].wav
        """
    }