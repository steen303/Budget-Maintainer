from domain.income_expense import IncomeExpense


class Expense(IncomeExpense):
    def __init__(self, id, year, month, day, description, value, categorie, from_who):
        super().__init__(id, year, month, day, description, value, categorie, from_who)


class ExpenseList:
    def __init__(self, expense_list=None):
        if expense_list is None:
            expense_list = []
        self.expense_list = expense_list

    def __sizeof__(self) -> int:
        return len(self.expense_list)

    def add_income(self, income):
        self.expense_list.append(income)

    def get_json(self):
        json_output = []
        for expense in self.expense_list:
            json_output.append(expense.get_json())
        return json_output
