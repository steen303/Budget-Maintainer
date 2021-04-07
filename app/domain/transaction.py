# TODO implement this class to avoid duplicate code in income.py and expense.py


class Transaction:

    def __init__(self, transaction_id, year, month: object, day, description, value, categorie, from_who, is_expense=False):
        """

        :type day: int
        """
        self.id = transaction_id
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.description = description
        self.value = float(value)
        self.categorie = categorie
        self.contact = from_who
        self.is_expense = bool(is_expense)

    def get_json(self):
        return {"name": str(self.transaction_id),
                "year": str(self.year),
                "month": str(self.month),
                "day": str(self.day),
                "description": self.description,
                "value": str(self.value),
                "categorie": self.categorie.get_json(),
                "contact": self.contact.name,
                "is_expense": self.is_expense
                }


class TansactionList:
    def __init__(self, transaction_list=None):
        if transaction_list is None:
            transaction_list = []
        self.transaction_list = transaction_list

    def __sizeof__(self) -> int:
        return len(self.transaction_list)

    def add_transaction(self, income):
        self.transaction_list.append(income)

    def sum(self):
        sum = 0
        for transaction in self.transaction_list:
            sum += transaction.value
        return sum

    def average(self):
        sum = 0
        for transaction in self.transaction_list:
            sum += transaction.value
        return sum / len(self.transaction_list)

    def min(self):
        min_value = self.transaction_list[0].value
        for transaction in self.transaction_list:
            if transaction.value < min_value:
                min_value = transaction.value
        return min_value

    def max(self):
        max_value = self.transaction_list[0].value
        for transaction in self.transaction_list:
            if transaction.value < max_value:
                max_value = transaction.value
        return max_value

    def get_json(self):
        json_output = []
        for transaction in self.transaction_list:
            json_output.append(transaction.get_json())
        return json_output
