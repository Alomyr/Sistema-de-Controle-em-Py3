from datetime import datetime
from sistema_controle.db.task_repository import add_task
from sistema_controle.src.model.task import Task
from .view.task_view import render_menu, cadastro

start = True


def main():
    while start:  ## passar isso para um maquina de estados
        opt = render_menu()

        match opt:
            case 1:
                cadastro()
            case 0:
                break


if __name__ == "__main__":
    main()
