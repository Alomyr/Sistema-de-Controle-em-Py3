import conexao


def criar_tabela():
    conection = conexao.conectar()
    cursor = conection.cursor()

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
    conection.commit()
    cursor.close()
    conection.close()

    print("creat tabela")


if __name__ == "__main__":
    criar_tabela()
