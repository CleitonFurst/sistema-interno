import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sistema_interno",
        user="dev_user",
        password="?#&l8N3^98.",
        host="localhost"
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro na conexão:", str(e).encode("utf-8", "ignore").decode("utf-8"))
