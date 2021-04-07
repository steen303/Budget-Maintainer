import logging
from mysql.connector import Error

from db.database import create_connection, close_connection
from domain.contact import Contact, Contacts


class DbContact:
    sql_get = "SELECT * FROM contact WHERE name = %s"
    sql_get_all = "SELECT * FROM contact"
    sql_add = "INSERT INTO contact (name) VALUES (%s)"
    sql_replace = "REPLACE INTO contact (name) VALUES (%s)"
    sql_delete = "DELETE FROM contact WHERE name = %s"

    def get_by_name(self, name):
        conn, c = create_connection()
        c.execute(self.sql_get, (name,))
        rows = c.fetchall()
        close_connection(conn, c)
        return Contact(rows[0][0])

    def get_all(self):
        conn, c = create_connection()
        c.execute(self.sql_get_all)
        contacts = Contacts()
        rows = c.fetchall()
        close_connection(conn, c)
        for row in rows:
            contacts.add_contact(Contact(row[0]))
        return contacts

    def add_contact(self, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_add, (name,))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def replace(self, name):
        try:
            conn, c = create_connection()
            c.execute(self.sql_replace, (name,))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def delete(self, id):
        conn, c = create_connection()
        c.execute(self.sql_delete, id)
        rows = c.fetchall()
        close_connection(conn, c)
