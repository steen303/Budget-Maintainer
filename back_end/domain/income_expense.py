class IncomeExpense:
    def __init__(self, id, year, month, day, description, value, categorie, from_who):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.description = description
        self.value = value
        self.categorie = categorie
        self.contact = from_who

    def get_json(self):
        return {"name": str(self.id),
                "year": str(self.year),
                "month": str(self.month),
                "day": str(self.day),
                "description": self.description,
                "value": str(self.value),
                "categorie": self.categorie.get_json(),
                "contact": self.contact.name}
