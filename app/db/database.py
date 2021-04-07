from mysql.connector import connect, Error
import logging


def create_connection(database="budget"):
    try:
        conn = connect(
            host="localhost",
            user="budget",
            password="DevTest",
            database=database)
        c = conn.cursor()
        logging.info("Connected to database")
        return conn, c
    except Error as e:
        # print(e)
        logging.error(e)
    return None


def close_connection(conn, c):
    """

    :rtype: object
    """
    c.close()
    conn.close()


def does_col_contain_val(statement: object, col: object, value: object) -> object:
    try:
        conn, c = create_connection()
        c.execute(statement, {col: value})
        value_found = (c.fetchone()[0] >= 1)
        close_connection(conn, c)
        return value_found
    except Error as e:
        print(e)


def fetch(sql):  # TODO use this function in db Classes
    try:
        conn, c = create_connection()
        c.execute(sql)
        result = c.fetchall()
        close_connection(conn, c)
        return result
    except Error as e:
        print(e)


def execute(sql):  # TODO use this function in db Classes
    try:
        conn, c = create_connection()
        c.execute(sql)
        close_connection(conn, c)
    except Error as e:
        print(e)


def get_boolean(txt_boolean):
    if txt_boolean == 0 or txt_boolean == "0":
        return False
    else:
        return True
