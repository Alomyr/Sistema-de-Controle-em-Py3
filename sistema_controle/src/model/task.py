from datetime import datetime


class Task:
    """
    Representa uma tarefa dentro do sistema de controle.

    A classe encapsula todos os dados necessários para uma tarefa, incluindo
    metadados gerados automaticamente, como a data de criação.

    Attributes:
        name (str): Nome ou título da tarefa (armazenado em Capitalize).
        dataDestino (datetime): Data e hora limite para a conclusão da tarefa.
        dataAuto (datetime): Data e hora em que a tarefa foi instanciada (gerada automaticamente).
        descricao (str): Detalhamento opcional sobre a tarefa.
        status (str): Estado atual da tarefa (ex: "Concluido", "In Progress").
    """

    def __init__(
        self,
        name: str,
        data_destino: datetime,
        descricao: str = "",
        status: str = "Pendente",
    ):
        """
        Inicializa uma nova instância de Task.

        Args:
            name (str): O nome da tarefa.
            data_destino (datetime): Objeto datetime representando o prazo final.
            descricao (str, optional): Texto descritivo. Defaults to "".
            status (str, optional): Status inicial da tarefa. Defaults to "Pendente".
        """
        # Formata o nome para garantir consistência visual (Primeira letra maiúscula)
        self.name = name.capitalize()

        # Define o prazo final da tarefa
        self.dataDestino = data_destino

        # Timestamp de criação (gerado no momento da execução)
        self.dataAuto = datetime.now()

        self.descricao = descricao
        self.status = status
