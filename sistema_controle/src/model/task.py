from datetime import datetime


class Task:
    def __init__(
        self, id: int, name: str, day: int, month: int, year: int, descriacao: str = ""
    ):
        self.nome = name.capitalize()
        self.dataDestino = datetime(year, month, day)
        self.dataAuto = datetime.now()
        self.descricao = descriacao
