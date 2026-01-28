from datetime import datetime
from sistema_controle.db.task_repository import add_task
from .model.task import Task
from .view.task_view import render_menu, cadastro, task_list_view
from .controller.state_machine import state_machine


# python -m sistema_controle.src.main
def main():
    state_machine()


if __name__ == "__main__":
    main()
