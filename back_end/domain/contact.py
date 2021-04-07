class Contact:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "name:" + self.name

    def __repr__(self) -> str:
        return "contact(%s)" % self.name

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False


class Contacts:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []
        self.contacts = contacts

    def __sizeof__(self) -> int:
        return len(self.contacts)

    def add_contact(self, categorie):
        self.contacts.append(categorie)

    def get_contacts_json(self):
        json_output = []
        for contact in self.contacts:
            json_output.append(contact.name)
        return json_output
