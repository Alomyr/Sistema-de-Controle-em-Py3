from sistema_controle.db.connectiondb import connection
from sistema_controle.src.model.task import Task


def add_task(task: Task):
    connectionTask = connection()
    cursor = connectionTask.cursor()

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
