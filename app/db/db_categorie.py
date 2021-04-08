import logging
from mysql.connector import Error

from db.database import create_connection, close_connection
from domain.category import Category, Categories


class DbCategory:
    sql_get_by_id = """SELECT * FROM category WHERE id = %s"""
    sql_get_by_name = "SELECT * FROM category WHERE name = %s"
    sql_get_all = "SELECT * FROM category ORDER BY name"
    sql_add = "INSERT INTO category (name) VALUES (%s)"
    sql_replace = "REPLACE INTO category (id, name) VALUES (%s, %s)"
    sql_delete = "DELETE FROM category WHERE name = %d"

    def get_by_id(self, categorie_id):
        conn, c = create_connection()
        c.execute(self.sql_get_by_id, (categorie_id,))
        rows = c.fetchall()
        close_connection(conn, c)
        return Category(rows[0][0], rows[0][1])

    def get_by_name(self, name):
        conn, c = create_connection()
        c.execute(self.sql_get_by_name, (name,))
        rows = c.fetchall()
        close_connection(conn, c)
        if len(rows) > 0:
            return Category(rows[0][0], rows[0][1])
        else:
            return None

    def get_all(self):
        conn, c = create_connection()
        c.execute(self.sql_get_all)
        cat = Categories()
        rows = c.fetchall()
        close_connection(conn, c)
        for row in rows:
            cat.add_categorie(Category(row[0], row[1]))
        return cat

    def add_category(self, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_add, (name,))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def replace(self, category_id, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_replace, (category_id, name))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def delete(self, category_id):
        conn, c = create_connection()
        c.execute(self.sql_delete, (category_id,))
        rows = c.fetchall()
        close_connection(conn, c)
