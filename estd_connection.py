import psycopg2


def estd_connection():
    conn = psycopg2.connect(
        database="data_info",
        user="postgres",
        password="apple",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection Established Successfully !!")
    cursor = conn.cursor()
    return cursor


estd_connection()


