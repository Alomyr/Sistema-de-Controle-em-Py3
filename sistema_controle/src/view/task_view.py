from datetime import datetime
from sistema_controle.db.task_repository import (
    add_task,
    edit_statos,
    edit_task,
    task_delet_all,
    task_list,
    task_delet,
    task_list_with_filter,
)
from sistema_controle.src.model.task import Task
from sistema_controle.src.service import cadastro_service
from sistema_controle.src.util.util import state_machine_status
from sistema_controle.src.service.cadastro_service import cadastro_service


# TODO: fazer o rende do menu com as novas opt e
# fazer o rende do status
# REFACTOR: LIMPAR E CORRIGIR METODOS REPETIDOS
def render_menu():
    print(
        "1. Adicionar Tarefa\n2. Listar tarefas\n3. Deletar tarefa\n4. Editar tarefa\n5. Editar status\n6. Deletar tudo\n7. Filtrar por status"
    )
    print("0. Sair")
    return int(input("opcao: "))


def cadastro():
    try:
        nome = input("Nome da tarefa: ")
        describe = input("Descricao: ")
        data_str = input("Data do compromiso: ")
        data_data = datetime.strptime(data_str, "%Y/%m/%d")
        status = state_machine_status()
        task = Task(nome, data_data, describe, status)
        cadastro_service(task)
    except Exception as errors:
        print(f"{errors}")


def task_list_view():
    print("Lista de todas as tarefas\n\n")
    try:
        task_list()
    except Exception as erros:
        print(f"{erros}")


def task_delet_view():
    task_list_view()
    id_delet = int(input("Digite o id da tarefa para deletar: "))
    task_delet(id_delet)


def task_delet_all_view():
    print("Deletando todas as tarefas...")
    task_delet_all()


def edit_task_view():
    task_list_view()
    try:
        id_edit = int(input("id da tarefa q vc quer editar: "))
        print("Novos dados:")
        nome = input("Nome da tarefa: ")
        describe = input("Descricao: ")
        data_str = input("Data do compromiso: ")
        data_data = datetime.strptime(data_str, "%Y/%m/%d")
        status = state_machine_status()
        task = Task(nome, data_data, describe, status)
        edit_task(id_edit, task)
    except Exception as errors:
        print(f"{errors}")


def edit_status_view():
    task_list_view()
    try:
        id_edit = int(input("id da tarefa q vc quer editar: "))
        print("Novos dados:")
        status = state_machine_status()
        edit_statos(id_edit, status)
    except Exception as errors:
        print(f"{errors}")


def status_filter_view():
    status = state_machine_status()
    task_list_with_filter(status)
