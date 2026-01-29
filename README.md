# 📝 Sistema de Controle de Tarefas (CLI)

Um gerenciador de tarefas robusto desenvolvido em Python 3, utilizando PostgreSQL para persistência de dados e seguindo padrões de arquitetura em camadas. O projeto conta com documentação automatizada e validações de regras de negócio.

## 🚀 Funcionalidades

    CRUD Completo: Adicionar, listar, editar e deletar tarefas.

    Máquina de Estados: Controle rigoroso de status (Não Iniciada, Em Progresso, Concluído).

    Filtros Avançados: Busca de tarefas por status específico.

    Exportação: Gera relatórios em formato .csv de todas as tarefas.

    Persistência: Integração com banco de dados relacional PostgreSQL.

    Interface Limpa: Renderização de tabelas alinhadas no terminal.

## 🛠️ Tecnologias Utilizadas

    Linguagem: Python 3.10+

    Banco de Dados: PostgreSQL

    Driver DB: Psycopg2

    Documentação: MkDocs com padrão Google Style.

    Variáveis de Ambiente: Python-dotenv

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

    Python 3

    PostgreSQL

    Git

### Dependências

Instale as bibliotecas necessárias:
        pip install psycopg2 python-dotenv mkdocs-material mkdocstrings[python]

## ⚙️ Configuração

#### Clonar o repositório

    git clone https://github.com/Alomyr/Sistema-de-Controle-em-Py3.git

    cd Sistema-de-Controle-em-Py3

#### Criar a Tabela: Execute o script de inicialização do banco ou use adicione uma tarefa e a tabela sera criada automaticamente

## 🏃 Como Rodar

### Para iniciar o sistema, execute o arquivo principal (ajuste conforme seu ponto de entrada)

        python -m sistema_controle.src.main

## 📂 Estrutura do Projeto

        ├── sistema_controle/
        │   ├── db/          # Conexão, Scripts SQL e Repositórios
        │   ├── src/
        │   │   ├── model/   # Classes de Entidade (Task)
        │   │   ├── service/ # Regras de Negócio e Validações
        │   │   ├── view/    # Interface de Usuário (CLI)
        │   │   └── util/    # Utilitários e Máquina de Estado
        │   ├── docs/            # Arquivos Markdown para documentação
        │   └── main.py          # Ponto de entrada do sistema
