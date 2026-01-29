from datetime import datetime
from sistema_controle.db.task_repository import add_task, task_list, task_delet
from sistema_controle.src.model.task import Task


# TODO: fazer o rende do menu com as novas opt e
# fazer o rende do status
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
        status = input("Estado: ")
        task = Task(nome, data_data, describe, status)
        add_task(task)
    except Exception as errors:
        print(f"{errors}")


def task_list_view():

    try:
        task_list()
    except Exception as erros:
        print(f"{erros}")


def task_delet_view():
    task_list_view()
    id_delet = int(input("Digite o id da tarefa para deletar: "))
    task_delet(id_delet)
