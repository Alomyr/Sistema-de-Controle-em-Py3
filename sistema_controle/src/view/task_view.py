"""
Módulo de Interface de Visualização (View) do Sistema de Controle de Tarefas.

Este módulo é responsável por gerenciar a interação com o usuário via terminal,
renderizando menus, tabelas e coletando inputs para as operações de CRUD.
"""

from datetime import datetime
from sistema_controle.db.task_repository import (
    add_task,
    edit_status,
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


def render_cabecario():
    """Exibe o cabeçalho principal do sistema no console."""
    print("LISTA DE TAREFAS")
    print("---" * 30)


def render_colunas():
    """
    Renderiza o cabeçalho da tabela de tarefas com alinhamento fixo.

    Define a estrutura visual para as colunas: ID, Tarefa, Descrição, Data e Criada.
    """
    header = f"{'ID':<5} {'Tarefa':<20} {'Descricao':<25} {'Data':<10} {'Criada':<20}"
    print(header)
    print("-" * len(header))


def render_bottom():
    """Exibe uma linha de rodapé para separar blocos de informação."""
    print("---" * 30)


def render_menu() -> int:
    """
    Exibe o menu de opções principal e captura a escolha do usuário.

    Returns:
        int: O número da opção selecionada pelo usuário.
    """
    render_cabecario()
    print(
        "1. Adicionar Tarefa"
        "\n2. Listar tarefas"
        "\n3. Deletar tarefa"
        "\n4. Editar tarefa"
        "\n5. Editar status"
        "\n6. Deletar tudo"
        "\n7. Filtrar por status"
        "\n8. Exportar lista de tarefas .csv"
        "\n0. Sair"
    )
    return int(input("opcao: "))


def cadastro():
    """
    Interface para criação de uma nova tarefa.

    Coleta dados via terminal, converte a string de data em objeto datetime
    e envia para o serviço de cadastro.

    Raises:
        ValueError: Se o formato da data for inválido.
        Exception: Captura erros genéricos durante o processo de cadastro.
    """
    render_cabecario()
    try:
        nome = input("Nome da tarefa: ")
        describe = input("Descricao: ")
        data_str = input("Data do compromiso (AAAA/MM/DD): ")
        data_data = datetime.strptime(data_str, "%Y/%m/%d")
        status = state_machine_status()
        task = Task(nome, data_data, describe, status)
        cadastro_service(task)
    except Exception as errors:
        print(f"Erro ao cadastrar: {errors}")
    render_bottom()


def task_list_view():
    """
    Exibe todas as tarefas cadastradas no banco de dados.

    Utiliza as funções de renderização de colunas e busca a lista no repositório.
    """
    render_cabecario()
    render_colunas()
    try:
        task_list()
    except Exception as erros:
        print(f"Erro ao listar tarefas: {erros}")
    render_bottom()


def task_delet_view():
    """
    Interface para exclusão de uma tarefa específica.

    Mostra a lista atualizada e solicita o ID da tarefa que deve ser removida.
    """
    task_list_view()
    try:
        id_delet = int(input("Digite o id da tarefa para deletar: "))
        task_delet(id_delet)
    except ValueError:
        print("ID inválido. Digite um número.")


def task_delet_all_view():
    """Remove todas as tarefas do banco de dados após confirmação visual."""
    print("Deletando todas as tarefas...")
    task_delet_all()


def edit_task_view():
    """
    Interface para edição completa de uma tarefa existente.

    Solicita o ID e os novos dados (nome, descrição, data e status),
    atualizando o registro no banco de dados.
    """
    task_list_view()
    try:
        id_edit = int(input("id da tarefa q vc quer editar: "))
        print("Novos dados:")
        nome = input("Nome da tarefa: ")
        describe = input("Descricao: ")
        data_str = input("Data do compromiso (AAAA/MM/DD): ")
        data_data = datetime.strptime(data_str, "%Y/%m/%d")
        status = state_machine_status()
        task = Task(nome, data_data, describe, status)
        edit_task(id_edit, task)
    except Exception as errors:
        print(f"Erro ao editar: {errors}")


def edit_status_view():
    """
    Interface para alteração rápida apenas do status de uma tarefa.
    """
    task_list_view()
    try:
        id_edit = int(input("id da tarefa q vc quer editar: "))
        print("Novo status:")
        status = state_machine_status()
        edit_status(id_edit, status)
    except Exception as errors:
        print(f"Erro ao atualizar status: {errors}")


def status_filter_view():
    """
    Filtra e exibe tarefas com base em um status selecionado.
    """
    status = state_machine_status()
    render_cabecario()
    render_colunas()
    task_list_with_filter(status)
    render_bottom()
