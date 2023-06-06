from estd_connection import estd_connection

def create_table():
    cursor = estd_connection()
    try:
        cursor.execute("DROP TABLE  DATA")

    except:
        sql = """
        CREATE TABLE DATA(
            TITLE CHAR(10),
            FIRST_NAME CHAR(20),
            LAST_NAME CHAR(20),
            AGE INT,
            STATUS CHAR(50),
            NATIONALITY CHAR(50),
            COMPLETED_COURSES INT,
            COMPLETED_SEMESTERS INT     
        )
        """

        cursor.execute(sql)
    else:
        sql = """
        CREATE TABLE DATA(
            TITLE CHAR(10),
            FIRST_NAME CHAR(20),
            LAST_NAME CHAR(20),
            AGE INT,
            STATUS CHAR(50),
            NATIONALITY CHAR(50),
            COMPLETED_COURSES INT,
            COMPLETED_SEMESTERS INT     
        )
        """

        cursor.execute(sql)
