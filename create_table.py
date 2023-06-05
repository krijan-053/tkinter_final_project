from estd_connection import estd_connection


def create_table():
    cursor = estd_connection()

    cursor.execute("DROP TABLE  DATA")

    sql = """
    CREATE TABLE DATA(
        TITLE CHAR(10),
        FIRST_NAME CHAR(20),
        LAST_NAME CHAR(20),
        AGE INT,
        NATIONALITY CHAR(50),
        COMPLETED_COURSES INT,
        COMPLETED_SEMESTERS INT

    )
    """

    cursor.execute(sql)