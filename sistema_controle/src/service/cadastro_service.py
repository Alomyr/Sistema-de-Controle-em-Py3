from datetime import datetime
from sistema_controle.db.task_repository import add_task


def cadastro_service(task):
    """ "Regra de negocios do add_task"""
    if not task.name or task.name.strip() == "":
        raise ValueError("Nome nao pode esta null")
    if task.dataDestino.date() < datetime.now().date():
        raise ValueError("A data nao pode ser inferior ao dia atual")

    return add_task(task)
