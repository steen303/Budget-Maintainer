import logging
from mysql.connector import Error

from db.database import create_connection, close_connection, get_boolean
from db.db_categorie import DbCategory
from domain.transaction import Transaction, TransactionList
from db.db_contact import DbContact
from domain.contact import Contact


def create_categorie(categorie_name):
    db_cat = DbCategory()
    if db_cat.get_by_name(categorie_name) is None:
        db_cat.add_category(categorie_name)
    return db_cat.get_by_name(categorie_name)


class DbTransaction:
    sql_get = "SELECT * FROM transactions WHERE transaction_id = %d"
    sql_get_all_income = "SELECT * FROM transactions WHERE is_expense = 0"
    sql_get_all_expense = "SELECT * FROM transactions WHERE is_expense = 1"
    sql_get_by_month = "SELECT * FROM transactions WHERE year = %s AND month = %s AND is_expense = %s ORDER BY day ASC"
    sql_add = "INSERT INTO transactions (year, month, day, description, value, categorie, contact, is_expense) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    sql_replace = "REPLACE INTO transactions (transaction_id, year, month, day, description, value, categorie, \
                                     contact, is_expense) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_delete = "DELETE FROM transactions WHERE transaction_id = %s"

    @staticmethod
    def sql_rows_to_transactions(rows):  # TODO can be static
        transaction_list = TransactionList()
        for row in rows:
            contact = Contact(row[7])
            db_cat = DbCategory()
            categorie = db_cat.get_by_id(row[6])
            transaction = Transaction(row[0], row[1], row[2],
                                      row[3], row[4], row[5], categorie, contact, get_boolean(row[8]))
            transaction_list.add_transaction(transaction)
        return transaction_list

    def get_by_id(self, transaction_id):  # TODO add try catch
        conn, c = create_connection()
        c.execute(self.sql_get, transaction_id)
        rows = c.fetchall()
        close_connection(conn, c)
        contact = Contact(rows[0][7])
        db_cat = DbCategory()
        categorie = db_cat.get_by_id(rows[0][6])

        return Transaction(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], categorie, contact,
                           get_boolean(rows[0][8]))

    def get_all(self, is_expense):
        transaction_list = TransactionList()
        try:
            conn, c = create_connection()
            if is_expense is False or is_expense is None:
                c.execute(self.sql_get_all_income)
            else:
                c.execute(self.sql_get_all_expense)
            rows = c.fetchall()
            close_connection(conn, c)
            transaction_list = self.sql_rows_to_transactions(rows)
        except Error as error:
            logging.error("Can't get transaction: " + str(error))
        return transaction_list

    def get_all_income(self):
        return self.get_all(False)

    def get_all_expense(self):
        return self.get_all(True)

    def get_by_month(self, year, month, is_expense=False):  # TODO add try catch
        conn, c = create_connection()
        c.execute(self.sql_get_by_month, (year, month, int(is_expense)))
        rows = c.fetchall()
        close_connection(conn, c)
        return self.sql_rows_to_transactions(rows)

    def add_transaction(self, year, month, day, description, value, categorie_name, contact, is_expense):
        print("Add transaction")
        try:
            conn, c = create_connection()
            categorie = create_categorie(categorie_name)
            db_cont = DbContact()
            db_cont.replace(contact)
            c.execute(self.sql_add, (year, month, day, description, value, categorie.id,
                                     contact, int(is_expense)))
            conn.commit()
            close_connection(conn, c)
        except Error as error:
            logging.error("Can't add transaction: " + str(error))

    def add_income(self, year, month, day, description, value, categorie_name, from_who):
        print("add_income")
        self.add_transaction(year, month, day, description, value, categorie_name, from_who, "0")

    def add_expense(self, year, month, day, description, value, categorie_name, to_who):
        self.add_transaction(year, month, day, description, value, categorie_name, to_who, "1")

    def replace(self, transaction_id, year, month, day, description, value, categorie_name, contact,
                is_expense):  # TODO update for income table
        try:
            conn, c = create_connection()
            categorie = create_categorie(categorie_name)
            db_cont = DbContact()
            db_cont.replace(contact)
            c.execute(self.sql_replace, (transaction_id, year, month, day, description, value, categorie.id,
                                         contact, int(is_expense)))
            conn.commit()
            close_connection(conn, c)
        except Error as error:
            logging.error("Can't replace transaction: " + str(error))

    def delete(self, categorie_id):  # TODO update for income table
        try:
            conn, c = create_connection()
            c.execute(self.sql_delete, categorie_id)
            close_connection(conn, c)
        except Error as error:
            logging.error("Can't delete transaction: " + str(error))
