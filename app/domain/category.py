class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "ID:" + self.id + ", " + self.name

    def __repr__(self) -> str:
        return "Category(%s, %s)" % (self.id, self.name)

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.name == other.name
        else:
            return False

    def get_json(self):
        return {"id": self.id, "name": self.name}


class Categories:
    def __init__(self, categories=None):
        if categories is None:
            categories = []
        self.categories = categories

    def __sizeof__(self) -> int:
        return len(self.categories)

    def add_categorie(self, categorie):
        self.categories.append(categorie)

    def get_categories_json(self):
        json_output = []
        for categorie in self.categories:
            json_output.append(categorie.get_json())
        return json_output
