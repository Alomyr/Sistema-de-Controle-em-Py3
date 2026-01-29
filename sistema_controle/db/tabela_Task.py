"""
Módulo de Definição de Esquema (Schema) do Banco de Dados.

Este script é responsável por garantir que a estrutura física do banco de dados
(tabelas e constraints) esteja presente antes da execução das operações de CRUD.
"""

from sistema_controle.db import connectiondb


def create_table():
    """
    Cria a tabela 'TASK' no banco de dados caso ela não exista.

    A tabela armazena as seguintes informações:
        - id: Identificador único autoincrementado.
        - nome: Título da tarefa.
        - descricao: Detalhes adicionais.
        - data_criacao: Data de registro automático.
        - data_destino: Prazo final definido pelo usuário.
        - status: Estado atual (Concluido, In Progress, Não Iniciada).

    Note:
        Para executar este script isoladamente, use o comando:
        python3 -m sistema_controle.db.tabela_Task
    """

    connection = connectiondb.connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS TASK (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            data_criacao TIMESTAMP NOT NULL,
            data_destino TIMESTAMP NOT NULL,
            status TEXT
        );
    """
    )
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_table()
