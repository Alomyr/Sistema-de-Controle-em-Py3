from ast import Delete
from sistema_controle.db.connectiondb import connection
from sistema_controle.src.model.task import Task
from sistema_controle.db.tabela_Task import create_table


# TEST: testa o status e colocar as coisas do metodo de status da tarefa
def add_task(task: Task):

    connectionTask = connection()
    cursor = connectionTask.cursor()

    create_table()

    cursor.execute(
        """
        INSERT INTO TASK (nome, descricao, data_criacao, data_destino, status)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            task.name,
            task.descricao,
            task.dataAuto,
            task.dataDestino,
            task.status,
        ),
    )

    connectionTask.commit()
    cursor.close()
    connectionTask.close()


# REFACTOR: colocar as opcoes de filtro nesse metodo e mudar o metodo de listagem para colcoar o status e o novo nome
def task_list():

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT id, nome, descricao, data_destino FROM TASK;")
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

        sql = "DELETE FROM TASK WHERE    id=%s"
        cursor.execute(sql, (id_delet,))

        connectionTask.commit()
        print(f"deletado a tarefa com id: {id_delet}")
        cursor.close
    except Exception as errors:
        print(errors)
    finally:
        if connectionTask is not None:
            connectionTask.close()
