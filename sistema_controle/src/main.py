from datetime import datetime
from sistema_controle.db.task_repository import add_task
from .model.task import Task
from .view.task_view import render_menu, cadastro, task_list_view
from .controller.state_machine import state_machine


# /**
#  NOTE: projeto precisa ser iniciado com o banco de dados configure no arquivo .vscode/settings.json
# */


def main():
    """
    Docstring for main

    classe inicial para rodar o sistema de controle de tarefas
    para rodar basta abrir o terminal com o venv ativo

        python -m sistema_controle.src.main

    """
    state_machine()


if __name__ == "__main__":
    main()
