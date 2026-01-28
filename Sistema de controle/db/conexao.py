import psycopg2

try:
    conexao = psycopg2.connect(
        host="127.0.0.1",
        database="sistama de tarefas",
        user="postgres",
        password="123456",
        port=5432,
    )

    print("✅ Conectado ao PostgreSQL")

    cursor = conexao.cursor()
    cursor.execute("SELECT version();")
    print(cursor.fetchone())

    # cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", ("Matheus", 21))
    # conexao.commit()

    cursor.execute("SELECT * FROM pessoas")

    for linha in cursor.fetchall():
        print(linha)

except Exception as erro:
    print("❌ Erro:", erro)

finally:
    if "conexao" in locals():
        cursor.close()
        conexao.close()
        print("🔒 Conexão encerrada")
