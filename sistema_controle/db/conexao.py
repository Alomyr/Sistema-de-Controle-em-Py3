import psycopg2


def conectar():
    return psycopg2.connect(
        host="127.0.0.1",
        database="sistama de tarefas",
        user="postgres",
        password="123456",
        port=5432,
    )
