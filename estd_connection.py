def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="data_info",
        user="postgres",
        password="apple",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor
