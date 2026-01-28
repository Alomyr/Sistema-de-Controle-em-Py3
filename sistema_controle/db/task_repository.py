from ast import Delete
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


def task_list():  # colcoar o metodo de filtro aqui dentro

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT id, nome, descricao, data_destino FROM tarefas;")
    list_task = cursor.fetchall()

    if not list_task:
        print("Lista vazia")

    else:
        for row in list_task:
            id_task = row[0]
            nome = row[1]
            desc = row[2]
            data = row[3]

            if hasattr(data, "strftime"):
                data_view = data.strftime("%d/%m/%Y")
            else:
                data_view = str(data)

            print(f"{id_task:<5} |{nome:<15} | {desc:<20} | {data_view}")

        cursor.close()
        connectionTask.close()


def task_delet(id_delet):
    try:
        connectionTask = connection()
        cursor = connectionTask.cursor()

        sql = "DELETE FROM tarefas WHERE    id=%s"
        cursor.execute(sql, (id_delet,))

        connectionTask.commit()
        print(f"deletado a tarefa com id: {id_delet}")
        cursor.close
    except Exception as errors:
        print(errors)
    finally:
        if connectionTask is not None:
            connectionTask.close()
