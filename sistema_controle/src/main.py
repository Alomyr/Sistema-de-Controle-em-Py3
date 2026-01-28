from datetime import datetime
from sistema_controle.db.task_repository import add_task
from sistema_controle.src.model.task import Task


def main():
    task = Task(
        name="estudar python + postgres",
        data_destino=datetime(2026, 2, 20),
        descricao="finalizar CRUD",
    )
    add_task(task)
    print("✅ Tarefa adicionada com sucesso!")


if __name__ == "__main__":
    main()
