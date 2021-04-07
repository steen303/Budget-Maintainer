import logging
from mysql.connector import Error

from db.database import create_connection, close_connection
from db.db_categorie import DbCategorie
from domain.income import Income, IncomeList
from domain.categorie import Categorie
from db.db_contact import DbContact
from domain.contact import Contact


# TODO change to income table



class DbIncome:
    sql_get = "SELECT * FROM income WHERE transaction_id = %d"
    sql_get_all = "SELECT * FROM income"
    sql_get_by_month = "SELECT * FROM income WHERE year = %s AND month = %s"
    sql_add = "INSERT INTO income (year, month, day, description, value, categorie, from_who) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql_replace = "REPLACE INTO contact (name) VALUES (%s)"  # TODO update
    sql_delete = "DELETE FROM contact WHERE name = %s"  # TODO update

    def get_by_id(self, id):
        conn, c = create_connection()
        c.execute(self.sql_get, id)
        rows = c.fetchall()
        close_connection(conn, c)
        contact = Contact(rows[0][7])
        dbCat = DbCategorie()
        categorie = dbCat.get_by_id(rows[0][6])
        return Income(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], categorie, contact)

    def get_all(self): # TODO refacter: duplicate code
        conn, c = create_connection()
        c.execute(self.sql_get_all)
        inc = IncomeList()
        rows = c.fetchall()
        close_connection(conn, c)
        for row in rows:
            contact = Contact(row[7])
            dbCat = DbCategorie()
            categorie = dbCat.get_by_id(row[6])
            income = Income(row[0], row[1], row[2],
                            row[3], row[4], row[5], categorie, contact)
            inc.add_income(income)
        return inc

    def get_by_month(self, year, month):
        conn, c = create_connection()
        c.execute(self.sql_get_by_month, (year, month))
        inc = IncomeList()
        rows = c.fetchall()
        close_connection(conn, c)
        for row in rows:
            contact = Contact(row[7])
            dbCat = DbCategorie()
            categorie = dbCat.get_by_id(row[6])
            income = Income(row[0], row[1], row[2],
                            row[3], row[4], row[5], categorie, contact)
            inc.add_income(income)
        return inc

    def add_income(self, year, month, day, description, value, categorie_name, from_who_name):
        try:
            conn, c = create_connection()
            categorie = self.create_categorie(categorie_name)
            dbCont = DbContact()
            dbCont.replace(from_who_name)
            c.execute(self.sql_add, (year, month, day, description, value, categorie.id, from_who_name))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def replace(self, id, name):  # TODO update for income table
        try:
            conn, c = create_connection()
            c.execute(self.sql_replace, (id, name))
            conn.commit()
        except Error as error:
            logging.error(error)
        finally:
            close_connection(conn, c)

    def delete(self, id):  # TODO update for income table
        conn, c = create_connection()
        c.execute(self.sql_delete, id)
        rows = c.fetchall()
        close_connection(conn, c)

    def create_categorie(self, categorie_name):
        dbCat = DbCategorie()
        if dbCat.get_by_name(categorie_name) is None:
            dbCat.add_categorie(categorie_name)
        return dbCat.get_by_name(categorie_name)
