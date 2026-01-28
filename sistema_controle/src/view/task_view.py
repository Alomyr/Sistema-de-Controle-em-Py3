from datetime import datetime
from sistema_controle.db.task_repository import add_task
from sistema_controle.src.model.task import Task


def render_menu():
    print("1. Adicionar Tarefa")
    print("0. Sair")
    return int(input("opcao: "))


def cadastro():
    try:
        nome = input("Nome da tarefa: ")
        describe = input("Descricao: ")
        data_str = input("Data do compromiso: ")
        data_data = datetime.strptime(data_str, "%Y/%m/%d")

        task = Task(nome, data_data, describe)
        add_task(task)
    except Exception as errors:
        print(f"{errors}")
