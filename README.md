# Organizador de Projetos Musicais

Um script em Python para organizar automaticamente arquivos de projetos musicais em pastas e subpastas, separando por **grupos** (BEAT, GRAVAÇÃO, ROUGH MIX, MIXAGEM, MASTERIZAÇÃO) e **tipos de arquivos** (STEMS, MULTITRACK, TRACKS, PROJETOS). Ideal para produtores musicais que querem manter seus projetos organizados de forma eficiente.

---

## 📝 Funcionalidades

- Validação de entradas e diretórios.
- Criação automática de pastas e subpastas com hierarquia:

GRUPO
├── EXPORTAÇÕES
│ ├── STEMS
│ ├── MULTITRACK
│ └── TRACKS
└── PROJETOS

- Separação de arquivos por **grupo**:
- `BEAT`
- `GRAVAÇÃO`
- `ROUGH MIX`
- `MIXAGEM`
- `MASTERIZAÇÃO`
- `OUTROS` (arquivos não categorizados)

- Identificação de arquivos por **tipo**:
- `STEMS` (ex.: KEYBOARDS, DRUMS, VOCALS)
- `MULTITRACK`
- `TRACKS` (faixas principais do projeto)
- `PROJETOS` (.zip, .flp)

- Movimento automático dos arquivos para suas respectivas pastas.

- Limpeza visual do terminal com animação de pontos durante a execução.

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Sistema operacional compatível: Windows, Linux ou macOS
- Permissões de leitura e escrita no diretório dos projetos

---

## 🚀 Como usar

1. Clone o repositório ou baixe o script.
2. Abra o terminal na pasta do script.
3. Execute o script:
 ```bash
 python organizador_projetos.py
 ```
4. Digite o caminho do diretório que deseja organizar.
5. O script irá:
    - Criar pastas e subpastas conforme os grupos.
    - Separar os arquivos por grupo e tipo.
    - Mover os arquivos para suas pastas corretas.
6. Ao final, o terminal será limpo e a organização estará concluída.

---

## 🏷️ Convenção de Nomes de Arquivos

Para que o script funcione corretamente, os arquivos precisam seguir um padrão de nomeação:

|Tipo|----|Padrão|------------------------------------------|Exemplo|--------------------------|
|STEM|----|(Nome_do_projeto)_(Tipo)_([Grupo]).extensão|-----|Projeto_BUS_VOCALS_[GRAVAÇÃO].wav
|MULTITRACK|(Nome_do_projeto)_(Elemento)_([Grupo]).extensão|Projeto_GUITARRA_[BEAT].wav
|PROJETO|--|(Nome_do_projeto)_([Grupo]).extensão|-----------|Projeto_[MIXAGEM].flp
|TRACK|----|(Nome_do_projeto)_([Grupo]).extensão|-----------|Projeto_[MASTERIZAÇÃO].wav

**⚠ Atenção: É importante manter o nome do grupo entre colchetes ([GRUPO]) e sem espaços para que o script consiga identificar corretamente.**

---

## 📁 Estrutura das pastas criada

DIRETÓRIO_DO_PROJETO
├── BEAT
│   ├── EXPORTAÇÕES
│   │   ├── STEMS
│   │   ├── MULTITRACK
│   │   └── TRACKS
│   └── PROJETOS
├── GRAVAÇÃO
│   ├── EXPORTAÇÕES
│   │   ├── STEMS
│   │   ├── MULTITRACK
│   │   └── TRACKS
│   └── PROJETOS
├── ROUGH MIX
│   ├── EXPORTAÇÕES
│   │   ├── INSTRUMENTAL
│   │   │   ├── STEMS
│   │   │   ├── MULTITRACK
│   │   │   └── TRACKS
│   │   └── VOCALS
│   │       ├── STEMS
│   │       ├── MULTITRACK
│   │       └── TRACKS
│   └── PROJETOS
├── MIXAGEM
│   ├── EXPORTAÇÕES
│   └── PROJETOS
├── MASTERIZAÇÃO
│   ├── EXPORTAÇÕES
│   └── PROJETOS
└── OUTROS

---

## 👤 Criador

- Nome: Anderson G. A. Alves
- Email: andersongaalves1@gmail.com
- GitHub: [https://github.com/andersongaalves](https://github.com/andersongaalves)
- LinkedIn: [https://www.linkedin.com/in/anderson-g-a-alves](https://www.linkedin.com/in/anderson-g-a-alves)