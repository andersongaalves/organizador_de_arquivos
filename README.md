# 📁 Organizador de arquivos 📁

Um script em Python para organizar automaticamente arquivos em pastas e subpastas, separando-os por grupos com base em um template definido em JSON.
Ideal para produtores musicais que querem manter seus projetos organizados de forma eficiente.

---

## 📝 Funcionalidades

- ✅ Validação de entradas e diretórios.
- ✅ Criação automática de pastas e subpastas hierárquicas.
- ✅ Suporte a templates de até 4 níveis de aninhamento.
- ✅ Separação de arquivos por grupo e subgrupo.
- ✅ Identificação de arquivos por extensão e palavra-chave.
- ✅ Movimento automático dos arquivos para suas respectivas pastas.

---

## ❔ Como criar templates

1. Abra o arquivo config.json
2. Crie adicione uma chave com o nome do seu template.
3. Para criar pastas e subpastas use {}.
4. Para sinalizar as extensões e palavras chaves dos arquivos que serão movidos, use [] (colchetes).
Ex: 

```json
{
    "MEU_TEMPLATE": {
        "Músicas": {
            "Pop": ["Billie Elish", "Ariana Grande", ".mp3"],
            "Rap": ["Kendrick Lammar", "Tyler The Creator", ".mp3"]
        }
    }
}
```

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Sistema operacional compatível: Windows, Linux ou macOS
- Permissões de leitura e escrita no diretório a ser organizado

---

## 🚀 Como usar

1. Clone o repositório ou baixe o script.
2. Abra o terminal na pasta do script.
3. Execute o script:
 ```bash
 python main.py
 ```
4. Digite o caminho do diretório que deseja organizar.
5. O script irá:
   - Criar pastas e subpastas conforme o template.
   - Separar os arquivos por extensão e grupo.
   - Mover os arquivos para suas respectivas pastas.

---

## 💡 Melhorias Futuras

- Função para criar templates automaticamente a partir da leitura de pastas.
- Função para renomear arquivos automaticamente com base no template.

---
## 👤 Criador

- Nome: Anderson G. A. Alves
- Email: andersongaalves1@gmail.com
- GitHub: [https://github.com/andersongaalves](https://github.com/andersongaalves)
- LinkedIn: [https://www.linkedin.com/in/anderson-g-a-alves](https://www.linkedin.com/in/anderson-g-a-alves)