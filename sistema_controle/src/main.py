from datetime import datetime
from sistema_controle.db.task_repository import add_task
from sistema_controle.src.model.task import Task
from .view.task_view import render_menu, cadastro

start = True


def main():
    # task = Task(
    #     name="estudar python + postgres",
    #     data_destino=datetime(2026, 2, 20),
    #     descricao="finalizar CRUD",
    # )
    # add_task(task)
    # print("✅ Tarefa adicionada com sucesso!")

    while start:
        opt = render_menu()

        match opt:
            case 1:
                cadastro()
            case 2:
                break


if __name__ == "__main__":
    main()
