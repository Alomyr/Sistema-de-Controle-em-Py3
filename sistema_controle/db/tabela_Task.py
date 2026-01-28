from sistema_controle.db import connectiondb


def create_table():
    """
    para rodar a criacao da tabela por esse aquivo deve usar:
        python3 -m sistema_controle.db.tabela_Task
    """
    # print("Criando tabela...")

    # TODO: tem q colocar o status da tarefa aqui e quais os tipos de estaos vao ser
    # adicionando aqui nele ou seja uma "maquina de estado" para definir o estado atual da tarefa
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
