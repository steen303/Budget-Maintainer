from domain.categorie import Categorie
from domain.contact import Contact
from domain.income_expense import IncomeExpense


class Income(IncomeExpense):
    def __init__(self, id, year, month, day, description, value, categorie, from_who):
        super().__init__(id, year, month, day, description, value, categorie, from_who)


class IncomeList:
    def __init__(self, income_list=None):
        if income_list is None:
            income_list = []
        self.income_list = income_list

    def __sizeof__(self) -> int:
        return len(self.income_list)

    def add_income(self, income):
        self.income_list.append(income)

    def get_json(self):
        json_output = []
        for income in self.income_list:
            json_output.append(income.get_json())
        return json_output
