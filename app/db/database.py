from mysql.connector import connect, Error
import logging


def create_connection():
    try:
        conn = connect(
            host="localhost",
            user="budget",
            password="DevTest",
            database="budget")
        c = conn.cursor()
        logging.info("Connected to database")
        return conn, c
    except Error as e:
        # print(e)
        logging.error(e)
    return None


def close_connection(conn, c):
    c.close()
    conn.close()


def does_col_contain_val(statement: object, col: object, value: object) -> object:
    try:
        conn, c = create_connection()
        c.execute(statement, {col: value})
        value_found = (c.fetchone()[0] >= 1)
        c.close()
        return value_found
    except Error as e:
        print(e)
