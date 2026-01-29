"""
Módulo de Repositório de Tarefas (Data Access Layer).

Este módulo gerencia todas as operações de banco de dados (CRUD) para a
entidade Task, utilizando o PostgreSQL/MySQL via conexões de cursor.
"""

from sistema_controle.db.connectiondb import connection
from sistema_controle.src.model import task
from sistema_controle.src.model.task import Task
from sistema_controle.db.tabela_Task import create_table
import csv


def add_task(task: Task):
    """
    Insere uma nova tarefa no banco de dados.

    Args:
        task (Task): Objeto Task contendo os dados a serem persistidos.
    """

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


def task_list():
    """
    Busca e exibe todas as tarefas cadastradas.

    Note:
        A formatação de exibição utiliza f-strings para alinhamento em colunas.
    """

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT id, nome, descricao, data_destino, status FROM TASK;")
    list_task = cursor.fetchall()

    if not list_task:
        print("Lista vazia")

    else:
        for row in list_task:
            id_task = row[0]
            nome = row[1]
            desc = row[2]
            data = row[3]
            status = row[4]

            if hasattr(data, "strftime"):
                data_view = data.strftime("%d/%m/%Y")
            else:
                data_view = str(data)

            print(f"{id_task:<5} |{nome:<15} | {desc:<20} | {data_view} | {status}")

        cursor.close()
        connectionTask.close()


def task_list_with_filter(status_filter: str):
    """
    Filtra tarefas com base no status fornecido.

    Args:
        status_filter (str): O status exato para filtrar (ex: 'Concluido').
    """

    status_filter = status_filter

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT id, nome, descricao, data_destino, status FROM TASK;")
    list_task = cursor.fetchall()

    if not list_task:
        print("Lista vazia")

    else:
        for row in list_task:
            id_task = row[0]
            nome = row[1]
            desc = row[2]
            data = row[3]
            status = row[4]

            if hasattr(data, "strftime"):
                data_view = data.strftime("%d/%m/%Y")
            else:
                data_view = str(data)

            if status == status_filter:  # pega apenas os q tem o mesmo status
                print(f"{id_task:<5} |{nome:<15} | {desc:<20} | {data_view} | {status}")

        cursor.close()
        connectionTask.close()


def task_delet(id_delet):
    """
    Remove uma tarefa específica pelo ID.

    Args:
        id_delet (int): O identificador único da tarefa.
    """

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


def edit_task(id_edit: int, task: task):
    """
    Atualiza todos os campos de uma tarefa existente.

    Args:
        id_edit (int): ID da tarefa a ser modificada.
        task (Task): Novos dados da tarefa.
    """
    try:
        connectionTask = connection()
        cursor = connectionTask.cursor()

        sql = """
                    UPDATE TASK 
                    SET nome = %s, descricao = %s, data_destino = %s, status = %s
                    WHERE id = %s
                """
        valores = (task.name, task.descricao, task.dataDestino, task.status, id_edit)

        cursor.execute(sql, valores)
        connectionTask.commit()

        print(f"editando a tarefa")
        cursor.close
        if cursor.rowcount == 0:
            print(f"id nao encontrado para {id_edit}")
        else:
            print("Tarefa editada com sucesso: ")
    except Exception as errors:
        print(errors)
    finally:
        if connectionTask is not None:
            connectionTask.close()


def edit_status(id_edit: int, status: str):
    """Atualiza apenas o status de uma tarefa."""

    try:
        connectionTask = connection()
        cursor = connectionTask.cursor()

        sql = """
                    UPDATE TASK 
                    SET status = %s
                    WHERE id = %s
                """
        valores = (status, id_edit)

        cursor.execute(sql, valores)
        connectionTask.commit()

        print(f"editando a tarefa")
        cursor.close
        if cursor.rowcount == 0:
            print(f"id nao encontrado para {id_edit}")
        else:
            print("Tarefa editada com sucesso: ")
    except Exception as errors:
        print(errors)
    finally:
        if connectionTask is not None:
            connectionTask.close()


def task_delet_all():
    """Remove a tabela inteira do banco de dados (CUIDADO)."""
    try:
        connectionTask = connection()
        cursor = connectionTask.cursor()

        sql = "DROP TABLE task"
        cursor.execute(sql)

        connectionTask.commit()
        cursor.close
    except Exception as errors:
        print(errors)
    finally:
        if connectionTask is not None:
            connectionTask.close()


def export_tasks():
    """Exporta todos os registros da tabela TASK para um arquivo CSV ('dados.csv')."""
    conn = connection()
    print("Exportado para um arquivo csv...")

    connectionTask = connection()
    cursor = connectionTask.cursor()

    cursor.execute("SELECT id, nome, descricao, data_destino, status FROM TASK;")
    list_task = cursor.fetchall()

    if not list_task:
        print("Lista vazia")

    else:
        for row in list_task:
            id_task = row[0]
            nome = row[1]
            desc = row[2]
            data = row[3]
            status = row[4]

            if hasattr(data, "strftime"):
                data_view = data.strftime("%d/%m/%Y")
            else:
                data_view = str(data)

            print(f"{id_task:<5} |{nome:<15} | {desc:<20} | {data_view} | {status}")
            with open("dados.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nome", "Descricao", "Data", "Status"])
                writer.writerows(list_task)

        cursor.close()
        connectionTask.close()
