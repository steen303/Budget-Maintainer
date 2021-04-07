import logging
from mysql.connector import Error

from db.database import create_connection, close_connection
from domain.categorie import Categorie, Categories


class DbCategorie:
    sql_get_by_id = """SELECT * FROM categorie WHERE id = %s"""
    sql_get_by_name = "SELECT * FROM categorie WHERE name = %s"
    sql_get_all = "SELECT * FROM categorie"
    sql_add = "INSERT INTO categorie (name) VALUES (%s)"
    sql_replace = "REPLACE INTO categorie (name, name) VALUES (%s, %s)"
    sql_delete = "DELETE FROM categorie WHERE name = %d"

    def get_by_id(self, categorie_id):
        conn, c = create_connection()
        c.execute(self.sql_get_by_id, (categorie_id,))
        rows = c.fetchall()
        close_connection(conn, c)
        return Categorie(rows[0][0], rows[0][1])

    def get_by_name(self, name):
        conn, c = create_connection()
        c.execute(self.sql_get_by_name, (name,))
        rows = c.fetchall()
        close_connection(conn, c)
        if len(rows) > 0:
            return Categorie(rows[0][0], rows[0][1])
        else:
            return None

    def get_all(self):
        conn, c = create_connection()
        c.execute(self.sql_get_all)
        cat = Categories()
        rows = c.fetchall()
        close_connection(conn, c)
        for row in rows:
            cat.add_categorie(Categorie(row[0], row[1]))
        return cat

    def add_categorie(self, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_add, (name,))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def replace(self, id, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_replace, (id, name))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def delete(self, id):
        conn, c = create_connection()
        c.execute(self.sql_delete, (id,))
        rows = c.fetchall()
        close_connection(conn, c)
