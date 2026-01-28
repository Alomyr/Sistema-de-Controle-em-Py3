from sistema_controle.db import connectiondb


def create_table():
    """
    para rodar a criacao da tabela por esse aquivo deve usar:
        python3 -m sistema_controle.db.tabela_Task
    """

    connection = connectiondb.connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            data_criacao TIMESTAMP NOT NULL,
            data_destino TIMESTAMP NOT NULL
        );
    """
    )
    connection.commit()
    cursor.close()
    connection.close()

    # print("creat tabela")


if __name__ == "__main__":
    create_table()
