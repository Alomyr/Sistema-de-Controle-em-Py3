from sistema_controle.db.connectiondb import connection
from sistema_controle.src.model.task import Task
from sistema_controle.db.tabela_Task import create_table


def add_task(task: Task):

    connectionTask = connection()
    cursor = connectionTask.cursor()

    create_table()

    cursor.execute(
        """
        INSERT INTO tarefas (nome, descricao, data_criacao, data_destino)
        VALUES (%s, %s, %s, %s)
        """,
        (
            task.name,
            task.descricao,
            task.dataAuto,
            task.dataDestino,
        ),
    )

    connectionTask.commit()
    cursor.close()
    connectionTask.close()


# fazer o delete e o list


def task_list():

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT nome, descricao, data_destino FROM tarefas;")
    list_task = cursor.fetchall()

    if not list_task:
        print("Lista vazia")

    else:
        for row in list_task:
            nome = row[0]
            desc = row[1]
            data = row[2]

            if hasattr(data, "strftime"):
                data_view = data.strftime("%d/%m/%Y")
            else:
                data_view = str(data)

            print(f"{nome:<15} | {desc:<20} | {data_view}")

        cursor.close()
        connectionTask.close()
