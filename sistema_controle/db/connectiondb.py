"""
Módulo de Configuração de Conexão com o Banco de Dados.

Este módulo centraliza a criação de instâncias de conexão com o PostgreSQL,
garantindo que todas as partes do sistema utilizem os mesmos parâmetros de acesso.
"""

import psycopg2


def connection():
    """
    Estabelece uma conexão ativa com o banco de dados PostgreSQL.

    Returns:
        psycopg2.extensions.connection: Um objeto de conexão pronto para uso.

    Raises:
        psycopg2.OperationalError: Se as credenciais estiverem incorretas ou o
                                   servidor estiver offline.
    """
    return psycopg2.connect(
        host="127.0.0.1",
        database="sistema_de_tarefas",
        user="postgres",
        password="123456",
        port=5432,
    )
