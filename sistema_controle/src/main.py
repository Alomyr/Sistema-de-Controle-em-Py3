from datetime import datetime
from sistema_controle.db.task_repository import add_task
from sistema_controle.src.model.task import Task
from .view.task_view import render_menu, cadastro, task_list_view

start = True


# python -m sistema_controle.src.main
def main():
    while start:  ## passar isso para um maquina de estados
        opt = render_menu()

        match opt:
            case 1:
                cadastro()
            case 0:
                task_list_view()
                break


if __name__ == "__main__":
    main()
