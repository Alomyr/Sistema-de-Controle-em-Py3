from datetime import datetime


class Task:
    def __init__(
        self, name: str, data_destino: datetime, descricao: str = "", status="null"
    ):
        self.name = name.capitalize()
        self.dataDestino = data_destino
        self.dataAuto = datetime.now()
        self.descricao = descricao
        self.status = status
