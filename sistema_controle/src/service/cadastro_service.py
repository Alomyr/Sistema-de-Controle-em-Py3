from datetime import datetime
from sistema_controle.db.task_repository import add_task


def cadastro_service(task):
    """
    Realiza a validação e o registro de uma nova tarefa no sistema.

    Esta função aplica as regras de negócio necessárias antes de persistir
    os dados no repositório.

    Regras de Negócio:
        1. O nome da tarefa é obrigatório e não pode ser apenas espaços.
        2. A data de destino não pode ser anterior à data atual.

    Args:
        task (Task): Objeto contendo os dados da tarefa (nome, data, etc).

    Returns:
        bool: True se a tarefa foi adicionada com sucesso.

    Raises:
        ValueError: Se o nome estiver vazio ou se a data for retroativa.
    """
    # Validação: Nome nulo ou vazio
    if not task.name or task.name.strip() == "":
        raise ValueError("O nome da tarefa não pode estar vazio.")

    # Validação: Data retroativa
    if task.dataDestino.date() < datetime.now().date():
        raise ValueError("A data do compromisso não pode ser inferior ao dia atual.")

    return add_task(task)
